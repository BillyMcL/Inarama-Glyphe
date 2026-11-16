import re
"""Conversion d'un sort du SRD 5.1 en glyphe d'Inarama (cercle et bande, déclarée et non déclarée).
Données D&D : srd/spells.json (SRD 5.1, CC-BY-4.0). Choix sémantiques : fiches.py."""
import sys, io, json, math, re, contextlib, unicodedata
import os as _os
D = _os.path.dirname(_os.path.abspath(__file__))
DATA = _os.path.join(D, "..", "donnees")
sys.path.insert(0, D)
with contextlib.redirect_stdout(io.StringIO()):
    import spells as SP
    import gen_glyphs as GG
    import band_glyph as BG
from combos import COMBOS, ECOLES, DAMAGE_COMBO, MEDIUM, code
from translit import alde

SRD = {s["index"]: s for s in json.load(open(DATA + "/srd/spells.json", encoding="utf-8"))}

def _merge24(old, new):
    """fiche D&D des règles de 2024 : les champs présents en 2024 l'emportent ; ceux que les données de 2024 omettent
    (zone, dégâts, soins) sont repris de 2014, et les dégâts ne changent de dés que si leur type est resté le même"""
    r = dict(old or {})
    for k in ("index", "name", "level", "school", "ritual", "concentration", "classes"):
        if k in new: r[k] = new[k]
    r["range"] = re.split(r"\s+component", new["range"], flags=re.I)[0]
    r["duration"] = new["duration"]
    ct = new["casting_time"].split(",")[0].strip()
    r["casting_time"] = {"action": "1 action", "bonus action": "1 bonus action", "reaction": "1 reaction"}.get(ct.lower(), ct)
    if re.match(r"action \(", ct.lower()): r["casting_time"] = "1 action"
    r["material"] = (new.get("material") or "").replace("+", "").replace(" GP", " gp").replace("GP", "gp") or None
    r["desc"] = [new.get("description", "")]
    if new.get("area_of_effect"): r["area_of_effect"] = new["area_of_effect"]
    if new.get("heal_at_slot_level"): r["heal_at_slot_level"] = new["heal_at_slot_level"]
    d_old = (old or {}).get("damage"); d_old = d_old[0] if isinstance(d_old, list) else d_old
    d_new = new.get("damage")
    if d_new and (not d_old or d_old.get("damage_type", {}).get("index") == d_new.get("damage_type", {}).get("index") or not old):
        r["damage"] = d_new
    r["_ed"] = "2024"
    return r
import srd35 as _srd35
SRD35 = _srd35.load(DATA + "/srd/srd35")
import pf1 as _pf1
PF1 = _pf1.load(DATA + "/pf1/sorts-pf1.json", SRD35)
import pf2 as _pf2
PF2, PF2R = _pf2.load(DATA + "/pf2/sorts-pf2.json")      # Pathfinder 2 : édition d'origine, version remaniée
import eldenring as _er
ER = _er.load(DATA + "/eldenring/sorts-eldenring.json")      # Elden Ring : relevé propre, sans texte du jeu
SRD24 = {}
for _s in json.load(open(DATA + "/srd/spells-2024.json", encoding="utf-8")):
    SRD24[_s["index"]] = _merge24(SRD.get(_s["index"]), _s)
GRIM = {s["title"]: s for s in SP.SPELLS}

ACCENTS = {"LUMIERE": "lumière", "NECROSE": "nécrose", "DUREE": "durée", "METRES": "mètres", "KILOMETRES": "kilomètres",
 "DIAMETRE": "diamètre", "COTE": "côté", "QUANTITE": "quantité", "COSMETIQUE": "cosmétique", "CONSOMME": "consommé",
 "EVOCATION": "évocation", "NECROMANCIE": "nécromancie", "ECRIT": "écrit", "DISCRETION": "discrétion", "MATIERE": "matière",
 "PIEGE": "piège", "BETE": "bête", "ECLAIR": "éclair", "ENTREE": "entrée", "PRESENCE": "présence", "CREATURE": "créature",
 "ARMEE": "armée", "REVE": "rêve", "VERITE": "vérité", "EPEE": "épée", "ETRE": "être", "ENERGIE": "énergie", "FIELON": "fiélon", "DECLENCHEUR": "déclencheur", "ELEMENT": "élément",
 "REVEIL": "réveil", "INTREPIDITE": "intrépidité", "HOSTILITE": "hostilité", "REPULSION": "répulsion", "ETOURDISSEMENT": "étourdissement",
 "MEMOIRE": "mémoire", "HUMANOIDE": "humanoïde", "COMPREHENSION": "compréhension", "ECOUTE": "écoute", "RESISTANCE": "résistance", "ESPECE": "espèce",
 "CELESTE": "céleste", "ELEMENTAIRE": "élémentaire", "FEE": "fée", "MORTVIVANT": "mort-vivant", "PROPRIETE": "propriété", "PRESAGE": "présage",
 "PENSEE": "pensée", "SANSPLOMB": "sans plomb", "SANSEAUVIVE": "sans eau vive", "LIEUCONNU": "lieu connu", "ETHERE": "éthéré", "OUIE": "ouïe",
 "OEIL": "œil", "REPONSE": "réponse", "DIVINITE": "divinité", "RENOMMEE": "renommée", "LEGENDE": "légende", "ECOLE": "école", "INTREPIDITE": "intrépidité"}
def disp(w): return ACCENTS.get(w, w.lower())
def shown(w):
    """le mot tel qu'on l'affiche : en clair s'il est écrit en minuscules accentuées dans la fiche"""
    return w if w != w.upper() else disp(norm(w))
def norm(w):
    return "".join(c for c in unicodedata.normalize("NFD", w.upper()) if unicodedata.category(c) != "Mn").replace("'", "").replace("-", "")
def word(w):
    w = norm(w)
    if w not in GG.LEX:
        GG.LEX[w] = SP.syll(alde(w))
    return w

def rnd(x): return int(math.floor(x + 0.5))
def ft2m(ft): return max(1, rnd(ft * 0.3))
def dice_avg(s, mod=3):
    s = s.replace("MOD", str(mod)).replace(" ", "")
    tot = 0
    for part in re.findall(r"[+-]?[^+-]+", s):
        sg = -1 if part.startswith("-") else 1
        part = part.lstrip("+-")
        if "d" in part:
            n, d = part.split("d"); tot += sg * int(n or 1) * (int(d) + 1) / 2
        elif part.isdigit(): tot += sg * int(part)
    return tot

UNITS = {"second": "SECONDES", "minute": "MINUTES", "hour": "HEURES", "day": "JOURS", "round": "SECONDES", "year": "ANS"}
UNIT_FR = {"MINUTES": ("minute", "minutes"), "HEURES": ("heure", "heures"), "JOURS": ("jour", "jours"), "ANS": ("an", "ans"), "SECONDES": ("seconde", "secondes")}
def fr_time(v, u):
    if v == "plein": return "jusqu'à dissipation"
    return f"{v} {UNIT_FR[u][0 if v == 1 else 1]}"
def parse_time(t):
    t = re.sub(r"^concentration,?\s+(?=\S)", "", t.lower()).replace("up to ", "")
    if "instantaneous" in t or "special" in t: return None
    if "until dispelled" in t or "permanent" in t: return ("plein", None)
    if t.strip() == "concentration": return ("plein", None)   # concentration sans durée maximale : infinie
    m = re.match(r"(\d+)\s*(second|round|minute|hour|day|year)", t)
    if not m: return None
    n, u = int(m.group(1)), m.group(2)
    if u == "round": return (n * 6, "SECONDES")
    if u == "hour" and n == 24: return (1, "JOURS")
    return (n, UNITS[u])
def parse_cast(t):
    t = t.lower()
    if "action" in t or "reaction" in t: return None
    return parse_time(t)

def localisation(rng):
    r = rng.lower()
    if r.startswith("self") or r == "special" or re.match(r"0\s*feet", r): return None   # portée nulle : vide, pas d'anneau
    if r == "touch": return (2, "METRES", "2 m : le contact")
    if r in ("sight", "unlimited"): return ("plein", None, "à vue" if r == "sight" else "illimitée")
    m = re.match(r"(\d+)\s*(feet|foot|mile|miles)", r)
    if not m: return None
    n = int(m.group(1))
    if "mile" in m.group(2):
        km = max(1, rnd(n * 1.6)); return (km, "KILOMETRES", f"{km} km ({n} mile{'s' if n > 1 else ''})")
    mm = ft2m(n)
    if mm >= 1000: return (rnd(mm / 1000), "KILOMETRES", f"{rnd(mm/1000)} km")
    return (mm, "METRES", f"{mm} m")

FORMES = {  # type D&D -> (silhouette, satellites, nom, grandeur)
 # les satellites portent les proportions ; 1 s'écrit par le trait. « SYM » : la règle de symétrie les place
 # (un seul, au nord ou au sud ; deux, nord-sud ou ouest-est ; le premier axe est celui du nord ou de l'ouest)
 "sphere": ("plein", [("SYM", 1)], "sphère", "DIAMETRE"),
 "cube": (4, [("SYM", 1)], "cube", "COTE"),
 "cone": (3, [("SYM", 2), ("SYM", 1)], "cône (hauteur 2, rayon 1)", "LONGUEUR"),
 "line": (1, [("SYM", 1)], "ligne", "LONGUEUR"),
 "cylinder": (9, [("SYM", 1), ("SYM", 1)], "cylindre", "DIAMETRE"),
}

CIBLES = {1: "soi", 2: "un allié", 3: "un ennemi", 4: "un inconnu", 5: "un être dissimulé ou gardé", 7: "un être sans corps",
          9: "un être qui relève d'un plan", "plein": "une zone"}
VERBS = {("existence", False): "Créer", ("existence", True): "Détruire", ("nature", False): "Transformer", ("nature", True): "Préserver",
         ("visibilite", False): "Révéler", ("visibilite", True): "Dissimuler", ("mouvement", False): "Déplacer", ("mouvement", True): "Ancrer",
         ("relation", False): "Lier", ("relation", True): "Séparer", ("intensite", False): "Amplifier", ("intensite", True): "Réduire",
         ("force", False): "Attirer", ("force", True): "Repousser", ("flux", False): "Absorber", ("flux", True): "Émettre",
         ("qualite", False): "Purifier", ("qualite", True): "Corrompre", ("identite", False): "Fusionner", ("identite", True): "Scinder",
         ("trame", False): "Invoquer", ("trame", True): "Bannir", ("ordre", False): "Stabiliser", ("ordre", True): "Déstabiliser"}
VERB_GROUP = {"existence": "Existence", "nature": "Nature", "visibilite": "Visibilité", "mouvement": "Mouvement", "relation": "Relation",
              "intensite": "Intensité", "force": "Force directionnelle", "flux": "Flux", "qualite": "Qualité", "identite": "Identité",
              "trame": "Trame", "ordre": "Ordre"}

# ---------- polarité des cercles ----------
SPACE = ["LOCALISATION", "FORME", "AMPLEUR", "DUREE", "COSMETIQUE", "INTERACTION", "COMPOSANTE", "CONDITION", "QUANTITE", "CIBLE", "IMPACT"]
IMPOSED = ["IMPACT", "CIBLE", "CONDITION", "COMPOSANTE", "QUANTITE", "DUREE", "COSMETIQUE", "INTERACTION", "AMPLEUR", "FORME", "LOCALISATION"]
def split_hybrid(crits, hemi, level):
    """Hybride : le camp de l'école est majoritaire ; cercles minoritaires = n × niveau ÷ 18, arrondi.
    Minorité ténébreuse (Hodolin) : ce qui s'impose aux êtres d'abord ; minorité lumineuse (Galombar) : ce qui décrit l'espace d'abord."""
    n = len(crits) + 1
    k = min(len(crits), rnd(n * level / 18), n // 2)
    order = IMPOSED if hemi == "H" else SPACE
    minor = [c for c in order if c in crits][:k]
    major = ["NOYAU"] + [c for c in crits if c not in minor]
    return (major, minor) if hemi == "H" else (minor, major)
def split_rare(crits):
    """Arts rares : 50/50, noyau neutre. Espace lumineux, ce qui s'impose ténébreux, la Durée en balancier."""
    space = {"LOCALISATION", "FORME", "AMPLEUR", "COSMETIQUE", "INTERACTION"}
    lum = [c for c in crits if c in space]; ten = [c for c in crits if c not in space and c != "DUREE"]
    if "DUREE" in crits: (lum if len(lum) <= len(ten) else ten).append("DUREE")
    while abs(len(lum) - len(ten)) > 1:
        big, small = (lum, ten) if len(lum) > len(ten) else (ten, lum)
        small.append(big.pop())
    return lum, ten

# ---------- un sort ----------
SYMS = {"feu": "feu", "air": "air", "terre": "terre", "eau": "eau", "lumineux": "lumineux", "tenebreux": "tenebreux"}
SYM_FR = {"feu": "le feu", "air": "l'air", "terre": "la terre", "eau": "l'eau", "lumineux": "la face lumineuse", "tenebreux": "la face ténébreuse"}
def sym(n): return ("sym", n)
def vshow(v):
    return f"symbole de {SYM_FR[v[1]]}" if isinstance(v, tuple) and v and v[0] == "sym" else ("vide" if v is None else str(v))
def verbal(s):
    """le sort a-t-il une composante verbale ? (§2 : la parole est la forme la plus commune de la Condition)"""
    c = s.get("components")
    if c is None: c = (s.get("_fields") or {}).get("components")
    if isinstance(c, list): return "V" in c
    if not c: return True          # composantes inconnues (quelques sorts de 2024) : la parole, cas ordinaire
    return bool(re.match(r"\s*V\b", str(c)))
# un sort hybride porte déjà sa combinaison dans le noyau : ces médiums la répètent
REDIT = {"Feu": {"FEU"}, "Glace": {"FROID", "GLACE"}, "Foudre": {"FOUDRE"}, "Éclair": {"FOUDRE", "ECLAIR"}, "Orage": {"TONNERRE", "ORAGE", "FOUDRE"},
         "Acide sulfurique": {"ACIDE"}, "Ammoniac": {"POISON"}, "Eau": {"EAU"}, "Air": {"AIR", "VENT"}, "Terre": {"TERRE"}, "Lave": {"LAVE"},
         "Vapeur ardente": {"VAPEUR"}, "Brume": {"BRUME"}, "Tempête": {"TEMPETE"}, "Roche": {"ROCHE"}, "Plasma": {"PLASMA"}}
# un sort d'Arcane qui décrit un impact élémentaire le dit par les symboles des éléments, en satellites de l'Impact
ELEM_UNITS = {"FEU": ["feu"], "AIR": ["air"], "TERRE": ["terre"], "EAU": ["eau"], "FROID": ["air", "terre", "eau", "eau"],
              "GLACE": ["air", "terre", "eau", "eau"], "FOUDRE": ["feu", "feu", "air", "air"], "TONNERRE": ["feu", "feu", "air", "eau"],
              "ACIDE": ["feu", "air", "eau", "eau"], "LAVE": ["feu", "terre", "terre", "terre"], "VAPEUR": ["feu", "feu", "feu", "eau"], "POISON": ["feu", "air", "air", "eau"], "VENT": ["air"],
              # le métal et le bois ne sont pas des éléments à part : ils s'inscrivent par leur combinaison (Acier, Bronze, Bois)
              "ACIER": ["feu", "air", "terre", "terre"], "METAL": ["feu", "air", "terre", "terre"], "BRONZE": ["feu", "feu", "terre", "eau"],
              "BOIS": ["air", "terre", "terre", "eau"]}
_T_DIST = {"METRES", "KILOMETRES"}
_T_TIME = {"SECONDES", "INSTANT", "INSTANTS", "ROUNDS", "MINUTE", "MINUTES", "HEURE", "HEURES", "JOUR", "JOURS", "SEMAINES", "MOIS", "ANS"}
_T_DIM = {"RAYON", "HAUTEUR", "LONGUEUR", "LARGEUR", "DIAMETRE", "COTE"}
from lexique import VERBES_NUISIBLES as L_NUISIBLES
_T_CATEG = {"MORTVIVANT", "HOSTILE", "PLAN", "INTANGIBLE", "GRAND", "ELEMENTAIRE", "FER", "MOURANT"}     # ceux que l'effet touche : une Condition
_T_FORME = {"EXPLOSION", "ORBE"}      # mots de forme : traités avec le cercle Forme (formes_mots), pas ici
def sat_type(v, ws, parent=None):
    """Un satellite qui porte une mesure n'est pas du critère de son cercle : il déclare le sien (arcane §4.2).
    Une part → Quantité « fractionné » ; une distance → Localisation ; une dimension → Ampleur ; un temps → Durée
    (« délai » quand c'est une attente). Renvoie (critère ou None, mots)."""
    if not isinstance(v, (int, float)): return None, ws
    S = {norm(w) for w in ws if not str(w).startswith("si:")}
    crit, out = None, list(ws)
    if S == {"FRACTIONNE"}: crit = "QUANTITE"
    elif parent == "CONDITION" and S == {"VIE"}: crit = "IMPACT"            # seuil de vie : la Condition se mesure en Impact
    elif parent == "CONDITION" and len(S) == 1 and S <= {"SPECTATEUR", "COUPS", "INTERDIT"}: crit = "QUANTITE"   # un nombre de choses, comme les officiants
    elif S and S <= _T_DIST: crit = "LOCALISATION"
    elif S and S <= _T_TIME: crit = "DUREE"
    elif S & _T_DIST and S <= _T_DIST | _T_DIM | {"CUBES", "CARRES"}: crit = "AMPLEUR"
    elif S == {"SEUIL"} and parent != "CONDITION": crit = "CONDITION"
    elif parent == "CONDITION" and S == {"VALEUR", "PLATINE"}: crit = "COMPOSANTE"      # un prix que la chose doit valoir
    elif "NIVEAU" in S and S <= {"SEUIL", "NIVEAU"}:
        # l'effet ne vaut que pour les sorts jusqu'à tel poids : le poids d'un sort se lit dans son Interaction (niveau + 1)
        crit = "INTERACTION"; out = []
    elif S == {"KILOGRAMMES"}:        # un poids que l'effet ne dépasse pas : une Condition de seuil posée sur l'effet
        crit = "CONDITION"; out = ["seuil", "kilo"]
    elif S & {"DELAI", "RETARD"} and S & _T_TIME and S <= _T_TIME | {"DELAI", "RETARD"}:
        crit = "DUREE"; out = ["délai" if norm(w) == "RETARD" else w for w in ws]
    if crit == parent: crit = None
    return crit, (out if crit else ws)
def place_sats(sats, parent=None):
    """satellites annotés (valeur, [mots]) : un seul se place au nord ou au sud ; deux, de part et d'autre"""
    if not sats: return []
    # sur le cercle, plusieurs satellites d'un même encart se répartissent symétriquement : opposés, à 120°, en croix…
    n = len(sats)
    # un seul : au nord ou au sud ; deux : nord-sud ou ouest-est, selon ce qu'ils cachent (« SYM », résolu au tracé)
    angles = ["NS"] if n == 1 else ["SYM", "SYM"] if n == 2 else [(90 + k * 360 / n) % 360 for k in range(n)]
    out = []
    for a, st_ in zip(angles, sats):
        v, ws = st_[0], st_[1]
        crit, ws = (st_[2], ws) if len(st_) > 2 and isinstance(st_[2], str) and st_[2] in SP.NAMES else sat_type(v, ws, parent)
        if crit == "INTERACTION": v = v + 1
        lab = " ".join(word(w[3:] if str(w).startswith("si:") else w) for w in ws)
        out.append((a, v, (crit + " " + lab).strip(), {"crit": crit}) if crit else (a, v, lab))
    return out
def sat_reading(sats, parent=None):
    """un satellite peut porter sa propre Condition (« si:mort-vivant ») : il ne vaut que pour ce qui la remplit"""
    if not sats: return ""
    out = ""
    for st_ in sats:
        v, ws = st_[0], st_[1]
        crit, ws = (st_[2], ws) if len(st_) > 2 and isinstance(st_[2], str) and st_[2] in SP.NAMES else sat_type(v, ws, parent)
        if crit == "INTERACTION":
            out += f" ; satellite Interaction {v + 1} : seulement les sorts dont l'Interaction ne dépasse pas {v + 1}"; continue
        cs = [w[3:] for w in ws if str(w).startswith("si:")]; ns = [w for w in ws if not str(w).startswith("si:")]
        out += (f" ; satellite {SP.NAMES[crit][1] + ' ' if crit else ''}{vshow(v)}" + (f" « {' · '.join(shown(w) for w in ns)} »" if ns else "")
                + (f", seulement si « {' · '.join(shown(w) for w in cs)} »" if cs else ""))
    return out

GRAFT = ("impact", "impact_add", "impact_sats", "cond", "cond_sats", "fin", "cible_note", "qty")
def graft(idx, fiche, g, fam, s, fr, level, ecole, hemi, notes):
    """sort du grimoire enrichi : on garde ses cercles validés, on y greffe ce qui le définit en propre
    (Impact, Condition, fin, précision de Cible, Quantité), et le satellite de durée suit la règle actuelle"""
    rings = []
    for r in g["rings"]:
        crit, v, words, reading, *rest = r
        sats = list(rest[0]) if rest else []
        if crit == "DUREE":
            sats = [(("NS" if d in (0, 90, 270) else d), sv, *x) for d, sv, *x in sats]
            if fiche.get("fin"):
                words = list(words) + [word(w) for w in fiche["fin"]]
                reading += " ; fin : « " + " · ".join(shown(w) for w in fiche["fin"]) + " »"
        if crit == "CIBLE" and fiche.get("cible_note"):
            words = list(words) + [word(w) for w in fiche["cible_note"]]
            reading += ", précisé « " + " · ".join(shown(w) for w in fiche["cible_note"]) + " »"
        if crit == "CONDITION" and fiche.get("cond"): continue
        if crit == "IMPACT" and fiche.get("impact"): continue
        if crit == "QUANTITE" and fiche.get("qty"): continue
        if crit == "COMPOSANTE" and cost(s) and v in (None, "plein"):
            c_ = cost(s); v = c_[0]; words = list(words) + [word(c_[1])]
            reading = f"valeur {c_[0]} pièce{'s' if c_[0] > 1 else ''} de {c_[1]} ; " + reading
        rings.append((crit, v, list(words), reading, sats))
    # une autre édition (2024, 3.5) d'un sort du grimoire se traite comme tout sort : sa durée, sa portée et le nombre
    # de ses cibles viennent de ses propres données ; le grimoire garde ses choix (noyau, annotations, cercles propres)
    if fiche.get("src"):
        gen = build_spell(idx, {k: fiche[k] for k in ("fr", "src", "src_idx", "dur", "fin", "loc", "no_loc") if k in fiche} | {"fam": "A", "verb": ("existence", False)})
        new = {r[0]: r for r in gen["rings"] if r[0] in ("DUREE", "LOCALISATION")}
        rings = [r for r in rings if r[0] not in ("DUREE", "LOCALISATION")] + list(new.values())
        if fiche.get("qty_cible"):
            q = fiche["qty_cible"]
            rings = [(r[0], r[1], r[2], r[3] + " ; satellite Quantité " + ("plein : tous ceux que je choisis" if q == "plein" else str(q)), list(r[4]) + [(90, q)])
                     if r[0] == "CIBLE" else r for r in rings]
    tmp = build_spell(idx, {k: fiche[k] for k in ("fr", "verb", "comb", "fam", "art", "cond", "cond_sats", "impact", "impact_add", "impact_sats", "qty") if k in fiche} | {"fam": "A", "verb": ("existence", False)})
    for r in tmp["rings"]:
        if r[0] in ("CONDITION", "IMPACT", "QUANTITE") and fiche.get({"CONDITION": "cond", "IMPACT": "impact", "QUANTITE": "qty"}[r[0]]):
            rings.append(r)
    rings = matieres(mesures_impact(emprunt_et_rythme(mots_univers(rings))))
    rings = energies_et_cibles(supports(formes_mots(rings)), fam, None)
    order = ["CIBLE", "FORME", "AMPLEUR", "DUREE", "LOCALISATION", "CONDITION", "IMPACT", "QUANTITE", "COMPOSANTE", "INTERACTION", "COSMETIQUE"]
    rings.sort(key=lambda r: order.index(r[0]))
    crits = []
    for r in rings:
        if r[0] not in crits: crits.append(r[0])
    core = g["core"]; split = None; pol = "up"
    if g["group"] == "X": split = g["split"]
    elif core[0] == "verb": pol = "down" if core[2] else "up"
    elif core[0] == "chrono": split = split_rare(crits)
    else: split = split_hybrid(crits, hemi, level)
    svg, rows = SP.build(core, pol, rings, g["r0"], split)
    return dict(idx=idx, fr=fr, en=s["name"], level=level, ecole=ecole, fam=fam, verb=g["verb"], core=core, rings=rings, split=split,
                bsplit=SP.PART[0], svg=svg, rows=rows, r0=g["r0"],
                notes=["Version du grimoire, enrichie de ce qui définit le sort en propre." if any(fiche.get(k) for k in GRAFT) else "Version du grimoire, mise aux règles actuelles (durée, composante chiffrée)."] + notes + g["notes"], dnd=dnd_line(s, fr), pol=pol)

def cost(s):
    """prix D&D de la composante, ramené au plus petit nombre : 10 pièces d'une sorte = 1 pièce de la sorte au-dessus
    (cuivre → argent → or → platine). Renvoie (valeur, métal) ou None."""
    m = re.search(r"(\d[\d,]*)\s*(gp|sp|cp)", s.get("material") or "")
    if not m: return None
    n = int(m.group(1).replace(",", "")); metals = ["cuivre", "argent", "or", "platine"]
    i = {"cp": 0, "sp": 1, "gp": 2}[m.group(2)]
    while i < 3 and n % 10 == 0: n //= 10; i += 1
    return n, metals[i]

def build_spell(idx, fiche):
    _FACE[0] = fiche.get("face")
    _ED[0] = fiche.get("src")
    s = {"2024": SRD24, "3.5": SRD35, "pf1": PF1, "pf2": PF2, "pf2r": PF2R, "er": ER}.get(fiche.get("src"), SRD)[fiche.get("src_idx", idx)]
    fr = fiche["fr"]
    level = fiche.get("niveau", s["level"])       # « niveau » : le niveau retenu sur l'échelle de D&D quand il s'écarte du rang d'origine
    ecole, hemi, comb_def = ECOLES[s["school"]["name"]]
    notes = list(fiche.get("notes", []))
    # sort déjà tracé dans le grimoire : on reprend la version validée
    if fiche.get("grimoire"):
        g = GRIM[fiche["grimoire"]]
        fam = {"H": "H", "G": "H", "R": "R", "X": "H"}.get(g["group"], "A")
        if g["group"] == "X" or any(fiche.get(k) for k in GRAFT) or cost(s) or fiche.get("src") or fiche.get("qty_cible"):
            return graft(idx, fiche, g, fam, s, fr, level, ecole, hemi, notes)
        return dict(idx=idx, fr=fr, en=s["name"], level=level, ecole=ecole, fam=fam, verb=g["verb"], core=g["core"],
                    rings=g["rings"], split=g["split"], bsplit=g["bsplit"], svg=g["svg"], rows=g["rows"], r0=g["r0"],
                    notes=["Version du grimoire, déjà validée."] + notes + g["notes"], dnd=dnd_line(s, fr), pol=None)
    dmg = s.get("damage") or {}
    if isinstance(dmg, list): dmg = dmg[0]
    dtype = (dmg.get("damage_type") or {}).get("name")
    fam = fiche.get("fam") or ("H" if dtype in DAMAGE_COMBO or fiche.get("comb") else "A")
    rings = []
    # 2 Cible
    c = fiche.get("cible")
    if c is not None:
        val, *opt = c if isinstance(c, tuple) else (c,)
        words = [word(w) for w in fiche.get("cible_obj", [])]
        reading = (("objet annoté « " + fiche["cible_obj"][0].lower() + " »") if words else CIBLES.get(val, str(val)))
        if val == "trame":      # contresort, dissipation : la Cible est vide, c'est la trame elle-même qui est visée
            val = None; reading = "vide : la trame elle-même"
        if dtype == "Psychic" and not fiche.get("impact") and "psyché" not in (fiche.get("cible_note") or []):
            fiche = {**fiche, "cible_note": list(fiche.get("cible_note") or []) + ["psyché"]}
        if fiche.get("cible_note"):
            words += [word(w) for w in fiche["cible_note"]]
            reading += ", précisé « " + " · ".join(shown(w) for w in fiche["cible_note"]) + " »"
        sats = []
        if fiche.get("qty_cible"):
            q = fiche["qty_cible"]; sats = [(90, q)]
            reading += " ; satellite Quantité " + ("plein : tous ceux que je choisis" if q == "plein" else str(q))
        for k_, fs in enumerate(fiche.get("cible_sym", [])):
            sats.append((270 if k_ == 0 else 210 + 60 * k_, sym(fs)))
            reading += f" ; satellite : symbole de {SYM_FR[fs]}"
        rings.append(("CIBLE", val, words, reading, sats))
    # 3-4 Forme, Ampleur
    aoe = fiche.get("aoe") or s.get("area_of_effect")
    if aoe and not fiche.get("no_aoe"):
        sil, sats, nom, gr = FORMES[aoe["type"]]
        t, a_ = aoe["type"], aoe["size"] * 0.3048
        rings.append(("FORME", sil, [], nom, sats))
        if t == "line":
            size, unit, u = max(1, rnd(a_)), "METRES", "m"
            if size >= 1000: size, unit, u = rnd(size / 1000), "KILOMETRES", "km"
            rings.append(("AMPLEUR", size, ["LONGUEUR", unit], f"{size} {u} de long"))
        else:
            vol = {"sphere": 4 / 3 * math.pi * a_ ** 3, "cube": a_ ** 3, "cone": math.pi * (a_ / 2) ** 2 * a_ / 3,
                   "cylinder": math.pi * a_ ** 2 * (aoe.get("height", 2 * aoe["size"]) * 0.3048)}[t]
            base = {"sphere": f"sphère de {ft2m(aoe['size'])} m de rayon", "cube": f"cube de {ft2m(aoe['size'])} m de côté",
                    "cone": f"cône de {ft2m(aoe['size'])} m de long", "cylinder": f"cylindre de {ft2m(aoe['size'])} m de rayon" + (f" et {ft2m(aoe['height'])} m de haut" if aoe.get("height") else " (hauteur prise égale au diamètre)")}[t]
            # l'unité grandit pour que la valeur s'écrive en quatre formes au plus (9 × 9 × 9 × 9)
            for div, unit, u in ((1, ["METRES", "CUBES"], "m³"), (1e3, ["DECAMETRES", "CUBES"], "dam³"),
                                 (1e6, ["HECTOMETRES", "CUBES"], "hm³"), (1e9, ["KILOMETRES", "CUBES"], "km³")):
                if vol / div <= 6000: break
            size = max(1, rnd(vol / div))
            rings.append(("AMPLEUR", size, [word(x) for x in ["volume"] + unit], f"{size} {u} ; taille d'origine : {base}"))
    for extra in fiche.get("forme", []):     # forme saisie à la main (disque, etc.)
        rings.append((extra[0], extra[1], [word(w) for w in extra[2]], *extra[3:]))
    # 5 Durée
    cast = parse_cast(s["casting_time"]); dur = parse_time(s["duration"])
    if fiche.get("dur"): dur = fiche["dur"]
    fin = [word(w) for w in fiche.get("fin", [])]
    fin_txt = (" ; fin : « " + " · ".join(shown(w) for w in fiche["fin"]) + " »") if fin else ""
    if cast:
        words = [cast[1]] + ([dur[1]] if dur and dur[1] else []) + fin
        sat = [("NS", dur[0])] if dur else []     # satellite unique, centré : durée maximale
        rd = f"incantation : {fr_time(*cast)}" + (f" ; durée maximale : {fr_time(*dur)}" if dur else "")
        rings.append(("DUREE", cast[0], words, rd + fin_txt, sat))
    elif dur:
        rings.append(("DUREE", dur[0], ([dur[1]] if dur[1] else []) + fin, ("permanent" if dur[0] == "plein" and fiche.get("dur") else fr_time(*dur)) + fin_txt))
    # 6 Localisation
    loc = fiche.get("loc") or localisation(s["range"])
    if loc and not fiche.get("no_loc"):
        rings.append(("LOCALISATION", loc[0], ([word(w) for w in loc[1]] if isinstance(loc[1], list) else [loc[1]]) if loc[1] else [], loc[2]))
    # 7 Condition : la composante verbale est la Condition la plus commune (§2) ; les restrictions s'y ajoutent
    conds = (["parole"] if verbal(s) and not fiche.get("sans_parole") else []) + [c for c in (fiche.get("cond") or []) if not (verbal(s) and norm(c) == "PAROLE")]
    # rituel : la présence des officiants est une Condition, leur nombre un satellite Quantité greffé sur elle ; le satellite
    # ne porte le mot « officiant » que s'il faut dire laquelle des conditions il compte (§4.2, forme de référence)
    off_n = fiche.get("officiants", s.get("_officiants", 0)) if s.get("_rituel") else 0
    cond_sats = list(fiche.get("cond_sats") or [])
    off_rd = ""
    if off_n:
        seul = not conds and not cond_sats
        conds = conds + ["officiant"]
        cond_sats.append((off_n, [] if seul else ["officiant"]))
        off_rd = f" ; satellite Quantité : {off_n} officiant{'s' if off_n > 1 else ''} en plus du meneur, {'chacun à sa place sur un' if off_n > 1 else 'à sa place sur le'} cercle périphérique"
    if conds:
        cw = [word(w) for w in conds]
        rd = " ; ".join(f"« {shown(w)} »" for w in conds)
        rings.append(("CONDITION", len(cw), cw, rd + sat_reading(fiche.get("cond_sats"), "CONDITION") + off_rd, place_sats(cond_sats, "CONDITION")))
    # 8 Impact
    imp = fiche.get("impact")
    if imp is None and (dmg or s.get("heal_at_slot_level")):
        if dmg:
            table = dmg.get("damage_at_slot_level") or dmg.get("damage_at_character_level") or {}
            d = table.get(str(level)) or (list(table.values())[0] if table else None)
            med = [] if dtype in ("Force", "Psychic") else (MEDIUM.get(dtype) or [])     # force, psyché, dégât sans nature : Impact nu — « vie » ne dit que le soin
            if d: imp = (rnd(dice_avg(d)), med, f"{d} en moyenne")
        else:
            d = s["heal_at_slot_level"].get(str(level)) or list(s["heal_at_slot_level"].values())[0]
            imp = (rnd(dice_avg(d)), None, d.replace("MOD", "3") + " en moyenne, avec un modificateur de +3")
    if imp:
        v, med, why = imp if len(imp) == 3 else (*imp, "")
        # fractions : la forme porte le numérateur, un satellite « fractionné » porte le diviseur (1/4 : 1, et 4 en satellite)
        isats = list(fiche.get("impact_sats") or [])
        if isinstance(med, list) and "fractionné" in med:
            med = [m for m in med if m != "fractionné"]; isats.append((v, ["fractionné"])); v = 1
        plus_ = []      # effets seconds tirés des satellites : (valeur, mots, pourquoi, conditions, satellites)
        for j, st in enumerate(list(isats)):
            if "fractionné" in (st[1] or []) and len(st[1]) > 1:      # « une part de tel effet » : un cercle à lui, avec son diviseur
                isats[j] = None; plus_.append((1, [w for w in st[1] if w != "fractionné"], "", [], [(st[0], ["fractionné"])]))
        isats = [st for st in isats if st is not None]
        meds = med if isinstance(med, list) else ([med] if med else [])
        extra_imp = []; els = []
        # une face écrite en mot sur un satellite plein s'inscrit par son symbole
        isats = [(sym({"LUMINEUX": "lumineux", "TENEBREUX": "tenebreux"}[norm(st[1][0])]), []) if st[0] == "plein" and len(st[1] or []) == 1 and norm(st[1][0]) in ("LUMINEUX", "TENEBREUX") else st for st in isats]
        nb = [st for st in isats if (st[1] or []) == ["nombre"]]
        if nb and not fiche.get("qty"): fiche = {**fiche, "qty": nb[0][0]}
        isats = [st for st in isats if (st[1] or []) != ["nombre"]]
        # faces du plan astral : un symbole en satellite, sur la Cible quand c'est l'être visé, sur l'Impact sinon
        # rayonnement et nécrose sont les énergies des deux faces : la nécrose est toujours ténébreuse ;
        # la lumière n'est lumineuse que lorsqu'elle frappe (une valeur chiffrée), sinon c'est de la lumière qu'on voit
        meds = ["tenebreux" if norm(m) == "NECROSE" else "lumineux" if norm(m) == "LUMIERE" and (v != "plein" or fiche.get("rayonnement")) else m for m in meds]
        isats = [(st[0], [{"NECROSE": "ténébreux", "LUMIERE": "lumineux"}.get(norm(w), w) for w in (st[1] or [])]) + tuple(st[2:]) for st in isats]
        faces = [norm(m) for m in meds if norm(m) in ("LUMINEUX", "TENEBREUX")]
        if fiche.get("face") and faces: faces = [norm(fiche["face"])]      # forme réciproque : la même énergie, tissée de l'autre face
        if faces:
            meds = [m for m in meds if norm(m) not in ("LUMINEUX", "TENEBREUX")]
            isats += [(sym(f_.lower()), []) for f_ in faces]
            if not meds: med = []
        comb_ = fiche.get("comb") or DAMAGE_COMBO.get(dtype) or comb_def
        red = REDIT.get(comb_, set()) | {norm(comb_)}
        if fam == "H":
            if any(norm(m) in red for m in meds):
                meds = [m for m in meds if norm(m) not in red]
                if not meds: med = []
        else:
            els = [m for m in meds if norm(m) in ELEM_UNITS]
            # une énergie par cercle d'Impact : la première reste ici, chacune des autres reçoit son propre cercle
            for m in els[:1]: isats += [(sym(u_), []) for u_ in ELEM_UNITS[norm(m)]]
            extra_imp += [(v, [m], "") for m in els[1:]]
            if els:
                meds = [m for m in meds if norm(m) not in ELEM_UNITS]
                if not meds: med = []
        if isinstance(med, list) and not meds: med = []
        add_ = list(fiche.get("impact_add", []))
        if fam == "H": add_ = [a_ for a_ in add_ if norm(a_) not in red]
        else:
            ea_ = [a_ for a_ in add_ if norm(a_) in ELEM_UNITS]
            if not any(isinstance(st[0], tuple) and st[0][1] in ("feu", "air", "terre", "eau") for st in isats):
                for a_ in ea_[:1]: isats += [(sym(u_), []) for u_ in ELEM_UNITS[norm(a_)]]
                ea_ = ea_[1:]
            extra_imp += [(v, [a_], "") for a_ in ea_]
            add_ = [a_ for a_ in add_ if norm(a_) not in ELEM_UNITS]
        isats += [(sym(norm(a_).lower()), []) for a_ in add_ if norm(a_) in ("LUMINEUX", "TENEBREUX")]
        add_ = [a_ for a_ in add_ if norm(a_) not in ("LUMINEUX", "TENEBREUX")]
        fiche = {**fiche, "impact_sats": isats, "impact_add": add_}
        add = fiche.get("impact_add", [])
        # un sens éteint (aveuglement, surdité) n'est pas une forme de l'Impact : il passe en Cosmétique, « sens éteint »
        ET = {"AVEUGLEMENT": "vue", "CECITE": "vue", "SURDITE": "ouïe"}
        if fiche.get("guerit") or tuple(fiche.get("verb") or ()) == ("qualite", False): ET = {}   # un sort qui guérit ces maux ne les inflige pas : ils restent des mots de l'Impact
        et_ = [ET[norm(m)] for m in list(meds) + list(add) if norm(m) in ET]
        et_ += [ET[norm(st[1][0])] for st in (fiche.get("impact_sats") or []) if len(st[1] or []) == 1 and norm(st[1][0]) in ET]
        if et_:
            meds = [m for m in meds if norm(m) not in ET]; add = [a_ for a_ in add if norm(a_) not in ET]
            if not meds: med = []
            fiche = {**fiche, "impact_add": add, "_eteint": list(dict.fromkeys(et_)),
                     "impact_sats": [st for st in fiche.get("impact_sats") or [] if not (len(st[1] or []) == 1 and norm(st[1][0]) in ET)]}
        # un satellite « effet + mesure » (lenteur · mètres, rongement · secondes) n'est pas une mesure de cet Impact : c'est un
        # second effet. Il devient un cercle d'Impact plein, lu après le premier, que précise un satellite du critère de la mesure.
        mesures_ = []; garde_ = []
        for st in fiche.get("impact_sats") or []:
            ws_ = list(st[1] or []) if len(st) > 1 else []
            S_ = {norm(w) for w in ws_}
            u_ = S_ & (_T_DIST | _T_TIME); e_ = S_ - u_
            if (isinstance(st[0], (int, float)) and u_ and e_ and not e_ & (_T_DIM | _T_FORME | {"DELAI", "RETARD", "CUBES", "CARRES"})
                    and not any(str(w).startswith("si:") for w in ws_)):
                mesures_.append((st[0], [w for w in ws_ if norm(w) not in u_], [w for w in ws_ if norm(w) in u_]))
            else: garde_.append(st)
        # Pas de satellite d'Impact sur un Impact (arcane §6.7) : un satellite « nombre + mot » ou « plein + mot » est un
        # second effet. Il devient un cercle d'Impact à lui, lu après le premier. Un mot qui nomme ceux qu'il touche
        # (mort-vivant, hostile…) devient un satellite Condition de ce cercle. Restent en satellite : les symboles, les
        # mesures typées, l'emplacement de sort, et pour l'instant les seuils de niveau et les catégories pleines.
        garde2_ = []
        for st in garde_:
            ws_ = list(st[1] or []) if len(st) > 1 else []
            S_ = {norm(w[3:] if str(w).startswith("si:") else w) for w in ws_}
            if S_ & _T_FORME and (st[0] == "plein" or isinstance(st[0], (int, float))):
                # une explosion, un orbe : un second effet dont la forme sera inscrite en satellite de Forme (formes_mots)
                if S_ & _T_DIST: plus_.append(("plein", [w for w in ws_ if norm(w) in _T_FORME], "", [], [(st[0], ["rayon", "mètres"], "AMPLEUR")]))
                else: plus_.append((st[0], ws_, "", [], []))
                continue
            if st[0] == "plein" and ws_ and S_ <= _T_CATEG:
                # « plein, seulement si mort-vivant » : l'effet du cercle ne vaut que pour ceux-là — une Condition, en satellite
                garde2_.append(("plein", ws_, "CONDITION")); continue
            if (st[0] is None or isinstance(st[0], tuple) or not ws_ or not (st[0] == "plein" or isinstance(st[0], (int, float)))
                    or sat_type(st[0], ws_, "IMPACT")[0] or S_ in ({"SORT"}, {"FOIS"}, {"NOMBRE"}, {"FRACTIONNE"})
                    or (st[0] != "plein" and S_ & (_T_DIST | _T_TIME))):
                garde2_.append(st); continue
            cd_ = [w[3:] if str(w).startswith("si:") else w for w in ws_ if str(w).startswith("si:") or norm(w) in _T_CATEG]
            mw_ = [w for w in ws_ if not str(w).startswith("si:") and norm(w) not in _T_CATEG]
            # sous un verbe qui nuit, « vie » chiffrée se lirait comme une blessure : la vie que le lanceur reprend s'écrit « regain »
            # (« vie · temporaire » devient de même « regain · temporaire »)
            if st[0] != "plein" and VERBS.get(tuple(fiche.get("verb") or ())) in L_NUISIBLES: mw_ = ["regain" if norm(w) == "VIE" else w for w in mw_]
            plus_.append((st[0], mw_, "", cd_, []))
        garde_ = garde2_
        fiche = {**fiche, "impact_sats": garde_}
        nu = isinstance(med, list) and not meds     # Impact nu : liste vide, la force brute du verbe (§6.7)
        words = list(dict.fromkeys(([word(m) for m in meds] if meds else ([] if nu else ["VIE"])) + [word(a) for a in add]))
        nat = ((", " + " · ".join(shown(m) for m in meds)) if meds else (", sans nature : la force brute du verbe" if nu else " de vie")) + ((" · " if meds else ", ") + " · ".join(shown(a) for a in add) if add else "")
        head = "plein" if v == "plein" else f"intensité {v}"
        rings.append(("IMPACT", v, words, head + nat + (f" ({why})" if why else "") + sat_reading(fiche.get("impact_sats")),
                      place_sats(fiche.get("impact_sats"))))
        for mv_, me_, mu_ in mesures_:
            rings.append(("IMPACT", "plein", [word(m) for m in me_], "plein, " + " · ".join(shown(m) for m in me_)
                          + sat_reading([(mv_, mu_)], "IMPACT"), place_sats([(mv_, mu_)], "IMPACT")))
        # les autres cercles d'Impact : une énergie de plus, ou un second effet saisi à part (impact_plus)
        vus_ = {tuple(ELEM_UNITS[norm(m)]) for m in (els[:1] if fam != "H" else [])}
        uniq_ = []
        for e_ in extra_imp:       # une même énergie dite par deux mots (vent, air) ne s'inscrit qu'une fois
            t_ = tuple(ELEM_UNITS.get(norm(e_[1][0]), [e_[1][0]]))
            if t_ not in vus_: vus_.add(t_); uniq_.append(e_)
        for v2, w2, why2, *x2 in uniq_ + plus_ + list(fiche.get("impact_plus", [])):
            s2 = [(("plein", [c_], "CONDITION")) for c_ in (x2[0] if x2 else []) if c_] + list(x2[1] if len(x2) > 1 else []); ww = []
            for m in w2:
                if fam != "H" and norm(m) in ELEM_UNITS: s2 += [(sym(u_), []) for u_ in ELEM_UNITS[norm(m)]]
                elif norm(m) in ("LUMINEUX", "TENEBREUX"): s2.append((sym(norm(m).lower()), []))
                elif not (fam == "H" and norm(m) in red): ww.append(m)
            rings.append(("IMPACT", v2, [word(m) for m in ww], ("plein" if v2 == "plein" else f"intensité {v2}") + (", " + " · ".join(shown(m) for m in ww) if ww else "")
                          + (f" ({why2})" if why2 else "") + sat_reading(s2), place_sats(s2)))
    # 9 Quantité
    if fiche.get("qty"):
        qn = fiche.get("qty_note") or []
        rings.append(("QUANTITE", fiche["qty"], [word(w) for w in qn],
                      f"{fiche['qty']} « {' · '.join(shown(w) for w in qn)} »" if qn else f"{fiche['qty']} instances du sort"))
    # 10 Composante
    if fiche.get("comp"):
        mat = (s.get("material") or "").lower()
        consumed = fiche.get("consumed", "consume" in mat or bool(s.get("_rituel")))
        cw = [word(w) for w in fiche["comp"]] + (["CONSOMME"] if consumed else [])
        c_ = fiche.get("prix") or cost(s); val = None; rd = ", ".join(shown(w) for w in fiche["comp"]) + (", consommé" if consumed else ", accompagnant")
        if c_:
            val = c_[0]; cw = cw + ([word(c_[1])] if word(c_[1]) not in cw else []); rd = f"valeur {c_[0]} pièce{'s' if c_[0] > 1 else ''} de {c_[1]} ; " + rd
            if c_[1] not in ("cuivre", "argent", "or", "platine", "vie"):     # contrepartie : le lanceur cède une part de lui-même (lucidité, garde, résistance, guérison)
                rd = f"{c_[0]} : contrepartie, le lanceur cède de lui-même « " + " · ".join(shown(w) for w in fiche["comp"]) + " »"
            if c_[1] == "vie":     # le lanceur se blesse pour lancer : il paie de sa propre substance, comme pour un coût en expérience
                rd = f"{c_[0]} point{'s' if c_[0] > 1 else ''} de vie : le lanceur se blesse pour lancer le sort"
        rings.append(("COMPOSANTE", val, cw, rd))
    # coût en expérience (3.5) : le lanceur paie de sa propre substance. Un niveau (1 000 × niveau du lanceur en XP) vaut un DV,
    # soit 4,5 points de vie : moins d'un point → 1 « vie » ; un point ou plus → n « vie · durable » (retirée pour de bon)
    if s.get("_xp"):
        xp, cl = int(s["_xp"]), int(s["_cl"]); pv = xp * 4.5 / (1000 * cl)
        n, xw = (1, ["VIE"]) if pv < 1 else (rnd(pv), ["VIE", word("durable")])
        xr = (f"{xp} points d'expérience au niveau {cl}, soit {pv:.2f} point de vie : 1 point de vie".replace('.', ',', 1) if pv < 1
              else f"{xp} points d'expérience au niveau {cl} : {n} point{'s' if n > 1 else ''} de vie retiré{'s' if n > 1 else ''} pour de bon")
        if fiche.get("comp"):   # matière ET expérience : la vie payée devient un satellite annoté de la Composante
            r = rings.pop(); sats = [(n, xw)]
            rings.append((r[0], r[1], r[2], r[3] + sat_reading(sats), place_sats(sats)))
        else: rings.append(("COMPOSANTE", n, xw, xr))
    # 11 Interaction avec la trame : la quantité de magie nécessaire (niveau du sort + 1 ; un tour de magie vaut 1)
    try: lv_ = int(str(level).split()[0])
    except ValueError: lv_ = 0
    ival = lv_ + 1
    isat = []; ird = f"{ival} : sort de niveau {lv_}" if lv_ else "1 : tour de magie"
    if fiche.get("discret"):
        dv = ival if fiche["discret"] is True else fiche["discret"]
        isat = [("NS", dv, word("soustrait"))]
        ird += f" ; satellite {dv} « soustrait » : la trace du sort " + ("entièrement effacée" if dv in (ival, "plein") else "réduite")
    rings.append(("INTERACTION", ival, [], ird, isat))
    # 12 Cosmétique : ce que les sens perçoivent du sort ; la valeur compte les sens touchés
    if fiche.get("sens"):
        sens_ = fiche["sens"]                                  # [(sens, intensité ou None)]
        manif = fiche.get("manif", [])
        n_ = "plein" if len(sens_) >= 5 else len(sens_)
        cs = [(iv, [se]) for se, iv in sens_ if iv]
        rd = " · ".join(shown(m) for m in manif) + f" ; {len(sens_)} sens : " + ", ".join(se for se, _ in sens_) + sat_reading(cs)
        if fiche.get("cosm"):     # une illusion : les sens trompés s'écrivent dans un second cercle, extrait
            pass
        rings.append(("COSMETIQUE", n_, [word(m) for m in manif], rd, place_sats(cs)))
    if fiche.get("cosm"):
        v, w = fiche["cosm"]
        sens = "sens" in w.lower()      # « sens trompé » : la valeur compte les sens trompés (1 la vue seule, plein tous les sens)
        rings.append(("COSMETIQUE", v, [word(x) for x in w.split()], f"{w.lower()}, " + (("tous les sens" if v == "plein" else f"{v} sens") if sens else ("au maximum" if v == "plein" else f"degré {v}"))))
    if fiche.get("_eteint"):
        se_ = fiche["_eteint"]
        rings.append(("COSMETIQUE", len(se_), [word("sens"), word("éteint")] + [word(x) for x in se_],
                      f"sens éteint, {len(se_)} sens : " + ", ".join(se_)))
    # une valeur qui demanderait plus de quatre formes est arrondie à la plus proche qui s'écrit simplement
    def nforms(n): return len(SP.val(n, "up")[0])
    # Composante : un prix qui ne s'écrit pas en quatre formes se décompose exactement, valeur × satellite « fois », plutôt que de s'arrondir
    for i, r in enumerate(rings):
        v = r[1]
        if r[0] == "COMPOSANTE" and isinstance(v, int) and nforms(v) > 4:
            fs = [(a_, v // a_) for a_ in range(2, int(v ** 0.5) + 1) if v % a_ == 0 and nforms(a_) <= 4 and nforms(v // a_) <= 4]
            if fs:
                b_, a_ = max(fs)                       # les deux facteurs les plus proches ; le plus grand reste la valeur du cercle
                old_ = [(x[1], [x[2]] if len(x) > 2 and x[2] else []) for x in (r[4] if len(r) > 4 else [])]
                rings[i] = (r[0], a_, r[2], r[3] + f" ; {v} s'écrit {a_} × {b_} : satellite {b_} « fois »", place_sats(old_ + [(b_, ["fois"])]))
    for i, r in enumerate(rings):
        v = r[1]
        if isinstance(v, int) and nforms(v) > 4:
            best = min((x for x in range(max(1, v - v // 4), v + v // 4 + 2) if nforms(x) <= 4), key=lambda x: (abs(x - v), x))
            rings[i] = (r[0], best, r[2], r[3] + f" ; arrondi de {v} à {best} pour s'écrire en {nforms(best)} formes", *r[4:])
    for crit_, sl in (fiche.get("sats") or {}).items():
        for i, r in enumerate(rings):
            if r[0] == crit_:
                old_ = [(x[1], [x[2]] if len(x) > 2 and x[2] else []) for x in (r[4] if len(r) > 4 else [])]
                rings[i] = (r[0], r[1], r[2], r[3] + sat_reading(sl, r[0]), place_sats(old_ + list(sl), r[0])); break
    rings = matieres(mesures_impact(emprunt_et_rythme(mots_univers(rings))))
    try: _comb = (fiche.get("comb") or DAMAGE_COMBO.get(dtype) or comb_def) if fam not in ("A", "R") else None
    except NameError: _comb = None
    rings = energies_et_cibles(supports(formes_mots(rings)), fam, _comb)
    order = ["CIBLE", "FORME", "AMPLEUR", "DUREE", "LOCALISATION", "CONDITION", "IMPACT", "QUANTITE", "COMPOSANTE", "INTERACTION", "COSMETIQUE"]
    rings.sort(key=lambda r: order.index(r[0]))
    crits = []
    for r in rings:
        if r[0] not in crits: crits.append(r[0])
    # noyau, polarité
    split = None; pol = "up"
    if fam == "A":
        vk, vn = fiche["verb"]; core = SP.verb(vk, vn); pol = "down" if vn else "up"; r0 = 34
        verb = f"{VERBS[(vk, vn)]} · {VERB_GROUP[vk].lower()} {'−' if vn else '+'}"
        notes.insert(0, "Arcane : aucun élément en jeu, un verbe suffit.")
    elif fam == "R":
        vk, vn = fiche["verb"]; art = fiche["art"]
        core = SP.chrono(vk, vn, art.upper()); r0 = 66
        split = split_rare(crits)
        verb = f"{art.capitalize()} · {VERBS[(vk, vn)]} ({VERB_GROUP[vk]} {'−' if vn else '+'}) cerné des quatre éléments"
        notes.insert(0, f"Art rare ({art}) : verbe arcanique au cœur, quatre éléments, équilibre astral 50/50.")
    else:
        comb = fiche.get("comb") or DAMAGE_COMBO.get(dtype) or comb_def
        f_, a_, t_, e_ = COMBOS[comb]
        core = SP.hyb(f=f_, a=a_, t=t_, e=e_, label=norm(ecole)); r0 = 66
        if norm(ecole) not in GG.LEX: word(ecole)
        split = split_hybrid(crits, hemi, level)
        verb = f"{ecole} · {'Hodolin' if hemi == 'H' else 'Galombar'} · {comb} ({code(comb)})"
        why = fiche.get("why") or (f"les dégâts de {disp(MEDIUM[dtype])}" if dtype in DAMAGE_COMBO else "l'élément en jeu")
        notes.insert(0, f"Magie hybride, combinaison {comb} : {why}.")
    svg, rows = SP.build(core, pol, rings, r0, split, officiants=off_n)
    return dict(idx=idx, fr=fr, en=s["name"], level=level, ecole=ecole, fam=fam, verb=verb, core=core, rings=rings, split=split, officiants=off_n,
                bsplit=SP.PART[0], svg=svg, rows=rows, r0=r0, notes=notes, dnd=dnd_line(s, fr), pol=pol)

# ---------- mots de l'univers ----------
import mots_univers as MU
def mots_univers(rings):
    """remplace les termes de jeu par les mots de l'univers, dans les annotations des cercles et de leurs satellites"""
    page = _PAGE[0]
    out = []
    for r in rings:
        ws, rd = list(r[2]), r[3]
        sats = list(r[4]) if len(r) > 4 and r[4] else []
        touche = False
        def conv(lst):
            nonlocal rd, touche
            res = []
            for w in lst:
                n = MU.remplace(page, w)
                if n is None: res.append(w); continue
                touche = True
                if not n: rd = _sans_mot(rd, w)
                else:       # dans la lecture, le mot est écrit avec ses accents : on le retrouve par sa forme normalisée
                    def _r(m, w=w, n=n):
                        t = m.group()
                        if norm(t) != w: return t
                        return t[:-1] if len(n) == 1 and norm(n[0]) == w[:-1] else " · ".join(n)
                    rd = re.sub(r"[^\W\d_]+(?:-[^\W\d_]+)*", _r, rd)
                res += [word(x) for x in n]
            return list(dict.fromkeys(res))
        ws = conv(ws)
        ns = []
        for st in sats:
            if len(st) > 2 and st[2] and isinstance(st[2], str):
                lw = st[2].split(); o = st[3] if len(st) > 3 and st[3] else {}
                head = lw[:1] if o.get("crit") else []
                ns.append((st[0], st[1], " ".join(head + conv(lw[len(head):])), *st[3:]))
            else: ns.append(st)
        out.append((r[0], r[1], ws, rd, ns) if (touche and ns) else (r[0], r[1], ws, rd, *r[4:]) if touche else r)
    return out

def emprunt_et_rythme(rings):
    """Deux mots de jeu deviennent des mécaniques du glyphe (décisions de Baptiste).
    « temporaire » : une vie d'emprunt n'est pas définitive et ne se cumule pas → satellite Durée plein (elle dure ce que dure
    le sort) et satellite Quantité 1 (une seule à la fois) sur son cercle d'Impact.
    « persistance », « par tour » : un effet qui revient à chaque instant → satellite Durée 1 « chaque · instants »."""
    def has(r): return (r[0] == "IMPACT" and {"TEMPORAIRE", "PERSISTANCE", "ENTIER", "LANCEUR"} & set(r[2])) or (r[0] == "IMPACT" and "JOURS" in r[2] and _PAGE[0] == "temporary-resurrection") or (
        r[0] == "DUREE" and any(len(st) > 2 and st[2] == "VIE TOUR" for st in (r[4] if len(r) > 4 and r[4] else [])))
    if not any(has(r) for r in rings): return rings
    chaque = lambda: ("SYM", 1, " ".join(["DUREE", word("chaque"), word("instants")]), {"crit": "DUREE"})
    out, neufs = [], []
    for r in rings:
        if not has(r): out.append(r); continue
        ws, rd, sats = list(r[2]), r[3], list(r[4]) if len(r) > 4 and r[4] else []
        if r[0] == "DUREE":
            for st in [st for st in sats if len(st) > 2 and st[2] == "VIE TOUR"]:
                sats.remove(st)
                neufs.append(("IMPACT", st[1], ["VIE"], f"intensité {st[1]}, vie ; satellite Durée 1 « chaque · instants » : rendue à chaque instant", _resats([chaque()])))
            rd = re.sub(r" ; satellite \d+ « vie · tour »", "", rd)
            out.append((r[0], r[1], ws, rd, _resats(sats)) if sats else (r[0], r[1], ws, rd)); continue
        if "TEMPORAIRE" in ws:
            ws.remove("TEMPORAIRE"); rd = _sans_mot(rd, "TEMPORAIRE")
            sats += [("SYM", "plein", "DUREE", {"crit": "DUREE"}), ("SYM", 1, "QUANTITE", {"crit": "QUANTITE"})]
            rd += " ; satellite Durée plein : d'emprunt, elle ne dure que ce que dure le sort ; satellite Quantité 1 : une seule à la fois, elle ne s'ajoute pas à une autre"
        if "ENTIER" in ws:         # « en entier » est une quantité : satellite Quantité plein
            ws.remove("ENTIER"); rd = _sans_mot(rd, "ENTIER")
            sats.append(("SYM", "plein", "QUANTITE", {"crit": "QUANTITE"})); rd += " ; satellite Quantité plein : en entier"
        if "LANCEUR" in ws:        # l'effet retombe sur celui qui lance : satellite Cible 1 (soi)
            ws.remove("LANCEUR"); rd = _sans_mot(rd, "LANCEUR")
            sats.append(("SYM", 1, "CIBLE", {"crit": "CIBLE"})); rd += " ; satellite Cible 1 : soi, celui qui lance"
        if "JOURS" in ws and _PAGE[0] == "temporary-resurrection":      # « un jour » est une durée : satellite Durée 1 « jours »
            ws.remove("JOURS"); rd = _sans_mot(rd, "JOURS")
            sats.append(("SYM", 1, "DUREE JOURS", {"crit": "DUREE"})); rd += " ; satellite Durée 1 « jours »"
        if "PERSISTANCE" in ws:
            ws.remove("PERSISTANCE"); rd = _sans_mot(rd, "PERSISTANCE")
            sats.append(chaque()); rd += " ; satellite Durée 1 « chaque · instants » : l'effet revient à chaque instant"
        out.append((r[0], r[1], ws, rd, _resats(sats)))
    return out + neufs

# ---------- mesures écrites dans l'Impact ----------
# Dans l'Impact il ne reste que ce que le sort fait. Une distance, une hauteur, un âge, une quantité de matière sont des
# mesures : elles passent en satellite du critère qui les porte, posé sur le cercle d'Impact (arcane §4.2).
_MES_AMPLEUR = {"beanstalk", "pillars-of-sand", "upheaval", "control-water"}          # le chiffre est une hauteur
_MES_SCINDE = {"chilling-spray": 2, "clinging-ice": 2, "lifes-fresh-bloom": 2}      # le chiffre est une blessure ou un soin ; le ralentissement (1,5 m) à part
_MES_RETIRE = {       # mots de mesure qui ne disent rien de plus que la Durée ou la Localisation du glyphe
    "thought-shield-i": {"DUREE"}, "interrogation": {"DUREE"}, "object-possession-lesser": {"DUREE"},
    "eagle-eye": {"HAUTEUR"}, "stabilize-pressure": {"INSTANTS"}, "momentary-recovery": {"INSTANTS"},
    "synchronize": {"HEURES"}, "time-sense": {"HEURES"}}
# Une allure (tant de mètres à chaque instant, aussi longtemps que dure le sort) n'est pas un élan (un seul mouvement de tant
# de mètres) : l'allure porte en plus un satellite Durée 1 « chaque · instants ».
_MES_ALLURE = {"VOL", "COURSE", "PAS", "VITESSE", "ALLURE", "LENTEUR", "FOULEE"}
_MES_ALLURE_PAGES = {"tanglefoot", "magical-fetters", "sea-of-thought", "oneiric-mire", "swampcall", "antlion-trap", "feather-fall", "friendly-push"}
_MES_LITRES = {7: 200, 9: 255}                                                        # Création : des pieds cubes aux litres
def mesures_impact(rings):
    page = _PAGE[0]
    duree_pleine = any(r[0] == "DUREE" and (r[1] == "plein" or any(st[1] == "plein" for st in (r[4] if len(r) > 4 and r[4] else []))) for r in rings)
    if page == "maze-of-locked-doors" and any(r[0] == "IMPACT" and r[2] == ["DISTANCE"] for r in rings):
        # les portes tous les 9 m ne sont pas un effet : c'est la forme du lieu, un couloir en tronçons de 9 m
        rings = [r for r in rings if not (r[0] == "IMPACT" and r[2] == ["DISTANCE"])]
        i_ = next((i for i, r in enumerate(rings) if r[0] != "CIBLE"), len(rings))
        rings[i_:i_] = [("FORME", 1, [], "ligne : un couloir", [("SYM", 1)]),
                        ("AMPLEUR", 9, [word("longueur"), word("mètres")], "9 m de long entre deux portes")]
    out = []
    def sat(crit, v, *mots): return ("SYM", v, " ".join([crit] + [word(m) for m in mots]), {"crit": crit})
    for r in rings:
        if r[0] != "IMPACT": out.append(r); continue
        v, ws, rd = r[1], list(r[2]), r[3]
        sats = list(r[4]) if len(r) > 4 and r[4] else []
        S = set(ws); neufs = []; plus = []
        def ote(*mots):
            nonlocal rd
            for m in mots:
                if m in ws: ws.remove(m); rd = _sans_mot(rd, m)
        num = isinstance(v, (int, float))
        for m in _MES_RETIRE.get(page, ()): ote(m)
        if page == "perfection-of-essence" and ws == ["PERMANENCE"]:       # ne plus vieillir : la jeunesse, aussi longtemps que dure le rite
            ws[0] = word("jeunesse"); rd = rd.replace("plein, permanence", "plein, jeunesse", 1); S = set(ws)
        if "FOIS" in S and num:
            # « deux fois plus » : le pendant de « fractionné ». « fois » reste l'annotation des formes qui se multiplient.
            ote("FOIS")
            if not any(len(st) > 2 and "FRACTIONNE" in str(st[2]) for st in sats):
                neufs.append((sat("QUANTITE", v, "multiplié"), f"satellite Quantité {v} « multiplié »"))
            v = "plein"; num = False
        if page in ("clarion-call", "bombers-eye", "longshot", "sacred-bond") and S & {"PORTEE", "DISTANCE"}:
            ote("PORTEE", "DISTANCE"); neufs.append((sat("LOCALISATION", "plein"), "satellite Localisation plein : au loin"))
        if "PERMANENCE" in S and page != "permanency" and len(S) > 1:
            ote("PERMANENCE")
            if not duree_pleine: neufs.append((sat("DUREE", "plein"), "satellite Durée plein : pour toujours"))
        if "DUREE" in S and page == "pain-strike":
            ote("DUREE"); neufs.append((sat("DUREE", 1, "chaque", "instants"), "satellite Durée 1 « chaque · instants » : à chaque instant"))
        if "DUREE" in S and page == "caustic-eruption":
            ote("DUREE"); neufs.append((sat("DUREE", 2, "instants"), "satellite Durée 2 « instants » : ronge encore deux instants"))
        if "ANS" in S:
            ote("ANS")
            if num: neufs.append((sat("DUREE", v, "ans"), f"satellite Durée {v} « ans »")); v = "plein"
            elif word("âge") not in ws: ws.append(word("âge")); rd = rd.replace("plein, pourriture", "plein, pourriture · âge")
        if "HEURES" in S and num and "KILOMETRES" not in S:
            ote("HEURES"); neufs.append((sat("DUREE", v, "heures"), f"satellite Durée {v} « heures »")); v = "plein"
        if S & {"LITRES", "KILO"} and num:
            u = "LITRES" if "LITRES" in S else "KILO"; ote(u)
            neufs.append((sat("AMPLEUR", v, u.lower()), f"satellite Ampleur {v} « {u.lower()} »")); v = "plein"
        if "VOLUME" in S and num and page == "creation":
            ote("VOLUME"); q = _MES_LITRES.get(v, v * 28)
            neufs.append((sat("AMPLEUR", q, "litres"), f"satellite Ampleur {q} « litres »")); v = "plein"
        if "VOL" in ws and num and not S & _T_DIST:
            # le chiffre est une blessure ; s'élever dans les airs est un autre effet, sur son propre cercle
            ote("VOL")
            if not any(x[0] == "IMPACT" and x[1] == "plein" and x[2] == ["VOL"] for x in rings): plus.append(("IMPACT", "plein", ["VOL"], "plein, vol"))
        if S & _T_DIST and num and "FOIS" not in S:
            km = "KILOMETRES" in S
            if page in _MES_SCINDE:
                d = _MES_SCINDE[page]; eff = "LENTEUR" if "LENTEUR" in ws else "VITESSE"
                ote("METRES")
                if eff in ws: ote(eff)
                plus.append(("IMPACT", "plein", [eff], f"plein, {shown(eff.lower())} ; satellite Localisation {d} « mètres » ; satellite Durée 1 « chaque · instants » : une allure",
                             _resats([sat("LOCALISATION", d, "mètres"), sat("DUREE", 1, "chaque", "instants")])))
            else:
                ote("METRES", "KILOMETRES", "PORTEE")
                if page in _MES_AMPLEUR:
                    if "HAUTEUR" in ws: ws[ws.index("HAUTEUR")] = word("élévation"); rd = rd.replace("hauteur", "élévation", 1)
                    neufs.append((sat("AMPLEUR", v, "hauteur", "mètres"), f"satellite Ampleur {v} « hauteur · mètres »"))
                else:
                    neufs.append((sat("LOCALISATION", v, "kilomètres" if km else "mètres"), f"satellite Localisation {v} « {'kilomètres' if km else 'mètres'} »"))
                    if not km and (set(ws) & _MES_ALLURE or page in _MES_ALLURE_PAGES):
                        neufs.append((sat("DUREE", 1, "chaque", "instants"), "satellite Durée 1 « chaque · instants » : une allure, non un élan"))
                    if km and "HEURES" in ws:
                        ote("HEURES"); neufs.append((sat("DUREE", 1, "chaque", "heures"), "satellite Durée 1 « chaque · heures »"))
                        if not ws: ws.append("VOL"); rd = "vol" + rd
                v = "plein"
        if not neufs and not plus and ws == list(r[2]): out.append(r); continue
        if v == "plein" and r[1] != "plein": rd = re.sub(r"^intensité \d+(, )?", lambda m: "plein" + (m.group(1) or ""), rd)
        if neufs:
            i_ = rd.find(")") if rd.find("(") >= 0 and rd.find(")") > rd.find("(") else 0      # pas dans la parenthèse d'explication
            cut = rd.find(" ;", i_) if rd.find(" ;", i_) >= 0 else len(rd)
            rd = rd[:cut] + "".join(" ; " + t for _, t in neufs) + rd[cut:]
        sats = _resats(sats + [s for s, _ in neufs]) if neufs else sats
        out.append((r[0], v, ws, rd, sats) if sats else (r[0], v, ws, rd))
        out += plus
    # les allures déjà écrites en satellite (saisies ainsi dans les fiches) reçoivent le même rythme
    for i_, r in enumerate(out):
        if r[0] != "IMPACT" or not set(r[2]) & {"VOL", "VITESSE", "ALLURE", "LENTEUR"} or len(r) < 5 or not r[4]: continue
        labs = [str(st[2]) if len(st) > 2 else "" for st in r[4]]
        if any(l.startswith("LOCALISATION") and isinstance(st[1], (int, float)) for l, st in zip(labs, r[4])) and not any("CHAQUE" in l for l in labs):
            out[i_] = (r[0], r[1], r[2], r[3] + " ; satellite Durée 1 « chaque · instants » : une allure, non un élan",
                       _resats(list(r[4]) + [sat("DUREE", 1, "chaque", "instants")]))
    return out

# ---------- mots de forme ----------
import formes_mots as FM
_PAGE = [None]
def _resats(sats):
    """replace des satellites déjà posés quand on en ajoute : même règle de symétrie que place_sats"""
    n = len(sats)
    angles = ["NS"] if n == 1 else ["SYM", "SYM"] if n == 2 else [(90 + k * 360 / n) % 360 for k in range(n)]
    return [(a, *st[1:]) for a, st in zip(angles, sats)]
def _sans_mot(reading, w):
    """retire un mot de la tête d'une lecture (« plein, pierre · mur (…) » → « plein, pierre (…) »)"""
    cut = min([i for i in (reading.find(" ("), reading.find(" ;")) if i >= 0] or [len(reading)])
    head, rest = reading[:cut], reading[cut:]
    if ", " in head:
        h0, lst = head.split(", ", 1)
        items = [x for x in lst.split(" · ") if norm(x) != w]
        head = h0 + (", " + " · ".join(items) if items else "")
    else:
        items = [x for x in head.split(" · ") if norm(x) != w]
        head = " · ".join(items)
    out = head + rest
    return out[3:] if out.startswith(" ; ") else out
def _sat_forme(prim, annot, taille):
    sil, props, nom = FM.PRIM[prim]
    out = [("SYM", sil, " ".join(["FORME"] + annot), {"crit": "FORME", "kids": list(props)})]
    rd = f" ; satellite Forme : {nom}" + (f" « {' · '.join(shown(a) for a in annot)} »" if annot else "")
    if taille:
        out.append(("SYM", taille[0], " ".join(["AMPLEUR"] + [word(x) for x in taille[1]]), {"crit": "AMPLEUR"}))
        rd += f" ; satellite Ampleur {taille[0]} « {' · '.join(taille[1])} »"
    return out, rd
def formes_mots(rings):
    """Une géométrie dite en mot s'inscrit par le cercle Forme. Selon la place du mot : le sort a déjà un cercle Forme → le mot
    disparaît ; mot sur le premier Impact sans cercle Forme → cercle Forme ajouté ; mot sur la Cosmétique ou sur un second
    Impact → satellite de Forme à deux niveaux. « explosion » reste en annotation de la Forme. Tourbillon : cylindre + hélice."""
    page = _PAGE[0]
    tr_ = FM.trait(page)
    if tr_ and any("TRAIT" in r[2] for r in rings):
        tw_ = word(tr_)
        rings = [(r[0], r[1], list(dict.fromkeys(tw_ if w == "TRAIT" else w for w in r[2])),
                  re.sub(r"\btraits\b", tr_ + "s", re.sub(r"\btrait\b", tr_, r[3])), *r[4:]) if "TRAIT" in r[2] else r for r in rings]
    def geo(r): return [(w, FM.forme_de(page, w)) for w in r[2] if FM.forme_de(page, w)]
    if not any(r[0] in ("IMPACT", "COSMETIQUE") and geo(r) for r in rings): return rings
    rings = [tuple(r) + ((),) * (5 - len(r)) if len(r) < 5 else tuple(r) for r in rings]
    rings = [(r[0], r[1], list(r[2]), r[3], list(r[4] or [])) for r in rings]
    def formes(): return [i for i, r in enumerate(rings) if r[0] == "FORME"]
    def fam_(i): return (rings[i][1], len(rings[i][4]))
    FAM = {p: (v[0], len(v[1])) for p, v in FM.PRIM.items()}
    imp = [i for i, r in enumerate(rings) if r[0] == "IMPACT"]
    i1 = imp[0] if imp else None
    fait = set()          # primitives déjà inscrites par le cercle Forme, pour cette forme du sort
    def drop(i, w, note=""):
        r = rings[i]; rp = FM.REMPLACE.get((page, w)) if r[0] == "IMPACT" else None
        if rp:
            rings[i] = (r[0], r[1], [word(rp) if x == w else x for x in r[2]], r[3].replace(shown(w), rp, 1) + note, r[4]); return
        rings[i] = (r[0], r[1], [x for x in r[2] if x != w], _sans_mot(r[3], w) + note, r[4])
    def add_sat(i, prim, annot, taille):
        r = rings[i]; ns, rd = _sat_forme(prim, annot, taille)
        rings[i] = (r[0], r[1], r[2], r[3] + rd, _resats(list(r[4]) + ns))
    def tourbillon():
        """cylindre + hélice : la zone que donne la source (ou un cylindre) puis une hélice annotée « ajout »"""
        fo = formes()
        hel = FM.PRIM["helice"]
        if fo:
            f0 = fo[0]; r = rings[f0]
            props = [st for st in r[4]]
            degs = [90] if len(props) == 1 else [180, 0] if len(props) == 2 else [90, 210, 330]
            sats = [(d, *st[1:]) for d, st in zip(degs, props)]; rd = r[3]
            amp = next((j for j in range(f0 + 1, len(rings)) if rings[j][0] == "AMPLEUR"), None)
            if amp is not None:          # forme composée : l'Ampleur devient le satellite sud de la forme qu'elle mesure
                a = rings[amp]
                sats.append((270, a[1], " ".join(["AMPLEUR"] + list(a[2])), {"crit": "AMPLEUR"}))
                rd += f" ; satellite Ampleur : {a[3]}"
                rings.pop(amp)
            rings[f0] = (r[0], r[1], r[2], rd, sats)
            at = f0 + 1
        else:
            cyl = FM.PRIM["cylindre"]
            at = next((j for j, r in enumerate(rings) if r[0] not in ("CIBLE",)), len(rings))
            rings.insert(at, ("FORME", cyl[0], [], cyl[2] + " (taille non donnée par la source)", [(180, cyl[1][0]), (0, cyl[1][1])])); at += 1
        rings.insert(at, ("FORME", hel[0], [word("ajout")], "hélice ajoutée à la forme précédente : le tourbillon", [(90, hel[1][0]), (210, hel[1][1]), (330, hel[1][2])]))
        fait.add("tourbillon")
    # 1. le premier cercle d'Impact
    for k_ in ("IMPACT1", "IMPACT2", "COSMETIQUE"):
        for i in range(len(rings)):
            imp = [j for j, r in enumerate(rings) if r[0] == "IMPACT"]
            r = rings[i]
            pos = ("IMPACT1" if imp and i == imp[0] else "IMPACT2") if r[0] == "IMPACT" else r[0]
            if pos != k_: continue
            for w, prim in geo(r):
                annot = [w] if w in FM.ANNOTE else []
                taille = FM.TAILLE.get((page, w))
                fo = formes()
                if prim == "tourbillon":
                    if pos == "IMPACT1":
                        if "tourbillon" not in fait: tourbillon()
                        i = next(j for j, x in enumerate(rings) if x is not None and x[0] == r[0] and w in x[2] and x[3] == r[3])
                        drop(i, w, " ; le tourbillon est inscrit par les cercles Forme (zone, puis hélice)")
                    elif "tourbillon" in fait: drop(i, w)
                    else: drop(i, w); add_sat(i, "helice", [], None)
                    continue
                if prim in FM.SATELLITE:
                    drop(i, w); add_sat(i, prim, annot, taille)
                elif pos == "IMPACT1":
                    if fo:
                        f0 = fo[0]; fr_ = rings[f0]
                        if prim == "dome" and fam_(f0) == FAM["sphere"]:
                            amp = next((j for j in range(f0 + 1, len(rings)) if rings[j][0] == "AMPLEUR"), None)
                            a = rings[amp] if amp is not None else None
                            if a and list(a[2])[-2:] == ["METRES", "CUBES"] and isinstance(a[1], (int, float)):
                                ray = (3 * a[1] / (4 * math.pi)) ** (1 / 3); surf = max(1, rnd(2 * math.pi * ray ** 2))
                                d_ = FM.PRIM["dome"]
                                rings[f0] = ("FORME", d_[0], fr_[2], d_[2], [("SYM", d_[1][0]), ("SYM", d_[1][1])])
                                rings[amp] = ("AMPLEUR", surf, [word("surface"), "METRES"], f"{surf} m² : la calotte d'un dôme de {rnd(ray)} m de rayon")
                        elif prim == "helice" and fam_(f0) == FAM["ligne"]:
                            h_ = FM.PRIM["helice"]
                            rings[f0] = ("FORME", h_[0], fr_[2], h_[2], [(90, h_[1][0]), (210, h_[1][1]), (330, h_[1][2])])
                        if annot:
                            fr_ = rings[f0]
                            if word(w) not in fr_[2]: rings[f0] = (fr_[0], fr_[1], list(fr_[2]) + [word(w)], fr_[3] + f" ; annotée « {shown(w)} »", fr_[4])
                        drop(i, w); fait.add(prim)
                    else:
                        sil, props, nom = FM.PRIM[prim]
                        at = next((j for j, x in enumerate(rings) if x[0] not in ("CIBLE",)), len(rings))
                        rings.insert(at, ("FORME", sil, [word(a) for a in annot], nom + (" « " + " · ".join(shown(a) for a in annot) + " »" if annot else "")
                                          + ("" if taille else " (taille non donnée par la source)"), [("SYM", p_) for p_ in props]))
                        if taille:
                            rings.insert(at + 1, ("AMPLEUR", taille[0], [word(x) for x in taille[1]], f"{taille[0]} « {' · '.join(taille[1])} »"))
                        i = next(j for j, x in enumerate(rings) if x[0] == r[0] and w in x[2] and x[3] == r[3])
                        drop(i, w); fait.add(prim)
                elif pos == "COSMETIQUE" and fo and (prim in fait or fam_(fo[0]) == FAM[prim]
                                                    or (prim == "dome" and fam_(fo[0]) == FAM["sphere"])):
                    if prim == "dome" and fam_(fo[0]) == FAM["sphere"] and "dome" not in fait:      # un dôme dit par la seule Cosmétique
                        add_sat(i, prim, annot, taille)
                    drop(i, w)
                else:
                    drop(i, w); add_sat(i, prim, annot, taille)
                r = rings[i]
    return [r if len(r) > 4 and r[4] else r[:4] for r in rings]

# ---------- supports ----------
import supports_mots as SM
def supports(rings):
    """Ce sur quoi l'effet agit (une faculté, une part de l'être) se dit dans la Cible. Un seul cercle d'Impact : le mot passe
    en annotation du cercle Cible. Plusieurs cercles d'Impact (chacun sa faculté et sa valeur), pas de cercle Cible, ou un
    Impact plein qui resterait sans mot : il devient un satellite Cible de son cercle d'Impact."""
    page = _PAGE[0]
    imp = [i for i, r in enumerate(rings) if r[0] == "IMPACT"]
    if not any(SM.support(page, w) for i in imp for w in rings[i][2]): return rings
    rings = [(r[0], r[1], list(r[2]), r[3], list(r[4]) if len(r) > 4 and r[4] else []) for r in rings]
    cib = next((i for i, r in enumerate(rings) if r[0] == "CIBLE"), None)
    for i in imp:
        r = rings[i]
        sup = [w for w in r[2] if SM.support(page, w)]
        if not sup: continue
        reste = [w for w in r[2] if w not in sup]
        rd = r[3]
        for w in sup: rd = _sans_mot(rd, w)
        noms = " · ".join(shown(w) for w in sup)
        if len(imp) == 1 and cib is not None and (reste or r[1] != "plein"):
            c = rings[cib]
            neufs = [w for w in sup if w not in c[2]]       # déjà dit par la Cible : le mot quitte seulement l'Impact
            if neufs: rings[cib] = (c[0], c[1], list(c[2]) + neufs, c[3] + f", précisé « {' · '.join(shown(w) for w in neufs)} »", c[4])
            rings[i] = (r[0], r[1], reste, rd + f" ; ce que l'effet touche (« {noms} ») est dit par la Cible", r[4])
        else:
            rings[i] = (r[0], r[1], reste, rd + f" ; satellite Cible « {noms} »",
                        _resats(list(r[4]) + [("SYM", None, " ".join(["CIBLE"] + sup), {"crit": "CIBLE"})]))
    return [r if r[4] else r[:4] for r in rings]

# ---------- matières et apparences écrites dans l'Impact ----------
import matieres_mots as MM
_FACE = [None]
def matieres(rings):
    """applique la table de matieres_mots : la matière ou l'apparence quitte l'Impact, le vrai effet y reste"""
    t = MM.TABLE.get(_PAGE[0])
    if (_PAGE[0] or "").startswith("er-"): t = MM.er(t)       # Elden Ring : règles par mot, valables pour toutes ses pages
    if t: rings = _matieres(rings, t)
    if _PAGE[0] in MM.AMPLEUR: rings = _portee(rings)
    if _PAGE[0] in MM.ALLURE: rings = _allure(rings)
    if t and t.get("ordre"): rings = _ordre(rings, t["ordre"])
    imp = MM.IMPARABLE.get(_PAGE[0])
    if imp and (_ED[0] or "5e") in imp[0]: rings = _imparable(rings, imp[1])
    return rings
_ED = [None]       # l'édition de la forme en cours : None (D&D 5), « 2024 », « 3.5 », « pf1 », « pf2 », « pf2r »
def _imparable(rings, ou):
    """un effet auquel la cible ne peut ni se soustraire ni résister : le mot « imparable » annote son cercle d'Impact
    (« premier » : le premier cercle ; « chiffrés » : tous les cercles chiffrés)"""
    w = word("imparable"); out = []; fait = False
    for r in rings:
        if r[0] == "IMPACT" and w not in r[2] and ((ou == "chiffrés" and r[1] != "plein") or (ou == "premier" and not fait)):
            fait = True; rd = r[3]
            if "la force brute du verbe" in rd and not r[2]: rd = rd.replace("la force brute du verbe", "la force brute du verbe, imparable", 1)
            else: rd = re.sub(r"^(plein|intensité \d+)(, )?", lambda m: m.group(1) + ", imparable" + (" · " if m.group(2) else ""), rd, count=1)
            r = (r[0], r[1], list(r[2]) + [w], rd, *r[4:])
        out.append(r)
    return out
def _ordre(rings, mots):
    """les cercles d'Impact se lisent du centre vers l'extérieur, dans l'ordre où les effets se produisent : « ordre » les range"""
    ks = [word(m) for m in mots]
    rang = lambda r: min([ks.index(w) for w in r[2] if w in ks] or [len(ks)])
    pos = [i for i, r in enumerate(rings) if r[0] == "IMPACT"]
    tri = sorted((rings[i] for i in pos), key=rang)
    out = list(rings)
    for i, r in zip(pos, tri): out[i] = r
    return out
def _allure(rings):
    """une distance qui est une vitesse (X mètres à chaque instant) : la Localisation reçoit son satellite Durée 1 « chaque · instants »"""
    L = lambda st: len(st) > 2 and isinstance(st[2], str) and st[2].startswith("LOCALISATION")
    D = lambda st: len(st) > 2 and isinstance(st[2], str) and st[2].startswith("DUREE")
    out = []
    for r in rings:
        s = list(r[4]) if len(r) > 4 and r[4] else []
        if r[0] == "IMPACT" and any(L(st) for st in s) and not any(D(st) for st in s):
            s = _resats(s + [("SYM", 1, "DUREE CHAQUE INSTANTS", {"crit": "DUREE"})])
            r = (r[0], r[1], r[2], r[3] + " ; satellite Durée 1 « chaque · instants » : une allure", s)
        out.append(r)
    return out
def _portee(rings):
    """« jusqu'à X mètres » est une Ampleur (une fourchette), non une Localisation (un point ou une distance précise) : la portée d'un sens,
    le rayon d'une aura, l'allonge, la distance au plus. Une allure (avec « chaque · instants ») reste une Localisation."""
    L = lambda st: len(st) > 2 and isinstance(st[2], str) and st[2].startswith("LOCALISATION")
    out = []
    for r in rings:
        s = list(r[4]) if len(r) > 4 and r[4] else []
        if r[0] == "IMPACT" and any(L(st) for st in s) and not any(len(st) > 2 and isinstance(st[2], str) and st[2].startswith("DUREE CHAQUE") for st in s):
            s = [(st[0], st[1], "AMPLEUR" + st[2][len("LOCALISATION"):], {**(st[3] if len(st) > 3 and st[3] else {}), "crit": "AMPLEUR"}) if L(st) else st for st in s]
            r = (r[0], r[1], r[2], r[3].replace("satellite Localisation", "satellite Ampleur"), s)
        out.append(r)
    return out
def _matieres(rings, t):
    cercle = {word(k): v for k, v in t.get("cercle", {}).items()}       # « cercle » : une retouche propre au cercle qui porte tel mot
    lum = norm(_FACE[0] or "") == "LUMINEUX"
    if lum and t.get("lum"): t = {**t, **t["lum"], "rempl": {**t.get("rempl", {}), **t["lum"].get("rempl", {})}}
    seul = word(t["seul"]) if t.get("seul") else None
    N = lambda l: [word(x) for x in l]
    _acc = {}       # l'orthographe accentuée telle que la table l'écrit
    def _note(v):
        if isinstance(v, str): _acc.setdefault(norm(v), v)
        elif isinstance(v, dict): [_note(x) for kv in v.items() for x in kv]
        elif isinstance(v, (list, tuple)): [_note(x) for x in v]
    _note(t)
    def aff(w): return _acc.get(norm(w)) or shown(w)
    rempl = {word(k): N(v) for k, v in t.get("rempl", {}).items()}
    cosm, cible, ote = N(t.get("cosm", [])), N(t.get("cible", [])), N(t.get("ote", []))
    dure = N(t.get("dure", []))       # ce qui blesse encore après le coup : satellite Durée 1 « chaque · instants »
    af = N(t.get("arme_forme", []))       # arme créée : Impact « arme », et son nom annote un satellite Forme (ligne)
    symmot = {word(k): v for k, v in t.get("sym_mot", {}).items()}       # un mot d'élément qui devient son symbole
    refait = bool(t.get("refait"))       # réécriture complète : les cercles d'Impact de la page sont remplacés par « plus »
    psi = word(t["plus_si"]) if t.get("plus_si") else None
    psi_vu = psi is None or any(r[0] == "IMPACT" and psi in r[2] for r in rings)
    sc, sk = N(t.get("sat_cible", [])), N(t.get("sat_cond", []))
    part = set(rempl) | set(cosm) | set(cible) | set(ote) | set(sc) | set(sk) | set(N(t.get("sur", []))) | set(symmot) | set(af) | set(dure)      # « sur » : mot gardé qui désigne le cercle à retoucher
    def sat(crit, v, mots): return ("SYM", v, " ".join([crit] + N(mots)), {"crit": crit})
    def lit(crit, v, mots): return f"satellite {crit.capitalize().replace('Duree', 'Durée').replace('Quantite', 'Quantité')}" + ("" if v is None else f" {v}") + (f" « {' · '.join(mots)} »" if mots else "")
    out, vus_c, vus_k, touche = [], [], [], bool(t.get("toujours"))       # « toujours » : la fiche s'applique même si aucun mot ne la désigne
    qte = word(t["quantite"]) if t.get("quantite") else None       # un cercle d'Impact qui ne comptait que des fois devient un cercle Quantité
    for r in rings:
        if refait and r[0] == "IMPACT": touche = True; continue
        cle = next((k for k in cercle if r[0] == "IMPACT" and k in r[2]), None)
        if cle: out += _matieres([r], cercle[cle]); touche = True; continue
        if qte and r[0] == "IMPACT" and r[2] == [qte]: out.append(("QUANTITE", r[1], [], f"{r[1]} " + t.get("quantite_lit", "fois en tout"), [])); touche = True; continue
        if r[0] != "IMPACT" or not (part & set(r[2])) or (seul and seul not in r[2]): out.append(r); continue
        touche = True
        ws, rd = [], r[3]
        sats = list(r[4]) if len(r) > 4 and r[4] else []
        ajout = []
        for w in r[2]:
            if w in rempl:
                neufs = [x for x in rempl[w] if x not in ws and x not in r[2]]
                rd = re.sub(r"[^\W\d_]+(?:-[^\W\d_]+)*", lambda m: (" · ".join(aff(x.lower()) for x in neufs) if norm(m.group()) == w else m.group()), rd, count=0) if neufs else _sans_mot(rd, w)
                ws += neufs
            elif w in af:
                if word("arme") not in ws and word("arme") not in r[2]:
                    ws.append(word("arme")); rd = re.sub(r"[^\W\d_]+(?:-[^\W\d_]+)*", lambda m: ("arme" if norm(m.group()) == w else m.group()), rd, count=1)
                else: rd = _sans_mot(rd, w)
                s_, txt = _sat_forme("ligne", [w], None)
                ajout += [(x, None) for x in s_]; rd += txt.replace("« " + shown(w) + " »", "« " + aff(w) + " »")
            elif w in cosm: vus_c.append(w); rd = _sans_mot(rd, w)
            elif w in cible: vus_k.append(w); rd = _sans_mot(rd, w)
            elif w in ote: rd = _sans_mot(rd, w)
            elif w in symmot:
                rd = _sans_mot(rd, w)
                for e in symmot[w]: ajout.append((("SYM", ("sym", e), ""), "satellite symbole : " + e))
            elif w in sc: ajout.append((sat("CIBLE", None, [w]), f"satellite Cible « {aff(w.lower())} »")); rd = _sans_mot(rd, w)
            elif w in sk: ajout.append((sat("CONDITION", "plein", [w]), f"satellite Condition « {aff(w.lower())} »")); rd = _sans_mot(rd, w)
            else: ws.append(w)
        for x in N(t.get("ajoute", [])):
            if x not in ws and "la force brute du verbe, " in rd: ws.append(x); rd = rd.replace("la force brute du verbe, ", "la force brute du verbe, " + aff(x.lower()) + " · ", 1)
            elif x not in ws: ws.append(x); rd = re.sub(r"^(plein|intensité \d+)(, )?", lambda m: m.group(1) + ", " + aff(x.lower()) + (" · " if m.group(2) else ""), rd, count=1)
        for crit, v, mots in t.get("sats", []): ajout.append((sat(crit, v, mots), lit(crit, v, mots)))
        if set(r[2]) & set(dure) and not any(len(st) > 2 and isinstance(st[2], str) and st[2].startswith("DUREE") for st in sats):
            ajout.append((sat("DUREE", 1, ["chaque", "instants"]), lit("DUREE", 1, ["chaque", "instants"])))
        astral_ = any(isinstance(st[1], tuple) and st[1][1] in ("lumineux", "tenebreux") for st in sats)
        for e in t.get("sym", []):       # une face astrale déjà inscrite sur le cercle dit déjà l'ombre ou la lumière
            if e in ("lumineux", "tenebreux") and astral_: continue
            if e == "tenebreux" and lum: e = "lumineux"
            ajout.append((("SYM", ("sym", e), ""), "satellite symbole : " + {"tenebreux": "la face ténébreuse du plan astral", "lumineux": "la face lumineuse du plan astral"}.get(e, e)))
        if t.get("forme_prim"):
            s_, txt = _sat_forme(t["forme_prim"], [], None)
            ajout += [(x, None) for x in s_]; rd += txt
        if t.get("forme"):
            s_, txt = _sat_forme("ligne", [word(t["forme"])], None)
            txt = txt.replace("« " + shown(word(t["forme"])) + " »", "« " + aff(t["forme"]) + " »")
            ajout += [(x, None) for x in s_]; rd += txt
        rd += "".join(" ; " + x for _, x in ajout if x)
        sats = _resats(sats + [s for s, _ in ajout]) if ajout else sats
        v_ = r[1]
        if t.get("valeur") and v_ != t["valeur"]:
            v_ = t["valeur"]; rd = re.sub(r"^intensité \d+", "plein", rd) if v_ == "plein" else re.sub(r"^(plein|intensité \d+)", f"intensité {v_}", rd)
        out.append((r[0], v_, ws, rd, sats) if sats else (r[0], v_, ws, rd))
    if not touche and not (t.get("cosm_plus") or t.get("cible_plus")): return rings
    for p_ in (t.get("plus", []) if touche and psi_vu else []):
        v, mots, ss = p_[:3]
        s2 = _resats([("SYM", ("sym", x), "") if c == "SYM" else sat(c, x, m) for c, x, m in ss])
        rd = ("plein" if v == "plein" else f"intensité {v}") + (", " + " · ".join(mots) if mots else "") + (f" ({p_[3]})" if len(p_) > 3 and p_[3] else "") + "".join(" ; " + (f"satellite symbole : {x}" if c == "SYM" else lit(c, x, m)) for c, x, m in ss)
        out.append(("IMPACT", v, N(mots), rd, s2) if s2 else ("IMPACT", v, N(mots), rd))
    if t.get("fin") and touche:       # condition de fin : c'est tout le sort qui s'arrête ; elle s'annote sur le cercle de Durée, comme partout ailleurs
        for i, r in enumerate(out):
            if r[0] == "DUREE":
                neufs = [w for w in N(t["fin"]) if w not in r[2]]
                if neufs: out[i] = (r[0], r[1], list(r[2]) + neufs, r[3] + f" ; fin : « {' · '.join(aff(w) for w in neufs)} »", *r[4:])
                break
    vus_c += [w for w in N(t.get("cosm_plus", [])) if touche and psi_vu]; vus_k += [w for w in N(t.get("cible_plus", [])) if touche]
    if lum and t.get("lum") is not None:        # face lumineuse : ce que l'on voit n'est plus l'ombre mais la lumière
        for i, r in enumerate(out):
            if r[0] == "COSMETIQUE" and "OMBRE" in r[2]:
                ws_ = list(dict.fromkeys(word("lumière") if w == "OMBRE" else w for w in r[2]))
                out[i] = (r[0], r[1], ws_, " · ".join(aff(w.lower()) for w in ws_) + r[3][r[3].find(","):] if "," in r[3] else r[3], *r[4:])
    if vus_c:
        i = next((i for i, r in enumerate(out) if r[0] == "COSMETIQUE"), None)
        if i is None: out.append(("COSMETIQUE", 1, list(dict.fromkeys(vus_c)), " · ".join(aff(w.lower()) for w in dict.fromkeys(vus_c)) + ", 1 sens"))
        else:
            c = out[i]; neufs = [w for w in dict.fromkeys(vus_c) if w not in c[2]]
            if neufs: out[i] = (c[0], c[1], list(c[2]) + neufs, " · ".join(aff(w.lower()) for w in neufs) + " · " + c[3], *c[4:])
    if vus_k:
        i = next((i for i, r in enumerate(out) if r[0] == "CIBLE"), None)
        if i is not None:
            c = out[i]; neufs = [w for w in dict.fromkeys(vus_k) if w not in c[2]]
            if neufs: out[i] = (c[0], c[1], list(c[2]) + neufs, c[3] + f", précisé « {' · '.join(aff(w.lower()) for w in neufs)} »", *c[4:])
    if t.get("forme_cercle") and touche:
        i = next((i for i, r in enumerate(out) if r[0] == "FORME"), None)
        if i is not None:
            c = out[i]; out[i] = (c[0], c[1], list(c[2]) + [word(t["forme_cercle"])], c[3] + f" « {t['forme_cercle']} »", *c[4:])
    return out

# ---------- énergies et cibles dites en mots ----------
import combos as _K
def energies_et_cibles(rings, fam=None, comb=None):
    """Sur l'Impact, une énergie (foudre, froid, lave, sable, brume, acier, terre) ne s'écrit pas en mot : elle s'inscrit par les
    symboles de sa combinaison élémentaire, en satellites — sauf en Magie hybride quand le noyau la dit déjà. Un cercle d'Impact
    est un effet : s'il nommait plusieurs énergies, chacune prend son propre cercle. De même « allié » et « ennemi » sont des
    valeurs de Cible : un satellite Cible chiffré (2, 3). Décisions de Baptiste, 16 novembre 2026."""
    AUTRES = {"FEU": "Feu", "ACIDE": None, "GLACE": "Glace", "TONNERRE": None}       # énergies qui accompagnent parfois les précédentes
    def est_energie(w, ws): return w in MU.ENERGIES or (w in AUTRES and any(x in MU.ENERGIES for x in ws))
    if not any(r[0] == "IMPACT" and any(w in MU.ENERGIES or w in MU.CIBLES for w in r[2]) for r in rings): return rings
    ELS = ("feu", "air", "terre", "eau")
    def unites(w):
        if w == "TERRE": return ["terre"], "Terre"
        nom = MU.ENERGIES.get(w) or AUTRES.get(w)
        if nom:
            f_, a_, t_, e_ = _K.COMBOS[nom]
            return ["feu"] * f_ + ["air"] * a_ + ["terre"] * t_ + ["eau"] * e_, nom
        return list(ELEM_UNITS[w]), shown(w)
    imp = [r for r in rings if r[0] == "IMPACT"]
    cib = next((r for r in rings if r[0] == "CIBLE"), None)
    hyb = fam not in ("A", "R", None)
    out = []
    for r in rings:
        if r[0] != "IMPACT": out.append(r); continue
        ws, rd, sats = list(r[2]), r[3], list(r[4]) if len(r) > 4 and r[4] else []
        en = [w for w in ws if est_energie(w, ws)]
        suite = []
        reste = [x for x in ws if x not in en]
        annote = any(len(st) > 2 and st[2] for st in sats)
        if en and not (hyb and r[1] == "plein" and not reste and not annote and len(en) == 1):    # un Impact plein hybride garde son mot d'action
            for k, w in enumerate(en):
                units, nom = unites(w)
                if hyb and comb == nom and k == 0:
                    rd = _sans_mot(rd, w) + f" ; l'énergie (« {shown(w)} ») est dite par le noyau"
                elif k == 0:
                    sats = [st for st in sats if not (isinstance(st[1], tuple) and st[1][1] in ELS)]
                    rd = re.sub(r" ; satellite symbole de (?:le feu|l'air|la terre|l'eau)", "", rd)
                    sats += [("SYM", ("sym", u), "") for u in units]
                    rd = _sans_mot(rd, w) + f" ; satellites : les symboles de la combinaison {nom}"
                else:      # une autre énergie est un autre effet : son propre cercle d'Impact, de même intensité
                    rd = _sans_mot(rd, w)
                    suite.append(("IMPACT", r[1], [], ("plein" if r[1] == "plein" else f"intensité {r[1]}") + f" ; satellites : les symboles de la combinaison {nom}",
                                  _resats([("SYM", ("sym", u), "") for u in units])))
            ws = reste
        for w in [w for w in ws if w in MU.CIBLES]:
            v = MU.CIBLES[w]; ws.remove(w); rd = _sans_mot(rd, w)
            if not (len(imp) == 1 and cib is not None and cib[1] == v):
                sats.append(("SYM", v, "CIBLE", {"crit": "CIBLE"})); rd += f" ; satellite Cible {v} : {CIBLES.get(v, '')}"
        out.append((r[0], r[1], ws, rd, _resats(sats)) if sats else (r[0], r[1], ws, rd))
        out += suite
    return out

def glyph_key(f):
    return (repr(f["core"]), repr([(r[0], r[1], tuple(r[2]), repr(r[4:5])) for r in f["rings"]]), repr(f["split"]))

def build_forms(idx, fiche):
    """toutes les formes d'un sort ; puis, pour un sort qui existe aussi dans les règles de 2024,
    ses formes de 2024 qui donnent un glyphe différent (un glyphe identique est le même sort)"""
    _PAGE[0] = idx
    forms = _forms(idx, fiche)
    if fiche.get("src") == "pf2r": return forms
    seen = {glyph_key(f) for f in forms}
    for ed, base, key in (("2024", SRD24, "v24"), ("3.5", SRD35, "v35"), ("PF1", PF1, "vpf"), ("PF2", PF2, "vp2"), ("PF2 remaniée", PF2R, "vr")):
        if fiche.get("src") == "pf2" and ed != "PF2 remaniée": continue
        if fiche.get("src") == "pf1" and ed not in ("PF2", "PF2 remaniée"): continue      # une page venue de Pathfinder 1 ne reçoit que les versions de Pathfinder 2
        if ed == fiche.get("src") or (fiche.get("src") == "3.5" and ed == "2024"): continue
        v = fiche.get(key, {} if ed == "2024" else None)   # 3.5 et Pathfinder 1 n'entrent qu'école par école, après relecture   # la 3.5 n'entre qu'école par école, après relecture
        if v is None: continue
        src_idx = v.get("src_idx", idx)
        if src_idx not in base: continue
        fe = {**fiche, **{k: x for k, x in v.items() if k not in ("name", "alt")}, "src": {"PF1": "pf1", "PF2": "pf2", "PF2 remaniée": "pf2r"}.get(ed, ed), "src_idx": src_idx}
        # la famille et la combinaison de la version d'origine se conservent, même si l'autre édition type autrement ses dégâts
        if not fiche.get("grimoire") and forms[0]["fam"] in ("H", "A") and "fam" not in fe:
            fe["fam"] = forms[0]["fam"]
            if fe["fam"] == "H" and not fe.get("comb") and idx not in SRD:
                fe["comb"] = forms[0].get("comb")      # sort venu de la 3.5 : sa combinaison d'origine
            elif fe["fam"] == "H" and not fe.get("comb"):
                d0 = SRD.get(idx, {}).get("damage") or {}; d0 = d0[0] if isinstance(d0, list) else d0
                fe["comb"] = DAMAGE_COMBO.get((d0.get("damage_type") or {}).get("name")) or ECOLES[SRD[idx]["school"]["name"]][2]
        if "options" in v and v["options"] is None: fe.pop("options", None)
        # une option de même nom garde ce que le sort donne à percevoir (Cosmétique), sauf si la version le redit
        if v.get("options") and fiche.get("options"):
            bo = {o["label"]: o for o in fiche["options"]}
            fe["options"] = [dict({k: bo[o["label"]][k] for k in ("sens", "manif") if k in bo.get(o["label"], {})}, **o) for o in v["options"]]
        # en 3.5, la portée lue dans le texte est la vraie : une portée forcée pour la 5e ne la remplace pas
        if ed in ("3.5", "PF1", "PF2", "PF2 remaniée") and "loc" not in v: fe.pop("loc", None)
        if ed in ("PF2", "PF2 remaniée") and "niveau" not in v: fe.pop("niveau", None)      # le rang de Pathfinder 2 s'inscrit tel quel dans l'Interaction
        fe["alt"] = [dict(a, **{k: x for k, x in v.items() if k in ("impact", "impact_sats", "impact_add", "aoe", "options")}) if not a.get("grimoire") else dict(a)
                     for a in fiche.get("alt", [])]
        for a, extra in zip(fe["alt"], v.get("alt", [])): a.update(extra)
        fe["alt"] = [a for a in fe["alt"] if not a.get("drop")]   # une version peut retirer une forme alternative qui n'existe pas chez elle
        fe.pop("v24", None); fe.pop("v35", None); fe.pop("vpf", None); fe.pop("vp2", None); fe.pop("vr", None)
        nom = f" ({v['name']})" if v.get("name") else ""
        for f in _forms(idx, fe, single_note=False):
            if glyph_key(f) in seen: continue
            seen.add(glyph_key(f))
            f["label"] = f["label"] + f" — version {ed}" + nom
            what = ("Règles de 2024" if ed == "2024" else f"D&D 3.5, lanceur de référence de niveau {base[src_idx]['_cl']}" if ed == "3.5"
                    else "Pathfinder 2, édition d'origine" if ed == "PF2" else "Pathfinder 2, version remaniée" if ed == "PF2 remaniée"
                    else f"Pathfinder 1, lanceur de référence de niveau {base[src_idx]['_cl']}")
            f["notes"] = [f"{what}{nom} : la version change ce que le glyphe inscrit."] + [n for n in f["notes"] if not n.startswith("Pas de forme")]
            forms.append(f)
    return forms

def _faces_of(f):
    out = set()
    for r in f["rings"]:
        for w in r[2]:
            if norm(w) in ("LUMINEUX", "TENEBREUX"): out.add(norm(w).lower())
        for x in (r[4] if len(r) > 4 and r[4] else []):
            for q in x:
                if isinstance(q, tuple) and len(q) == 2 and q[0] == "sym" and q[1] in ("lumineux", "tenebreux"): out.add(q[1])
                elif isinstance(q, (list, tuple)):
                    for w in q:
                        if isinstance(w, str) and norm(w) in ("LUMINEUX", "TENEBREUX"): out.add(norm(w).lower())
    return out

def _autre_face(src, face):
    """la même fiche, tissée de l'autre face : les deux faces s'échangent partout, l'énergie propre à une face prend le nom de l'autre"""
    def m(o, energie=False):
        if isinstance(o, str):
            n = norm(o)
            if n == "LUMINEUX": return "ténébreux"
            if n == "TENEBREUX": return "lumineux"
            if energie and n == "NECROSE" and face == "lumineux": return "lumineux"
            if energie and n == "LUMIERE" and face == "tenebreux": return "ténébreux"
            return o
        if isinstance(o, tuple): return tuple(m(x, energie) for x in o)
        if isinstance(o, list): return [m(x, energie) for x in o]
        if isinstance(o, dict): return {k: m(x, energie) for k, x in o.items()}
        return o
    out = dict(src)
    for k in ("impact", "impact_add", "impact_plus", "impact_sats"):
        if k in out: out[k] = m(out[k], True)
    for k in ("cond", "cond_sats", "cible_note"):
        if k in out: out[k] = m(out[k])
    if "cible_sym" in out: out["cible_sym"] = [{"lumineux": "tenebreux", "tenebreux": "lumineux"}.get(x, x) for x in out["cible_sym"]]
    out["face"] = "ténébreux" if face == "tenebreux" else "lumineux"
    return out

def _forms(idx, fiche, single_note=True):
    fams = [fiche]
    for alt in fiche.get("alt", []):
        base = {k: v for k, v in fiche.items() if k not in ("grimoire", "alt", "notes", "label", "why_single", "options")}
        if alt.get("grimoire"): base = {"fr": fiche["fr"], **({"src": fiche["src"]} if fiche.get("src") else {})}
        fams.append({**base, **alt})
    forms, srcs = [], []
    for i, fam in enumerate(fams):
        opts = fiche.get("options")
        if not opts:
            forms.append(build_spell(idx, {k: v for k, v in fam.items() if k != "options"})); srcs.append(fam); continue
        for o in opts:
            o = dict(o); lab = o.pop("label")
            if o.pop("only_base", False) and i > 0: continue
            if "only" in o and o.pop("only") != i: continue
            src = {**{k: v for k, v in fam.items() if k != "options"}, **o}
            forms.append(build_spell(idx, src)); srcs.append({**src, "_opt": lab})
    if fiche.get("reciproque"):
        # canon : une face astrale ne va pas sans l'autre ; chaque forme qui n'en inscrit qu'une reçoit sa réciproque
        forms2, srcs2 = [], []
        for f, src in zip(forms, srcs):
            fa = _faces_of(f)
            if len(fa) != 1 or src.get("face"):
                forms2.append(f); srcs2.append(src); continue
            nat = fa.pop(); oth = "tenebreux" if nat == "lumineux" else "lumineux"
            nom = {"lumineux": "Forme lumineuse", "tenebreux": "Forme ténébreuse"}
            forms2.append(f); srcs2.append({**src, "_opt": (src["_opt"] + " — " + nom[nat].lower()) if src.get("_opt") else nom[nat]})
            src_o = _autre_face(src, oth)
            forms2.append(build_spell(idx, {k: v for k, v in src_o.items() if k != "_opt"}))
            srcs2.append({**src_o, "_opt": (src["_opt"] + " — " + nom[oth].lower()) if src.get("_opt") else nom[oth]})
        forms, srcs = forms2, srcs2
    if single_note and len(forms) == 1 and not fiche.get("single_note") is False:
        f0 = forms[0]
        if fiche.get("why_single"): f0["notes"].append(fiche["why_single"])
        elif f0["fam"] == "H": f0["notes"].append("Pas de forme arcane : le sort façonne la matière elle-même, que l'Arcane ne touche pas.")
        elif f0["fam"] == "A": f0["notes"].append("Pas de forme hybride : aucune combinaison naturelle ne porte cet effet.")
    for f, src in zip(forms, srcs):
        base_lab = src.get("label") or {"A": "Forme arcane", "H": "Forme hybride", "R": "Art rare"}[f["fam"]]
        f["label"] = (f"{base_lab} — {src['_opt']}" if len(fams) > 1 else src["_opt"]) if src.get("_opt") else base_lab
    return forms

def words_of(sp, declared=True):
    """les mots d'Alde employés par le glyphe : noyau, cercles, satellites astraux"""
    out = []
    def add(w):
        if w and w not in out: out.append(w)
    c = sp["core"]
    if c[0] == "hyb" and c[2]: add(c[2])
    if c[0] == "chrono": add(c[4])
    for crit, v, words, *rest in sp["rings"]:
        add(crit)
        for w in words: add(w)
        for st in (rest[1] if len(rest) > 1 else []):
            for w in (st[2].split() if len(st) > 2 and st[2] else []): add(w)
        if v is not None and SP.val(v, "up")[1]: add("FOIS")
    if sp["split"]:
        for side in sp["split"]:
            for cr in side:
                if cr != "NOYAU": add(cr)
    return out

SCHOOL_FR = {k: v[0] for k, v in ECOLES.items()}
def fr_cast(t):
    t = t.lower()
    m = {"1 action": "1 action", "1 bonus action": "1 action bonus", "1 reaction": "1 réaction", "action": "1 action", "bonus action": "1 action bonus", "reaction": "1 réaction"}
    if t in m: return m[t]
    p = parse_time(t); return fr_time(*p) if p else t
def fr_range(r):
    rl = r.lower()
    if rl == "self": return "soi"
    if rl.startswith("self"):
        m = re.search(r"(\d+)-foot[- ](\w+)", rl)
        shapes = {"cone": "cône", "radius": "rayon", "line": "ligne", "cube": "cube", "sphere": "sphère", "hemisphere": "hémisphère"}
        return f"soi ({shapes.get(m.group(2), m.group(2))} de {ft2m(int(m.group(1)))} m)" if m else "soi"
    if rl == "touch": return "contact"
    if rl == "sight": return "à vue"
    if rl == "unlimited": return "illimitée"
    if rl == "special": return "spéciale"
    m = re.match(r"(\d+)\s*(feet|mile|miles)", rl)
    if m:
        n = int(m.group(1))
        return f"{n} pieds ({ft2m(n)} m)" if "feet" in m.group(2) else f"{n} mile{'s' if n > 1 else ''}"
    return r
def fr_duration(d):
    dl = d.lower()
    if "instantaneous" in dl: return "instantanée"
    if "until dispelled" in dl: return "jusqu'à dissipation" + (" ou déclenchement" if "triggered" in dl else "")
    if "special" in dl: return "spéciale"
    m = re.search(r"(\d+)\s*(second|round|minute|hour|day)", dl)
    if not m: return d
    n, u = int(m.group(1)), m.group(2)
    fr = {"second": ("seconde", "secondes"), "round": ("round", "rounds"), "minute": ("minute", "minutes"), "hour": ("heure", "heures"), "day": ("jour", "jours")}[u][0 if n == 1 else 1]
    return ("concentration, jusqu'à " if "up to" in dl else "") + f"{n} {fr}"
def dnd_line(s, fr):
    lv = "tour de magie" if s["level"] == 0 else f"niveau {s['level']}"
    rit = " (rituel)" if s.get("ritual") else ""
    if s.get("_ed") in ("pf2", "pf2r"):
        ed_ = "édition d'origine" if s["_ed"] == "pf2" else "version remaniée"
        rg_ = "tour de magie" if s["level"] == 0 else f"rang {s['_rang']}"
        if s.get("_rituel"):
            n_ = s["_officiants"]
            return (f"Pathfinder 2 ({ed_}, {s['_book']}, {s['_rarete']}) : rituel de rang {s['_rang']} · {SCHOOL_FR[s['school']['name']].lower()} · exécution {fr_cast(s['casting_time'])}"
                    f" · {n_} officiant{'s' if n_ > 1 else ''} en plus du meneur · portée {fr_range(s['range'])} · durée {fr_duration(s['duration'])}")
        return f"Pathfinder 2 ({ed_}, {s['_book']}, {s['_rarete']}) : {rg_} · {SCHOOL_FR[s['school']['name']].lower()} · incantation {fr_cast(s['casting_time'])} · portée {fr_range(s['range'])} · durée {fr_duration(s['duration'])}"
    if s.get("_ed") == "er":
        return (f"Elden Ring ({s['_kind']}, {s['_origine']}) : {'tour de magie' if s['level'] == 0 else 'niveau équivalent ' + str(s['level'])} · {SCHOOL_FR[s['school']['name']].lower()}"
                f" · portée {fr_range(s['range'])} · durée {'tant que le sort est tenu' if s['duration'] == 'Concentration' else fr_duration(s['duration'])}")
    if s.get("_ed") == "pf1":
        return f"Pathfinder 1 (lanceur de niveau {s['_cl']}, {s['_book']}) : {lv} · {SCHOOL_FR[s['school']['name']].lower()} · incantation {fr_cast(s['casting_time'])} · portée {fr_range(s['range'])} · durée {fr_duration(s['duration'])}"
    if s.get("_ed") == "3.5":
        return f"D&amp;D 3.5 (lanceur de niveau {s['_cl']}) : {lv} · {SCHOOL_FR[s['school']['name']].lower()} · incantation {fr_cast(s['casting_time'])} · portée {fr_range(s['range'])} · durée {fr_duration(s['duration'])}"
    ed = " (règles de 2024)" if s.get("_ed") else ""
    return f"D&amp;D 5e{ed} : {lv}{rit} · {SCHOOL_FR[s['school']['name']].lower()} · incantation {fr_cast(s['casting_time'])} · portée {fr_range(s['range'])} · durée {fr_duration(s['duration'])}"

# ---------- bande ----------
def band_rings(sp):
    lum = sp["split"][0] if sp["split"] else None
    out = []
    for crit, v, words, reading, *rest in sp["rings"]:
        if lum is not None: pol = "up" if crit in lum else "down"
        else: pol = "down" if (sp["core"][0] == "verb" and sp["core"][2]) else "up"
        spec, mult, ok = SP.val(v, pol) if v is not None else ([], False, False)
        raw = rest[0] if rest else []
        if len(raw) >= 2:
            # en bandeau, plusieurs satellites se centrent de part et d'autre du milieu, à intervalles égaux
            # (deux satellites : au quart et aux trois quarts, l'est et l'ouest du cercle déroulé)
            k = len(raw); xs = [0.5 + (i - (k - 1) / 2) / k for i in range(k)]
            raw = [((270 - 360 * x) % 360, sv, *rest_) for x, (d, sv, *rest_) in zip(xs, raw)]
        sats = [((90 if isinstance(d, str) or d % 360 == 270 else d), SP.val(sv, pol)[0], SP.sat_label(sv, x, pol), SP.sat_opts(x, pol)) for d, sv, *x in raw]
        out.append(dict(label=" ".join([crit] + list(words) + (["FOIS"] if mult else [])), spec=spec, sats=sats))
    return out
def band_svg(sp, declared):
    split = sp["split"] if declared else sp["bsplit"]
    main = BG.band(sp["core"], band_rings(sp), declared)
    left = BG.astral_band("ten", split[1]) if split and (split[1] or declared) else None
    right = BG.astral_band("lum", split[0]) if split and (split[0] or declared) else None
    return BG.compose(main, left, right)


def sources_of(idx, fiche):
    """d'où vient le sort : chaque édition où il existe, que son glyphe y change ou non"""
    out = set()
    src = fiche.get("src")
    if src is None and idx in SRD: out.add("5.1")
    if src == "2024": out.add("5.2")
    if src == "3.5": out.add("3.5")
    if src == "pf1": out.add("pf1")
    if src in ("pf2", "pf2r", "er"): out.add(src)
    for ed, base, key in (("5.2", SRD24, "v24"), ("3.5", SRD35, "v35"), ("pf1", PF1, "vpf"), ("pf2", PF2, "vp2"), ("pf2r", PF2R, "vr")):
        v = fiche.get(key, {} if ed == "5.2" else None)
        if v is None or (src is not None and not (src == "3.5" and ed == "pf1") and not (ed in ("pf2", "pf2r") and src != ed)): continue
        ids = [v.get("src_idx", idx)] + [o.get("src_idx") for o in (v.get("options") or []) if o.get("src_idx")]
        if any(i in base for i in ids): out.add(ed)
    return sorted(out)
