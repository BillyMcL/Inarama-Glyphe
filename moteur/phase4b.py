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

ETAPE = int(os.environ.get("PHASE4B_ETAPE", "8"))      # étapes de la phase 4b appliquées (0 ou 1 : aucune donnée)
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
# notes du modèle qui parlent du verbe ou de l'Arcane : pas reprises sur une forme hybride créée (décision du 21 novembre 2026)
NOTES_VERBE = ("Dégât de force : la force brute de Détruire, sans médium.",
               "Sept rayons de sept natures : aucun élément ne domine, l'Arcane les porte tous par la lumière.")
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
            cnt = tuple(el.count(e) for e in ELS)
            nom = next((n for n, c in KB.COMBOS.items() if tuple(c) == cnt), None)
            if el == units: cas = comb.lower()
            elif mono and set(el) == {units[0]}: cas = units[0]
            elif nom and C.norm(nom) in C.REDIT.get(comb, set()): cas = nom.lower()     # table REDIT du moteur (Éclair dit la foudre…)
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
        rd = rd.replace(f" ; satellites : les symboles de la combinaison {comb}", "").replace(" ; satellite : symbole du feu", "")
        if nom: rd = rd.replace(f" ; satellites : les symboles de la combinaison {nom}", "")
        rd = re.sub(r" ; satellites : symboles (?:du feu|de l'air|de la terre|de l'eau)(?:, (?:du feu|de l'air|de la terre|de l'eau))*", "", rd)
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
_B5 = os.path.join(P4B, "B5_mots_d_action.csv")
MOTS = {(l["cle"], int(l["rang_forme_modele"]), l["combinaison"], int(l["impact"])): l
        for l in (csv.DictReader(open(_B5, encoding="utf-8-sig"), delimiter=";") if os.path.exists(_B5) else [])}
MOTS_FAITS, MOTS_REFUS = [], []     # lignes de B5 appliquées ; (ligne, raison) refusées


def _mots_action(rings, l, k):
    """B5 : un cercle d'Impact en attente reçoit ses mots d'action et sa valeur (forme hybride seulement) ; les satellites
    sont gardés (sauf un satellite ajouté que la note demande) ; le début de la phrase est régénéré, la parenthèse gardée"""
    import convert as C, corrections as K, lint as LI
    imps = [j for j, r in enumerate(rings) if r[0] == "IMPACT"]
    out = list(rings)
    for i, j in enumerate(imps):
        m = MOTS.get((k[0], k[1], l["combinaison"], i))
        if m is None: continue
        r = rings[j]
        if r[3] != m["lecture_actuelle"]: MOTS_REFUS.append((m, f"lecture actuelle « {r[3]} »")); continue
        ws = m["mots"].split()
        hors = [w for w in ws if LI.MILLE_ET_UN is not None and w not in LI.MILLE_ET_UN]
        if hors: MOTS_REFUS.append((m, f"hors lexique : {hors}")); continue
        ws = [C.word(w) for w in ws]
        v = "plein" if m["valeur"] == "plein" else int(m["valeur"])
        sats = list(r[4]) if len(r) > 4 and r[4] else []
        if "IMPACT CLIMAT" in m["note"]:        # Plumes d'hiver : garde du climat, écrite comme les autres gardes du dépôt
            sats = C._resats(sats + [("SYM", 5, "IMPACT CLIMAT", {"crit": "IMPACT"})])
        with K._Accentue():                    # orthographe accentuée relevée dans les textes du moteur (comme en phase 4a)
            rd = K._tete("IMPACT", v, ws) + K.parenthese(r[3]) + K._lecture_sats(sats, k, ws)
        out[j] = (r[0], v, ws, rd, sats) if sats else (r[0], v, ws, rd)
        MOTS_FAITS.append((m, r[3], rd))
    return out


EN_ATTENTE = []                     # formes non créées faute de mot d'action : (cle, rang du modèle, type, combinaison, n° d'Impact, lecture)


# Décision du 21 novembre 2026 : oubli de B3 — ces trois faces ténébreuses sont d'Évocation (Galombar) ; leur Impact
# ténébreux est alors du côté de l'école (plus d'Impact opposé).
ECOLE_CORRIGEE = {("umbral-extraction", 0, "contre-sort (noyau vide)"): ("Évocation", "Galombar"),
                  ("umbral-graft", 0, "contre-sort (noyau vide)"): ("Évocation", "Galombar"),
                  ("shadow-siphon", 0, "contre-sort (noyau vide)"): ("Évocation", "Galombar")}

# B6 : relecture de formes d'Arcane modèles (et de leurs formes hybrides créées), décision du 21 novembre 2026 ;
# exception validée à la règle 5 : ces formes d'Arcane changent.
_B6 = os.path.join(P4B, "B6_relecture_formes.csv")
RELECTURE = _dd(list)
for _l in (csv.DictReader(open(_B6, encoding="utf-8-sig"), delimiter=";") if os.path.exists(_B6) else []):
    RELECTURE[(_l["cle"], int(_l["rang_forme_modele"]))].append(_l)
RELU_FAITS, RELU_REFUS = [], []


def relecture(g, k, hybrides):
    """B6 : les lignes « ET toutes les formes hybrides » (hybrides=True, avant la création) ou « seulement » (après) ;
    le cercle d'Impact prend mots et valeur, garde ses satellites (sauf ajout demandé), début de phrase régénéré,
    parenthèse gardée ; un cercle d'Impact ajouté si demandé"""
    import convert as C, corrections as K, lint as LI
    ls = [l for l in RELECTURE.get(k, []) if ("ET toutes" in l["applique_a"]) == hybrides]
    if not ls or ETAPE < 5: return g
    rings = list(g["rings"])
    for l in sorted(ls, key=lambda x: -int(x["impact"])):
        imps = [j for j, r in enumerate(rings) if r[0] == "IMPACT"]
        i = int(l["impact"])
        if g["fam"] != "A" or g["fr"] != l["sort"] or g["label"] != l["forme_modele"] or i >= len(imps):
            RELU_REFUS.append((l, f"forme « {g['fr']} [{g['label']}] » ({g['fam']}), {len(imps)} Impacts")); continue
        ws = l["mots"].split()
        hors = [w for w in ws if LI.MILLE_ET_UN is not None and w not in LI.MILLE_ET_UN]
        if hors: RELU_REFUS.append((l, f"hors lexique : {hors}")); continue
        ws = [C.word(w) for w in ws]
        v = "plein" if l["valeur"] == "plein" else int(l["valeur"])
        j = imps[i]; r = rings[j]
        sats = list(r[4]) if len(r) > 4 and r[4] else []
        if "IMPACT CLIMAT" in l["note"]:
            sats = C._resats(sats + [("SYM", 5, "IMPACT CLIMAT", {"crit": "IMPACT"})])
        par = K.parenthese(r[3])
        if "ajouter « 2d8 en moyenne »" in l["note"]:      # comme les autres blessures du dépôt : les dés en tête de la parenthèse
            par = " (2d8 en moyenne, " + par[2:] if par else " (2d8 en moyenne)"
        with K._Accentue():
            rd = K._tete("IMPACT", v, ws) + par + K._lecture_sats(sats, k, ws)
            nouveau = [(r[0], v, ws, rd, sats) if sats else (r[0], v, ws, rd)]
            if l["impact_a_ajouter"]:
                m = re.search(r"valeur (\d+), mot (\w+) \(([^)]*)\)", l["impact_a_ajouter"])
                if not m: RELU_REFUS.append((l, "cercle à ajouter illisible")); continue
                w2 = [C.word(m.group(2))]
                nouveau.append(("IMPACT", int(m.group(1)), w2, K._tete("IMPACT", int(m.group(1)), w2) + f" ({m.group(3)})"))
        rings[j:j + 1] = nouveau
        RELU_FAITS.append((k, i, hybrides, r[3], rd))
    return dict(g, rings=rings) if rings != list(g["rings"]) else g


def _poles_b6(ps, k, ecole_pole):
    """pôles des formes hybrides créées : colonne pole_hybride de B6, et le pôle de l'école pour un Impact ajouté"""
    ps = list(ps)
    for l in sorted((x for x in RELECTURE.get(k, []) if "ET toutes" in x["applique_a"]), key=lambda x: -int(x["impact"])):
        i = int(l["impact"])
        if l["pole_hybride"]: ps[i] = l["pole_hybride"]
        if l["impact_a_ajouter"]: ps.insert(i + 1, ecole_pole)
    return ps


def hybride(g, l, k, plusieurs):
    """une forme hybride créée d'après la forme modèle g (recette du prompt de la phase 4b)"""
    import convert as C, combos as KB
    if (k[0], k[1], l["type"]) in ECOLE_CORRIGEE:
        e_, h_ = ECOLE_CORRIGEE[(k[0], k[1], l["type"])]
        ps_ = poles(l)
        l = dict(l, ecole=e_, hemisphere=h_, impacts_opposes=" | ".join(str(i) for i, p in enumerate(ps_) if p != POLE_HEMI[h_]))
    comb, ecole, hemi = l["combinaison"], l["ecole"], l["hemisphere"]
    if HEMI_ECOLE.get(ecole) != hemi: _refus(l, f"hémisphère {hemi} hors de l'école {ecole}"); return None
    vide = comb == "(vide)"
    if not vide and comb not in KB.COMBOS: _refus(l, f"combinaison inconnue « {comb} »"); return None
    rings = list(g["rings"]) if vide else _redit(g["rings"], comb, k[0], k[1])
    rings = [r[:5] if len(r) > 5 and r[5] == "SANS_MOT" else r for r in rings]
    rings = _mots_action(rings, l, k)
    attente = sans_mot(rings)
    if attente:             # règle 1 : un Impact plein hybride demande un mot d'action ; la forme attend son mot (décision du 21 novembre)
        imps = [r for r in rings if r[0] == "IMPACT"]
        for i in attente: EN_ATTENTE.append((k[0], k[1], l["type"], comb, i, imps[i][3]))
        return None
    n_imp = sum(1 for r in rings if r[0] == "IMPACT")
    ps = poles(l)
    opp = {i for i, p in enumerate(ps) if p != POLE_HEMI[hemi]}
    if opp != {int(x) for x in l["impacts_opposes"].split("|") if x.strip()}: _refus(l, f"Impacts opposés / pôles {ps}"); return None
    ps = _poles_b6(ps, k, POLE_HEMI[hemi])
    if len(ps) != n_imp: _refus(l, f"{len(ps)} pôles pour {n_imp} cercles d'Impact"); return None
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
    notes = tete + [n for n in g["notes"] if n not in NOTES_RETIREES and n not in NOTES_VERBE]
    nom = nom_hybride(g["label"], comb if not vide else "", plusieurs)
    CREEES.append((k[0], k[1], l["type"], comb, nom))
    return dict(g, fam="H", core=core, verb=verb, rings=rings, notes=notes, r0=66, label=nom, split=None,
                poles_impacts=tuple(ps) or None, regle_4b=True, element_par_defaut=False, cree_4b=(k[1], l["type"]))


def nom_famille(modele, famille):
    """nom d'une forme créée d'une autre famille (« Art rare », « Forme arcane »), selon l'usage du dépôt"""
    for avant in ("Forme arcane", "Art rare"):
        if modele == avant: return famille
        if modele.startswith(avant + " — "): return famille + modele[len(avant):]
    return famille + " — " + modele


def _verbe_de(nom):
    import convert as C
    return next(((vk, vn) for (vk, vn), n in C.VERBS.items() if n == nom), None)


def art_rare(g, l, k):
    """étape 6 : une forme d'art rare d'après la forme d'Arcane modèle — Noyau du moteur (verbe d'Arcane cerné des quatre
    éléments, mot de l'art), mêmes cercles et phrases, répartition 50/50 du moteur"""
    import convert as C
    v = _verbe_de(l["verbe"])
    if g["fam"] != "A" or g["core"][0] != "verb" or v is None or (g["core"][1], bool(g["core"][2])) != v:
        _refus(l, f"modèle « {g['verb']} » / verbe « {l['verbe']} »"); return None
    vk, vn = v; art = l["art"]
    notes = [f"Art rare ({art}) : verbe arcanique au cœur, quatre éléments, équilibre astral 50/50."] + [n for n in g["notes"] if n not in NOTES_RETIREES]
    nom = nom_famille(g["label"], "Art rare")
    CREEES.append((k[0], k[1], l["type"], art, nom))
    return dict(g, fam="R", core=SP.chrono(vk, vn, art.upper()), r0=66, split=None, notes=notes, label=nom,
                verb=f"{art.capitalize()} · {C.VERBS[(vk, vn)]} ({C.VERB_GROUP[vk]} {'−' if vn else '+'}) cerné des quatre éléments",
                poles_impacts=None, regle_4b=False, element_par_defaut=False, cree_4b=(k[1], l["type"]))


def sans_temps(f):
    """le mot « temps » retiré des cercles d'Impact (règle du moteur _sans_mot pour la phrase)"""
    import convert as C
    rings = [(r[0], r[1], [w for w in r[2] if w != "TEMPS"], C._sans_mot(r[3], "TEMPS"), *r[4:]) if r[0] == "IMPACT" and "TEMPS" in r[2] else r
             for r in f["rings"]]
    return dict(f, rings=rings)


def arcane_nouvelle(g, l, k):
    """étape 6 : copie en Arcane de la forme d'art rare, qui reste ; le mot « temps » de l'Impact est retiré"""
    import convert as C
    c = g["core"]
    if g["fam"] != "R" or c[0] != "chrono" or C.VERBS[(c[1], bool(c[2]))] != l["verbe"]:
        _refus(l, f"modèle « {g['verb']} »"); return None
    vk, vn = c[1], bool(c[2])
    notes = ["Arcane : aucun élément en jeu, un verbe suffit." if n.startswith("Art rare (") else n for n in g["notes"]]
    nom = nom_famille(g["label"], "Forme arcane")
    CREEES.append((k[0], k[1], l["type"], "", nom))
    return sans_temps(dict(g, fam="A", core=SP.verb(vk, vn), pol="down" if vn else "up", split=None, r0=34, notes=notes, label=nom,
                           verb=f"{C.VERBS[(vk, vn)]} · {C.VERB_GROUP[vk].lower()} {'−' if vn else '+'}",
                           poles_impacts=None, regle_4b=False, element_par_defaut=False, cree_4b=(k[1], l["type"])))


def creer(g, k):
    """formes créées d'après la forme modèle g (rang d'origine k), pour les étapes atteintes ; à redessiner par l'appelant"""
    ls = [l for l in CREER.get(k, []) if l["type"] in types_actifs()
          # le modèle de ces lignes est la forme d'Arcane créée à l'étape 6 (Lenteur) : elles attendent l'étape 6
          and not (l["note"].startswith("modèle : la forme d'Arcane de cette édition") and ETAPE < 6)]
    out, arcane = [], None
    for l in sorted(ls, key=lambda x: x["type"] != "forme d'Arcane nouvelle"):      # la forme d'Arcane nouvelle d'abord
        if l["type"] in HYBRIDES:
            plusieurs = sum(1 for x in ls if x["type"] == l["type"] == "élément choisi") > 1
            modele = g
            if l["note"].startswith("modèle : la forme d'Arcane de cette édition"):
                # Lenteur : la forme d'Arcane de l'édition (créée ici, ou convertie à l'étape 2), sans le mot « temps »
                base = arcane if arcane is not None else (g if g["fam"] == "A" else None)
                if base is None: _refus(l, "pas de forme d'Arcane de cette édition"); continue
                modele = sans_temps(base)
            nf = hybride(modele, l, k, plusieurs)
            if nf is not None: out.append(nf)
        elif l["type"] == "art rare":
            nf = art_rare(g, l, k)
            if nf is not None: out.append(nf)
        elif l["type"] == "forme d'Arcane nouvelle":
            arcane = arcane_nouvelle(g, l, k)
            if arcane is not None: out.append(arcane)
        else:
            _refus(l, f"type « {l['type']} » non traité")
    return out


# ---------- étape 7 : les formes nouvelles (B4_formes_nouvelles.json) ----------
import json as _json
_B4 = os.path.join(P4B, "B4_formes_nouvelles.json")
NOUVELLES = _dd(list)               # (cle, rang d'origine du modèle) → formes nouvelles, dans l'ordre du fichier
for _b in (_json.load(open(_B4, encoding="utf-8"))["formes"] if os.path.exists(_B4) else []):
    NOUVELLES[(_b["cle"], int(_b["rang_forme_modele"]))].append(_b)
B4_FAITES, B4_REFUS = [], []        # (cle, rang, nom) ; (forme, raison)
PARENTHESES_ENTIERES = []           # cercles de B4 dont le champ « parenthese » était la phrase entière
VERBE_PORTAIL = "Invoquer"          # Portail « Appel d'un être » : verbe proposé ; Lier s'il donne un glyphe en double


def b4(k):
    return NOUVELLES.get(k, []) if ETAPE >= 7 else []


def _suffixe(modele):
    """la précision d'édition d'un nom de forme (« — version 3.5 »), pour que deux formes d'un sort n'aient pas le même nom"""
    m = re.search(r"( — version .+)$", modele)
    return m.group(1) if m else ""


def renomme(g, b):
    """action « ajouter » : la forme modèle prend le nom donné (précision d'édition gardée)"""
    return dict(g, label=b["forme_modele_renommee"] + _suffixe(g["label"])) if b.get("forme_modele_renommee") else g


def _cercles_b4(g, b, k):
    """les cercles de la forme nouvelle (même format que l'état cible de la phase 4a) : inchangé = recopié, phrase comprise ;
    modifié = début régénéré et parenthèse donnée, sinon celle d'origine ; ajouté = phrase générée avec la parenthèse"""
    import corrections as K
    cs = [dict(c, satellites=[dict(s, valeur=None if s["valeur"] == "" else s["valeur"]) for s in c["satellites"]]) for c in b["cercles"]]
    try:
        rings, _, _ = K._cercles(g, {"cercles": cs})
    except StopIteration:
        B4_REFUS.append((b, "un cercle « inchangé » ne se retrouve pas dans la forme modèle")); return None
    out = []
    with K._Accentue():
        for r, c in zip(rings, cs):
            if c["etat"] == "inchangé":
                out.append(r); continue
            sats = list(r[4]) if len(r) > 4 and r[4] else []
            tete = K._tete(r[0], r[1], r[2])
            if c.get("parenthese", "").startswith(tete + " ("):        # B4 donne parfois la phrase entière : n'en garder que la parenthèse
                PARENTHESES_ENTIERES.append((b["cle"], b["nom_de_la_forme"], r[0], c["parenthese"])); par = K.parenthese(c["parenthese"])
            elif c.get("parenthese"): par = f" ({c['parenthese']})"
            elif c["etat"] == "modifié": par = K.parenthese(c.get("lecture_d_origine") or "")
            else: par = ""
            rd = K._tete(r[0], r[1], r[2]) + par + K._lecture_sats(sats, k, r[2])
            out.append((r[0], r[1], r[2], rd, sats) if sats else (r[0], r[1], r[2], rd))
    return out


def nouvelle(g, b, k):
    """une forme nouvelle de B4, d'après la forme modèle g"""
    import convert as C, combos as KB, lint as LI
    rings = _cercles_b4(g, b, k)
    if rings is None: return None
    mots = []
    for r in rings:
        mots += list(r[2])
        for s in (r[4] if len(r) > 4 and r[4] else []):
            if len(s) > 2 and s[2]: mots += [x for x in str(s[2]).split() if x not in SP.NAMES]
    hors = sorted({w for w in mots if LI.MILLE_ET_UN is not None and w not in LI.MILLE_ET_UN})
    if hors:
        B4_REFUS.append((b, f"hors lexique : {hors}")); return None
    if b["niveau"] != g["level"]:
        B4_REFUS.append((b, f"niveau {b['niveau']} / modèle {g['level']}")); return None
    nom = b["nom_de_la_forme"] + _suffixe(g["label"])
    base = dict(g, rings=rings, label=nom, poles_impacts=None, regle_4b=False, element_par_defaut=False,
                cree_4b=(k[1], "forme nouvelle (B4)"))
    fam = b["famille"]
    if fam == "Arcane":
        v = _verbe_de(b["verbe"])
        if v is None:
            B4_REFUS.append((b, f"verbe « {b['verbe']} »")); return None
        vk, vn = v
        notes = ["Arcane : aucun élément en jeu, un verbe suffit." if n.startswith("Art rare (") else n for n in g["notes"]]
        f = dict(base, fam="A", core=SP.verb(vk, vn), pol="down" if vn else "up", split=None, r0=34, notes=notes,
                 verb=f"{C.VERBS[(vk, vn)]} · {C.VERB_GROUP[vk].lower()} {'−' if vn else '+'}")
    elif fam == "Art rare":
        if g["core"][0] != "chrono":
            B4_REFUS.append((b, "modèle sans Noyau d'art rare")); return None
        vk, vn = _verbe_de(VERBE_PORTAIL if b["cle"] == "gate" else b["verbe"])
        art = g["core"][4]
        f = dict(base, fam="R", core=SP.chrono(vk, vn, art), r0=66, split=None,
                 verb=f"{art.capitalize()} · {C.VERBS[(vk, vn)]} ({C.VERB_GROUP[vk]} {'−' if vn else '+'}) cerné des quatre éléments")
    else:       # Magie hybride sans forme d'Arcane
        comb, ecole = b["combinaison"], b["ecole"]
        hemi = HEMI_ECOLE[ecole]
        n_imp = sum(1 for r in rings if r[0] == "IMPACT")
        if b["impacts_poles"].strip() in ("tous lumineux", "tous ténébreux"): ps = [b["impacts_poles"].split()[1]] * n_imp
        else: ps = [x.split(":")[1].strip() for x in b["impacts_poles"].split("|")]
        if len(ps) != n_imp:
            B4_REFUS.append((b, f"{len(ps)} pôles pour {n_imp} Impacts")); return None
        f_, a_, t_, e_ = KB.COMBOS[comb]
        if g["fam"] == "H": notes = g["notes"]
        else: notes = [f"Magie hybride, combinaison {comb} : l'élément en jeu."] + [n for n in g["notes"] if n not in NOTES_RETIREES]
        f = dict(base, fam="H", core=SP.hyb(f=f_, a=a_, t=t_, e=e_, label=C.norm(ecole)), r0=66, split=None, notes=notes,
                 verb=f"{ecole} · {hemi} · {comb} ({KB.code(comb)})", poles_impacts=tuple(ps), regle_4b=True)
    B4_FAITES.append((k[0], k[1], nom))
    CREEES.append((k[0], k[1], "forme nouvelle (B4)", fam, nom))
    return f


def jumelles(nf, k):
    """les jumelles hybrides d'une forme nouvelle d'Arcane, d'après les lignes B3 de sa forme modèle"""
    ls = [l for l in CREER.get(k, []) if l["type"] in HYBRIDES and l["type"] in types_actifs()]
    out = []
    for l in ls:
        plusieurs = sum(1 for x in ls if x["type"] == l["type"] == "élément choisi") > 1
        h = hybride(nf, l, k, plusieurs)
        if h is not None: out.append(dict(h, cree_4b=(k[1], "jumelle d'une forme nouvelle (B4)")))
    return out


# ---------- étape 8 : notes de famille (décision du 21 novembre 2026) ----------
NOTE_PAS_HYBRIDE = "Pas de forme hybride : aucune combinaison naturelle ne porte cet effet."
NOTE_PAS_ARCANE = "Pas de forme arcane : le sort façonne la matière elle-même, que l'Arcane ne touche pas."
NOTES_FAITES = {"pas_hybride_retiree": [], "pas_arcane_retiree": []}     # (cle, nom de la forme)


def notes_famille(cle, formes):
    """une note « Pas de forme hybride… » (forme d'Arcane) ou « Pas de forme arcane… » (forme hybride) ne reste que là où elle
    est vraie : elle est retirée quand le sort a maintenant une forme de l'autre famille. Seules les notes changent."""
    if ETAPE < 8: return formes
    fams = {f["fam"] for f in formes}
    out = []
    for f in formes:
        if f["fam"] == "A" and "H" in fams and NOTE_PAS_HYBRIDE in f["notes"]:
            f = dict(f, notes=[n for n in f["notes"] if n != NOTE_PAS_HYBRIDE]); NOTES_FAITES["pas_hybride_retiree"].append((cle, f["label"]))
        elif f["fam"] == "H" and "A" in fams and NOTE_PAS_ARCANE in f["notes"]:
            f = dict(f, notes=[n for n in f["notes"] if n != NOTE_PAS_ARCANE]); NOTES_FAITES["pas_arcane_retiree"].append((cle, f["label"]))
        out.append(f)
    return out


# ---------- compléments du 21 novembre 2026 ----------
# Quatre sorts oubliés par les fichiers (homonymes d'un autre sort) : leur forme hybride, recette habituelle, d'après leur forme
# d'Arcane (rang d'origine 0). Averse et Isolement : l'Impact suit l'école.
SUPPLEMENTS = [
    dict(cle="drench", rang=0, combinaison="Eau", ecole="Invocation", poles=["lumineux"]),
    dict(cle="isolation", rang=0, combinaison="Brume", ecole="Illusion", poles=["lumineux"]),
    dict(cle="boiling-blood", rang=0, combinaison="Sang", ecole="Transmutation", poles=["ténébreux"]),
    dict(cle="blood-boil", rang=0, combinaison="Sang", ecole="Nécromancie", poles=["ténébreux", "ténébreux"]),
]
for _s in SUPPLEMENTS:
    _h = HEMI_ECOLE[_s["ecole"]]
    CREER[(_s["cle"], _s["rang"])].append(dict(
        statut="à créer", type="combinaison fixe", cle=_s["cle"], rang_forme_modele=str(_s["rang"]), combinaison=_s["combinaison"],
        ecole=_s["ecole"], hemisphere=_h, face="", art="", verbe="", note="complément du 21 novembre 2026 (sort oublié par B3)",
        impacts_poles=" | ".join(f"{i}:{p}" for i, p in enumerate(_s["poles"])),
        impacts_opposes=" | ".join(str(i) for i, p in enumerate(_s["poles"]) if p != POLE_HEMI[_h]), raisons=""))
