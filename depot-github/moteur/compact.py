"""Allège une page : chaque syllabe d'Alde est dessinée une fois (defs), puis réemployée (<use>) avec une seule matrice."""
import re, math, sys

ALDE = re.compile(r'<g transform="([^"]*)" class="alde">((?:<path[^>]*/>|<circle[^>]*/>|<g transform="[^"]*">(?:<path[^>]*/>|<circle[^>]*/>)*</g>)*)</g>')
TF = re.compile(r'(translate|rotate|scale|skewX)\(([^)]*)\)')
STY = {'class="s"': 'style="fill:none;stroke:var(--ink);stroke-width:7;stroke-linecap:round;stroke-linejoin:round"',
       'class="f"': 'style="fill:var(--ink)"'}

def mul(a, b):
    return (a[0]*b[0] + a[2]*b[1], a[1]*b[0] + a[3]*b[1], a[0]*b[2] + a[2]*b[3], a[1]*b[2] + a[3]*b[3],
            a[0]*b[4] + a[2]*b[5] + a[4], a[1]*b[4] + a[3]*b[5] + a[5])

def matrix(t):
    m = (1, 0, 0, 1, 0, 0)
    for op, args in TF.findall(t):
        v = [float(x) for x in re.split(r"[ ,]+", args.strip())]
        if op == "translate": n = (1, 0, 0, 1, v[0], v[1] if len(v) > 1 else 0)
        elif op == "scale": n = (v[0], 0, 0, v[1] if len(v) > 1 else v[0], 0, 0)
        elif op == "rotate":
            r = math.radians(v[0]); n = (math.cos(r), math.sin(r), -math.sin(r), math.cos(r), 0, 0)
        else: n = (1, 0, math.tan(math.radians(v[0])), 1, 0, 0)
        m = mul(m, n)
    def f(x):
        t = ("%.3f" % x).rstrip("0").rstrip(".")
        t = t.replace("-0.", "-.") if t.startswith("-0.") else (t[1:] if t.startswith("0.") else t)
        return t if t not in ("", "-0", "-") else "0"
    return " ".join(f(x) for x in m)

def compact(html):
    ids = {}
    def sub(mo):
        inner = mo.group(2)
        if inner not in ids: ids[inner] = "y%d" % len(ids)
        return '<use href="#%s" transform="matrix(%s)"/>' % (ids[inner], matrix(mo.group(1)))
    out = ALDE.sub(sub, html)
    if not ids: return html
    defs = "".join('<g id="%s">%s</g>' % (i, re.sub(r'class="[sf]"', lambda c: STY[c.group(0)], k)) for k, i in ids.items())
    sprite = '<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>%s</defs></svg>' % defs
    return out.replace('<div class="wrap">', sprite + '<div class="wrap">', 1)

if __name__ == "__main__":
    for p in sys.argv[1:]:
        h = open(p, encoding="utf-8").read(); c = compact(h); open(p, "w", encoding="utf-8").write(c)
