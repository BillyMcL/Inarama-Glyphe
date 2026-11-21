"""Phase 4b : formes hybrides et arts rares (couche voisine de corrections.py, appelée par corrections.appliquer).

Données : donnees/phase4b/B3_formes_hybrides.csv. Les formes sont retrouvées par clé et RANG D'ORIGINE (rang parmi les
formes du sort, à partir de 0, Elden Ring exclu, compté avant les retraits de la phase 4a), comme en phase 4a.

Étape 2 : formes existantes. Hybrides : école de B3, hémisphère de l'école, pôle de chaque cercle d'Impact ; conversions
d'art rare (en hybride ou en Arcane) ; formes à retirer. Une ligne qui ne s'accorde pas avec la forme est refusée et listée.

Règle des pôles (validée le 20 novembre 2026) : le quota minoritaire se compte par critère, comme split_hybrid ; le critère
Impact prend une seule place dès qu'un de ses cercles est opposé ; les autres places vont aux critères suivants dans l'ordre
du moteur, Impact sauté ; sans Impact opposé, l'Impact reste du côté de l'école ; le quota ne monte que de zéro à un, quand
un Impact est opposé. Chaque cercle d'Impact garde son pôle (champ poles_impacts).
"""
import os, csv, re
import spells as SP

ETAPE = int(os.environ.get("PHASE4B_ETAPE", "4"))      # étapes de la phase 4b appliquées (0 ou 1 : aucune donnée)
D = os.path.dirname(os.path.abspath(__file__))
P4B = os.path.join(D, "..", "donnees", "phase4b")
B3 = list(csv.DictReader(open(os.path.join(P4B, "B3_formes_hybrides.csv"), encoding="utf-8-sig"), delimiter=";")) \
    if os.path.exists(os.path.join(P4B, "B3_formes_hybrides.csv")) else []
EXISTANTES = {(l["cle"], int(l["rang_forme_modele"])): l for l in B3 if l["statut"] == "existante"}
HEMI_ECOLE = {"Abjuration": "Hodolin", "Divination": "Hodolin", "Illusion": "Hodolin", "Invocation": "Hodolin",
              "Enchantement": "Galombar", "Transmutation": "Galombar", "Évocation": "Galombar", "Nécromancie": "Galombar"}
POLE_HEMI = {"Hodolin": "lumineux", "Galombar": "ténébreux"}

FAITS = {"ecole": [], "hemisphere": [], "poles": [], "retrait": [], "vers_hybride": [], "vers_arcane": [], "quota_monte": [], "face_dans_un_impact": []}
REFUS = []          # (ligne, raison)


def poles(l):
    """« 0:lumineux | 1:ténébreux » → ["lumineux", "ténébreux"] (dans l'ordre des cercles d'Impact)"""
    if not l["impacts_poles"].strip(): return []
    out = {}
    for x in l["impacts_poles"].split("|"):
        i, p = x.split(":"); out[int(i)] = p.strip()
    return [out[i] for i in range(len(out))]


def split_poles(crits, hemi, level, poles_impacts):
    """répartition d'une forme hybride selon la règle des pôles ; hemi : « H » (Hodolin) ou « G » (Galombar)"""
    import convert as C
    ecole = "lumineux" if hemi == "H" else "ténébreux"
    opp = [p for p in (poles_impacts or []) if p != ecole]
    gardes = [p for p in (poles_impacts or []) if p == ecole]
    n = len(crits) + 1
    k = min(len(crits), C.rnd(n * level / 18), n // 2)
    monte = k == 0 and bool(opp)
    if monte: k = 1
    order = C.IMPOSED if hemi == "H" else C.SPACE
    minor = ((["IMPACT"] if opp else []) + [c for c in order if c in crits and c != "IMPACT"])[:k]
    major = ["NOYAU"] + [c for c in crits if c not in minor or (c == "IMPACT" and gardes)]
    return ((major, minor) if hemi == "H" else (minor, major)), monte


def repartition(f, crits):
    """appelée par corrections.repartition pour une forme soumise à la règle des pôles"""
    sp, monte = split_poles(crits, "H" if "· Hodolin ·" in f["verb"] else "G", f["level"], f.get("poles_impacts"))
    return sp


def _refus(l, why):
    REFUS.append((l, why))


def existante(g, k):
    """étape 2 : applique la ligne « existante » de B3 à la forme g (rang d'origine k) ; renvoie (forme, à retirer ?)"""
    import convert as C, combos as KB
    l = EXISTANTES.get(k)
    if l is None or ETAPE < 2: return g, False
    t = l["type"]
    if t.startswith("à retirer"):
        if g["fam"] != "H": _refus(l, f"famille {g['fam']}"); return g, False
        # une forme remplacée par des formes par élément n'est retirée qu'avec leur création (étape 5) : sinon son sort
        # resterait sans aucune forme (Vague d'anéantissement élémentaire n'a que ces deux formes)
        if t == "à retirer (remplacée par une forme par élément)" and ETAPE < 5: return g, False
        FAITS["retrait"].append(k); return g, True
    n_imp = sum(1 for r in g["rings"] if r[0] == "IMPACT")
    ps = poles(l)
    if t in ("hybride", "conversion : art rare → hybride"):
        ecole, hemi, comb = l["ecole"], l["hemisphere"], l["combinaison"]
        if HEMI_ECOLE.get(ecole) != hemi: _refus(l, f"hémisphère {hemi} hors de l'école {ecole}"); return g, False
        if comb not in KB.COMBOS: _refus(l, f"combinaison inconnue « {comb} »"); return g, False
        if len(ps) != n_imp: _refus(l, f"{len(ps)} pôles pour {n_imp} cercles d'Impact"); return g, False
        opp = {i for i, p in enumerate(ps) if p != POLE_HEMI[hemi]}
        dit = {int(x) for x in l["impacts_opposes"].split("|") if x.strip()}
        if opp != dit: _refus(l, f"Impacts opposés {sorted(dit)} / pôles {ps}"); return g, False
        une_des_faces = any(x in g["label"].lower() for x in ("lumineu", "ténébreu"))      # la forme est une des deux faces du sort
        if l["face"] and une_des_faces and POLE_HEMI[hemi] != {"lumineuse": "lumineux", "ténébreuse": "ténébreux"}[l["face"]]:
            _refus(l, f"face {l['face']} sous {hemi}"); return g, False
        f_, a_, t_, e_ = KB.COMBOS[comb]
        core = SP.hyb(f=f_, a=a_, t=t_, e=e_, label=C.norm(ecole))
        verb = f"{ecole} · {hemi} · {comb} ({KB.code(comb)})"
        if t == "hybride":
            m = re.match(r"(.+) · (Hodolin|Galombar) · (.+) \(", g["verb"])
            if g["fam"] != "H" or not m or m.group(3) != comb:
                _refus(l, f"noyau actuel « {g['verb']} »"); return g, False
            if m.group(1) != ecole: FAITS["ecole"].append((k, m.group(1), ecole))
            if m.group(2) != hemi: FAITS["hemisphere"].append((k, m.group(2), hemi))
            g2 = dict(g, core=core, verb=verb)
        else:
            if g["fam"] != "R": _refus(l, f"famille {g['fam']}"); return g, False
            notes = [f"Magie hybride, combinaison {comb} : l'élément en jeu." if n.startswith("Art rare (") else n for n in g["notes"]]
            g2 = dict(g, fam="H", core=core, verb=verb, notes=notes, r0=66, label=g["label"].replace("Art rare", "Forme hybride", 1))
            FAITS["vers_hybride"].append(k)
        if l["face"] and not une_des_faces and POLE_HEMI[hemi] != {"lumineuse": "lumineux", "ténébreuse": "ténébreux"}[l["face"]]:
            FAITS["face_dans_un_impact"].append(k)      # forme unique qui porte le symbole d'une face dans un Impact opposé
        FAITS["poles"].append(k)
        crits = list(dict.fromkeys(r[0] for r in g2["rings"]))
        _, monte = split_poles(crits, "H" if hemi == "Hodolin" else "G", g2["level"], ps or None)
        if monte: FAITS["quota_monte"].append(k)
        return dict(g2, poles_impacts=tuple(ps) or None, regle_4b=True, element_par_defaut=False), False
    if t == "conversion : art rare → Arcane":
        c = g["core"]
        if g["fam"] != "R" or c[0] != "chrono": _refus(l, f"famille {g['fam']}"); return g, False
        vk, vn = c[1], bool(c[2])
        if C.VERBS[(vk, vn)] != l["verbe"]: _refus(l, f"verbe actuel {C.VERBS[(vk, vn)]}"); return g, False
        notes = ["Arcane : aucun élément en jeu, un verbe suffit." if n.startswith("Art rare (") else n for n in g["notes"]]
        FAITS["vers_arcane"].append(k)
        return dict(g, fam="A", core=SP.verb(vk, vn), pol="down" if vn else "up", split=None, r0=34, notes=notes,
                    verb=f"{C.VERBS[(vk, vn)]} · {C.VERB_GROUP[vk].lower()} {'−' if vn else '+'}",
                    label=g["label"].replace("Art rare", "Forme arcane", 1)), False
    _refus(l, f"type « {t} » non traité à l'étape 2"); return g, False


# ---------- étapes 4 à 7 : formes créées ----------
from collections import defaultdict as _dd
CREER = _dd(list)                   # (cle, rang d'origine du modèle) → lignes « à créer », dans l'ordre du fichier
for _l in B3:
    if _l["statut"] == "à créer": CREER[(_l["cle"], int(_l["rang_forme_modele"]))].append(_l)
TYPES = {4: {"combinaison fixe", "énergie pure"},
         5: {"élément choisi", "élément au choix (noyau vide)", "contre-sort (noyau vide)"},
         6: {"art rare", "forme d'Arcane nouvelle"}}
HYBRIDES = {"combinaison fixe", "énergie pure", "élément choisi", "élément au choix (noyau vide)", "contre-sort (noyau vide)"}
CREEES = []                         # (cle, rang du modèle, type, combinaison, nom de la forme)
REDITS = []                         # (cle, rang du modèle, combinaison, critère, lecture avant, lecture après)
NOTES_RETIREES = ("Arcane : aucun élément en jeu, un verbe suffit.", "Pas de forme hybride : aucune combinaison naturelle ne porte cet effet.")


def types_actifs():
    return set().union(*(TYPES[e] for e in TYPES if e <= ETAPE))


def nom_hybride(modele, comb, plusieurs):
    """nom d'une forme hybride créée (décision du 21 novembre 2026)"""
    if modele == "Forme arcane": n = "Forme hybride"
    elif modele.startswith("Forme arcane — "): n = "Forme hybride — " + modele[len("Forme arcane — "):]
    else: n = "Forme hybride — " + modele
    return n + (f" — {comb}" if plusieurs else "")


def _redit(rings, comb, cle, rang):
    """règle REDIT du moteur appliquée à une forme créée : les symboles d'un Impact que la combinaison du Noyau dit déjà ne
    sont pas posés — l'Impact porte exactement les symboles de la combinaison, ou, pour une combinaison d'un seul élément,
    seulement le symbole de cet élément. La lecture retire la mention de ces symboles et dit que le noyau porte l'énergie."""
    import combos as KB, convert as C
    f_, a_, t_, e_ = KB.COMBOS[comb]
    units = sorted(["feu"] * f_ + ["air"] * a_ + ["terre"] * t_ + ["eau"] * e_)
    mono = len(set(units)) == 1
    ELS = ("feu", "air", "terre", "eau")
    out = []
    for r in rings:
        sats = list(r[4]) if len(r) > 4 and r[4] else []
        sy = [s for s in sats if C.est_symbole(s[1]) and s[1][1] in ELS]
        cas = None
        if r[0] == "IMPACT" and sy:
            el = sorted(s[1][1] for s in sy)
            if el == units: cas = comb.lower()
            elif mono and set(el) == {units[0]}: cas = units[0]
        if cas is None:
            out.append(r); continue
        reste = [s for s in sats if s not in sy]
        if r[1] == "plein" and not r[2] and not any(not C.est_symbole(s[1]) for s in reste):
            # Impact plein dont l'énergie est le seul contenu : comme le moteur (energies_et_cibles), l'énergie reste en mot
            # d'action ; le mot est celui de la fiche que le moteur traduit exactement par ces symboles
            mot = _mot_energie(cle, sorted(s[1][1] for s in sy))
            import lint as LI
            if mot is not None and LI.MILLE_ET_UN is not None and mot not in LI.MILLE_ET_UN:
                HORS_LEXIQUE.append((cle, rang, comb, mot)); mot = None          # un mot hors lexique se signale, il ne s'ajoute pas
            if mot is None:
                out.append((*r[:3], r[3], r[4], "SANS_MOT")); continue
            rd = r[3]
            for e in set(s[1][1] for s in sy):
                for pat in (f" ; satellite symbole de {C.SYM_FR[e]}", f" ; satellite : symbole de {C.SYM_FR[e]}"):
                    rd = rd.replace(pat, "")
            rd = rd.replace(f" ; satellites : les symboles de la combinaison {comb}", "")
            vu = C.shown(mot)
            if rd.startswith("plein, sans nature : la force brute du verbe"): rd = f"plein, {vu}" + rd[len("plein, sans nature : la force brute du verbe"):]
            elif rd.startswith("plein"): rd = f"plein, {vu}" + rd[len("plein"):]
            REDITS.append((cle, rang, comb, r[0], r[3], rd))
            out.append((r[0], r[1], [mot], rd, C._resats(reste)) if reste else (r[0], r[1], [mot], rd))
            continue
        rd = r[3]
        for e in set(s[1][1] for s in sy):
            for pat in (f" ; satellite symbole de {C.SYM_FR[e]}", f" ; satellite : symbole de {C.SYM_FR[e]}"):
                rd = rd.replace(pat, "")
        rd = rd.replace(f" ; satellites : les symboles de la combinaison {comb}", "")
        rd += f" ; l'énergie (« {cas} ») est dite par le noyau"
        REDITS.append((cle, rang, comb, r[0], r[3], rd))
        out.append((r[0], r[1], r[2], rd, C._resats(reste)) if reste else (r[0], r[1], r[2], rd))
    return out


def _mot_energie(cle, symboles):
    """le mot d'Impact de la fiche que le moteur traduit exactement par ces symboles ; None s'il n'y en a pas un seul"""
    import convert as C, combos as KB, mots_univers as MU
    from fiches import FICHES
    imp = (FICHES.get(cle) or {}).get("impact")
    if not imp or len(imp) < 2: return None
    def unites(W):
        if W in ("FEU", "AIR", "TERRE", "EAU"): return [W.lower()]
        if W in C.ELEM_UNITS: return list(C.ELEM_UNITS[W])
        if W in MU.ENERGIES:
            f_, a_, t_, e_ = KB.COMBOS[MU.ENERGIES[W]]; return ["feu"] * f_ + ["air"] * a_ + ["terre"] * t_ + ["eau"] * e_
        return None
    ok = [w for w in imp[1] if unites(C.norm(w)) is not None and sorted(unites(C.norm(w))) == symboles]
    return C.word(ok[0]) if len({C.norm(w) for w in ok}) == 1 else None      # convert.word : le mot se dessine, comme tout mot de fiche


def sans_mot(rings):
    """numéros (parmi les Impacts) des cercles d'Impact « plein » sans mot ni satellite à mot : refusés par la règle 1 en hybride"""
    import convert as C
    out, i = [], 0
    for r in rings:
        if r[0] != "IMPACT": continue
        sats = r[4] if len(r) > 4 and r[4] else []
        if r[1] == "plein" and not r[2] and not any(not C.est_symbole(s[1]) and len(s) > 2 and s[2] for s in sats): out.append(i)
        i += 1
    return out


HORS_LEXIQUE = []                   # (cle, rang du modèle, combinaison, mot) : mot d'énergie gardé mais absent du lexique fermé
EN_ATTENTE = []                     # formes non créées faute de mot d'action : (cle, rang du modèle, type, combinaison, n° d'Impact, lecture)


def hybride(g, l, k, plusieurs):
    """une forme hybride créée d'après la forme modèle g (recette du prompt de la phase 4b)"""
    import convert as C, combos as KB
    comb, ecole, hemi = l["combinaison"], l["ecole"], l["hemisphere"]
    if HEMI_ECOLE.get(ecole) != hemi: _refus(l, f"hémisphère {hemi} hors de l'école {ecole}"); return None
    vide = comb == "(vide)"
    if not vide and comb not in KB.COMBOS: _refus(l, f"combinaison inconnue « {comb} »"); return None
    rings = list(g["rings"]) if vide else _redit(g["rings"], comb, k[0], k[1])
    rings = [r[:5] if len(r) > 5 and r[5] == "SANS_MOT" else r for r in rings]
    attente = sans_mot(rings)
    if attente:             # règle 1 : un Impact plein hybride demande un mot d'action ; la forme attend son mot (décision du 21 novembre)
        imps = [r for r in rings if r[0] == "IMPACT"]
        for i in attente: EN_ATTENTE.append((k[0], k[1], l["type"], comb, i, imps[i][3]))
        return None
    n_imp = sum(1 for r in rings if r[0] == "IMPACT")
    ps = poles(l)
    if len(ps) != n_imp: _refus(l, f"{len(ps)} pôles pour {n_imp} cercles d'Impact"); return None
    opp = {i for i, p in enumerate(ps) if p != POLE_HEMI[hemi]}
    if opp != {int(x) for x in l["impacts_opposes"].split("|") if x.strip()}: _refus(l, f"Impacts opposés / pôles {ps}"); return None
    une_des_faces = any(x in g["label"].lower() for x in ("lumineu", "ténébreu"))
    if l["face"] and une_des_faces and POLE_HEMI[hemi] != {"lumineuse": "lumineux", "ténébreuse": "ténébreux"}[l["face"]]:
        _refus(l, f"face {l['face']} sous {hemi}"); return None
    if vide:
        core = SP.hyb(label=C.norm(ecole)); verb = f"{ecole} · {hemi} · combinaison vide"
        tete = [l["note"].replace("mention : ", "", 1)] if l["note"].startswith("mention : ") else []
    else:
        f_, a_, t_, e_ = KB.COMBOS[comb]
        core = SP.hyb(f=f_, a=a_, t=t_, e=e_, label=C.norm(ecole)); verb = f"{ecole} · {hemi} · {comb} ({KB.code(comb)})"
        tete = [f"Magie hybride, combinaison {comb} : l'élément en jeu."]
    notes = tete + [n for n in g["notes"] if n not in NOTES_RETIREES]
    nom = nom_hybride(g["label"], comb if not vide else "", plusieurs)
    CREEES.append((k[0], k[1], l["type"], comb, nom))
    return dict(g, fam="H", core=core, verb=verb, rings=rings, notes=notes, r0=66, label=nom, split=None,
                poles_impacts=tuple(ps) or None, regle_4b=True, element_par_defaut=False, cree_4b=(k[1], l["type"]))


def creer(g, k):
    """formes créées d'après la forme modèle g (rang d'origine k), pour les étapes atteintes ; à redessiner par l'appelant"""
    ls = [l for l in CREER.get(k, []) if l["type"] in types_actifs()]
    out = []
    for l in ls:
        if l["type"] in HYBRIDES:
            plusieurs = sum(1 for x in ls if x["type"] == l["type"] == "élément choisi") > 1
            nf = hybride(g, l, k, plusieurs)
            if nf is not None: out.append(nf)
        else:
            _refus(l, f"type « {l['type']} » pas encore traité")
    return out
