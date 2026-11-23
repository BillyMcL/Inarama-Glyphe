"""Seconde mesure du barème, réglée sur D&D 5 (partie 7 du document) : version actuelle et variantes D, C, D + C.
Rien n'est écrit dans la bibliothèque ni dans le site.

    python outils/mesure_bareme_2.py <dossier de sortie>

Écrit <sortie>/mesure_bareme_2.txt et <sortie>/couts_formes.json (version actuelle, avec les paliers des variantes).
"""
import os, sys, json, collections
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ICI, "..", "moteur")); os.chdir(os.path.join(ICI, "..", "moteur"))
import convert as C, corrections as K, bareme as B
from fiches import FICHES

OUT = sys.argv[1] if len(sys.argv) > 1 else "."
# Simulation (hors glyphe) : les glyphes de D&D 5 n'écrivent pas la concentration ; pour la variante C, la mesure la lit aussi
# dans la source D&D 5 (SRD), pour cette simulation seulement. Le coût d'Inarama, lui, ne lit que le glyphe.
_SRD = os.path.join(ICI, "..", "donnees", "srd")
CONC = {"5e": {s["index"] for s in json.load(open(os.path.join(_SRD, "spells.json"), encoding="utf-8")) if s.get("concentration")},
        "2024": {s["index"] for s in json.load(open(os.path.join(_SRD, "spells-2024.json"), encoding="utf-8")) if s.get("concentration")}}
SIMS = [("C* 0,5", dict(rabais_concentration=0.5)), ("C* 1", dict(rabais_concentration=1.0)),
        ("D + C* 0,5", dict(degats_officiels=True, rabais_concentration=0.5)), ("D + C* 1", dict(degats_officiels=True, rabais_concentration=1.0))]
JEU = {"5.1": "5e", "5.2": "2024", "3.5": "3.5", "pf1": "PF1", "pf2": "PF2", "pf2r": "PF2"}
DND = {"5e", "2024"}
FAMILLE = {"A": "Arcane", "H": "hybride", "R": "arts rares"}
VERSIONS = [("actuelle", {}), ("D", dict(degats_officiels=True)),
            ("C 0,5", dict(rabais_concentration=0.5)), ("C 1", dict(rabais_concentration=1.0)),
            ("D + C 0,5", dict(degats_officiels=True, rabais_concentration=0.5)), ("D + C 1", dict(degats_officiels=True, rabais_concentration=1.0))]
GENRES = ["blessure", "soin", "état", "être appelé", "outil ou déplacement", "garde", "autre"]
TRANCHES = ["0", "1-2", "3-4", "5-6", "7-9", "10"]
MESURABLES = {"IMPACT", "AMPLEUR", "LOCALISATION", "QUANTITE", "DUREE"}
NON_LUS = {"INTERACTION", "COSMETIQUE"}


def source(f):
    d = f["dnd"]
    return ("er" if d.startswith("Elden Ring") else "pf2r" if d.startswith("Pathfinder 2 (version") else "pf2" if d.startswith("Pathfinder 2")
            else "pf1" if d.startswith("Pathfinder 1") else "3.5" if "D&amp;D 3.5" in d else "5.2" if "2024" in d else "5.1")


def tranche(n): return "0" if n == 0 else "1-2" if n <= 2 else "3-4" if n <= 4 else "5-6" if n <= 6 else "7-9" if n <= 9 else "10"


def sig_sats(r):
    return tuple(sorted((str(s[2]) if len(s) > 2 else "", repr(s[1])) for s in (r[4] if len(r) > 4 and r[4] else [])))


def dimensions(f):
    """ (clé de groupe, valeur) pour chaque point mesurable : la forme sans ce point, et la valeur du point """
    src = [r for r in f["rings"] if r[0] not in NON_LUS]      # le barème ne lit ni l'Interaction (le niveau + 1) ni la Cosmétique
    rings = [(r[0], r[1], tuple(r[2]), sig_sats(r)) for r in src]
    base = (f["verb"], f["fam"], bool(f.get("combinee")))
    out = []
    for i, r in enumerate(rings):
        if r[0] in MESURABLES and (B._num(r[1]) or r[1] == "plein") and not (r[0] == "DUREE" and r[3]):
            out.append(((base, i, "v", tuple(x if j != i else (x[0], "*", x[2], x[3]) for j, x in enumerate(rings))), r[1]))
        if r[0] == "CIBLE":
            for k, s in enumerate(src[i][4] if len(src[i]) > 4 and src[i][4] else []):
                if not B._txt(s) and not B._est_sym(s[1]) and (B._num(s[1]) or s[1] == "plein"):
                    rr = list(rings); rr[i] = (r[0], r[1], r[2], ("cibles *",))
                    out.append(((base, i, "q", tuple(rr)), s[1]))
    return out


lignes, dims, erreurs = [], collections.defaultdict(list), []
for cle, fi in FICHES.items():
    for f in K.appliquer(cle, C.build_forms(cle, fi)):
        if K.est_elden_ring(f) or not any(r[0] == "IMPACT" for r in f["rings"]): continue
        jeu = JEU[source(f)]
        try:
            res = {nom: B.cout(f, **kw) for nom, kw in VERSIONS}
            if jeu in ("5e", "2024"):
                cc = cle in CONC[jeu]
                res.update({nom: B.cout(f, concentration=cc, **kw) for nom, kw in SIMS})
        except Exception as e:
            erreurs.append((cle, f["label"], repr(e))); continue
        a = res["actuelle"]
        x = dict(cle=cle, sort=f["fr"], jeu=jeu, forme=f["label"], niveau=int(f["level"]), famille="formes combinées" if f.get("combinee") else FAMILLE[f["fam"]],
                 fam=f["fam"], cout=a["cout"], palier=a["palier"], genre=a["genre"], detail=a["detail"], sans_trace=a["sans_trace"], defaut=a["defaut"],
                 paliers={nom: res[nom]["palier"] for nom, _ in VERSIONS}, couts={nom: res[nom]["cout"] for nom, _ in VERSIONS},
                 _details={nom: res[nom]["detail"] for nom in ("D", "D + C 0,5", "D + C 1")},
                 _sim={nom: res[nom]["palier"] for nom, _ in SIMS if nom in res}, _conc=jeu in ("5e", "2024") and cle in CONC[jeu])
        n = len(lignes); lignes.append(x)
        for k, v in dimensions(f): dims[k].append((v, n))


def st(xs, ver):
    if not xs: return "—"
    d = [x["paliers"][ver] - x["niveau"] for x in xs]; n = len(d)
    pc = lambda k: 100 * sum(1 for e in d if abs(e) <= k) / n
    return f"{n:5d} | {pc(0):5.1f} % | {pc(1):5.1f} % | {pc(2):5.1f} % | {sum(d) / n:+.2f}"


def table(titre, groupes, sel):
    T = [titre, "", "  (formes | bon palier | à 1 près | à 2 près | écart moyen)"]
    for g in groupes:
        xs = sel(g)
        if not xs: continue
        T.append(f"  {g:22s}")
        for v, _ in VERSIONS: T.append(f"      {v:12s} {st(xs, v)}")
    return T + [""]


dnd = [x for x in lignes if x["jeu"] in DND]
T = ["SECONDE MESURE DU BARÈME — réglée sur D&D 5 (5e et 2024)",
     "Branche bareme (bibliothèque de main 7eca99b, aucune forme changée). Version actuelle = règles du 22 novembre corrigées",
     "du 23 novembre (cible profonde, condition qui ouvre, palier 10). Variantes : D = dégâts lus dans le tableau officiel de",
     "D&D 5 ; C x = rabais de concentration x ; D + C x = les deux. Colonnes : nombre de formes | bon palier | à 1 près |",
     "à 2 près | écart moyen (palier − niveau). Formes : celles qui ont un cercle d'Impact, hors Elden Ring.",
     f"Erreurs de calcul : {len(erreurs)}." + (" " + repr(erreurs[:5]) if erreurs else ""), ""]
T += ["A. D&D 5 SEUL (la cible)", "=" * 24, ""]
T += table("A.1 Ensemble", ["5e et 2024", "5e", "2024"], lambda g: dnd if g == "5e et 2024" else [x for x in dnd if x["jeu"] == g])
T += table("A.2 Par tranche de niveau", TRANCHES[:5], lambda g: [x for x in dnd if tranche(x["niveau"]) == g])
T += table("A.3 Par genre d'effet (l'effet le plus cher de la forme, version actuelle)", GENRES, lambda g: [x for x in dnd if x["genre"] == g])
# meilleur rabais de concentration
conc = [x for x in dnd if x["paliers"]["C 1"] != x["paliers"]["actuelle"] or x["couts"]["C 1"] != x["couts"]["actuelle"]]
T += ["A.4 Rabais de concentration (variante C) : formes de D&D 5 dont la Condition porte « concentration »", ""]
for base, pre in (("sans D", ""), ("avec D", "D + ")):
    for r_, ver in (("0", "D" if pre else "actuelle"), ("0,5", pre + "C 0,5"), ("1", pre + "C 1")):
        T.append(f"      {base}, rabais {r_:3s} : sur les {len(conc)} formes concernées {st(conc, ver)} ; sur tout D&D 5 {st(dnd, ver)}")
T += ["", "A.4 bis SIMULATION, HORS GLYPHE : la concentration lue dans la source D&D 5 (le glyphe ne l'écrit pas)", ""]
cs = [x for x in dnd if x["_conc"]]
for nom, _ in [("actuelle", 0), ("D", 0)] + SIMS:
    def st2(xs):
        d = [(x["_sim"][nom] if nom in x["_sim"] else x["paliers"][nom]) - x["niveau"] for x in xs]; n = len(d)
        pc = lambda k: 100 * sum(1 for e in d if abs(e) <= k) / n
        return f"{n:5d} | {pc(0):5.1f} % | {pc(1):5.1f} % | {pc(2):5.1f} % | {sum(d) / n:+.2f}"
    T.append(f"      {nom:12s} sorts à concentration {st2(cs)} ; tout D&D 5 {st2(dnd)}")
T += [""]
# 30 plus loin
for ver in [v for v, _ in VERSIONS]:
    haut = sorted(dnd, key=lambda x: (-(x["paliers"][ver] - x["niveau"]), -(x["couts"][ver] - x["niveau"])))[:15]
    bas = sorted(dnd, key=lambda x: ((x["paliers"][ver] - x["niveau"]), (x["couts"][ver] - x["niveau"])))[:15]
    T += [f"A.5 Les 30 formes de D&D 5 les plus loin de leur niveau — version {ver} (15 au-dessus, 15 au-dessous)", ""]
    for x in haut + bas:
        T.append(f"  {x['sort']} ({x['cle']}, {x['jeu']}) — « {x['forme']} » — niveau {x['niveau']}, coût {x['couts'][ver]:.2f}, palier {x['paliers'][ver]} "
                 f"(écart {x['paliers'][ver] - x['niveau']:+d})")
        dt = x["detail"] if ver == "actuelle" else x["_details"].get(ver)
        if dt is not None:
            for d in dt: T.append(f"      {d}")
    T += [""]
# B. cohérence entre jeux
T += ["B. COHÉRENCE ENTRE JEUX", "=" * 23, "",
      "Paires : pour chaque sort présent en D&D 5 et dans un autre jeu (même clé), la première forme de chaque famille (Arcane avec",
      "Arcane, hybride avec hybride) ; la forme D&D 5 est celle de 5e, ou de 2024 à défaut. Même effet attendu : même palier.", ""]
prem = {}
for x in lignes: prem.setdefault((x["cle"], x["jeu"], x["fam"]), x)
paires = collections.defaultdict(list)
for (cle, jeu, fam), x in prem.items():
    if jeu in DND: continue
    d = prem.get((cle, "5e", fam)) or prem.get((cle, "2024", fam))
    if d: paires[jeu].append((d, x))
for ver, _ in VERSIONS:
    T.append(f"  version {ver}")
    for jeu in ("3.5", "PF1", "PF2"):
        ps = paires[jeu]
        if not ps: continue
        e = [o["paliers"][ver] - d["paliers"][ver] for d, o in ps]
        T.append(f"      D&D 5 / {jeu:4s} {len(ps):5d} paires | même palier {100 * sum(1 for v in e if v == 0) / len(e):5.1f} % | à 1 près "
                 f"{100 * sum(1 for v in e if abs(v) <= 1) / len(e):5.1f} % | écart moyen (autre − D&D 5) {sum(e) / len(e):+.2f}")
T += ["", "  Niveau d'origine de l'autre jeu comparé au palier d'Inarama (toutes les formes du jeu) : écart moyen niveau − palier,",
      "  par tranche du palier d'Inarama, et niveau d'origine moyen à chaque palier (base de l'estimation « ≈ niveau n » de l'éditeur)", ""]
for ver, _ in VERSIONS:
    T.append(f"  version {ver}")
    for jeu in ("3.5", "PF1", "PF2"):
        xs = [x for x in lignes if x["jeu"] == jeu]
        ligne = []
        for t in TRANCHES:
            g = [x for x in xs if tranche(x["paliers"][ver]) == t]
            if g: ligne.append(f"{t}: {sum(x['niveau'] - x['paliers'][ver] for x in g) / len(g):+.2f} ({len(g)})")
        moy = []
        for p in range(11):
            g = [x["niveau"] for x in xs if x["paliers"][ver] == p]
            if g: moy.append(f"{p}→{sum(g) / len(g):.1f}")
        T.append(f"      {jeu:4s} écart par tranche : " + " ; ".join(ligne))
        T.append(f"      {'':4s} niveau moyen par palier : " + " ".join(moy))
T += [""]
# C. plus fort = plus cher
T += ["C. L'EXIGENCE « PLUS FORT = PLUS CHER »", "=" * 39, "",
      "Paires de formes (toute la bibliothèque hors Elden Ring) au même verbe, même famille, mêmes cercles, mêmes mots et mêmes",
      "satellites (les cercles que le barème ne lit pas, Interaction et Cosmétique, sont mis de côté), sauf UN point plus grand chez l'une : valeur d'un Impact (montant ou degré), d'une Ampleur, d'une Localisation,",
      "d'une Quantité, d'une Durée (sans incantation), ou nombre de cibles. Plein compte plus que tout nombre. Une paire est en",
      "défaut quand la plus forte reçoit un palier plus bas (et, plus finement, un coût plus bas).", ""]
def plus_grand(a, b):
    if a == b: return False
    if a == "plein": return True
    if b == "plein": return False
    return a > b
for ver, _ in VERSIONS:
    vus, defauts, defauts_cout, total = set(), [], 0, 0
    for k, lst in dims.items():
        if len(lst) < 2: continue
        for va, ia in lst:
            for vb, ib in lst:
                if not plus_grand(va, vb): continue
                a, b = lignes[ia], lignes[ib]
                cle_p = (k[1], k[2], ia, ib)
                if cle_p in vus: continue
                vus.add(cle_p); total += 1
                if a["couts"][ver] < b["couts"][ver] - 1e-9: defauts_cout += 1
                if a["paliers"][ver] < b["paliers"][ver]: defauts.append((k, va, vb, a, b))
    crit = collections.Counter(k[3][k[1]][0] + (" (cibles)" if k[2] == "q" else "") for k, *_ in defauts)
    T.append(f"  version {ver} : {total} paires comparables ; {len(defauts)} en défaut sur le palier ({100 * len(defauts) / max(total, 1):.1f} %), "
             f"{defauts_cout} sur le coût ; par point : {dict(crit.most_common())}")
    if ver in ("actuelle", "D", "D + C 0,5"):
        for k, va, vb, a, b in defauts[:12]:
            T.append(f"      {k[3][k[1]][0]}{' (cibles)' if k[2] == 'q' else ''} {va} > {vb} : « {a['sort']} — {a['forme']} » ({a['jeu']}) palier {a['paliers'][ver]} "
                     f"(coût {a['couts'][ver]:.2f}) < « {b['sort']} — {b['forme']} » ({b['jeu']}) palier {b['paliers'][ver]} (coût {b['couts'][ver]:.2f})")
T += [""]
# D. autres jeux
T += ["D. LES AUTRES JEUX, POUR INFORMATION", "=" * 36, ""]
T += table("D.1 Par jeu (toutes versions)", ["3.5", "PF1", "PF2"], lambda g: [x for x in lignes if x["jeu"] == g])
T += ["D.2 Première mesure (22 novembre, sans les corrections du 23), par jeu, pour mémoire :",
      "      5e    868 formes | bon 25,0 % | à 1 62,0 % | à 2 80,6 % | écart +0,43",
      "      2024  296 formes | bon 29,7 % | à 1 66,2 % | à 2 89,5 % | écart +0,71",
      "      3.5  1487 formes | bon 26,8 % | à 1 66,3 % | à 2 82,2 % | écart −0,01",
      "      PF1  4808 formes | bon 22,8 % | à 1 59,5 % | à 2 81,0 % | écart −0,01",
      "      PF2  3521 formes | bon 22,8 % | à 1 56,9 % | à 2 79,7 % | écart +0,07", ""]
T += table("D.3 Toute la bibliothèque", ["toutes"], lambda g: lignes)
open(os.path.join(OUT, "mesure_bareme_2.txt"), "w", encoding="utf-8").write("\n".join(T) + "\n")
json.dump(dict(_lisez_moi="Coût de chaque forme qui a un cercle d'Impact (hors Elden Ring), calculé sur le glyphe seul par moteur/bareme.py "
                          "(version du 23 novembre : cible profonde, condition qui ouvre, palier 10). niveau : le niveau du sort dans sa source ; "
                          "cout, palier, detail : la version actuelle ; genre : le genre de l'effet le plus cher ; paliers et couts : la version "
                          "actuelle et les variantes à l'essai (D : dégâts du tableau officiel de D&D 5 ; C 0,5 et C 1 : rabais de "
                          "concentration ; D + C : les deux), non adoptées.",
               formes=[{k: v for k, v in x.items() if not k.startswith("_") and k != "fam"} for x in lignes]),
          open(os.path.join(OUT, "couts_formes.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("formes", len(lignes), "| erreurs", len(erreurs))
for v, _ in VERSIONS: print(v, "D&D 5 :", st(dnd, v), "| tout :", st(lignes, v))
