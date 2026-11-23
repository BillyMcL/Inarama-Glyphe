"""Barème par cercles, version 2 (décisions des étapes 1 à 3) : un barème par système, conversion vers Inarama au cercle, et la
mesure honnête « sort caché ». Rien n'est écrit dans la bibliothèque.

    python outils/mesure_bareme_cercles_v2.py <dossier de sortie> <dossier des documents du barème (Claude outputs/phase4)>

- Relations (a × log2(cibles) + b × marche + c × restriction, a ≥ 0, b ≥ 0, c ≤ 0) : 3.5, PF1 et PF2 ont chacun leurs règles par
  genre, réglées sur leurs propres formes ; un genre de moins de 15 formes prend la règle générale du système. D&D 5 prend, pour
  chaque genre, la règle réglée sur 3.5 + PF1 + PF2 ensemble. Blessures et soins : a n'est pas réglé (déjà dans leur prix).
- Prix propre d'un effet unique (cercle d'Impact sans prix, identifié comme au répertoire, satellites compris) : sur les formes où il
  est le seul effet d'Impact, niveau − prix décidés − relations du système ; médian par système.
- Conversion au cercle : par système, l'écart médian « prix propre en D&D 5 − prix propre dans le système » sur les cercles qui ont
  les deux ; prix d'Inarama = le prix en D&D 5, sinon le médian des prix convertis.
- Sort caché : relations, prix propres et conversion se recalculent sans le sort mesuré (même clé, dans tous les systèmes).
"""
import os, sys, json, math, collections, statistics, re
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ICI, "..", "moteur")); os.chdir(os.path.join(ICI, "..", "moteur"))
import convert as C, corrections as K, bareme_cercles as BC
from fiches import FICHES
OUT, DOCS = sys.argv[1], sys.argv[2]
SYSTEME = {"5.1": "D&D 5", "5.2": "D&D 5", "3.5": "3.5", "pf1": "PF1", "pf2": "PF2", "pf2r": "PF2"}
JEU = {"5.1": "5e", "5.2": "2024", "3.5": "3.5", "pf1": "PF1", "pf2": "PF2", "pf2r": "PF2 remaniée"}
AUTRES = ["3.5", "PF1", "PF2"]
SYSTEMES = ["D&D 5"] + AUTRES
MIN = 15
GEN = "(règle générale)"


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
        m = a["mesures"]
        g = ("état : " + (a["famille"] or "?")) if a["genre"] == "état" else a["genre"]
        sans_prix = [e for e in a["effets"] if e["sans_prix"]]
        x = dict(cle=cle, sort=f["fr"], jeu=JEU[src], systeme=SYSTEME[src], forme=f["label"], niveau=int(f["level"]), a=a, sig=sig, groupe=g,
                 v=(math.log2(max(m["cibles"], 1)), m["marche"], -(1.0 if m["restriction"] else 0.0)), fixe=a["genre"] in ("blessure", "soin"),
                 paye=not a["sans_impact"] and not sans_prix, unique=(sans_prix[0]["cercle"] if len(a["effets"]) == 1 and sans_prix else None),
                 puissance1=any(r[0] == "IMPACT" and r[2][:1] == ["PUISSANCE"] and r[1] == 1 for r in f["rings"]),
                 impacts_plein=[(tuple(r[2])) for r in f["rings"] if r[0] == "IMPACT" and r[1] == "plein"])
        x["y"] = x["niveau"] - a["prix_effet"] - a["decides"]
        F.append(x)
print("formes", len(F))


# ---------------------------------------------------------------- moindres carrés sous contraintes, par sommes
def zero(): return [0.0, [[0.0] * 3 for _ in range(3)], [0.0] * 3]
def ajoute(S, v, y, sgn=1):
    S[0] += sgn
    for i in range(3):
        S[2][i] += sgn * v[i] * y
        for j in range(3): S[1][i][j] += sgn * v[i] * v[j]
def moins(S, T): return [S[0] - T[0], [[S[1][i][j] - T[1][i][j] for j in range(3)] for i in range(3)], [S[2][i] - T[2][i] for i in range(3)]]
def plus(*Ss):
    out = zero()
    for S in Ss:
        out[0] += S[0]
        for i in range(3):
            out[2][i] += S[2][i]
            for j in range(3): out[1][i][j] += S[1][i][j]
    return out


def resoudre(S, libres):
    """a, b, c ≥ 0 sur les variables libres (c porte déjà le signe −) : le meilleur sous-ensemble faisable"""
    best, bx = 0.0, [0.0, 0.0, 0.0]          # écart à zéro : comparer les sommes de carrés expliquées
    for m in range(1, 2 ** len(libres)):
        idx = [libres[j] for j in range(len(libres)) if m >> j & 1]
        M = [[S[1][p][q] for q in idx] for p in idx]; b = [S[2][p] for p in idx]; n = len(idx)
        try:
            for c in range(n):
                piv = max(range(c, n), key=lambda r: abs(M[r][c]))
                if abs(M[piv][c]) < 1e-9: raise ZeroDivisionError
                M[c], M[piv] = M[piv], M[c]; b[c], b[piv] = b[piv], b[c]
                for r in range(n):
                    if r != c:
                        t = M[r][c] / M[c][c]; M[r] = [x - t * yy for x, yy in zip(M[r], M[c])]; b[r] -= t * b[c]
            sol = [b[c] / M[c][c] for c in range(n)]
        except ZeroDivisionError:
            continue
        if any(v < -1e-9 for v in sol): continue
        gain = sum(v * S[2][p] for v, p in zip(sol, idx))        # baisse de la somme des carrés = x·Xty (à l'optimum)
        if gain > best + 1e-12:
            best = gain; bx = [0.0, 0.0, 0.0]
            for p, v in zip(idx, sol): bx[p] = v
    return dict(a=bx[0], b=bx[1], c=-bx[2])


STATS = collections.defaultdict(zero); PAR_CLE = collections.defaultdict(lambda: collections.defaultdict(zero))
for x in F:
    if not x["paye"]: continue
    for k in ((x["systeme"], x["groupe"]), (x["systeme"], GEN)):
        ajoute(STATS[k], x["v"], x["y"]); ajoute(PAR_CLE[x["cle"]][k], x["v"], x["y"])
GROUPES = sorted({x["groupe"] for x in F})


def modele(cache=None):
    """règles, prix propres et conversion, sans le sort « cache » (une clé)"""
    sub = PAR_CLE.get(cache, {}) if cache else {}
    st = lambda k: moins(STATS[k], sub[k]) if k in sub else STATS[k]
    co = {}
    for s in AUTRES:
        gen = st((s, GEN)); co[(s, GEN)] = resoudre(gen, [0, 1, 2])
        for g in GROUPES:
            S = st((s, g))
            if S[0] >= MIN: co[(s, g)] = resoudre(S, [1, 2] if g in ("blessure", "soin") else [0, 1, 2])
    pg = plus(*[st((s, GEN)) for s in AUTRES]); co[("D&D 5", GEN)] = resoudre(pg, [0, 1, 2])
    for g in GROUPES:
        S = plus(*[st((s, g)) for s in AUTRES])
        if S[0] >= MIN: co[("D&D 5", g)] = resoudre(S, [1, 2] if g in ("blessure", "soin") else [0, 1, 2])
    def regle(s, g):
        r = co.get((s, g)) or dict(co[(s, GEN)])
        if g in ("blessure", "soin"): r = dict(r, a=0.0)
        return r
    pp = collections.defaultdict(list)
    for x in F:
        if x["unique"] is None or x["cle"] == cache: continue
        r = regle(x["systeme"], x["groupe"])
        pp[(x["unique"], x["systeme"])].append(x["niveau"] - x["a"]["decides"] - (r["a"] * x["v"][0] + r["b"] * x["v"][1] - r["c"] * x["v"][2]))
    pm = {k: statistics.median(v) for k, v in pp.items()}
    conv = {"D&D 5": 0.0}
    for s in AUTRES:
        d = [pm[(u, "D&D 5")] - pm[(u, s)] for (u, ss) in pm if ss == s and (u, "D&D 5") in pm]
        conv[s] = statistics.median(d) if d else 0.0
    inar, src_ = {}, {}
    for u in {u for (u, s) in pm}:
        if (u, "D&D 5") in pm: inar[u] = pm[(u, "D&D 5")]; src_[u] = "D&D 5"
        else:
            cv = [pm[(u, s)] + conv[s] for s in AUTRES if (u, s) in pm]
            inar[u] = statistics.median(cv); src_[u] = "autres systèmes, convertis"
    return dict(regle=regle, pm=pm, pn={k: len(v) for k, v in pp.items()}, conv=conv, inar=inar, src=src_, co=co)


def calcul(x, M, mode):
    """(coût, palier, relations, prix des effets) ; mode « propre » (unités du système) ou « inarama »"""
    a = x["a"]; s = x["systeme"]
    prix = []
    for e in a["effets"]:
        if not e["sans_prix"]: prix.append((e["prix"], "prix du calcul")); continue
        u = e["cercle"]
        if mode == "propre":
            if (u, s) in M["pm"]: prix.append((M["pm"][(u, s)], f"prix propre ({s})"))
            elif u in M["inar"]: prix.append((M["inar"][u] - M["conv"][s], "prix d'Inarama, ramené au système"))
            else: prix.append((3.0, "aucun prix propre : défaut 3,0"))
        else:
            if u in M["inar"]: prix.append((M["inar"][u], "prix d'Inarama (" + M["src"][u] + ")"))
            else: prix.append((3.0, "aucun prix propre : défaut 3,0"))
    pe = BC.combiner([p for p, _ in prix], a.get("suggestion")) if prix else 0.0
    r = M["regle"](s if mode == "propre" else "D&D 5", x["groupe"])
    rel = r["a"] * x["v"][0] + r["b"] * x["v"][1] - r["c"] * x["v"][2]
    cout = pe + a["decides"] + rel
    return round(cout, 3), int(min(10, max(0, math.floor(cout + 0.5)))), round(rel, 3), prix, r


M0 = modele(None)
for x in F:
    x["propre"] = calcul(x, M0, "propre"); x["inarama"] = calcul(x, M0, "inarama")
cles = sorted({x["cle"] for x in F})
par_cle = collections.defaultdict(list)
for x in F: par_cle[x["cle"]].append(x)
for i, c in enumerate(cles):
    M = modele(c)
    for x in par_cle[c]:
        x["propre_c"] = calcul(x, M, "propre"); x["inarama_c"] = calcul(x, M, "inarama")
    if i % 500 == 0: print("sort caché", i, "/", len(cles), flush=True)


# ---------------------------------------------------------------- mesure
def st(xs, cle_):
    xs = [x for x in xs if not x["a"]["sans_impact"]]
    if not xs: return "—"
    d = [x[cle_][1] - x["niveau"] for x in xs]; n = len(d)
    pc = lambda k: 100 * sum(1 for e in d if abs(e) <= k) / n
    return f"{n:5d} | {pc(0):5.1f} % | {pc(1):5.1f} % | {pc(2):5.1f} % | {sum(d) / n:+.2f}"
def deux(xs, c1, c2): return f"{st(xs, c1)}   ||   {st(xs, c2)}"


avec = [x for x in F if not x["a"]["sans_impact"]]
dnd = [x for x in avec if x["systeme"] == "D&D 5"]
T = ["MESURE DU BARÈME PAR CERCLES, VERSION 2 — un barème par système, conversion au cercle, « sort caché »",
     "Branche bareme-cercles (bibliothèque de main 33016e2, aucune forme changée). Formes : celles qui ont un cercle d'Impact, hors Elden Ring.",
     "Colonnes : formes | bon palier | à 1 près | à 2 près | écart moyen (palier − niveau). À gauche, SORT CACHÉ (relations, prix propres et",
     "conversion recalculés sans le sort mesuré) ; à droite, SANS CACHER.", ""]
T += ["A. D&D 5 (5e et 2024) — palier d'Inarama", "=" * 40, "", f"  {'':22s} {'sort caché':^44s}   ||   {'sans cacher':^44s}",
      f"  ensemble              {deux(dnd, 'inarama_c', 'inarama')}", f"  5e                    {deux([x for x in dnd if x['jeu'] == '5e'], 'inarama_c', 'inarama')}",
      f"  2024                  {deux([x for x in dnd if x['jeu'] == '2024'], 'inarama_c', 'inarama')}", "", "  par tranche :"]
for t in ["0", "1-2", "3-4", "5-6", "7-9"]: T.append(f"    {t:20s}{deux([x for x in dnd if tranche(x['niveau']) == t], 'inarama_c', 'inarama')}")
T += ["", "  par genre :"]
for g in sorted({x["a"]["genre"] for x in dnd}, key=lambda g: -sum(1 for x in dnd if x["a"]["genre"] == g)):
    T.append(f"    {g:20s}{deux([x for x in dnd if x['a']['genre'] == g], 'inarama_c', 'inarama')}")
T += ["", "  Les 40 formes de D&D 5 les plus loin de leur niveau (sort caché), avec le détail :", ""]
def detail(x, k):
    cout, pal, rel, prix, r = x[k]
    L = [f"  {x['sort']} ({x['cle']}, {x['jeu']}) — « {x['forme']} » — niveau {x['niveau']}, coût {cout:.2f}, palier {pal} (écart {pal - x['niveau']:+d})"]
    m = x["a"]["mesures"]
    L.append(f"      genre {x['a']['genre']} ; groupe {x['groupe']} ; cibles {m['cibles']} ({m['cibles_lecture']}) ; marche {m['marche']} ; "
             f"restriction {', '.join(m['restriction']) or 'non'} ; règle a {r['a']:.2f} b {r['b']:.2f} c {r['c']:.2f} → relations {rel:+.2f}")
    for (p, why), e in zip(prix, x["a"]["effets"]):
        L.append(f"      effet {' · '.join(e['cercle'][2]).lower() or 'sans mot'} {json.loads(e['cercle'][1])} : {p:+.2f} — {why}")
    for d in x["a"]["detail"]:
        if d["cercle"] != "IMPACT": L.append(f"      {d['cercle']} : {d['prix']:+.2f} — {d['regle']}")
    return L
for x in sorted(dnd, key=lambda x: (-abs(x["inarama_c"][1] - x["niveau"]), -abs(x["inarama_c"][0] - x["niveau"])))[:40]: T += detail(x, "inarama_c")
T += ["", "", "B. 3.5, PF1, PF2", "=" * 16, "",
      "  Dans leurs propres unités (règles et prix propres du système), puis convertis (prix d'Inarama, règles de D&D 5), face au niveau de",
      "  leur source. Sort caché || sans cacher.", ""]
for s in AUTRES:
    xs = [x for x in avec if x["systeme"] == s]
    T += [f"  {s}", f"    propres unités        {deux(xs, 'propre_c', 'propre')}", f"    converti (Inarama)    {deux(xs, 'inarama_c', 'inarama')}", "    par tranche (propres unités, sort caché) :"]
    for t in ["0", "1-2", "3-4", "5-6", "7-9", "10"]:
        g = [x for x in xs if tranche(x["niveau"]) == t]
        if g: T.append(f"      {t:18s}{st(g, 'propre_c')}")
    T.append("    par genre (propres unités, sort caché) :")
    for g in sorted({x["a"]["genre"] for x in xs}, key=lambda g: -sum(1 for x in xs if x["a"]["genre"] == g)):
        T.append(f"      {g:18s}{st([x for x in xs if x['a']['genre'] == g], 'propre_c')}")
    T.append("")
T += [f"  Conversion au cercle (sans cacher) : " + " ; ".join(f"{s} {M0['conv'][s]:+.2f}" for s in AUTRES)
      + f"  (sur {', '.join(str(sum(1 for (u, ss) in M0['pm'] if ss == s and (u, 'D&D 5') in M0['pm'])) + ' cercles (' + s + ')' for s in AUTRES)})", "", ""]
# C. plus fort = plus cher
rep = {e["id"]: e for e in json.load(open(os.path.join(DOCS, "repertoire_cercles.json"), encoding="utf-8"))["cercles"]}
pa = json.load(open(os.path.join(DOCS, "paires_cercles.json"), encoding="utf-8"))
idx = {(x["cle"], x["jeu"], x["forme"]): x for x in F}
FORT = {"IMPACT", "AMPLEUR", "LOCALISATION", "QUANTITE", "DUREE", "FORME"}
def plus_fort(ca, cb):
    if ca is None or cb is None:
        c = rep[ca or cb]; sgn = 1 if ca else -1
        return sgn if c["type"] in FORT else -sgn if c["type"] in ("CONDITION", "COMPOSANTE") else 0
    a, b = rep[ca], rep[cb]
    if a["type"] != b["type"] or a["mots"] != b["mots"] or a["satellites"] != b["satellites"] or a["type"] not in FORT: return 0
    va, vb = a["valeur"], b["valeur"]
    if va == vb: return 0
    if va == "plein": return 1
    if vb == "plein": return -1
    return (1 if va > vb else -1) if isinstance(va, (int, float)) and isinstance(vb, (int, float)) else 0
viol, tot = [], 0
for p in pa["paires"]:
    fa, fb = pa["formes"][p["a"]], pa["formes"][p["b"]]
    if fa["jeu"] != fb["jeu"]: continue
    s_ = plus_fort(p["cercle_a"], p["cercle_b"])
    xa, xb = idx.get((fa["cle"], fa["jeu"], fa["forme"])), idx.get((fb["cle"], fb["jeu"], fb["forme"]))
    if not s_ or not xa or not xb: continue
    tot += 1
    fort, faible = (xa, xb) if s_ > 0 else (xb, xa)
    if fort["inarama_c"][1] < faible["inarama_c"][1]: viol.append((fort, faible))
T += ["C. « PLUS FORT = PLUS CHER » (palier d'Inarama, sort caché)", "=" * 57, "",
      f"  Paires à un cercle près, même édition, où l'on sait lequel est le plus fort : {tot} ; le plus fort reçoit un palier plus bas : {len(viol)}.", ""]
for fo, fa_ in viol[:40]:
    T.append(f"    {fo['sort']} ({fo['jeu']}) « {fo['forme']} » palier {fo['inarama_c'][1]}  <  {fa_['sort']} « {fa_['forme']} » palier {fa_['inarama_c'][1]}")
T += ["", ""]
# D. lacunes
def table_md(path, titre, col):
    txt = open(path, encoding="utf-8").read(); i = txt.find(titre)
    if i < 0: return set()
    hdr, out = None, set()
    for l in txt[i:].split("\n")[1:]:
        if l.startswith("## "): break
        if l.startswith("| Sort"): hdr = [c.strip() for c in l.strip("|").split("|")]; continue
        if hdr and l.startswith("|") and not l.startswith("|---"):
            cs = [c.strip() for c in l.strip("|").split("|")]
            if len(cs) >= len(hdr) and col in hdr and cs[hdr.index(col)].lower().startswith("oui"): out.add((cs[0], cs[1]))
    return out
jet = set()
for nom in os.listdir(DOCS):
    if nom.startswith("releve_etats_"): jet |= table_md(os.path.join(DOCS, nom), "## D.", "Jet renouvelé")
txt = open(os.path.join(DOCS, "releve_bonus_mecaniques.md"), encoding="utf-8").read()
bonus = {tuple(c.strip() for c in l.strip("|").split("|")[:2]) for l in txt[txt.find("## A."):txt.find("## B.")].split("\n")
         if l.startswith("|") and not l.startswith("| Sort") and not l.startswith("|---")}
causeA = set()
for l in open(os.path.join(DOCS, "bareme_etape3b_desaccords.md"), encoding="utf-8").read().split("\n"):
    cs = [c.strip() for c in l.strip().strip("|").split("|")]
    m = re.match(r"plein «(.*?)»$", cs[0]) if len(cs) >= 8 else None
    if m and cs[5].startswith("A"):                  # colonne « Cause » : A, ou A + B
        causeA.add(tuple(w.strip().upper() for w in m.group(1).split("·") if w.strip()))
def jd(x): return {"PF2 remaniée": "PF2"}.get(x["jeu"], x["jeu"])
sig_sys = collections.Counter((x["sig"], x["systeme"]) for x in avec)
LAC = {
    "zones sans Forme ni taille (Cible « une zone » sans Forme, Forme sans Ampleur, figures à part)":
        lambda x: any(("zone sans" in l) or ("figure à part" in l) for l in x["a"]["lacunes"]),
    "cercles d'Impact « plein » de cause A (étape 3b : un même cercle pour des sorts sans rapport)":
        lambda x: any(w in causeA for w in x["impacts_plein"]),
    "jet renouvelé (relevés des états)": lambda x: (x["sort"], jd(x)) in jet,
    "mécaniques des bonus (relevé des bonus)": lambda x: (x["sort"], jd(x)) in bonus,
    "jumelles (même glyphe, même système, autre forme)": lambda x: sig_sys[(x["sig"], x["systeme"])] > 1,
    "puissance inférieure à 1 (puissance 1 écrite, 4 êtres ou plus)": lambda x: x["puissance1"] and x["a"]["mesures"]["instances"] >= 4,
}
T += ["D. LE POIDS DE CHAQUE LACUNE D'ÉCRITURE (sort caché, propres unités ; D&D 5 = palier d'Inarama)", "=" * 88, "",
      "  (formes | bon | à 1 | à 2 | écart moyen ; puis l'écart absolu moyen)", ""]
def ab(xs, k): return sum(abs(x[k][1] - x["niveau"]) for x in xs) / len(xs) if xs else 0
sans = [x for x in avec if not any(fn(x) for fn in LAC.values())]
for nom, fn in list(LAC.items()) + [("formes sans aucune de ces lacunes", lambda x: x in sans)]:
    xs = [x for x in avec if fn(x)]
    T.append(f"  {nom}")
    T.append(f"      {st(xs, 'propre_c')} ; écart absolu {ab(xs, 'propre_c'):.2f} ; par système : " + ", ".join(f"{s} {sum(1 for x in xs if x['systeme'] == s)}" for s in SYSTEMES))
T += ["", f"  Cercles de cause A reconnus (Impact plein, mots de l'étape 3b) : {len(causeA)}.", "", ""]
# E. écarts de 2 ou plus
loin = [x for x in avec if abs(x["inarama_c"][1] - x["niveau"]) >= 2]
T += ["E. LES FORMES DONT LE PALIER D'INARAMA S'ÉCARTE DE 2 OU PLUS DU NIVEAU DE LEUR SOURCE (sort caché)", "=" * 92, "",
      f"  {len(loin)} formes sur {len(avec)}.", ""]
T.append(f"  {'système':10s}" + "".join(f"{t:>8s}" for t in ["0", "1-2", "3-4", "5-6", "7-9", "10"]) + f"{'total':>8s}")
for s in SYSTEMES:
    T.append(f"  {s:10s}" + "".join(f"{sum(1 for x in loin if x['systeme'] == s and tranche(x['niveau']) == t):8d}" for t in ["0", "1-2", "3-4", "5-6", "7-9", "10"])
             + f"{sum(1 for x in loin if x['systeme'] == s):8d}")
T += ["", "  La liste (système, sort, jeu, forme, niveau → palier) :", ""]
for x in sorted(loin, key=lambda x: (SYSTEMES.index(x["systeme"]), x["sort"], x["forme"])):
    T.append(f"  {x['systeme']:6s} {x['sort']} ({x['jeu']}) « {x['forme']} » : {x['niveau']} → {x['inarama_c'][1]} ({x['inarama_c'][1] - x['niveau']:+d})")
open(os.path.join(OUT, "mesure_bareme_cercles_v2.txt"), "w", encoding="utf-8").write("\n".join(T) + "\n")

# ---------------------------------------------------------------- fichiers
ids = {}
for e in json.load(open(os.path.join(DOCS, "repertoire_cercles.json"), encoding="utf-8"))["cercles"]:
    ids[(e["type"], json.dumps(e["valeur"], ensure_ascii=False), tuple(e["mots"]), tuple(json.dumps(s, ensure_ascii=False) for s in e["satellites"]))] = e["id"]
def ident(u): return ids.get(u) or ids.get((u[0], u[1], u[2], tuple(json.dumps(json.loads(s), ensure_ascii=False) for s in u[3])))
PRIX = []
for u in sorted({u for (u, s) in M0["pm"]}, key=lambda u: ident(u) or ""):
    par = {s: dict(prix=round(M0["pm"][(u, s)], 3), formes=M0["pn"][(u, s)], converti=round(M0["pm"][(u, s)] + M0["conv"][s], 3)) for s in SYSTEMES if (u, s) in M0["pm"]}
    PRIX.append(dict(id=ident(u), type=u[0], valeur=json.loads(u[1]), mots=list(u[2]), satellites=[json.loads(s) for s in u[3]], par_systeme=par,
                     prix_inarama=round(M0["inar"][u], 3), source=M0["src"][u]))
json.dump(dict(_lisez_moi="Prix propres des cercles d'Impact sans prix (effets uniques), identifiés comme au répertoire (satellites compris). "
                          "par_systeme : prix propre médian dans le système (niveau − prix décidés − relations du système, sur les formes où le "
                          "cercle est le seul effet d'Impact), nombre de formes, prix converti (+ conversion du système). prix_inarama : le prix "
                          "en D&D 5 s'il existe, sinon le médian des prix convertis. Calcul sans cacher (sur toute la bibliothèque).",
               conversion=M0["conv"], cercles=PRIX), open(os.path.join(OUT, "prix_cercles_v2.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
def fiche(x):
    out = dict(cle=x["cle"], sort=x["sort"], jeu=x["jeu"], systeme=x["systeme"], forme=x["forme"], niveau=x["niveau"], genre=x["a"]["genre"], groupe=x["groupe"],
               mesures=x["a"]["mesures"], lacunes=x["a"]["lacunes"], prix_decides=x["a"]["decides"], detail=x["a"]["detail"])
    for k, nom in (("inarama_c", "inarama_sort_cache"), ("inarama", "inarama_sans_cacher"), ("propre_c", "systeme_sort_cache"), ("propre", "systeme_sans_cacher")):
        if k in x:
            c, p, rel, prix, r = x[k]
            out[nom] = dict(cout=c, palier=p, relations=rel, regle=r, effets=[dict(cercle=ident(e["cercle"]), prix=round(pp, 3), regle=why) for (pp, why), e in zip(prix, x["a"]["effets"])])
    return out
json.dump(dict(_lisez_moi="Pour chaque forme (hors Elden Ring) : palier d'Inarama (prix d'Inarama, règles de D&D 5) et palier dans son système "
                          "(règles et prix propres du système), chacun « sort caché » et « sans cacher » ; le détail cercle par cercle avec la "
                          "règle ; les mesures lues sur le glyphe.", formes=[fiche(x) for x in F]),
          open(os.path.join(OUT, "couts_formes_cercles_v2.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=str)
json.dump(dict(conv=M0["conv"], causeA=len(causeA), viol=len(viol), tot=tot, loin=len(loin), prix=len(PRIX),
               sans_inar=sum(1 for x in avec for e in x["a"]["effets"] if e["sans_prix"] and e["cercle"] not in M0["inar"]),
               regles={f"{s}|{g}": v for (s, g), v in M0["co"].items()}),
          open(os.path.join(OUT, "comptes_v2.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("D&D 5 caché :", st(dnd, "inarama_c"), "| sans cacher :", st(dnd, "inarama"), "| conversion", {k: round(v, 2) for k, v in M0["conv"].items()})
