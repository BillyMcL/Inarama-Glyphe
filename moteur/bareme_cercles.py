"""Barème par cercles : le coût d'une forme lu sur son glyphe, cercle par cercle (décisions du 23 novembre 2026, « validé pour
l'instant, affiné à la fin »). Aucune construction du site ne l'appelle.

Sources : les lots du barème (Claude outputs/phase4 : lots 1 à 7, I1, I2, I3, I6, I7-I12) et donnees/bareme/bareme_tables
(échelles d'états, prix fixes des outils), lus pour les prix décidés ; les prix provisoires et les relations sont marqués.

    analyse(forme)          -> les mesures lues sur le glyphe et le prix de chaque cercle (sans les relations)
    palier(analyse, coefs)  -> le coût et le palier, avec les coefficients des relations réglés (regles_systeme ; outils/mesure_bareme_cercles_v5.py)

Prix décidés (points de départ) : Localisation (lot 1), rabais d'incantation (lot 2), Condition (lot 3 : parole, concentration,
officiants), Composante (lot 4), Cosmétique (lot 6), blessures (I1), soins (I2), êtres appelés (I6).
Provisoires : états et genres voisins (échelles de bareme_tables), outils et déplacements (prix fixes), garde (échelle I3),
plusieurs effets (règle 2.3 de l'ancien barème).
Relations réglées sur les niveaux de la source, système par système (décision du 24 novembre, version B) : b (durée) réglé une
fois par système sur tous les genres ; a (cibles) et c (restriction) réglés genre par genre avec ce b fixé (regles_systeme) :
    palier ≈ prix de l'effet + a × log2(cibles) + b × marche de durée + c × restriction + prix décidés
Effets uniques (aucun prix ici, prix propre par cercle déduit des niveaux) : cercles sans règle, absorption, puissance « pleine ».
"""
import math, re
import bareme as B          # échelles et tables du barème du 22 novembre (prix_degre, MOT_ECHELLE, OUTIL…)
import lexique as LX

PALIER_MAX = 10


def _num(v): return isinstance(v, (int, float)) and not isinstance(v, bool)


def cle_cercle(r):
    """l'identité d'un cercle, comme le répertoire : type, valeur, mots dans l'ordre, satellites (position, valeur, texte, options)"""
    import json
    jv = lambda x: json.loads(json.dumps(x, ensure_ascii=False, default=repr))
    sats = tuple(json.dumps(jv([s[0], s[1], s[2] if len(s) > 2 else None, dict(sorted((s[3] if len(s) > 3 and s[3] else {}).items()))]),
                            ensure_ascii=False) for s in (r[4] if len(r) > 4 and r[4] else []))
    return (r[0], json.dumps(jv(r[1]), ensure_ascii=False), tuple(r[2]), sats)


def combiner(prix, sugg=False):
    """plusieurs effets (règle 2.3, provisoire) : le plus cher entier, les autres en part"""
    if not prix: return 0.0
    ps = sorted(prix, reverse=True); g = ps[0]
    part = 0.5 if g < 3 else 0.25 if g < 6 else 0.1
    return g + part * sum(max(x, 0) for x in ps[1:]) - (1 if sugg else 0)
def _sats(r): return list(r[4]) if len(r) > 4 and r[4] else []
def _txt(s): return s[2] if len(s) > 2 and isinstance(s[2], str) else ""
def _sym(v): return isinstance(v, (tuple, list)) and len(v) == 2 and v[0] == "sym"


def interp_log(x, points):
    """interpolation « à proportion sur une échelle de rapports » (logarithmique) entre les deux paliers qui encadrent x ;
    bornée au premier et au dernier palier"""
    if x <= points[0][0]: return points[0][1]
    for (x1, p1), (x2, p2) in zip(points, points[1:]):
        if x <= x2: return p1 + (p2 - p1) * math.log(x / x1) / math.log(x2 / x1)
    return points[-1][1]


# ---------------------------------------------------------------- lot 1 : Localisation (ajout, prix décidé)
LOCALISATION = [(3, 0.10), (9, 0.25), (18, 0.30), (27, 0.33), (36, 0.36), (45, 0.40), (90, 0.50), (150, 0.60), (300, 0.75),
                (1600, 1.00), (8000, 1.50), (160000, 2.00), (800000, 2.50)]
def prix_localisation(r):
    if r is None: return 0.0, "pas de Localisation (soi) : 0"
    if r[1] == "plein": return 3.0, "lot 1 : illimitée 3,00"
    if set(r[2]) & {"AVENIR", "PASSE"}: return 0.0, "lot 1 : Localisation dans le temps, sans prix (lacune)"
    m = r[1] * (1000 if "KILOMETRES" in r[2] else 1)
    if m <= 2: return 0.0, "lot 1 : contact 0"
    if m < 3: return 0.0, "lot 1 : sous 3 m, 0"
    return round(interp_log(m, LOCALISATION), 3), f"lot 1 : {m:g} m"


# ---------------------------------------------------------------- lot 2 : Durée (marche, mesure) et incantation (rabais décidé)
UNITES = {"SECONDES": 1, "MINUTES": 60, "HEURES": 3600, "JOURS": 86400, "ANS": 31536000}
MARCHES = [(6, 1), (60, 2), (600, 3), (3600, 4), (28800, 5), (86400, 6), (604800, 7), (31536000, 8)]
INCANTATION = [(6, 0.10), (60, 0.50), (600, 0.75), (3600, 1.00), (28800, 1.25), (43200, 1.35), (86400, 1.50), (604800, 2.00)]
def duree(rings):
    """(secondes de l'effet ou None si permanent, permanent, secondes d'incantation)"""
    r = next((x for x in rings if x[0] == "DUREE"), None)
    if r is None: return 0.0, False, 0.0
    us = [w for w in r[2] if w in UNITES]
    st = [s for s in _sats(r) if not _txt(s) and not _sym(s[1]) and (s[0] == "NS" or len(_sats(r)) == 1)]
    if st:                                      # incantation sur le cercle, durée de l'effet en satellite nord-sud
        cast = r[1] * UNITES[us[0]] if _num(r[1]) and us else 0.0
        dv = st[0][1]
        if dv == "plein": return None, True, cast
        u = us[1] if len(us) > 1 else (us[0] if us else "SECONDES")
        return float(dv) * UNITES[u], False, cast
    if r[1] == "plein": return None, True, 0.0
    if _num(r[1]) and us: return float(r[1]) * UNITES[us[0]], False, 0.0
    return 0.0, False, 0.0


def marche(sec, perm):
    if perm: return 9.0
    if not sec: return 0.0
    if sec < 6: return sec / 6                  # sous le round : à proportion du round
    return min(8.0, interp_log(sec, MARCHES)) if sec <= 31536000 else 8.0


def rabais_incantation(cast):
    if cast < 6: return 0.0
    return round(interp_log(cast, INCANTATION), 3)


# ---------------------------------------------------------------- lot 3 : Condition (rabais décidés)
OFFICIANTS = {1: 0.25, 2: 0.35, 3: 0.43, 4: 0.50, 5: 0.55, 6: 0.60}
FAMILLE2 = set("VIVANT COMPAGNON MORTVIVANT BETE PEUPLE HOSTILE TENEBREUX LUMINEUX INVOQUE ESPECE PLANTE DRAGON CADAVRE MINUSCULE PAIR ALLIE "
               "MONTURE FOULE EQUIPAGE GRAND MONSTRE PROIE SEMBLABLE SERVITEUR INSTINCT PARENTE SOUFFLE SANG".split())
def rabais_condition(rings):
    out, det = 0.0, []
    for r in rings:
        if r[0] != "CONDITION": continue
        if "PAROLE" in r[2]: out += 0.10; det.append("parole 0,10")
        if "CONCENTRATION" in r[2]: out += 0.50; det.append("concentration 0,50")
        if "OFFICIANT" in r[2]:
            n = [s[1] for s in _sats(r) if _num(s[1]) and _txt(s) in ("", "OFFICIANT")]
            if n:
                x = OFFICIANTS.get(int(n[0]), 0.60 if n[0] > 6 else 0.0); out += x; det.append(f"{n[0]} officiant(s) {x:.2f}")
    return out, det


# ---------------------------------------------------------------- lot 4 : Composante (rabais décidé)
COMPOSANTE = [(0.1, 0.05), (1, 0.15), (2.5, 0.20), (5, 0.30), (10, 0.40), (25, 0.55), (50, 0.70), (100, 0.85), (250, 1.00), (500, 1.20),
              (1000, 1.40), (2500, 1.60)]
def rabais_composante(rings):
    out, det, ouverts = 0.0, [], []
    for r in rings:
        if r[0] != "COMPOSANTE": continue
        if r[2][:1] in (["CONTREPARTIE"], ["VIE"], ["GARDE"]):
            ouverts.append(" · ".join(r[2]).lower()); continue
        if not _num(r[1]): continue                         # matériel sans valeur : 0
        mon = "PLATINE" if "PLATINE" in r[2] else "OR" if "OR" in r[2] else "ARGENT" if "ARGENT" in r[2] else None
        if mon is None: continue
        v = r[1] * {"PLATINE": 1, "OR": 0.1, "ARGENT": 0.01}[mon]
        for s in _sats(r):
            if _txt(s) == "FOIS" and _num(s[1]): v *= s[1]
        x = interp_log(v, COMPOSANTE) if v >= 0.1 else 0.05 * v / 0.1
        tenu = "CONSOMME" not in r[2]
        if tenu: x /= 2
        out += x; det.append(f"{v:g} platine{' tenu (moitié)' if tenu else ''} {x:.2f}")
    return out, det, ouverts


# ---------------------------------------------------------------- cibles (lot 5) et zones (lot 1)
SUPPORTS = {"COUP", "RESISTANCE", "APTITUDE", "FRAPPE", "GARDE", "PRESTANCE", "RAISON", "LUCIDITE", "ENDURANCE", "ADRESSE", "FORCE"}
FAMILLE_D = set("BETE ELEMENTAIRE PLANTE FEE INVOQUE CADAVRE MONTURE SERVITEUR MORTVIVANT DRAGON DIVINITE PETIT COMPAGNON VERMINE INSECTE NUEE "
                "ANCETRE ARAIGNEE MOLOSSE CHEVAL ETRE GOULE CREATURE MILLEPATTES GOLEM MORT GENIE GUEPE VIVANT SERPENT HOSTILE VER EQUIPAGE AIGLE "
                "AUROCHS FOULE GRENOUILLE MONSTRE SINGE PASSAGER FOURMI ALLIE CORBEAU GEANT LOUP SAVANT LUMINEUX CHAUVESOURIS RAT SQUELETTE "
                "TENEBREUX MAMMOUTH".split())
FIGURES = {("plein", 1): "sphère", (4, 1): "cube", (3, 2): "cône", (1, 1): "ligne", (9, 2): "cylindre"}    # (valeur de la Forme, satellites de proportion)
DIVISEUR = {"sphère": 5, "cylindre": 5, "cube": 5, "cône": 10, "ligne": 30}
def _m3(a):
    v, ws = a[1], list(a[2])
    if not _num(v): return None, None
    if ws[:1] == ["VOLUME"] or ws[-1:] == ["CUBES"]:
        return v * {"METRES": 1, "DECAMETRES": 1e3, "HECTOMETRES": 1e6, "KILOMETRES": 1e9}.get(next((w for w in ws if w in ("METRES", "DECAMETRES", "HECTOMETRES", "KILOMETRES")), "METRES"), 1), "volume"
    if ws[:1] == ["LONGUEUR"]: return v * (1000 if "KILOMETRES" in ws else 1), "longueur"
    return None, None


def cibles_zone(rings):
    """(nombre de cibles de la zone, explication) ; None si la mesure manque (figure à part, zone sans taille)"""
    f = next((r for r in rings if r[0] == "FORME"), None)
    cible_zone = any(r[0] == "CIBLE" and r[1] == "plein" for r in rings)
    if f is None and not cible_zone: return None, None
    if f is None: return None, "zone sans Forme ni taille"
    sats_f = _sats(f)
    fig = FIGURES.get((f[1], len([s for s in sats_f if not _txt(s) and not _sym(s[1])])))
    if set(f[2]) & {"EXPLOSION", "PONT"} or fig is None:
        return None, f"figure à part ({' · '.join(f[2]).lower() or f[1]})"
    a = next((r for r in rings if r[0] == "AMPLEUR"), None)
    taille = _m3(a) if a else (None, None)
    if taille[0] is None:
        sa = [s for s in sats_f if _txt(s).startswith("AMPLEUR")]
        if sa and _num(sa[0][1]):
            taille = _m3(("AMPLEUR", sa[0][1], _txt(sa[0]).split()[1:]))
    v, sorte = taille
    if v is None: return None, f"zone sans taille ({fig})"
    if sorte == "longueur": dim = v
    elif fig == "sphère": dim = (3 * v / (4 * math.pi)) ** (1 / 3)
    elif fig == "cube": dim = v ** (1 / 3)
    elif fig == "cylindre": dim = (v / (2 * math.pi)) ** (1 / 3)
    elif fig == "cône": dim = (12 * v / math.pi) ** (1 / 3)
    else: dim = v                                  # une ligne écrite en volume : rare
    pieds = max(5, 5 * round(dim / 0.3048 / 5))
    n = max(1, math.ceil(pieds / DIVISEUR[fig]))
    return n, f"{fig} de {pieds} pieds → {n} cibles"


def nombre_cibles(rings):
    c = next((r for r in rings if r[0] == "CIBLE"), None)
    q = [s[1] for s in (_sats(c) if c else []) if not _txt(s) and not _sym(s[1]) and (_num(s[1]) or s[1] == "plein")]
    if q:
        if q[0] == "plein": return 10, "Quantité pleine (« tous ceux que je choisis ») lue 10", False
        return int(q[0]), f"Quantité {q[0]} sur la Cible", False
    n, why = cibles_zone(rings)
    if n is not None: return n, "zone : " + why, True
    if why: return 1, "mesure absente : " + why, True
    return 1, "une cible", False


def restriction(rings):
    # une Cible « un être qui relève d'un plan » (valeur 9) : ses mots et son pôle disent QUEL être est appelé, jamais une
    # restriction (décision du 23 novembre) : la forme n'a pas de restriction
    if any(r[0] == "CIBLE" and r[1] == 9 for r in rings): return []
    out = []
    for r in rings:
        if r[0] == "CONDITION": out += [w for w in r[2] if w in FAMILLE2]
        if r[0] == "CIBLE":
            out += [{"lumineux": "LUMINEUX", "tenebreux": "TENEBREUX"}[s[1][1]] + " (pôle)" for s in _sats(r) if _sym(s[1]) and s[1][1] in ("lumineux", "tenebreux")]
            if r[1] not in (1, None): out += [w for w in r[2] if w in FAMILLE_D]
    return sorted(set(out))


# ---------------------------------------------------------------- les effets (cercles d'Impact)
BLESSURE = {"CHOC", "PERCE", "TRANCHANT", "FRACAS", "VENIN", "SAIGNEMENT", "DOULEUR", "IMPARABLE"}
DEGATS = {"une": [5.5, 11, 16.5, 27.5, 33, 38.5, 55, 60.5, 66, 82.5], "plusieurs": [3.5, 7, 10.5, 21, 24.5, 28, 38.5, 42, 45.5, 49]}
GARDE = {1: 1.2, 2: 1.6, 3: 1.9, 4: 2.25, 5: 2.6, 6: 2.95}
GRANDE_FAMILLE = {"sens": "sens", "savoir": "savoir", "être vu": "caché", "matière": "caché", "paraître": "caché", "forme": "caché",
                  "illusion": "caché", "peur": "esprit", "attitude": "esprit", "conduite": "esprit", "conscience": "esprit", "oubli": "esprit"}
def palier_degats(m, col):
    t = DEGATS[col]
    if m <= t[0]: return max(0.0, (m - t[0]) / (t[1] - t[0]))
    for i in range(9):
        if m <= t[i + 1]: return i + (m - t[i]) / (t[i + 1] - t[i])
    return min(float(PALIER_MAX), 9 + (m - t[9]) / (t[9] - t[8]))


# v7 (25 novembre) : la protection reprend l'échelle DÉCIDÉE de la garde (lot I3) ; le seuil prend la même échelle (provisoire) ;
# les autres mécaniques sont réglées par la mesure (a × degré, ou prix fixe)
MECAS = {"RENFORT": "renfort", "FAIBLESSE": "faiblesse", "CHANCE": "chance", "MALCHANCE": "malchance", "MESURE": "mesure",
         "SURCROIT": "surcroît"}


COUPS = {"CHOC", "PERCE", "TRANCHANT", "FRACAS", "VENIN"}


def une_sorte(r):
    """v8 : l'effet ne vaut que contre UNE sorte (le nom de cette sorte), sinon None : un symbole d'élément (un ou plusieurs symboles
    qui forment un seul élément), un symbole de face astrale, un mot de sorte de coup, ou, pour une forme hybride, l'élément de son
    Noyau quand le glyphe ne le redit pas (la phrase « … est dite par le noyau »)"""
    ss = _sats(r); sortes = []
    if any(_sym(s_[1]) and s_[1][1] in ("feu", "air", "terre", "eau") for s_ in ss): sortes.append("élément")
    sortes += [s_[1][1] for s_ in ss if _sym(s_[1]) and s_[1][1] in ("lumineux", "tenebreux")]
    sortes += [w.lower() for w in r[2] if w in COUPS]
    m = re.search(r"\(« ([^»]+) »\) est dite par le noyau", r[3] or "")
    if m and not sortes: sortes.append(m.group(1))
    return sortes[0] if len(sortes) == 1 else None


def effet(r, ctx):
    """(prix, genre, famille, rôle, règle) d'un cercle d'Impact ; ctx : plusieurs cibles, zone, nombre d'êtres, verbe, supports"""
    v, ws = r[1], [w for w in r[2]]
    st = _sats(r)
    repete = any(_txt(s).startswith("DUREE CHAQUE") for s in st)
    seuil_i = [s for s in st if _txt(s).split()[:1] == ["IMPACT"] and len(_txt(s).split()) > 1]
    seuil_x = [s for s in st if _txt(s).split()[:1] == ["INTERACTION"]]
    frac = next((s_[1] for s_ in st if _txt(s_).startswith("QUANTITE FRACTIONNE") and _num(s_[1]) and s_[1] > 0), None)
    if "PUISSANCE" in ws[:1] or (ws and ws[0] == "PUISSANCE"):
        if not _num(v):                          # décision du 24 novembre : un être choisi sans plafond est un effet unique
            return 3.0, "être appelé", None, None, "aucun prix : puissance pleine, effet unique (prix propre)"
        n = ctx["etres"]
        pv = v / frac if frac else v             # v6 : puissance ½ ou ¼ (satellite « fractionné »)
        return pv + math.log2(max(n, 1)), "être appelé", None, None, f"I6 : puissance {pv:g}" + (f" (= {v} fractionné {frac})" if frac else "") + f" + log2({n})"
    if ws[:1] == ["ANIMATION"] and _num(v):      # v6 : animation, n = la taille ; la règle des êtres appelés
        n = ctx["etres"] if ctx["etres"] > 1 else ctx["etres_cible"]     # le nombre : cercle de Quantité, ou Quantité de la Cible
        pv = v / frac if frac else v
        return pv + math.log2(max(n, 1)), "être appelé", None, None, f"I6 : animation {pv:g} (taille) + log2({n})"
    if ws[:1] == ["NOURRITURE"]:                 # v7 : une relation sur log2(personnes nourries), réglée par la mesure ; « plein » : prix propre
        if _num(v): return 3.0, "autre", None, None, f"mécanique:nourriture:{v} — provisoire : 3,0"
        return 3.0, "autre", None, None, f"aucun prix : nourriture {v}, effet unique (prix propre)"
    if ws[:1] == ["SEUIL"] and _num(v):          # v7 : le seuil (défense fixée) prend l'échelle de la protection, provisoire
        return GARDE.get(v, 2.95 + 0.35 * (v - 6)), "garde", "garde", "protéger", f"seuil {v} : l'échelle de la protection (provisoire, v7)"
    if ws[:1] and ws[0] in MECAS:                # v6 : mécaniques des bonus (prix réglé par la mesure : a × degré, ou prix fixe)
        m = MECAS[ws[0]]
        if _num(v):
            return B.prix_degre("facultés", v), "bonus", None, None, f"mécanique:{m}:{v} — provisoire : échelle des facultés"
        if v == "plein" and ws[0] in ("CHANCE", "MALCHANCE"):
            m = ("relance" if ws[0] == "CHANCE" else "relance au pire") if "REPETITION" in ws else ("avantage" if ws[0] == "CHANCE" else "désavantage")
            return 3.0, "bonus", None, None, f"mécanique:{m}:plein — provisoire : 3,0"
    # bonus : la Cible porte un support (coup, garde, résistance, une faculté) et l'Impact est chiffré ou de facultés
    if ctx["supports"] and _num(v) and (not ws or B.MOT_ECHELLE.get(ws[0]) == "facultés"):
        p = B.prix_degre("facultés", v)
        return p, "bonus", None, None, f"provisoire : bonus {v} sur l'échelle des facultés"
    if ws[:1] == ["VIE"] and _num(v) and ctx["verbe"].split(" · ")[0] not in LX.VERBES_NUISIBLES:
        p = -3.1 + 1.4 * math.log2(max(v, 1)) + (2 if ctx["plusieurs"] else 0)
        p = min(PALIER_MAX, max(0.0, p))
        quoi = "vie d'emprunt" if any(_txt(s) == "DUREE" and s[1] == "plein" for s in st) else "soin répété (prix ouvert)" if repete else "soin"
        return p, "soin", None, None, f"I2 : {quoi} {v} : −3,1 + 1,4 × log2" + (" + 2 (plusieurs cibles)" if ctx["plusieurs"] else "")
    if ws[:1] == ["REMPART"] and _num(v):        # décision du 23 novembre : 1,33 + 1,33 × log2(montant), − 2,4 contre une seule sorte (v8)
        une = une_sorte(r)
        p = 1.33 + 1.33 * math.log2(max(v, 1)) - (2.4 if une else 0)
        return p, "garde", "garde", "protéger", f"rempart {v} : 1,33 + 1,33 × log2" + (f" − 2,4 (contre une seule sorte : {une})" if une else "")
    if ws[:1] == ["ABSORPTION"]:                 # décision du 23 novembre : effet unique, prix propre
        return 3.0, "garde", "garde", "protéger", "aucun prix : absorption, effet unique (prix propre)"
    if ws[:1] == ["RIPOSTE"] and _num(v):
        return B.prix_montant(v), "garde", "garde", "protéger", f"provisoire : riposte {v}, règle des montants (règle à fixer, I3)"
    garde = [w for w in ws if B.MOT_ECHELLE.get(w) == "garde"]
    if garde:
        w = garde[0]
        if v == "plein" and w in ("IMMUNITE", "BARRIERE", "PROTECTION"): p = 4.0
        elif w == "RESISTANCE": p = 2.6
        elif w == "PROTECTION" and _num(v): p = GARDE.get(v, 2.95 + 0.35 * (v - 6))
        else: p = B.prix_degre("garde", v if (_num(v) or v == "plein") else "plein")
        return p, "garde", "garde", "protéger", f"I3 : {w.lower()} {v}" + ("" if w in ("PROTECTION", "RESISTANCE", "IMMUNITE", "BARRIERE") else " (hors échelle validée, provisoire)")
    if _num(v) and (not ws or ws[0] in BLESSURE or ws[0] in B.MONTANT or ws[0] not in B.DEGRES) and not [w for w in ws if B.MOT_ECHELLE.get(w) or w in B.OUTIL]:
        m = v * (1.5 if repete else 1)
        col = "plusieurs" if ctx["plusieurs"] else "une"
        if not ctx["zone"] and ctx["instances"] > 1: m *= ctx["instances"]
        p = palier_degats(m, col)
        return p, "blessure", None, None, (f"I1 : montant {v}" + (" × 1,5 (répétée)" if repete else "") + (f" × {ctx['instances']} (Quantité)" if not ctx["zone"] and ctx["instances"] > 1 else "")
                                          + f", colonne « {'plusieurs cibles' if col == 'plusieurs' else 'une cible'} »")
    role = "lever" if seuil_i else "protéger" if set(ws) & {"LIBERTE", "CONTRE", "IMMUNITE", "PROTECTION"} else "infliger"
    if seuil_x and not seuil_i:
        x = seuil_x[0][1]
        return (9.0 if not _num(x) else float(max(0, x - 1))), "état", "dissipation", "lever", "provisoire : seuil en Interaction (dissiper jusqu'au palier)"
    if seuil_i:
        p, _k, rg, *_ = B.prix_impact(r)
        fam = B._echelle_mot(_txt(seuil_i[0]).split()[1], ws) or "autre"
        return p, genre_echelle(fam), fam, "lever", "provisoire : " + rg
    cands = []
    for w in ws:
        e = B._echelle_mot(w, ws)
        if e: cands.append((B.prix_degre(e, v if (_num(v) or v == "plein") else "plein") * (1.5 if w == "CHANCE" else 1), e, w))
    if cands:
        p, e, w = max(cands)
        return p, genre_echelle(e), e, role, f"provisoire : état « {w.lower()} » {v} sur l'échelle {e}"
    outils = [(B.OUTIL[w], w) for w in ws if w in B.OUTIL]
    if outils:
        p, w = max(outils)
        return float(p), "outil ou déplacement", None, None, f"provisoire : prix fixe de « {w.lower()} »"
    if "SOUHAIT" in ws: return 9.0, "autre", None, None, "provisoire : souhait"
    return 3.0, "autre", None, None, "aucun prix : défaut 3,0 (" + (" · ".join(ws).lower() or "sans mot") + ")"


def genre_echelle(e):
    if e == "savoir": return "savoir"
    if e == "création": return "création"
    if e == "illusion": return "illusion"
    if e in ("mort", "retour"): return "mort ou retour"
    if e == "garde": return "garde"
    return "état"


# ---------------------------------------------------------------- analyse d'une forme
def sursaut(rings):
    """v6 : la nouvelle chance (« fin : chaque · … · sursaut »), sur la Durée ou en satellite de Durée d'un Impact"""
    for r in rings:
        if r[0] == "DUREE" and "SURSAUT" in r[2]: return True
        if r[0] == "IMPACT" and any(_txt(s_).startswith("DUREE") and "SURSAUT" in _txt(s_).split() for s_ in _sats(r)): return True
    return False


UNITE_BASE = {("VOLUME", "METRES", "CUBES"): 1, ("VOLUME", "DECAMETRES", "CUBES"): 1e3, ("VOLUME", "HECTOMETRES", "CUBES"): 1e6,
              ("VOLUME", "KILOMETRES", "CUBES"): 1e9, ("SURFACE", "METRES"): 1, ("LONGUEUR", "METRES"): 1, ("LONGUEUR", "KILOMETRES"): 1e3,
              ("DIAMETRE", "METRES"): 1, ("HAUTEUR", "METRES"): 1}


def figure_a_part(rings):
    """v6 : (figure, log2 de sa taille écrite, taille) d'une figure à part — chacune pour elle-même, aucun regroupement ; None sinon.
    Figures : explosion, pont, dôme (calotte), disque, mur et paroi (Forme 2 dite mur, muret, rempart, panneaux, paroi), figure 2
    (les autres plans), figure 9 (un cylindre à trois satellites), « plein » (une sphère à deux satellites), hélice."""
    f = next((r for r in rings if r[0] == "FORME"), None)
    if f is None: return None
    sats_f = _sats(f)
    prop = len([s_ for s_ in sats_f if not _txt(s_) and not _sym(s_[1])])
    if FIGURES.get((f[1], prop)) and not set(f[2]) & {"EXPLOSION", "PONT"} and len(sats_f) == prop: return None
    rd = f[3].lower()
    if "EXPLOSION" in f[2]: fig = "explosion"
    elif "PONT" in f[2] or "pont" in rd: fig = "pont"
    elif rd.startswith("calotte"): fig = "dôme"
    elif "hélice" in rd: fig = "hélice"
    elif f[1] == 9 and rd.startswith("disque"): fig = "disque"
    elif f[1] == 2 and re.search(r"mur|paroi|rempart|panneau", rd): fig = "mur et paroi"
    elif f[1] == 2: fig = "figure 2"
    elif f[1] == 9: fig = "figure 9"
    elif f[1] == "plein": fig = "plein"
    else: fig = f"figure {f[1]}"
    a = next((r for r in rings if r[0] == "AMPLEUR"), None)
    v, u = (a[1], tuple(a[2])) if a else (None, None)
    if v is None:
        sa = [s_ for s_ in sats_f if _txt(s_).startswith("AMPLEUR")]
        if sa: v, u = sa[0][1], tuple(_txt(sa[0]).split()[1:])
    if not _num(v) or u not in UNITE_BASE: return (fig, None, None)
    t = v * UNITE_BASE[u]
    return (fig, round(math.log2(max(t, 1)), 4), t)


def analyse(f):
    rings = f["rings"]
    I = [r for r in rings if r[0] == "IMPACT"]
    n_cibles, why_c, est_zone = nombre_cibles(rings)
    q = [r for r in rings if r[0] == "QUANTITE" and _num(r[1])]
    instances = int(q[0][1]) if q and not q[0][2] else 1
    c = next((r for r in rings if r[0] == "CIBLE"), None)
    ctx = dict(plusieurs=n_cibles > 1 or est_zone, zone=est_zone, instances=instances, etres=int(q[0][1]) if q else 1,
               etres_cible=n_cibles if why_c.startswith("Quantité") else 1,
               verbe=f.get("verb", ""), supports=bool(c and set(c[2]) & SUPPORTS))
    sec, perm, cast = duree(rings)
    det, lacunes = [], []
    if "mesure absente" in why_c: lacunes.append(why_c.replace("mesure absente : ", ""))
    # effets
    es = []
    etre = any(r[2][:1] == ["PUISSANCE"] for r in I)
    sugg = False
    for r in I:
        ws = set(r[2])
        if etre and ws & {"INJONCTION", "SUGGESTION", "DOMINATION"} and "PUISSANCE" not in ws:
            sugg = sugg or "SUGGESTION" in ws
            det.append(dict(cercle="IMPACT", lecture=" · ".join(r[2]).lower(), prix=0.0, regle="2.3 : comprise dans la puissance de l'être appelé")); continue
        p, g, fam, role, rg = effet(r, ctx)
        mm = re.match(r"mécanique:([^:]+):(\S+)", rg)
        gw = next((w for w in r[2] if w in ("IMMUNITE", "RESISTANCE", "BARRIERE", "PROTECTION", "REMPART")), None)
        es.append(dict(prix=p, genre=g, famille=fam, role=role, cercle=cle_cercle(r), sans_prix=rg.startswith("aucun prix"),
                       meca=mm.group(1) if mm else None, degre=(None if not mm or mm.group(2) == "plein" else float(mm.group(2))),
                       garde=gw if g == "garde" else None, une_sorte=une_sorte(r) if g == "garde" else None))
        det.append(dict(cercle="IMPACT", lecture=f"{r[1]} « {' · '.join(r[2]).lower()} »", prix=round(p, 3), regle=rg))
    if es:
        es.sort(key=lambda e: -e["prix"])
        g = es[0]["prix"]
        part = 0.5 if g < 3 else 0.25 if g < 6 else 0.1
        prix_effet = g + part * sum(max(e["prix"], 0) for e in es[1:]) - (1 if sugg else 0)
        if len(es) > 1: det.append(dict(cercle="(effets)", prix=round(prix_effet, 3), regle=f"provisoire, règle 2.3 : le plus cher {g:.2f} + {part:g} × les autres"))
        principal = es[0]
    else:                                                   # Cosmétique seule : le plus petit prix d'un effet
        prix_effet, principal = 0.0, dict(genre="cosmétique seule", famille=None, role=None)
    loc = next((r for r in rings if r[0] == "LOCALISATION"), None)
    p_loc, rg_loc = prix_localisation(loc)
    det.append(dict(cercle="LOCALISATION", prix=p_loc, regle=rg_loc))
    if "dans le temps" in rg_loc: lacunes.append("Localisation dans le temps")
    r_inc = rabais_incantation(cast)
    if r_inc: det.append(dict(cercle="DUREE (incantation)", prix=-r_inc, regle=f"lot 2 : incantation de {cast:g} s, rabais"))
    r_cond, d_cond = rabais_condition(rings)
    if r_cond: det.append(dict(cercle="CONDITION", prix=-round(r_cond, 3), regle="lot 3 : " + " ; ".join(d_cond)))
    r_comp, d_comp, ouverts = rabais_composante(rings)
    if r_comp: det.append(dict(cercle="COMPOSANTE", prix=-round(r_comp, 3), regle="lot 4 : " + " ; ".join(d_comp)))
    if ouverts: det.append(dict(cercle="COMPOSANTE", prix=0.0, regle="lot 4 : payé par le lanceur, prix ouvert (" + ", ".join(ouverts) + ")"))
    cosm = 0.0                                   # décision du 23 novembre (provisoire) : 0,05 par sens, « plein » = 5 sens
    for r in rings:
        if r[0] == "COSMETIQUE":
            n = 5 if r[1] == "plein" else (r[1] if _num(r[1]) else 0)
            cosm += 0.05 * n; det.append(dict(cercle="COSMETIQUE", prix=round(0.05 * n, 3), regle=f"Cosmétique : {n} sens × 0,05"))
    decides = p_loc - r_inc - r_cond - r_comp + cosm
    rs = restriction(rings)
    mesures = dict(cibles=n_cibles, cibles_lecture=why_c, zone=est_zone, marche=round(marche(sec, perm), 3), duree_s=sec, permanent=perm,
                   incantation_s=cast, restriction=rs, instances=instances, sursaut=sursaut(rings), figure=figure_a_part(rings))
    return dict(prix_effet=round(prix_effet, 3), decides=round(decides, 3), genre=principal["genre"], famille=principal.get("famille"),
                effets=[dict(prix=round(e["prix"], 3), genre=e["genre"], cercle=e["cercle"], sans_prix=e["sans_prix"], meca=e["meca"], degre=e["degre"],
                             garde=e["garde"], une_sorte=e["une_sorte"])
                        for e in es], suggestion=sugg,
                role=principal.get("role"), mesures=mesures, detail=det, lacunes=lacunes, sans_impact=not es)


def groupe(a):
    """le groupe de réglage d'une forme : son genre ; pour un état, sa famille (et sa grande famille en repli)"""
    if a["genre"] == "état": return "état : " + (a["famille"] or "?")
    return a["genre"]


def palier(a, coefs):
    """coût et palier avec les coefficients des relations (a, b, c) du groupe ; coefs : dict(a=, b=, c=, groupe=)"""
    m = a["mesures"]
    x_c = math.log2(max(m["cibles"], 1)) if a["genre"] not in ("blessure", "soin") else 0.0
    rel = (coefs.get("a", 0) * x_c + coefs.get("b", 0) * m["marche"] + coefs.get("c", 0) * (1 if m["restriction"] else 0)
           + coefs.get("d", 0) * (1 if m.get("sursaut") else 0))          # v6 : d ≤ 0, le rabais de la nouvelle chance
    cout = a["prix_effet"] + a["decides"] + rel
    return round(cout, 3), int(min(PALIER_MAX, max(0, math.floor(cout + 0.5)))), round(rel, 3)


# ---------------------------------------------------------------- réglage des relations (décision du 24 novembre : version B)
# Pour un système : la règle générale (a, b, c réglés ensemble sur toutes ses formes) donne le b de la durée, commun à tous les
# genres ; puis a et c de chaque genre (15 formes ou plus) sont réglés avec ce b fixé ; un genre plus petit prend la règle générale.
# Blessures et soins : a n'est pas réglé (la relation « cibles » est dans leur prix). Contraintes : a ≥ 0, b ≥ 0, c ≤ 0.
# Les moindres carrés se font sur des sommes (n, XᵀX, Xᵀy), qu'on peut additionner et retrancher (calcul « sort caché »).
# Variables : x = (log2(cibles), marche de durée, −restriction, −nouvelle chance) ; y = niveau − prix des effets − prix décidés.
# v6 : la nouvelle chance (« fin : chaque · … · sursaut ») est une relation réglée comme la restriction (d ≤ 0 : un rabais).
GEN = "(règle générale)"
MIN_FORMES = 15


NV = 4             # v6 : (log2(cibles), marche de durée, −restriction, −nouvelle chance)
NOUVELLE_CHANCE = False     # v7 (25 novembre) : le rabais de la nouvelle chance n'est pas prouvé (il ne tient pas partout) : 0 pour l'instant
def sommes_vides(): return [0.0, [[0.0] * NV for _ in range(NV)], [0.0] * NV]


def sommes_ajoute(S, v, y, sgn=1):
    S[0] += sgn
    for i in range(NV):
        S[2][i] += sgn * v[i] * y
        for j in range(NV): S[1][i][j] += sgn * v[i] * v[j]


def sommes_moins(S, T): return [S[0] - T[0], [[S[1][i][j] - T[1][i][j] for j in range(NV)] for i in range(NV)], [S[2][i] - T[2][i] for i in range(NV)]]


def sommes_plus(*Ss):
    out = sommes_vides()
    for S in Ss:
        out[0] += S[0]
        for i in range(NV):
            out[2][i] += S[2][i]
            for j in range(NV): out[1][i][j] += S[1][i][j]
    return out


def moindres_carres(S, libres):
    """moindres carrés positifs (a, b ≥ 0 ; c ≤ 0, porté par la variable −restriction) sur les variables libres : le meilleur
    sous-ensemble faisable"""
    best, bx = 0.0, [0.0] * NV
    for m in range(1, 2 ** len(libres)):
        idx = [libres[j] for j in range(len(libres)) if m >> j & 1]
        M = [[S[1][p][q] for q in idx] for p in idx]; b = [S[2][p] for p in idx]; n = len(idx)
        try:
            for c in range(n):
                piv = max(range(c, n), key=lambda r: abs(M[r][c]))
                if abs(M[piv][c]) < 1e-9: raise ZeroDivisionError
                M[c], M[piv] = M[piv], M[c]; b[c], b[piv] = b[piv], b[c]
                for r in range(n):
                    if r != c:
                        t = M[r][c] / M[c][c]; M[r] = [x - t * yy for x, yy in zip(M[r], M[c])]; b[r] -= t * b[c]
            sol = [b[c] / M[c][c] for c in range(n)]
        except ZeroDivisionError:
            continue
        if any(v < -1e-9 for v in sol): continue
        gain = sum(v * S[2][p] for v, p in zip(sol, idx))        # baisse de la somme des carrés à l'optimum
        if gain > best + 1e-12:
            best = gain; bx = [0.0] * NV
            for p, v in zip(idx, sol): bx[p] = v
    return dict(a=bx[0], b=bx[1], c=-bx[2], d=-bx[3])


def regle_genre(S, genre, b, nc=None):
    """a et c d'un genre, b (commun au système) fixé : on retire b × marche de la cible, puis moindres carrés sur a et c"""
    T = [S[0], S[1], [S[2][i] - b * S[1][i][1] for i in range(NV)]]
    nc = NOUVELLE_CHANCE if nc is None else nc
    r = moindres_carres(T, [i for i in ([2, 3] if genre in ("blessure", "soin") else [0, 2, 3]) if nc or i != 3])
    return dict(r, b=b)


def regles_systeme(general, par_genre, nc=None):
    """general : sommes de toutes les formes du système ; par_genre : {genre: sommes}. Rend {genre ou GEN: dict(a, b, c)}"""
    nc = NOUVELLE_CHANCE if nc is None else nc      # v8 : réglée dans les systèmes où elle tient (3.5, PF1), 0 ailleurs
    co = {GEN: moindres_carres(general, [0, 1, 2, 3] if nc else [0, 1, 2])}
    for g, S in par_genre.items():
        if S[0] >= MIN_FORMES: co[g] = regle_genre(S, g, co[GEN]["b"], nc)
    return co


def regle(co, genre):
    """la règle d'un genre dans un système (co : rendu de regles_systeme)"""
    r = dict(co.get(genre) or co[GEN])
    if genre in ("blessure", "soin"): r["a"] = 0.0
    return r
