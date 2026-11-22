"""Mesure du barème (moteur/bareme.py) sur la bibliothèque : le palier calculé sur le glyphe, comparé au niveau du sort
dans sa source. Rien n'est écrit dans la bibliothèque ni dans le site.

    python outils/mesure_bareme.py <dossier de sortie>

Écrit <sortie>/mesure_bareme.txt (le rapport) et <sortie>/couts_formes.json (coût, palier et détail de chaque forme).
Formes mesurées : toutes celles qui ont un cercle d'Impact, hors Elden Ring.
"""
import os, sys, json, collections, math
ICI = os.path.dirname(os.path.abspath(__file__))
MOT = os.path.join(ICI, "..", "moteur")
sys.path.insert(0, MOT); os.chdir(MOT)
import convert as C, corrections as K, bareme as B
from fiches import FICHES

OUT = sys.argv[1] if len(sys.argv) > 1 else "."
JEU = {"5.1": "5e", "5.2": "2024", "3.5": "3.5", "pf1": "PF1", "pf2": "PF2", "pf2r": "PF2"}
FACTEUR = {"3.5": 1.25, "PF1": 1.2, "PF2": 1.25}         # ancien calcul (20 novembre), pour comparaison seulement
FAMILLE = {"A": "Arcane", "H": "hybride", "R": "arts rares"}


def source(f):
    d = f["dnd"]
    return ("er" if d.startswith("Elden Ring") else "pf2r" if d.startswith("Pathfinder 2 (version") else "pf2" if d.startswith("Pathfinder 2")
            else "pf1" if d.startswith("Pathfinder 1") else "3.5" if "D&amp;D 3.5" in d else "5.2" if "2024" in d else "5.1")


lignes, erreurs = [], []
for cle, fi in FICHES.items():
    for f in K.appliquer(cle, C.build_forms(cle, fi)):
        if K.est_elden_ring(f) or not any(r[0] == "IMPACT" for r in f["rings"]): continue
        jeu = JEU[source(f)]
        try:
            a = B.cout(f)
            b = B.cout(f, facteur_montant=FACTEUR.get(jeu, 1.0))
            c = B.cout(f, force_tous_ajouts=False)
        except Exception as e:
            erreurs.append((cle, f["label"], repr(e))); continue
        fam = "formes combinées" if f.get("combinee") else FAMILLE[f["fam"]]
        lecture = {" ".join([r[0], str(r[1])] + list(r[2])): r[3] for r in f["rings"] if r[0] == "IMPACT"}
        lignes.append(dict(cle=cle, sort=f["fr"], jeu=jeu, forme=f["label"], niveau=int(f["level"]), famille=fam,
                           cout=a["cout"], palier=a["palier"], sorte=a["sorte"], detail=a["detail"], sans_trace=a["sans_trace"],
                           defaut=a["defaut"], palier_facteur=b["palier"], palier_ajouts_20nov=c["palier"], _lecture=lecture))


def stats(xs, cle="palier"):
    if not xs: return "—"
    d = [x[cle] - x["niveau"] for x in xs]
    n = len(d)
    pc = lambda k: 100 * sum(1 for e in d if abs(e) <= k) / n
    return (f"{n:6d} formes | bon palier {pc(0):5.1f} % | à 1 près {pc(1):5.1f} % | à 2 près {pc(2):5.1f} % | "
            f"écart moyen {sum(d) / n:+.2f} (absolu {sum(abs(e) for e in d) / n:.2f})")


def tranche(n): return "0" if n == 0 else "1-2" if n <= 2 else "3-4" if n <= 4 else "5-6" if n <= 6 else "7-9" if n <= 9 else "10 (PF2)"


T = []
T += ["MESURE DU BARÈME — le palier calculé sur le glyphe seul, comparé au niveau du sort dans sa source",
      "Bibliothèque de la branche bareme (main 7eca99b, aucune forme changée). Formes : toutes celles qui ont un cercle d'Impact,",
      "hors Elden Ring. Palier = coût arrondi (demi vers le haut), borné de 0 à 9. Écart = palier − niveau de la source.",
      f"Erreurs de calcul : {len(erreurs)}." + (" " + repr(erreurs[:5]) if erreurs else ""), ""]
T += ["1. ENSEMBLE", "=" * 11, "", "  sans facteur par jeu (le coût d'Inarama)  : " + stats(lignes),
      "  avec le facteur de l'ancien calcul        : " + stats(lignes, "palier_facteur") + "   (3.5 × 1,25 ; PF1 × 1,2 ; PF2 × 1,25 sur les montants)",
      "  ajouts × force sur cibles et zone seules  : " + stats(lignes, "palier_ajouts_20nov") + "   (lecture du 20 novembre de la règle 2.4)",
      "  référence du 20 novembre : 5 740 formes, 62 % à un palier, 84 % à deux.", ""]
for titre, cle_g, ordre in (("2. PAR JEU", "jeu", ["5e", "2024", "3.5", "PF1", "PF2"]),
                            ("3. PAR TRANCHE DE NIVEAU", "tranche", ["0", "1-2", "3-4", "5-6", "7-9", "10 (PF2)"]),
                            ("4. PAR FAMILLE", "famille", ["Arcane", "hybride", "arts rares", "formes combinées"])):
    T += [titre, "=" * len(titre), ""]
    for g in ordre:
        xs = [x for x in lignes if (tranche(x["niveau"]) if cle_g == "tranche" else x[cle_g]) == g]
        if not xs: continue
        T += [f"  {g:17s} sans facteur : " + stats(xs), f"  {'':17s} avec facteur : " + stats(xs, "palier_facteur")]
    T += [""]
# mots au défaut
md = collections.defaultdict(lambda: dict(cercles=0, formes=set(), ex=[]))
for x in lignes:
    vus = set()
    for w in x["defaut"]:
        m = md[w]; m["cercles"] += 1; m["formes"].add((x["cle"], x["forme"]))
        if x["sort"] not in [e[0] for e in m["ex"]] and len(m["ex"]) < 3:
            ph = next((v for k, v in x["_lecture"].items() if w.split()[0] in k.split()), next(iter(x["_lecture"].values())))
            m["ex"].append((x["sort"], x["jeu"], ph))
T += ["5. MOTS D'IMPACT TOMBÉS AU PRIX PAR DÉFAUT (3,0)", "=" * 48, "",
      f"  {len(md)} mots ; {sum(m['cercles'] for m in md.values())} cercles ; "
      f"{len({k for m in md.values() for k in m['formes']})} formes. Un cercle sans aucun mot connu compte chacun de ses mots.", ""]
for w, m in sorted(md.items(), key=lambda t: (-t[1]["cercles"], t[0])):
    T.append(f"  {w.lower()} — {m['cercles']} cercles, {len(m['formes'])} formes")
    for s, j, ph in m["ex"]: T.append(f"      {s} ({j}) : {ph}")
T += [""]
st = collections.Counter(t for x in lignes for t in x["sans_trace"])
T += ["6. RELATIONS SANS TRACE SUR LE GLYPHE", "=" * 37, "", "  (nombre de formes où la relation manque alors qu'une règle en a besoin)", ""]
for t, n in st.most_common(): T.append(f"  {n:5d}  {t}")
T += [""]
loin = sorted(lignes, key=lambda x: (-abs(x["palier"] - x["niveau"]), -abs(x["cout"] - x["niveau"])))[:30]
T += ["7. LES 30 FORMES LES PLUS LOIN DE LEUR NIVEAU", "=" * 45, "",
      f"  {sum(1 for x in loin if x['palier'] > x['niveau'])} au-dessus, {sum(1 for x in loin if x['palier'] < x['niveau'])} au-dessous.", ""]
for x in loin:
    T.append(f"  {x['sort']} ({x['cle']}, {x['jeu']}) — « {x['forme']} » — niveau {x['niveau']}, coût {x['cout']:.2f}, palier {x['palier']} "
             f"(écart {x['palier'] - x['niveau']:+d})")
    for d in x["detail"]: T.append(f"      {d}")
    for s in x["sans_trace"]: T.append(f"      sans trace : {s}")
open(os.path.join(OUT, "mesure_bareme.txt"), "w", encoding="utf-8").write("\n".join(T) + "\n")
json.dump(dict(_lisez_moi="Coût de chaque forme qui a un cercle d'Impact (hors Elden Ring), calculé sur le glyphe seul par moteur/bareme.py. "
                          "niveau : le niveau du sort dans sa source ; cout : le total ; palier : arrondi, borné de 0 à 9 ; detail : les "
                          "étapes, avec le numéro de la règle (document bareme_regles_2026-11-22.md) ; sans_trace : relations dont une "
                          "règle a besoin et que le glyphe n'écrit pas ; defaut : mots tombés au prix par défaut (3,0) ; palier_facteur : "
                          "le palier avec le facteur par jeu de l'ancien calcul, pour comparaison seulement.",
               formes=[{k: v for k, v in x.items() if not k.startswith("_") and k != "palier_ajouts_20nov"} for x in lignes]),
          open(os.path.join(OUT, "couts_formes.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("formes", len(lignes), "| erreurs", len(erreurs)); print(stats(lignes)); print(stats(lignes, "palier_facteur"))
