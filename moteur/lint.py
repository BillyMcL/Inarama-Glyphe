# -*- coding: utf-8 -*-
"""Contrôle des glyphes : les règles de l'audit du 14 novembre. Une forme qui en enfreint une bloque la construction stricte."""
import collections, json, os
import lexique as L
# Le lexique fermé : les mille et un mots de l'Arcane. Toute annotation (d'un cercle ou d'un satellite) doit en être.
_LX = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "donnees", "lexique_1001.json")
MILLE_ET_UN = set(json.load(open(_LX, encoding="utf-8"))) if os.path.exists(_LX) else None
CRITERES = {"CIBLE", "FORME", "AMPLEUR", "DUREE", "LOCALISATION", "CONDITION", "IMPACT", "QUANTITE", "COMPOSANTE", "INTERACTION", "COSMETIQUE"}

def lint(spells):
    """spells : [{fr, forms:[{label, fam, verb, rings}]}] → liste de (règle, sort, forme, détail)"""
    out = []
    for sp in spells:
        for fm in sp["forms"]:
            if MILLE_ET_UN is not None:
                for r in fm["rings"]:
                    mots = list(r[2])
                    for x in (r[4] if len(r) > 4 and r[4] else []):
                        if len(x) > 2 and x[2]: mots += [w for w in str(x[2]).split() if w not in CRITERES]
                    for w in mots:
                        if w not in MILLE_ET_UN: out.append(("lexique", sp["fr"], fm["label"], f"« {w.lower()} » n'est pas l'un des mille et un mots"))
            if "grimoire" in " ".join(fm.get("notes") or []).lower() and fm["notes"][0].startswith("Version du grimoire"): continue
            if fm.get("combinee"): out += combinee(sp, fm)        # forme combinée (B12) : ses règles propres, puis les règles communes
            verbe = fm["verb"].split(" ·")[0]
            def err(regle, detail=""): out.append((regle, sp["fr"], fm["label"], detail))
            R = collections.defaultdict(list)
            for r in fm["rings"]: R[r[0]].append(r)
            sats = lambda r: [(x[1], x[2] if len(x) > 2 else "") for x in (r[4] if len(r) > 4 and r[4] else [])]
            if not R["IMPACT"] and not R["COSMETIQUE"]: err("muet", "ni Impact ni Cosmétique")
            if not R["CIBLE"] and fm["fam"] == "A" and verbe not in ("Créer", "Invoquer"): err("règle 6", "pas de cercle Cible")
            for r in R["CIBLE"]:
                for w in r[2]:
                    if w not in L.CIBLE_MOTS: err("règle 5", f"« {w.lower()} » n'est pas un mot de Cible déclaré au lexique")
            for r in R["IMPACT"]:
                ss = sats(r); mots = [l for v, l in ss if not isinstance(v, tuple)]
                elems = [v for v, l in ss if isinstance(v, tuple) and v[1] in ("feu", "air", "terre", "eau")]
                if fm["fam"] == "H" and r[1] == "plein" and not r[2] and not any(mots): err("règle 1", "hybride : Impact plein sans mot d'action")
                # (une part de la vie de la cible — « vie » avec un satellite « fractionné » — est une mesure, non un soin)
                # exception (chantier d'écriture 2, 28 novembre 2026, décision de l'utilisateur) : la « vie » qui porte sa propre Cible
                # alliée en satellite (Cible 2) soigne un autre que la cible du verbe qui nuit (Chaleur guérisseuse PF1) ; élargie
                # (chantier 2, passe 3, décision de l'utilisateur) : elle joue dès que la vie porte sa propre Cible, soi (1) ou un allié (2),
                # celle qui reçoit le soin, autre que celle que le verbe blesse (Appel du sang PF2, Brise légère PF2 forme arcane)
                allie = any(v in (1, 2) and (l or "").split()[:1] == ["CIBLE"] for v, l in ss)
                if r[1] != "plein" and r[2][:1] == ["VIE"] and verbe in L.VERBES_NUISIBLES and not any("FRACTIONNE" in l for l in mots) and not allie: err("règle 3", "« vie » chiffrée sous un verbe qui nuit")
                if len(elems) > 4: err("règle 4", f"{len(elems)} symboles d'éléments sur un seul Impact")
                degre = bool(r[2]) and r[2][0] in L.DEGRES        # premier mot de degré : un degré, pas une mesure (phase 4a)
                # un mot placé juste après « contre » dit ce dont on se garde, pas une mesure (chantier « contre », 22 novembre 2026)
                gardes = {r[2][i + 1] for i, w in enumerate(r[2][:-1]) if w == "CONTRE"}
                mesures = {w for w in r[2] if w not in gardes} & L.MESURES
                if r[1] != "plein" and mesures and not set(r[2]) & L.UNITES and not any("FRACTIONNE" in l for l in mots) and not degre:
                    err("règle 7", "mesure sans unité : " + " · ".join(w.lower() for w in r[2]))
                for v, l in ss:
                    if not isinstance(v, tuple) and not l: err("satellite", "satellite d'Impact sans annotation")
                    if v == "plein" and l in ("LUMINEUX", "TENEBREUX"): err("satellite", "face écrite en mot au lieu du symbole")
            for r in R["COSMETIQUE"]:
                if "ETEINT" in r[2] and verbe == "Purifier": err("règle 2", "« sens éteint » sur un sort qui guérit")
                if r[1] == "plein" and "SENS" not in r[2]: err("cosmétique", "ancien format")
    return out

RANGS = ["CIBLE", "FORME", "AMPLEUR", "DUREE", "LOCALISATION", "CONDITION", "IMPACT", "QUANTITE", "COMPOSANTE", "INTERACTION", "COSMETIQUE"]
def combinee(sp, fm):
    """forme combinée (B12, 22 novembre 2026) : au moins deux Noyaux, chacun d'une combinaison connue ; le nom de l'école (annotation
    du cercle d'École) est l'un des mille et un mots ; dans chaque Noyau et dans les cercles communs, l'ordre habituel des cercles ;
    la Durée est toujours commune ; tous les cercles (Noyaux et communs) sont ceux que contrôlent les règles communes."""
    import combos as KB, convert as C
    out = []
    def err(detail): out.append(("combinée", sp["fr"], fm["label"], detail))
    cb = fm["combinee"]
    if len(cb["noyaux"]) < 2: err(f"{len(cb['noyaux'])} Noyau(x)")
    for n in cb["noyaux"]:
        if n["combinaison"] not in KB.COMBOS: err(f"combinaison inconnue « {n['combinaison']} »")
        if any(r[0] == "DUREE" for r in n["cercles"]): err(f"Durée propre au Noyau {n['combinaison']}")
    for nom, rs in [(f"Noyau {n['combinaison']}", n["cercles"]) for n in cb["noyaux"]] + [("cercles communs", cb["communs"])]:
        rg = [RANGS.index(r[0]) for r in rs]
        if rg != sorted(rg): err(f"{nom} : cercles hors de l'ordre habituel")
    if MILLE_ET_UN is not None:
        for w in (C.norm(cb["ecole"]),):
            if w not in MILLE_ET_UN: err(f"« {w.lower()} » (cercle d'École) n'est pas l'un des mille et un mots")
    tous = [r for n in cb["noyaux"] for r in n["cercles"]] + list(cb["communs"])
    if [tuple(map(repr, r[:3])) for r in tous] != [tuple(map(repr, r[:3])) for r in fm["rings"]]: err("cercles de la forme et des Noyaux différents")
    return out

def rapport(errs):
    c = collections.Counter(e[0] for e in errs)
    lignes = [f"{n:4d}  {r}" for r, n in sorted(c.items())]
    for e in errs[:40]: lignes.append(f"   [{e[0]}] {e[1]} — {e[2]} : {e[3]}")
    return "\n".join(lignes)
