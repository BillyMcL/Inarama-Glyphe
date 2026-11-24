"""Barème par cercles, version 6 (24 novembre) : la mesure refaite sur les glyphes corrigés (main 019a95f, m128), et les trois prix
laissés ouverts : les mécaniques des bonus (a × degré par mécanique et par système ; prix fixe pour avantage, désavantage, relance),
la nouvelle chance (un rabais réglé comme une relation, d ≤ 0), les figures à part (a_fig × log2 de la taille écrite, par figure et
par système). Le reste comme en v5 (moteur/bareme_cercles.py : version B, effets uniques, conversion au cercle, sort caché).
Rien n'est écrit dans la bibliothèque.

    python outils/mesure_bareme_cercles_v6.py <dossier de sortie> <dossier des documents du barème> [<couts v5>]
"""
import os, sys, json, math, collections, statistics, re
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ICI, "..", "moteur")); os.chdir(os.path.join(ICI, "..", "moteur"))
import convert as C, corrections as K, bareme_cercles as BC, concentration as CC, constats as B13, bareme as B
from fiches import FICHES
OUT, DOCS = sys.argv[1], sys.argv[2]
SYSTEME = {"5.1": "D&D 5", "5.2": "D&D 5", "3.5": "3.5", "pf1": "PF1", "pf2": "PF2", "pf2r": "PF2"}
JEU = {"5.1": "5e", "5.2": "2024", "3.5": "3.5", "pf1": "PF1", "pf2": "PF2", "pf2r": "PF2 remaniée"}
AUTRES = ["3.5", "PF1", "PF2"]
SYSTEMES = ["D&D 5"] + AUTRES
GEN = BC.GEN


def source(f):
    d = f["dnd"]
    return ("er" if d.startswith("Elden Ring") else "pf2r" if d.startswith("Pathfinder 2 (version") else "pf2" if d.startswith("Pathfinder 2")
            else "pf1" if d.startswith("Pathfinder 1") else "3.5" if "D&amp;D 3.5" in d else "5.2" if "2024" in d else "5.1")


# niveau source le plus bas en 3.5 et en PF1 (décision du 23 novembre) : le plus bas des niveaux par classe, lu dans la source
CLS35 = {"Brd", "Clr", "Drd", "Pal", "Rgr", "Sor/Wiz", "Sor", "Wiz", "Adp", "Asn", "Blk", "Hlr", "Duskblade"}
_PF1 = {x["Name"]: x for x in json.load(open(os.path.join(ICI, "..", "donnees", "pf1", "sorts-pf1.json"), encoding="utf-8"))}
MULTI = {}
def niveaux_classes(cle, jeu):
    r = CC._source(cle, jeu)
    if r is None: return {}
    out = {}
    if jeu == "3.5":
        for part in (r.get("_fields") or {}).get("level", "").split(","):
            m = re.match(r"\s*(.+?)\s+(\d+)\s*$", part)
            if m and m.group(1).strip() in CLS35: out[m.group(1).strip()] = int(m.group(2))
    else:
        x = _PF1.get(r["name"]) or {}
        for cls, L in (x.get("access_ways") or {}).get("Level", []):
            if cls not in ("adept", "red mantiss assasin", "sahirafiyun"): out[cls] = L
    return out


def absorption_lue(u):
    """(montant, contre un seul élément) d'un cercle d'absorption chiffré ; None sinon"""
    if "ABSORPTION" not in u[2]: return None
    v = json.loads(u[1])
    if not isinstance(v, (int, float)) or isinstance(v, bool): return None
    elem = False
    for s in u[3]:
        sv = json.loads(s)[1]
        if isinstance(sv, list) and len(sv) == 2 and sv[0] == "sym" and sv[1] in ("feu", "air", "terre", "eau"): elem = True
    return (v, elem)


def tranche(n): return "0" if n == 0 else "1-2" if n <= 2 else "3-4" if n <= 4 else "5-6" if n <= 6 else "7-9" if n <= 9 else "10"


def zone_std(rings):
    """(forme du tableau, log2 de sa taille écrite) pour une zone ordinaire (sphère, cube, cône, ligne, cylindre) : la référence
    à laquelle on compare les figures à part"""
    f_ = next((r for r in rings if r[0] == "FORME"), None)
    a_ = next((r for r in rings if r[0] == "AMPLEUR"), None)
    if f_ is None or a_ is None or not BC._num(a_[1]) or tuple(a_[2]) not in BC.UNITE_BASE: return None
    nom = {"plein": "sphère", 4: "cube", 3: "cône", 1: "ligne", 9: "cylindre"}.get(f_[1])
    if nom is None: return None
    return (nom, math.log2(max(a_[1] * BC.UNITE_BASE[tuple(a_[2])], 1)))


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
        niv = int(f["level"])
        if src in ("3.5", "pf1"):
            jj = "3.5" if src == "3.5" else "PF1"
            if (cle, jj) not in MULTI:
                lv = niveaux_classes(cle, jj)
                MULTI[(cle, jj)] = (f["fr"], niv, min(lv.values()), max(lv.values()), lv) if len(set(lv.values())) > 1 else None
            if MULTI[(cle, jj)]: niv = MULTI[(cle, jj)][2]
        x = dict(cle=cle, sort=f["fr"], jeu=JEU[src], systeme=SYSTEME[src], forme=f["label"], niveau=niv, niveau_bibliotheque=int(f["level"]), a=a, sig=sig, groupe=g,
                 v=(math.log2(max(m["cibles"], 1)), m["marche"], -(1.0 if m["restriction"] else 0.0), -(1.0 if m.get("sursaut") else 0.0)),
                 fixe=a["genre"] in ("blessure", "soin"),
                 paye=not a["sans_impact"] and not sans_prix, unique=(sans_prix[0]["cercle"] if len(a["effets"]) == 1 and sans_prix else None),
                 puissance1=any(r[0] == "IMPACT" and r[2][:1] == ["PUISSANCE"] and r[1] == 1 for r in f["rings"]),
                 impacts_plein=[(tuple(r[2])) for r in f["rings"] if r[0] == "IMPACT" and r[1] == "plein"])
        x["y"] = x["niveau"] - a["prix_effet"] - a["decides"]
        ab_ = [e for e in a["effets"] if e["sans_prix"] and absorption_lue(e["cercle"])]
        x["abs_seul"] = absorption_lue(ab_[0]["cercle"]) if len(a["effets"]) == 1 and ab_ else None
        x["etre_plein"] = any(e["sans_prix"] and e["cercle"][2][:1] == ("PUISSANCE",) for e in a["effets"])
        x["a_meca"] = any(e.get("meca") for e in a["effets"])
        x["meca_seul"] = (a["effets"][0]["meca"], a["effets"][0]["degre"]) if len(a["effets"]) == 1 and a["effets"][0].get("meca") else None
        fg = m.get("figure")
        x["fig"] = (fg[0], fg[1]) if fg and fg[1] is not None else None
        x["fig_nom"] = fg[0] if fg else None
        x["zone_std"] = zone_std(f["rings"]) if not fg else None
        F.append(x)
print("formes", len(F))


# ---------------------------------------------------------------- relations (moteur : version B), par sommes
STATS = collections.defaultdict(BC.sommes_vides); PAR_CLE = collections.defaultdict(lambda: collections.defaultdict(BC.sommes_vides))
for x in F:
    if not x["paye"] or x["a_meca"] or x["fig_nom"]: continue
    for k in ((x["systeme"], x["groupe"]), (x["systeme"], GEN)):
        BC.sommes_ajoute(STATS[k], x["v"], x["y"]); BC.sommes_ajoute(PAR_CLE[x["cle"]][k], x["v"], x["y"])
GROUPES = sorted({x["groupe"] for x in F})


def relx(r, x):
    """a × log2(cibles) + b × marche + c × restriction + d × nouvelle chance (c, d ≤ 0)"""
    return r["a"] * x["v"][0] + r["b"] * x["v"][1] - r["c"] * x["v"][2] - r.get("d", 0.0) * x["v"][3]


MECA_MIN = FIG_MIN = 15
MECAS_TOUTES = ["protection", "renfort", "faiblesse", "chance", "malchance", "seuil", "mesure", "surcroît",
                "avantage", "désavantage", "relance", "relance au pire"]
FIGS = ["mur et paroi", "dôme", "explosion", "disque", "pont", "figure 2", "figure 9", "plein", "hélice"]


def pente(pts):
    """a ≥ 0 tel que y ≈ a × x (moindres carrés par l'origine)"""
    den = sum(u * u for u, _ in pts)
    return max(0.0, sum(u * y for u, y in pts) / den) if den else None


def par_systeme(pts_par_s, fn, mini, dnd_autres=False):
    """pour chaque système : sa règle s'il a assez de formes, sinon celle des autres systèmes ensemble ; D&D 5 compris, ou, comme
    les relations (dnd_autres), D&D 5 toujours réglé sur 3.5 + PF1 + PF2"""
    out = {}
    for s_ in SYSTEMES:
        own = pts_par_s.get(s_, [])
        if len(own) >= mini and not (dnd_autres and s_ == "D&D 5"): pts, src = own, "propre"
        else: pts, src = [p for s2 in SYSTEMES if s2 != s_ for p in pts_par_s.get(s2, [])], "autres systèmes ensemble"
        if not pts and own: pts, src = own, "propre (moins de 15 formes, aucune ailleurs)"
        if pts: out[s_] = (fn(pts), len(own), src, len(pts))
    return out


def modele(cache=None):
    """règles, prix propres et conversion, sans le sort « cache » (une clé)"""
    sub = PAR_CLE.get(cache, {}) if cache else {}
    st = lambda k: BC.sommes_moins(STATS[k], sub[k]) if k in sub else STATS[k]
    CO = {}
    for s in AUTRES:
        CO[s] = BC.regles_systeme(st((s, GEN)), {g: st((s, g)) for g in GROUPES})
    CO["D&D 5"] = BC.regles_systeme(BC.sommes_plus(*[st((s, GEN)) for s in AUTRES]),
                                    {g: BC.sommes_plus(*[st((s, g)) for s in AUTRES]) for g in GROUPES})
    co = {(s, g): r for s in CO for g, r in CO[s].items()}
    def regle(s, g): return BC.regle(CO[s], g)
    def reste(x, s_):            # niveau − prix − prix décidés − relations sans la part des cibles (pour les figures)
        r = regle(s_, x["groupe"]); return x["y"] - (r["b"] * x["v"][1] - r["c"] * x["v"][2] - r.get("d", 0.0) * x["v"][3])
    # figures à part (v6) : a_fig × log2(taille écrite), par figure et par système ; D&D 5 : les autres systèmes ensemble
    fp = collections.defaultdict(lambda: collections.defaultdict(list))
    for x in F:
        if x["fig"] is None or x["cle"] == cache or not x["paye"] or x["a_meca"]: continue
        fp[x["fig"][0]][x["systeme"]].append((x["fig"][1], reste(x, x["systeme"])))
    FIG = {}
    for fg, d_ in fp.items():
        for s_, v_ in par_systeme(d_, pente, FIG_MIN, dnd_autres=True).items(): FIG[(fg, s_)] = v_
    def figt(x, s_):
        if x["fig"] is None: return 0.0
        v_ = FIG.get((x["fig"][0], s_)); return (v_[0] or 0.0) * x["fig"][1] if v_ else 0.0
    pp = collections.defaultdict(list)
    for x in F:
        if x["unique"] is None or x["cle"] == cache: continue
        r = regle(x["systeme"], x["groupe"])
        pp[(x["unique"], x["systeme"])].append(x["niveau"] - x["a"]["decides"] - (relx(r, x)) - figt(x, x["systeme"]))
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
    # mécaniques des bonus (v6) : prix = a × degré par mécanique et par système (a ≥ 0) ; avantage, désavantage, relance : prix fixe
    mp = collections.defaultdict(lambda: collections.defaultdict(list))
    for x in F:
        if x["meca_seul"] is None or x["cle"] == cache: continue
        r = regle(x["systeme"], x["groupe"])
        mp[x["meca_seul"][0]][x["systeme"]].append((x["meca_seul"][1], x["niveau"] - x["a"]["decides"] - relx(r, x) - figt(x, x["systeme"])))
    MEC = {}
    for m_, d_ in mp.items():
        plein = all(u is None for s_ in d_ for u, _ in d_[s_])
        fn = (lambda pts: statistics.median(y for _, y in pts)) if plein else pente
        for s_, v_ in par_systeme(d_, fn, MECA_MIN).items(): MEC[(m_, s_)] = v_
    M = dict(regle=regle, pm=pm, pn={k: len(v) for k, v in pp.items()}, conv=conv, inar=inar, src=src_, co=co, fig=FIG, figt=figt, mec=MEC)
    for u, cibles in DECIDES.items():
        if u in CERCLES_DND or (u, "D&D 5") in pm: continue      # seulement les cercles sans équivalent en D&D 5 (aucune forme de D&D 5)
        vals = []
        for x, L in cibles:
            autres = [e for e in x["a"]["effets"] if e["cercle"] != u]
            def cout_(p):
                pr = [p] + [(inar.get(e["cercle"], 3.0) if e["sans_prix"] else e["prix"]) for e in autres]
                r = regle("D&D 5", x["groupe"])
                return BC.combiner(pr, x["a"].get("suggestion")) + x["a"]["decides"] + relx(r, x) + figt(x, "D&D 5")
            lo, hi = -20.0, 30.0
            for _ in range(60):
                mid = (lo + hi) / 2
                if cout_(mid) < L: lo = mid
                else: hi = mid
            vals.append(lo)
        if vals:
            inar[u] = statistics.median(vals); src_[u] = "décision : forme de base au niveau " + "/".join(sorted({f"{L:g}" for _, L in cibles}))
    return M


def calcul(x, M, mode):
    """(coût, palier, relations, prix des effets) ; mode « propre » (unités du système) ou « inarama »"""
    a = x["a"]; s = x["systeme"]
    prix = []
    for e in a["effets"]:
        if e.get("meca"):
            ss = s if mode == "propre" else "D&D 5"
            v_ = M["mec"].get((e["meca"], ss))
            if v_ is None or v_[0] is None: prix.append((e["prix"], f"mécanique {e['meca']} : pas de règle, échelle provisoire")); continue
            if e["degre"] is None: prix.append((v_[0], f"mécanique {e['meca']} : prix fixe {v_[0]:.2f} ({ss}, {v_[2]})")); continue
            prix.append((v_[0] * e["degre"], f"mécanique {e['meca']} : {v_[0]:.2f} × {e['degre']:g} ({ss}, {v_[2]})")); continue
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
    rel = relx(r, x) + M["figt"](x, s if mode == "propre" else "D&D 5")
    cout = pe + a["decides"] + rel
    return round(cout, 3), int(min(10, max(0, math.floor(cout + 0.5)))), round(rel, 3), prix, r


# les cercles des trois sorts (décision du 23 novembre) : chaque forme d'Arcane qui porte le cercle (sans prix) doit donner le niveau décidé
NIVEAUX_DECIDES = {"control-water": 4, "aura-of-the-unremarkable": 4}
CERCLES_DND = {e["cercle"] for x in F if x["systeme"] == "D&D 5" for e in x["a"]["effets"]}
DECIDES, CONSEIL = collections.defaultdict(list), {}
for x in F:
    if x["cle"] in NIVEAUX_DECIDES and x["a"]["effets"] and x["forme"].startswith("Forme arcane") or (x["cle"] in NIVEAUX_DECIDES and x["a"]["effets"] and "hybride" not in x["forme"].lower()):
        for e in x["a"]["effets"]:
            if e["sans_prix"] and (x, NIVEAUX_DECIDES[x["cle"]]) not in DECIDES[e["cercle"]]: DECIDES[e["cercle"]].append((x, NIVEAUX_DECIDES[x["cle"]]))
    if x["cle"] == "dream-council":
        for e in x["a"]["effets"]:
            if e["sans_prix"]: CONSEIL.setdefault(x["systeme"], set()).add(e["cercle"])
_c = list(CONSEIL.values())
CONSEIL_MEME = len(_c) == 2 and bool(_c[0] & _c[1])
if not CONSEIL_MEME:            # deux cercles distincts : chacun son niveau (PF1 6, PF2 8)
    for x in F:
        if x["cle"] == "dream-council" and "hybride" not in x["forme"].lower():
            for e in x["a"]["effets"]:
                if e["sans_prix"]: DECIDES[e["cercle"]].append((x, 6 if x["systeme"] == "PF1" else 8))
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
V5 = {}
if len(sys.argv) > 3:
    for r in json.load(open(sys.argv[3], encoding="utf-8"))["formes"]: V5[(r["cle"], r["jeu"], r["forme"])] = r
K5 = {"inarama_c": "inarama_sort_cache", "inarama": "inarama_sans_cacher", "propre_c": "systeme_sort_cache", "propre": "systeme_sans_cacher"}
def court(d):
    if not d: return f"{'—':^27s}"
    n = len(d); pc = lambda k: 100 * sum(1 for e in d if abs(e) <= k) / n
    return f"{pc(0):5.1f} {pc(1):5.1f} {pc(2):5.1f} {sum(d) / n:+.2f}"
def ecarts(xs, k, ver):
    xs = [x for x in xs if not x["a"]["sans_impact"]]
    if ver == "v6": return [x[k][1] - x["niveau"] for x in xs]
    rs = [V5.get((x["cle"], x["jeu"], x["forme"])) for x in xs]
    return [r[K5[k]]["palier"] - r["niveau"] for r in rs if r and K5[k] in r]
def paire(xs, k): return " | ".join(court(ecarts(xs, k, v)) for v in ("v5", "v6"))
def deux(xs, c1, c2):
    n = sum(1 for x in xs if not x["a"]["sans_impact"])
    return f"{n:5d} || {paire(xs, c1)} || {paire(xs, c2)}"
ENTETE = (f"  {'':22s}{'formes':>5s} || {'sort caché : v5':^27s} | {'v6':^27s} || {'sans cacher : v5':^27s} | {'v6':^27s}")
SOUS = f"  {'':22s}{'':5s} || " + " | ".join(["  bon   à 1   à 2  écart    "] * 2) + " || " + " | ".join(["  bon   à 1   à 2  écart    "] * 2)

avec = [x for x in F if not x["a"]["sans_impact"]]
dnd = [x for x in avec if x["systeme"] == "D&D 5"]
T = ["MESURE DU BARÈME PAR CERCLES, VERSION 6 — glyphes corrigés (m128) ; bonus, nouvelle chance, figures à part",
     "Branche bareme-cercles (bibliothèque de main 019a95f, m128 ; aucune forme changée par le barème). Formes : celles qui ont un cercle d'Impact, hors Elden Ring.",
     "Colonnes : formes || SORT CACHÉ (relations, prix propres, mécaniques, figures et conversion recalculés sans le sort mesuré) : v5 (anciens",
     "glyphes), v6 || SANS CACHER : v5, v6. Chaque bloc : bon palier %, à 1 près %, à 2 près %, écart moyen (palier − niveau).",
     "Sauf mention, les points C à E et I à P sont en v6. En 3.5 et PF1, le niveau source est le plus bas des niveaux par classe.", ""]
T += ["A. D&D 5 (5e et 2024) — palier d'Inarama", "=" * 40, "", ENTETE, SOUS,
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
      "  leur source.", ENTETE, SOUS]
for s in AUTRES:
    xs = [x for x in avec if x["systeme"] == s]
    T += [f"  {s}", f"    propres unités        {deux(xs, 'propre_c', 'propre')}", f"    converti (Inarama)    {deux(xs, 'inarama_c', 'inarama')}", "    par tranche (propres unités, sort caché : v4 B | v5) :"]
    for t in ["0", "1-2", "3-4", "5-6", "7-9", "10"]:
        g = [x for x in xs if tranche(x["niveau"]) == t]
        if g: T.append(f"      {t:18s}{len(g):5d} || {paire(g, 'propre_c')}")
    T.append("    par genre (propres unités, sort caché : v4 B | v5) :")
    for g in sorted({x["a"]["genre"] for x in xs}, key=lambda g: -sum(1 for x in xs if x["a"]["genre"] == g)):
        gx = [x for x in xs if x['a']['genre'] == g]; T.append(f"      {g:18s}{len(gx):5d} || {paire(gx, 'propre_c')}")
    T.append("")
T += [f"  Conversion au cercle (sans cacher) : " + " ; ".join(f"{s} {M0['conv'][s]:+.2f}" for s in AUTRES)
      + f"  (sur {', '.join(str(sum(1 for (u, ss) in M0['pm'] if ss == s and (u, 'D&D 5') in M0['pm'])) + ' cercles (' + s + ')' for s in AUTRES)})", "", ""]
# C. plus fort = plus cher
rep = {e["id"]: e for e in json.load(open(os.path.join(DOCS, "repertoire_cercles.json"), encoding="utf-8"))["cercles"]}
ids = {}
for e in json.load(open(os.path.join(DOCS, "repertoire_cercles.json"), encoding="utf-8"))["cercles"]:
    ids[(e["type"], json.dumps(e["valeur"], ensure_ascii=False), tuple(e["mots"]), tuple(json.dumps(s, ensure_ascii=False) for s in e["satellites"]))] = e["id"]
def ident(u): return ids.get(u) or ids.get((u[0], u[1], u[2], tuple(json.dumps(json.loads(s), ensure_ascii=False) for s in u[3])))
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
LAC_Z = lambda x: any(("zone sans" in l) or ("figure à part" in l) for l in x["a"]["lacunes"])
LAC_A = lambda x: any(w in causeA for w in x["impacts_plein"])
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
T += ["", f"  Cercles de cause A reconnus (Impact plein, mots de l'étape 3b) : {len(causeA)}.", "",
      "  Ce qu'il en est advenu (formes de la v5 → formes de la v6 ; v5 : mesure_bareme_cercles_v5.txt, point D) :",
      f"    cercles « plein » de cause A : 450 → {sum(1 for x in avec if LAC_A(x))} (les mots de l'étape 3b encore portés par un Impact plein)",
      f"    zones sans Forme ni taille : 1 022 → {sum(1 for x in avec if LAC_Z(x))}",
      f"    jet renouvelé : 146 formes des sorts du relevé ; aujourd'hui {sum(1 for x in avec if (x['sort'], jd(x)) in jet and x['v'][3])} d'entre elles portent la nouvelle chance,"
      f" et {sum(1 for x in avec if x['v'][3])} formes en tout",
      f"    mécaniques des bonus : 291 formes des sorts du relevé ; aujourd'hui {sum(1 for x in avec if (x['sort'], jd(x)) in bonus and x['a_meca'])} d'entre elles portent une mécanique,"
      f" et {sum(1 for x in avec if x['a_meca'])} formes en tout", "", ""]
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
# F. coefficients des relations (v5)
T += ["", "", "F. LES RÈGLES DES RELATIONS (v6, sans cacher) : b commun du système ; a, c et d par genre, b fixé", "=" * 90, "",
      "  (b, puis (a, c, d) ; d = la nouvelle chance ; genres de 15 formes ou plus ; un genre plus petit prend la règle générale du système)", ""]
gs = sorted({g for (s_, g) in M0["co"] if g != GEN})
def cell(M_, s_, g):
    r = M_["co"].get((s_, g))
    if r and g in ("blessure", "soin"): r = dict(r, a=0.0)
    return f"{r['b']:.2f} ({r['a']:.2f}, {r['c']:.2f}, {r.get('d', 0.0):.2f})" if r else "—"
T.append(f"  {'':30s}" + "".join(f"{s_:>22s}" for s_ in SYSTEMES))
T.append(f"  {'règle générale':30s}" + "".join(f"{cell(M0, s_, GEN):>22s}" for s_ in SYSTEMES))
for g in gs:
    T.append(f"  {g[:30]:30s}" + "".join(f"{cell(M0, s_, g):>22s}" for s_ in SYSTEMES))
# G. êtres appelés
T += ["", "", "G. ÊTRES APPELÉS (et garde), PAR SYSTÈME (D&D 5 : palier d'Inarama ; autres : propres unités) : v5 | v6", "=" * 100, "", ENTETE, SOUS]
for g in ("être appelé", "garde"):
    T.append(f"  {g}")
    for s_ in SYSTEMES:
        xs = [x for x in avec if x["systeme"] == s_ and x["a"]["genre"] == g]
        k1, k2 = ("inarama_c", "inarama") if s_ == "D&D 5" else ("propre_c", "propre")
        if xs: T.append(f"    {s_:20s}{deux(xs, k1, k2)}")
    if g == "être appelé":
        for lab, fn in (("pleine", lambda x: x["etre_plein"]), ("chiffrée", lambda x: not x["etre_plein"])):
            T.append(f"  être appelé, puissance {lab}")
            for s_ in SYSTEMES:
                xs = [x for x in avec if x["systeme"] == s_ and x["a"]["genre"] == g and fn(x)]
                k1, k2 = ("inarama_c", "inarama") if s_ == "D&D 5" else ("propre_c", "propre")
                if xs: T.append(f"    {s_:20s}{deux(xs, k1, k2)}")
T += ["", "  Les formes d'êtres appelés qui bougent le plus (palier d'Inarama, sort caché, v5 → v6) :", ""]
mv = []
for x in avec:
    if x["a"]["genre"] != "être appelé": continue
    r = V5.get((x["cle"], x["jeu"], x["forme"]))
    if r and "inarama_sort_cache" in r: mv.append((x["inarama_c"][1] - r["inarama_sort_cache"]["palier"], x, r))
for dlt, x, r in sorted(mv, key=lambda t: (-abs(t[0]), t[1]["sort"]))[:20]:
    T.append(f"  {x['sort']} ({x['jeu']}) « {x['forme']} » : niveau {x['niveau']} ; palier {r['inarama_sort_cache']['palier']} → {x['inarama_c'][1]} ({dlt:+d})")
# H. puissance « pleine »
PLEINS = sorted({e["cercle"] for x in F for e in x["a"]["effets"] if e["sans_prix"] and e["cercle"][2][:1] == ("PUISSANCE",)}, key=lambda u: ident(u) or "")
T += ["", "", "H. LES CERCLES D'ÊTRES APPELÉS À PUISSANCE « PLEINE » (effets uniques)", "=" * 70, "",
      f"  {len(PLEINS)} cercles. Pour chacun : prix propres par système (sans cacher ; nombre de formes où il est le seul effet d'Impact),",
      "  prix d'Inarama et sa source ; puis chaque forme qui le porte : niveau source, palier d'Inarama v5 → v6, sort caché puis sans cacher",
      "  (* = forme où il est le seul effet d'Impact).", ""]
sans_seul = []
for u in PLEINS:
    sats = "; ".join(json.dumps(json.loads(s_)[:3], ensure_ascii=False) for s_ in u[3]) or "aucun"
    pr = " ; ".join(f"{s_} {M0['pm'][(u, s_)]:.2f} ({M0['pn'][(u, s_)]})" for s_ in SYSTEMES if (u, s_) in M0["pm"]) or "aucun"
    ia = f"{M0['inar'][u]:.2f} ({M0['src'][u]})" if u in M0["inar"] else "aucun : 3,0 gardé (aucune forme où il est le seul effet d'Impact), non tranché"
    if u not in M0["inar"]: sans_seul.append(u)
    T += [f"  {ident(u) or '?'} — mots {' · '.join(u[2]).lower()} ; satellites {sats}", f"      prix propres : {pr}", f"      prix d'Inarama : {ia}"]
    for x in sorted((x for x in F if any(e["cercle"] == u for e in x["a"]["effets"])), key=lambda x: (SYSTEMES.index(x["systeme"]), x["sort"], x["forme"])):
        r = V5.get((x["cle"], x["jeu"], x["forme"]))
        T.append(f"      {x['systeme']:6s} {x['sort']} ({x['jeu']}) « {x['forme']} »{' *' if x['unique'] == u else ''} : niveau {x['niveau']} ; "
                 f"sort caché {r['inarama_sort_cache']['palier'] if r else '—'} → {x['inarama_c'][1]} (coût {x['inarama_c'][0]:.2f}) ; "
                 f"sans cacher {r['inarama_sans_cacher']['palier'] if r else '—'} → {x['inarama'][1]} (coût {x['inarama'][0]:.2f})")
    T.append("")
T.append(f"  Cercles sans aucune forme où ils sont le seul effet d'Impact (3,0 gardé, non tranché) : {len(sans_seul)}"
         + (" : " + ", ".join(ident(u) or "?" for u in sans_seul) if sans_seul else "."))
T += ["", "", "I. LES TROIS SORTS ÉQUILIBRÉS AUTREMENT, ET INVOCATION D'ÊTRE ASTRAL (palier d'Inarama, sort caché)", "=" * 95, "",
      "  Conseil des rêves : " + ("les formes PF1 et PF2 portent LE MÊME cercle d'Impact (" + ", ".join(sorted(ident(u) or "?" for u in set.intersection(*CONSEIL.values()))) +
                                 ") : lacune d'écriture, cercle laissé comme en v3 et v4." if CONSEIL_MEME else "deux cercles distincts, chacun réglé sur son niveau (PF1 6, PF2 8)."), ""]
for c in ("control-water", "aura-of-the-unremarkable", "dream-council", "conjure-celestial"):
    for x in par_cle[c]:
        if x["a"]["sans_impact"]: continue
        T += detail(x, "inarama_c")
T += ["", "", "J. REMPART : CHAQUE FORME", "=" * 25, "", "  (palier d'Inarama sort caché ; palier dans son système sort caché ; niveau source)", ""]
for x in sorted(avec, key=lambda x: (SYSTEMES.index(x["systeme"]), x["sort"])):
    mots = {w for e in x["a"]["effets"] for w in e["cercle"][2]}
    if mots & {"REMPART"}:
        T.append(f"  {x['systeme']:6s} {x['sort']} ({x['jeu']}) « {x['forme']} » [rempart] : "
                 f"niveau {x['niveau']} ; Inarama {x['inarama_c'][1]} ({x['inarama_c'][0]:.2f}) ; système {x['propre_c'][1]} ({x['propre_c'][0]:.2f})")
T += ["", "", "K. CAS DE CONTRÔLE : THAUMATURGIE, LUMIÈRE, PRESTIDIGITATION (v6 ; D&D 5, palier d'Inarama, sort caché)", "=" * 96, ""]
for c in ("thaumaturgy", "light", "prestidigitation"):
    for x in par_cle[c]:
        if x["systeme"] == "D&D 5": T += detail(x, "inarama_c")
th = [x for x in par_cle["thaumaturgy"] if x["systeme"] == "D&D 5" and "hybride" not in x["forme"].lower()]
if len(th) >= 3:
    cos = lambda x: sum(d["prix"] for d in x["a"]["detail"] if d["cercle"] == "COSMETIQUE")
    trois = th[0]["inarama_c"][0] + cos(th[1]) + cos(th[2])
    T += ["", f"  Thaumaturgie avec trois effets actifs à la fois (« {th[0]['forme']} » + les Cosmétiques de « {th[1]['forme']} » et « {th[2]['forme']} ») : "
              f"coût {trois:.2f}, palier {int(min(10, max(0, math.floor(trois + 0.5))))}."]
c0 = [x["inarama_c"][0] for x in dnd if x["niveau"] == 0]; c0b = [x["inarama"][0] for x in dnd if x["niveau"] == 0]
T += [f"  Coût médian des tours de magie de D&D 5 : {statistics.median(c0):.2f} (sort caché) ; {statistics.median(c0b):.2f} (sans cacher) ; {len(c0)} formes.", ""]
T += ["", "L. COÛT MÉDIAN PAR NIVEAU SOURCE, PAR SYSTÈME (v6 ; coût d'Inarama, sort caché)", "=" * 72, ""]
T.append(f"  {'niveau':8s}" + "".join(f"{s:>12s}" for s in SYSTEMES))
for n in range(0, 11):
    cells = []
    for s in SYSTEMES:
        v = [x["inarama_c"][0] for x in avec if x["systeme"] == s and x["niveau"] == n]
        cells.append(f"{statistics.median(v):6.2f} ({len(v)})" if v else "—")
    T.append(f"  {n:<8d}" + "".join(f"{c:>12s}" for c in cells))

# ---------------------------------------------------------------- v6 : les trois prix réglés, les états avec et sans nouvelle chance
def f2(v): return "—" if v is None else f"{v:.2f}"
T += ["", "", "M. LES MÉCANIQUES DES BONUS (v6, sans cacher) : prix = a × degré ; avantage, désavantage, relance : un prix fixe", "=" * 100, "",
      "  Par système : la valeur réglée (formes où la mécanique est le seul effet d'Impact) ; « * » = moins de 15 formes dans le système,",
      "  la règle des autres systèmes ensemble. Inarama = D&D 5. Conversion = D&D 5 ÷ système (pente) ou D&D 5 − système (prix fixe).",
      "  Repère : l'échelle provisoire des facultés de la v5 (prix_degre « facultés » : degré 1, 2, 3, 5).", ""]
T.append(f"  {'mécanique':18s}" + "".join(f"{s_:>22s}" for s_ in SYSTEMES) + f"{'conversion 3.5 / PF1 / PF2':>34s}")
for m_ in MECAS_TOUTES:
    vals = {s_: M0["mec"].get((m_, s_)) for s_ in SYSTEMES}
    if not any(vals.values()): continue
    cells = []
    for s_ in SYSTEMES:
        v_ = vals[s_]
        cells.append("—" if not v_ else f"{f2(v_[0])}{'*' if v_[2] != 'propre' else ''} ({v_[1]})")
    fixe = m_ in ("avantage", "désavantage", "relance", "relance au pire")
    conv_ = []
    for s_ in AUTRES:
        a_, b_ = vals["D&D 5"], vals[s_]
        if not a_ or not b_ or a_[0] is None or b_[0] is None: conv_.append("—")
        else: conv_.append(f"{a_[0] - b_[0]:+.2f}" if fixe else (f"×{a_[0] / b_[0]:.2f}" if b_[0] else "—"))
    T.append(f"  {m_:18s}" + "".join(f"{c:>22s}" for c in cells) + f"{' / '.join(conv_):>34s}")
T += ["", "  Échelle des facultés de la v5, pour comparer : " + " ; ".join(f"degré {d_} → {B.prix_degre('facultés', d_):.2f}" for d_ in (1, 2, 3, 5)), ""]
T.append("  Les formes à mécanique, par système (sort caché ; D&D 5 : palier d'Inarama ; autres : propres unités) : v5 | v6")
T += [ENTETE, SOUS]
for m_ in MECAS_TOUTES:
    for s_ in SYSTEMES:
        xs = [x for x in avec if x["systeme"] == s_ and any(e.get("meca") == m_ for e in x["a"]["effets"])]
        k1, k2 = ("inarama_c", "inarama") if s_ == "D&D 5" else ("propre_c", "propre")
        if xs: T.append(f"    {(m_ + ' ' + s_)[:20]:20s}{deux(xs, k1, k2)}")

T += ["", "", "N. LES FIGURES À PART (v6, sans cacher) : a_fig × log2(taille écrite), par figure et par système", "=" * 90, "",
      "  Chaque figure pour elle-même (aucun regroupement). D&D 5 prend la règle de 3.5 + PF1 + PF2 (comme les cibles) ; « * » = moins",
      "  de 15 formes dans le système : la règle des autres systèmes ensemble. Taille écrite : m³, m² ou m (Ampleur, ou satellite d'Ampleur).",
      "  Référence : la même pente réglée sur les zones du tableau (sphère, cube, cône, ligne, cylindre), avec son erreur type.", ""]
T.append(f"  {'figure':16s}{'formes':>8s}" + "".join(f"{s_:>18s}" for s_ in SYSTEMES))
nfig = collections.Counter(x["fig_nom"] for x in F if x["fig_nom"])
sans_taille = collections.Counter(x["fig_nom"] for x in F if x["fig_nom"] and x["fig"] is None)
for fg in FIGS:
    if not nfig.get(fg): continue
    cells = []
    for s_ in SYSTEMES:
        v_ = M0["fig"].get((fg, s_))
        cells.append("—" if not v_ else f"{f2(v_[0])}{'*' if v_[2] != 'propre' else ''} ({v_[1]})")
    T.append(f"  {fg:16s}{nfig[fg]:8d}" + "".join(f"{c:>18s}" for c in cells) + (f"   ({sans_taille[fg]} sans taille lisible)" if sans_taille.get(fg) else ""))
# référence : les zones du tableau
def reste0(x, s_):
    r = M0["regle"](s_, x["groupe"]); return x["y"] - (r["b"] * x["v"][1] - r["c"] * x["v"][2] - r.get("d", 0.0) * x["v"][3])
def pente_err(pts):
    a_ = pente(pts)
    if a_ is None or len(pts) < 3: return a_, None
    den = sum(u * u for u, _ in pts); res = sum((y - a_ * u) ** 2 for u, y in pts) / (len(pts) - 1)
    return a_, (res / den) ** 0.5
T += ["", "  Zones du tableau (référence, même méthode, toutes formes payées hors mécaniques) :"]
REF = {}
for nom in ("sphère", "cube", "cône", "ligne", "cylindre"):
    pts = [(x["zone_std"][1], reste0(x, x["systeme"])) for x in F if x["zone_std"] and x["zone_std"][0] == nom and x["paye"] and not x["a_meca"] and x["systeme"] in AUTRES]
    a_, e_ = pente_err(pts); REF[nom] = (a_, e_)
    T.append(f"    {nom:12s} pente {f2(a_)} ± {f2(e_)} ({len(pts)} formes de 3.5, PF1, PF2)")
T += ["", "  Figures à part comparées (pente 3.5 + PF1 + PF2 ensemble, ± erreur type) ; « comme » = la pente d'une forme du tableau tombe",
      "  dans deux erreurs types (dit seulement, rien n'est fusionné) :"]
for fg in FIGS:
    pts = [(x["fig"][1], reste0(x, x["systeme"])) for x in F if x["fig"] and x["fig"][0] == fg and x["paye"] and not x["a_meca"] and x["systeme"] in AUTRES]
    if not pts: continue
    a_, e_ = pente_err(pts)
    comme = [nom for nom, (ar, er) in REF.items() if a_ is not None and ar is not None and e_ is not None and abs(a_ - ar) <= 2 * ((e_ or 0) ** 2 + (er or 0) ** 2) ** 0.5]
    T.append(f"    {fg:14s} pente {f2(a_)} ± {f2(e_)} ({len(pts)} formes)" + (f" ; comme : {', '.join(comme)}" if comme else " ; ne ressemble à aucune forme du tableau"))

T += ["", "", "O. LA NOUVELLE CHANCE (« fin : chaque · … · sursaut ») : un rabais réglé comme une relation (d ≤ 0)", "=" * 90, ""]
T.append(f"  {'genre':30s}" + "".join(f"{s_:>12s}" for s_ in SYSTEMES))
for g in ["(règle générale)"] + sorted({g for (s_, g) in M0["co"] if g != GEN}):
    cs = []
    for s_ in SYSTEMES:
        r = M0["co"].get((s_, GEN if g == "(règle générale)" else g))
        cs.append(f"{-r.get('d', 0.0):+.2f}" if r else "—")
    if g == "(règle générale)" or any(c not in ("—", "+0.00", "-0.00") for c in cs):
        T.append(f"  {g[:30]:30s}" + "".join(f"{c:>12s}" for c in cs))
T += ["", "  (rabais en paliers : la nouvelle chance retire ce nombre au coût ; « + » = un rabais, 0 = rien n'est payé)", ""]
nsur = collections.Counter(x["systeme"] for x in F if x["v"][3])
T.append("  Formes avec nouvelle chance : " + " ; ".join(f"{s_} {nsur[s_]}" for s_ in SYSTEMES))
# paires de D&D 5 : même état avec et sans nouvelle chance
def etat_sig(x):
    return tuple(sorted((json.dumps(e["cercle"][1]), e["cercle"][2]) for e in x["a"]["effets"] if e["genre"] == "état"))
grp = collections.defaultdict(lambda: ([], []))
for x in avec:
    if x["systeme"] != "D&D 5" or x["a"]["genre"] != "état": continue
    sg = etat_sig(x)
    if sg: grp[sg][1 if x["v"][3] else 0].append(x)
paires_ = [(sg, a_, b_) for sg, (a_, b_) in grp.items() if a_ and b_]
T += ["", f"  Paires de D&D 5 où le même état existe avec et sans nouvelle chance : {len(paires_)} états."]
if paires_:
    dn = [statistics.mean(y["niveau"] for y in a_) - statistics.mean(y["niveau"] for y in b_) for _, a_, b_ in paires_]
    T.append(f"  Écart moyen de niveau (sans − avec nouvelle chance) : {statistics.mean(dn):+.2f} (médian {statistics.median(dn):+.2f}) ; repère du guide du maître :")
    T.append("  sans nouvelle chance, au moins le niveau 6.")
    for sg, a_, b_ in sorted(paires_, key=lambda t: -len(t[1]) - len(t[2]))[:25]:
        T.append(f"    {' ; '.join(str(json.loads(v)) + ' ' + ' · '.join(w).lower() for v, w in sg)[:60]:60s} sans : "
                 + ", ".join(sorted({f'{y['sort']} ({y['niveau']})' for y in a_}))[:70] + " | avec : " + ", ".join(sorted({f'{y['sort']} ({y['niveau']})' for y in b_}))[:70])
T += ["", "  Les états, avec et sans nouvelle chance, par système (sort caché ; D&D 5 : palier d'Inarama ; autres : propres unités) : v5 | v6", ENTETE, SOUS]
for s_ in SYSTEMES:
    for lab, fn in (("avec", lambda x: x["v"][3]), ("sans", lambda x: not x["v"][3])):
        xs = [x for x in avec if x["systeme"] == s_ and x["a"]["genre"] == "état" and fn(x)]
        k1, k2 = ("inarama_c", "inarama") if s_ == "D&D 5" else ("propre_c", "propre")
        if xs: T.append(f"    {('états ' + lab + ' ' + s_)[:20]:20s}{deux(xs, k1, k2)}")

T += ["", "", "P. ÊTRES APPELÉS ET BONUS, PAR SYSTÈME (sort caché ; D&D 5 : palier d'Inarama ; autres : propres unités) : v5 | v6", "=" * 100, "", ENTETE, SOUS]
for g in ("être appelé", "bonus", "garde"):
    T.append(f"  {g}")
    for s_ in SYSTEMES:
        xs = [x for x in avec if x["systeme"] == s_ and x["a"]["genre"] == g]
        k1, k2 = ("inarama_c", "inarama") if s_ == "D&D 5" else ("propre_c", "propre")
        if xs: T.append(f"    {s_:20s}{deux(xs, k1, k2)}")
an = [x for x in avec if any(e["cercle"][2][:1] == ("ANIMATION",) for e in x["a"]["effets"])]
T += ["", f"  Animation (règle des êtres appelés) : {len(an)} formes ; sort caché, palier d'Inarama :"]
for x in sorted(an, key=lambda x: (SYSTEMES.index(x["systeme"]), x["sort"]))[:40]:
    T.append(f"    {x['systeme']:6s} {x['sort']} ({x['jeu']}) « {x['forme']} » : niveau {x['niveau']} ; palier {x['inarama_c'][1]} ({x['inarama_c'][0]:.2f})")
no = [x for x in F if x["unique"] and x["unique"][2][:1] == ("NOURRITURE",)]
T += ["", f"  Nourriture (effet unique) : {len(no)} formes où elle est le seul effet. Prix propre contre log2(personnes nourries) :"]
pts = []
for x in no:
    v_ = json.loads(x["unique"][1])
    if isinstance(v_, (int, float)) and not isinstance(v_, bool):
        r = M0["regle"](x["systeme"], x["groupe"]); pts.append((math.log2(max(v_, 1)), x["niveau"] - x["a"]["decides"] - relx(r, x), x))
        T.append(f"    {x['systeme']:6s} {x['sort']} ({x['jeu']}) : {v_} personnes ; niveau {x['niveau']} ; reste {pts[-1][1]:+.2f}")
if len(pts) >= 3:
    mx = statistics.mean(p_[0] for p_ in pts); my = statistics.mean(p_[1] for p_ in pts)
    sxx = sum((p_[0] - mx) ** 2 for p_ in pts); sxy = sum((p_[0] - mx) * (p_[1] - my) for p_ in pts)
    syy = sum((p_[1] - my) ** 2 for p_ in pts)
    pen = sxy / sxx if sxx else 0; rr = (sxy / (sxx * syy) ** 0.5) if sxx and syy else 0
    T.append(f"  Pente du reste sur log2(personnes) : {pen:+.2f} ; corrélation {rr:+.2f} sur {len(pts)} formes "
             + ("(une relation au nombre apparaît)" if abs(rr) >= 0.5 and len(pts) >= 10 else "(pas de relation prouvée : la nourriture reste un effet unique)"))

open(os.path.join(OUT, "mesure_bareme_cercles_v6.txt"), "w", encoding="utf-8").write("\n".join(T) + "\n")
json.dump({f"{c}|{j}": v for (c, j), v in MULTI.items() if v}, open(os.path.join(OUT, "niveaux_multi_v6.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)

# ---------------------------------------------------------------- fichiers
PRIX = []
for u in sorted({u for (u, s) in M0["pm"]}, key=lambda u: ident(u) or ""):
    par = {s: dict(prix=round(M0["pm"][(u, s)], 3), formes=M0["pn"][(u, s)], converti=round(M0["pm"][(u, s)] + M0["conv"][s], 3)) for s in SYSTEMES if (u, s) in M0["pm"]}
    PRIX.append(dict(id=ident(u), type=u[0], valeur=json.loads(u[1]), mots=list(u[2]), satellites=[json.loads(s) for s in u[3]], par_systeme=par,
                     prix_inarama=round(M0["inar"][u], 3), source=M0["src"][u]))
json.dump(dict(_lisez_moi="Prix propres des cercles d'Impact sans prix (effets uniques), identifiés comme au répertoire (satellites compris). "
                          "par_systeme : prix propre médian dans le système (niveau − prix décidés − relations du système, sur les formes où le "
                          "cercle est le seul effet d'Impact), nombre de formes, prix converti (+ conversion du système). prix_inarama : le prix "
                          "en D&D 5 s'il existe, sinon le médian des prix convertis. Version 6 (glyphes corrigés m128 ; mécaniques des bonus en a × degré, figures à part, nouvelle chance) ; clés mecaniques et figures : les prix réglés par système. Calcul sans cacher (sur toute la bibliothèque).",
               conversion=M0["conv"], regles={f"{s}|{g}": v for (s, g), v in M0["co"].items()},
               mecaniques={f"{m}|{s}": dict(valeur=v[0], formes_du_systeme=v[1], source=v[2], formes_du_reglage=v[3]) for (m, s), v in M0["mec"].items()},
               figures={f"{f}|{s}": dict(pente=v[0], formes_du_systeme=v[1], source=v[2], formes_du_reglage=v[3]) for (f, s), v in M0["fig"].items()},
               cercles=PRIX), open(os.path.join(OUT, "prix_cercles_v6.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
def fiche(x):
    out = dict(cle=x["cle"], sort=x["sort"], jeu=x["jeu"], systeme=x["systeme"], forme=x["forme"], niveau=x["niveau"], genre=x["a"]["genre"], groupe=x["groupe"],
               mesures=x["a"]["mesures"], lacunes=x["a"]["lacunes"], prix_decides=x["a"]["decides"], detail=x["a"]["detail"])
    for k, nom in (("inarama_c", "inarama_sort_cache"), ("inarama", "inarama_sans_cacher"), ("propre_c", "systeme_sort_cache"), ("propre", "systeme_sans_cacher")):
        if k in x:
            c, p, rel, prix, r = x[k]
            out[nom] = dict(cout=c, palier=p, relations=rel, regle=r, effets=[dict(cercle=ident(e["cercle"]), prix=round(pp, 3), regle=why) for (pp, why), e in zip(prix, x["a"]["effets"])])
    return out
json.dump(dict(_lisez_moi="Version 6 (glyphes corrigés m128 ; mécaniques des bonus, nouvelle chance, figures à part). Pour chaque forme (hors Elden Ring) : palier d'Inarama (prix d'Inarama, règles de D&D 5) et palier dans son système "
                          "(règles et prix propres du système), chacun « sort caché » et « sans cacher » ; le détail cercle par cercle avec la "
                          "règle ; les mesures lues sur le glyphe.", formes=[fiche(x) for x in F]),
          open(os.path.join(OUT, "couts_formes_cercles_v6.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=str)
json.dump(dict(conv=M0["conv"], causeA=len(causeA), viol=len(viol), tot=tot, loin=len(loin), prix=len(PRIX),
               sans_inar=sum(1 for x in avec for e in x["a"]["effets"] if e["sans_prix"] and e["cercle"] not in M0["inar"]),
               regles={f"{s}|{g}": v for (s, g), v in M0["co"].items()}),
          open(os.path.join(OUT, "comptes_v6.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("D&D 5 caché :", st(dnd, "inarama_c"), "| sans cacher :", st(dnd, "inarama"), "| conversion", {k: round(v, 2) for k, v in M0["conv"].items()})
