"""Couche de corrections de la phase 4a.

Elle s'applique en toute fin de construction, sur les formes déjà construites
(cercles et phrases de lecture compris), juste après convert.build_forms et
avant le contrôle d'unicité de site.py. Les corrections décidées sont dans
donnees/phase4/ ; ce module ne décide rien.

Une forme se retrouve par sa clé de sort et son rang : sa position parmi les
formes de ce sort, à partir de 0, Elden Ring exclu (ses sorts ont leurs propres
clés « er-… » et ne sont jamais touchés).

Étape 1 : le module lit l'état cible, retrouve chaque forme et compare
« origine » aux cercles actuels. Une forme dont l'origine ne correspond pas
n'est pas touchée.

Étape 2 : pour chaque forme retrouvée, la liste « cercles » remplace tous les
cercles, dans l'ordre donné. Un cercle « inchangé » reprend tel quel le cercle
actuel (phrase et satellites compris). Un cercle « modifié » garde pour
l'instant sa « lecture_d_origine », un cercle « ajouté » n'a pas encore de
phrase : les phrases viennent à l'étape 3. La répartition lumineux/ténébreux
des formes hybrides et des arts rares est recalculée par la règle du moteur
(split_hybrid, split_rare), puis le glyphe est redessiné (spells.build).

    python corrections.py    → compte rendu
"""
import os, json
import spells as SP

D = os.path.dirname(os.path.abspath(__file__))
P4 = os.path.join(D, "..", "donnees", "phase4")
CIBLE = json.load(open(os.path.join(P4, "A_etat_cible_final.json"), encoding="utf-8"))["formes"]
PAR_CLE = {(x["cle"], x["rang"]): x for x in CIBLE}

_vues = {}        # (cle, rang) → (forme construite, cercles actuels) pour chaque forme de l'état cible retrouvée
_faites = {}      # (cle, rang) → nombre de cercles changés (modifiés + ajoutés + retirés)


def est_elden_ring(forme):
    return forme["dnd"].startswith("Elden Ring")


def _norm(x):
    """une valeur comparable à celle du fichier JSON (tuples en listes)"""
    return json.loads(json.dumps(x, ensure_ascii=False, default=repr))


def cercles_actuels(forme):
    """les cercles d'une forme construite, comme le fichier les écrit : [cercle, valeur, mots]"""
    return [[r[0], _norm(r[1]), _norm(list(r[2]))] for r in forme["rings"]]


def satellite_moteur(s):
    """un satellite du fichier {position, valeur, texte, options} → le tuple du moteur (position, valeur[, texte[, options]])"""
    v = s["valeur"]
    if isinstance(v, dict) and "sym" in v:
        v = ("sym", v["sym"])
    t = (s["position"], v, s["texte"], s["options"])
    if not s["options"]:
        t = t[:3]
        if not s["texte"] and not isinstance(v, tuple):
            t = t[:2]
    return t


def repartition(f, crits):
    """la répartition des cercles entre les deux pôles, par la règle du moteur"""
    import convert as C
    if f["fam"] == "H":
        return C.split_hybrid(crits, "H" if "Hodolin" in f["verb"] else "G", f["level"])
    if f["fam"] == "R":
        return C.split_rare(crits)
    return f["split"]


CRITERES = {"CIBLE", "FORME", "AMPLEUR", "DUREE", "LOCALISATION", "CONDITION", "IMPACT", "QUANTITE", "COMPOSANTE", "INTERACTION", "COSMETIQUE"}


def _transcrire(c):
    """les mots d'un cercle passent par convert.word, comme ceux d'une fiche : transcription en Alde pour le dessin.
    Cela n'ajoute rien au lexique fermé (donnees/lexique_1001.json) : un mot qui n'en est pas est signalé par lint."""
    import convert as C
    for w in c["mots"]:
        C.word(w)
    for s in c["satellites"]:
        for w in s["texte"].split():
            if w not in CRITERES:
                C.word(w)


def _cercles(f, x):
    """étape 2 : les cercles de l'état cible, dans l'ordre ; renvoie (cercles, nombre de cercles changés)"""
    restants = list(f["rings"])
    out, changes = [], 0
    for c in x["cercles"]:
        if c["etat"] == "inchangé":
            r = next(r for r in restants if r[0] == c["cercle"] and _norm(r[1]) == c["valeur"] and _norm(list(r[2])) == c["mots"])
            restants.remove(r)
            out.append(r)
            continue
        changes += 1
        _transcrire(c)
        lecture = c["lecture_d_origine"] if c["etat"] == "modifié" else ""
        out.append((c["cercle"], c["valeur"], list(c["mots"]), lecture, [satellite_moteur(s) for s in c["satellites"]]))
    retires = len(restants) - sum(c["etat"] == "modifié" for c in x["cercles"])     # un cercle modifié remplace un cercle actuel
    return out, changes + max(0, retires), len(restants)


def _redessine(f, rings):
    crits = list(dict.fromkeys(r[0] for r in rings))
    split = repartition(f, crits)
    svg, rows = SP.build(f["core"], f["pol"], rings, f["r0"], split, officiants=f["officiants"])
    return dict(f, rings=rings, split=split, svg=svg, rows=rows, bsplit=SP.PART[0])


def appliquer(cle, formes):
    """reçoit les formes construites d'un sort et les rend corrigées"""
    rang, out = 0, []
    for f in formes:
        if est_elden_ring(f):
            out.append(f)
            continue
        k = (cle, rang)
        rang += 1
        x = PAR_CLE.get(k)
        if x is None:
            out.append(f)
            continue
        _vues[k] = (f, cercles_actuels(f))
        if _norm(x["origine"]) != cercles_actuels(f):
            out.append(f)          # l'origine ne correspond pas : ne pas appliquer (signalé par bilan())
            continue
        rings, n, _ = _cercles(f, x)
        _faites[k] = n
        out.append(_redessine(f, rings))
    return out


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
    print(f"étape 2 : {len(_faites)} formes recevant leurs cercles ; {sum(_faites.values())} cercles changés")
    for k in b["introuvables"]:
        print("  introuvable :", k)
    for e in b["ecarts"]:
        print(f"  écart : {e['cle']} rang {e['rang']} · {e['sort']} [{e['forme']}]" + (f" · contrôle {e['controle']}" if e["controle"] else ""))
        print("     attendu :", json.dumps(e["attendu"], ensure_ascii=False))
        print("     actuel  :", json.dumps(e["actuel"], ensure_ascii=False))
