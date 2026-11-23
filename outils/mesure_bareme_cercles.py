"""Réglage des relations et mesure du barème par cercles (moteur/bareme_cercles.py). Rien n'est écrit dans la bibliothèque.

    python outils/mesure_bareme_cercles.py <dossier de sortie> <dossier des documents du barème (Claude outputs/phase4)>

Écrit mesure_bareme_cercles.txt, coefficients_bareme_cercles.json, couts_formes_cercles.json (et donnees_lacunes.json).
"""
import os, sys, json, math, re, collections, itertools
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ICI, "..", "moteur")); os.chdir(os.path.join(ICI, "..", "moteur"))
import convert as C, corrections as K, bareme_cercles as BC
from fiches import FICHES
OUT, DOCS = sys.argv[1], sys.argv[2]
SYSTEME = {"5.1": "D&D 5", "5.2": "D&D 5", "3.5": "3.5", "pf1": "PF1", "pf2": "PF2", "pf2r": "PF2"}
JEU = {"5.1": "5e", "5.2": "2024", "3.5": "3.5", "pf1": "PF1", "pf2": "PF2", "pf2r": "PF2 remaniée"}
SYSTEMES = ["D&D 5", "3.5", "PF1", "PF2"]
MIN_FAMILLE = 15          # une famille d'états se règle seule à partir de 15 formes ; sinon sa grande famille
MIN_GENRE = 8             # un genre trop petit se règle avec tous les genres de son système


def source(f):
    d = f["dnd"]
    return ("er" if d.startswith("Elden Ring") else "pf2r" if d.startswith("Pathfinder 2 (version") else "pf2" if d.startswith("Pathfinder 2")
            else "pf1" if d.startswith("Pathfinder 1") else "3.5" if "D&amp;D 3.5" in d else "5.2" if "2024" in d else "5.1")


def tranche(n): return "0" if n == 0 else "1-2" if n <= 2 else "3-4" if n <= 4 else "5-6" if n <= 6 else "7-9" if n <= 9 else "10"


# ---------------------------------------------------------------- relevé
F = []
for cle, fi in FICHES.items():
    for f in K.appliquer(cle, C.build_forms(cle, fi)):
        if K.est_elden_ring(f): continue
        src = source(f)
        a = BC.analyse(f)
        rings = [r for r in f["rings"] if r[0] != "INTERACTION"]
        sig = json.dumps([f["fam"], f["verb"], repr(f["core"]), repr(f.get("poles_impacts")),
                          sorted(repr((r[0], r[1], tuple(r[2]), repr(list(r[4]) if len(r) > 4 and r[4] else []))) for r in rings)], ensure_ascii=False)
        F.append(dict(cle=cle, sort=f["fr"], jeu=JEU[src], systeme=SYSTEME[src], forme=f["label"], niveau=int(f["level"]), famille_forme=f["fam"],
                      a=a, sig=sig, puissance1=any(r[0] == "IMPACT" and r[2][:1] == ["PUISSANCE"] and r[1] == 1 for r in f["rings"])))


# ---------------------------------------------------------------- moindres carrés sous contraintes (a ≥ 0, b ≥ 0, c ≤ 0)
def resoudre(A, y):
    """moindres carrés non négatifs, par énumération des variables actives (au plus 3)"""
    k = len(A[0]) if A else 0
    best = (sum(v * v for v in y), [0.0] * k)
    for m in range(1, 2 ** k):
        idx = [j for j in range(k) if m >> j & 1]
        # équations normales
        M = [[sum(A[i][p] * A[i][q] for i in range(len(A))) for q in idx] for p in idx]
        b = [sum(A[i][p] * y[i] for i in range(len(A))) for p in idx]
        n = len(idx)
        try:
            for c in range(n):          # Gauss
                piv = max(range(c, n), key=lambda r: abs(M[r][c]))
                if abs(M[piv][c]) < 1e-12: raise ZeroDivisionError
                M[c], M[piv] = M[piv], M[c]; b[c], b[piv] = b[piv], b[c]
                for r in range(n):
                    if r != c:
                        t = M[r][c] / M[c][c]
                        M[r] = [x - t * yy for x, yy in zip(M[r], M[c])]; b[r] -= t * b[c]
            sol = [b[c] / M[c][c] for c in range(n)]
        except ZeroDivisionError:
            continue
        if any(v < -1e-9 for v in sol): continue
        x = [0.0] * k
        for j, v in zip(idx, sol): x[j] = v
        sse = sum((y[i] - sum(A[i][j] * x[j] for j in range(k))) ** 2 for i in range(len(A)))
        if sse < best[0] - 1e-12: best = (sse, x)
    return best[1]


def regler(rows, avec_cibles):
    """coefficients (a, b, c) sur des formes : niveau − prix de l'effet − prix décidés ≈ a·log2(cibles) + b·marche + c·restriction"""
    A, y = [], []
    for x in rows:
        m = x["a"]["mesures"]
        lig = ([math.log2(max(m["cibles"], 1))] if avec_cibles else []) + [m["marche"], -(1.0 if m["restriction"] else 0.0)]
        A.append(lig); y.append(x["niveau"] - x["a"]["prix_effet"] - x["a"]["decides"])
    if not A: return dict(a=0.0, b=0.0, c=0.0)
    s = resoudre(A, y)
    if avec_cibles: return dict(a=round(s[0], 3), b=round(s[1], 3), c=round(-s[2], 3))
    return dict(a=0.0, b=round(s[0], 3), c=round(-s[1], 3))


def cle_groupe(x, n_fam, n_grande, n_genre):
    a = x["a"]; s = x["systeme"]
    if a["sans_impact"]: return None
    if a["genre"] == "état":
        fam = a["famille"] or "?"
        if n_fam[(s, fam)] >= MIN_FAMILLE: return f"état : {fam}"
        gf = BC.GRANDE_FAMILLE.get(fam, "corps")
        if n_grande[(s, gf)] >= MIN_FAMILLE: return f"état (grande famille) : {gf}"
        return "état (toutes familles)"
    if n_genre[(s, a["genre"])] >= MIN_GENRE: return a["genre"]
    return "autres genres (trop peu de formes)"


n_fam = collections.Counter((x["systeme"], x["a"]["famille"] or "?") for x in F if x["a"]["genre"] == "état")
n_grande = collections.Counter((x["systeme"], BC.GRANDE_FAMILLE.get(x["a"]["famille"] or "?", "corps")) for x in F if x["a"]["genre"] == "état")
n_genre = collections.Counter((x["systeme"], x["a"]["genre"]) for x in F)
for x in F: x["groupe"] = cle_groupe(x, n_fam, n_grande, n_genre)
COEFS = collections.defaultdict(dict)
for s in SYSTEMES:
    for g in sorted({x["groupe"] for x in F if x["systeme"] == s and x["groupe"]}):
        rows = [x for x in F if x["systeme"] == s and x["groupe"] == g]
        avec = not any(x["a"]["genre"] in ("blessure", "soin") for x in rows)
        c = regler(rows, avec)
        c["formes"] = len(rows); c["cibles_reglees"] = avec
        COEFS[s][g] = c
for x in F:
    c = COEFS[x["systeme"]].get(x["groupe"], dict(a=0, b=0, c=0)) if x["groupe"] else dict(a=0, b=0, c=0)
    x["cout"], x["palier"], x["relations"] = BC.palier(x["a"], c)
    x["ecart"] = x["palier"] - x["niveau"]


# ---------------------------------------------------------------- mesure
def st(xs):
    if not xs: return "—"
    d = [x["ecart"] for x in xs]; n = len(d)
    pc = lambda k: 100 * sum(1 for e in d if abs(e) <= k) / n
    return f"{n:5d} | {pc(0):5.1f} % | {pc(1):5.1f} % | {pc(2):5.1f} % | {sum(d) / n:+.2f}"


T = ["MESURE DU BARÈME PAR CERCLES — version réglée (relations par genre et par système)",
     "Branche bareme-cercles (bibliothèque de main 33016e2, aucune forme changée). Formes : toutes celles qui ont un cercle d'Impact, hors",
     "Elden Ring (les formes sans Impact, Cosmétique seule, sont comptées à part). Colonnes : formes | bon palier | à 1 près | à 2 près |",
     "écart moyen (palier − niveau). Chaque système est réglé sur ses propres niveaux.", ""]
avec = [x for x in F if not x["a"]["sans_impact"]]
dnd = [x for x in avec if x["systeme"] == "D&D 5"]
T += ["A. D&D 5 (5e et 2024)", "=" * 21, "", "  (formes | bon | à 1 | à 2 | écart)", f"  ensemble            {st(dnd)}", f"  5e                  {st([x for x in dnd if x['jeu'] == '5e'])}",
      f"  2024                {st([x for x in dnd if x['jeu'] == '2024'])}", "", "  par tranche de niveau :"]
for t in ["0", "1-2", "3-4", "5-6", "7-9"]: T.append(f"    {t:16s} {st([x for x in dnd if tranche(x['niveau']) == t])}")
T += ["", "  par genre (de l'effet le plus cher) :"]
for g in sorted({x["a"]["genre"] for x in dnd}, key=lambda g: -sum(1 for x in dnd if x["a"]["genre"] == g)):
    T.append(f"    {g:24s} {st([x for x in dnd if x['a']['genre'] == g])}")
T += ["", "  par groupe de réglage :"]
for g in sorted({x["groupe"] for x in dnd}, key=lambda g: -sum(1 for x in dnd if x["groupe"] == g)):
    T.append(f"    {g:40s} {st([x for x in dnd if x['groupe'] == g])}")
T += ["", "  Les 40 formes de D&D 5 les plus loin de leur niveau (dans les deux sens) :", ""]
for x in sorted(dnd, key=lambda x: (-abs(x["ecart"]), -abs(x["cout"] - x["niveau"])))[:40]:
    m = x["a"]["mesures"]
    T.append(f"  {x['sort']} ({x['cle']}, {x['jeu']}) — « {x['forme']} » — niveau {x['niveau']}, coût {x['cout']:.2f}, palier {x['palier']} (écart {x['ecart']:+d})")
    T.append(f"      genre {x['a']['genre']}{(' / ' + x['a']['famille']) if x['a']['famille'] else ''} ; groupe {x['groupe']} ; cibles {m['cibles']} ({m['cibles_lecture']}) ; "
             f"marche {m['marche']} ; restriction {', '.join(m['restriction']) or 'non'} ; relations {x['relations']:+.2f}")
    for d in x["a"]["detail"]: T.append(f"      {d['cercle']} {d.get('lecture', '')} : {d['prix']:+.2f} — {d['regle']}")
T += ["", ""]
# B. coefficients
T += ["B. COEFFICIENTS RÉGLÉS, PAR GROUPE ET PAR SYSTÈME", "=" * 47, "",
      "  a : par doublement des cibles ; b : par marche de durée ; c : restriction de sortes d'êtres (≤ 0). « — » : groupe absent du système.",
      "  Blessures et soins : la relation « cibles » est déjà dans le prix (colonne du tableau, +2) ; a n'est pas réglé.", ""]
groupes = sorted({g for s in SYSTEMES for g in COEFS[s]})
T.append(f"  {'groupe':42s}" + "".join(f"{s:>26s}" for s in SYSTEMES))
alertes = []
for g in groupes:
    cells = []
    for s in SYSTEMES:
        c = COEFS[s].get(g)
        cells.append(f"a {c['a']:.2f} b {c['b']:.2f} c {c['c']:.2f} ({c['formes']})" if c else "—")
    T.append(f"  {g:42s}" + "".join(f"{c:>26s}" for c in cells))
    for k in ("a", "b", "c"):
        vals = [(s, COEFS[s][g][k]) for s in SYSTEMES if g in COEFS[s] and COEFS[s][g]["formes"] >= MIN_GENRE]
        nz = [v for _, v in vals if abs(v) > 0.05]
        if len(vals) >= 2 and nz and (len(nz) < len(vals) or max(abs(v) for v in nz) > 2 * min(abs(v) for v in nz)):
            alertes.append(f"  {g} — {k} : " + ", ".join(f"{s} {v:.2f}" for s, v in vals))
T += ["", "  Relations qui ne sont pas les mêmes d'un système à l'autre (nulle ici et non nulle là, ou de taille au moins double) :", ""] + (alertes or ["  aucune"]) + ["", ""]
# C. conversion
T += ["C. CONVERSION VERS D&D 5", "=" * 24, "", "  Écart moyen restant (palier − niveau, chaque système avec ses propres coefficients), par genre et par tranche :", ""]
for s in SYSTEMES[1:]:
    xs = [x for x in avec if x["systeme"] == s]
    T.append(f"  {s} : ensemble {st(xs)}")
    T.append("     par genre : " + " ; ".join(f"{g} {sum(x['ecart'] for x in xs if x['a']['genre'] == g) / max(1, sum(1 for x in xs if x['a']['genre'] == g)):+.2f} ({sum(1 for x in xs if x['a']['genre'] == g)})"
                                       for g in sorted({x['a']['genre'] for x in xs})))
    T.append("     par tranche : " + " ; ".join(f"{t} {sum(x['ecart'] for x in xs if tranche(x['niveau']) == t) / max(1, sum(1 for x in xs if tranche(x['niveau']) == t)):+.2f}"
                                         for t in ["0", "1-2", "3-4", "5-6", "7-9", "10"] if any(tranche(x['niveau']) == t for x in xs)))
T += ["", "  Décalage vers D&D 5, sur les sorts présents dans les deux systèmes (même clé ; première forme de chaque famille) :",
      "  « niveau » = niveau D&D 5 − niveau de l'autre système ; « palier » = palier calculé D&D 5 − palier calculé de l'autre système.", ""]
prem = {}
for x in avec: prem.setdefault((x["cle"], x["systeme"], x["famille_forme"]), x)
DEC = {}
for s in SYSTEMES[1:]:
    ps = [(prem[(c, "D&D 5", fm)], o) for (c, ss, fm), o in prem.items() if ss == s and (c, "D&D 5", fm) in prem]
    if not ps: continue
    dn = sum(d["niveau"] - o["niveau"] for d, o in ps) / len(ps); dp = sum(d["palier"] - o["palier"] for d, o in ps) / len(ps)
    DEC[s] = dict(paires=len(ps), niveau=round(dn, 2), palier=round(dp, 2))
    T.append(f"  {s} : {len(ps)} paires ; décalage de niveau {dn:+.2f} ; décalage de palier calculé {dp:+.2f}")
    par = collections.defaultdict(list)
    for d, o in ps: par[d["a"]["genre"]].append(d["niveau"] - o["niveau"])
    T.append("     par genre (niveau) : " + " ; ".join(f"{g} {sum(v) / len(v):+.2f} ({len(v)})" for g, v in sorted(par.items(), key=lambda t: -len(t[1]))))
T += ["", ""]
# D. plus fort = plus cher
rep = {e["id"]: e for e in json.load(open(os.path.join(DOCS, "repertoire_cercles.json"), encoding="utf-8"))["cercles"]}
pa = json.load(open(os.path.join(DOCS, "paires_cercles.json"), encoding="utf-8"))
idx = {(x["cle"], x["jeu"], x["forme"]): x for x in F}
FORT = {"IMPACT", "AMPLEUR", "LOCALISATION", "QUANTITE", "DUREE", "FORME"}
def plus_fort(ca, cb):
    """1 si le cercle ca est plus fort que cb, −1 si plus faible, 0 si on ne sait pas"""
    if ca is None or cb is None:
        c = rep[ca or cb]; sgn = 1 if ca else -1
        if c["type"] in FORT: return sgn
        if c["type"] in ("CONDITION", "COMPOSANTE"): return -sgn
        return 0
    a, b = rep[ca], rep[cb]
    if a["type"] != b["type"] or a["mots"] != b["mots"] or a["satellites"] != b["satellites"] or a["type"] not in FORT: return 0
    va, vb = a["valeur"], b["valeur"]
    if va == vb: return 0
    if va == "plein": return 1
    if vb == "plein": return -1
    if isinstance(va, (int, float)) and isinstance(vb, (int, float)): return 1 if va > vb else -1
    return 0
viol, tot_cmp = [], 0
for p in pa["paires"]:
    fa, fb = pa["formes"][p["a"]], pa["formes"][p["b"]]
    if fa["jeu"] != fb["jeu"]: continue
    s_ = plus_fort(p["cercle_a"], p["cercle_b"])
    if not s_: continue
    xa, xb = idx.get((fa["cle"], fa["jeu"], fa["forme"])), idx.get((fb["cle"], fb["jeu"], fb["forme"]))
    if not xa or not xb: continue
    tot_cmp += 1
    fort, faible = (xa, xb) if s_ > 0 else (xb, xa)
    if fort["palier"] < faible["palier"]:
        cf = p["cercle_a"] if s_ > 0 else p["cercle_b"]; cw = p["cercle_b"] if s_ > 0 else p["cercle_a"]
        viol.append((fort, faible, cf, cw))
T += ["D. « PLUS FORT = PLUS CHER »", "=" * 27, "",
      f"  Paires à un cercle près, même édition (paires_cercles.json), où l'on sait lequel est le plus fort : {tot_cmp}. Plus fort : une valeur plus",
      "  grande (Impact, Ampleur, Localisation, Quantité, Durée, Forme ; plein au-dessus de tout nombre), ou un de ces cercles en plus ;",
      "  plus faible : une Condition ou une Composante en plus.",
      f"  Paires où le plus fort reçoit un palier plus bas : {len(viol)}.", ""]
cnt = collections.Counter(rep[(cf or cw)]["type"] for _, _, cf, cw in viol)
T.append("  par type du cercle qui change : " + (", ".join(f"{k} {v}" for k, v in cnt.most_common()) or "—"))
for fort, faible, cf, cw in viol[:40]:
    def dc(c): return "absent" if c is None else f"{c} {rep[c]['type']} {rep[c]['valeur']} « {' · '.join(rep[c]['mots']).lower()} »"
    T.append(f"    {fort['sort']} ({fort['jeu']}) « {fort['forme']} » palier {fort['palier']} [{dc(cf)}]  <  {faible['sort']} « {faible['forme']} » palier {faible['palier']} [{dc(cw)}]")
T += ["", ""]
# E. lacunes
def table_md(path, titre_section, col):
    """(sort, jeu) des lignes d'une table Markdown dont la colonne col vaut « oui »"""
    txt = open(path, encoding="utf-8").read()
    i = txt.find(titre_section)
    if i < 0: return set()
    lignes = txt[i:].split("\n")
    hdr = None; out = set()
    for l in lignes[1:]:
        if l.startswith("## "): break
        if l.startswith("| Sort"): hdr = [c.strip() for c in l.strip("|").split("|")]; continue
        if hdr and l.startswith("|") and not l.startswith("|---") and not set(l) <= set("|- :"):
            cs = [c.strip() for c in l.strip("|").split("|")]
            if len(cs) >= len(hdr) and col in hdr and cs[hdr.index(col)].lower().startswith("oui"):
                out.add((cs[0], cs[1]))
    return out
jet = set()
for nom in os.listdir(DOCS):
    if nom.startswith("releve_etats_"): jet |= table_md(os.path.join(DOCS, nom), "## D.", "Jet renouvelé")
bonus = set()
txt = open(os.path.join(DOCS, "releve_bonus_mecaniques.md"), encoding="utf-8").read()
partA = txt[txt.find("## A."):txt.find("## B.")]
for l in partA.split("\n"):
    if l.startswith("|") and not l.startswith("| Sort") and not l.startswith("|---"):
        cs = [c.strip() for c in l.strip("|").split("|")]
        if len(cs) > 2: bonus.add((cs[0], cs[1]))
def jeu_doc(x): return {"PF2 remaniée": "PF2"}.get(x["jeu"], x["jeu"])
sig_sys = collections.Counter((x["sig"], x["systeme"]) for x in avec)
groupes_lac = {
    "jet renouvelé (relevés des états, section D)": [x for x in avec if (x["sort"], jeu_doc(x)) in jet],
    "mécaniques des bonus (relevé des bonus, section A)": [x for x in avec if (x["sort"], jeu_doc(x)) in bonus],
    "jumelles (même glyphe, même système, autre forme)": [x for x in avec if sig_sys[(x["sig"], x["systeme"])] > 1],
    "puissance inférieure à 1 (puissance 1 écrite, 4 êtres ou plus)": [x for x in avec if x["puissance1"] and x["a"]["mesures"]["instances"] >= 4],
    "zones sans taille (une Forme sans Ampleur, lot 1)": [x for x in avec if any(l.startswith("zone sans taille") for l in x["a"]["lacunes"])],
    "figures à part (plans, dômes, explosions…, lot 1)": [x for x in avec if any(l.startswith("figure à part") for l in x["a"]["lacunes"])],
    "Cible « une zone » sans Forme ni taille": [x for x in avec if "zone sans Forme ni taille" in x["a"]["lacunes"]],
}
T += ["E. LES LACUNES D'ÉCRITURE QUI PÈSENT DANS LES ERREURS", "=" * 52, "",
      f"  Toutes les formes : écart moyen {sum(x['ecart'] for x in avec) / len(avec):+.2f}, écart absolu moyen {sum(abs(x['ecart']) for x in avec) / len(avec):.2f}.", ""]
for nom, xs in groupes_lac.items():
    if not xs: T.append(f"  {nom} : aucune forme retrouvée"); continue
    par_sys = collections.Counter(x["systeme"] for x in xs)
    T.append(f"  {nom} : {len(xs)} formes ({', '.join(f'{s} {n}' for s, n in par_sys.items())}) ; écart moyen {sum(x['ecart'] for x in xs) / len(xs):+.2f}, "
             f"absolu {sum(abs(x['ecart']) for x in xs) / len(xs):.2f}")
T += ["", "  (Le jet renouvelé et les mécaniques des bonus ne se lisent pas sur le glyphe : les formes sont retrouvées par sort et jeu dans les",
      "  relevés. Les jumelles sont recalculées ici sur les glyphes, cercle d'Interaction mis à part.)", ""]
open(os.path.join(OUT, "mesure_bareme_cercles.txt"), "w", encoding="utf-8").write("\n".join(T) + "\n")
json.dump(dict(_lisez_moi="Coefficients des relations du barème par cercles, réglés sur les niveaux de la source, groupe par groupe et système par "
                          "système : palier ≈ prix de l'effet + a × log2(cibles) + b × marche de durée + c × restriction + prix décidés. "
                          "a ≥ 0, b ≥ 0, c ≤ 0. Blessures et soins : a non réglé (déjà dans le prix). formes : le nombre de formes du réglage.",
               coefficients=COEFS, decalage_vers_dnd5=DEC, seuils=dict(famille=MIN_FAMILLE, genre=MIN_GENRE)),
          open(os.path.join(OUT, "coefficients_bareme_cercles.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(dict(_lisez_moi="Pour chaque forme (hors Elden Ring) : le palier calculé par le barème par cercles (version réglée), son coût, le détail "
                          "cercle par cercle avec la règle appliquée, les mesures lues sur le glyphe (cibles, marche de durée, restriction), le "
                          "groupe de réglage et l'apport des relations.",
               formes=[dict(cle=x["cle"], sort=x["sort"], jeu=x["jeu"], systeme=x["systeme"], forme=x["forme"], niveau=x["niveau"], palier=x["palier"],
                            cout=x["cout"], ecart=x["ecart"], genre=x["a"]["genre"], famille=x["a"]["famille"], role=x["a"]["role"], groupe=x["groupe"],
                            prix_effet=x["a"]["prix_effet"], prix_decides=x["a"]["decides"], relations=x["relations"], mesures=x["a"]["mesures"],
                            detail=x["a"]["detail"], lacunes=x["a"]["lacunes"]) for x in F]),
          open(os.path.join(OUT, "couts_formes_cercles.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=str)
json.dump(dict(genres_dnd5=collections.Counter(x["a"]["genre"] for x in dnd), lacunes={k: len(v) for k, v in groupes_lac.items()}, jet=len(jet), bonus=len(bonus),
               sans_impact=sum(1 for x in F if x["a"]["sans_impact"]), violations=len(viol), comparables=tot_cmp, alertes=len(alertes),
               cibles_lecture=collections.Counter(x["a"]["mesures"]["cibles_lecture"].split(" :")[0].split(" (")[0] for x in avec).most_common(12)),
          open(os.path.join(OUT, "donnees_lacunes.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=str)
print("formes", len(F), "| avec Impact", len(avec), "| D&D 5 :", st(dnd), "| violations", len(viol), "/", tot_cmp)
