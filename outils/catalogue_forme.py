"""Catalogue des prix des cercles, lot 2 : la Forme ; et la vérification des règles existantes (26 novembre 2026). Un calcul.

    python outils/catalogue_forme.py <dossier de sortie> <dossier des documents du barème> <repertoire_cercles_v6.json> <catalogue_prix.json du lot 1>

- Lot 1 (Quantité), décisions de l'utilisateur inscrites au catalogue : « instances » = 0,99 × log2(n) en Inarama (plancher 0,01) ; sur une
  blessure, plancher (le montant total paie la Quantité) ; autres éditions converties par la méthode a (rapport des pentes coût → niveau) ;
  « mesure » au plancher.
- Vérification, par édition et en sort caché, de quatre règles en place : la relation « cibles », le rabais des officiants, la puissance
  des êtres appelés (puissance, fractionnée ou non, + log2(nombre)), le montant multiplié des blessures.
- Lot 2 : les 30 cercles de Forme ; prix = p (prix propre, au moins 0,01) + une relation à la taille, réglés par édition : A) le tableau
  du guide du maître (cibles = sphère et cylindre rayon ÷ 5, cube côté ÷ 5, cône longueur ÷ 10, ligne longueur ÷ 30, en pieds ; a × log2),
  B) une pente libre sur log2 de la taille écrite, par Forme ; la meilleure en sort caché. Les satellites de Forme sont relevés.
"""
import os, sys, json, math, collections, statistics, re
ICI = os.path.dirname(os.path.abspath(__file__))
OUT, DOCS, REP, CAT1 = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
RAPIDE = os.environ.get("RAPIDE")
V8 = os.path.join(ICI, "mesure_bareme_cercles_v8.py")
src = open(V8, encoding="utf-8").read()
src = src[:src.index("M0 = modele(None)")]
src = src.replace('''        F.append(x)\n''', '''        x["_f"] = dict(rings=f["rings"], verb=f.get("verb"))\n        F.append(x)\n''', 1)
ns = {"__file__": V8, "__name__": "v8"}
sys.argv = [V8, OUT, DOCS]
exec(compile(src, V8, "exec"), ns)
F, BC, modele, calcul, SYSTEMES = ns["F"], ns["BC"], ns["modele"], ns["calcul"], ns["SYSTEMES"]
EDITIONS = ["5e", "2024", "3.5", "PF1", "PF2", "PF2 remaniée"]
MIN, PLANCHER = 10, 0.01

rep = json.load(open(REP, encoding="utf-8"))["cercles"]
IDS = {}
for e in rep:
    IDS[(e["type"], json.dumps(e["valeur"], ensure_ascii=False), tuple(e["mots"]), tuple(json.dumps(s, ensure_ascii=False) for s in e["satellites"]))] = e["id"]
def ident(u): return IDS.get(u) or IDS.get((u[0], u[1], u[2], tuple(json.dumps(json.loads(s), ensure_ascii=False) for s in u[3])))
CF = {e["id"]: e for e in rep if e["type"] == "FORME"}
def _txt(s): return s[2] if len(s) > 2 and isinstance(s[2], str) else ""
def num(v): return isinstance(v, (int, float)) and not isinstance(v, bool)
def f2(v, d=2): return "—" if v is None else f"{v:.{d}f}"


def refait(x, rings):
    a = BC.analyse(dict(rings=rings, verb=x["_f"]["verb"]))
    m = a["mesures"]
    g = ("état : " + (a["famille"] or "?")) if a["genre"] == "état" else a["genre"]
    fg = m.get("figure")
    return dict(x, a=a, groupe=g, v=(math.log2(max(m["cibles"], 1)), m["marche"], -(1.0 if m["restriction"] else 0.0), -(1.0 if m.get("sursaut") else 0.0)),
                fig=(fg[0], fg[1]) if fg and fg[1] is not None else None, fig_nom=fg[0] if fg else None)


def couts(x, M):
    """coût ; coût sans la relation « cibles » ni la part de figure (la Forme sans prix) ; la règle a utilisée"""
    c, _, _, _, r = calcul(x, M, "propre")
    c0 = calcul(dict(x, v=(0.0,) + tuple(x["v"][1:]), fig=None), M, "propre")[0]
    return c, c0, r.get("a", 0.0)


def taille(rings):
    f_ = next((r for r in rings if r[0] == "FORME"), None)
    a_ = next((r for r in rings if r[0] == "AMPLEUR"), None)
    if a_ is not None and num(a_[1]) and tuple(a_[2]) in BC.UNITE_BASE: return a_[1] * BC.UNITE_BASE[tuple(a_[2])]
    if f_ is not None:
        for s_ in (f_[4] if len(f_) > 4 and f_[4] else []):
            t = _txt(s_).split()
            if t[:1] == ["AMPLEUR"] and num(s_[1]) and tuple(t[1:]) in BC.UNITE_BASE: return s_[1] * BC.UNITE_BASE[tuple(t[1:])]
    return None


# ---------------------------------------------------------------- les formes et leurs variantes
VAR = {}                        # (cle, jeu, forme) -> variantes calculées
for x in F:
    if x["a"]["sans_impact"]: continue
    rings = x["_f"]["rings"]
    d = dict(x=x)
    fr = next((r for r in rings if r[0] == "FORME"), None)
    if fr is not None:
        d["forme_id"] = ident(BC.cle_cercle(fr)); d["taille"] = taille(rings)
        n_, why = BC.cibles_zone(rings); d["n_guide"] = n_
    # officiants (Condition) : la forme sans ses satellites d'officiants
    off = [(i, j) for i, r in enumerate(rings) if r[0] == "CONDITION" for j, s_ in enumerate(r[4] if len(r) > 4 and r[4] else [])
           if (_txt(s_).startswith("OFFICIANT") or not _txt(s_)) and num(s_[1])]
    if off:
        rr = list(rings)
        for i in {i for i, _ in off}:
            r = rr[i]; rr[i] = (*r[:4], [s_ for j, s_ in enumerate(r[4]) if (i, j) not in off], *r[5:])
        d["sans_off"] = refait(x, rr); d["n_off"] = sum(rings[i][4][j][1] for i, j in off)
    # êtres appelés : puissance (fractionnée ou non) et nombre, sur les formes à un seul effet
    if x["a"]["genre"] == "être appelé" and len(x["a"]["effets"]) == 1:
        rg = next((dd["regle"] for dd in x["a"]["detail"] if dd["cercle"] == "IMPACT"), "")
        m_ = re.search(r"(?:puissance|animation) ([\d.]+).*?log2\((\d+)\)", rg)
        if m_: d["etre"] = (float(m_.group(1)), math.log2(max(int(m_.group(2)), 1)), "fractionné" in rg)
    # blessures : un seul effet ; multiplié par la Quantité ?
    if x["a"]["genre"] == "blessure" and len(x["a"]["effets"]) == 1:
        d["blessure_multipliee"] = x["a"]["mesures"]["instances"] > 1 and not x["a"]["mesures"]["zone"]
    VAR[(x["cle"], x["jeu"], x["forme"])] = d
print("formes", len(VAR))

M0 = modele(None)
cles = sorted({d["x"]["cle"] for d in VAR.values()})
par_cle = collections.defaultdict(list)
for d in VAR.values(): par_cle[d["x"]["cle"]].append(d)
for i, c in enumerate(cles):
    M = modele(c) if not (RAPIDE and i > 40) else M0
    for d in par_cle[c]:
        x = d["x"]
        d["cout"], d["cout0"], d["a_regle"] = couts(x, M0)
        d["cout_c"], d["cout0_c"], d["a_regle_c"] = couts(x, M)
        if "sans_off" in d:
            d["off"] = (calcul(d["sans_off"], M0, "propre")[0], calcul(d["sans_off"], M, "propre")[0])
    if i % 500 == 0: print("sort caché", i, "/", len(cles), flush=True)


# ---------------------------------------------------------------- outils de régression
def droite(pts):
    """(pente, ordonnée, erreur type de la pente, n) de y = b x + c"""
    n = len(pts)
    if n < 3: return None
    mx = statistics.mean(p[0] for p in pts); my = statistics.mean(p[1] for p in pts)
    sxx = sum((p[0] - mx) ** 2 for p in pts)
    if not sxx: return None
    b = sum((p[0] - mx) * (p[1] - my) for p in pts) / sxx; c = my - b * mx
    res = sum((p[1] - (b * p[0] + c)) ** 2 for p in pts) / (n - 2)
    return b, c, (res / sxx) ** 0.5, n


def moyenne_err(v):
    if len(v) < 2: return (statistics.mean(v) if v else None), None, len(v)
    return statistics.mean(v), statistics.stdev(v) / len(v) ** 0.5, len(v)


def verdict(ecart, err):
    if ecart is None or err is None: return "trop peu de formes"
    return "tient" if abs(ecart) <= 2 * err else "ne tient pas"


def ed_de(d): return d["x"]["jeu"]


REGLES = []      # lignes du point 2
# 2.1 la relation « cibles » : la pente de (niveau − coût sans la relation) sur log2(cibles), contre la règle en place
for ed in EDITIONS:
    ds = [d for d in VAR.values() if ed_de(d) == ed and d["x"]["a"]["genre"] not in ("blessure", "soin")]
    pts = [(d["x"]["v"][0], d["x"]["niveau"] - (d["cout_c"] - d["a_regle_c"] * d["x"]["v"][0])) for d in ds]
    dr = droite(pts)
    en_place = [d["a_regle_c"] for d in ds if d["x"]["v"][0] > 0]
    ap = statistics.mean(en_place) if en_place else None
    REGLES.append(("relation « cibles » (pente sur log2 des cibles)", ed, f"{f2(ap)} (moyenne des règles par genre)",
                   f"{f2(dr[0])} ± {f2(dr[2])}" if dr else "—", len(pts), sum(1 for p in pts if p[0] > 0),
                   verdict(dr[0] - ap if dr and ap is not None else None, dr[2] if dr else None)))
# 2.2 le rabais des officiants : k tel que niveau ≈ coût sans officiants − k × rabais ; la règle dit k = 1
for ed in EDITIONS:
    ds = [d for d in VAR.values() if ed_de(d) == ed and "off" in d]
    pts = [(d["off"][1] - d["cout_c"], d["x"]["niveau"] - d["off"][1]) for d in ds if d["off"][1] - d["cout_c"] > 0]
    if not pts: continue
    k = -sum(r * y for r, y in pts) / sum(r * r for r, _ in pts) if sum(r * r for r, _ in pts) else None
    res = [y + k * r for r, y in pts] if k is not None else []
    err = (statistics.stdev(res) / (sum(r * r for r, _ in pts)) ** 0.5) if len(res) > 2 else None
    REGLES.append(("rabais des officiants (k : la part du rabais 0,25…0,60 qui tient ; règle k = 1)", ed, "1,00",
                   f"{f2(k)} ± {f2(err)}", len(pts), len(pts), verdict(k - 1 if k is not None else None, err)))
# 2.3 la puissance des êtres appelés : niveau − (coût − effet) = α × puissance + β × log2(nombre) + γ ; la règle dit α = β = 1
def deux_variables(pts):
    """y = α p + β l + γ (moindres carrés) ; erreurs types"""
    n = len(pts)
    if n < 5: return None
    import itertools
    X = [[p, l, 1.0] for p, l, _ in pts]; Y = [y for _, _, y in pts]
    A = [[sum(X[k][i] * X[k][j] for k in range(n)) for j in range(3)] for i in range(3)]
    b = [sum(X[k][i] * Y[k] for k in range(n)) for i in range(3)]
    # inverse 3 × 3
    def det(m): return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
    D = det(A)
    if abs(D) < 1e-9: return None
    inv = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            mi = [[A[r][c] for c in range(3) if c != j] for r in range(3) if r != i]
            inv[j][i] = ((-1) ** (i + j)) * (mi[0][0] * mi[1][1] - mi[0][1] * mi[1][0]) / D
    sol = [sum(inv[i][j] * b[j] for j in range(3)) for i in range(3)]
    res = sum((Y[k] - sum(sol[i] * X[k][i] for i in range(3))) ** 2 for k in range(n)) / (n - 3)
    return sol, [(res * inv[i][i]) ** 0.5 if inv[i][i] > 0 else None for i in range(3)], n
for ed in EDITIONS:
    ds = [d for d in VAR.values() if ed_de(d) == ed and "etre" in d]
    pts = [(d["etre"][0], d["etre"][1], d["x"]["niveau"] - (d["cout_c"] - (d["etre"][0] + d["etre"][1]))) for d in ds]
    r_ = deux_variables(pts)
    frac = [d["x"]["niveau"] - d["cout_c"] for d in ds if d["etre"][2]]; autres = [d["x"]["niveau"] - d["cout_c"] for d in ds if not d["etre"][2]]
    mf, ef, nf = moyenne_err(frac); ma, ea, na = moyenne_err(autres)
    if r_:
        (al, be, ga), (eal, ebe, ega), n = r_
        dege = not eal or not ebe or eal < 1e-6 or ebe < 1e-6          # points confondus : la régression ne dit rien
        v_ = "trop peu de formes (points confondus)" if dege else "tient" if (abs(al - 1) <= 2 * eal and abs(be - 1) <= 2 * ebe) else "ne tient pas"
        REGLES.append(("êtres appelés : puissance + log2(nombre) (α puissance, β log2 ; règle α = β = 1)", ed, "α 1,00 ; β 1,00",
                       f"α {f2(al)} ± {f2(eal)} ; β {f2(be)} ± {f2(ebe)}", n, nf, v_ + (f" ; fractionnés : reste moyen {f2(mf)} contre {f2(ma)} pour les autres" if nf else "")))
    elif ds:
        REGLES.append(("êtres appelés : puissance + log2(nombre)", ed, "α 1,00 ; β 1,00", "—", len(ds), nf, "trop peu de formes"))
# 2.4 le montant multiplié des blessures : le reste (niveau − coût) des blessures multipliées contre celui des autres blessures
for ed in EDITIONS:
    ds = [d for d in VAR.values() if ed_de(d) == ed and "blessure_multipliee" in d]
    mu = [d["x"]["niveau"] - d["cout_c"] for d in ds if d["blessure_multipliee"]]; so = [d["x"]["niveau"] - d["cout_c"] for d in ds if not d["blessure_multipliee"]]
    if not mu: continue
    m1, e1, n1 = moyenne_err(mu); m0, e0, n0 = moyenne_err(so)
    err = ((e1 or 0) ** 2 + (e0 or 0) ** 2) ** 0.5 if e1 is not None and e0 is not None else None
    REGLES.append(("blessures : le tableau du guide sur le montant total (reste des multipliées − reste des autres ; règle 0)", ed, "0,00",
                   f"{f2(m1 - m0 if m0 is not None else None)} ± {f2(err)} (multipliées {f2(m1)}, autres {f2(m0)})", n1 + n0, n1,
                   verdict(m1 - m0 if m0 is not None else None, err)))

# ---------------------------------------------------------------- lot 2 : les Formes
FD = [d for d in VAR.values() if d.get("forme_id") in CF]
GUIDE = {"C00666", "C00667", "C00674", "C00675", "C00676", "C00677", "C00678", "C00681", "C00682", "C00683", "C00684", "C00685",
         "C00686", "C00687", "C00688", "C00689", "C00690", "C00693", "C00694"}          # ligne, cône, cube, cylindre, sphère
def ycache(d, cache=True): return d["x"]["niveau"] - (d["cout0_c"] if cache else d["cout0"])
def regle_forme(ds, modele_):
    """paramètres réglés sur ds : A (a commun, p par Forme), B (b et p par Forme), 0 (p seul)"""
    par = collections.defaultdict(list)
    for d in ds: par[d["forme_id"]].append(d)
    out = dict(p={}, b={}, a=0.0)
    if modele_ == "A":
        num_, den_ = 0.0, 0.0
        for fid, l in par.items():
            l = [d for d in l if d["n_guide"]]
            if len(l) < 2: continue
            mx = statistics.mean(math.log2(d["n_guide"]) for d in l); my = statistics.mean(ycache(d) for d in l)
            num_ += sum((math.log2(d["n_guide"]) - mx) * (ycache(d) - my) for d in l); den_ += sum((math.log2(d["n_guide"]) - mx) ** 2 for d in l)
        out["a"] = max(0.0, num_ / den_) if den_ else 0.0
    for fid, l in par.items():
        if modele_ == "A" and fid in GUIDE:
            out["p"][fid] = max(PLANCHER, statistics.mean(ycache(d) - out["a"] * math.log2(max(d["n_guide"] or 1, 1)) for d in l))
        elif modele_ in ("A", "B") and len([d for d in l if d["taille"]]) >= 3:
            pts = [(math.log2(max(d["taille"], 1)), ycache(d)) for d in l if d["taille"]]
            dr = droite(pts); b_ = max(0.0, dr[0]) if dr else 0.0
            out["b"][fid] = b_
            out["p"][fid] = max(PLANCHER, statistics.mean(ycache(d) - b_ * (math.log2(max(d["taille"], 1)) if d["taille"] else 0) for d in l))
        else:
            out["p"][fid] = max(PLANCHER, statistics.mean(ycache(d) for d in l))
    return out
def prix_forme(d, P):
    fid = d["forme_id"]; p = P["p"].get(fid)
    if p is None: return None
    if fid in GUIDE and "a" in P and P.get("modele") == "A": return p + P["a"] * math.log2(max(d["n_guide"] or 1, 1))
    return p + P["b"].get(fid, 0.0) * (math.log2(max(d["taille"], 1)) if d["taille"] else 0.0)
RES = {}
for ed in EDITIONS:
    ds = [d for d in FD if ed_de(d) == ed]
    if not ds: continue
    for mo in ("A", "B", "0"):
        P = regle_forme(ds, mo); P["modele"] = mo
        ecarts = []
        for c in sorted({d["x"]["cle"] for d in ds}):               # sort caché : réglé sans le sort, appliqué à ses formes
            Pc = regle_forme([d for d in ds if d["x"]["cle"] != c], mo); Pc["modele"] = mo
            for d in ds:
                if d["x"]["cle"] != c: continue
                pf = prix_forme(d, Pc)
                if pf is None: continue
                ecarts.append(int(min(10, max(0, math.floor(d["cout0_c"] + pf + 0.5)))) - d["x"]["niveau"])
        n = len(ecarts)
        RES[(ed, mo)] = dict(P=P, n=n, a1=100 * sum(1 for e in ecarts if abs(e) <= 1) / n if n else None,
                             mae=statistics.mean(abs(e) for e in ecarts) if n else None, ecart=statistics.mean(ecarts) if n else None)
MEILLEUR = {ed: min(("A", "B"), key=lambda mo: RES[(ed, mo)]["mae"] if RES.get((ed, mo)) and RES[(ed, mo)]["mae"] is not None else 99) for ed in EDITIONS if (ed, "A") in RES}

# conversion a (lot 1) : pente coût → niveau par édition
def pente_niveau(ds):
    pts = [(d["cout"], d["x"]["niveau"]) for d in ds]; dr = droite(pts); return dr[0] if dr else None
K = {ed: pente_niveau([d for d in VAR.values() if ed_de(d) == ed]) for ed in EDITIONS}
K["D&D 5"] = pente_niveau([d for d in VAR.values() if d["x"]["systeme"] == "D&D 5"])
def conv(v, ed): return None if v is None or not K.get(ed) else v * K["D&D 5"] / K[ed]

# ---------------------------------------------------------------- lot 1 : les décisions dans le catalogue
cat = json.load(open(CAT1, encoding="utf-8"))
S1 = {k: v for k, v in cat["pentes"].items()}
for e in cat["cercles"]:
    n = e["n"]
    if e["sorte"] == "instances":
        e["prix_inarama"] = max(PLANCHER, 0.99 * math.log2(n))
        e["regle"] = "Inarama : 0,99 × log2(n), plancher 0,01 (décision du lot 1) ; sur une blessure : plancher (le montant total paie la Quantité)"
        for ed, pe in e["par_edition"].items():
            s_ = (S1.get(f"instances|{ed}|tous|cache") or {}).get("s")
            pe["prix"] = max(PLANCHER, s_ * math.log2(n)) if s_ is not None else None
            pe["prix_sur_une_blessure"] = PLANCHER
            pe["converti"] = max(PLANCHER, conv(s_, ed) * math.log2(n)) if s_ is not None and conv(s_, ed) is not None else None
            pe.pop("converti_b", None); pe["converti_a"] = pe["converti"]
    else:
        e["prix_inarama"] = PLANCHER; e["regle"] = "« mesure » : au plancher pour l'instant (décision du lot 1)"
        for pe in e["par_edition"].values(): pe["prix"] = PLANCHER; pe["converti"] = PLANCHER
cat["_lisez_moi"] = ("Catalogue des prix des cercles (lots 1 : Quantité, et 2 : Forme). Un cercle par entrée, identifié comme au répertoire "
                     "(repertoire_cercles_v6.json) ; prix par édition (5e, 2024, 3.5, PF1, PF2, PF2 remaniée), converti vers D&D 5 par la méthode a "
                     "(rapport des pentes coût → niveau, décision du lot 1) ; prix d'Inarama. Plancher 0,01 ; le Noyau vaut 0. Les satellites ne "
                     "sont pas des entrées : leurs règles de relation sont à décider (catalogue_lot1_quantite.md, catalogue_lot2_forme.md).")
cat["decisions_lot1"] = dict(instances="0,99 × log2(n) en Inarama ; plancher sur une blessure ; conversion a", mesure="plancher")

# ---------------------------------------------------------------- lot 2 : le catalogue et le rapport
def formes_par(fid): return collections.Counter(ed_de(d) for d in FD if d["forme_id"] == fid)
L_ = ["# Catalogue des prix des cercles — lot 2 : la Forme ; vérification des règles existantes", "",
      "*Branche `catalogue`, 26 novembre 2026. Un calcul : rien n'est écrit dans la bibliothèque.*", "",
      "## 1. Les règles qui existent déjà, vérifiées par édition (sort caché)", "",
      "« Tient » : l'écart entre la règle réglée sur l'édition et la règle en place reste dans deux erreurs types.", "",
      "| Règle | Édition | En place | Réglée sur l'édition | Formes | Formes concernées | Verdict |", "|---|---|---|---|---|---|---|"]
for r in REGLES: L_.append("| " + " | ".join(str(x_) for x_ in r) + " |")
L_ += ["", "## 2. Les Formes : le modèle retenu par édition (sort caché)", "",
       "A = le tableau du guide (a × log2(cibles), a commun à l'édition, p par Forme ; les Formes hors du tableau prennent leur pente libre) ;",
       "B = une pente libre b × log2(taille écrite) par Forme ; 0 = p seul. Écart absolu moyen et « à 1 près » des paliers en sort caché.", "",
       "| Édition | Formes | A : écart abs / à 1 | B : écart abs / à 1 | p seul : écart abs / à 1 | a (A) | Retenu |", "|---|---|---|---|---|---|---|"]
for ed in EDITIONS:
    if (ed, "A") not in RES: continue
    ra, rb, r0 = RES[(ed, "A")], RES[(ed, "B")], RES[(ed, "0")]
    L_.append(f"| {ed} | {ra['n']} | {f2(ra['mae'])} / {f2(ra['a1'], 1)} % | {f2(rb['mae'])} / {f2(rb['a1'], 1)} % | {f2(r0['mae'])} / {f2(r0['a1'], 1)} % | {f2(ra['P']['a'], 3)} | {MEILLEUR[ed]} |")
L_ += ["", f"Pente coût → niveau (conversion a) : " + " ; ".join(f"{ed} {f2(K[ed], 3)}" for ed in EDITIONS + ['D&D 5'] if K.get(ed)), "",
       "## 3. Les cercles de Forme", "",
       "p et relation par édition (modèle retenu) ; converti a = (p + relation) × pente D&D 5 ÷ pente de l'édition, à la taille médiane de ses",
       "formes ; Inarama : D&D 5 (5e et 2024) si 10 formes, sinon le médian des convertis. « [ ] » = moins de 10 formes.", "",
       "| Cercle | Valeur | Mots | Satellites | Lecture | Formes par édition | p et relation par édition | Sans taille | Converti a | Inarama |",
       "|---|---|---|---|---|---|---|---|---|---|"]
CERCLES2 = []
for fid in sorted(CF):
    e = CF[fid]; fp = formes_par(fid)
    if not fp: fp = collections.Counter()
    cells, convs, par_ed = [], [], {}
    for ed in EDITIONS:
        if not fp.get(ed): continue
        mo = MEILLEUR.get(ed, "B"); P = RES[(ed, mo)]["P"]
        p = P["p"].get(fid); b_ = P["b"].get(fid)
        rel = (f"a {f2(P['a'], 2)} × log2(cibles)" if (mo == "A" and fid in GUIDE) else f"b {f2(b_, 2)} × log2(taille)" if b_ is not None else "aucune (p seul)")
        ok = fp[ed] >= MIN
        cells.append(f"{ed} {'' if ok else '['}p {f2(p)} + {rel}{'' if ok else ']'}")
        ds = [d for d in FD if d["forme_id"] == fid and ed_de(d) == ed]
        pm = statistics.median(prix_forme(d, P) or 0 for d in ds) if ds else None
        cv = conv(pm, ed); convs.append((ed, cv, fp[ed]))
        par_ed[ed] = dict(formes=fp[ed], modele=mo, p=p, a=P["a"] if (mo == "A" and fid in GUIDE) else None, b=b_, prix_median=pm, converti_a=cv, retenu=ok)
    dnd = [cv for ed, cv, n in convs if ed in ("5e", "2024") and cv is not None]
    ndnd = sum(n for ed, cv, n in convs if ed in ("5e", "2024"))
    inar = (statistics.median(dnd) if dnd and ndnd >= MIN else statistics.median([cv for _, cv, _ in convs if cv is not None]) if any(cv is not None for _, cv, _ in convs) else None)
    inar = max(PLANCHER, inar) if inar is not None else PLANCHER
    st = sum(1 for d in FD if d["forme_id"] == fid and not d["taille"])
    sats = "; ".join(f"{s['valeur'] if isinstance(s, dict) else s[1]}" + (f" « {(s['texte'] if isinstance(s, dict) else s[2]).lower()} »" if (s['texte'] if isinstance(s, dict) else s[2]) else "") for s in e["satellites"])
    L_.append(f"| {fid} | {e['valeur']} | {' · '.join(w.lower() for w in e['mots']) or '—'} | {sats or '—'} | {e['lectures'][0][:40]} | "
              + ", ".join(f"{ed} {fp[ed]}" for ed in EDITIONS if fp.get(ed)) + f" | {' ; '.join(cells) or '—'} | {st} | "
              + " ; ".join(f"{ed} {f2(cv)}" for ed, cv, _ in convs) + f" | {f2(inar)} |")
    CERCLES2.append(dict(id=fid, type="FORME", valeur=e["valeur"], mots=e["mots"], satellites=e["satellites"], lecture=e["lectures"][0],
                         par_edition=par_ed, sans_taille=st, prix_inarama=inar,
                         regle="p + relation à la taille (modèle retenu par édition : A tableau du guide, B pente libre sur log2 de la taille) ; plancher 0,01"))
# satellites de Forme
L_ += ["", "## 4. Les satellites de Forme portés par d'autres cercles (candidats de règles de relation)", "",
       "Reste moyen (niveau − coût, sort caché) des formes qui portent le satellite, comparé à celui des autres formes de même genre de l'édition :",
       "un reste nettement positif dit que le coût actuel (une seule cible) est trop bas, et que la Forme devrait agir comme une zone.", "",
       "| Porteur | Satellite | Édition | Formes | Reste moyen | Autres formes du genre | Écart |", "|---|---|---|---|---|---|---|"]
SAT = collections.defaultdict(list)
for d in VAR.values():
    for r in d["x"]["_f"]["rings"]:
        if r[0] == "FORME": continue
        for s_ in (r[4] if len(r) > 4 and r[4] else []):
            if _txt(s_).split()[:1] == ["FORME"]:
                SAT[(ident(BC.cle_cercle(r)) or "?", r[0], f"{s_[1]} « {_txt(s_).lower()} »", ed_de(d))].append(d)
for (pid, crit, lab, ed), ds in sorted(SAT.items()):
    g = ds[0]["x"]["a"]["genre"]
    m1, e1, n1 = moyenne_err([d["x"]["niveau"] - d["cout_c"] for d in ds])
    m0, e0, n0 = moyenne_err([d["x"]["niveau"] - d["cout_c"] for d in VAR.values() if ed_de(d) == ed and d["x"]["a"]["genre"] == g and d not in ds])
    L_.append(f"| {pid} ({crit.lower()}) | {lab} | {ed} | {n1} | {f2(m1)} | {f2(m0)} ({n0}, {g}) | {f2(m1 - m0 if m0 is not None else None)} |")
L_ += ["", f"{len({k[:3] for k in SAT})} satellites différents (porteur, satellite) ; {sum(len(v) for v in SAT.values())} formes.", ""]
open(os.path.join(OUT, "catalogue_lot2_corps.md"), "w", encoding="utf-8").write("\n".join(L_) + "\n")
cat["cercles"] = [c for c in cat["cercles"] if c["type"] != "FORME"] + CERCLES2
cat["regles_verifiees"] = [dict(regle=r[0], edition=r[1], en_place=r[2], reglee=r[3], formes=r[4], concernees=r[5], verdict=r[6]) for r in REGLES]
cat["formes_modeles"] = {f"{ed}|{mo}": dict(a=v["P"]["a"], formes=v["n"], ecart_absolu=v["mae"], a_1_pres=v["a1"]) for (ed, mo), v in RES.items()}
cat["pente_cout_niveau"] = {ed: v for ed, v in K.items()}
json.dump(cat, open(os.path.join(OUT, "catalogue_prix.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok", len(FD), len(REGLES))
