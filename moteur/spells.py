import sys, itertools
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import gen_glyphs as GG

# ---------------- lexique (mots français transcrits en Alde, en attendant le lexique propre) ----------------
VOW = set("aeiou")
WORDS = {
 "CIBLE": "s i b l", "FORME": "f o r m", "AMPLEUR": "a m p l e r", "DUREE": "d u r e",
 "LOCALISATION": "l o k a l i s a s i o n", "CONDITION": "k o n d i s i o n", "IMPACT": "i m p a k t",
 "QUANTITE": "k a n t i t e", "COMPOSANTE": "k o m p o s a n t", "COSMETIQUE": "k o s m e t i k",
 "METRES": "m e t r", "KILOMETRES": "k i l o m e t r", "MINUTES": "m i n u t", "HEURES": "e r",
 "JOURS": "y u r", "SECONDES": "s e g o n d", "DIAMETRE": "d i a m e t r", "LONGUEUR": "l o ng e r",
 "COTE": "k o t e", "FOIS": "f w a",
 "FEU": "f e", "FOUDRE": "f u d r", "TONNERRE": "t o n e r", "VIE": "v i", "TAILLE": "t a y",
 "MALADIE": "m a l a d i", "PIERRE": "p y e r", "BETE": "b e t", "IMAGE": "i m a g", "GARDE": "g a r d",
 "SEL": "s e l", "COQUILLES": "k o k i y", "ENCENS": "a n s a n", "VERRE": "v e r", "CONSOMME": "k o n s o m e",
 "CORPS": "k o r", "OS": "o s", "COUP": "k u", "ESPRIT": "e s p r i",
 "NOYAU": "n o y o", "ACIER": "a s y e", "PLASMA": "p l a s m a", "AIR": "e r", "POLLEN": "p o l e n",
 "ROCHE": "r o s", "ECLAIR": "e k l e r", "SANG": "s a n",
 "ABJURATION": "a b y u r a s i o n", "DIVINATION": "d i v i n a s i o n", "ILLUSION": "i l u s i o n",
 "INVOCATION": "i n v o k a s i o n", "ENCHANTEMENT": "a n s a n t m a n", "TRANSMUTATION": "t r a n s m u t a s i o n",
 "EVOCATION": "e v o k a s i o n", "NECROMANCIE": "n e k r o m a n s i",
 "INTERACTION": "i n t e r a k s i o n", "CHRONOMANCIE": "k r o n o m a n s i", "SPATIOMANCIE": "s p a s i o m a n s i",
 "TEMPS": "t a n", "REGARD": "r e g a r", "MOT": "m o", "VERROU": "v e r u", "NECROSE": "n e k r o s",
 "MERCURE": "m e r k u r", "PHOSPHORE": "f o s f o r", "DIAMANT": "d i a m a n", "OPALE": "o p a l",
 "LUEUR": "l u e r", "TRACE": "t r a s",
}
def syll(phon):
    t = phon.split(); out = []; i = 0
    while i < len(t):
        if t[i] in VOW: out.append((None, t[i])); i += 1
        elif i + 1 < len(t) and t[i + 1] in VOW: out.append((t[i], t[i + 1])); i += 2
        else: out.append((t[i], None)); i += 1
    return out
for w, ph in WORDS.items():
    GG.LEX[w] = syll(ph)

# ---------------- valeurs → formes ----------------
PRIM = {1: "line", 2: "cross", 3: 3, 4: 4, 5: 5, 7: 7, 9: 9}
POS = {"up": True, "down": False}
def form(p, pol, k=0):
    """p : valeur primitive ; pol : "up" (Hodolin, positif) ou "down" (Galombar, négatif) ; k : indice de copie"""
    pos = POS[pol] ^ (k % 2 == 1)          # une seconde copie prend l'orientation opposée
    if p == 1: return ("line", 0, 90 if pos else 0)          # vertical / horizontal
    if p == 2: return ("cross", 0, 0 if pos else 45)         # + / ×
    if p == 4: return ("poly", 4, 45 if pos else 0)          # carré / losange
    return ("poly", p, 90 if pos else 270)                   # pointe en haut / en bas
def best_factors(n):
    for size in (2, 3, 4):
        for combo in itertools.combinations_with_replacement([9, 7, 5, 4, 3, 2], size):
            prod = 1
            for c in combo: prod *= c
            if prod == n: return list(combo)
    return None
def val(n, pol):
    """renvoie (spec, multiplicatif ?, polarité lisible ?)"""
    if n == "plein": return [("full", 0, 0)], False, False
    if n in PRIM: return [form(n, pol)], False, True
    if n == 6: return [form(3, pol, 0), form(3, pol, 1)], False, False
    if n == 8: return [form(4, pol, 0), form(4, pol, 1)], False, False
    f = best_factors(n)
    if f:
        spec, seen = [], {}
        for p in f:
            spec.append(form(p, pol, seen.get(p, 0))); seen[p] = seen.get(p, 0) + 1
        single = any(c == 1 for c in seen.values())
        return spec, True, single
    spec, rest, k = [], n, 0
    while rest >= 9: spec.append(form(9, pol, k)); rest -= 9; k += 1
    if rest: spec += val(rest, pol)[0]
    return spec, False, (k <= 1)

# ---------------- un sort ----------------
NAMES = {"CIBLE": ("2", "Cible"), "FORME": ("3", "Forme"), "AMPLEUR": ("4", "Ampleur"), "DUREE": ("5", "Durée"),
         "LOCALISATION": ("6", "Localisation"), "CONDITION": ("7", "Condition"), "IMPACT": ("8", "Impact"),
         "QUANTITE": ("9", "Quantité"), "COMPOSANTE": ("10", "Composante"), "INTERACTION": ("11", "Interaction"), "COSMETIQUE": ("12", "Cosmétique")}

import math, re as _re
def build(core, pol, rings, r0=34, split=None):
    """split = (lumineux, ténébreux) : chaque cercle prend la polarité de son camp"""
    gr, rows, undet = [], [], []
    for crit, v, words, reading, *rest in rings:
        sats = rest[0] if rest else []
        p = pol
        if split: p = "up" if crit in split[0] else "down"
        spec, mult, ok = val(v, p) if v is not None else ([], False, False)
        svals = [(d, val(sv, p), (x[0] if x else "")) for d, sv, *x in sats]
        mult = mult or any(m for _, (_, m, _), _ in svals)
        ok = ok or any(o for _, (_, _, o), _ in svals)
        if not ok: undet.append(crit)
        words = list(words) + (["FOIS"] if mult else [])
        gr.append(dict(label=" ".join([crit] + words), spec=spec, sats=[(d, sp, lab) for d, (sp, _, _), lab in svals]))
        rows.append((NAMES[crit][0], NAMES[crit][1], reading))
    dec, epu = GG.glyph(core, gr, r0=r0)
    RAW[0] = (dec, epu); PART[0] = None
    if split:
        full = split
        part = ([c for c in split[0] if c in undet], [c for c in split[1] if c in undet])
        dec = compose(dec, full, always=True)
        epu = compose(epu, part, always=False)
        PART[0] = part
    return (dec, epu), rows

def star():
    out = ""
    for k in range(8):
        a = math.radians(45 * k); L = 15 if k % 2 == 0 else 9
        out += f'<line x1="{3*math.cos(a):.1f}" y1="{3*math.sin(a):.1f}" x2="{L*math.cos(a):.1f}" y2="{L*math.sin(a):.1f}" class="ink-s"/>'
    return out
def abyss():
    return '<circle r="14" class="ink-s"/><circle cx="0" cy="6" r="8" class="ink-s"/>'

def astral(kind, crits):
    """glyphe satellite : noyau astral, puis un cercle annoté par critère concerné"""
    R0s, GAPs, BANDs = 20, 6, GG.BAND
    parts, prev, geo = [], R0s, []
    for c in crits:
        rin = prev + GAPs; rout = rin + BANDs; geo.append((rin, rout)); prev = rout
    for c, (rin, rout) in reversed(list(zip(crits, geo))):
        parts.append(f'<circle r="{rout:.1f}" class="paper-f"/><circle r="{rin:.1f}" class="ink-s"/><circle r="{rout:.1f}" class="ink-s"/>')
        parts.append(GG.label_alde(rin, rout, c, []))
    parts.append(f'<circle r="{R0s}" class="paper-f ink-s"/>' + (star() if kind == "lum" else abyss()))
    return "".join(parts), prev

def compose(svg, split, always=False):
    """place le glyphe principal entre ses deux satellites : ténébreux à gauche, lumineux à droite"""
    vb = [float(x) for x in _re.search(r'viewBox="([^"]+)"', svg).group(1).split()]
    h = -vb[1]
    inner = _re.sub(r'^<svg[^>]*>', '', svg)[:-6]
    out, xs = [], []
    lum, ten = split
    width_main = h
    Rm = max(float(x) for x in _re.findall(r'<circle r="([\d.]+)"', inner))
    pieces = []
    if not ten and not lum and not always: return svg
    if ten or always:
        g, r = astral("ten", ten); pieces.append(("ten", g, r))
    if lum or always:
        g, r = astral("lum", lum); pieces.append(("lum", g, r))
    left = next((p for p in pieces if p[0] == "ten"), None)
    right = next((p for p in pieces if p[0] == "lum"), None)
    gap = 18
    xl = -(width_main + gap + (left[2] if left else 0))
    xr = (width_main + gap + (right[2] if right else 0))
    body = inner
    if left:
        body += f'<line x1="{-Rm:.1f}" y1="0" x2="{xl + left[2]:.1f}" y2="0" class="ink-s"/><g transform="translate({xl:.1f},0)">{left[1]}</g>'
    if right:
        body += f'<line x1="{Rm:.1f}" y1="0" x2="{xr - right[2]:.1f}" y2="0" class="ink-s"/><g transform="translate({xr:.1f},0)">{right[1]}</g>'
    x0 = xl - (left[2] if left else 0) - 6 if left else -h
    x1 = xr + (right[2] if right else 0) + 6 if right else h
    return f'<svg viewBox="{x0:.1f} {-h:.1f} {x1 - x0:.1f} {2*h:.1f}" role="img" xmlns="http://www.w3.org/2000/svg">{body}</svg>'

def verb(key, neg): return ("verb", key, neg)
def chrono(key, neg, label): return ("chrono", key, neg, ("feu", "air", "terre", "eau"), label)
def hyb(f=0, a=0, t=0, e=0, label=None):
    units = ["feu"] * f + ["air"] * a + ["terre"] * t + ["eau"] * e
    slots = {}
    if "feu" in units: slots[90] = "feu"; units.remove("feu")
    if "eau" in units: slots[270] = "eau"; units.remove("eau")
    for s_ in (180, 0, 90, 270):
        if s_ not in slots and units: slots[s_] = units.pop(0)
    return ("hyb", tuple(slots[s_] for s_ in (90, 180, 0, 270)), label)

SAT_UP, SAT_DOWN = 270, 90      # satellite unique de la Forme : à l'opposé des pointes
L2 = ("LOCALISATION", 2, ["METRES"], "2 m : le contact")

SPELLS = []
RAW = [None]
PART = [None]
LEVEL = {"Hâte": 3, "Téléportation": 7, "Foulée brumeuse": 2, "Lenteur": 3, "Porte dimensionnelle": 4, "Symbole": 7, "Bouclier": 1, "Clairvoyance": 3, "Image silencieuse": 1, "Invocation d'élémentaire": 5,
         "Charme-personne": 1, "Chair en pierre": 6, "Éclair": 3, "Animation des morts": 3}
def S(group, title, verb_label, core, pol, dnd, rings, notes, r0=34, split=None):
    svg, rows = build(core, pol, rings, r0, split)
    SPELLS.append(dict(group=group, title=title, verb=verb_label, svg=svg, rows=rows, dnd=dnd, notes=notes, split=split, level=LEVEL.get(title), raw=RAW[0], bsplit=PART[0], core=core, rings=rings, r0=r0))

# ===== Groupe I =====
S("I", "Mur de force", "Créer · existence +", verb("existence", False), "up",
  "Mur de force · niveau 5 · sphère de 3 m de rayon · portée 36 m · 10 minutes",
  [("FORME", "plein", [], "sphère", [(SAT_UP, "plein")]),
   ("AMPLEUR", 6, ["DIAMETRE", "METRES"], "6 m de diamètre"),
   ("DUREE", 10, ["MINUTES"], "10 minutes"),
   ("LOCALISATION", 36, ["METRES"], "36 m")],
  ["Pas de Cible : le mur est déposé dans la trame, comme la Boule de feu posée. De l'énergie pure mise en forme, sans médium."])
S("I", "Désintégration", "Détruire · existence −", verb("existence", True), "down",
  "Désintégration · niveau 6 · portée 18 m · 10d6 + 40 de force",
  [("CIBLE", 3, [], "un ennemi"),
   ("LOCALISATION", 18, ["METRES"], "18 m"),
   ("IMPACT", 75, ["VIE"], "75 de vie retirée (moyenne de 10d6 + 40)")],
  ["Impact sans médium : la force brute de Détruire, qui est exactement le « force » de D&D."])
S("I", "Métamorphose", "Transformer · nature +", verb("nature", False), "up",
  "Métamorphose · niveau 4 · portée 18 m · 1 heure",
  [("CIBLE", 2, [], "un allié"),
   ("DUREE", 1, ["HEURES"], "1 heure"),
   ("LOCALISATION", 18, ["METRES"], "18 m"),
   ("IMPACT", "plein", ["BETE"], "transformation complète, en bête")],
  ["L'annotation « bête » dit en quoi l'on transforme : c'est la place qu'on cherchait pour le résultat de Transformer."])
S("I", "Doux repos", "Préserver · nature −", verb("nature", True), "down",
  "Doux repos · niveau 2 · contact · 10 jours · sel et pièces de cuivre",
  [("CIBLE", 4, ["CORPS"], "un objet annoté « corps »"),
   ("DUREE", 10, ["JOURS"], "10 jours"),
   L2,
   ("COMPOSANTE", None, ["SEL"], "du sel, accompagnant")],
  ["Le sel n'est pas consommé : il accompagne, et sa pertinence est évidente, il porte la forme de ce qui conserve."])
S("I", "Détection de la magie", "Révéler · visibilité +", verb("visibilite", False), "up",
  "Détection de la magie · niveau 1 · sphère de 9 m autour de soi · 10 minutes",
  [("FORME", "plein", [], "sphère", [(SAT_UP, "plein")]),
   ("AMPLEUR", 18, ["DIAMETRE", "METRES"], "18 m de diamètre"),
   ("DUREE", 10, ["MINUTES"], "10 minutes")],
  ["Pas de Cible : on révèle la trame elle-même. Pas de Localisation : la sphère est centrée sur le lanceur."])
S("I", "Invisibilité", "Dissimuler · visibilité −", verb("visibilite", True), "down",
  "Invisibilité · niveau 2 · contact · 1 heure",
  [("CIBLE", 2, [], "un allié"),
   ("DUREE", 1, ["HEURES"], "1 heure"),
   L2],
  ["Un sort négatif porté sur un allié : la polarité dit l'acte (dissimuler), pas l'intention."])
S("I", "Lévitation", "Déplacer · mouvement +", verb("mouvement", False), "up",
  "Lévitation · niveau 2 · portée 18 m · 10 minutes · jusqu'à 6 m de hauteur",
  [("CIBLE", 2, [], "un allié"),
   ("DUREE", 10, ["MINUTES"], "10 minutes"),
   ("LOCALISATION", 18, ["METRES"], "18 m"),
   ("IMPACT", 6, ["METRES"], "élévation de 6 m")],
  [])
S("I", "Immobilisation de personne", "Ancrer · mouvement −", verb("mouvement", True), "down",
  "Immobilisation de personne · niveau 2 · portée 18 m · 1 minute",
  [("CIBLE", 3, [], "un ennemi"),
   ("DUREE", 1, ["MINUTES"], "1 minute"),
   ("LOCALISATION", 18, ["METRES"], "18 m")],
  [])
# ===== Groupe II =====
S("II", "Lien télépathique", "Lier · relation +", verb("relation", False), "up",
  "Lien télépathique de Rary · niveau 5 · huit créatures · 9 m · 1 heure · coquilles d'œuf",
  [("CIBLE", 2, [], "un allié, × 8 par le satellite Quantité", [(90, 8)]),
   ("DUREE", 1, ["HEURES"], "1 heure"),
   ("LOCALISATION", 9, ["METRES"], "9 m"),
   ("COMPOSANTE", None, ["COQUILLES"], "coquilles, accompagnant")],
  ["Le satellite greffé sur la Cible est une Quantité : il multiplie la Cible, pas le sort (huit alliés liés par un seul sort)."])
S("II", "Dissipation de la magie", "Séparer · relation −", verb("relation", True), "down",
  "Dissipation de la magie · niveau 3 · portée 36 m",
  [("LOCALISATION", 36, ["METRES"], "36 m"),
   ("IMPACT", 3, [], "intensité 3 : les sorts de niveau 3 ou moins")],
  ["Pas de Cible : on sépare un sort de la trame où il est noué."])
S("II", "Agrandissement", "Amplifier · intensité +", verb("intensite", False), "up",
  "Agrandissement/rapetissement (agrandir) · niveau 2 · portée 9 m · 1 minute",
  [("CIBLE", 2, [], "un allié"),
   ("DUREE", 1, ["MINUTES"], "1 minute"),
   ("LOCALISATION", 9, ["METRES"], "9 m"),
   ("IMPACT", 2, ["TAILLE"], "taille × 2")],
  ["Même sort D&D que le suivant : une seule polarité les sépare."])
S("II", "Rapetissement", "Réduire · intensité −", verb("intensite", True), "down",
  "Agrandissement/rapetissement (rapetisser) · niveau 2 · portée 9 m · 1 minute",
  [("CIBLE", 3, [], "un ennemi"),
   ("DUREE", 1, ["MINUTES"], "1 minute"),
   ("LOCALISATION", 9, ["METRES"], "9 m"),
   ("IMPACT", 2, ["TAILLE"], "taille ÷ 2")],
  ["Le même glyphe que l'Agrandissement, pictogramme tourné d'un quart et formes vers le bas."])
S("II", "Foudre attirante", "Attirer · force directionnelle +", verb("force", False), "up",
  "Foudre attirante · tour de magie · portée 4,5 m · attire de 3 m",
  [("CIBLE", 3, [], "un ennemi"),
   ("LOCALISATION", 5, ["METRES"], "5 m"),
   ("IMPACT", 3, ["METRES"], "attire de 3 m")],
  ["D&D ajoute 1d8 de foudre au contact : un second Impact, d'une autre intensité, qu'il faudrait extraire. Laissé de côté."])
S("II", "Vague tonnante", "Repousser · force directionnelle −", verb("force", True), "down",
  "Vague tonnante · niveau 1 · cube de 4,5 m depuis soi · 2d8 de tonnerre · repousse de 3 m",
  [("CIBLE", "plein", [], "une zone"),
   ("FORME", 4, [], "cube", [(SAT_DOWN, "plein")]),
   ("AMPLEUR", 5, ["COTE", "METRES"], "5 m de côté"),
   ("IMPACT", 9, ["TONNERRE"], "intensité 9, tonnerre (2d8)")],
  ["Pas de Localisation : le cube part du lanceur. La poussée de 3 m est ce que fait le verbe ; le tonnerre est son médium."])
S("II", "Absorption des éléments", "Absorber · flux +", verb("flux", False), "up",
  "Absorption des éléments · niveau 1 · réaction · jusqu'au tour suivant",
  [("CIBLE", 1, [], "soi"),
   ("DUREE", 6, ["SECONDES"], "6 secondes, un tour"),
   ("CONDITION", 1, ["COUP"], "une condition : « un coup »")],
  ["La réaction de D&D devient une Condition : le sort attend d'être frappé pour partir."])
S("II", "Rayon ardent", "Émettre · flux −", verb("flux", True), "down",
  "Rayon ardent · niveau 2 · trois rayons · portée 36 m · 2d6 de feu chacun",
  [("CIBLE", 3, [], "un ennemi"),
   ("LOCALISATION", 36, ["METRES"], "36 m"),
   ("IMPACT", 7, ["FEU"], "intensité 7, feu"),
   ("QUANTITE", 3, [], "trois instances")],
  [])
# ===== Groupe III =====
S("III", "Restauration partielle", "Purifier · qualité +", verb("qualite", False), "up",
  "Restauration partielle · niveau 2 · contact",
  [("CIBLE", 2, [], "un allié"), L2,
   ("IMPACT", "plein", ["MALADIE"], "la maladie, entièrement")],
  [])
S("III", "Contagion", "Corrompre · qualité −", verb("qualite", True), "down",
  "Contagion · niveau 5 · contact · 7 jours",
  [("CIBLE", 3, [], "un ennemi"),
   ("DUREE", 7, ["JOURS"], "7 jours"),
   L2,
   ("IMPACT", "plein", ["MALADIE"], "la maladie, entièrement")],
  ["Le miroir exact de la Restauration : même médium, verbe retourné."])
S("III", "Fusion dans la pierre", "Fusionner · identité +", verb("identite", False), "up",
  "Fusion dans la pierre · niveau 3 · soi · 8 heures",
  [("CIBLE", 1, [], "soi"),
   ("DUREE", 8, ["HEURES"], "8 heures"),
   ("IMPACT", "plein", ["PIERRE"], "fusion complète, avec la pierre")],
  [])
S("III", "Image miroir", "Scinder · identité −", verb("identite", True), "down",
  "Image miroir · niveau 2 · soi · trois doubles · 1 minute",
  [("CIBLE", 1, [], "soi"),
   ("DUREE", 1, ["MINUTES"], "1 minute"),
   ("IMPACT", 3, ["IMAGE"], "trois images")],
  [])
S("III", "Appel de familier", "Invoquer · trame +", verb("trame", False), "up",
  "Appel de familier · niveau 1 · rituel d'une heure · 3 m · encens brûlé (consommé)",
  [("CIBLE", 7, ["ESPRIT"], "un être sans corps : un esprit"),
   ("DUREE", 1, ["HEURES"], "incantation : 1 heure ; fin : permanente", [(0, "plein")]),
   ("LOCALISATION", 3, ["METRES"], "3 m"),
   ("COMPOSANTE", None, ["ENCENS", "CONSOMME"], "encens, consommé")],
  ["La seule Durée qui porte une valeur au cercle principal : le temps d'incantation du rituel. Le satellite de fin, tracé sans forme, vaut plein : permanent."])
S("III", "Bannissement", "Bannir · trame −", verb("trame", True), "down",
  "Bannissement · niveau 4 · portée 18 m · 1 minute",
  [("CIBLE", 9, [], "un être qui relève d'un plan"),
   ("DUREE", 1, ["MINUTES"], "1 minute"),
   ("LOCALISATION", 18, ["METRES"], "18 m")],
  [])
S("III", "Épargner les mourants", "Stabiliser · ordre +", verb("ordre", False), "up",
  "Épargner les mourants · tour de magie · contact",
  [("CIBLE", 2, [], "un allié"), L2],
  ["Le plus simple des 24 : un verbe, une cible, une distance."])
S("III", "Confusion", "Déstabiliser · ordre −", verb("ordre", True), "down",
  "Confusion · niveau 4 · sphère de 3 m de rayon · portée 27 m · 1 minute",
  [("CIBLE", "plein", [], "une zone"),
   ("FORME", "plein", [], "sphère", [(SAT_DOWN, "plein")]),
   ("AMPLEUR", 6, ["DIAMETRE", "METRES"], "6 m de diamètre"),
   ("DUREE", 1, ["MINUTES"], "1 minute"),
   ("LOCALISATION", 27, ["METRES"], "27 m")],
  [])

# ===== Écoles de Magie (glyphes hybrides) =====
S("H", "Bouclier", "Abjuration · Hodolin · Acier (1F 1A 2T)", hyb(f=1, a=1, t=2, label="ABJURATION"), "up",
  "Bouclier · niveau 1 · réaction · +5 à la CA jusqu'au tour suivant",
  [("CIBLE", 1, [], "soi"),
   ("DUREE", 6, ["SECONDES"], "6 secondes"),
   ("CONDITION", 1, ["COUP"], "« un coup »"),
   ("IMPACT", 5, ["GARDE"], "garde + 5")],
  ["L'Acier : la combinaison qui protège."], r0=66, split=(["NOYAU", "CIBLE", "DUREE", "CONDITION", "IMPACT"], []))
S("H", "Clairvoyance", "Divination · Hodolin · Verre (2F 1A 1T)", hyb(f=2, a=1, t=1, label="DIVINATION"), "up",
  "Clairvoyance · niveau 3 · 1,6 km · 10 minutes · foyer en verre",
  [("DUREE", 10, ["MINUTES"], "10 minutes"),
   ("LOCALISATION", 2, ["KILOMETRES"], "2 km (1,6 km arrondis)"),
   ("COMPOSANTE", None, ["VERRE"], "un œil de verre, accompagnant")],
  ["Le Verre : ce qui laisse passer la vue. La composante de D&D (un œil de verre ou une corne ornée) devient pertinente."], r0=66, split=(["NOYAU", "DUREE", "COMPOSANTE"], ["LOCALISATION"]))
S("H", "Image silencieuse", "Illusion · Hodolin · Plasma (1F 3A)", hyb(f=1, a=3, label="ILLUSION"), "up",
  "Image silencieuse · niveau 1 · cube de 4,5 m · portée 18 m · 10 minutes",
  [("FORME", 4, [], "cube", [(SAT_UP, "plein")]),
   ("AMPLEUR", 5, ["COTE", "METRES"], "5 m de côté"),
   ("DUREE", 10, ["MINUTES"], "10 minutes"),
   ("LOCALISATION", 18, ["METRES"], "18 m"),
   ("COSMETIQUE", "plein", ["IMAGE"], "une image, au maximum")],
  ["Le Plasma : l'air chauffé qui fait naître le mirage. Une illusion est un sort de Cosmétique pur."], r0=66, split=(["NOYAU", "FORME", "AMPLEUR", "DUREE", "LOCALISATION", "COSMETIQUE"], []))
S("H", "Invocation d'élémentaire", "Invocation · Hodolin · Air (4A)", hyb(a=4, label="INVOCATION"), "up",
  "Invocation d'élémentaire (air) · niveau 5 · incantation 1 minute · portée 27 m · 1 heure · encens",
  [("CIBLE", 9, [], "un être qui relève d'un plan"),
   ("DUREE", 1, ["MINUTES", "HEURES"], "incantation : 1 minute ; fin : 1 heure", [(0, 1)]),
   ("LOCALISATION", 27, ["METRES"], "27 m"),
   ("COMPOSANTE", None, ["ENCENS"], "encens, accompagnant")],
  ["L'Air pur pour un élémentaire de l'air : la combinaison change avec l'élémentaire appelé."], r0=66, split=(["NOYAU", "DUREE", "LOCALISATION", "COMPOSANTE"], ["CIBLE"]))
S("G", "Charme-personne", "Enchantement · Galombar · Pollen (2A 1T 1E)", hyb(a=2, t=1, e=1, label="ENCHANTEMENT"), "down",
  "Charme-personne · niveau 1 · portée 9 m · 1 heure",
  [("CIBLE", 3, [], "un ennemi"),
   ("DUREE", 1, ["HEURES"], "1 heure"),
   ("LOCALISATION", 9, ["METRES"], "9 m")],
  ["Le Pollen : ce qui se respire et enivre."], r0=66, split=([], ["NOYAU", "CIBLE", "DUREE", "LOCALISATION"]))
S("G", "Chair en pierre", "Transmutation · Galombar · Roche (1A 3T)", hyb(a=1, t=3, label="TRANSMUTATION"), "down",
  "Pétrification (chair en pierre) · niveau 6 · portée 18 m · 1 minute",
  [("CIBLE", 3, [], "un ennemi"),
   ("DUREE", 1, ["MINUTES"], "1 minute"),
   ("LOCALISATION", 18, ["METRES"], "18 m"),
   ("IMPACT", "plein", ["PIERRE"], "en pierre, entièrement")],
  [], r0=66, split=(["LOCALISATION", "DUREE"], ["NOYAU", "CIBLE", "IMPACT"]))
S("G", "Éclair", "Évocation · Galombar · Éclair (3F 1A)", hyb(f=3, a=1, label="EVOCATION"), "down",
  "Éclair · niveau 3 · ligne de 30 m depuis soi · 8d6 de foudre",
  [("CIBLE", "plein", [], "une zone"),
   ("FORME", 1, [], "ligne", [(SAT_DOWN, "plein")]),
   ("AMPLEUR", 30, ["LONGUEUR", "METRES"], "30 m de long"),
   ("IMPACT", 28, ["FOUDRE"], "intensité 28, foudre")],
  ["La combinaison porte littéralement le nom du sort."], r0=66, split=(["FORME"], ["NOYAU", "CIBLE", "AMPLEUR", "IMPACT"]))
S("G", "Animation des morts", "Nécromancie · Galombar · Sang (1F 1T 2E)", hyb(f=1, t=1, e=2, label="NECROMANCIE"), "down",
  "Animation des morts · niveau 3 · incantation 1 minute · portée 3 m · 1 jour (24 heures) de contrôle",
  [("CIBLE", 4, ["OS"], "un objet annoté « os »"),
   ("DUREE", 1, ["MINUTES", "JOURS"], "incantation : 1 minute ; fin : 1 jour", [(0, 1)]),
   ("LOCALISATION", 3, ["METRES"], "3 m")],
  ["Le Sang : le fluide vital qu'on rend à ce qui n'en a plus."], r0=66, split=(["DUREE"], ["NOYAU", "CIBLE", "LOCALISATION"]))

# ===== Arts rares =====
S("R", "Lenteur", "Chronomancie · Corrompre (Qualité −) cerné des quatre éléments", chrono("qualite", True, "CHRONOMANCIE"), "down",
  "Lenteur · niveau 3 · jusqu'à 6 créatures dans un cube de 12 m · portée 36 m · 1 minute",
  [("CIBLE", 3, [], "six ennemis : satellite Quantité 6", [(90, 6)]),
   ("FORME", 4, [], "cube", [(90, "plein")]),
   ("AMPLEUR", 12, ["COTE", "METRES"], "12 m de côté"),
   ("DUREE", 1, ["MINUTES"], "1 minute"),
   ("LOCALISATION", 36, ["METRES"], "36 m"),
   ("IMPACT", 2, ["TEMPS"], "le temps des cibles divisé par deux")],
  ["Les trois sources réunies, comme l'exige la chronomancie : le pictogramme au cœur (énergie pure), les quatre éléments autour (énergie naturelle), les deux satellites astraux (le rythme).",
   "Équilibre astral strict, trois cercles de chaque côté. Le noyau, d'énergie pure, n'appartient à aucun astre et ne figure dans aucun satellite.",
   "Corrompre et non Ancrer : le temps des cibles est altéré, pas arrêté. Ancrer serait l'arrêt du temps.",
   "Répartition : ce qui décrit l'espace (forme, ampleur, portée) est lumineux, ce qui s'impose aux êtres (qui, à quel degré) est ténébreux. La Durée sert de balancier pour tenir le 50/50 : ici, ténébreuse."],
  r0=66, split=(["FORME", "AMPLEUR", "LOCALISATION"], ["CIBLE", "DUREE", "IMPACT"]))
S("R", "Hâte", "Chronomancie · Amplifier (Intensité +) cerné des quatre éléments", chrono("intensite", False, "CHRONOMANCIE"), "up",
  "Hâte · niveau 3 · une créature consentante · portée 9 m · 1 minute · vitesse doublée, +2 CA, une action de plus",
  [("CIBLE", 2, [], "un allié"),
   ("DUREE", 1, ["MINUTES"], "1 minute"),
   ("LOCALISATION", 9, ["METRES"], "9 m"),
   ("IMPACT", 2, ["TEMPS"], "le temps de la cible multiplié par deux")],
  ["Le miroir de Lenteur : même Impact « temps » à 2, mais Amplifier au lieu de Corrompre. Le temps de l'allié est intensifié.",
   "Répartition : portée lumineuse, cible et impact ténébreux ; la Durée, balancier, passe côté lumineux pour tenir le 50/50."],
  r0=66, split=(["DUREE", "LOCALISATION"], ["CIBLE", "IMPACT"]))
S("R", "Porte dimensionnelle", "Spatiomancie · Créer (Existence +) cerné des quatre éléments", chrono("existence", False, "SPATIOMANCIE"), "up",
  "Porte dimensionnelle · niveau 4 · soi et un allié consentant · 150 m · instantané",
  [("CIBLE", 1, [], "soi"),
   ("CIBLE", 2, [], "un allié"),
   ("LOCALISATION", 150, ["METRES"], "150 m")],
  ["Créer et non Déplacer : le sort ouvre une porte, et c'est en la franchissant qu'on arrive. Le déplacement est la conséquence, la porte est l'acte.",
   "Deux cercles Cible empilés plutôt que superposés : un trait dans une croix disparaîtrait.",
   "Comme pour la chronomancie, le noyau montre la maîtrise absolue de l'art : un verbe arcanique au cœur, les quatre éléments autour, les deux astres en satellites. Équilibre astral strict, un cercle de chaque côté ; le noyau reste neutre.",
   "Lacune : la direction du saut. D&D la donne en mots (« 150 m vers le haut, au nord-ouest ») ; le canon la confie aux satellites de longitude et de latitude, mais leur unité d'angle n'existe pas encore. Ici, le glyphe vise par son orientation au moment du tracé."],
  r0=66, split=(["LOCALISATION"], ["CIBLE"]))

S("R", "Téléportation", "Spatiomancie · Déplacer (Mouvement +) cerné des quatre éléments", chrono("mouvement", False, "SPATIOMANCIE"), "up",
  "Téléportation · niveau 7 · soi · un lieu connu, à n'importe quelle distance sur le même plan",
  [("CIBLE", 1, [], "soi"),
   ("LOCALISATION", 81, ["KILOMETRES"], "81 km, pour l'exemple : la valeur est la distance réelle du lieu visé")],
  ["La Localisation écrit la distance vraie : 81 km font deux nonagones multipliés, l'un pointe en haut, l'autre pointe en bas.",
   "Les ancrages du canon s'appliquent : saut direct entre deux ancrages d'un même hémisphère, passage obligé par les Plaines de Guerres pour le bandeau ou l'autre hémisphère.",
   "Équilibre astral strict, un cercle de chaque côté ; le noyau reste neutre."],
  r0=66, split=(["LOCALISATION"], ["CIBLE"]))
S("H", "Foulée brumeuse", "Invocation · Hodolin · Brume (3A 1E)", hyb(a=3, e=1, label="INVOCATION"), "up",
  "Foulée brumeuse · niveau 2 · action bonus · soi · jusqu'à 9 m",
  [("CIBLE", 1, [], "soi"),
   ("LOCALISATION", 9, ["METRES"], "9 m")],
  ["Ce n'est pas de la spatiomancie : la Brume dissout le corps et le recompose plus loin. Le mage traverse vraiment la distance, en un instant, et ne passe pas un mur sans interstice.",
   "Niveau 2 : tout le sort reste lumineux."],
  r0=66, split=(["NOYAU", "CIBLE", "LOCALISATION"], []))

# ===== Le glyphe le plus chargé =====
S("X", "Symbole", "Abjuration · Hodolin · Acier (1F 1A 2T)", hyb(f=1, a=1, t=2, label="ABJURATION"), "up",
  "Symbole (effet « Mort ») · niveau 7 · incantation 1 minute · au contact · sphère de 18 m de rayon · 10d10 nécrotiques · mercure, phosphore, poudre de diamant et d'opale (1 000 po) consommés · presque invisible · jusqu'à dissipation ou déclenchement",
  [("CIBLE", "plein", [], "une zone"),
   ("FORME", "plein", [], "sphère", [(90, "plein")]),
   ("AMPLEUR", 36, ["DIAMETRE", "METRES"], "36 m de diamètre"),
   ("DUREE", 1, ["MINUTES", "MINUTES"], "incantation : 1 minute ; fin de la lueur : 10 minutes", [(0, 10)]),
   ("LOCALISATION", 2, ["METRES"], "2 m : le contact"),
   ("CONDITION", 2, ["REGARD", "MOT"], "deux termes : « quand on le regarde », « sauf qui dit le mot »"),
   ("CONDITION", "plein", ["VERROU"], "verrou total : le glyphe tient sans son auteur"),
   ("IMPACT", 54, ["NECROSE"], "intensité 54 (55 arrondis), nécrose"),
   ("COMPOSANTE", "plein", ["MERCURE", "PHOSPHORE", "DIAMANT", "OPALE", "CONSOMME"], "quatre matières, consommées"),
   ("INTERACTION", 9, [], "maîtrise 9 sur les 12 premiers mètres", [(270, 12)]),
   ("INTERACTION", 5, [], "maîtrise 5 jusqu'à 24 m", [(90, 24)]),
   ("INTERACTION", 2, [], "maîtrise 2 jusqu'à 36 m", [(270, 36)]),
   ("COSMETIQUE", 2, ["LUEUR"], "une lueur faible"),
   ("COSMETIQUE", 1, ["TRACE"], "un tracé presque invisible")],
  ["Pourquoi ce sort : c'est un glyphe dans le monde de D&amp;D. Il remplit presque tous les critères sans rien inventer : condition, composante consommée, effet différé, discrétion à l'œil comme à la trame.",
   "Trois cercles 11 dessinent un profil de densité (canon §6.10) : un maître discret qui ne laisse aucun pic à la source du piège. C'est un choix d'auteur, pas une donnée D&amp;D, qui ne parle que de l'œil.",
   "Deux Conditions et deux Cosmétiques empilées : des intensités différentes interdisent de les fondre dans un même encart. L'extraction hors de la pile (§4.3) serait l'autre écriture.",
   "Le verrou est une proposition : un piège gravé doit survivre au départ de son auteur, ce que seul le plein de la Condition garantit dans le canon.",
   "Niveau 7, Hodolin : quatre cercles ténébreux sur onze (cible, condition, impact, composante), le reste lumineux."],
  r0=66, split=(["NOYAU", "FORME", "AMPLEUR", "DUREE", "LOCALISATION", "INTERACTION", "COSMETIQUE"], ["CIBLE", "CONDITION", "IMPACT", "COMPOSANTE"]))
