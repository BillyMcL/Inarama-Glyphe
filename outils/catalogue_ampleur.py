"""Catalogue des prix des cercles, lot 3 : la Forme et l'Ampleur ensemble ; et les décisions du lot 2 (26 novembre 2026). Un calcul.

    python outils/catalogue_ampleur.py <dossier de sortie> <dossier des documents du barème> <repertoire_cercles_v6.json> <catalogue_prix.json>

Décisions de l'utilisateur appliquées dans ce calcul (le moteur du barème ne change pas) :
1. Inarama se cale sur la 5e (2014) seule ; la 2024 est convertie comme les autres éditions (méthode a : rapport des pentes coût →
   niveau). Une règle que la 5e ne peut pas régler (moins de 10 formes) prend celle des autres éditions ensemble, convertie.
2. Une règle en place qui ne tient pas dans une édition y est remplacée par la règle réglée sur elle (relation « cibles » en 2024 ;
   officiants en PF2 remaniée ; puissance des êtres appelés en 3.5 et PF1 ; montant multiplié des blessures en 3.5, PF1, PF2) ; réglée
   sans le sort mesuré (sort caché).
3. Tous les cercles de Forme d'un glyphe sont lus (formes composées).
4. Une même Forme a un seul prix, quelle que soit la position de son satellite (la Forme « unifiée » : valeur, mots, satellites de
   proportion et d'angle, sans leur position ni le satellite d'Ampleur).
5. Une Forme en satellite d'un Impact fait agir cet Impact comme une zone (relation « cibles » quand sa taille est lisible).
Lot 3 : la Forme et son Ampleur se règlent ensemble (le couple : p de la Forme + relation à la taille : le tableau du guide pour les
formes qu'il connaît, a × log2(cibles), a par édition ; une pente libre b × log2(taille) pour les autres) ; l'Ampleur sans Forme a son
propre prix, s × log2(taille), par sorte (porteur et mots).
"""
import os, sys, json, math, collections, statistics, re
ICI = os.path.dirname(os.path.abspath(__file__))
OUT, DOCS, REP, CAT = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
RAPIDE = os.environ.get("RAPIDE")
V8 = os.path.join(ICI, "mesure_bareme_cercles_v8.py")
src = open(V8, encoding="utf-8").read()
src = src[:src.index("M0 = modele(None)")]
src = src.replace('''        F.append(x)\n''', '''        x["_f"] = dict(rings=f["rings"], verb=f.get("verb"))\n        F.append(x)\n''', 1)
ns = {"__file__": V8, "__name__": "v8"}
sys.argv = [V8, OUT, DOCS]
exec(compile(src, V8, "exec"), ns)
F, BC, modele, calcul = ns["F"], ns["BC"], ns["modele"], ns["calcul"]
EDITIONS = ["5e", "2024", "3.5", "PF1", "PF2", "PF2 remaniée"]
MIN, PLANCHER, REF = 10, 0.01, "5e"

rep = json.load(open(REP, encoding="utf-8"))["cercles"]
IDS = {}
for e in rep:
    IDS[(e["type"], json.dumps(e["valeur"], ensure_ascii=False), tuple(e["mots"]), tuple(json.dumps(s, ensure_ascii=False) for s in e["satellites"]))] = e["id"]
def ident(u): return IDS.get(u) or IDS.get((u[0], u[1], u[2], tuple(json.dumps(json.loads(s), ensure_ascii=False) for s in u[3])))
CR = {e["id"]: e for e in rep}
def _txt(s): return s[2] if len(s) > 2 and isinstance(s[2], str) else ""
def num(v): return isinstance(v, (int, float)) and not isinstance(v, bool)
def f2(v, d=2): return "—" if v is None else f"{v:.{d}f}"
def sats(r): return list(r[4]) if len(r) > 4 and r[4] else []


def refait(x, rings):
    a = BC.analyse(dict(rings=rings, verb=x["_f"]["verb"]))
    m = a["mesures"]
    g = ("état : " + (a["famille"] or "?")) if a["genre"] == "état" else a["genre"]
    fg = m.get("figure")
    return dict(x, a=a, groupe=g, v=(math.log2(max(m["cibles"], 1)), m["marche"], -(1.0 if m["restriction"] else 0.0), -(1.0 if m.get("sursaut") else 0.0)),
                fig=(fg[0], fg[1]) if fg and fg[1] is not None else None, fig_nom=fg[0] if fg else None)


# ---------------------------------------------------------------- les Formes (toutes, unifiées) et leurs Ampleurs
NOMS = {"plein": "sphère", 4: "cube", 3: "cône", 1: "ligne", 9: "cylindre", 2: "plan"}
def forme_unifiee(r):
    """la Forme sans la position de ses satellites ni son satellite d'Ampleur : (valeur, mots, satellites de proportion et d'angle)"""
    ss = sorted(json.dumps(s_[1], ensure_ascii=False) for s_ in sats(r) if not _txt(s_).startswith("AMPLEUR"))
    return (json.dumps(r[1], ensure_ascii=False), tuple(r[2]), tuple(ss))
def nom_forme(fu, lecture):
    v = json.loads(fu[0]); ws = fu[1]; rd = lecture.lower()
    if "EXPLOSION" in ws: return "sphère « explosion »"
    if "PONT" in ws: return "ligne « pont »"
    for k in ("hélice", "calotte", "paroi", "disque", "plan"):
        if rd.startswith(k) or k in rd.split(" ;")[0]: return k + (" « " + " · ".join(w.lower() for w in ws) + " »" if ws else "")
    return NOMS.get(v, str(v)) + (" « " + " · ".join(w.lower() for w in ws) + " »" if ws else "")
GUIDE = {"sphère": 5, "cylindre": 5, "cube": 5, "cône": 10, "ligne": 30}
def cibles_guide(nom, taille, unite):
    """le nombre de cibles du tableau du guide (en pieds) pour une taille écrite (m³ ou m)"""
    if nom not in GUIDE or not taille: return None
    if unite == "longueur" or nom == "ligne": dim = taille
    elif nom == "sphère": dim = (3 * taille / (4 * math.pi)) ** (1 / 3)
    elif nom == "cube": dim = taille ** (1 / 3)
    elif nom == "cylindre": dim = (taille / (2 * math.pi)) ** (1 / 3)
    else: dim = (12 * taille / math.pi) ** (1 / 3)
    pieds = max(5, 5 * round(dim / 0.3048 / 5))
    return max(1, math.ceil(pieds / GUIDE[nom]))
def ampleur_de(rings, i):
    """(taille en unités de base, unité, cercle ou satellite d'Ampleur, id) de la Forme du cercle i"""
    r = rings[i]
    for s_ in sats(r):
        t = _txt(s_).split()
        if t[:1] == ["AMPLEUR"] and num(s_[1]) and tuple(t[1:]) in BC.UNITE_BASE:
            return s_[1] * BC.UNITE_BASE[tuple(t[1:])], ("longueur" if t[1] in ("LONGUEUR", "DIAMETRE") else "surface" if t[1] == "SURFACE" else "volume"), "satellite", ident(BC.cle_cercle(r))
    if i + 1 < len(rings) and rings[i + 1][0] == "AMPLEUR":
        a = rings[i + 1]
        if num(a[1]) and tuple(a[2]) in BC.UNITE_BASE:
            return a[1] * BC.UNITE_BASE[tuple(a[2])], ("longueur" if a[2][0] in ("LONGUEUR", "DIAMETRE") else "surface" if a[2][0] == "SURFACE" else "volume"), "cercle", ident(BC.cle_cercle(a))
    return None, None, None, None


# ---------------------------------------------------------------- relevé des formes
VAR = []
for x in F:
    if x["a"]["sans_impact"]: continue
    rings = x["_f"]["rings"]; d = dict(x=x, formes=[], ampl_sf=[])
    pris = set()
    for i, r in enumerate(rings):
        if r[0] == "FORME":
            fu = forme_unifiee(r); nom = nom_forme(fu, r[3])
            t, u, ou, aid = ampleur_de(rings, i)
            if ou == "cercle": pris.add(i + 1)
            sv = next(((s_[1], _txt(s_)) for s_ in sats(r) if _txt(s_).startswith("AMPLEUR")), None) if ou == "satellite" else None
            d["formes"].append(dict(fu=fu, nom=nom, id=ident(BC.cle_cercle(r)), taille=t, unite=u, ampl_id=aid, ampl_ou=ou, ampl_sat=sv,
                                    n=cibles_guide(nom.split(" «")[0], t, u)))
    d["zone_fi"] = []
    for i, r in enumerate(rings):                              # l'Ampleur sans Forme : cercles non pris, satellites hors Forme
        if r[0] == "AMPLEUR" and i not in pris and num(r[1]) and tuple(r[2]) in BC.UNITE_BASE:
            d["ampl_sf"].append(dict(sorte="cercle d'Ampleur « " + " · ".join(w.lower() for w in r[2]) + " »", taille=r[1] * BC.UNITE_BASE[tuple(r[2])],
                                     id=ident(BC.cle_cercle(r)), porteur=None, rings=[q for k, q in enumerate(rings) if k != i]))
        if r[0] != "FORME":
            for j, s_ in enumerate(sats(r)):
                t = _txt(s_).split()
                if t[:1] == ["AMPLEUR"]:
                    v = s_[1]; mots = tuple(t[1:])
                    base = BC.UNITE_BASE.get(mots) or BC.UNITE_BASE.get(("LONGUEUR",) + mots) or (1 if mots and mots[-1] in ("METRES",) else 1e3 if mots[-1:] == ("KILOMETRES",) else 1)
                    if not num(v): continue
                    fs = [s2 for s2 in sats(r) if _txt(s2).split()[:1] == ["FORME"]] if r[0] == "IMPACT" else []
                    if fs:                                     # décision 5 : l'Ampleur d'une Forme en satellite d'un Impact
                        nm = NOMS.get(fs[0][1], str(fs[0][1]))
                        d["zone_fi"].append(dict(porteur=ident(BC.cle_cercle(r)), forme=f"{nm} ({_txt(fs[0])})", valeur=v, mots=mots,
                                                 n=cibles_guide(nm, v * base, "longueur" if "LONGUEUR" in mots else "volume")))
                        continue
                    rr = list(rings); rr[i] = (*r[:4], [q for k, q in enumerate(sats(r)) if k != j], *r[5:])
                    d["ampl_sf"].append(dict(sorte=f"{r[0].capitalize()} : Ampleur « {' · '.join(w.lower() for w in mots)} »", taille=v * base,
                                             id=None, porteur=ident(BC.cle_cercle(r)), valeur=v, mots=mots, rings=rr))
    # décision 5 : un satellite de Forme sur un Impact
    d["forme_sur_impact"] = [(ident(BC.cle_cercle(r)), s_[1], _txt(s_)) for r in rings if r[0] == "IMPACT" for s_ in sats(r) if _txt(s_).split()[:1] == ["FORME"]]
    # décision 2 : les variantes des règles
    off = [(i, j) for i, r in enumerate(rings) if r[0] == "CONDITION" for j, s_ in enumerate(sats(r)) if (_txt(s_).startswith("OFFICIANT") or not _txt(s_)) and num(s_[1])]
    if off:
        rr = list(rings)
        for i in {i for i, _ in off}:
            r = rr[i]; rr[i] = (*r[:4], [s_ for j, s_ in enumerate(r[4]) if (i, j) not in off], *r[5:])
        d["sans_off"] = refait(x, rr)
    if x["a"]["genre"] == "être appelé" and len(x["a"]["effets"]) == 1:
        rg = next((dd["regle"] for dd in x["a"]["detail"] if dd["cercle"] == "IMPACT"), "")
        m_ = re.search(r"(?:puissance|animation) ([\d.]+).*?log2\((\d+)\)", rg)
        if m_: d["etre"] = (float(m_.group(1)), math.log2(max(int(m_.group(2)), 1)))
    if x["a"]["genre"] == "blessure" and len(x["a"]["effets"]) == 1:
        d["bm"] = x["a"]["mesures"]["instances"] > 1 and not x["a"]["mesures"]["zone"]
    VAR.append(d)
print("formes", len(VAR))

M0 = modele(None)
par_cle = collections.defaultdict(list)
for d in VAR: par_cle[d["x"]["cle"]].append(d)
cles = sorted(par_cle)
for i, c in enumerate(cles):
    M = modele(c) if not (RAPIDE and i > 40) else M0
    for d in par_cle[c]:
        x = d["x"]
        cc, _, _, _, r = calcul(x, M, "propre")
        d["cout_c"] = cc; d["a_regle"] = r.get("a", 0.0)
        d["cout0_c"] = calcul(dict(x, v=(0.0,) + tuple(x["v"][1:]), fig=None), M, "propre")[0]
        d["cout"] = calcul(x, M0, "propre")[0]
        if "sans_off" in d: d["off_c"] = calcul(d["sans_off"], M, "propre")[0]
        for a_ in d["ampl_sf"]: a_["sans_c"] = calcul(refait(x, a_["rings"]), M, "propre")[0]
    if i % 500 == 0: print("sort caché", i, "/", len(cles), flush=True)


def ed(d): return d["x"]["jeu"]
def droite(pts):
    n = len(pts)
    if n < 3: return None
    mx = statistics.mean(p[0] for p in pts); my = statistics.mean(p[1] for p in pts)
    sxx = sum((p[0] - mx) ** 2 for p in pts)
    if not sxx: return None
    b = sum((p[0] - mx) * (p[1] - my) for p in pts) / sxx
    return b, my - b * mx
def pente0(pts):
    den = sum(L * L for L, _ in pts); return max(0.0, sum(L * y for L, y in pts) / den) if den else None
def palier(c): return int(min(10, max(0, math.floor(c + 0.5))))
def score(ecarts):
    n = len(ecarts)
    return (n, 100 * sum(1 for e in ecarts if abs(e) <= 1) / n if n else None, statistics.mean(abs(e) for e in ecarts) if n else None,
            statistics.mean(ecarts) if n else None)


# ---------------------------------------------------------------- décision 2 : les règles remplacées (réglées sans le sort mesuré)
REMPLACE = {"cibles": ["2024"], "officiants": ["PF2 remaniée"], "êtres": ["3.5", "PF1"], "blessures": ["3.5", "PF1", "PF2"]}
def regle_cibles(ds):
    pts = [(d["x"]["v"][0], d["x"]["niveau"] - (d["cout_c"] - d["a_regle"] * d["x"]["v"][0])) for d in ds if d["x"]["a"]["genre"] not in ("blessure", "soin")]
    dr = droite(pts); return max(0.0, dr[0]) if dr else None
def regle_off(ds):
    pts = [(d["off_c"] - d["cout_c"], d["x"]["niveau"] - d["off_c"]) for d in ds if "off_c" in d and d["off_c"] - d["cout_c"] > 0]
    den = sum(r * r for r, _ in pts); return (-sum(r * y for r, y in pts) / den) if den else None
def regle_etres(ds):
    pts = [(d["etre"][0], d["etre"][1], d["x"]["niveau"] - (d["cout_c"] - d["etre"][0] - d["etre"][1])) for d in ds if "etre" in d]
    if len(pts) < 5: return None
    # moindres carrés y = α p + β l + γ
    S = [[0.0] * 3 for _ in range(3)]; b = [0.0] * 3
    for p, l, y in pts:
        v = (p, l, 1.0)
        for i in range(3):
            b[i] += v[i] * y
            for j in range(3): S[i][j] += v[i] * v[j]
    try:
        for c in range(3):
            piv = max(range(c, 3), key=lambda r: abs(S[r][c]))
            if abs(S[piv][c]) < 1e-9: return None
            S[c], S[piv] = S[piv], S[c]; b[c], b[piv] = b[piv], b[c]
            for r in range(3):
                if r != c:
                    t = S[r][c] / S[c][c]; S[r] = [a - t * q for a, q in zip(S[r], S[c])]; b[r] -= t * b[c]
        return tuple(b[c] / S[c][c] for c in range(3))
    except ZeroDivisionError:
        return None
def regle_bm(ds):
    mu = [d["x"]["niveau"] - d["cout_c"] for d in ds if d.get("bm")]; so = [d["x"]["niveau"] - d["cout_c"] for d in ds if d.get("bm") is False]
    return (statistics.mean(mu) - statistics.mean(so)) if mu and so else None
def delta(d, R, sans_cibles=False):
    """le changement de coût d'une forme quand les règles réglées R remplacent les règles en place"""
    x = d["x"]; e = ed(d); dt = 0.0
    if not sans_cibles and e in REMPLACE["cibles"] and R.get("cibles") is not None and x["a"]["genre"] not in ("blessure", "soin"): dt += (R["cibles"] - d["a_regle"]) * x["v"][0]
    if e in REMPLACE["officiants"] and R.get("officiants") is not None and "off_c" in d: dt += (1 - R["officiants"]) * (d["off_c"] - d["cout_c"])
    if e in REMPLACE["êtres"] and R.get("êtres") and "etre" in d:
        al, be, ga = R["êtres"]; dt += (al - 1) * d["etre"][0] + (be - 1) * d["etre"][1] + ga
    if e in REMPLACE["blessures"] and R.get("blessures") is not None and d.get("bm"): dt += R["blessures"]
    return dt
AVANT_APRES, REGLES_EDITION = {}, {}
for e in EDITIONS:
    ds = [d for d in VAR if ed(d) == e]
    R_tout = dict(cibles=regle_cibles(ds), officiants=regle_off(ds), êtres=regle_etres(ds), blessures=regle_bm(ds))
    REGLES_EDITION[e] = R_tout
    av, ap = [], []
    for c in sorted({d["x"]["cle"] for d in ds}):
        reste = [d for d in ds if d["x"]["cle"] != c]
        R = dict(cibles=regle_cibles(reste), officiants=regle_off(reste), êtres=regle_etres(reste), blessures=regle_bm(reste))
        for d in ds:
            if d["x"]["cle"] != c: continue
            av.append(palier(d["cout_c"]) - d["x"]["niveau"]); ap.append(palier(d["cout_c"] + delta(d, R)) - d["x"]["niveau"])
            d["cout_c2"] = d["cout_c"] + delta(d, R); d["cout0_c2"] = d["cout0_c"] + delta(d, R, sans_cibles=True)
    AVANT_APRES[e] = (score(av), score(ap))

# ---------------------------------------------------------------- conversion a (5e) et prix d'Inarama
def pente_niveau(ds):
    dr = droite([(d["cout"], d["x"]["niveau"]) for d in ds]); return dr[0] if dr else None
K = {e: pente_niveau([d for d in VAR if ed(d) == e]) for e in EDITIONS}
def conv(v, e): return None if v is None or not K.get(e) else v * K[REF] / K[e]

# ---------------------------------------------------------------- lot 3 : les couples Forme + Ampleur (toutes les Formes, unifiées)
def y_forme(d, cv=False): return (d["x"]["niveau"] - d["cout0_c2"]) * (K[REF] / K[ed(d)] if cv else 1)
def regler_couples(ds, cv=False):
    """moindres carrés : y = Σ_Formes [ p(Forme) + a × log2(cibles) (formes du guide) ou b(Forme) × log2(taille) (les autres) ]"""
    fus = sorted({f["fu"] for d in ds for f in d["formes"]})
    libres = sorted({f["fu"] for d in ds for f in d["formes"] if f["n"] is None and f["taille"]})
    cols = [("p", fu) for fu in fus] + [("a", None)] + [("b", fu) for fu in libres]
    idx = {c: i for i, c in enumerate(cols)}; n = len(cols)
    A = [[0.0] * n for _ in range(n)]; B = [0.0] * n
    for d in ds:
        v = [0.0] * n
        for f in d["formes"]:
            v[idx[("p", f["fu"])]] += 1
            if f["n"]: v[idx[("a", None)]] += math.log2(f["n"])
            elif f["taille"] and ("b", f["fu"]) in idx: v[idx[("b", f["fu"])]] += math.log2(max(f["taille"], 1))
        y = y_forme(d, cv)
        for i in range(n):
            if not v[i]: continue
            B[i] += v[i] * y
            for j in range(n): A[i][j] += v[i] * v[j]
    for i in range(n): A[i][i] += 1e-6                           # une colonne vide ne bloque pas
    for c in range(n):
        piv = max(range(c, n), key=lambda r: abs(A[r][c]))
        A[c], A[piv] = A[piv], A[c]; B[c], B[piv] = B[piv], B[c]
        for r in range(n):
            if r != c and A[r][c]:
                t = A[r][c] / A[c][c]; A[r] = [a - t * q for a, q in zip(A[r], A[c])]; B[r] -= t * B[c]
    sol = {cols[c]: B[c] / A[c][c] for c in range(n)}
    P = dict(p={fu: max(PLANCHER, sol[("p", fu)]) for fu in fus}, a=max(0.0, sol[("a", None)]), b={fu: max(0.0, sol[("b", fu)]) for fu in libres})
    return P
def prix_couple(f, P):
    p = P["p"].get(f["fu"])
    if p is None: return None
    if f["n"]: return p + P["a"] * math.log2(f["n"])
    if f["taille"] and f["fu"] in P["b"]: return p + P["b"][f["fu"]] * math.log2(max(f["taille"], 1))
    return p
COUPLES, SC3 = {}, {}
for e in EDITIONS:
    ds = [d for d in VAR if ed(d) == e and d["formes"]]
    if not ds: continue
    COUPLES[e] = regler_couples(ds)
    ec = []
    for c in sorted({d["x"]["cle"] for d in ds}):
        P = regler_couples([d for d in ds if d["x"]["cle"] != c])
        for d in ds:
            if d["x"]["cle"] != c: continue
            pz = [prix_couple(f, P) for f in d["formes"]]
            if any(p is None for p in pz): continue
            ec.append(palier(d["cout0_c2"] + sum(pz)) - d["x"]["niveau"]); d["ec3"] = ec[-1]
    SC3[e] = score(ec)
    # le lot 2 pour comparer (première Forme seule, cercles séparés, relation du moteur) : coût en place
    SC3[(e, "lot 2")] = score([palier(d["cout_c2"]) - d["x"]["niveau"] for d in ds])
# décision 1 : une Forme que la 5e ne règle pas (moins de 10 formes) prend la règle des autres éditions ensemble, converties vers la 5e
POOL = regler_couples([d for d in VAR if ed(d) != REF and d["formes"]], cv=True)
N5 = collections.Counter(f["fu"] for d in VAR if ed(d) == REF for f in d["formes"])
def P_inarama(fu): return (COUPLES[REF], "5e") if N5[fu] >= MIN else (POOL, "autres éditions ensemble, converties")

# ---------------------------------------------------------------- l'Ampleur sans Forme : s × log2(taille), par sorte et édition
SF = collections.defaultdict(list)
for d in VAR:
    for a_ in d["ampl_sf"]: SF[(a_["sorte"], ed(d))].append((math.log2(max(a_["taille"], 1)), d["x"]["niveau"] - a_["sans_c"], d, a_))
S_SF = {k: (pente0([(L, y) for L, y, _, _ in v]), len(v)) for k, v in SF.items()}
S_POOL = {}
for so in {k[0] for k in SF}:
    pts = [(L, y * K[REF] / K[e]) for (so2, e), v in SF.items() if so2 == so and e != REF for L, y, _, _ in v]
    S_POOL[so] = (pente0(pts) if pts else None, len(pts))
def s_inarama(so):
    s5, n5 = S_SF.get((so, REF), (None, 0))
    return (s5, "5e", n5) if s5 is not None and n5 >= MIN else (S_POOL[so][0], "autres éditions ensemble, converties", S_POOL[so][1])




# ---------------------------------------------------------------- le rapport (parties 1 à 3 ; les ambiguïtés sont écrites à la main)
cat = json.load(open(CAT, encoding="utf-8"))
s5_lot1 = (cat["pentes"].get("instances|5e|tous|cache") or {}).get("s")
def crochet(v, n): return v if n >= MIN else f"[{v}]"
L_ = ["## 1. Ce que changent les décisions du lot 2", "",
      "**Décision 1 — Inarama calé sur la 5e (2014) seule ; la 2024 convertie (méthode a).** Pente coût → niveau, par édition : "
      + " ; ".join(f"{e} {f2(K[e], 3)}" for e in EDITIONS) + ". Facteur de conversion vers la 5e (K 5e / K édition) : "
      + " ; ".join(f"{e} × {f2(K[REF] / K[e], 2)}" for e in EDITIONS if K.get(e)) + ".", "",
      f"- Lot 1 (Quantité, instances) : Inarama passait par D&D 5 (5e + 2024) : 0,99 × log2(n) ; maintenant la 5e seule (sort caché, 30 formes) : "
      f"{f2(s5_lot1, 3)} × log2(n). Les prix « convertis » des autres éditions sont recalculés avec le facteur ci-dessus.",
      "- Lot 2 (Formes) : remplacé par le lot 3 (les couples Forme + Ampleur, parties 2 et 3).",
      "- Une Forme ou une sorte d'Ampleur que la 5e ne règle pas (moins de 10 formes en 5e) prend la règle des autres éditions ENSEMBLE, "
      "chaque forme convertie vers la 5e avant le réglage ; c'est dit dans la colonne « Inarama ».", "",
      "**Décision 2 — les règles qui ne tiennent pas sont remplacées dans leur édition** (réglées sur l'édition, sans le sort mesuré).",
      "Paliers, sort caché, toutes les formes de l'édition, avant → après :", "",
      "| Édition | Règles remplacées | Valeur réglée (sans cacher) | Formes concernées | Formes | à 1 près | écart absolu moyen | écart moyen |",
      "|---|---|---|---|---|---|---|---|"]
for e in EDITIONS:
    (n, a1, mae, em), (_, b1, mbe, bm) = AVANT_APRES[e]
    R = REGLES_EDITION[e]; rem = [k for k, v in REMPLACE.items() if e in v]; ds = [d for d in VAR if ed(d) == e]
    det, conc = [], []
    if "cibles" in rem:
        det.append(f"cibles : a = {f2(R['cibles'])} (en place 0,22)"); conc.append(f"cibles {sum(1 for d in ds if d['x']['v'][0] > 0 and d['x']['a']['genre'] not in ('blessure', 'soin'))}")
    if "officiants" in rem:
        det.append(f"officiants : k = {f2(R['officiants'])}"); conc.append(f"officiants {sum(1 for d in ds if 'off_c' in d and d['off_c'] - d['cout_c'] > 0)}")
    if "êtres" in rem:
        det.append(f"êtres appelés : α = {f2(R['êtres'][0])}, β = {f2(R['êtres'][1])}, γ = {f2(R['êtres'][2])}" if R["êtres"] else "êtres appelés : pas réglable")
        conc.append(f"êtres {sum(1 for d in ds if 'etre' in d)}")
    if "blessures" in rem:
        det.append(f"blessures multipliées : {f2(R['blessures'])}"); conc.append(f"blessures multipliées {sum(1 for d in ds if d.get('bm'))}")
    pv = any(int(c.split()[-1]) < MIN for c in conc)
    L_.append(f"| {e} | {', '.join(rem) or '—'} | {' ; '.join(det) or '—'} | {', '.join(conc) or '—'}{' (provisoire : moins de 10)' if pv else ''} | {n} | "
              f"{f2(a1, 1)} → {f2(b1, 1)} % | {f2(mae)} → {f2(mbe)} | {f2(em)} → {f2(bm)} |")
NZ = [z for d in VAR for z in d["zone_fi"]]
L_ += ["", f"**Décisions 3 et 4 — toutes les Formes ; une Forme, un prix.** {sum(len(d['formes']) for d in VAR)} cercles de Forme lus sur "
       f"{sum(1 for d in VAR if d['formes'])} formes, dont {sum(1 for d in VAR if len(d['formes']) > 1)} à plusieurs Formes (le lot 2 ne lisait que la première) ; "
       f"les {len({f['id'] for d in VAR for f in d['formes']})} cercles de Forme se ramènent à {len({f['fu'] for d in VAR for f in d['formes']})} Formes "
       "(même valeur, mêmes mots, mêmes satellites de proportion ou d'angle ; la position du satellite et le satellite d'Ampleur ne comptent pas).", "",
       f"**Décision 5 — une Forme en satellite d'un Impact fait de lui une zone.** {sum(1 for d in VAR if d['forme_sur_impact'])} formes portent une Forme "
       f"en satellite d'Impact ; {sum(1 for d in VAR if d['zone_fi'])} seulement ont aussi une Ampleur sur cet Impact (donc une taille) : "
       + "; ".join(sorted({f"{z['forme']} {z['valeur']} {' '.join(z['mots']).lower()} → {z['n']} cible(s)" for z in NZ}))
       + ". Le tableau du guide y donne 1 cible : la relation « cibles » y vaut 0. Les autres n'ont aucune taille écrite : la relation ne se calcule pas "
       "sans inventer une taille (elles gardent leur prix actuel).", ""]

# ---- partie 2 : une ligne par cercle et satellite d'Ampleur
FU = collections.defaultdict(list)
for d in VAR:
    for f in d["formes"]: FU[f["fu"]].append((d, f))
NOMF = {}
for fu, lst in FU.items():
    ids = sorted({f["id"] for _, f in lst if f["id"]}); NOMF[fu] = f"{lst[0][1]['nom']} ({ids[0]}{'…' if len(ids) > 1 else ''})"
L_ += ["## 2. Les cercles et satellites d'Ampleur", "",
       "**Ampleur d'une Forme** : le prix est celui du COUPLE Forme + Ampleur (p de la Forme + sa relation à cette taille, partie 3), par édition ;",
       "« Formes par édition » = formes de la bibliothèque qui portent ce couple ; [ ] = la Forme a moins de 10 formes dans l'édition (provisoire).",
       "Converti = vers la 5e (méthode a). Inarama = la relation de la Forme en 5e si elle y a 10 formes, sinon celle des autres éditions ensemble, converties.", "",
       "| Ampleur | Valeur | Mots | Porteur | Forme liée | Formes par édition | Prix du couple par édition | Converti (5e) | Inarama |", "|---|---|---|---|---|---|---|---|---|"]
AMPL = collections.defaultdict(list)
for d in VAR:
    for f in d["formes"]:
        if f["ampl_ou"] == "cercle": AMPL[("cercle", f["ampl_id"], None, f["fu"])].append((d, f))
        elif f["ampl_ou"] == "satellite": AMPL[("satellite", f["ampl_id"], json.dumps(f["ampl_sat"], ensure_ascii=False), f["fu"])].append((d, f))
NFU = {e: collections.Counter(f["fu"] for d in VAR if ed(d) == e for f in d["formes"]) for e in EDITIONS}
AMPL_JSON = []
for (ou, aid, sv, fu), lst in sorted(AMPL.items(), key=lambda t: (t[0][0] != "cercle", str(t[0][1]), str(t[0][2]))):
    f0 = lst[0][1]
    if ou == "cercle":
        e0 = CR.get(aid, {}); nid, val, mots, porteur = aid, e0.get("valeur"), " · ".join(w.lower() for w in e0.get("mots", [])), "— (cercle)"
    else:
        v_, t_ = json.loads(sv); nid, val, mots, porteur = "satellite", v_, " · ".join(w.lower() for w in t_.split()[1:]), aid
    fp = collections.Counter(ed(d) for d, _ in lst); prs, cvs, par_ed = [], [], {}
    for e in EDITIONS:
        if not fp.get(e): continue
        pr = prix_couple(f0, COUPLES[e]); nf = NFU[e][fu]
        prs.append(f"{e} {crochet(f2(pr), nf)}"); cvs.append(f"{e} {f2(conv(pr, e))}")
        par_ed[e] = dict(formes=fp[e], formes_de_la_forme=nf, prix=pr, converti=conv(pr, e), provisoire=nf < MIN)
    Pi, src_ = P_inarama(fu); inar = max(PLANCHER, prix_couple(f0, Pi))
    L_.append(f"| {nid} | {val} | {mots} | {porteur} | {NOMF[fu]} | " + ", ".join(f"{e} {fp[e]}" for e in EDITIONS if fp.get(e))
              + f" | {' ; '.join(prs)} | {' ; '.join(cvs)} | {f2(inar)}{'' if src_ == '5e' else ' *'} |")
    AMPL_JSON.append(dict(id=aid if ou == "cercle" else None, porteur=aid if ou == "satellite" else None, type="AMPLEUR", valeur=val, mots=mots,
                          forme_liee=NOMF[fu], taille_base=f0["taille"], cibles_guide=f0["n"], par_edition=par_ed, prix_inarama=inar, source_inarama=src_,
                          regle="prix du couple Forme + Ampleur (lot 3)"))
nc = len({a["id"] for a in AMPL_JSON if a["id"]})
L_ += ["", f"\\* = la Forme a moins de 10 formes en 5e : relation des autres éditions ensemble, converties. {nc} cercles d'Ampleur sur 135 sont liés à une Forme "
       f"(un même cercle peut suivre plusieurs Formes : une ligne par couple) ; "
       f"{sum(1 for a in AMPL_JSON if a['porteur'])} couples ont leur Ampleur en satellite de la Forme.", ""]
manq = sorted(set(e["id"] for e in rep if e["type"] == "AMPLEUR") - {a["id"] for a in AMPL_JSON if a["id"]})
if manq: L_ += [f"Cercles d'Ampleur sans Forme liée ni prix : {', '.join(manq)}.", ""]

# Ampleur sans Forme
SFG = collections.defaultdict(list)
for d in VAR:
    for a_ in d["ampl_sf"]: SFG[(a_["sorte"], a_.get("porteur") or a_.get("id"), a_.get("valeur", a_["taille"]))].append((ed(d), a_))
L_ += ["**Ampleur sans Forme** : prix = s × log2(taille en unités de base : m, m², m³, litres, kilos), s réglé par sorte et par édition (sort caché",
       "pour les paliers, sans le satellite pour le reste du coût) ; plancher 0,01. Les sortes :", "",
       "| Sorte | Édition : s (formes) | Converti (5e) | Inarama : s (source) |", "|---|---|---|---|"]
for so in sorted({k[0] for k in SF}):
    si, src_, n_ = s_inarama(so)
    L_.append(f"| {so} | " + " ; ".join(f"{e} {crochet(f2(S_SF[(so, e)][0], 3), S_SF[(so, e)][1])} ({S_SF[(so, e)][1]})" for e in EDITIONS if (so, e) in S_SF)
              + " | " + " ; ".join(f"{e} {f2(conv(S_SF[(so, e)][0], e), 3)}" for e in EDITIONS if (so, e) in S_SF)
              + f" | {f2(si, 3)} ({src_}, {n_} formes{', provisoire' if n_ < MIN else ''}) |")
L_ += ["", "Une ligne par satellite d'Ampleur sans Forme :", "",
       "| Ampleur | Valeur | Mots | Porteur | Forme liée | Formes par édition | Prix par édition | Converti (5e) | Inarama |", "|---|---|---|---|---|---|---|---|---|"]
SF_JSON = []
for (so, pid, val), lst in sorted(SFG.items(), key=lambda t: (t[0][0], str(t[0][1]), str(t[0][2]))):
    a0 = lst[0][1]; t = a0["taille"]; L2 = math.log2(max(t, 1)); fp = collections.Counter(e for e, _ in lst); prs, cvs, par_ed = [], [], {}
    for e in EDITIONS:
        if not fp.get(e): continue
        s_, n = S_SF[(so, e)]; pr = max(PLANCHER, s_ * L2) if s_ is not None else None
        prs.append(f"{e} {crochet(f2(pr), n)}"); cvs.append(f"{e} {f2(max(PLANCHER, conv(s_, e) * L2) if s_ is not None else None)}")
        par_ed[e] = dict(formes=fp[e], s=s_, prix=pr, provisoire=n < MIN)
    si, src_, _ = s_inarama(so); inar = max(PLANCHER, (si or 0) * L2)
    mots = " · ".join(w.lower() for w in a0["mots"]) if a0.get("mots") else so
    L_.append(f"| {'satellite' if a0.get('porteur') else a0['id']} | {a0.get('valeur', '—')} | {mots} | {a0.get('porteur') or '—'} | — | "
              + ", ".join(f"{e} {fp[e]}" for e in EDITIONS if fp.get(e)) + f" | {' ; '.join(prs)} | {' ; '.join(cvs)} | {f2(inar)} |")
    SF_JSON.append(dict(id=a0["id"], porteur=a0.get("porteur"), type="AMPLEUR", sorte=so, valeur=a0.get("valeur"), mots=list(a0.get("mots") or []),
                        taille_base=t, par_edition=par_ed, prix_inarama=inar, source_inarama=src_, regle="Ampleur sans Forme : s × log2(taille)"))
for z in NZ: pass
ZJ = {}
for d in VAR:
    for z in d["zone_fi"]: ZJ.setdefault((z["porteur"], z["valeur"], z["mots"]), (z, collections.Counter()))[1][ed(d)] += 1
for (pid, val, mots), (z, fp) in ZJ.items():
    L_.append(f"| satellite | {val} | {' · '.join(w.lower() for w in mots)} | {pid} | {z['forme']} en satellite (décision 5) | "
              + ", ".join(f"{e} {fp[e]}" for e in EDITIONS if fp.get(e)) + f" | relation « cibles » : {z['n']} cible → 0 | — | {f2(PLANCHER)} |")
    SF_JSON.append(dict(id=None, porteur=pid, type="AMPLEUR", sorte="Ampleur d'une Forme en satellite d'Impact (décision 5)", valeur=val, mots=list(mots),
                        cibles_guide=z["n"], prix_inarama=PLANCHER, regle="zone : relation « cibles » (1 cible : 0) ; plancher"))
L_ += ["", f"{len(SF_JSON)} satellites d'Ampleur sans Forme (porteur, valeur) ; {sum(len(v) for v in SF.values())} formes.", ""]

# ---- partie 3 : chaque Forme, sa relation à la taille
L_ += ["## 3. Chaque Forme : sa relation à la taille, par édition", "",
       "Le couple : p (prix propre de la Forme, au moins 0,01) + a × log2(cibles du tableau du guide) pour les formes que le guide connaît (sphère, cube,",
       "cylindre, cône, ligne ; a commun aux Formes d'une édition) ; p + b × log2(taille) (pente libre propre à la Forme) pour les autres. Réglé par",
       "moindres carrés sur TOUTES les Formes de chaque forme, sur le coût sans relation « cibles » ni figure (règles de la décision 2 appliquées).",
       "[ ] = moins de 10 formes dans l'édition (provisoire). « Sans taille » : formes où cette Forme n'a pas de taille lisible (p seul) — comptées.", "",
       "Paliers en sort caché (le couple réglé sans le sort mesuré), comparés au coût en place (moteur v8 + décision 2) :", "",
       "| Édition | Formes | a (guide) | Couples : à 1 près / écart absolu / écart moyen | En place : à 1 près / écart absolu / écart moyen |", "|---|---|---|---|---|"]
for e in EDITIONS:
    if e not in SC3: continue
    n, a1, mae, em = SC3[e]; _, b1, mbe, bm = SC3[(e, "lot 2")]
    L_.append(f"| {e} | {n} | {f2(COUPLES[e]['a'], 3)} | {f2(a1, 1)} % / {f2(mae)} / {f2(em)} | {f2(b1, 1)} % / {f2(mbe)} / {f2(bm)} |")
GRP = (("avec figure à part (prix retiré, repris par le couple)", lambda d: d["x"]["fig"] is not None),
       ("une Forme sans taille lisible", lambda d: any(not f["taille"] for f in d["formes"])),
       ("plusieurs Formes", lambda d: len(d["formes"]) > 1),
       ("le reste", lambda d: d["x"]["fig"] is None and all(f["taille"] for f in d["formes"]) and len(d["formes"]) == 1))
L_ += ["", "Où le couple perd ou gagne (sort caché, à 1 près couples → en place, formes) :", "", "| Édition | " + " | ".join(g for g, _ in GRP) + " |", "|---|" + "---|" * len(GRP)]
for e in EDITIONS:
    cel = []
    for g, fn in GRP:
        ds_ = [d for d in VAR if ed(d) == e and d["formes"] and "ec3" in d and fn(d)]
        if not ds_: cel.append("—"); continue
        cel.append(f"{100 * sum(abs(d['ec3']) <= 1 for d in ds_) / len(ds_):.0f} → {100 * sum(abs(palier(d['cout_c2']) - d['x']['niveau']) <= 1 for d in ds_) / len(ds_):.0f} % ({len(ds_)})")
    L_.append(f"| {e} | " + " | ".join(cel) + " |")
L_ += ["", "| Édition | Formes | a (guide) | | |", "|---|---|---|---|---|"]
L_ += [f"| autres éditions ensemble, converties (règle d'Inarama quand la 5e a moins de 10 formes) | {sum(1 for d in VAR if ed(d) != REF and d['formes'])} | {f2(POOL['a'], 3)} | — | — |",
       "", "| Forme | Cercles | Formes par édition | Sans taille | Relation par édition | Inarama |", "|---|---|---|---|---|---|"]
FORMES_JSON = []
for fu, lst in sorted(FU.items(), key=lambda t: -len(t[1])):
    ids = sorted({f["id"] for _, f in lst if f["id"]}); fp = collections.Counter(ed(d) for d, _ in lst)
    guide = any(f["n"] for _, f in lst); rel, par_ed = [], {}
    for e in EDITIONS:
        if not fp.get(e): continue
        P = COUPLES[e]; p = P["p"].get(fu)
        r_ = (f"p {f2(p)} + {f2(P['a'])} × log2(cibles)" if guide else f"p {f2(p)} + {f2(P['b'][fu])} × log2(taille)" if fu in P["b"] else f"p {f2(p)} seul")
        rel.append(f"{e} {crochet(r_, fp[e])}")
        par_ed[e] = dict(formes=fp[e], p=p, a=P["a"] if guide else None, b=P["b"].get(fu), provisoire=fp[e] < MIN,
                         p_converti=conv(p, e), a_converti=conv(P["a"], e) if guide else None, b_converti=conv(P["b"].get(fu), e))
    Pi, src_ = P_inarama(fu); pi = Pi["p"].get(fu, PLANCHER)
    ri = (f"p {f2(pi)} + {f2(Pi['a'])} × log2(cibles)" if guide else f"p {f2(pi)} + {f2(Pi['b'][fu])} × log2(taille)" if fu in Pi["b"] else f"p {f2(pi)} seul")
    st = sum(1 for _, f in lst if not f["taille"])
    L_.append(f"| {lst[0][1]['nom']} | {', '.join(ids)} | " + ", ".join(f"{e} {fp[e]}" for e in EDITIONS if fp.get(e)) + f" | {st} | {' ; '.join(rel)} | {ri} ({src_}) |")
    FORMES_JSON.append(dict(forme=lst[0][1]["nom"], unifiee=list(fu), cercles=ids, par_edition=par_ed, sans_taille=st,
                            inarama=dict(p=pi, a=Pi["a"] if guide else None, b=Pi["b"].get(fu), source=src_)))
L_ += ["", "Points du réglage : les Formes « plan » et « disque » n'ont pas de tableau du guide (pente libre) ; « hélice », « paroi », la calotte d'angle",
       "C00692 n'ont jamais de taille lisible (p seul).", ""]
open(os.path.join(OUT, "catalogue_lot3_corps.md"), "w", encoding="utf-8").write("\n".join(L_) + "\n")

# ---------------------------------------------------------------- le catalogue
for e_ in cat["cercles"]:                         # décision 1 : lot 1 recalé sur la 5e (s de la 5e en sort caché)
    if e_["type"] == "QUANTITE" and e_.get("sorte") == "instances" and s5_lot1 is not None:
        e_["prix_inarama"] = max(PLANCHER, s5_lot1 * math.log2(e_["n"]))
        e_["regle"] = f"Inarama : {s5_lot1:.3f} × log2(n) (5e seule, décision du lot 2), plancher 0,01 ; sur une blessure : plancher"
        for ed_, pe in e_.get("par_edition", {}).items():
            s_ = pe.get("s") if isinstance(pe, dict) else None
            if s_ is not None and K.get(ed_): pe["converti"] = pe["converti_a"] = max(PLANCHER, conv(s_, ed_) * math.log2(e_["n"]))
cat["cercles"] = [c for c in cat["cercles"] if c["type"] not in ("FORME", "AMPLEUR")]
cat.pop("formes_modeles", None)
cat["formes_unifiees"] = FORMES_JSON
cat["cercles"] += AMPL_JSON + SF_JSON
cat["ampleur_sans_forme_pentes"] = {so: dict(par_edition={e: dict(s=S_SF[(so, e)][0], formes=S_SF[(so, e)][1]) for e in EDITIONS if (so, e) in S_SF},
                                             inarama=dict(zip(("s", "source", "formes"), s_inarama(so)))) for so in sorted({k[0] for k in SF})}
cat["couples_a"] = {e: COUPLES[e]["a"] for e in COUPLES} | {"autres éditions converties": POOL["a"]}
cat["decisions_lot2"] = dict(inarama="5e (2014) seule ; 2024 convertie (méthode a) ; moins de 10 formes en 5e : autres éditions ensemble, converties",
                             regles_remplacees=REMPLACE, toutes_les_formes=True, forme_unifiee=True,
                             forme_sur_impact="zone (relation « cibles ») quand sa taille est lisible")
cat["pente_cout_niveau"] = K
cat["regles_par_edition"] = {e: dict(cibles=v["cibles"], officiants=v["officiants"], etres=v["êtres"], blessures_multipliees=v["blessures"]) for e, v in REGLES_EDITION.items()}
cat["_lisez_moi"] = ("Catalogue des prix des cercles (lots 1 Quantité, 2 et 3 Forme et Ampleur). Un cercle par entrée (repertoire_cercles_v6.json). "
                     "Les Formes sont dans « formes_unifiees » (une Forme = un prix, quelle que soit la position de ses satellites : p + a × log2(cibles "
                     "du guide) ou p + b × log2(taille)). Une Ampleur liée à une Forme a le prix du couple Forme + Ampleur ; une Ampleur sans Forme : "
                     "s × log2(taille). Prix par édition, convertis vers la 5e (méthode a) ; Inarama calé sur la 5e (2014) ; moins de 10 formes en 5e : "
                     "les autres éditions ensemble, converties. « provisoire » = moins de 10 formes. Plancher 0,01 ; le Noyau vaut 0.")
json.dump(cat, open(os.path.join(OUT, "catalogue_prix.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=list)
print("ok", len(VAR), len(AMPL_JSON), len(SF_JSON), len(FORMES_JSON), "manquants", manq)
