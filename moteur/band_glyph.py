"""Glyphe en bande : conversion propre d'un glyphe circulaire.
Haut = centre (noyau), bas = extérieur. x = angle, coupé au nord, sens horaire.
Couronnes et encarts gardent la même hauteur que dans le cercle ; les formes restent rectilignes."""
import math, sys
import os as _os
D = _os.path.dirname(_os.path.abspath(__file__))
DATA = _os.path.join(D, "..", "donnees")
sys.path.insert(0, D)
import gen_glyphs as GG
from alde import a1_syll
from build_picto import picto

def f(x): return f"{x:.2f}"
HN = 76                    # hauteur de la rangée du noyau
L = 960                    # longueur de la bande (le tour complet)
GAP, BAND = GG.GAP, GG.BAND

# Repères : les huit emplacements des encarts. Le nord est au milieu, sous le noyau ;
# le sud est coupé en deux, une moitié à chaque bout. Sens horaire : sud, ouest, nord, est, sud.
def X(deg):                # angle du cercle (0 = est, sens trigo) -> abscisse
    return ((270 - deg) % 360) / 360 * L
SLOTS = [("S", 0), ("SO", 1/8), ("O", 1/4), ("NO", 3/8), ("N", 1/2), ("NE", 5/8), ("E", 3/4), ("SE", 7/8), ("S", 1)]

def hline(y, x0=0, x1=None): return f'<line x1="{f(x0)}" y1="{f(y)}" x2="{f(x1 if x1 is not None else L)}" y2="{f(y)}" class="ink-s"/>'
def vline(x, y0, y1): return f'<line x1="{f(x)}" y1="{f(y0)}" x2="{f(x)}" y2="{f(y1)}" class="ink-s"/>'

def is_pos(kind, arg, rot):
    """traduit l'orientation du cercle en polarité : True = Hodolin / positif"""
    if kind == "line": return rot % 180 == 90
    if kind == "cross": return rot % 90 == 0
    if kind == "poly" and arg == 4: return rot % 90 == 45
    return rot % 360 == 90

LANE = 26                  # hauteur d'une voie quand la couronne porte plusieurs formes
DEPTH = 0.55               # les côtés d'un polygone descendent à mi-voie : seuls ses n sommets touchent une paroi

def couronne_h(spec):
    n = len([t for t in spec if t[0] != "full"])
    return LANE if n <= 1 else n * LANE

def lane_lines(kind, pos):
    """trait et croix n'ont pas de sommet : ils touchent les deux parois, et leur polarité reste dans leur position"""
    if kind == "line":
        return [L/2, 0, L] if pos else [L/4, 3*L/4]                       # nord-sud / ouest-est
    return [L/2, L/4, 3*L/4, 0, L] if pos else [L/8, 3*L/8, 5*L/8, 7*L/8]  # + / ×

def form(spec, ytop, ybot=None, rin=None):
    """Une voie par forme. Polygone : n sommets touchent une paroi, la paroi du haut (le centre) si positif, du bas si négatif ;
    un sommet toujours au nord, au milieu de la bande. Les voies sont séparées par un filet fin."""
    items = [t for t in spec if t[0] != "full"]
    if not items: return ""
    # les voies qui touchent le haut d'abord : deux sommets ne se rencontrent jamais sur un même filet
    items.sort(key=lambda t: 0 if is_pos(*t) else 1)
    H = (ybot - ytop) / len(items)
    out = ""
    for i, (kind, arg, rot) in enumerate(items):
        t, b = ytop + i * H, ytop + (i + 1) * H
        if i: out += f'<line x1="0" y1="{f(t)}" x2="{L}" y2="{f(t)}" class="ink-s lane"/>'
        pos = is_pos(kind, arg, rot)
        if kind in ("line", "cross"):
            for x in lane_lines(kind, pos):
                out += vline(x, t, b)
        else:
            n = arg; span = L / n
            wall, sgn = (t, 1) if pos else (b, -1)
            d = H * DEPTH
            for k in range(-n, 2 * n):
                x0 = L/2 + k * span
                if x0 < -span or x0 > L + span: continue
                for side in (-1, 1):
                    out += f'<line x1="{f(x0)}" y1="{f(wall)}" x2="{f(x0 + side*span/2)}" y2="{f(wall + sgn*d)}" class="ink-s"/>'
    return out

ADV = GG.ALW * GG.AK * 1.18
def word_units(text):
    words = [GG.LEX[w] for w in text.replace("·", " ").split()]
    units = []
    for k, w in enumerate(words):
        if k: units.append(None)
        units += w
    return units

def annot(text, ytop, ybot, sats, L=None):
    L = L or globals()['L']
    Xl = lambda d: ((270 - d) % 360) / 360 * L
    units = word_units(text)
    if not units: return ""
    width = ADV * len(units)
    # mêmes emplacements que le cercle : huit à 45°, satellites prioritaires, retrait deux par deux
    centers = GG.annot_slots(sats, 360 * width / L)
    base = ybot - 0.8 - 14 * GG.AK          # pied des lettres vers l'extérieur, haut vers le centre : écriture droite
    out = ""
    for c in centers:
        x0 = Xl(c) - width / 2 + ADV / 2
        for xs in (x0, x0 - L, x0 + L):
            if xs + width < -ADV or xs > L + ADV: continue
            for i, u in enumerate(units):
                if u is None: continue
                out += (f'<g transform="translate({f(xs + i * ADV)},{f(base)}) scale({GG.AK}) translate({-GG.ALW/2 + 4},0) {GG.ITAL}" class="alde">'
                        f'{a1_syll("ink", u[0], u[1])}</g>')
    return out


# ---------- chiffres aldiens ----------
NUM_H = 23            # les chiffres gardent tous la même taille, centrés sur leur voie
NUM = {1: (1, 0, 0), 2: (2, 0, 0), 3: (3, 0, 0), 4: (3, 1, 0), 5: (3, 2, 0), 7: (3, 2, 2), 9: (3, 3, 3)}
def numeral(n, cx, cy, h):
    """barres verticales (trois au plus), puis diagonales descendantes et montantes : le nombre de traits est la valeur"""
    bars, dn, up = NUM[n]
    k = h / 330; s = 47 * k; half = h / 2
    out = ""
    xs = [(i - (bars - 1) / 2) * s for i in range(bars)]
    for x in xs:
        out += f'<line x1="{f(cx + x)}" y1="{f(cy - half)}" x2="{f(cx + x)}" y2="{f(cy + half)}" class="ink-s num"/>'
    w = (xs[-1] - xs[0]) / 2 + 70 * k; dy = 141 * k / 2
    def offs(m): return [(i - (m - 1) / 2) * 47 * k for i in range(m)]
    for o in offs(dn):
        out += f'<line x1="{f(cx - w)}" y1="{f(cy + o - dy)}" x2="{f(cx + w)}" y2="{f(cy + o + dy)}" class="ink-s num"/>'
    for o in offs(up):
        out += f'<line x1="{f(cx - w)}" y1="{f(cy + o + dy)}" x2="{f(cx + w)}" y2="{f(cy + o - dy)}" class="ink-s num"/>'
    return out
def lane_value(kind, arg):
    return 1 if kind == "line" else 2 if kind == "cross" else arg

# ---------- noyau ----------
def noyau_band(core, cx, cy, R):
    """le noyau dessiné intact, sans son encart circulaire : l'école ou l'art s'écrit à plat dans la rangée"""
    out = ""
    if core[0] == "verb":
        return f'<g class="pk pos" transform="translate({f(cx)},{f(cy)}) scale({R / 46:.3f})">{picto(core[1], core[2])}</g>'
    out += f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(R)}" class="paper-f ink-s"/>'
    if core[0] == "chrono":
        rc = R * 0.46; rs = (R - rc) / 2 - 1; d = rc + rs
        out += f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(rc)}" class="ink-s"/><g class="pk pos" transform="translate({f(cx)},{f(cy)}) scale({rc / 46:.3f})">{picto(core[1], core[2])}</g>'
        els = core[3]
    else:
        rs = (R - 3) / (1 + math.sqrt(2)); d = rs * math.sqrt(2); els = core[1]
    for deg, el in zip((90, 180, 0, 270), els):
        ex, ey = GG.pt(d, deg)
        out += f'<g transform="translate({f(cx + ex)},{f(cy + ey)})"><circle r="{f(rs)}" class="paper-f ink-s"/>{GG.element(el, rs * 0.62)}</g>'
    return out
def core_label(core):
    if core[0] == "chrono": return core[4]
    if core[0] == "hyb": return core[2]
    return None

def sat_r(sp):
    return 18 + 10 * max(0, len([t for t in sp if t[0] != "full"]) - 1)
EL = 44              # hauteur de la voie élémentaire
M = 44            # marge latérale où s'écrivent les chiffres
def band(core, rings, declared=True, length=None, numerals=True, keep_sat_encart=True, thick=False):
    """rings : dict(label, spec, sats), du centre vers l'extérieur. Renvoie (svg intérieur, largeur, hauteur)."""
    Lb = length or L
    Xb = lambda d: ((270 - d) % 360) / 360 * Lb
    W = (lambda yy: hline(yy, 0, Lb).replace('class="ink-s"', 'class="ink-s wall"')) if thick else (lambda yy: hline(yy, 0, Lb))
    parts, y = [], 0
    kind = core[0]
    if kind in ("verb", "chrono"):            # le verbe arcanique seul, en haut au centre
        vk, vn = (core[1], core[2])
        parts.append(f'<g class="pk pos" transform="translate({f(Lb/2)},{f(HN/2)}) scale({(HN/2 - 5) / 46:.3f})">{picto(vk, vn)}</g>')
        y = HN
    conn = HN / 2
    if kind in ("chrono", "hyb"):             # voie des quatre éléments, puis son encart
        els = core[3] if kind == "chrono" else core[1]
        parts.append(W(y))
        rs = EL / 2 - 4
        # chaque élément avance d'un huitième de tour : feu au nord-est, terre au sud-est, eau au sud-ouest, air au nord-ouest
        for deg, el in zip((90, 180, 0, 270), els):
            ex = Xb(deg - 45)
            parts.append(f'<g transform="translate({f(ex)},{f(y + EL/2)})"><circle r="{f(rs)}" class="paper-f ink-s"/>{GG.element(el, rs * 0.62)}</g>')
        conn = y + EL / 2
        y += EL
        parts.append(W(y))
        lab = core_label(core)
        if lab:
            parts.append(annot(lab, y, y + BAND, [], Lb))
            y += BAND
    parts.append(W(y))
    nums, sats_draw = [], []
    # les satellites grandissent librement ; les couronnes voisines s'élargissent pour leur faire place
    def texts(ring):
        words = ring["label"].replace("·", " ").split()
        t = " ".join(words if declared else words[1:])
        if not t and keep_sat_encart and ring.get("sats"): t = words[0]
        return t
    CH = [couronne_h(r["spec"]) for r in rings]
    HE = [BAND if texts(r) else 0 for r in rings]
    RS = [max([sat_r(s[1]) + (GG.SBAND if len(s) > 2 and s[2] else 0) for s in r.get("sats", [])] or [0]) for r in rings]
    tail = 0
    ov = [max(0, rs + 4 - HE[i] / 2) if rs else 0 for i, rs in enumerate(RS)]   # débord d'un satellite hors de son encart
    for i in range(len(rings)):
        above = ov[i] + (ov[i - 1] if i else 0)          # la couronne i sépare l'encart i-1 de l'encart i
        CH[i] = max(CH[i], above)
    if rings: tail = ov[-1]
    for idx, ring in enumerate(rings):
        words = ring["label"].replace("·", " ").split()
        text = " ".join(words if declared else words[1:])
        if not text and keep_sat_encart and ring.get("sats"):
            text = words[0]          # un cercle à satellite garde son encart, et on le remplit : le nom du critère
        ch = CH[idx]
        globals()['L'], old = Lb, globals()['L']
        parts.append(form(ring["spec"], y, y + ch))
        globals()['L'] = old
        items = sorted([t for t in ring["spec"] if t[0] != "full"], key=lambda t: 0 if is_pos(*t) else 1)
        if numerals and items:
            lh = ch / len(items)
            for i, t in enumerate(items):
                for cx in (-M / 2, Lb + M / 2):
                    nums.append(numeral(lane_value(t[0], t[1]), cx, y + (i + 0.5) * lh, NUM_H))
        y += ch
        parts.append(W(y))
        he = BAND if (text or (keep_sat_encart and ring.get("sats"))) else 0
        if he:
            parts.append(W(y + he))
            parts.append(annot(text, y, y + he, [s[0] for s in ring.get("sats", [])], Lb))
        for d, sp, *lab in ring.get("sats", []):
            if lab and lab[0]: sats_draw.append(GG.satellite_annot(Xb(d), y + he / 2, sat_r(sp), sp, lab[0]))
            else: sats_draw.append(GG.satellite(Xb(d), y + he / 2, sat_r(sp), sp))
        y += he
    y += tail
    _cid[0] += 1; cid = f"bandclip{_cid[0]}"
    inner = (f'<defs><clipPath id="{cid}"><rect x="0" y="-30" width="{Lb}" height="{y + 60}"/></clipPath></defs>'
             f'<g clip-path="url(#{cid})">' + "".join(parts) + '</g>' + "".join(sats_draw) + "".join(nums))
    return inner, Lb, y, conn
_cid = [0]

def astral_band(kind, crits, length=300):
    """satellite astral en bande : son symbole en tête, puis un encart par critère classé"""
    Lb = length
    parts = [hline(HN, 0, Lb)]
    sym = GG.__dict__.get("_astral_sym")
    import spells as SP
    g = SP.star() if kind == "lum" else SP.abyss()
    parts.append(f'<g transform="translate({Lb/2},{HN/2}) scale(1.6)"><circle r="20" class="paper-f ink-s"/>{g}</g>')
    y = HN
    for c in crits:
        y += 6; parts.append(hline(y, 0, Lb))
        units = word_units(c); w = ADV * len(units)
        for cx in (Lb / 4, 3 * Lb / 4):          # deux copies, aux repères ouest et est
            x0 = cx - w / 2 + ADV / 2
            for i, u in enumerate(units):
                if u is None: continue
                parts.append(f'<g transform="translate({f(x0 + i * ADV)},{f(y + BAND - 0.8 - 14 * GG.AK)}) scale({GG.AK}) translate({-GG.ALW/2 + 4},0) {GG.ITAL}" class="alde">{a1_syll("ink", u[0], u[1])}</g>')
        y += BAND; parts.append(hline(y, 0, Lb))
    return "".join(parts), Lb, y

def compose(main, left=None, right=None, gap=36):
    """bande principale, chiffres en marge, satellites astraux de part et d'autre (ténébreux à gauche, lumineux à droite)"""
    inner, Lm, Hm, conn = main
    pieces, x = [], 0
    H = Hm
    if left:
        li, ll, lh = left
        pieces.append(f'<g transform="translate(0,0)">{li}</g>'); x = ll + gap
        pieces.append(f'<line x1="{ll}" y1="{f(conn)}" x2="{x + M}" y2="{f(conn)}" class="ink-s"/>')
        H = max(H, lh)
    xm = x + M
    pieces.append(f'<g transform="translate({xm},0)">{inner}</g>')
    x = xm + Lm + M
    if right:
        ri, rl, rh = right
        pieces.append(f'<line x1="{x - M}" y1="{f(conn)}" x2="{x + gap}" y2="{f(conn)}" class="ink-s"/>')
        pieces.append(f'<g transform="translate({x + gap},0)">{ri}</g>'); x += gap + rl
        H = max(H, rh)
    pad = 8
    return (f'<svg viewBox="{-pad} {-pad} {x + 2*pad} {H + 2*pad}" role="img" xmlns="http://www.w3.org/2000/svg">'
            f'<rect x="{-pad}" y="{-pad}" width="{x + 2*pad}" height="{H + 2*pad}" class="paper-f"/>' + "".join(pieces) + '</svg>')
