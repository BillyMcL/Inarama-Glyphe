"""Formes combinées (B12) : le dessin à plusieurs Noyaux. ESSAI (22 novembre 2026) : aucune construction du site n'appelle
ce module ; il ne change le dessin d'aucun glyphe existant. Il se lance seul :
    python moteur/combinees.py <dossier de sortie>        → page d'essai (index.html, style.css) et pages d'image

Une forme combinée : plusieurs Noyaux hybrides (un par combinaison), lancés en même temps. École, hémisphère et pôle sont
communs. Les cercles gardent l'ordre habituel (1 École … 12 Cosmétique) ; chacun est soit commun (autour du centre du
glyphe), soit propre à un Noyau (autour de ce Noyau). Second essai : le cercle d'École, premier cercle commun, relie les
Noyaux (il passe par leurs centres, répartis également) ; tous les autres cercles communs (Cible … Cosmétique) sont à
l'extérieur. Lecture : d'abord les Noyaux (simultanés), puis les cercles communs, du centre vers l'extérieur."""
import os, sys, json, math, re, html
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, D)
import convert as C, spells as SP, gen_glyphs as GG, combos as KB, corrections as K, fautes as FT, formes_mots as FM
import phase4b as P

B12 = os.path.join(D, "..", "donnees", "phase4b", "B12_formes_combinees.json")
RANG = {"ECOLE": 1, "CIBLE": 2, "FORME": 3, "AMPLEUR": 4, "DUREE": 5, "LOCALISATION": 6, "CONDITION": 7, "IMPACT": 8,
        "QUANTITE": 9, "COMPOSANTE": 10, "INTERACTION": 11, "COSMETIQUE": 12}

# ---------- choix de dessin de l'essai (à juger sur l'essai) ----------
R_NOYAU = 50        # rayon du Noyau hybride sans encart d'école : ses quatre sous-cercles ont la taille de ceux d'aujourd'hui (66 − 16)
MARGE = 14          # écart minimal entre deux Noyaux voisins (cercles propres et satellites compris)
ANGLES = {1: [90], 2: [180, 0], 3: [90, 210, 330], 4: [135, 225, 315, 45]}     # 2 : ouest puis est ; 4 : en carré, sur les diagonales

FAITS = []          # ce que l'essai a dû interpréter : (sort, forme, cercle, ce qui a été fait)


# ---------- les cercles : données B12 → cercles du moteur ----------
def _sat(txt, par):
    """satellite de B12 → satellite du moteur. « N| » : une proportion de la Forme ; « sym:x » : un symbole ;
    « forme:x » : un satellite de Forme de la primitive x (comme convert._sat_forme) ; « N|CRITÈRE MOTS » : comme B7 à B11."""
    if txt.startswith("sym:"): return ("SYM", ("sym", txt[4:]), "")
    if txt.startswith("forme:"):
        sil, props, nom = FM.PRIM[txt[6:]]
        return ("SYM", sil, "FORME", {"crit": "FORME", "kids": list(props), "nom": nom})
    v, t = txt.split("|", 1)
    v = "plein" if v == "plein" else int(v) if v else None
    if not t.strip(): return ("SYM", v)
    return P._sat_b7(txt)


def cercle(c, niveau, ref, ou):
    """un cercle de B12 → (critère, valeur, mots, lecture, satellites), lecture écrite comme le moteur"""
    crit, v, par = c["cercle"], c["valeur"], c["parenthese"]
    ws = [C.word(w) for w in c["mots"]]
    sats = [_sat(s, par) for s in c["satellites"]]
    prim = c.get("primitive")
    if crit == "FORME" and prim:
        sil, props, nom = FM.PRIM[prim]
        if sil != v: raise ValueError(f"Forme {v} ≠ silhouette de {prim}")
        prop = [s for s in sats if len(s) == 2]
        if [s[1] for s in prop] != list(props):
            FAITS.append((*ou, "FORME", f"{nom} : proportions {[s[1] for s in prop]} dans B12, {props} pour la primitive du moteur — celles du moteur"))
            sats = [("SYM", p) for p in props] + [s for s in sats if len(s) != 2]
    tourbillon = crit == "FORME" and any(len(s) > 3 and s[3].get("crit") == "AMPLEUR" for s in sats)
    forme_sats = [s for s in sats if len(s) > 3 and s[3].get("kids")]
    sats = [(s[0], s[1], s[2], {k: w for k, w in s[3].items() if k != "nom"}) if len(s) > 3 else s for s in sats]
    if tourbillon:      # règle du tourbillon (convert.formes_mots) : proportions à l'ouest et à l'est, l'Ampleur au sud
        prop, amp = [s for s in sats if len(s) == 2], [s for s in sats if len(s) > 3]
        sats = [(a, s[1]) for a, s in zip((180, 0), prop)] + [(270, *s[1:]) for s in amp]
    else:
        sats = C._resats(sats) if sats else []
    if any(C.est_symbole(s[1]) for s in sats):
        p_ = C.placer_symboles(sats)
        if p_: sats = p_
    # la phrase : début régénéré, parenthèse de B12, puis les satellites
    for s in forme_sats:            # « ; satellite Forme : hélice » : le moteur l'écrit lui-même après la parenthèse
        fin = f" ; satellite Forme : {s[3]['nom'].split(' :')[0]}"
        if par.endswith(fin):
            par = par[:-len(fin)]
            FAITS.append((*ou, crit, f"parenthèse : « {fin[3:]} » retiré (le moteur l'écrit après la parenthèse)"))
    with K._Accentue():
        if crit == "FORME":
            nom = FM.PRIM[prim][2] if prim else K._tete(crit, v, ws)
            tete, par_ = (nom, "") if nom.startswith(par) else (par, "") if par.startswith(nom.split(" (")[0]) else (nom, f" ({par})" if par else "")
        elif crit == "AMPLEUR":
            tete, par_ = par, ""
            m = re.search(r"arrondi de \d+ à (\d+)$", par)
            if m and int(m.group(1)) == v:         # la formule du moteur : « … pour s'écrire en N formes »
                nf = len(SP.val(v, "up")[0])
                tete += f" pour s'écrire en {nf} formes"
                FAITS.append((*ou, crit, f"« {m.group(0)} » complété par la formule du moteur : « pour s'écrire en {nf} formes »"))
        elif crit == "IMPACT" and not ws:      # forme combinée : pas de verbe, l'énergie est dite par le Noyau
            tete, par_ = ("plein" if v == "plein" else f"intensité {v}"), (f" ({par})" if par else "")
        elif crit == "LOCALISATION":
            tete, par_ = (f"{v} m" if ws == ["METRES"] else f"{v} km" if ws == ["KILOMETRES"] else K._tete(crit, v, ws)), (f" ({par})" if par else "")
        elif crit == "INTERACTION":
            tete, par_ = (f"{v} : sort de niveau {v - 1}" if v != 1 else "1 : tour de magie"), (f" ({par})" if par else "")
            if v != niveau + 1: FAITS.append((*ou, crit, f"Interaction {v} pour un sort de niveau {niveau}"))
        elif crit == "COSMETIQUE":
            r0 = next((r for r in ref if r[0] == crit and r[1] == v and list(r[2]) == ws), None)
            if r0 is None: raise ValueError(f"Cosmétique {v} {ws} : sens inconnus")
            tete, par_ = r0[3].split(" ; satellite")[0], (f" ({par})" if par else "")
        else:
            tete, par_ = K._tete(crit, v, ws), (f" ({par})" if par else "")
        autres = [s for s in sats if not (len(s) > 3 and s[3].get("kids"))]
        if crit == "FORME": autres = []        # proportions et Ampleur du tourbillon : la phrase de la Forme les dit
        rd = tete + par_ + K._lecture_sats(autres, ("combinee",), ws)
        rd += "".join(f" ; satellite Forme : {s[3]['nom']}" for s in forme_sats)
    return (crit, v, ws, FT.corriger(rd, False), sats)


def anneau(r, p):
    """cercle du moteur → cercle du dessin (comme spells.build) ; renvoie (cercle, polarité lisible ?)"""
    crit, v, words, _, sats = r
    spec, mult, ok = SP.val(v, p) if v is not None else ([], False, False)
    svals = [(d, SP.val(sv, p), SP.sat_label(sv, x, p), SP.sat_opts(x, p)) for d, sv, *x in sats]
    mult = mult or any(m for _, (_, m, _), _, o_ in svals if not o_.get("crit"))
    ok = ok or any(o for _, (_, _, o), _, _ in svals)
    words = list(words) + (["FOIS"] if mult else [])
    return dict(label=" ".join([crit] + words), spec=spec, sats=[(d, sp, lab, o) for d, (sp, _, _), lab, o in svals]), ok


# ---------- une forme combinée ----------
def forme(s, f, niveau, ref):
    """s : le sort (B12), f : la forme combinée ; ref : les cercles de la forme d'Arcane de main (pour les sens de la Cosmétique)"""
    nc = s["noyau_commun"]; ecole, hemi, pole = nc["ecole"], nc["hemisphere"], nc["pole"]
    ou = (s["sort"], f["nom"])
    communs = [cercle(c, niveau, ref, ou) for c in f["communs"]]
    noyaux = [(n["combinaison"], [cercle(c, niveau, ref, ou + (n["combinaison"],)) for c in n["cercles"]]) for n in f["noyaux"]]
    for x in [communs] + [r for _, r in noyaux]:
        rg = [RANG[r[0]] for r in x]
        if rg != sorted(rg): raise ValueError(f"cercles hors d'ordre : {[r[0] for r in x]}")
    crits = []
    for r in sorted(communs + [r for _, rs in noyaux for r in rs], key=lambda r: RANG[r[0]]):
        if r[0] not in crits: crits.append(r[0])
    n_imp = sum(1 for r in communs if r[0] == "IMPACT") + sum(1 for _, rs in noyaux for r in rs if r[0] == "IMPACT")
    split, _ = P.split_poles(crits, hemi[0], niveau, [pole] * n_imp)
    pol = "up" if hemi == "Hodolin" else "down"
    def p_of(crit):
        if crit == "IMPACT": return "up" if pole == "lumineux" else "down"
        return "up" if crit in split[0] else "down"
    undet = []
    def des(rs):
        out = []
        for r in rs:
            a, ok = anneau(r, p_of(r[0]))
            if not ok: undet.append(r[0])
            out.append(a)
        return out
    g_com = des(communs)
    g_noy = [(comb, SP.hyb(*KB.COMBOS[comb]), des(rs)) for comb, rs in noyaux]
    part = ([c for c in split[0] if c in undet], [c for c in split[1] if c in undet])
    lab_ecole = C.word(C.norm(ecole)); C.word("ECOLE")
    dec = dessin(lab_ecole, g_com, g_noy, True)
    epu = dessin(lab_ecole, g_com, g_noy, False)
    svg = (SP.compose(dec, split, always=True), SP.compose(epu, part, always=False))
    verb = f"{ecole} · {hemi} · " + " + ".join(f"{comb} ({KB.code(comb)})" for comb, _ in noyaux)
    # lecture : d'abord les Noyaux (simultanés ; chacun ses cercles dans l'ordre), puis les cercles communs, du centre vers l'extérieur
    rows = []
    for comb, rs in noyaux:
        rows += [(str(RANG[r[0]]), SP.NAMES[r[0]][1], f"Noyau {comb}", r[3]) for r in rs]
    rows.append(("1", "École", "commun (relie les Noyaux)", ecole))
    rows += [(str(RANG[r[0]]), SP.NAMES[r[0]][1], "commun", r[3]) for r in communs]
    return dict(sort=s["sort"], cle=s["cle"], jeu=s["jeu"], label=f["nom"], verb=verb, svg=svg, rows=rows, split=split,
                niveau=niveau, communs=communs, noyaux=noyaux)


# ---------- le dessin ----------
def _rayon_max(rings, geo):
    """rayon atteint par une pile de cercles, satellites compris"""
    R = geo[-1][1] if geo else 0
    for ring, (rin, rout) in zip(rings, geo):
        for deg, spec, *x in ring.get("sats", []):
            lab, opts = GG.sat_parts(x)
            R = max(R, (rin + rout) / 2 + GG.sat_radius(spec, opts) + (GG.SBAND if lab else 0) + GG.kid_reach(opts))
    return R


def _poser(rings, geo, centres, Rn):
    """satellites « NS » / « SYM » d'un cercle commun : même règle que le moteur (un : nord ou sud ; deux : nord-sud ou
    ouest-est ; trois et plus, également depuis le nord) ; on garde la disposition qui ne touche pas les Noyaux (à défaut,
    celle qui les touche le moins)."""
    out = []
    for ring, (rin, rout) in zip(rings, geo):
        src = list(ring.get("sats", []))
        mid = (rin + rout) / 2
        def gene(d, sp, x):
            cx, cy = GG.pt(mid, d); lab, o = GG.sat_parts(x)
            rs = GG.sat_radius(sp, o) + (GG.SBAND if lab else 0) + GG.kid_reach(o)
            return sum(max(0, Rn + rs + 3 - math.hypot(cx - nx, cy - ny)) for nx, ny in centres)
        sym = [j for j, s_ in enumerate(src) if s_[0] in ("SYM", "NS")]
        if sym:
            n = len(sym)
            cands = [[90], [270]] if n == 1 else [[90, 270], [180, 0]] if n == 2 else [[(90 + k * 360 / n) % 360 for k in range(n)]]
            best = min(cands, key=lambda c: sum(gene(d, src[j][1], src[j][2:]) for d, j in zip(c, sym)))
            for d, j in zip(best, sym): src[j] = (d, *src[j][1:])
        out.append(dict(ring, sats=src))
    return out


def _cercles(rings, geo, declared, evite=()):
    """cercles concentriques autour du centre (comme gen_glyphs._glyph) : du plus extérieur au plus intérieur"""
    parts = []
    for ring, (rin, rout) in reversed(list(zip(rings, geo))):
        parts.append(f'<circle r="{GG.f(rout)}" class="paper-f"/>')
        parts.append(GG.value(rin, ring["spec"]))
        words = ring["label"].replace("·", " ").split()
        text = " ".join(words if declared or ring.get("garde") else words[1:])
        if rout > rin: parts.append(f'<circle r="{GG.f(rin)}" class="ink-s"/><circle r="{GG.f(rout)}" class="ink-s"/>')
        else: parts.append(f'<circle r="{GG.f(rin)}" class="ink-s"/>')
        parts.append(GG.label_alde(rin, rout, text, [s[0] for s in ring.get("sats", [])] + list(ring.get("evite", ()))))
    return parts


def _sats(rings, geo):
    parts = []
    for ring, (rin, rout) in zip(rings, geo):
        for deg, spec, *x in ring.get("sats", []):
            lab, opts = GG.sat_parts(x)
            sx, sy = GG.pt((rin + rout) / 2, deg)
            parts.append(GG.draw_sat(sx, sy, GG.sat_radius(spec, opts), spec, lab, opts, deg))
    return parts


def _has_text(declared):
    def h(ring):
        w = ring["label"].replace("·", " ").split()
        return len(w if declared or ring.get("garde") else w[1:]) > 0
    return h


def dessin(lab_ecole, g_com, g_noy, declared):
    """le glyphe combiné, sans ses satellites astraux"""
    n = len(g_noy)
    # 1. les piles des Noyaux : chacune dessinée par le moteur, comme un glyphe hybride sans encart d'école
    piles = []
    for comb, core, rings in g_noy:
        rings = GG.resolve_ns(rings, R_NOYAU)
        GG.R0 = R_NOYAU
        geo = GG.ring_geo(rings, R_NOYAU, None, _has_text(declared))
        svg = GG._glyph(core, rings, r0=R_NOYAU, declared=declared)
        inner = re.sub(r'^<svg[^>]*>', '', svg)[:-6]
        piles.append((inner, max(R_NOYAU, _rayon_max(rings, geo))))
    Rn = max(r for _, r in piles)
    # 2. le cercle d'École : il passe par le centre des Noyaux, répartis également ; sans valeur
    #    (déclarée : « école · évocation » ; non déclarée : « évocation », comme les autres cercles)
    s_ = math.sin(math.pi / n) if n > 1 else 1
    Dr = (Rn + MARGE / 2) / s_
    centres = [GG.pt(Dr, a) for a in ANGLES[n]]
    ecole = dict(label=f"ECOLE {lab_ecole}", spec=[], sats=[], evite=ANGLES[n])
    geo_c = [(Dr, Dr + GG.BAND)]
    # 3. tous les autres cercles communs, à l'extérieur, au-delà des Noyaux, dans l'ordre habituel
    geo_e = GG.ring_geo(g_com, Dr + Rn, GG.GAP, _has_text(declared)) if g_com else []
    exterieurs = _poser(g_com, geo_e, centres, Rn)
    parts = _cercles(exterieurs, geo_e, declared) + _cercles([ecole], geo_c, declared)
    for (inner, _), (cx, cy) in zip(piles, centres):
        parts.append(f'<g transform="translate({GG.f(cx)},{GG.f(cy)})">{inner}</g>')
    parts += _sats(exterieurs, geo_e)
    R = max([Dr + Rn, _rayon_max(exterieurs, geo_e) if g_com else 0]) + 24
    return f'<svg viewBox="{GG.f(-R)} {GG.f(-R)} {GG.f(2*R)} {GG.f(2*R)}" role="img" xmlns="http://www.w3.org/2000/svg">{"".join(parts)}</svg>'


# ---------- l'essai ----------
ESSAI = [("entropic-wheel", "Forme combinée Feu et Glace"), ("redistribute-potential", "Forme combinée Glace et Feu"),
         ("elemental-assessor", "Forme combinée Acide sulfurique, Glace, Éclair et Feu"),
         ("summon-draconic-legion", "Cône Glace, ligne Acide sulfurique"),
         ("torrent-of-elemental-rage", "Forme combinée Feu, Glace, Tempête et Acier"),
         ("elemental-confluence", "Forme combinée Foudre et Terre")]


def _main_forms(cle):
    from fiches import FICHES
    return K.appliquer(cle, C.build_forms(cle, FICHES[cle]))


def table(rows, ou=True):
    th = "<th>Rang</th><th>Critère</th>" + ("<th>Où</th>" if ou else "") + "<th>Lecture</th>"
    tr = "".join(f"<tr><td class='num'>{a}</td><td>{b}</td>" + (f"<td>{html.escape(c)}</td>" if ou else "") + f"<td>{html.escape(d)}</td></tr>"
                 for a, b, c, d in rows)
    return f"<table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>"


def pol_html(split):
    lum = ", ".join(SP.NAMES[c][1].lower() if c in SP.NAMES else "noyaux" for c in split[0]) or "aucun cercle"
    ten = ", ".join(SP.NAMES[c][1].lower() if c in SP.NAMES else "noyaux" for c in split[1]) or "aucun cercle"
    return f'<p class="pol"><span>Lumineux :</span> {lum}<br><span>Ténébreux :</span> {ten}</p>'


def _styles():
    """CSS, HEAD et FOOT du site, lus dans site.py sans l'exécuter (l'importer lancerait la construction du site)"""
    import ast, types
    t = ast.parse(open(os.path.join(D, "site.py"), encoding="utf-8").read())
    ns = {}
    for n in t.body:
        if isinstance(n, ast.Assign) and len(n.targets) == 1 and getattr(n.targets[0], "id", None) in ("CSS", "HEAD", "FOOT"):
            ns[n.targets[0].id] = ast.literal_eval(n.value)
    return types.SimpleNamespace(**ns)


def essai(out):
    ST = _styles()
    os.makedirs(out, exist_ok=True)
    data = {s["cle"]: s for s in json.load(open(B12, encoding="utf-8"))["sorts"]}
    res = []
    for cle, nom in ESSAI:
        s = data[cle]
        mf = _main_forms(cle)
        arc = next(x for x in mf if x["fam"] == "A")
        f = next(x for x in s["formes_combinees"] if x["nom"] == nom)
        res.append(forme(s, f, arc["level"], arc["rings"]))
    fb = next(x for x in _main_forms("fireball") if x["fam"] == "H")
    open(os.path.join(out, "style.css"), "w", encoding="utf-8").write(ST.CSS + """
.essai figure.grand svg { max-height:none; }
.essai .note { font-size:.92rem; color:var(--muted); max-width:90ch; }
""")
    arts = []
    for i, r in enumerate(res, 1):
        arts.append(f"""<article class="forme" id="g{i}"><header class="fh"><div class="eyebrow">{i}. {html.escape(r['sort'])} · {r['jeu']} · niveau {r['niveau']}</div>
<h2>{html.escape(r['label'])}</h2><p class="lede">{html.escape(r['verb'])}</p></header>
<section class="sec"><h3>Glyphe circulaire</h3><div class="pair one"><figure class="grand">{r['svg'][0]}<figcaption>Déclarée · tous les cercles classés</figcaption></figure>
<figure class="grand">{r['svg'][1]}<figcaption>Non déclarée · seuls les cercles à polarité illisible</figcaption></figure></div>{pol_html(r['split'])}</section>
<section class="sec"><h3>Lecture</h3>{table(r['rows'])}</section></article>""")
    fbrows = [(a, b, "", c) for a, b, c in [("1", "Noyau", fb["verb"])] + fb["rows"]]
    arts.append(f"""<article class="forme" id="gc"><header class="fh"><div class="eyebrow">Pour comparaison · telle qu'elle est sur main</div>
<h2>{html.escape(fb['fr'])} (5e) — {html.escape(fb['label'])}</h2><p class="lede">{html.escape(fb['verb'])}</p></header>
<section class="sec"><h3>Glyphe circulaire</h3><div class="pair one"><figure class="grand">{fb['svg'][0]}<figcaption>Déclarée · tous les cercles classés</figcaption></figure>
<figure class="grand">{fb['svg'][1]}<figcaption>Non déclarée · seuls les cercles à polarité illisible</figcaption></figure></div>{pol_html(fb['split'])}</section>
<section class="sec"><h3>Lecture</h3>{table(fbrows, ou=False).replace("<td></td>", "")}</section></article>""")
    sommaire = "".join(f'<a class="chip" href="#g{i}">{i}. {html.escape(r["sort"])}</a>' for i, r in enumerate(res, 1)) + '<a class="chip" href="#gc">Boule de feu (main)</a>'
    page = ST.HEAD.format(title="Essai · formes combinées", root="") + f"""
<header><div class="eyebrow">Essai · chantier « combinees » · rien n'entre dans la bibliothèque</div><h1>Formes combinées : essai de dessin</h1>
<p class="lede">Second essai. Plusieurs Noyaux hybrides, un par combinaison, lancés en même temps. Le cercle d'École, premier cercle commun, passe
par le centre des Noyaux et les relie ; tous les autres cercles communs, de la Cible à la Cosmétique, sont à l'extérieur ; chaque Noyau
porte ses propres cercles autour de lui. Lecture : d'abord les Noyaux, puis les cercles communs, du centre vers l'extérieur.</p>
<div class="chips">{sommaire}</div></header>
<div class="essai">""" + "".join(arts) + "</div>" + ST.FOOT
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(page)
    # une page par glyphe, pour les images
    for i, r in enumerate(res, 1):
        open(os.path.join(out, f"_image_{i}.html"), "w", encoding="utf-8").write(
            '<!doctype html><html data-theme="light"><head><meta charset="utf-8"><link rel="stylesheet" href="style.css"><style>html,body{margin:0;background:var(--paper)}'
            'svg{width:100vw;height:100vh;display:block}</style></head><body>' + r["svg"][0] + "</body></html>")
    return res, fb


if __name__ == "__main__":
    res, fb = essai(sys.argv[1])
    json.dump(dict(formes=[dict(r, svg=list(r["svg"])) for r in res], faits=FAITS, boule_de_feu=dict(svg=list(fb["svg"]))),
              open(os.path.join(sys.argv[1], "_essai.json"), "w", encoding="utf-8"), ensure_ascii=False, default=repr)
    for r in res: print(r["sort"], "|", r["label"], "|", len(r["svg"][0]), len(r["svg"][1]))
    for x in FAITS: print("  fait :", x)
