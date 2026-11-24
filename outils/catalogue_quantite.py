"""Catalogue des prix des cercles, lot 1 : la Quantité (25 novembre 2026). Un calcul : rien n'est écrit dans la bibliothèque.

    python outils/catalogue_quantite.py <dossier de sortie> <dossier des documents du barème> <repertoire_cercles_v6.json>

Principe (décision de l'utilisateur) : l'unité est le CERCLE ; chaque cercle du catalogue reçoit SON prix (plancher 0,01, le Noyau
excepté) ; un satellite agit sur son porteur : son effet est une règle de relation, mesurée ici, pas additionnée. Prix réglés par
système ET par édition (5e, 2024, 3.5, PF1, PF2, PF2 remaniée), puis convertis vers Inarama (calé sur D&D 5).

Ce lot : les 18 cercles de Quantité (« instances » : des fois le sort ; « mesure » : autre chose, dit par ses mots), et les
satellites de Quantité portés par d'autres cercles.
- Coût de la forme SANS le cercle : le moteur du barème v8 (outils/mesure_bareme_cercles_v8.py, sans cacher et en sort caché) sur la
  forme dont la Quantité est retirée — ce qui retire aussi ce qu'elle faisait ailleurs (montant multiplié des blessures, log2 du
  nombre des êtres appelés : l'analyse les lit dans le cercle de Quantité).
- prix du cercle = s × log2(n), au moins 0,01 ; s ≥ 0 réglé par moindres carrés sur niveau − coût sans le cercle.
- Satellites : la pente de (niveau − coût du porteur sans le satellite) sur log2(n), par sorte de porteur, système et édition.
- Conversion vers D&D 5 : a) rapport des pentes coût → niveau ; b) écart médian, cercle par cercle (méthode de la v5).
"""
import os, sys, json, math, collections, statistics, re
ICI = os.path.dirname(os.path.abspath(__file__))
OUT, DOCS, REP = sys.argv[1], sys.argv[2], sys.argv[3]
V8 = os.path.join(ICI, "mesure_bareme_cercles_v8.py")
src = open(V8, encoding="utf-8").read()
src = src[:src.index("M0 = modele(None)")]
src = src.replace('''        F.append(x)\n''', '''        x["_f"] = dict(rings=f["rings"], verb=f.get("verb"))\n        F.append(x)\n''', 1)
ns = {"__file__": V8, "__name__": "v8"}
sys.argv = [V8, OUT, DOCS]
exec(compile(src, V8, "exec"), ns)
F, BC, modele, calcul, SYSTEMES = ns["F"], ns["BC"], ns["modele"], ns["calcul"], ns["SYSTEMES"]
EDITIONS = ["5e", "2024", "3.5", "PF1", "PF2", "PF2 remaniée"]
MIN = 10
PLANCHER = 0.01

rep = json.load(open(REP, encoding="utf-8"))["cercles"]
IDS = {}
for e in rep:
    IDS[(e["type"], json.dumps(e["valeur"], ensure_ascii=False), tuple(e["mots"]), tuple(json.dumps(s, ensure_ascii=False) for s in e["satellites"]))] = e["id"]
def ident(u): return IDS.get(u) or IDS.get((u[0], u[1], u[2], tuple(json.dumps(json.loads(s), ensure_ascii=False) for s in u[3])))
CQ = {e["id"]: e for e in rep if e["type"] == "QUANTITE"}


def _txt(s): return s[2] if len(s) > 2 and isinstance(s[2], str) else ""
def _sym(v): return isinstance(v, (tuple, list)) and len(v) == 2 and v[0] == "sym"
def num(v): return isinstance(v, (int, float)) and not isinstance(v, bool)


def refait(x, rings):
    """la forme x relue sur d'autres cercles (même sort, même jeu)"""
    a = BC.analyse(dict(rings=rings, verb=x["_f"]["verb"]))
    m = a["mesures"]
    g = ("état : " + (a["famille"] or "?")) if a["genre"] == "état" else a["genre"]
    fg = m.get("figure")
    return dict(x, a=a, groupe=g, v=(math.log2(max(m["cibles"], 1)), m["marche"], -(1.0 if m["restriction"] else 0.0), -(1.0 if m.get("sursaut") else 0.0)),
                fig=(fg[0], fg[1]) if fg and fg[1] is not None else None, fig_nom=fg[0] if fg else None)


def cout(x, M): return calcul(x, M, "propre")[0]


def genre_eff(x):
    g = x["a"]["genre"]
    return g if g in ("blessure", "être appelé") else "autre"


# ---------------------------------------------------------------- les cercles de Quantité et les satellites de Quantité
QF = []          # (x, ring, id, sorte, n)
for x in F:
    if x["a"]["sans_impact"]: continue
    for r in x["_f"]["rings"]:
        if r[0] != "QUANTITE" or not num(r[1]): continue
        u = BC.cle_cercle(r); cid = ident(u)
        if cid not in CQ: continue
        n = float(r[1])
        for s_ in (r[4] if len(r) > 4 and r[4] else []):
            if _txt(s_).startswith("QUANTITE MULTIPLIE") and num(s_[1]): n *= s_[1]
            if _txt(s_).startswith("QUANTITE FRACTIONNE") and num(s_[1]) and s_[1]: n /= s_[1]
        QF.append((x, r, cid, "instances" if not r[2] else "mesure", n))
print("formes à Quantité", len(QF))


def sat_sorte(porteur, s_):
    """la sorte d'un satellite de Quantité (ou None) : (sorte du porteur, n)"""
    t, v = _txt(s_), s_[1]
    if _sym(v): return None
    n = 10.0 if v == "plein" else float(v) if num(v) else None
    if n is None: return None
    if porteur == "CIBLE" and not t: return ("Cible : Quantité", n)
    if porteur == "CONDITION" and (t.startswith("OFFICIANT") or not t): return ("Condition : officiants", n)
    if t.startswith("QUANTITE"):
        w = t.split()[1:] or ["(sans mot)"]
        if w[0] == "FRACTIONNE": n = 1.0 / n if n else None
        return (f"{porteur.capitalize()} : Quantité « {' · '.join(x_.lower() for x_ in w)} »", n)
    return None


SF = []          # (x, index du cercle, index du satellite, sorte, n, id du porteur)
for x in F:
    if x["a"]["sans_impact"]: continue
    for i, r in enumerate(x["_f"]["rings"]):
        for j, s_ in enumerate(r[4] if len(r) > 4 and r[4] else []):
            so = sat_sorte(r[0], s_)
            if so and so[1]: SF.append((x, i, j, so[0], so[1], ident(BC.cle_cercle(r))))
print("formes à satellite de Quantité", len(SF))

# ---------------------------------------------------------------- les coûts sans le cercle / sans le satellite, sans cacher et en sort caché
M0 = modele(None)
cles = sorted({x["cle"] for x, *_ in QF} | {x["cle"] for x, *_ in SF})
MC = {}
for i, c in enumerate(cles):
    MC[c] = modele(c)
    if i % 100 == 0: print("sort caché", i, "/", len(cles), flush=True)
ROWS, SROWS = [], []
for x, r, cid, sorte, n in QF:
    xs = refait(x, [q for q in x["_f"]["rings"] if q is not r])
    ROWS.append(dict(x=x, id=cid, sorte=sorte, n=n, L=math.log2(n), sans=cout(xs, M0), sans_c=cout(xs, MC[x["cle"]]),
                     avec=cout(x, M0), genre=genre_eff(x)))
for x, i, j, so, n, pid in SF:
    rings = list(x["_f"]["rings"]); r = rings[i]
    sats = [s_ for k, s_ in enumerate(r[4]) if k != j]
    rings[i] = (*r[:4], sats, *r[5:])
    xs = refait(x, rings)
    SROWS.append(dict(x=x, sorte=so, n=n, L=math.log2(n), porteur=pid, sans=cout(xs, M0), sans_c=cout(xs, MC[x["cle"]]), avec=cout(x, M0)))


def pente(pts, positif=True):
    den = sum(L * L for L, _ in pts)
    if not den: return None
    s_ = sum(L * y for L, y in pts) / den
    return max(0.0, s_) if positif else s_


# ---------------------------------------------------------------- réglage de s
S = {}           # (sorte, édition, genre ou None, caché?) -> (s, formes)
for sorte in ("instances", "mesure"):
    for ed in EDITIONS + ["D&D 5"]:
        for gen in (None, "blessure", "être appelé", "autre"):
            pts = [r for r in ROWS if r["sorte"] == sorte and (r["x"]["jeu"] == ed or (ed == "D&D 5" and r["x"]["systeme"] == "D&D 5"))
                   and (gen is None or r["genre"] == gen)]
            if not pts: continue
            for cache in (False, True):
                k_ = "sans_c" if cache else "sans"
                S[(sorte, ed, gen, cache)] = (pente([(p["L"], p["x"]["niveau"] - p[k_]) for p in pts]), len(pts))
SS = {}          # satellites : (sorte, édition, caché?) -> (pente, formes)
for so in sorted({r["sorte"] for r in SROWS}):
    for ed in EDITIONS + ["D&D 5"]:
        pts = [r for r in SROWS if r["sorte"] == so and (r["x"]["jeu"] == ed or (ed == "D&D 5" and r["x"]["systeme"] == "D&D 5"))]
        if not pts: continue
        for cache in (False, True):
            k_ = "sans_c" if cache else "sans"
            SS[(so, ed, cache)] = (pente([(p["L"], p["x"]["niveau"] - p[k_]) for p in pts], positif=False), len(pts))

# ---------------------------------------------------------------- conversion a : pente coût → niveau, par édition (toutes les formes, barème v8)
def pente_niveau(xs):
    cs = [cout(x, M0) for x in xs]; ns_ = [x["niveau"] for x in xs]
    mc, mn = statistics.mean(cs), statistics.mean(ns_)
    v_ = sum((c_ - mc) ** 2 for c_ in cs)
    return sum((c_ - mc) * (n_ - mn) for c_, n_ in zip(cs, ns_)) / v_ if v_ else None
K = {}
for ed in EDITIONS:
    xs = [x for x in F if x["jeu"] == ed and not x["a"]["sans_impact"]]
    if xs: K[ed] = (pente_niveau(xs), len(xs))
xs = [x for x in F if x["systeme"] == "D&D 5" and not x["a"]["sans_impact"]]
K["D&D 5"] = (pente_niveau(xs), len(xs))


def s_de(sorte, ed, cache=True):
    v_ = S.get((sorte, ed, None, cache)); return v_
def prix(sorte, ed, n, cache=True):
    v_ = s_de(sorte, ed, cache)
    if not v_ or v_[0] is None: return None
    return max(PLANCHER, v_[0] * math.log2(n))


# s retenu : 10 formes au moins ; Inarama : D&D 5 (5e et 2024 ensemble) s'il a 10 formes, sinon le médian des s convertis (a)
def retenu(sorte, ed): v_ = s_de(sorte, ed); return v_ if v_ and v_[1] >= MIN else None
def conv_a(sorte, ed):
    v_ = retenu(sorte, ed)
    if not v_ or not K.get(ed) or not K[ed][0]: return None
    return v_[0] * K["D&D 5"][0] / K[ed][0]
S_INAR = {}
for sorte in ("instances", "mesure"):
    v_ = retenu(sorte, "D&D 5")
    if v_: S_INAR[sorte] = (v_[0], "D&D 5 (5e et 2024 ensemble)")
    else:
        cv = [conv_a(sorte, ed) for ed in EDITIONS if conv_a(sorte, ed) is not None]
        S_INAR[sorte] = (statistics.median(cv), "médian des s convertis (a)") if cv else (None, "aucune édition n'a 10 formes")

# conversion b (v5) : écart médian, cercle par cercle, entre le prix en D&D 5 et le prix dans l'édition
def formes_par(cid):
    c_ = collections.Counter(r["x"]["jeu"] for r in ROWS if r["id"] == cid); return c_
CONV_B = {}
for ed in EDITIONS:
    d_ = []
    for cid, e in CQ.items():
        fp = formes_par(cid); sorte = "instances" if not e["mots"] else "mesure"
        n = float(e["valeur"])
        if fp.get(ed) and (fp.get("5e") or fp.get("2024")):
            a_, b_ = prix(sorte, "D&D 5", n), prix(sorte, ed, n)
            if a_ is not None and b_ is not None: d_.append(a_ - b_)
    CONV_B[ed] = (statistics.median(d_) if d_ else None, len(d_))

# ---------------------------------------------------------------- les fichiers
def f2(v, d=2): return "—" if v is None else f"{v:.{d}f}"
L_ = ["# Catalogue des prix des cercles — lot 1 : la Quantité", "",
      "*Branche `catalogue` (partie de `bareme-cercles-v6` 7d1e04c), 25 novembre 2026. Un calcul : rien n'est écrit dans la bibliothèque.*", "",
      "Méthode : coût de la forme SANS le cercle de Quantité (moteur du barème v8, la Quantité retirée — et avec elle le montant multiplié des",
      "blessures et le log2 du nombre des êtres appelés, que l'analyse lit dans ce cercle) ; prix = s × log2(n), au moins 0,01 ; s ≥ 0 réglé par",
      "moindres carrés sur niveau − coût sans le cercle, par sorte (« instances », « mesure »), système et édition. « Sort caché » : le modèle",
      "du barème (relations, prix propres, conversion) refait sans le sort mesuré. Moins de 10 formes : s donné, non retenu.", "",
      "## 1. Les cercles de Quantité", "",
      "Prix par édition = s(édition, sort caché) × log2(n) ; converti a = s × (pente coût → niveau de D&D 5 ÷ celle de l'édition) ;",
      "converti b = prix de l'édition + écart médian D&D 5 − édition (méthode de la v5). Inarama proposé : s de D&D 5 (5e et 2024 ensemble) ×",
      "log2(n), au moins 0,01. « (n) » = formes ; un prix entre crochets vient d'un s réglé sur moins de 10 formes.", "",
      "| Cercle | Valeur | Mots | Sorte | Formes par édition | Prix par édition | Converti a | Converti b | Inarama proposé |",
      "|---|---|---|---|---|---|---|---|---|"]
JSON = []
for cid in sorted(CQ):
    e = CQ[cid]; sorte = "instances" if not e["mots"] else "mesure"; n = float(e["valeur"])
    fp = formes_par(cid)
    pr, ca, cb, par_ed = [], [], [], {}
    for ed in EDITIONS:
        if not fp.get(ed): continue
        v_ = s_de(sorte, ed); p_ = prix(sorte, ed, n)
        ok = v_ and v_[1] >= MIN
        pr.append(f"{ed} {'' if ok else '['}{f2(p_)}{'' if ok else ']'}")
        a_ = conv_a(sorte, ed); a_p = max(PLANCHER, a_ * math.log2(n)) if a_ is not None else None
        b_ = (p_ + CONV_B[ed][0]) if (p_ is not None and CONV_B[ed][0] is not None) else None
        ca.append(f"{ed} {f2(a_p)}"); cb.append(f"{ed} {f2(b_)}")
        par_ed[ed] = dict(formes=fp[ed], prix=p_, s=v_[0] if v_ else None, s_formes=v_[1] if v_ else 0, retenu=bool(ok), converti_a=a_p, converti_b=b_)
    si = S_INAR[sorte][0]; inar = max(PLANCHER, si * math.log2(n)) if si is not None else None
    L_.append(f"| {cid} | {e['valeur']} | {' · '.join(w.lower() for w in e['mots']) or '—'} | {sorte} | "
              + ", ".join(f"{ed} {fp[ed]}" for ed in EDITIONS if fp.get(ed)) + f" | {' ; '.join(pr)} | {' ; '.join(ca)} | {' ; '.join(cb)} | {f2(inar)} |")
    JSON.append(dict(id=cid, type="QUANTITE", valeur=e["valeur"], mots=e["mots"], sorte=sorte, n=n, par_edition=par_ed, prix_inarama=inar,
                     regle=f"s × log2(n), au moins {PLANCHER} ; s Inarama = {f2(si, 3)} ({S_INAR[sorte][1]})"))
L_ += ["", "## 2. Les pentes s (par sorte, système et édition ; sans cacher | sort caché ; formes)", "",
       "| Sorte | Édition | Genre | s sans cacher | s sort caché | Formes | Retenu |", "|---|---|---|---|---|---|---|"]
for (sorte, ed, gen, cache), v_ in sorted(S.items(), key=lambda t: (t[0][0], (EDITIONS + ["D&D 5"]).index(t[0][1]), str(t[0][2]))):
    if cache: continue
    vc = S[(sorte, ed, gen, True)]
    L_.append(f"| {sorte} | {ed} | {gen or 'tous'} | {f2(v_[0], 3)} | {f2(vc[0], 3)} | {v_[1]} | {'oui' if v_[1] >= MIN and gen is None else 'non' if gen is None else '—'} |")
L_ += ["", "Pente coût → niveau (toutes les formes de l'édition, barème v8, propres unités) : "
       + " ; ".join(f"{ed} {f2(K[ed][0], 3)} ({K[ed][1]})" for ed in EDITIONS + ['D&D 5'] if ed in K),
       "Écart médian D&D 5 − édition, cercle par cercle (conversion b) : "
       + " ; ".join(f"{ed} {f2(CONV_B[ed][0])} ({CONV_B[ed][1]} cercles)" for ed in EDITIONS), "",
       "s d'Inarama : " + " ; ".join(f"{so} {f2(v_[0], 3)} ({v_[1]})" for so, v_ in S_INAR.items()), ""]
# satellites
L_ += ["## 3. Les satellites de Quantité portés par d'autres cercles (candidats de règles de relation)", "",
       "Pas additionnés : pour chaque sorte de porteur, la pente de (niveau − coût du porteur sans le satellite) sur log2(n) (n « plein » = 10 ;",
       "« fractionné » d = 1/d), par édition, sans cacher | sort caché. Une pente négative est donnée telle quelle.", "",
       "| Sorte de satellite | Édition | Pente sans cacher | Pente sort caché | Formes |", "|---|---|---|---|---|"]
for (so, ed, cache), v_ in sorted(SS.items(), key=lambda t: (t[0][0], (EDITIONS + ["D&D 5"]).index(t[0][1]))):
    if cache: continue
    L_.append(f"| {so} | {ed} | {f2(v_[0], 3)} | {f2(SS[(so, ed, True)][0], 3)} | {v_[1]} |")
L_ += ["", "Chaque satellite (porteur, valeur, mots, formes par édition) :", "",
       "| Porteur | Sorte | n | Formes par édition |", "|---|---|---|---|"]
grp = collections.defaultdict(collections.Counter)
for r in SROWS: grp[(r["porteur"], r["sorte"], r["n"])][r["x"]["jeu"]] += 1
for (pid, so, n), c_ in sorted(grp.items(), key=lambda t: (t[0][1], str(t[0][0]), t[0][2])):
    L_.append(f"| {pid or '?'} | {so} | {n:g} | " + ", ".join(f"{ed} {c_[ed]}" for ed in EDITIONS if c_.get(ed)) + " |")
L_ += ["", f"{len(grp)} satellites différents (porteur, sorte, valeur) ; {len(SROWS)} formes ; sortes : "
       + ", ".join(f"{so} ({sum(1 for r in SROWS if r['sorte'] == so)} formes)" for so in sorted({r['sorte'] for r in SROWS})), ""]
open(os.path.join(OUT, "catalogue_lot1_corps.md"), "w", encoding="utf-8").write("\n".join(L_) + "\n")
json.dump(dict(_lisez_moi="Catalogue des prix des cercles (début : lot 1, la Quantité). Un cercle par entrée, identifié comme au répertoire "
                          "(repertoire_cercles_v6.json) ; prix par édition (s × log2(n), s réglé en sort caché sur les formes de l'édition ; "
                          "« retenu » : s réglé sur 10 formes ou plus), convertis vers D&D 5 (a : rapport des pentes coût → niveau ; b : écart "
                          "médian, méthode de la v5) ; prix d'Inarama proposé. Plancher 0,01. Le Noyau vaut 0.",
               plancher=PLANCHER, s_inarama={k: dict(s=v[0], source=v[1]) for k, v in S_INAR.items()},
               pentes={f"{so}|{ed}|{gen or 'tous'}|{'cache' if c else 'sans_cacher'}": dict(s=v[0], formes=v[1]) for (so, ed, gen, c), v in S.items()},
               satellites={f"{so}|{ed}|{'cache' if c else 'sans_cacher'}": dict(pente=v[0], formes=v[1]) for (so, ed, c), v in SS.items()},
               pente_cout_niveau={ed: dict(pente=v[0], formes=v[1]) for ed, v in K.items()}, conversion_b={ed: dict(ecart=v[0], cercles=v[1]) for ed, v in CONV_B.items()},
               cercles=JSON), open(os.path.join(OUT, "catalogue_prix.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok", len(ROWS), len(SROWS))
