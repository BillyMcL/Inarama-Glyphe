"""Allège une page : chaque syllabe d'Alde est dessinée une fois (defs), puis réemployée (<use>) avec une seule matrice."""
import re, math, sys, json, gzip, base64

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

REGISTRE = {}       # e1 : syllabes communes à tout le site (même identifiant d'une page à l'autre)


def compact(html, partage=False):
    """partage=True (e1) : les identifiants des syllabes sont communs à tout le site ; la page ne porte pas leurs dessins,
    elle charge le fichier commun alde.js (voir sprite_js)"""
    ids = REGISTRE if partage else {}
    def sub(mo):
        inner = mo.group(2)
        if inner not in ids: ids[inner] = "y%d" % len(ids)
        return '<use href="#%s" transform="matrix(%s)"/>' % (ids[inner], matrix(mo.group(1)))
    out = ALDE.sub(sub, html)
    if partage:
        return out.replace('<div class="wrap">', '<script src="../alde.js"></script><div class="wrap">', 1) if out != html else html
    if not ids: return html
    defs = "".join('<g id="%s">%s</g>' % (i, re.sub(r'class="[sf]"', lambda c: STY[c.group(0)], k)) for k, i in ids.items())
    sprite = '<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>%s</defs></svg>' % defs
    return out.replace('<div class="wrap">', sprite + '<div class="wrap">', 1)

def sprite_js():
    """e1 : le fichier commun des syllabes ; chargé par chaque page, il pose les dessins des syllabes dans la page (même
    élément <svg><defs> qu'avant, mais pour tout le site), là où les dessins les réemploient par <use>"""
    defs = "".join('<g id="%s">%s</g>' % (i, re.sub(r'class="[sf]"', lambda c: STY[c.group(0)], k)) for k, i in REGISTRE.items())
    sprite = '<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>%s</defs></svg>' % defs
    return "document.currentScript.insertAdjacentHTML('afterend'," + json.dumps(sprite, ensure_ascii=False) + ");\n"


# f2 : les quatre dessins de chaque forme rangés compressés dans la page (gzip puis base64), décompressés par le navigateur
FIG_SVG = re.compile(r'<figure>(<svg viewBox="[^"]*"[^>]*>.*?</svg>)(?=<figcaption>)', re.S)
NOSCRIPT = ('<noscript><p class="sans-js">Les dessins de cette page s’affichent avec JavaScript, qui est désactivé dans '
            'votre navigateur. Les lectures, les notes et les légendes restent lisibles.</p></noscript>')
ECHEC = "Ce dessin n’a pas pu s’afficher dans ce navigateur."
DECOMPRESSE = ("<script>(()=>{const L=[...document.querySelectorAll('svg[data-gz]')],vus=new Set();"
               "const echec=s=>{s.outerHTML='<p class=\"echec\">" + ECHEC + "</p>'};"
               "const un=async s=>{try{const b=Uint8Array.from(atob(s.dataset.gz),c=>c.charCodeAt(0));"
               "s.outerHTML=await new Response(new Blob([b]).stream().pipeThrough(new DecompressionStream('gzip'))).text()}catch(e){echec(s)}};"
               "const va=s=>{if(!vus.has(s)){vus.add(s);if(io)io.unobserve(s);un(s)}};"
               "if(!('DecompressionStream' in window)){L.forEach(echec);return}"
               # d'abord ce qui est à l'écran (et un peu au-delà), puis le reste par petits paquets
               "const io='IntersectionObserver' in window?new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)va(e.target)}),{rootMargin:'800px'}):null;"
               "if(io)L.forEach(s=>io.observe(s));let i=0;"
               "const suite=()=>{const t0=performance.now();while(i<L.length&&performance.now()-t0<25)va(L[i++]);if(i<L.length)setTimeout(suite,0)};"
               "setTimeout(suite,io?150:0)})();</script>")


def ranger(html):
    """f2 : chaque dessin d'une figure est remplacé par un <svg> vide de même viewBox (la place reste réservée), qui porte
    le dessin compressé ; le script le décompresse et remet à sa place le SVG du moteur, octet pour octet"""
    def sub(mo):
        svg = mo.group(1); tag = re.match(r"<svg[^>]*>", svg).group(0)
        b = base64.b64encode(gzip.compress(svg.encode("utf-8"), 9, mtime=0)).decode("ascii")
        return "<figure>" + tag[:-1] + ' data-gz="' + b + '"></svg>'
    out = FIG_SVG.sub(sub, html)
    if out == html: return html
    out = out.replace('<div class="wrap">', '<div class="wrap">' + NOSCRIPT, 1)
    return out.replace("</body>", DECOMPRESSE + "</body>", 1)


if __name__ == "__main__":
    for p in sys.argv[1:]:
        h = open(p, encoding="utf-8").read(); c = compact(h); open(p, "w", encoding="utf-8").write(c)
