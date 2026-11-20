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

ETAPE = int(os.environ.get("PHASE4B_ETAPE", "2"))      # étapes de la phase 4b appliquées (0 ou 1 : aucune donnée)
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
