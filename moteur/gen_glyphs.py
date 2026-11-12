import math, html

R0 = 34          # rayon du noyau
GAP = 24         # couronne (zone où la forme se lit)
BAND = 16        # largeur de l'encart (double paroi)
HALO = 0         # les formes touchent les parois

def pt(r, deg):
    a = math.radians(deg)
    return (r * math.cos(a), -r * math.sin(a))

def f(x):
    return f"{x:.2f}"

def poly(r, n, rot):
    pts = [pt(r, rot + 360 * k / n) for k in range(n)]
    return '<polygon points="%s" class="ink-s"/>' % " ".join(f"{f(x)},{f(y)}" for x, y in pts)

def line(r, rot):
    (x1, y1), (x2, y2) = pt(r, rot), pt(r, rot + 180)
    return f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" class="ink-s"/>'

def value(r, spec, cx=0, cy=0):
    """spec: list of (kind, arg, rot). kind in line, cross, poly, full"""
    out = []
    for kind, arg, rot in spec:
        if kind == "line":
            out.append(line(r, rot))
        elif kind == "cross":
            out.append(line(r, rot)); out.append(line(r, rot + 90))
        elif kind == "poly":
            out.append(poly(r, arg, rot))
        elif kind == "full":
            pass                                   # plein : le cercle tracé, sans forme
    s = "".join(out)
    if cx or cy:
        s = f'<g transform="translate({f(cx)},{f(cy)})">{s}</g>'
    return s

_pid = [0]
def label_arc(r, text, a1=200, a2=340, size=8, top=False):
    _pid[0] += 1
    pid = f"p{_pid[0]}"
    if top:   # arc supérieur, gauche -> droite
        (x1, y1), (x2, y2) = pt(r, 180 - (a1 - 180)), pt(r, 360 - (a2 - 180))
        x1, y1 = pt(r, 160); x2, y2 = pt(r, 20)
        d = f"M{f(x1)},{f(y1)} A{f(r)},{f(r)} 0 0 1 {f(x2)},{f(y2)}"
    else:     # arc inférieur, gauche -> droite
        x1, y1 = pt(r, a1); x2, y2 = pt(r, a2)
        large = 1 if (a2 - a1) > 180 else 0
        d = f"M{f(x1)},{f(y1)} A{f(r)},{f(r)} 0 {large} 0 {f(x2)},{f(y2)}"
    return (f'<path id="{pid}" d="{d}" fill="none"/>'
            f'<text class="enc" font-size="{size}" dy="{f(size*0.35)}"><textPath href="#{pid}" startOffset="50%" text-anchor="middle">{html.escape(text)}</textPath></text>')

def spiral(rmax, turns=2.25, steps=140):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        a = math.radians(90 + 360 * turns * t)
        r = 3 + (rmax - 3) * t
        pts.append((r * math.cos(a), -r * math.sin(a)))
    return "M" + " L".join(f"{f(x)},{f(y)}" for x, y in pts)

def noyau(kind):
    if isinstance(kind, tuple) and kind[0] == "verb":
        from build_picto import picto as _picto
        k = R0 / 46
        return f'<circle r="{R0}" class="paper-f ink-s"/><g class="pk pos" transform="scale({k:.3f})">{_picto(kind[1], kind[2])}</g>'
    if kind in ("pos", "neg"):
        from build_picto import picto as _picto
        k = R0 / 46
        return f'<circle r="{R0}" class="paper-f ink-s"/><g class="pk pos" transform="scale({k:.3f})">{_picto("existence", kind == "neg")}</g>'
    if isinstance(kind, tuple) and kind[0] == "chrono":
        from build_picto import picto as _picto
        Ri = R0 - BAND
        out = f'<circle r="{R0}" class="paper-f ink-s"/><circle r="{f(Ri)}" class="ink-s"/>' + label_alde(Ri, R0, kind[4], [])
        rc = Ri * 0.46
        rs = (Ri - rc) / 2 - 1
        d = rc + rs
        out += f'<circle r="{f(rc)}" class="ink-s"/><g class="pk pos" transform="scale({rc / 46:.3f})">{_picto(kind[1], kind[2])}</g>'
        for (deg, el) in zip((90, 180, 0, 270), kind[3]):
            cx, cy = pt(d, deg)
            out += f'<g transform="translate({f(cx)},{f(cy)})"><circle r="{f(rs)}" class="paper-f ink-s"/>{element(el, rs*0.62)}</g>'
        return out
    # noyau hybride : quatre sous-cercles = les quatre unités de la combinaison
    # (troisième élément facultatif : l'annotation du noyau, combinaison + école)
    if len(kind) > 2 and kind[2]:
        Ri = R0 - BAND
        out = f'<circle r="{R0}" class="paper-f ink-s"/><circle r="{f(Ri)}" class="ink-s"/>' + label_alde(Ri, R0, kind[2], [])
    else:
        Ri = R0
        out = f'<circle r="{R0}" class="paper-f ink-s"/>'
    rs = (Ri - 3) / (1 + math.sqrt(2))   # quatre sous-cercles en contact deux à deux
    d = rs * math.sqrt(2)
    for (deg, el) in zip((90, 180, 0, 270), kind[1]):
        cx, cy = pt(d, deg)
        out += f'<g transform="translate({f(cx)},{f(cy)})"><circle r="{f(rs)}" class="paper-f ink-s"/>{element(el, rs*0.62)}</g>'
    return out

def element(el, s):
    if el == "terre":
        return f'<rect x="{f(-s*0.78)}" y="{f(-s*0.78)}" width="{f(s*1.56)}" height="{f(s*1.56)}" class="el"/>'
    if el == "eau":
        return (f'<path d="M0,{f(-s)} C{f(s*0.15)},{f(-s*0.55)} {f(s*0.8)},{f(-s*0.05)} {f(s*0.8)},{f(s*0.38)} '
                f'A{f(s*0.8)},{f(s*0.8)} 0 0 1 {f(-s*0.8)},{f(s*0.38)} C{f(-s*0.8)},{f(-s*0.05)} {f(-s*0.15)},{f(-s*0.55)} 0,{f(-s)} Z" class="el"/>')
    if el == "feu":
        # symbole fourni par Baptiste, vectorisé
        import json as _j
        pts = _j.load(open(__import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)), "feu_path.json"), encoding="utf-8"))[0]
        k = s * 1.05
        return '<path d="M' + " L".join(f"{f(x*k)},{f(y*k)}" for x, y in pts) + ' Z" class="ink-f"/>'
    if el == "air":
        w = ""
        for dy in (-s * 0.35, s * 0.35):
            w += (f'<path d="M{f(-s)},{f(dy)} C{f(-s*0.5)},{f(dy - s*0.45)} {f(0)},{f(dy - s*0.45)} {f(0)},{f(dy)} '
                  f'S{f(s*0.5)},{f(dy + s*0.45)} {f(s)},{f(dy)}" class="el"/>')
        return w
    return ""

def satellite(cx, cy, rs, spec, label=None):
    s = f'<g transform="translate({f(cx)},{f(cy)})">'
    s += f'<circle r="{rs + 2.5}" class="paper-f"/><circle r="{rs}" class="paper-f ink-s"/>'
    if label:
        ri = rs - 7
        s += f'<circle r="{ri}" class="ink-s thin"/>'
        _pid[0] += 1
        pid = f"p{_pid[0]}"
        rr = (rs + ri) / 2
        x1, y1 = pt(rr, 200); x2, y2 = pt(rr, 340)
        s += (f'<path id="{pid}" d="M{f(x1)},{f(y1)} A{f(rr)},{f(rr)} 0 0 0 {f(x2)},{f(y2)}" fill="none"/>'
              f'<text class="enc" font-size="5.2" dy="1.8"><textPath href="#{pid}" startOffset="50%" text-anchor="middle">{label}</textPath></text>')
        s += value(ri - 1.5, spec)
    else:
        s += value(rs - 2.5, spec)
    return s + "</g>"

SBAND, SAK = 10, 0.13
def satellite_annot(cx, cy, base, spec, text):
    """satellite porteur de sa propre annotation : il se dédouble comme un cercle principal"""
    ri = base; ro = base + SBAND
    s = f'<g transform="translate({f(cx)},{f(cy)})">'
    s += f'<circle r="{f(ro + 2.5)}" class="paper-f"/><circle r="{f(ro)}" class="paper-f ink-s"/>'
    s += value(ri, spec) + f'<circle r="{f(ri)}" class="ink-s"/>' + label_alde(ri, ro, text, [], ak=SAK)
    return s + "</g>"

def label_sym(rmid, text, axis="v", size=8):
    """Annotation écrite deux fois, sur l'axe libre de satellites, haut des lettres vers l'extérieur."""
    out = ""
    r = rmid - size * 0.35
    centers = (90, 270) if axis == "v" else (0, 180)
    for c in centers:
        _pid[0] += 1
        pid = f"p{_pid[0]}"
        x1, y1 = pt(r, c + 70); x2, y2 = pt(r, c - 70)
        out += (f'<path id="{pid}" d="M{f(x1)},{f(y1)} A{f(r)},{f(r)} 0 0 1 {f(x2)},{f(y2)}" fill="none"/>'
                f'<text class="enc" font-size="{size}"><textPath href="#{pid}" startOffset="50%" text-anchor="middle">{html.escape(text)}</textPath></text>')
    return out

from alde import a1_syll
LEX = {
 "CIBLE": [("s", "i"), ("b", None), ("l", None)],
 "FORME": [("f", "o"), ("r", None), ("m", None)],
 "AMPLEUR": [(None, "a"), ("m", None), ("p", None), ("l", "e"), ("r", None)],
 "LOCALISATION": [("l", "o"), ("k", "a"), ("l", "i"), ("s", "a"), ("s", "i"), (None, "o"), ("n", None)],
 "IMPACT": [(None, "i"), ("m", None), ("p", "a"), ("k", None), ("t", None)],
 "PIEDS": [("p", "i"), (None, "e")],
 "CUBES": [("k", "u"), ("b", None)],
 "FEU": [("f", "e")],
 "METRES": [("m", "e"), ("t", None), ("r", None)],
 "KILOMETRES": [("k", "i"), ("l", "o"), ("m", "e"), ("t", None), ("r", None)],
 "FOIS": [("f", None), ("w", "a")],
 "DIAMETRE": [("d", "i"), (None, "a"), ("m", "e"), ("t", None), ("r", None)],
 "VIE": [("v", "i")],
}
AK, ALW = 0.2, 34
def annot_slots(sats, text_deg):
    """Huit emplacements à 45° ; les satellites passent d'abord ; on remplit uniformément,
    en retirant les copies deux par deux tant que l'annotation ne tient pas."""
    sats = [s % 360 for s in sats]
    def free(a): return all(abs((a - s + 180) % 360 - 180) > 1 for s in sats)
    cands = []
    if not sats:
        cands.append((8, [k * 45 for k in range(8)], 45))
    else:
        opp = {(s + 180) % 360 for s in sats}
        six = [k * 45 for k in range(8) if free(k * 45) and (k * 45) not in opp]
        if len(six) == 6: cands.append((6, six, 45))
    diag = [45, 135, 225, 315]; axes = [0, 90, 180, 270]
    cands.append((4, diag if all(free(a) for a in diag) else axes, 90))
    two = [90, 270] if (free(90) and free(270)) else [0, 180]
    cands.append((2, two, 180))
    for n, centers, gap in cands:
        if text_deg <= gap * 0.82:
            return centers
    return cands[-1][1]

ITAL = "skewX(-14)"
def label_alde(rin, rout, text, sats=(), ak=None):
    ak = ak or AK
    words = [LEX[w] for w in text.replace("·", " ").split()]
    if not words: return ""
    units = []
    for k, w in enumerate(words):
        if k: units.append(None)
        units += w
    rb = rin + 0.8 + 14 * ak
    adv = ALW * ak * 1.18                       # chasse élargie
    step = math.degrees(adv / rb)
    out = ""
    for cm in annot_slots(sats, step * len(units)):
        center = -cm
        for i, u in enumerate(units):
            if u is None: continue
            phi = center - (len(units) - 1) / 2 * step + i * step
            x, y = rb * math.cos(math.radians(phi)), rb * math.sin(math.radians(phi))
            out += (f'<g transform="translate({f(x)},{f(y)}) rotate({f(phi + 90)}) scale({ak}) translate({-ALW/2 + 4},0) {ITAL}" class="alde">'
                    f'{a1_syll("ink", u[0], u[1])}</g>')
    return out

def strokes(r, spec):
    """segments d'une valeur tracée au rayon r"""
    segs = []
    for kind, arg, rot in spec:
        if kind == "line": segs.append((pt(r, rot), pt(r, rot + 180)))
        elif kind == "cross":
            segs += [(pt(r, rot), pt(r, rot + 180)), (pt(r, rot + 90), pt(r, rot + 270))]
        elif kind == "poly":
            P = [pt(r, rot + 360 * k / arg) for k in range(arg)]
            segs += [(P[k], P[(k + 1) % arg]) for k in range(arg)]
    return segs

def sat_radius(spec):
    return 10 + 7 * max(0, len([t for t in spec if t[0] != "full"]) - 1)

def resolve_ns(rings, r0=34, first_gap=None):
    """Satellite « NS » : placé au nord ou au sud, là où il recouvre le moins de tracé
    (formes du cercle porteur et du cercle suivant, dans leurs couronnes visibles)."""
    if not any(s[0] == "NS" for r in rings for s in r.get("sats", [])): return rings
    geo, prev = [], r0
    for i, ring in enumerate(rings):
        rin = prev + (first_gap if (i == 0 and first_gap) else GAP)
        rout = rin + (BAND if ring["label"].split() else 0)
        geo.append((rin, rout)); prev = rout
    def covered(i, deg, rs):
        cx, cy = pt((geo[i][0] + geo[i][1]) / 2, deg); tot = 0
        for j in (i, i + 1):
            if j >= len(rings): continue
            lo = geo[j - 1][1] if j else r0; hi = geo[j][0]
            for (x1, y1), (x2, y2) in strokes(hi, rings[j]["spec"]):
                for t in range(201):
                    x, y = x1 + (x2 - x1) * t / 200, y1 + (y2 - y1) * t / 200
                    if lo <= math.hypot(x, y) <= hi and math.hypot(x - cx, y - cy) <= rs + 2.5: tot += 1
        return tot
    out = []
    for i, ring in enumerate(rings):
        sats = []
        for d, sp, *x in ring.get("sats", []):
            if d == "NS":
                rs = sat_radius(sp) + (SBAND if x and x[0] else 0)
                d = 90 if covered(i, 90, rs) <= covered(i, 270, rs) else 270
            sats.append((d, sp, *x))
        out.append(dict(ring, sats=sats))
    return out

def glyph(core, rings, **k):
    rings = resolve_ns(rings, k.get("r0", 34), k.get("first_gap"))
    return (_glyph(core, rings, declared=True, **k), _glyph(core, rings, declared=False, **k))

def _glyph(core, rings, extract=None, first_gap=None, r0=34, declared=True):
    global R0
    R0 = r0
    """rings"""
    geo = []
    prev = R0
    def has_text(ring):
        w = ring["label"].replace("·", " ").split()
        return len(w if declared else w[1:]) > 0
    for i, ring in enumerate(rings):
        g = first_gap if (i == 0 and first_gap) else GAP
        rin = prev + g
        rout = rin + (BAND if has_text(ring) else 0)   # sans annotation : une seule paroi, pas d'encart vide
        geo.append((rin, rout))
        prev = rout
    outer = prev
    parts = []
    # du plus extérieur au plus intérieur : chaque cercle masque l'intérieur
    for idx in reversed(range(len(rings))):
        ring, (rin, rout) = rings[idx], geo[idx]
        pad = 0
        parts.append(f'<circle r="{f(rout + HALO + pad)}" class="paper-f"/>')
        parts.append(value(rin, ring["spec"]))
        words = ring["label"].replace("·", " ").split()
        text = " ".join(words if declared else words[1:])
        if rout > rin:
            parts.append(f'<circle r="{f(rin)}" class="ink-s"/><circle r="{f(rout)}" class="ink-s"/>')
        else:
            parts.append(f'<circle r="{f(rin)}" class="ink-s"/>')
        a1, a2 = ring.get("arc", (215, 325))
        parts.append(label_alde(rin, rout, text, [s[0] for s in ring.get("sats", [])]))
    parts.append(f'<circle r="{R0}" class="paper-f"/>')
    # extraction (avant le noyau, pour que les segments partent de sa paroi)
    ext_parts = []
    width = outer + 24
    if extract:
        dx = outer + 52
        for side, ex in zip((-1, 1), extract):
            cx = side * dx
            ext_parts.append(f'<line x1="{f(side*R0)}" y1="0" x2="{f(cx - side*(ex["r"]+BAND))}" y2="0" class="ink-s seg"/>')
        width = dx + 60
    parts += ext_parts
    parts.append(noyau(core))
    # extraits
    if extract:
        dx = outer + 52
        for side, ex in zip((-1, 1), extract):
            cx = side * dx
            rin, rout = ex["r"], ex["r"] + BAND
            g = f'<g transform="translate({f(cx)},0)">'
            g += f'<circle r="{f(rout+HALO)}" class="paper-f"/>' + value(rin, ex["spec"])
            g += f'<circle r="{f(rin)}" class="ink-s"/><circle r="{f(rout)}" class="ink-s"/>'
            g += label_arc((rin + rout) / 2, ex["label"], 215, 325, size=7)
            for deg, spec, lab in ex.get("sats", []):
                sx, sy = pt(rout, deg)
                g += satellite(sx, sy, 21, spec, lab)
            g += "</g>"
            parts.append(g)
    # satellites de la pile
    for ring, (rin, rout) in zip(rings, geo):
        words = ring["label"].replace("·", " ").split()
        has_enc = declared or len(words) > 1
        for deg, spec, *lab in ring.get("sats", []):
            sx, sy = pt((rin + rout) / 2, deg)
            if lab and lab[0]: parts.append(satellite_annot(sx, sy, sat_radius(spec), spec, lab[0]))
            else: parts.append(satellite(sx, sy, sat_radius(spec), spec))
    h = outer + 26
    vb = f"{-width} {-h} {2*width} {2*h}"
    return f'<svg viewBox="{vb}" role="img" xmlns="http://www.w3.org/2000/svg">{"".join(parts)}</svg>'

FULL = [("full", 0, 0)]
EMPTY = []
LOC_SATS = []
AMPLEUR_8 = [("poly", 4, 22.5), ("poly", 4, 67.5)]
IMPACT_6 = [("poly", 3, 90), ("poly", 3, 270)]
LOC_9 = [("poly", 9, 90)]

G = {}
AMP_900_N = [("poly", 4, 45), ("poly", 9, 270), ("poly", 5, 258), ("poly", 5, 282)]
AMP_900_P = [("poly", 4, 45), ("poly", 9, 90), ("poly", 5, 78), ("poly", 5, 102)]
G["feu"] = glyph("neg", [
    dict(label="CIBLE", spec=FULL),
    dict(label="FORME", spec=FULL, sats=[(90, EMPTY)]),
    dict(label="AMPLEUR · DIAMETRE · METRES", spec=[("poly", 9, 270), ("poly", 3, 270)]),
    dict(label="LOCALISATION · METRES · FOIS", spec=[("poly", 5, 270), ("poly", 9, 270)], sats=LOC_SATS),
    dict(label="IMPACT · FEU · FOIS", spec=[("poly", 4, 0), ("poly", 7, 270)]),
])
G["feu_pose"] = glyph("pos", [
    dict(label="FORME", spec=FULL, sats=[(270, EMPTY)]),
    dict(label="AMPLEUR · DIAMETRE · METRES", spec=[("poly", 9, 90), ("poly", 3, 90)]),
    dict(label="LOCALISATION · METRES · FOIS", spec=[("poly", 5, 90), ("poly", 9, 90)], sats=LOC_SATS),
    dict(label="IMPACT · FEU · FOIS", spec=[("poly", 4, 45), ("poly", 7, 90)]),
])
G["soins"] = glyph("pos", [
    dict(label="CIBLE", spec=[("cross", 0, 0)]),
    dict(label="LOCALISATION · METRES", spec=[("cross", 0, 0)], sats=LOC_SATS),
    dict(label="IMPACT · VIE", spec=[("poly", 4, 45), ("poly", 4, 0)]),
])
G["blessure"] = glyph("neg", [
    dict(label="CIBLE", spec=[("poly", 3, 270)]),
    dict(label="LOCALISATION · METRES", spec=[("cross", 0, 45)], sats=LOC_SATS),
    dict(label="IMPACT · VIE", spec=[("poly", 9, 270), ("poly", 5, 270), ("poly", 3, 270)]),
])
G["tp"] = glyph(("hyb", ("feu", "air", "terre", "eau")), [
    dict(label="CIBLE", spec=[("line", 0, 90)]),
    dict(label="LOCALISATION · KILOMETRES · FOIS", spec=[("poly", 9, 0), ("poly", 9, 20)], sats=LOC_SATS),
], r0=50)
G["foulee"] = glyph(("hyb", ("air", "air", "air", "eau")), [
    dict(label="CIBLE", spec=[("line", 0, 90)]),
    dict(label="LOCALISATION · METRES", spec=[("poly", 9, 0)], sats=LOC_SATS),
], r0=50)

if __name__ == "__main__":
    import json, sys
    json.dump(G, open(sys.argv[1], "w"))
