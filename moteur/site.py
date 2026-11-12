"""Génère la bibliothèque glyphique (site statique) : python3 site.py <dossier de sortie>"""
import sys, os, io, json, html, contextlib, shutil
import os as _os
D = _os.path.dirname(_os.path.abspath(__file__))
DATA = _os.path.join(D, "..", "donnees")
sys.path.insert(0, D)
from compact import compact
import convert as C
from fiches import FICHES
OUT = sys.argv[1] if len(sys.argv) > 1 else _os.path.join(D, "..", "site")
FAM = {"A": "Arcane", "H": "Magie hybride", "R": "Art rare"}
CRIT_FR = {"NOYAU": "noyau", "CIBLE": "cible", "FORME": "forme", "AMPLEUR": "ampleur", "DUREE": "durée", "LOCALISATION": "localisation",
           "CONDITION": "condition", "IMPACT": "impact", "QUANTITE": "quantité", "COMPOSANTE": "composante", "INTERACTION": "interaction", "COSMETIQUE": "cosmétique"}

CSS = """/* Bibliothèque glyphique d'Inarama */
:root { --bg:#E7EAE6; --paper:#F3F5F2; --ink:#1D2327; --muted:#5C676C; --rule:#C3CBC7; --accent:#34586B; --off:#8A9599;
  --f-display:"Alegreya SC",Georgia,serif; --f-body:"Alegreya Sans","Segoe UI",system-ui,sans-serif; --f-mono:"IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { --bg:#121618; --paper:#1A1F22; --ink:#DCE2E1; --muted:#93A0A4; --rule:#333D41; --accent:#8EB4C6; --off:#66737A; color-scheme:dark } }
:root[data-theme="dark"] { --bg:#121618; --paper:#1A1F22; --ink:#DCE2E1; --muted:#93A0A4; --rule:#333D41; --accent:#8EB4C6; --off:#66737A; color-scheme:dark }
* { box-sizing:border-box; }
body { margin:0; background:var(--bg); color:var(--ink); font-family:var(--f-body); font-size:16px; line-height:1.5; }
a { color:var(--accent); }
.wrap { max-width:1240px; margin:0 auto; padding-block:32px 64px; padding-left:max(16px, env(safe-area-inset-left, 0px)); padding-right:max(16px, env(safe-area-inset-right, 0px)); display:grid; gap:32px; min-width:0; }
h1,h2,h3 { font-family:var(--f-display); margin:0; text-wrap:balance; }
h1 { font-size:clamp(2rem,4.5vw,3rem); line-height:1.05; } h2 { font-size:1.5rem; } h3 { font-size:1.15rem; }
p { margin:0; max-width:75ch; }
.eyebrow { font-family:var(--f-mono); font-size:.75rem; letter-spacing:.12em; text-transform:uppercase; color:var(--accent); margin-bottom:8px; }
.lede { color:var(--muted); font-size:1.1rem; margin-top:10px; }
.nav { display:flex; flex-wrap:wrap; justify-content:space-between; gap:8px; font-family:var(--f-mono); font-size:.8rem; }
.nav a { text-decoration:none; }
.chips { display:flex; flex-wrap:wrap; gap:6px; margin-top:12px; }
.chip { font-family:var(--f-mono); font-size:.75rem; border:1px solid var(--rule); background:var(--paper); padding:3px 8px; }
.en { font-family:var(--f-mono); font-size:.85rem; color:var(--muted); margin-top:4px; }
.sec { border-top:2px solid var(--ink); padding-top:14px; display:grid; gap:14px; }
.pair { display:grid; grid-template-columns:1fr 1fr; gap:12px; }
.pair.one { grid-template-columns:1fr; }
figure { margin:0; background:var(--paper); border:1px solid var(--rule); padding:10px; }
figure svg { width:100%; height:auto; display:block; }
figcaption { font-family:var(--f-mono); font-size:.72rem; color:var(--muted); text-align:center; margin-top:4px; }
table { border-collapse:collapse; width:100%; font-size:.92rem; }
th { text-align:left; font-family:var(--f-mono); font-weight:500; font-size:.7rem; letter-spacing:.08em; text-transform:uppercase; color:var(--muted); border-bottom:1px solid var(--ink); padding:6px 8px; }
td { border-bottom:1px solid var(--rule); padding:5px 8px; vertical-align:top; }
td.num { font-family:var(--f-mono); color:var(--accent); width:2.5em; }
.pol span { font-family:var(--f-mono); font-size:.78rem; color:var(--accent); }
ul.notes { margin:0; padding-left:20px; display:grid; gap:6px; }
footer { font-size:.8rem; color:var(--muted); border-top:1px solid var(--rule); padding-top:12px; }
/* index */
.bar { display:grid; gap:10px; background:var(--paper); border:1px solid var(--rule); padding:14px; position:sticky; top:env(safe-area-inset-top, 0px); z-index:2; }
.bar input { font:inherit; padding:8px 10px; border:1px solid var(--rule); background:var(--bg); color:var(--ink); width:100%; }
.bar .row { display:flex; flex-wrap:wrap; gap:6px; align-items:center; }
.bar .lbl { font-family:var(--f-mono); font-size:.72rem; color:var(--muted); min-width:70px; }
.bar button { font-family:var(--f-mono); font-size:.78rem; padding:4px 10px; border:1px solid var(--ink); background:var(--paper); color:var(--ink); cursor:pointer; }
.bar button[aria-pressed="true"] { background:var(--ink); color:var(--paper); }
.count { font-family:var(--f-mono); font-size:.8rem; color:var(--muted); }
.lvl h2 { margin-bottom:6px; }
.list { display:grid; grid-template-columns:repeat(auto-fill,minmax(280px,1fr)); gap:8px; }
.item { display:grid; gap:2px; background:var(--paper); border:1px solid var(--rule); padding:10px 12px; text-decoration:none; color:var(--ink); }
.item:hover { border-color:var(--accent); }
.item b { font-family:var(--f-display); font-size:1.05rem; font-weight:500; }
.item span { font-family:var(--f-mono); font-size:.72rem; color:var(--muted); }
.box { background:var(--paper); border:1px solid var(--rule); border-left:3px solid var(--accent); padding:18px 20px; display:grid; gap:10px; }
.box ol, .box ul { margin:0; padding-left:20px; display:grid; gap:8px; max-width:90ch; }
@media (max-width:760px) { .pair { grid-template-columns:1fr; } }
@media (max-width:600px) { body { font-size:15px; } .wrap { padding-block:14px 48px; gap:22px; } figure { padding:6px; } table { font-size:.85rem; } td, th { padding:5px 4px; } td.num { width:2em; } .nav { font-size:.75rem; } }
/* glyphes */
.ink-s { fill:none; stroke:var(--ink); stroke-width:1.4; } .ink-f { fill:var(--ink); stroke:none; } .paper-f { fill:var(--paper); }
.el { fill:none; stroke:var(--ink); stroke-width:1.7; stroke-linecap:round; stroke-linejoin:round; }
.pk .p { fill:none; stroke:var(--ink); stroke-width:5; stroke-linecap:round; stroke-linejoin:round; } .pk .pf { fill:var(--ink); }
.alde .s { fill:none; stroke:var(--ink); stroke-width:7; stroke-linecap:round; stroke-linejoin:round; } .alde .f { fill:var(--ink); }
.num { stroke-width:1.2; }
.forme { display:grid; gap:20px; border-top:3px double var(--ink); padding-top:18px; }
.forme > .fh h2 { font-size:1.35rem; }
details.lex { background:var(--paper); border:1px solid var(--rule); padding:8px 12px; }
details.lex summary { cursor:pointer; font-family:var(--f-mono); font-size:.8rem; color:var(--accent); }
details.lex table { margin-top:8px; } td.syl { font-family:var(--f-mono); font-size:.8rem; color:var(--muted); }
.aw { height:30px; width:auto; display:block; } .aw .s { stroke-width:6; }
a.chip { text-decoration:none; } .lane { stroke-width:.6; opacity:.7; }
"""
HEAD = """<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Alegreya+SC:wght@500;700&family=Alegreya+Sans:ital,wght@0,400;0,500;0,700;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="{root}style.css"></head><body><div class="wrap">"""
FOOT = """<footer>Données de sorts tirées du System Reference Document 5.1 de Wizards of the Coast LLC, sous licence Creative Commons Attribution 4.0 International. Glyphes, conversions et système d'Inarama : création originale.</footer></div></body></html>"""

import sys as _s
_s.path.insert(0, D)
from alde import a1_syll
def word_svg(w):
    syl = C.GG.LEX[w]; W = 30
    inner = "".join(f'<g transform="translate({i*W},0)">{a1_syll("ink", c, v)}</g>' for i, (c, v) in enumerate(syl))
    return f'<svg viewBox="-6 -64 {len(syl)*W+12} 90" class="aw alde" aria-hidden="true">{inner}</svg>'
def syl_txt(w):
    return " · ".join((c or "") + ("-" if c and v else "") + (v or "") for c, v in C.GG.LEX[w])
def lexique(sp):
    rows = "".join(f"<tr><td>{C.disp(w)}</td><td class='syl'>{syl_txt(w)}</td><td>{word_svg(w)}</td></tr>" for w in C.words_of(sp))
    return (f'<details class="lex"><summary>Les annotations traduites</summary><table><thead><tr><th>Mot</th><th>Syllabes</th><th>En Alde</th></tr></thead>'
            f'<tbody>{rows}</tbody></table></details>')
def lv_name(l): return "Tours de magie" if l == 0 else f"Niveau {l}"
def form_html(sp, n):
    rows = "".join(f"<tr><td class='num'>{r}</td><td>{c}</td><td>{l}</td></tr>" for r, c, l in [("1", "Noyau", sp["verb"])] + sp["rows"])
    pol = ""
    if sp["split"]:
        lum = ", ".join(CRIT_FR[c] for c in sp["split"][0]) or "aucun cercle"
        ten = ", ".join(CRIT_FR[c] for c in sp["split"][1]) or "aucun cercle"
        pol = f'<p class="pol"><span>Lumineux :</span> {lum}<br><span>Ténébreux :</span> {ten}</p>'
    wide = " one" if sp["split"] else ""
    notes = "".join(f"<li>{x}</li>" for x in sp["notes"])
    cap2 = "Non déclarée · seuls les cercles à polarité illisible" if sp["split"] else "Non déclarée"
    cap1 = "Déclarée · tous les cercles classés" if sp["split"] else "Déclarée"
    head = f'<header class="fh" id="forme-{n}"><div class="eyebrow">{sp["label"]}</div><h2>{sp["verb"]}</h2></header>' 
    return f"""<article class="forme">{head}
<section class="sec"><h3>Glyphe circulaire</h3><div class="pair{wide}">
<figure>{sp['svg'][0]}<figcaption>{cap1}</figcaption></figure><figure>{sp['svg'][1]}<figcaption>{cap2}</figcaption></figure></div>{pol}</section>
<section class="sec"><h3>Glyphe en bande</h3><div class="pair one">
<figure>{C.band_svg(sp, True)}<figcaption>{cap1}</figcaption></figure><figure>{C.band_svg(sp, False)}<figcaption>{cap2}</figcaption></figure></div></section>
<section class="sec"><h3>Lecture</h3><table><thead><tr><th>Rang</th><th>Critère</th><th>Lecture</th></tr></thead><tbody>{rows}</tbody></table>
{lexique(sp)}
{('<ul class="notes">' + notes + '</ul>') if notes else ''}</section></article>"""

def page(entry, prev, nxt):
    forms = entry["forms"]; sp = forms[0]
    nav = (f'<nav class="nav"><a href="../index.html">← Bibliothèque</a><span>'
           + (f'<a href="{prev["idx"]}.html">‹ {prev["fr"]}</a>' if prev else "") + " &nbsp; "
           + (f'<a href="{nxt["idx"]}.html">{nxt["fr"]} ›</a>' if nxt else "") + '</span></nav>')
    fams = " · ".join(dict.fromkeys(FAM[f["fam"]] for f in forms))
    chips = "".join(f'<a class="chip" href="#forme-{i}">{f["label"]}</a>' for i, f in enumerate(forms)) if len(forms) > 1 else ""
    return HEAD.format(title=f"{sp['fr']} · Bibliothèque glyphique", root="../") + f"""
{nav}
<header><div class="eyebrow">{lv_name(sp['level'])} · {sp['ecole']} · {fams}</div><h1>{sp['fr']}</h1><p class="en">{sp['en']}</p>
<p class="lede">{sp['dnd']}</p>{('<div class="chips">' + chips + '</div>') if chips else ''}</header>
""" + "".join(form_html(f, i) for i, f in enumerate(forms)) + FOOT

IDX_CSS = """
/* index : lisible sur tout écran */
.idx .wrap { gap:20px; padding-top:20px; }
.bar { gap:8px; padding:10px; }
.bar input { font-size:16px; padding:10px 12px; }
.bar button { min-height:36px; padding:6px 12px; font-size:.8rem; }
details.flt > summary { cursor:pointer; font-family:var(--f-mono); font-size:.78rem; color:var(--accent); list-style:none; display:flex; gap:10px; align-items:center; min-height:32px; }
details.flt > summary span + span { margin-left:auto; }
details.flt > summary::-webkit-details-marker { display:none; }
details.flt > summary::after { content:"＋"; } details.flt[open] > summary::after { content:"－"; }
details.flt .row { margin-top:6px; }
.bar .row { overflow-x:auto; flex-wrap:nowrap; padding-bottom:2px; scrollbar-width:thin; }
.bar .row button { flex:0 0 auto; }
.bar .lbl { flex:0 0 auto; }
.list { grid-template-columns:repeat(auto-fill,minmax(min(100%,300px),1fr)); }
details.sp { background:var(--paper); border:1px solid var(--rule); }
details.sp > summary { list-style:none; cursor:pointer; padding:10px 12px; display:grid; gap:2px; }
details.sp > summary::-webkit-details-marker { display:none; }
details.sp[open] { border-color:var(--accent); grid-column:1/-1; }
details.sp b { font-family:var(--f-display); font-size:1.08rem; font-weight:500; }
details.sp .m { font-family:var(--f-mono); font-size:.72rem; color:var(--muted); }
.spb { padding:0 12px 12px; display:grid; gap:12px; }
.spb .dnd { font-size:.85rem; color:var(--muted); }
.spb .go { font-family:var(--f-mono); font-size:.8rem; }
.fm { border-top:1px solid var(--rule); padding-top:8px; display:grid; gap:6px; }
.fm .lab { font-family:var(--f-mono); font-size:.72rem; letter-spacing:.06em; text-transform:uppercase; color:var(--accent); }
.fm .vb { font-family:var(--f-display); font-size:1rem; }
.rd { display:grid; grid-template-columns:auto 1fr; gap:2px 10px; font-size:.88rem; }
.rd dt { font-family:var(--f-mono); font-size:.72rem; color:var(--muted); padding-top:2px; white-space:nowrap; }
.rd dd { margin:0; overflow-wrap:anywhere; }
@media (max-width:600px) {
  body { font-size:15px; }
  .wrap { padding-block:14px 48px; }
  h1 { font-size:1.9rem; }
  .lede { font-size:1rem; }
  .rd { grid-template-columns:1fr; } .rd dt { padding-top:6px; }
}
"""
SOURCES = {"5.1": "D&D 5e · 2014 (SRD 5.1)", "5.2": "D&D 5e · 2024 (SRD 5.2)", "3.5": "D&D 3.5 (SRD 3.5)", "pf1": "Pathfinder 1"}
def form_source(x):
    d = x["dnd"]
    return "pf1" if d.startswith("Pathfinder 1") else "3.5" if "D&amp;D 3.5" in d else "5.2" if "2024" in d else "5.1"
def index(spells):
    data = []
    for s in spells:
        fs = [dict(b=x["label"], v=x["verb"], r=[[c, l] for _, c, l in x["rows"]]) for x in s["forms"]]
        data.append(dict(i=s["idx"], f=s["fr"], e=s["en"], l=s["level"], c=s["ecole"], m=sorted(set(x["fam"] for x in s["forms"])), o=sorted(set(s["src"]) | set(form_source(x) for x in s["forms"])), d=s["forms"][0]["dnd"], x=fs))
    ecoles = sorted({s["ecole"] for s in spells})
    levels = sorted({s["level"] for s in spells})
    head = HEAD.format(title="Bibliothèque glyphique", root="").replace('<link rel="stylesheet" href="style.css">', f"<style>{CSS}{IDX_CSS}</style>").replace("<body>", '<body class="idx">')
    return head + f"""
<header><div class="eyebrow">Inarama · Arcane et Magie</div><h1>Bibliothèque glyphique</h1>
<p class="lede">Les sorts de D&amp;D (SRD 5.1, 5.2 et 3.5) et de Pathfinder 1 transposés en glyphes d'Inarama. Touchez un sort pour lire chacune de ses formes ; les glyphes eux-mêmes sont sur sa page. <a href="regles.html">Les règles de lecture</a>.</p></header>
<div class="bar">
<input id="q" type="search" placeholder="Chercher un sort (français ou anglais)" aria-label="Chercher un sort">
<details class="flt"><summary><span id="n"></span><span>Filtres</span></summary>
<div class="row"><span class="lbl">Niveau</span>{''.join(f'<button type="button" data-l="{l}" aria-pressed="false">{"TM" if l == 0 else l}</button>' for l in levels)}</div>
<div class="row"><span class="lbl">Famille</span>{''.join(f'<button type="button" data-m="{k}" aria-pressed="false">{v}</button>' for k, v in FAM.items())}</div>
<div class="row"><span class="lbl">Source</span>{''.join(f'<button type="button" data-o="{k}" aria-pressed="false">{v}</button>' for k, v in SOURCES.items())}</div>
<div class="row"><span class="lbl">École</span>{''.join(f'<button type="button" data-c="{e}" aria-pressed="false">{e}</button>' for e in ecoles)}</div>
</details></div>
<div id="out"></div>
<script>
const S = {json.dumps(data, ensure_ascii=False, separators=(",", ":"))};
const FAM = {json.dumps(FAM, ensure_ascii=False)};
const st = {{l:new Set(), m:new Set(), c:new Set(), o:new Set(), q:""}};
const SRC = {{"3.5":"D&D 3.5","5.1":"5e 2014","5.2":"5e 2024","pf1":"Pathfinder 1"}};
const norm = s => s.normalize("NFD").replace(/[\\u0300-\\u036f]/g,"").toLowerCase();
const esc = s => String(s).replace(/&(?!amp;|nbsp;)/g,"&amp;").replace(/</g,"&lt;");
const body = s => `<div class="spb"><p class="dnd">${{s.d}}</p>` + s.x.map(x =>
  `<div class="fm"><div class="lab">${{esc(x.b)}}</div><div class="vb">${{esc(x.v)}}</div><dl class="rd">` +
  x.r.map(r => `<dt>${{esc(r[0])}}</dt><dd>${{esc(r[1])}}</dd>`).join("") + `</dl></div>`).join("") +
  `<a class="go" href="sorts/${{s.i}}.html">Voir les glyphes →</a></div>`;
function draw(){{
  const q = norm(st.q);
  const f = S.filter(s => (!st.l.size||st.l.has(String(s.l))) && (!st.m.size||s.m.some(x=>st.m.has(x))) && (!st.c.size||st.c.has(s.c)) && (!st.o.size||s.o.some(x=>st.o.has(x))) && (!q||norm(s.f+" "+s.e).includes(q)));
  document.getElementById("n").textContent = f.length + " sort" + (f.length>1?"s":"") + " sur " + S.length;
  const by = {{}}; f.forEach(s => (by[s.l] = by[s.l]||[]).push(s));
  document.getElementById("out").innerHTML = Object.keys(by).sort((a,b)=>a-b).map(l =>
    `<section class="lvl sec"><h2>${{l==0?"Tours de magie":"Niveau "+l}}</h2><div class="list">` +
    by[l].sort((a,b)=>a.f.localeCompare(b.f,"fr")).map(s => `<details class="sp" data-i="${{s.i}}"><summary><b>${{s.f}}</b>` +
      `<span class="m">${{s.e}} · ${{s.c}} · ${{s.m.map(x=>FAM[x]).join(" + ")}}${{s.x.length>1?" · "+s.x.length+" formes":""}} · ${{s.o.map(x=>SRC[x]).join(" / ")}}</span></summary></details>`).join("") +
    `</div></section>`).join("");
}}
const BY = Object.fromEntries(S.map(s => [s.i, s]));
document.getElementById("out").addEventListener("toggle", e => {{
  const d = e.target; if (d.open && !d.dataset.done) {{ d.insertAdjacentHTML("beforeend", body(BY[d.dataset.i])); d.dataset.done = 1; }}
}}, true);
document.getElementById("q").addEventListener("input", e => {{ st.q = e.target.value; draw(); }});
document.querySelectorAll(".bar button").forEach(b => b.addEventListener("click", () => {{
  const k = b.dataset.l!==undefined?"l":b.dataset.m!==undefined?"m":b.dataset.o!==undefined?"o":"c"; const v = b.dataset[k];
  const on = b.getAttribute("aria-pressed")!=="true"; b.setAttribute("aria-pressed", on);
  on ? st[k].add(v) : st[k].delete(v); draw(); }}));
if (matchMedia("(min-width:900px)").matches) document.querySelector("details.flt").open = true;
draw();
</script>
""" + FOOT

def regles():
    g = open(DATA + "/grimoire_glyphique.html", encoding="utf-8").read()
    a = g.index('<section class="read">'); b = g.index("</section>", g.index('<section class="box">', a)) + 10
    circ = g[a:b]
    bp = open(DATA + "/glyphes_en_bande.html", encoding="utf-8").read()
    i = bp.index('<section class="box">\n    <h3>Les règles de conversion appliquées</h3>'); j = bp.index("</section>", i) + 10
    band = bp[i:j]
    lib = """<section class="box"><h3>Conversion des sorts de D&amp;D</h3><ul>
<li><b>Famille.</b> Arcane par défaut : un verbe suffit. Magie hybride dès qu'un élément des combinaisons naturelles est en jeu (feu, froid, foudre, tonnerre, acide, poison, eau, plantes, brume…). Arts rares pour le temps et la téléportation. Les sorts déjà tracés dans le grimoire gardent leurs cercles validés, enrichis de ce qui les définit en propre.</li>
<li><b>Combinaison d'un sort hybride.</b> Celle de l'élément en jeu (Feu, Glace, Foudre, Orage, Acide sulfurique, Ammoniac, Plante, Brume…), à défaut celle de l'école.</li>
<li><b>Répartition astrale d'un sort hybride.</b> Le camp de l'école est majoritaire ; cercles minoritaires = nombre de cercles × niveau ÷ 18, arrondi. Sous Hodolin, la minorité ténébreuse prend d'abord ce qui s'impose aux êtres (impact, cible, condition…) ; sous Galombar, la minorité lumineuse prend d'abord ce qui décrit l'espace (localisation, forme, ampleur…).</li>
<li><b>Valeurs.</b> Pieds × 0,3, arrondis au mètre ; 1 mile ≈ 2 km ; dégâts et soins à la moyenne des dés (modificateur +3) ; 1 round = 6 secondes ; 24 heures = 1 jour. Une zone de D&amp;D donne une Forme (sphère, cube, cône, ligne, cylindre) et une Ampleur (diamètre, côté, longueur).</li>
<li><b>Composante.</b> Tracée seulement quand D&amp;D la rend indispensable : coûteuse ou consommée. Son prix s'inscrit dans la forme, ramené au plus petit nombre (10 pièces d'une sorte = 1 de la sorte au-dessus : cuivre, argent, or, platine) ; la matière et le métal de la pièce vont en annotation.</li>
<li><b>Un glyphe, un sort.</b> Deux glyphes strictement identiques sont, par définition, le même sort : tout ce qui distingue un sort s'inscrit dans son glyphe. La construction de la bibliothèque s'arrête si deux sorts différents produisent le même glyphe.</li>
<li><b>Où s'inscrit ce qui distingue un sort.</b> La nature de l'effet dans l'Impact (annotation du cercle, ou satellite annoté pour un aspect à isoler) ; un Impact plein annoté pour un effet total ; ce sur quoi le sort peut être lancé dans la Condition (« ne peut viser qu'un humanoïde ») ; ce que le sort touche en annotation de la Cible (« tous les alliés dans la zone ») ; les fins anticipées en annotation de la Durée ; les seuils (points de vie, niveau de sort) dans un satellite annoté et chiffré.</li>
<li><b>Deux éditions de D&amp;D.</b> Les sorts viennent du SRD 5.1 (règles de 2014) et du SRD 5.2 (règles de 2024). Une révision de 2024 qui change le glyphe devient une forme « version 2024 » sur la page du sort ; une révision qui ne le change pas est le même sort et n'ajoute rien. Quand les deux versions n'ont plus rien en commun, la version de 2024 a sa propre entrée.</li>
<li><b>Une forme par option.</b> Quand un sort laisse choisir l'effet ou la géométrie au lancement, chaque option est un glyphe à part, et la bibliothèque les montre toutes.</li>
<li><b>Êtres invoqués.</b> L'Impact dit l'être (sa nature) et sa puissance (son intensité), alignée pour l'instant sur le facteur de puissance de D&amp;D ; le nombre d'êtres en satellite.</li>
<li><b>Jets de sauvegarde.</b> Non inscrits : leur difficulté dépend de l'incantateur, non du sort.</li>
<li><b>D&amp;D 3.5.</b> Les sorts du SRD 3.5 entrent école par école. Le lanceur de référence est le plus petit lanceur capable du sort : portées, durées et nombres de cibles « par niveau » se calculent à son niveau. Un sort commun dont le glyphe change devient une forme « version 3.5 » ; les sorts propres à la 3.5 ont leur entrée.</li>
<li><b>Dés de vie.</b> Comme les dégâts, ils se ramènent à une valeur fixe : un dé de vie vaut 4,5 points de vie (un d8), arrondi à l'entier. Réserves et seuils s'écrivent donc en « vie », comme en 5e.</li>
<li><b>L'alignement transposé.</b> Inarama n'a pas de balance morale universelle : ce qui est bon à Galombar ne l'est pas à Hodolin. Le système d'alignement est écarté, pas les sorts. Bien et mal deviennent la bienveillance et l'hostilité envers le lanceur (Cible allié, Cible ennemi) ; loi et chaos deviennent l'énergie astrale lumineuse de l'Étoile et ténébreuse de l'Abysse, et ce qui en est chargé. Un sort « contre » l'alignement est un seul sort en trois formes : contre l'hostile, contre le lumineux, contre le ténébreux.</li>
<li><b>Probabilités.</b> Une chance s'écrit en fraction, comme les êtres invoqués : 1 annoté « moitié », « quart », « cinquième »… plutôt qu'un pourcentage.</li>
<li><b>Coût en expérience.</b> Quand un sort de la 3.5 coûte de l'expérience, le lanceur paie de sa propre substance : une Composante annotée « vie ». Un niveau d'expérience vaut un dé de vie, soit 4,5 points de vie ; moins d'un point s'écrit 1 « vie », un point ou plus s'écrit en « vie durable », retirée pour de bon.</li>
<li><b>Échelons.</b> Des variantes qui ne diffèrent que par les chiffres (intensité, quantité, seuil) sont un même sort : une page, une forme par échelon (Soins mineurs à intensifs, Convocation de monstres I à IX…). Quand l'effet change, la variante a sa propre entrée.</li>
<li><b>Êtres convoqués de la 3.5.</b> Le rang de la liste se convertit en facteur de puissance, sur l'échelle de la 5e : I = ½, II = 1, III = 2, IV = 4, V = 5, VI = 7, VII = 9, VIII = 11, IX = 12 (puissance de la meilleure créature de chaque liste, estimée). Les créatures célestes et fiélonnes deviennent des êtres chargés d'énergie lumineuse ou ténébreuse.</li>
<li><b>Plans de l'Ombre et de la Lumière.</b> Ils se transposent en hémisphères ténébreux et lumineux ; leur énergie est l'énergie astrale. Un sort lié à l'une des deux énergies a toujours sa forme réciproque, car l'une n'existe pas sans l'autre : les sorts d'ombre de la 3.5, renommés « astraux » (Invocation astrale, Évocation astrale, Traversée astrale), ont une forme lumineuse et une forme ténébreuse, avec la part de réalité en cinquièmes.</li>
<li><b>Matière et expérience.</b> Quand un sort coûte à la fois une matière et de l'expérience, la matière garde la valeur de la Composante et la vie payée devient un satellite annoté « vie ».</li>
<li><b>Énergie positive et négative.</b> Elles s'écrivent « vie » et « nécrose », non lumineux et ténébreux : on soigne et on blesse dans les deux hémisphères. Un niveau perdu vaut un dé de vie, soit 4,5 points de vie, « durable » quand la perte peut devenir définitive.</li>
<li><b>Grimoire et éditions.</b> Un sort du grimoire se traite comme les autres : son glyphe validé reste la forme de référence, et ses versions 2024 ou 3.5 prennent leur durée, leur portée et leur nombre de cibles dans leurs propres données ; options et échelons s'y ajoutent de même.</li>
<li><b>Emplacement de sort.</b> Un sort qui stocke, reproduit, imite ou prolonge un autre sort (Souhait, Miracle, Glyphe de sort, Contingence…) porte sur l'Impact un satellite vide annoté « sort » : il reçoit au lancement le glyphe du sort concerné.</li>
<li><b>Plusieurs satellites.</b> Sur le cercle, ils se répartissent symétriquement (opposés, à 120°, en croix) ; sur la bande, ils se centrent de part et d'autre du milieu, à intervalles égaux.</li>
<li><b>Portée nulle.</b> Un sort qui naît là où se tient le lanceur n'a pas d'anneau de Localisation : le vide.</li>
<li><b>Concentration sans terme.</b> Une durée qui tient tant que dure la concentration, sans maximum, est pleine : infinie.</li>
<li><b>Unités.</b> Mètres, kilogrammes et litres, en attendant les unités propres aux peuples d'Inarama.</li>
<li><b>Les sorts divins sont de l'Arcane.</b> Dans Inarama, la religion passe par une magie très académique, et ses grands praticiens deviennent des figures de culte : les sorts de clerc s'écrivent en glyphes arcaniques, la lumière radiante comme médium.</li>
<li><b>Plusieurs formes pour un même sort.</b> Un sort peut s'inscrire en Arcane et en Magie hybride : les deux pratiques l'écrivent différemment, et la bibliothèque montre toutes les formes connues.</li>
<li><b>Valeurs trop longues.</b> Une valeur qui demanderait plus de quatre formes est arrondie à la plus proche qui s'écrit simplement ; la lecture le signale.</li>
<li><b>Pathfinder 1.</b> Seuls les sorts légaux en Pathfinder Society sont repris. Le lanceur de référence est de niveau 2L−1 pour les classes à neuf niveaux de sorts, 3L−2 pour celles à six niveaux, le paladin et le rôdeur. Un nom propre du monde de Golarion s'efface et le sort garde son sens ; un sort dont l'effet dépend de ce monde, ou qui n'est qu'une mécanique de jeu (jets de dés, actions, dons, pouvoirs de classe), est écarté. Sont aussi écartés les sorts qui ne servent qu'aux armes à feu, ou qui supposent d'autres mondes : Inarama n'a ni l'un ni l'autre. Une mécanique de jeu dans un sort gardé se transpose par son esprit, sans vocabulaire de jeu.</li>
<li><b>Souhait</b> se trace comme Miracle : un Impact plein « souhait », et le niveau maximal des sorts qu'il reproduit en satellite de seuil.</li>
<li><b>Annotations.</b> Mots français transcrits en Alde, en attendant le lexique propre.</li></ul></section>"""
    return HEAD.format(title="Règles · Bibliothèque glyphique", root="") + """
<nav class="nav"><a href="index.html">← Bibliothèque</a></nav>
<header><div class="eyebrow">Bibliothèque glyphique</div><h1>Règles de lecture</h1></header>
<section class="sec"><h2>Le glyphe circulaire</h2>""" + circ + """</section>
<section class="sec"><h2>Le glyphe en bande</h2>""" + band + """</section>
<section class="sec"><h2>De D&amp;D à Inarama</h2>""" + lib + "</section>" + FOOT

if __name__ == "__main__":
    os.makedirs(OUT + "/sorts", exist_ok=True)
    spells = []
    for k, f in FICHES.items():
        forms = C.build_forms(k, f)
        spells.append(dict(idx=k, fr=f["fr"], en=forms[0]["en"], level=forms[0]["level"], ecole=forms[0]["ecole"], forms=forms, src=C.sources_of(k, f)))
    spells.sort(key=lambda s: (s["level"], s["fr"]))
    # contrôle d'unicité : deux glyphes strictement identiques sont, par définition, le même sort
    seen, dups = {}, []
    for sp in spells:
        for fm in sp["forms"]:
            key = (repr(fm["core"]), repr([(r[0], r[1], tuple(r[2]), repr(r[4:5])) for r in fm["rings"]]), repr(fm["split"]))
            if key in seen: dups.append((seen[key][1], f'{sp["fr"]} [{fm["label"]}]'))
            else: seen.setdefault(key, (sp["idx"], f'{sp["fr"]} [{fm["label"]}]'))
    if dups:
        print(f"ATTENTION : {len(dups)} glyphe(s) en double")
        for a_, b_ in dups: print("   ", a_, "=", b_)
        if os.environ.get("STRICT"): raise SystemExit("construction arrêtée : glyphes en double")
    for i, sp in enumerate(spells):
        prev = spells[i - 1] if i else None; nxt = spells[i + 1] if i + 1 < len(spells) else None
        open(f"{OUT}/sorts/{sp['idx']}.html", "w", encoding="utf-8").write(compact(page(sp, prev, nxt)))
    open(OUT + "/index.html", "w", encoding="utf-8").write(index(spells))
    open(OUT + "/regles.html", "w", encoding="utf-8").write(regles())
    open(OUT + "/style.css", "w", encoding="utf-8").write(CSS)
    print(len(spells), "sorts")
