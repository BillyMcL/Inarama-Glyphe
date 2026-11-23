"""Barème des sorts : le coût d'une forme calculé sur le glyphe seul (Noyau, cercles, valeurs, mots, satellites).

Cahier des charges : donnees/bareme/bareme_regles_2026-11-22.md ; tables : donnees/bareme/bareme_tables_2026-11-22.json.
Ce module n'est appelé par aucune construction du site : il sert à la mesure (outils/mesure_bareme.py) et à l'éditeur.

    cout(forme) -> dict(cout, palier, detail, effets, sans_trace, defaut)

- cout : le total, nombre décimal ; palier : le total arrondi (demi vers le haut) et borné de 0 à 10 (2.6) ;
- detail : chaque étape du calcul, avec la règle appliquée (« 2.1 état », « 2.4 zone »… : numéros du document) ;
- sans_trace : les relations dont une règle a besoin et dont le glyphe ne dit rien (lacunes d'écriture, partie 4.2) ;
- defaut : les mots des cercles d'Impact tombés au prix par défaut (3,0).

Le glyphe ne dit pas de quel jeu vient une forme : aucun facteur par jeu (partie 6). Le paramètre facteur_montant n'existe
que pour la comparaison de la mesure (ancien calcul : 3.5 × 1,25 ; PF1 × 1,2 ; PF2 × 1,25 sur les montants).
Le cercle d'Interaction (le palier du sort, + 1) n'est jamais lu : le coût en serait tiré par construction.
Les choix de lecture (ce que le document ne précise pas) sont marqués « LECTURE » et repris dans bilan_bareme.txt.
"""
import os, json, math

D = os.path.dirname(os.path.abspath(__file__))
TABLES = json.load(open(os.path.join(D, "..", "donnees", "bareme", "bareme_tables_2026-11-22.json"), encoding="utf-8"))
ECHELLES = {k: tuple(v) for k, v in TABLES["echelles"].items()}
MOT_ECHELLE = TABLES["mot_echelle"]
MONTANT = set(TABLES["mots_montant"])
OUTIL = TABLES["outils_prix_fixe"]
COEF_LEVEE = TABLES["coef_levee"]
FIN = TABLES["fin"]
SAVOIRFAIRE = {"SAVOIRFAIRE", "DISCRETION", "VIGILANCE"}      # facultés de savoir-faire (la parole et la connaissance ont leur échelle)
DEFAUT = 3.0

import lexique as LX
DEGRES = LX.DEGRES                      # mots de degré (A7) : un Impact chiffré dont le premier mot en est un dit un degré
PROFONDE = {"AME", "CORPS", "ESPRIT", "SORT"}          # cible profonde (2.4, document du 23 novembre)
OUVRE = {"MORT", "SORT", "ARTEFACT"}                   # condition qui ouvre (2.4)
ETRES = LX.CIBLE["ETRE"] | {"MORTVIVANT", "VIVANT", "MORT", "HOSTILE"}   # sortes d'êtres (LECTURE : lexique.py, catégorie ETRE)
PALIER_MAX = 10                                        # 2.6 : le palier 10 (la Quintessence) est atteignable
# Variante D : dégâts officiels de D&D 5 (Guide du maître, partie 8 du document), une action, instantané, jet pour moitié
DEGATS = {"une": [5.5, 11, 16.5, 27.5, 33, 38.5, 55, 60.5, 66, 82.5], "plusieurs": [3.5, 7, 10.5, 21, 24.5, 28, 38.5, 42, 45.5, 49]}
VERBES_NUISIBLES = LX.VERBES_NUISIBLES
OBJETS = LX.CIBLE["OBJET"]
UNITES = {"SECONDES": 1, "MINUTES": 60, "HEURES": 3600, "JOURS": 86400, "ANS": 31536000}
MANIERE = {"CONTRE", "MALGRE", "SANS", "SAUF", "TANTQUE", "PROCHAIN"}
COND_NEUTRES = {"PAROLE", "CONCENTRATION"}      # parole : la Condition commune ; concentration : pas de rabais pour l'instant (partie 3)


def _sats(r): return list(r[4]) if len(r) > 4 and r[4] else []
def _txt(s): return s[2] if len(s) > 2 and isinstance(s[2], str) else ""
def _est_sym(v): return isinstance(v, (tuple, list)) and len(v) == 2 and v[0] == "sym"
def _num(v): return isinstance(v, (int, float)) and not isinstance(v, bool)


def prix_degre(echelle, d):
    """prix d'un degré d (1 à 9 ; plein ou 10 et plus = le plein) sur une échelle : plein × (a + (d−1)/8 × (b − a))"""
    P, a, b = ECHELLES[echelle]
    if d == "plein" or (_num(d) and d >= 10): return P
    d = max(1, d)
    return P * (a + (d - 1) / 8 * (b - a))


def prix_montant(v, facteur=1.0):
    """règle des montants : −2,8 + 1,25 × log2(montant), jamais moins de 1"""
    return max(1.0, -2.8 + 1.25 * math.log2(max(v * facteur, 1)))


def palier_degats(m, colonne):
    """variante D : le palier d'un montant lu dans le tableau officiel, en interpolant entre les lignes ; sous le tour de magie,
    la première pente prolongée (plancher 0) ; au-delà du niveau 9, la dernière pente prolongée, jusqu'au palier 10"""
    t = DEGATS[colonne]
    if m <= t[0]: return max(0.0, (m - t[0]) / (t[1] - t[0]))
    for i in range(9):
        if m <= t[i + 1]: return i + (m - t[i]) / (t[i + 1] - t[i])
    return min(float(PALIER_MAX), 9 + (m - t[9]) / (t[9] - t[8]))


def _echelle_mot(w, ws):
    e = MOT_ECHELLE.get(w)
    if e == "facultés" and set(ws) & SAVOIRFAIRE: e = "savoirfaire"
    return e


# ---------------------------------------------------------------- 2.1 le prix d'un cercle d'Impact
def prix_impact(r, facteur=1.0, degats=None):
    """(prix, sorte, règle, mots au défaut, lacunes) d'un cercle d'Impact"""
    v, ws = r[1], [w for w in r[2] if w != "IMPARABLE"]
    st = _sats(r)
    seuil_x = [s for s in st if _txt(s).split()[:1] == ["INTERACTION"]]
    seuil_i = [s for s in st if _txt(s).split()[:1] == ["IMPACT"] and len(_txt(s).split()) > 1]
    if ws[:1] == ["PUISSANCE"] or "PUISSANCE" in ws and not [w for w in ws if MOT_ECHELLE.get(w) or w in OUTIL]:
        if _num(v): return float(v), "être", f"2.1 être appelé : puissance {v}", [], []
        return DEFAUT, "être", "2.1 être appelé : puissance sans valeur, prix par défaut 3,0", ["PUISSANCE (plein)"], ["puissance d'un être appelé (valeur pleine)"]
    if seuil_x and not seuil_i:
        x = seuil_x[0][1]
        p = 9.0 if not _num(x) else float(max(0, x - 1))
        return p, "seuil", f"2.1 seuil en Interaction {x if _num(x) else 'plein'} : dissiper jusqu'au palier {p:g}", [], []
    if seuil_i:
        ps, regles, dft, lac = [], [], [], []
        for s in seuil_i:
            mot = _txt(s).split()[1]
            if mot == "PUISSANCE":
                if _num(s[1]): ps.append(float(s[1])); regles.append(f"seuil puissance {s[1]}")
                else: ps.append(DEFAUT); regles.append("seuil puissance sans valeur (3,0)"); lac.append("puissance d'un seuil (valeur pleine)")
                continue
            e = _echelle_mot(mot, ws)
            if e is None:
                ps.append(DEFAUT); regles.append(f"seuil « {mot} » sans échelle (3,0)"); dft.append(f"{mot} (seuil)"); continue
            c = COEF_LEVEE.get(e, 0.8)
            p = max(0.4, prix_degre(e, s[1] if (_num(s[1]) or s[1] == "plein") else "plein") * c)
            ps.append(p); regles.append(f"seuil {mot} {s[1]} ({e}) × {c:g}")
        if "FORME" in ws and any(_txt(s).split()[1] == "PUISSANCE" for s in seuil_i):      # forme prise (décision du 18 novembre)
            pu = [float(s[1]) for s in seuil_i if _txt(s).split()[1] == "PUISSANCE" and _num(s[1])]
            pu = pu[0] if pu else DEFAUT
            k = 2 / 3 if (_num(v) and v <= 6) else 1.0
            return 2.3 + k * pu, "forme prise", f"2.1 forme prise : socle 2,3 + {'deux tiers de ' if k < 1 else ''}la puissance {pu:g}", dft, lac
        ps.sort(reverse=True)
        part = 0.5 if ps[0] < 3 else 0.25 if ps[0] < 6 else 0.1
        p = ps[0] + part * sum(ps[1:])
        return p, "seuil", "2.1 lever, garder, agir malgré : " + " ; ".join(regles), dft, lac
    cands = []
    for w in ws:
        e = _echelle_mot(w, ws)
        if e:
            d = v if (_num(v) or v == "plein") else "plein"
            p = prix_degre(e, d) * (1.5 if w == "CHANCE" else 1)
            cands.append((p, "état", f"2.1 état « {w} » {d} sur l'échelle {e}" + (" × 1,5 (chance)" if w == "CHANCE" else "")))
    for w in ws:
        if w in OUTIL: cands.append((float(OUTIL[w]), "outil", f"2.1 prix fixe de « {w} »"))
    if "SOUHAIT" in ws:
        p = float(min(9, max(x[1] for x in seuil_x))) if seuil_x and all(_num(x[1]) for x in seuil_x) else 9.0
        cands.append((p, "souhait", "2.1 souhait : palier du sort reproduit + 1"))
    if _num(v) and (not ws or ws[0] in MONTANT or ws[0] not in DEGRES) and not cands:       # un état ou un outil l'emporte
        if degats:
            p = palier_degats(v * facteur, degats)
            cands.append((p, "blessure", f"variante D : montant {v} lu dans le tableau officiel de D&D 5, colonne « {'une cible' if degats == 'une' else 'plusieurs cibles'} »"))
        else:
            p = prix_montant(v, facteur)
            cands.append((p, "blessure", f"2.1 montant {v}" + (f" × {facteur:g}" if facteur != 1 else "") + " : −2,8 + 1,25 × log2, plancher 1"))
    if cands:
        p, k, rg = max(cands, key=lambda c: c[0])
        return p, k, rg, [], []
    lac = []
    if v == "plein" and set(ws) & MONTANT: lac.append("montant plein (sans valeur)")
    mots = [w for w in ws if w not in MANIERE] or ["(aucun mot)"]
    return DEFAUT, "inconnu", "2.1 aucun mot connu : prix par défaut 3,0", mots, lac


# ---------------------------------------------------------------- lecture des relations sur les cercles (partie 4.2)
def _duree(rings):
    """(secondes, permanent, incantation en secondes, mots de fin) lus sur le cercle Durée"""
    r = next((x for x in rings if x[0] == "DUREE"), None)
    if r is None: return 0.0, False, 0.0, []
    us = [w for w in r[2] if w in UNITES]; fins = [w for w in r[2] if w not in UNITES]
    st = [s for s in _sats(r) if not _txt(s) and not _est_sym(s[1])]
    if st:                                  # incantation sur le cercle, durée maximale en satellite (convert : « incantation : … »)
        cast = r[1] * UNITES[us[0]] if _num(r[1]) and us else 0.0
        dv = st[0][1]
        if dv == "plein": return 0.0, True, cast, fins
        u = us[1] if len(us) > 1 else (us[0] if us else "SECONDES")
        return float(dv) * UNITES[u], False, cast, fins
    if r[1] == "plein": return 0.0, True, 0.0, fins
    if _num(r[1]) and us: return float(r[1]) * UNITES[us[0]], False, 0.0, fins     # LECTURE : une seule unité = la durée
    return 0.0, False, 0.0, fins


def _volume(a):
    v, ws = a[1], a[2]
    if not _num(v): return None
    if ws[:1] == ["VOLUME"]:
        return v * {"METRES": 1, "DECAMETRES": 1e3, "HECTOMETRES": 1e6, "KILOMETRES": 1e9}.get(ws[1] if len(ws) > 1 else "METRES", 1)
    if ws[:1] == ["LONGUEUR"]: return v * (1000 if "KILOMETRES" in ws else 1) * 1.5 * 1.5      # LECTURE : ligne de 1,5 m de large
    if ws[:1] == ["SURFACE"]: return v * 3.0                                                 # LECTURE : 3 m de haut
    if ws[:1] == ["DIAMETRE"]: return 4 / 3 * math.pi * (v / 2) ** 3
    return None


def relations(f):
    """ce que les cercles disent des relations : cibles, zone, distance, durée, prix, conditions"""
    rings = f["rings"]
    R = dict(sans_trace=[])
    cible = next((r for r in rings if r[0] == "CIBLE"), None)
    R["cible_val"] = cible[1] if cible else None
    R["cible_mots"] = list(cible[2]) if cible else []
    qs = [s[1] for s in (_sats(cible) if cible else []) if not _txt(s) and not _est_sym(s[1])]
    R["n_cibles"] = qs[0] if qs else 1
    R["budget"] = [s[1] for s in (_sats(cible) if cible else []) if _txt(s).startswith("VIE REPARTIR") and _num(s[1])]
    R["psyche"] = "PSYCHE" in R["cible_mots"] or any(_txt(s) == "CIBLE PSYCHE" for r in rings if r[0] == "IMPACT" for s in _sats(r))
    R["objet"] = bool(set(R["cible_mots"]) & OBJETS)
    # zone : cercles Forme et Ampleur (toutes les zones d'une forme combinée : la plus grande compte)
    zone = R["cible_val"] == "plein" or any(r[0] == "FORME" for r in rings)
    vols = [x for x in (_volume(r) for r in rings if r[0] == "AMPLEUR") if x]
    R["zone"], R["volume"] = zone, (max(vols) if vols else None)
    if zone and not vols: R["sans_trace"].append("zone sans taille (ni Ampleur ni volume)")
    loc = next((r for r in rings if r[0] == "LOCALISATION"), None)
    R["distance"] = None
    if loc:
        if set(loc[2]) & {"AVENIR", "PASSE"}: R["distance"] = "temps"
        elif loc[1] == "plein" or "KILOMETRES" in loc[2]: R["distance"] = "loin"
        elif _num(loc[1]): R["distance"] = "loin" if loc[1] > 2 else "contact"
    R["duree"], R["permanent"], R["incantation"], R["fins"] = _duree(rings)
    q = [r[1] for r in rings if r[0] == "QUANTITE"]
    R["instances"] = q[0] if q and _num(q[0]) else 1
    if q and not _num(q[0]): R["sans_trace"].append("quantité pleine (nombre d'instances non écrit)")
    comp = [r for r in rings if r[0] == "COMPOSANTE"]
    R["prix_or"], R["consomme"], R["contrecoup"] = None, False, []
    for c in comp:
        if "CONTREPARTIE" in c[2]: R["contrecoup"].append(c); continue
        if c[2][:1] == ["VIE"]: continue
        R["consomme"] = R["consomme"] or "CONSOMME" in c[2]
        mon = next((m for m in ("PLATINE", "OR", "ARGENT", "CUIVRE") if m in c[2]), None)
        if _num(c[1]) and mon: R["prix_or"] = c[1] * {"PLATINE": 10, "OR": 1, "ARGENT": 0.1, "CUIVRE": 0.01}[mon]
        elif "CONSOMME" in c[2] or mon: R["sans_trace"].append("prix d'une Composante sans valeur")
    cond = [r for r in rings if r[0] == "CONDITION"]
    cw = [w for r in cond for w in r[2]]
    R["etres_condition"] = [w for w in cw if w in ETRES and w not in OUVRE]     # « mort » en Condition : la condition qui ouvre
    R["profonde"] = sorted(set(R["cible_mots"]) & PROFONDE)
    R["ouvre"] = sorted(set(cw) & OUVRE)
    R["concentration"] = "CONCENTRATION" in cw
    R["exigence"] = [w for w in cw if w not in COND_NEUTRES and w not in ETRES and w not in MANIERE and w not in OUVRE]
    R["prochain"] = "PROCHAIN" in cw or any("PROCHAIN" in _txt(s).split() for r in rings for s in _sats(r))
    R["seuil_vie"] = [s[1] for r in cond for s in _sats(r) if _txt(s).startswith("IMPACT VIE") and _num(s[1])]
    return R


# ---------------------------------------------------------------- le calcul
def genre(r, sorte, verbe):
    """le genre d'un effet, pour la mesure : blessure, soin, état, être appelé, outil ou déplacement, garde, autre"""
    ws = set(r[2])
    if sorte == "être": return "être appelé"
    if sorte == "outil": return "outil ou déplacement"
    if sorte in ("état", "seuil", "forme prise"):
        return "garde" if any(MOT_ECHELLE.get(w) == "garde" for w in ws) else "état"
    if sorte == "blessure":
        if ws & {"REMPART", "ABSORPTION", "RIPOSTE"}: return "garde"
        if "VIE" in ws and verbe.split(" · ")[0] not in VERBES_NUISIBLES: return "soin"
        return "blessure"
    return "autre"


def cout(f, facteur_montant=1.0, force_tous_ajouts=True, degats_officiels=False, rabais_concentration=0.0, concentration=None):
    """coût d'une forme (dict du moteur) ; force_tous_ajouts : chaque ajout × force de l'effet (document, 2.4) ;
    False : seulement les cibles et la zone (calcul du 20 novembre), pour comparaison.
    degats_officiels : variante D (montants lus dans le tableau de D&D 5) ; rabais_concentration : variante C (la
    concentration lue sur la Condition ; concentration=True/False ne sert qu'à une simulation de la mesure, hors glyphe)."""
    det, dft, lac = [], [], []
    rings = f["rings"]
    I = [r for r in rings if r[0] == "IMPACT"]
    if not I: return None
    R = relations(f); lac += R["sans_trace"]
    etre = any(r[2][:1] == ["PUISSANCE"] for r in I)
    n = R["n_cibles"]
    multi = n == "plein" or (_num(n) and n >= 2)
    colonne = ("plusieurs" if (multi or R["zone"]) else "une") if degats_officiels else None
    es, sugg = [], False
    for r in I:
        ws = set(r[2])
        if etre and ws & {"INJONCTION", "SUGGESTION", "DOMINATION"} and "PUISSANCE" not in ws:
            sugg = sugg or "SUGGESTION" in ws
            det.append(f"2.3 « {' · '.join(sorted(ws & {'INJONCTION', 'SUGGESTION', 'DOMINATION'})).lower()} » comprise dans la puissance de l'être appelé")
            continue
        p, k, rg, d_, l_ = prix_impact(r, facteur_montant, colonne)
        dft += d_; lac += l_
        aj = []
        st = _sats(r)
        if any(_txt(s).startswith("DUREE CHAQUE") for s in st) and not any(_txt(s).startswith("LOCALISATION") for s in st):
            p += 1.0; aj.append("2.2 chaque instant +1")
        if "IMPARABLE" in r[2]:
            x = 0 if p < 3 else 1 if p < 6 else 3; p += x; aj.append(f"2.2 imparable +{x}")
        conds = [s for s in st if _txt(s).split()[:1] == ["CONDITION"] and "PROCHAIN" not in _txt(s).split()]
        if conds and p > 3:
            x = 0.3 * (p - 3); p -= x; aj.append(f"2.2 condition sur l'effet −{x:.2f}")
        if "SUSPENSION" in ws: p -= 1.0; aj.append("2.2 suspension −1")
        es.append((p, k, genre(r, k, f.get("verb", "")))); det.append(f"effet « {' · '.join(r[2]).lower() or 'sans mot'} » {r[1]} : {p:.2f} — {rg}" + (" ; " + " ; ".join(aj) if aj else ""))
    if not es: return None
    es.sort(key=lambda e: -e[0])
    g, k0, genre0 = es[0]
    inst = (not R["permanent"]) and 0 < R["duree"] <= 6
    if inst and k0 == "état":
        g *= 0.75; det.append("2.3 état d'un instant × 0,75")
    part = 0.5 if g < 3 else 0.25 if g < 6 else 0.1
    autres = sum(max(e[0], 0) for e in es[1:])
    c = g + part * autres
    if len(es) > 1: det.append(f"2.3 plusieurs effets : le plus cher {g:.2f} + {part:g} × {autres:.2f}")
    if sugg: c -= 1; det.append("2.3 suggestion −1")
    # 2.4 ajouts
    fz = min(1.0, max(g, 0) / 3)
    ext, aj = 0.0, []
    def ajoute(x, nom, force=True):
        nonlocal ext
        x2 = x * (fz if (force and (force_tous_ajouts or nom in ("cibles", "zone", "budget"))) else 1.0)
        if x2 > 0.005: ext += x2; aj.append(f"{nom} +{x2:.2f}")
    long_ = R["permanent"] or R["duree"] > 3600
    tableau = colonne == "plusieurs" and k0 == "blessure"      # variante D : la colonne « plusieurs cibles » compte déjà zone et cibles
    if tableau: aj.append("variante D : ni zone ni cibles (le tableau officiel les compte)")
    if multi and not tableau:
        ajoute((4.0 if long_ else 2.5) if n == "plein" else 2.0 if n >= 4 else 1.0, "cibles")
    elif R["budget"] and not multi:
        ajoute(1.0 if R["budget"][0] < 60 else 2.0, "budget")
    if R["distance"] == "loin": ajoute(0.4, "distance")
    if R["zone"] and R["volume"] and not multi and not tableau:
        ajoute(min(3.0, 0.3 * math.log2(max(R["volume"], 30) / 30)), "zone")
    if R["psyche"]: ajoute(0.3, "psyché")
    if R["profonde"]: ajoute(1.0, "cible profonde « " + " · ".join(w.lower() for w in R["profonde"]) + " »")
    if R["ouvre"]: ajoute(1.0, "condition qui ouvre « " + " · ".join(w.lower() for w in R["ouvre"]) + " »")
    if R["permanent"] or R["duree"] > 6:
        L = 6.0 if R["permanent"] else min(5.0, math.log10(R["duree"] / 6))
        w = 1 if g < 3 else 0.5 if g < 6 else 0.25
        ajoute(0.3 * L * w, "durée", force=False)
    if _num(R["instances"]) and R["instances"] > 1:
        ajoute((1.0 if k0 == "blessure" else 0.5) * math.log2(R["instances"]), "quantité")
    plaf = max(g, 0) + 1
    if ext > plaf: aj.append(f"plafond : {ext:.2f} ramené à {plaf:.2f}"); ext = plaf
    if aj: det.append("2.4 ajouts : " + " ; ".join(aj))
    # 2.5 rabais
    rab_cat = 0.0
    if R["cible_val"] == 3 and (set(R["cible_mots"]) & ETRES or R["etres_condition"]):
        rab_cat = 3.0 if g >= 3 else 1.0; det.append(f"2.5 limitation à une sorte d'êtres −{rab_cat:g} (LECTURE : cible ennemie et sorte d'êtres écrite)")
    rabs = []
    gp = max(0.0, g - 3)
    fins = [] if R["fins"][:2] == ["TANTQUE", "CONCENTRATION"] else R["fins"]       # tant que concentration : la concentration (partie 3)
    for w in fins:
        if w == "CONCENTRATION": continue
        if w in FIN: rabs.append((FIN[w] * max(g, 0), f"fin « {w.lower()} » (table)"))
        elif w not in MANIERE or w == "TANTQUE": rabs.append((0.3 * gp, f"fin « {w.lower()} »"))
    if R["prochain"]: rabs.append((0.3 * gp, "occasion « prochain »"))
    if R["exigence"]: rabs.append((0.3 * gp, "condition ou exigence « " + " · ".join(w.lower() for w in R["exigence"]) + " »"))
    if R["objet"]: rabs.append((0.3 * gp, "cible-objet"))
    if R["incantation"] >= 600: rabs.append((0.3 * gp, "incantation longue"))
    if R["prix_or"] is not None:
        fv = (0.1 if R["prix_or"] < 10 else 0.2 if R["prix_or"] < 100 else 0.3) * (1.0 if R["consomme"] else 0.5)
        rabs.append((fv * gp, f"Composante {R['prix_or']:g} po" + (", consommée" if R["consomme"] else "")))
    rabs = sorted([r for r in rabs if r[0] > 0.005], key=lambda r: -r[0])
    rp = min(2.0, (rabs[0][0] + 0.5 * sum(x for x, _ in rabs[1:])) if rabs else 0.0)
    if rabs: det.append("2.5 rabais : " + " ; ".join(f"{n_} −{x:.2f}" for x, n_ in rabs) + f" → −{rp:.2f} (le plus fort entier, la moitié des autres, 2 au plus)")
    tot = c + ext - rab_cat - rp
    if rabais_concentration and (R["concentration"] if concentration is None else concentration):
        tot -= rabais_concentration; det.append(f"variante C : concentration −{rabais_concentration:g}")
    for r in R["contrecoup"]:
        mot = r[2][1] if len(r[2]) > 1 else None
        e = _echelle_mot(mot, r[2]) if mot else None
        if e: pc = prix_degre(e, r[1] if (_num(r[1]) or r[1] == "plein") else "plein")
        elif _num(r[1]): pc = prix_montant(r[1])
        else: pc = DEFAUT
        tot -= part * pc; det.append(f"2.5 contrecoup « {(mot or '').lower()} » −{part * pc:.2f}")
    sv = R["seuil_vie"] + R["budget"]
    if sv:
        fr = 0.3 if sv[0] < 30 else 0.2 if sv[0] < 60 else 0.1 if sv[0] <= 120 else 0.0
        if fr:
            x = fr * max(tot, 0); tot -= x; det.append(f"2.5 seuil de vie {sv[0]} : −{100 * fr:.0f} % (−{x:.2f})")
    palier = int(min(PALIER_MAX, max(0, math.floor(tot + 0.5))))
    return dict(cout=round(tot, 3), palier=palier, detail=det, effets=[(round(p, 3), k) for p, k, _ in es], sorte=k0, genre=genre0,
                sans_trace=sorted(set(lac)), defaut=dft)
