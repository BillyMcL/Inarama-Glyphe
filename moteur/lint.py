# -*- coding: utf-8 -*-
"""Contrôle des glyphes : les règles de l'audit du 14 novembre. Une forme qui en enfreint une bloque la construction stricte."""
import collections
import lexique as L

def lint(spells):
    """spells : [{fr, forms:[{label, fam, verb, rings}]}] → liste de (règle, sort, forme, détail)"""
    out = []
    for sp in spells:
        for fm in sp["forms"]:
            if "grimoire" in " ".join(fm.get("notes") or []).lower() and fm["notes"][0].startswith("Version du grimoire"): continue
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
                if r[1] != "plein" and "VIE" in r[2] and verbe in L.VERBES_NUISIBLES: err("règle 3", "« vie » chiffrée sous un verbe qui nuit")
                if len(elems) > 4: err("règle 4", f"{len(elems)} symboles d'éléments sur un seul Impact")
                if r[1] != "plein" and set(r[2]) & L.MESURES and not set(r[2]) & L.UNITES and not any("FRACTIONNE" in l for l in mots):
                    err("règle 7", "mesure sans unité : " + " · ".join(w.lower() for w in r[2]))
                for v, l in ss:
                    if not isinstance(v, tuple) and not l: err("satellite", "satellite d'Impact sans annotation")
                    if v == "plein" and l in ("LUMINEUX", "TENEBREUX"): err("satellite", "face écrite en mot au lieu du symbole")
            for r in R["COSMETIQUE"]:
                if "ETEINT" in r[2] and verbe == "Purifier": err("règle 2", "« sens éteint » sur un sort qui guérit")
                if r[1] == "plein" and "SENS" not in r[2]: err("cosmétique", "ancien format")
    return out

def rapport(errs):
    c = collections.Counter(e[0] for e in errs)
    lignes = [f"{n:4d}  {r}" for r, n in sorted(c.items())]
    for e in errs[:40]: lignes.append(f"   [{e[0]}] {e[1]} — {e[2]} : {e[3]}")
    return "\n".join(lignes)
