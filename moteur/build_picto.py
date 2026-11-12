import math

def spiral_circle():
    pts = []
    R = 30
    turns = 2.0
    a0 = 180
    for i in range(161):
        t = i / 160
        a = math.radians(a0 + 360 * turns * t)
        r = 3 + (R - 3) * t
        pts.append((r * math.cos(a), r * math.sin(a)))
    for i in range(1, 91):
        a = math.radians(a0 + 360 * turns + 4 * i)
        pts.append((R * math.cos(a), R * math.sin(a)))
    return '<path d="M' + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + '" class="p"/>'

def arcpt(r, deg):
    a = math.radians(deg)
    return r * math.cos(a), r * math.sin(a)

def ouroboros():
    R = 27
    x1, y1 = arcpt(R, -34)
    x2, y2 = arcpt(R, -56)
    hx, hy = arcpt(R, -45)
    return (f'<path d="M{x1:.1f},{y1:.1f} A{R} {R} 0 1 1 {x2:.1f},{y2:.1f}" class="p"/>'
            f'<ellipse cx="{hx:.1f}" cy="{hy:.1f}" rx="13" ry="8.5" transform="rotate(45 {hx:.1f} {hy:.1f})" class="pf"/>')

def indra():
    R = 30; out = [f'<circle r="{R}" class="p"/>']
    for c in (-12, 12):
        for sgn in (1, -1):
            A = 2; B = 2 * sgn * c; C = c * c - R * R
            d = math.sqrt(B * B - 4 * A * C)
            xa = (-B - d) / (2 * A); xb = (-B + d) / (2 * A)
            out.append(f'<line x1="{xa:.1f}" y1="{sgn*xa+c:.1f}" x2="{xb:.1f}" y2="{sgn*xb+c:.1f}" class="p"/>')
    for x, y in ((0, 12), (0, -12), (12, 0), (-12, 0)):
        out.append(f'<circle cx="{x}" cy="{y}" r="4" class="pf"/>')
    return "".join(out)

P = {}
P["existence"] = '<path d="M0,0 L0,26 A26 26 0 1 1 14.9,21.3" class="p"/><circle r="5.5" class="pf"/>'
P["nature"] = ouroboros()
P["visibilite"] = '<path d="M0,-32 A34 34 0 0 1 0,32 A34 34 0 0 1 0,-32Z" class="p"/>'
P["mouvement"] = spiral_circle()
P["relation"] = '<circle cx="-15" cy="0" r="15" class="p"/><circle cx="15" cy="0" r="15" class="p"/>'
P["intensite"] = '<path d="M0,-36 L-17,-18 L0,0 L17,-18Z M0,36 L-17,18 L0,0 L17,18Z" class="p"/>'
q = 22 / math.sqrt(2)
P["force"] = '<path d="M-22,-32 Q22,0 -22,32 M22,-32 Q-22,0 22,32" class="p"/>'
P["flux"] = (f'<circle r="22" class="p"/><circle r="6" class="p"/>'
             + "".join(f'<line x1="{sx*q:.1f}" y1="{sy*q:.1f}" x2="{sx*6/math.sqrt(2):.1f}" y2="{sy*6/math.sqrt(2):.1f}" class="p"/>' for sx in (1, -1) for sy in (1, -1))
             + f'<path d="M{-q:.1f},{-q:.1f} L-38,0 L{-q:.1f},{q:.1f} M{q:.1f},{-q:.1f} L38,0 L{q:.1f},{q:.1f}" class="p"/>')
P["qualite"] = '<path d="M-22,-34 Q-20,-14 0,-13 Q20,-14 22,-34 M0,-36 L0,-5 M0,5 L0,13 M0,13 L-22,34 M0,13 L22,34" class="p"/>'
P["identite"] = '<circle r="26" class="p"/><path d="M-35,0 L-26,0 A13 13 0 0 1 0,0 A13 13 0 0 0 26,0 L35,0" class="p"/>'
P["trame"] = indra()
P["ordre"] = ('<rect x="-20" y="-24" width="40" height="34" class="p"/>'
              '<path d="M-29,-13 L29,-13 M-29,-2 L29,-2 M0,-24 L0,-34 M-8,10 L-8,35 M8,10 L8,35 M-24,16 Q-22,36 0,38 Q22,36 24,16" class="p"/>')

ITEMS = [
 ("existence", "1", "Existence", "Créer / Détruire", "I", "Cupule à sillon",
  "Un anneau presque complet, laissé ouvert juste avant le sillon qui le relie à la cupule centrale. Le tracé part de la cupule, descend par le sillon puis fait le tour de l'anneau.",
  "Un seul tenant ✓. Le sillon court vers l'intérieur et non vers l'extérieur, sinon il faudrait lever l'outil."),
 ("nature", "2", "Nature", "Transformer / Préserver", "I", "Ouroboros",
  "Un anneau dont une extrémité devient la tête et l'autre entre dans sa gueule.",
  "Un seul tenant ✓. La queue disparaît dans la tête : aucun écart visible, sinon l'anneau se lirait comme un trait interrompu, donc groupe III."),
 ("visibilite", "3", "Visibilité", "Révéler / Dissimuler", "I", "Mandorle",
  "L'amande seule, deux arcs fermés en un trait.",
  "Un seul tenant ✓. Déjà réduite au minimum."),
 ("mouvement", "4", "Mouvement", "Déplacer / Ancrer", "I", "Spirale (ton dessin)",
  "La spirale part du centre et son dernier tour devient le cercle extérieur, comme sur ton dessin.",
  "Un seul tenant ✓. Le cercle extérieur reste en retrait de la paroi du noyau, pour ne pas s'y fondre en réserve."),
 ("relation", "5", "Relation", "Lier / Séparer", "II", "Deux anneaux tangents",
  "Deux cercles égaux qui se touchent en un point.",
  "Jonction ✓."),
 ("intensite", "6", "Intensité", "Amplifier / Réduire", "II", "Ton dessin, réduit",
  "Deux losanges superposés. Leurs moitiés extérieures pointent vers le dehors (amplifier), leurs moitiés intérieures vers le centre (réduire).",
  "Jonction ✓ : les deux losanges se touchent par la pointe. Le X qui se forme au point de contact appartient à la jonction, principe même du groupe II."),
 ("force", "7", "Force directionnelle", "Attirer / Repousser", "II", "Deux courbes dos à dos",
  "Deux arcs dont les dos se touchent au centre.",
  "Jonction ✓. Les courbes sont tangentes : elles se touchent sans se croiser."),
 ("flux", "8", "Flux énergétique", "Absorber / Émettre", "II", "Ton dessin",
  "Le cercle et les deux pointes latérales sont gardés. Le X devient quatre rayons qui aboutissent à un petit anneau central.",
  "Jonction ✓. Les rayons convergent sans se traverser, ce qui garde ton sens : l'énergie qui afflue au centre ou en part."),
 ("qualite", "9", "Qualité", "Purifier / Corrompre", "III", "Lotus rompu",
  "En haut, la fleur : une fourche à trois branches. En bas, les racines : un Y renversé à branches droites, de même taille. Entre les deux, la tige rompue.",
  "Rupture ✓ sur la tige. Le pétale central est un trait et non une amande, pour ne pas rappeler la mandorle."),
 ("identite", "10", "Identité", "Fusionner / Scinder", "III", "Taijitu dépouillé, couché",
  "Le cercle et le S couché, sans les points. Le S dépasse le cercle des deux côtés.",
  "Rupture ✓ : le S franchit le cercle. S'il s'arrêtait sur le cercle, ce serait une jonction, donc groupe II."),
 ("trame", "11", "Trame", "Invoquer / Bannir", "III", "Filet d'Indra allégé",
  "Deux lignes dans chaque sens, et quatre joyaux aux croisements.",
  "Croisements ✓."),
 ("ordre", "12", "Ordre", "Stabiliser / Déstabiliser", "III", "Djed (ton dessin)",
  "Ton cadre, ta tige et ton socle. Les deux barres débordent du cadre de chaque côté.",
  "Rupture ✓ : les barres franchissent le cadre. Arrêtées sur le cadre, ce seraient des jonctions en T, donc groupe II."),
]

# La polarité se lit dans l'orientation du pictogramme, plus dans le remplissage du cercle
POS_T = {"trame": "rotate(45)"}
NEG_T = {"existence": "rotate(180)", "nature": "rotate(180)", "qualite": "rotate(180)", "ordre": "rotate(180)",
         "visibilite": "rotate(90)", "relation": "rotate(90)", "intensite": "rotate(90)", "force": "rotate(90)",
         "flux": "rotate(90)", "identite": "rotate(90)", "mouvement": "scale(-1,1)", "trame": ""}
NEG_TXT = {"existence": "demi-tour", "nature": "demi-tour", "qualite": "demi-tour", "ordre": "demi-tour",
           "visibilite": "quart de tour", "relation": "quart de tour", "intensite": "quart de tour", "force": "quart de tour",
           "flux": "quart de tour", "identite": "quart de tour", "mouvement": "symétrie : la spirale tourne vers la gauche",
           "trame": "le filet passe de + à ×"}
def picto(key, neg=False):
    t = NEG_T[key] if neg else POS_T.get(key, "")
    return f'<g transform="{t}">{P[key]}</g>'

def noyau(key, neg=False, cls="big"):
    c = "neg" if neg else "pos"
    return (f'<svg viewBox="-50 -50 100 100" class="{cls} {c}" aria-hidden="true">'
            f'<circle r="46" class="disc"/>{picto(key, neg)}</svg>')

grid_pos = "".join(f'<figure>{noyau(k, False, "g")}<figcaption>{n} {nom}</figcaption></figure>' for k, n, nom, *_ in ITEMS)
grid_neg = "".join(f'<figure>{noyau(k, True, "g")}<figcaption>{n} {nom}</figcaption></figure>' for k, n, nom, *_ in ITEMS)
small = "".join(f'{noyau(k, False, "xs")}{noyau(k, True, "xs")}' for k, *_ in ITEMS)

cards = ""
for k, n, nom, poles, grp, src, red, chk in ITEMS:
    cards += f'''<article class="card">
  <div class="pair">{noyau(k)}{noyau(k, True)}</div>
  <div class="txt">
    <p class="kicker">{n} · groupe {grp} · négatif : {NEG_TXT[k]}</p>
    <h3>{nom}</h3>
    <p class="poles">{poles}</p>
    <p><b>Source :</b> {src}</p>
    <p><b>Réduction :</b> {red}</p>
    <p><b>Construction :</b> {chk}</p>
  </div>
</article>'''

page = f'''<title>Pictogrammes du noyau</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Alegreya+SC:wght@500;700&family=Alegreya+Sans:ital,wght@0,400;0,500;0,700;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* Banc d'essai : les douze en grille, puis une fiche par pictogramme */
:root {{
  --bg: #E7EAE6; --paper: #F3F5F2; --ink: #1D2327; --muted: #5C676C; --rule: #C3CBC7; --accent: #34586B;
  --f-display: "Alegreya SC", Georgia, serif; --f-body: "Alegreya Sans", "Segoe UI", system-ui, sans-serif; --f-mono: "IBM Plex Mono", ui-monospace, Menlo, monospace;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg: #121618; --paper: #1A1F22; --ink: #DCE2E1; --muted: #93A0A4; --rule: #333D41; --accent: #8EB4C6; color-scheme: dark }} }}
:root[data-theme="dark"] {{
  --bg: #121618; --paper: #1A1F22; --ink: #DCE2E1; --muted: #93A0A4; --rule: #333D41; --accent: #8EB4C6; color-scheme: dark }}
body {{ background: var(--bg); color: var(--ink); font-family: var(--f-body); font-size: 16px; line-height: 1.5; }}
.wrap {{ max-width: 1180px; margin: 0 auto; padding-block: 40px 64px;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); display: grid; gap: 36px; }}
h1, h2, h3 {{ font-family: var(--f-display); margin: 0; text-wrap: balance; }}
h1 {{ font-size: clamp(2rem, 4.5vw, 3rem); line-height: 1.05; }}
h2 {{ font-size: 1.6rem; }}
h3 {{ font-size: 1.3rem; }}
p {{ margin: 0; max-width: 68ch; }}
.eyebrow, .kicker {{ font-family: var(--f-mono); font-size: .75rem; letter-spacing: .12em; text-transform: uppercase; color: var(--accent); }}
.eyebrow {{ margin-bottom: 8px; }}
.lede {{ color: var(--muted); font-size: 1.1rem; margin-top: 10px; }}
.poles {{ font-family: var(--f-mono); font-size: .85rem; color: var(--accent); }}
section {{ display: grid; gap: 14px; }}
.grid {{ display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 12px; background: var(--paper); border: 1px solid var(--rule); padding: 18px; }}
.grid figure {{ margin: 0; display: grid; gap: 4px; justify-items: center; text-align: center; }}
.grid figcaption {{ font-family: var(--f-mono); font-size: .7rem; color: var(--muted); }}
.g {{ width: 100%; max-width: 110px; height: auto; }}
.xsrow {{ display: flex; flex-wrap: wrap; gap: 6px; align-items: center; background: var(--paper); border: 1px solid var(--rule); padding: 14px; }}
.xs {{ width: 26px; height: 26px; }}
.cards {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr)); gap: 14px; }}
.card {{ background: var(--paper); border: 1px solid var(--rule); padding: 16px; display: grid; gap: 12px; align-content: start; }}
.pair {{ display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }}
.big {{ width: 100%; height: auto; max-width: 150px; justify-self: center; }}
.txt {{ display: grid; gap: 6px; min-width: 0; font-size: .95rem; }}
.box {{ background: var(--paper); border: 1px solid var(--rule); border-left: 3px solid var(--accent); padding: 22px 24px; display: grid; gap: 10px; }}
.box ol {{ margin: 0; padding-left: 20px; display: grid; gap: 8px; max-width: 85ch; }}
/* noyau : positif = cercle vide, pictogramme plein ; négatif = cercle plein, pictogramme en réserve */
.disc {{ fill: var(--paper); stroke: var(--ink); stroke-width: 2.5; }}

.p {{ fill: none; stroke-width: 5; stroke-linecap: round; stroke-linejoin: round; }}
.p {{ stroke: var(--ink); }}
.pf {{ fill: var(--ink); }}
.xs .p {{ stroke-width: 6; }}
@media (max-width: 760px) {{ .grid {{ grid-template-columns: repeat(3, minmax(0, 1fr)); }} }}
</style>
<div class="wrap">
  <header>
    <div class="eyebrow">Arcane · noyau · méthode D, premier jet</div>
    <h1>Pictogrammes du noyau</h1>
    <p class="lede">Les douze symboles retenus, réduits à quelques traits et mis à l'épreuve dans le noyau. Chaque pictogramme est montré dans ses deux polarités. La polarité se lit dans l'orientation : demi-tour pour les pictogrammes asymétriques, quart de tour pour les symétriques, symétrie pour la spirale, + ou × pour le filet.</p>
  </header>

  <section>
    <h2>Positif</h2>
    <div class="grid">{grid_pos}</div>
  </section>
  <section>
    <h2>Négatif</h2>
    <div class="grid">{grid_neg}</div>
  </section>
  <section>
    <h2>Test en petit</h2>
    <p style="color:var(--muted)">Les douze, dans l'ordre, à la taille d'un noyau dans un glyphe chargé. C'est ici qu'on voit ce qui se confond.</p>
    <div class="xsrow">{small}</div>
  </section>

  <section>
    <h2>Fiches</h2>
    <div class="cards">{cards}</div>
  </section>

  <section class="box">
    <h3>À regarder en priorité</h3>
    <ol>
      <li><b>Le groupe I est entièrement circulaire.</b> La cupule, l'ouroboros et la spirale reposent tous les trois sur un anneau. Le test en petit dira s'ils restent distincts.</li>
      <li><b>Le Flux garde son petit anneau central</b>, seule façon que j'ai trouvée de transformer le X en jonction. L'Intensité se fait sans anneau : deux losanges pointe contre pointe.</li>
      <li><b>Les dessins sont des réductions de travail, pas des tracés définitifs.</b> Les proportions et l'épaisseur restent à régler une fois les formes validées.</li>
    </ol>
  </section>
</div>'''
if __name__ == "__main__":
    open("pictogrammes_noyau.html", "w", encoding="utf-8").write(page)
    print(len(page))
