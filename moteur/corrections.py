"""Couche de corrections de la phase 4a.

Elle s'applique en toute fin de construction, sur les formes déjà construites
(cercles et phrases de lecture compris), juste après convert.build_forms et
avant le contrôle d'unicité de site.py. Les corrections décidées sont dans
donnees/phase4/ ; ce module ne décide rien.

Une forme se retrouve par sa clé de sort et son rang : sa position parmi les
formes de ce sort, à partir de 0, Elden Ring exclu (ses sorts ont leurs propres
clés « er-… » et ne sont jamais touchés).

Étape 1 : à vide. Le module lit l'état cible, retrouve chaque forme et compare
« origine » aux cercles actuels ; il ne change rien.

    python corrections.py    → compte rendu de la comparaison
"""
import os, json

D = os.path.dirname(os.path.abspath(__file__))
P4 = os.path.join(D, "..", "donnees", "phase4")
CIBLE = json.load(open(os.path.join(P4, "A_etat_cible_final.json"), encoding="utf-8"))["formes"]
PAR_CLE = {(x["cle"], x["rang"]): x for x in CIBLE}

_vues = {}        # (cle, rang) → (forme construite, cercles actuels) pour chaque forme de l'état cible retrouvée


def est_elden_ring(forme):
    return forme["dnd"].startswith("Elden Ring")


def _norm(x):
    """une valeur comparable à celle du fichier JSON (tuples en listes)"""
    return json.loads(json.dumps(x, ensure_ascii=False, default=repr))


def cercles_actuels(forme):
    """les cercles d'une forme construite, comme le fichier les écrit : [cercle, valeur, mots]"""
    return [[r[0], _norm(r[1]), _norm(list(r[2]))] for r in forme["rings"]]


def appliquer(cle, formes):
    """reçoit les formes construites d'un sort et les rend corrigées (étape 1 : inchangées)"""
    rang = 0
    for f in formes:
        if est_elden_ring(f):
            continue
        if (cle, rang) in PAR_CLE:
            _vues[(cle, rang)] = (f, cercles_actuels(f))
        rang += 1
    return formes


def bilan():
    """retrouvées, origines conformes, et le détail de chaque écart"""
    introuvables = [k for k in PAR_CLE if k not in _vues]
    ecarts = []
    for k, x in PAR_CLE.items():
        if k not in _vues:
            continue
        f, actuels = _vues[k]
        controle = [c for c, a, b in (("sort", x["sort"], f["fr"]), ("forme", x["forme"], f["label"]), ("niveau", x["niveau"], f["level"])) if a != b]
        if _norm(x["origine"]) != actuels or controle:
            ecarts.append(dict(cle=k[0], rang=k[1], sort=x["sort"], forme=x["forme"], controle=controle,
                               attendu=x["origine"], actuel=actuels))
    return dict(total=len(PAR_CLE), retrouvees=len(_vues), introuvables=introuvables,
                conformes=len(_vues) - len(ecarts), ecarts=ecarts)


if __name__ == "__main__":
    import sys
    sys.path.insert(0, D)
    import convert as C
    from fiches import FICHES
    for k, fi in FICHES.items():
        appliquer(k, C.build_forms(k, fi))
    b = bilan()
    print(f"état cible : {b['total']} formes ; retrouvées {b['retrouvees']} ; introuvables {len(b['introuvables'])} ; "
          f"origine conforme {b['conformes']} ; écarts {len(b['ecarts'])}")
    for k in b["introuvables"]:
        print("  introuvable :", k)
    for e in b["ecarts"]:
        print(f"  écart : {e['cle']} rang {e['rang']} · {e['sort']} [{e['forme']}]" + (f" · contrôle {e['controle']}" if e["controle"] else ""))
        print("     attendu :", json.dumps(e["attendu"], ensure_ascii=False))
        print("     actuel  :", json.dumps(e["actuel"], ensure_ascii=False))
