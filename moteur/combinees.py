"""Formes combinées (B12) : le dessin à plusieurs Noyaux. ESSAI (22 novembre 2026) : aucune construction du site n'appelle
ce module ; il ne change le dessin d'aucun glyphe existant. Il se lance seul :
    python moteur/combinees.py <dossier de sortie>        → page d'essai (index.html, style.css) et pages d'image

Une forme combinée : plusieurs Noyaux hybrides (un par combinaison), lancés en même temps. École, hémisphère et pôle sont
communs. Les cercles gardent l'ordre habituel (1 École … 12 Cosmétique) ; chacun est soit commun (autour du centre du
glyphe), soit propre à un Noyau (autour de ce Noyau). Le cercle d'École, premier cercle commun, relie les
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
MARGE = 4           # écart entre deux Noyaux voisins (cercles propres et satellites compris) : ils se touchent presque
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
    dec = dessin(lab_ecole, g_com, g_noy, True, f"{s['sort']} — {f['nom']}")
    epu = dessin(lab_ecole, g_com, g_noy, False, f"{s['sort']} — {f['nom']}")
    svg = (SP.compose(dec, split, always=True), SP.compose(epu, part, always=False))
    nom_f = f"{s['sort']} — {f['nom']}"
    svg_b = (bande(nom_f, lab_ecole, g_noy, communs, split, part, pole, True), bande(nom_f, lab_ecole, g_noy, communs, split, part, pole, False))
    verb = f"{ecole} · {hemi} · " + " + ".join(f"{comb} ({KB.code(comb)})" for comb, _ in noyaux)
    # lecture : d'abord les Noyaux (simultanés ; chacun ses cercles dans l'ordre), puis les cercles communs, du centre vers l'extérieur
    rows = []
    for comb, rs in noyaux:
        rows += [(str(RANG[r[0]]), SP.NAMES[r[0]][1], f"Noyau {comb}", r[3]) for r in rs]
    rows.append(("1", "École", "commun (relie les Noyaux)", ecole))
    rows += [(str(RANG[r[0]]), SP.NAMES[r[0]][1], "commun", r[3]) for r in communs]
    return dict(sort=s["sort"], cle=s["cle"], jeu=s["jeu"], label=f["nom"], verb=verb, svg=svg, bande=svg_b, rows=rows, split=split,
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


# ---------- le dessin (troisième essai) ----------
DESSIN = []         # ce que le dessin relève : (forme, version, ce qui se lit mal ou a été déplacé)
_FORME = [""]       # nom de la forme en cours (pour les relevés)


def _ang(x, y):
    return math.degrees(math.atan2(-y, x)) % 360


def _dist_ang(a, b):
    return abs((a - b + 180) % 360 - 180)


def _couverture(r, disques):
    """portions du cercle de rayon r cachées par des disques (cx, cy, R) : liste d'intervalles (centre, demi-largeur) en degrés"""
    out = []
    for cx, cy, R in disques:
        d = math.hypot(cx, cy)
        if d == 0 or abs(r - d) >= R: continue
        c = (r * r + d * d - R * R) / (2 * r * d)
        out.append((_ang(cx, cy), math.degrees(math.acos(max(-1, min(1, c))))))
    return out


def _cache(a, r, disques, marge=0.0):
    """l'angle a du cercle de rayon r est-il caché (à « marge » degrés près) ?"""
    return any(_dist_ang(a, c) <= h + marge for c, h in _couverture(r, disques))


def _part_cachee(r, disques, pas=0.5):
    n = int(360 / pas)
    return sum(1 for k in range(n) if _cache(k * pas, r, disques)) / n


def _unites(text):
    words = [GG.LEX[w] for w in text.replace("·", " ").split()]
    units = []
    for k, w in enumerate(words):
        if k: units.append(None)
        units += w
    return units


def _label(rin, rout, text, centres, ak=None):
    """annotation écrite aux centres donnés (même tracé que gen_glyphs.label_alde, emplacements imposés)"""
    ak = ak or GG.AK
    units = _unites(text)
    if not units: return ""
    rb = rin + 0.8 + 14 * ak
    step = math.degrees(GG.ALW * ak * 1.18 / rb)
    out = ""
    for cm in centres:
        center = -cm
        for i, u in enumerate(units):
            if u is None: continue
            phi = center - (len(units) - 1) / 2 * step + i * step
            x, y = rb * math.cos(math.radians(phi)), rb * math.sin(math.radians(phi))
            out += (f'<g transform="translate({GG.f(x)},{GG.f(y)}) rotate({GG.f(phi + 90)}) scale({ak}) translate({-GG.ALW/2 + 4},0) {GG.ITAL}" class="alde">'
                    f'{GG.a1_syll("ink", u[0], u[1])}</g>')
    return out


def _largeur(rin, text, ak=None):
    ak = ak or GG.AK
    rb = rin + 0.8 + 14 * ak
    return math.degrees(GG.ALW * ak * 1.18 / rb) * len(_unites(text))


def _places(rin, rout, text, sats_ang, disques, nom):
    """emplacements de l'annotation d'un cercle commun : d'abord ceux du moteur (8, 6, 4 ou 2 copies, en évitant les
    satellites) s'ils sont tous visibles ; sinon une copie au milieu de chaque portion visible assez large ; sinon, la
    plus large portion visible, et c'est relevé."""
    td = _largeur(rin, text)
    if td == 0: return []
    def libre(c):           # la copie entière est visible (aux deux parois) et ne touche pas un satellite
        for k in range(21):
            a = c - td / 2 + td * k / 20
            if _cache(a, rin, disques, 1) or _cache(a, rout, disques, 1): return False
            if any(_dist_ang(a, s) < w + 1 for s, w in sats_ang): return False
        return True
    cands = []
    if not sats_ang: cands.append([k * 45 for k in range(8)])
    else:
        opp = {(s + 180) % 360 for s, _ in sats_ang}
        six = [k * 45 for k in range(8) if all(_dist_ang(k * 45, s) > 1 for s, _ in sats_ang) and k * 45 not in opp]
        if len(six) == 6: cands.append(six)
    cands += [[45, 135, 225, 315], [0, 90, 180, 270], [90, 270], [0, 180]]
    for cs in cands:
        if all(libre(c) for c in cs) and (len(cs) < 2 or td <= 360 / len(cs) * 0.82): return cs
    # portions visibles : on parcourt le cercle par pas d'un degré
    vis = [not (_cache(a, rin, disques, 1) or _cache(a, rout, disques, 1) or any(_dist_ang(a, s) < w + 1 for s, w in sats_ang)) for a in range(360)]
    if all(vis): return [90, 270]
    k0 = vis.index(False)
    portions, cur = [], []
    for k in range(360):
        a = (k0 + k) % 360
        if vis[a]: cur.append(a)
        elif cur: portions.append(cur); cur = []
    if cur: portions.append(cur)
    ok = [p for p in portions if len(p) >= td + 2]
    if ok:
        return [(p[0] + (len(p) - 1) / 2) % 360 for p in ok][:8]
    if portions:
        p = max(portions, key=len)
        DESSIN.append((_FORME[0], nom, f"annotation « {text.lower()} » : aucune portion visible assez large ({len(p)}° pour {td:.0f}°) ; écrite au milieu de la plus large, en partie cachée"))
        return [(p[0] + (len(p) - 1) / 2) % 360]
    DESSIN.append((_FORME[0], nom, f"annotation « {text.lower()} » : cercle entièrement caché ; annotation au nord, cachée"))
    return [90]


def _sat_disque(mid, d, sp, x):
    cx, cy = GG.pt(mid, d); lab, o = GG.sat_parts(x)
    return cx, cy, GG.sat_radius(sp, o) + (GG.SBAND if lab else 0) + GG.kid_reach(o)


def _poser(rings, geo, disques, declared):
    """satellites d'un cercle commun : la disposition du moteur (un : nord ou sud ; deux : nord-sud ou ouest-est ; trois et
    plus, également depuis le nord ; ou les angles fixés par une règle) ; si elle touche un Noyau, tout le groupe tourne
    le long du cercle, du plus petit angle qui le rend visible (symétrie gardée). Sinon, l'angle qui touche le moins."""
    out = []
    for ring, (rin, rout) in zip(rings, geo):
        src = list(ring.get("sats", []))
        mid = (rin + rout) / 2
        if not src: out.append(ring); continue
        def gene(angles):
            t = 0
            for d, s_ in zip(angles, src):
                cx, cy, rs = _sat_disque(mid, d, s_[1], s_[2:])
                t += sum(max(0, R + rs + 3 - math.hypot(cx - nx, cy - ny)) for nx, ny, R in disques)
            return t
        sym = [j for j, s_ in enumerate(src) if s_[0] in ("SYM", "NS")]
        n = len(sym)
        bases = []
        if sym:
            cands = [[90], [270]] if n == 1 else [[90, 270], [180, 0]] if n == 2 else [[(90 + k * 360 / n) % 360 for k in range(n)]]
            for c in cands:
                a = [s_[0] for s_ in src]
                for d, j in zip(c, sym): a[j] = d
                bases.append(a)
        else:
            bases.append([s_[0] for s_ in src])
        best = None
        for dl in sorted(range(-180, 181, 2), key=abs):
            for b in bases:
                a = [(x + dl) % 360 for x in b]
                g = gene(a)
                if best is None or (g, abs(dl)) < (best[0], abs(best[1])): best = (g, dl, a)
            if best[0] == 0: break
        g, dl, a = best
        nom = ring["label"].split()[0]
        if dl and declared: DESSIN.append((_FORME[0], nom, f"satellites tournés de {dl:+d}° le long du cercle pour rester visibles"))
        if g > 0 and declared: DESSIN.append((_FORME[0], nom, "satellite : aucune place sans toucher un Noyau ; posé là où il touche le moins (dessiné par-dessus)"))
        out.append(dict(ring, sats=[(d, *s_[1:]) for d, s_ in zip(a, src)]))
    return out


def _cercles(rings, geo, declared, disques):
    """cercles concentriques autour du centre, du plus extérieur au plus intérieur ; annotations dans les portions visibles"""
    parts = []
    for ring, (rin, rout) in reversed(list(zip(rings, geo))):
        parts.append(f'<circle r="{GG.f(rout)}" class="paper-f"/>')
        parts.append(GG.value(rin, ring["spec"]))
        words = ring["label"].replace("·", " ").split()
        text = " ".join(words if declared else words[1:])
        if rout > rin: parts.append(f'<circle r="{GG.f(rin)}" class="ink-s"/><circle r="{GG.f(rout)}" class="ink-s"/>')
        else: parts.append(f'<circle r="{GG.f(rin)}" class="ink-s"/>')
        if text:
            mid = (rin + rout) / 2
            sats_ang = [(s[0], math.degrees(math.asin(min(1, _sat_disque(mid, s[0], s[1], s[2:])[2] / mid)))) for s in ring.get("sats", [])]
            centres = ring.get("centres") or _places(rin, rout, text, sats_ang, disques, words[0] if declared else ring["label"].split()[0])
            parts.append(_label(rin, rout, text, centres))
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
        return len(w if declared else w[1:]) > 0
    return h


def _sud_vers_l_exterieur(rings, a):
    """Noyau non tourné (nord en haut) : un satellite de cercle propre que le moteur pose au sud (270°) se pose du côté
    qui regarde vers l'extérieur du glyphe (angle a du Noyau sur le cercle d'École) ; les autres gardent leur place."""
    return [dict(ring, sats=[((a if s_[0] == 270 else s_[0]), *s_[1:]) for s_ in ring.get("sats", [])]) for ring in rings]


def _tourne(x, y, th):
    t = math.radians(th)
    return x * math.cos(t) - y * math.sin(t), x * math.sin(t) + y * math.cos(t)


def dessin(lab_ecole, g_com, g_noy, declared, nom=""):
    """le glyphe combiné, sans ses satellites astraux"""
    _FORME[0] = nom
    n = len(g_noy)
    # 1. les piles des Noyaux, dessinées par le moteur, droites (nord en haut) ; satellites du sud vers l'extérieur
    piles = []
    for (comb, core, rings), a in zip(g_noy, ANGLES[n]):
        rings = _sud_vers_l_exterieur(GG.resolve_ns(rings, R_NOYAU), a)
        GG.R0 = R_NOYAU
        geo = GG.ring_geo(rings, R_NOYAU, None, _has_text(declared))
        svg = GG._glyph(core, rings, r0=R_NOYAU, declared=declared)
        inner = re.sub(r'^<svg[^>]*>', '', svg)[:-6]
        corps = geo[-1][1] if geo else R_NOYAU
        locaux = [(0.0, 0.0, corps)]
        for ring, (rin, rout) in zip(rings, geo):
            for d, sp, *x in ring.get("sats", []):
                locaux.append(_sat_disque((rin + rout) / 2, d, sp, x))
        piles.append((inner, locaux))
    # 2. le cercle d'École : le plus petit rayon où deux Noyaux voisins (corps et satellites) ne se touchent pas
    def placer(Dr):
        out = []
        for (inner, locaux), a in zip(piles, ANGLES[n]):
            th = 0                              # Noyau droit, jamais tourné
            cx, cy = GG.pt(Dr, a)
            out.append((inner, th, cx, cy, [(cx + _tourne(x, y, th)[0], cy + _tourne(x, y, th)[1], r) for x, y, r in locaux]))
        return out
    def touche(pl):
        for i in range(len(pl)):
            for j in range(i + 1, len(pl)):
                for x1, y1, r1 in pl[i][4]:
                    for x2, y2, r2 in pl[j][4]:
                        if math.hypot(x1 - x2, y1 - y2) < r1 + r2 + MARGE: return True
        return False
    Dr = max(max(l[0][2] for _, l in piles) / (math.sin(math.pi / n) if n > 1 else 1), 1)
    # annotations de l'École : au milieu des intervalles entre les Noyaux
    A_ = ANGLES[n]
    gaps = sorted((A_[k] + ((A_[(k + 1) % n] - A_[k]) % 360) / 2) % 360 for k in range(n)) if n > 1 else [270]
    def tient(Dr, pl):
        """l'annotation déclarée de l'École (la plus longue : même rayon pour les deux versions) tient entière et visible
        dans chaque intervalle, à sa taille habituelle"""
        dq = [d for p in pl for d in p[4]]
        td_ = _largeur(Dr, f"ECOLE {lab_ecole}")
        return not any(_cache(g - td_ / 2 + td_ * k / 20, r, dq, 1) for g in gaps for k in range(21) for r in (Dr, Dr + GG.BAND))
    # le plus petit rayon où (a) deux Noyaux voisins ne se touchent pas et (b) l'annotation de l'École tient
    while touche(placer(Dr)): Dr += 0.5
    D_contact = Dr
    while not tient(Dr, placer(Dr)): Dr += 0.5
    if declared and Dr > D_contact:
        DESSIN.append((nom, "ECOLE", f"Noyaux écartés pour l'annotation de l'École : rayon {D_contact:.1f} → {Dr:.1f}"))
    pl = placer(Dr)
    disques = [d for p in pl for d in p[4]]
    ecole = dict(label=f"ECOLE {lab_ecole}", spec=[], sats=[], centres=gaps)
    geo_c = [(Dr, Dr + GG.BAND)]
    t_ec = f"ECOLE {lab_ecole}" if declared else lab_ecole
    td = _largeur(Dr, t_ec)
    for g in gaps:
        if any(_cache(g + s * td / 2, r, disques, 1) for s in (-1, 1) for r in (Dr, Dr + GG.BAND)):
            DESSIN.append((nom, "ECOLE", f"annotation « {t_ec.lower()} » ({td:.0f}°) en partie cachée par les Noyaux à {g:.0f}°"))
    # 3. les autres cercles communs, juste après l'École, à l'écart habituel ; ils passent sous les Noyaux
    geo_e = GG.ring_geo(g_com, Dr + GG.BAND, None, _has_text(declared)) if g_com else []
    communs = _poser(g_com, geo_e, disques, declared)
    if declared:
        for ring, (rin, rout) in zip(communs, geo_e):
            p = max(_part_cachee(rin, disques), _part_cachee(rout, disques))
            if p > 0: DESSIN.append((nom, ring["label"].split()[0], f"cercle caché sous les Noyaux sur {100 * p:.0f} % de son tour"))
    parts = _cercles(communs, geo_e, declared, disques) + _cercles([ecole], geo_c, declared, disques)
    for inner, th, cx, cy, _ in pl:
        parts.append(f'<g transform="translate({GG.f(cx)},{GG.f(cy)})">{inner}</g>')
    parts += _sats(communs, geo_e)          # par-dessus : un satellite qui n'a pas trouvé de place libre reste visible
    R = max([math.hypot(x, y) + r for x, y, r in disques] + ([_rayon_max(communs, geo_e)] if g_com else [])) + 24
    return f'<svg viewBox="{GG.f(-R)} {GG.f(-R)} {GG.f(2*R)} {GG.f(2*R)}" role="img" xmlns="http://www.w3.org/2000/svg">{"".join(parts)}</svg>'


# ---------- le glyphe en bande (essai) ----------
PAD_RANG = 10       # marge au-dessus et au-dessous des médaillons, dans la rangée du haut
ECART_MED = 12      # écart minimal entre deux médaillons voisins
BANDE_FAITS = []    # (forme, ce qui a été fait ou se lit mal)


def bande(nom, lab_ecole, g_noy, communs, split, part, pole, declared):
    """Bande d'une forme combinée : rangée du haut, les Noyaux en médaillons (glyphe rond du moteur : matière, cercles
    propres, satellites à leur place habituelle, le sud vers le bas, c'est-à-dire vers l'extérieur de la bande),
    côte à côte dans l'ordre de B12, centrés à intervalles égaux ; dessous, l'encart de l'École (comme l'encart d'école
    sous la voie des éléments d'une bande hybride) ; puis les cercles communs déroulés par le moteur (band_glyph.band)."""
    import band_glyph as BG
    n = len(g_noy)
    meds = []
    for comb, core, rings in g_noy:
        rings = GG.resolve_ns(rings, R_NOYAU)
        GG.R0 = R_NOYAU
        geo = GG.ring_geo(rings, R_NOYAU, None, _has_text(declared))
        inner = re.sub(r'^<svg[^>]*>', '', GG._glyph(core, rings, r0=R_NOYAU, declared=declared))[:-6]
        corps = geo[-1][1] if geo else R_NOYAU
        dq = [(0.0, 0.0, corps)] + [_sat_disque((rin + rout) / 2, d, sp, x) for ring, (rin, rout) in zip(rings, geo) for d, sp, *x in ring.get("sats", [])]
        meds.append((inner, min(x - r for x, y, r in dq), max(x + r for x, y, r in dq), min(y - r for x, y, r in dq), max(y + r for x, y, r in dq)))
    # longueur : la longueur habituelle (960), allongée seulement si les médaillons n'y tiennent pas
    pas = max(m[2] - m[1] for m in meds) + ECART_MED
    Lb = max(BG.L, math.ceil(n * pas))
    if declared and Lb > BG.L: BANDE_FAITS.append((nom, f"bande allongée de {BG.L} à {Lb} pour que les médaillons tiennent côte à côte"))
    yc = PAD_RANG + max(-m[3] for m in meds)
    Hr = yc + max(m[4] for m in meds) + PAD_RANG
    parts = []
    for k, (inner, x0, x1, y0, y1) in enumerate(meds):
        cx = Lb * (k + 0.5) / n
        parts.append(f'<g transform="translate({GG.f(cx)},{GG.f(yc)})">{inner}</g>')
    if declared:
        lib = min(Lb / n - (m[2] - m[1]) for m in meds)
        BANDE_FAITS.append((nom, f"rangée des médaillons : hauteur {Hr:.0f}, écart le plus petit entre deux médaillons {lib:.0f}"))
    # l'encart de l'École, sous la rangée
    t_ec = f"ECOLE {lab_ecole}" if declared else lab_ecole
    parts.append(BG.hline(Hr, 0, Lb))
    parts.append(BG.annot(t_ec, Hr, Hr + GG.BAND, [], Lb))
    parts.append(BG.hline(Hr + GG.BAND, 0, Lb))
    top = Hr + GG.BAND
    # les cercles communs, déroulés par le moteur, avec la polarité de la forme
    sp = dict(split=split, poles_impacts=[pole] * sum(1 for r in communs if r[0] == "IMPACT"), core=("hyb", (None,) * 4, None), rings=communs)
    rings_b = C.band_rings(sp)
    inner_c, _, Hc, _ = BG.band(("aucun",), rings_b, declared, length=Lb)
    BG._cid[0] += 1; cid = f"bandclip{BG._cid[0]}"          # l'encart de l'École est coupé aux bouts, comme toute bande
    enc = "".join(parts[-3:])
    body = ("".join(parts[:-3]) + f'<defs><clipPath id="{cid}"><rect x="0" y="{GG.f(Hr - 30)}" width="{Lb}" height="{GG.f(GG.BAND + 60)}"/></clipPath></defs>'
            f'<g clip-path="url(#{cid})">{enc}</g>' + f'<g transform="translate(0,{GG.f(top)})">{inner_c}</g>')
    main = (body, Lb, top + Hc, yc)
    sp_ = split if declared else part
    left = BG.astral_band("ten", sp_[1]) if (sp_[1] or declared) else None
    right = BG.astral_band("lum", sp_[0]) if (sp_[0] or declared) else None
    return BG.compose(main, left, right)


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
<section class="sec"><h3>Glyphe en bande</h3><div class="pair one"><figure>{r['bande'][0]}<figcaption>Déclarée · tous les cercles classés</figcaption></figure>
<figure>{r['bande'][1]}<figcaption>Non déclarée · seuls les cercles à polarité illisible</figcaption></figure></div></section>
<section class="sec"><h3>Lecture</h3>{table(r['rows'])}</section></article>""")
    fbrows = [(a, b, "", c) for a, b, c in [("1", "Noyau", fb["verb"])] + fb["rows"]]
    arts.append(f"""<article class="forme" id="gc"><header class="fh"><div class="eyebrow">Pour comparaison · telle qu'elle est sur main</div>
<h2>{html.escape(fb['fr'])} (5e) — {html.escape(fb['label'])}</h2><p class="lede">{html.escape(fb['verb'])}</p></header>
<section class="sec"><h3>Glyphe circulaire</h3><div class="pair one"><figure class="grand">{fb['svg'][0]}<figcaption>Déclarée · tous les cercles classés</figcaption></figure>
<figure class="grand">{fb['svg'][1]}<figcaption>Non déclarée · seuls les cercles à polarité illisible</figcaption></figure></div>{pol_html(fb['split'])}</section>
<section class="sec"><h3>Glyphe en bande</h3><div class="pair one"><figure>{C.band_svg(fb, True)}<figcaption>Déclarée · tous les cercles classés</figcaption></figure>
<figure>{C.band_svg(fb, False)}<figcaption>Non déclarée · seuls les cercles à polarité illisible</figcaption></figure></div></section>
<section class="sec"><h3>Lecture</h3>{table(fbrows, ou=False).replace("<td></td>", "")}</section></article>""")
    sommaire = "".join(f'<a class="chip" href="#g{i}">{i}. {html.escape(r["sort"])}</a>' for i, r in enumerate(res, 1)) + '<a class="chip" href="#gc">Boule de feu (main)</a>'
    page = ST.HEAD.format(title="Essai · formes combinées", root="") + f"""
<header><div class="eyebrow">Essai · chantier « combinees » · rien n'entre dans la bibliothèque</div><h1>Formes combinées : essai de dessin</h1>
<p class="lede">Troisième essai. Plusieurs Noyaux hybrides, un par combinaison, lancés en même temps. Le cercle d'École, premier cercle commun, passe
par le centre des Noyaux et les relie ; tous les autres cercles communs, de la Cible à la Cosmétique, sont à l'extérieur ; chaque Noyau
porte ses propres cercles autour de lui, droit ; un satellite qui se poserait au sud se pose vers l'extérieur du glyphe. Les cercles communs suivent le cercle d'École
à l'écart habituel et passent sous les Noyaux ; leurs annotations se placent dans les portions visibles. Lecture : d'abord les Noyaux, puis les cercles communs, du centre vers l'extérieur.
Essai de la bande (sous chaque glyphe rond) : les Noyaux en médaillons côte à côte, dans l'ordre de B12, l'encart de l'École dessous, puis les cercles communs déroulés.</p>
<div class="chips">{sommaire}</div></header>
<div class="essai">""" + "".join(arts) + "</div>" + ST.FOOT
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(page)
    # une page par glyphe, pour les images
    for i, r in enumerate(res, 1):
        open(os.path.join(out, f"_image_{i}.html"), "w", encoding="utf-8").write(
            '<!doctype html><html data-theme="light"><head><meta charset="utf-8"><link rel="stylesheet" href="style.css"><style>html,body{margin:0;background:var(--paper)}'
            'svg{width:100vw;height:100vh;display:block}</style></head><body>' + r["svg"][0] + "</body></html>")
        open(os.path.join(out, f"_image_{i}_bande.html"), "w", encoding="utf-8").write(
            '<!doctype html><html data-theme="light"><head><meta charset="utf-8"><link rel="stylesheet" href="style.css"><style>html,body{margin:0;background:var(--paper)}'
            'svg{width:100vw;height:100vh;display:block}</style></head><body>' + r["bande"][0] + "</body></html>")
    return res, fb


if __name__ == "__main__":
    res, fb = essai(sys.argv[1])
    json.dump(dict(formes=[dict(r, svg=list(r["svg"]), bande=list(r["bande"])) for r in res], faits=FAITS, dessin=DESSIN, bande_faits=BANDE_FAITS, boule_de_feu=dict(svg=list(fb["svg"]))),
              open(os.path.join(sys.argv[1], "_essai.json"), "w", encoding="utf-8"), ensure_ascii=False, default=repr)
    for r in res: print(r["sort"], "|", r["label"], "|", len(r["svg"][0]), len(r["svg"][1]))
    for x in FAITS: print("  fait :", x)
    for x in DESSIN: print("  dessin :", x)
    for x in BANDE_FAITS: print("  bande :", x)
