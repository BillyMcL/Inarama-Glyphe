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

UNITS = {"minute": "MINUTES", "hour": "HEURES", "day": "JOURS", "round": "SECONDES"}
UNIT_FR = {"MINUTES": ("minute", "minutes"), "HEURES": ("heure", "heures"), "JOURS": ("jour", "jours"), "SECONDES": ("seconde", "secondes")}
def fr_time(v, u):
    if v == "plein": return "jusqu'à dissipation"
    return f"{v} {UNIT_FR[u][0 if v == 1 else 1]}"
def parse_time(t):
    t = t.lower().replace("up to ", "")
    if "instantaneous" in t or "special" in t: return None
    if "until dispelled" in t or "permanent" in t: return ("plein", None)
    if t.strip() == "concentration": return ("plein", None)   # concentration sans durée maximale : infinie
    m = re.match(r"(\d+)\s*(round|minute|hour|day)", t)
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
 "sphere": ("plein", [(90, "plein")], "sphère", "DIAMETRE"),
 "cube": (4, [(90, "plein")], "cube", "COTE"),
 "cone": (3, [(90, 2), (210, "plein")], "cône (hauteur 2, rayon 1)", "LONGUEUR"),
 "line": (1, [(90, "plein")], "ligne", "LONGUEUR"),
 "cylinder": (9, [(90, "plein"), (210, "plein")], "cylindre", "DIAMETRE"),
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
def place_sats(sats):
    """satellites annotés (valeur, [mots]) : un seul se place au nord ou au sud ; deux, de part et d'autre"""
    if not sats: return []
    # sur le cercle, plusieurs satellites d'un même encart se répartissent symétriquement : opposés, à 120°, en croix…
    n = len(sats)
    angles = ["NS"] if n == 1 else [90, 270] if n == 2 else [(90 + k * 360 / n) % 360 for k in range(n)]
    return [(a, v, " ".join(word(w) for w in ws)) for a, (v, ws) in zip(angles, sats)]
def sat_reading(sats):
    if not sats: return ""
    return "".join(f" ; satellite {'vide' if v is None else v} « {' · '.join(shown(w) for w in ws)} »" for v, ws in sats)

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
    s = {"2024": SRD24, "3.5": SRD35, "pf1": PF1}.get(fiche.get("src"), SRD)[fiche.get("src_idx", idx)]
    fr = fiche["fr"]
    level = s["level"]
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
        if fiche.get("cible_note"):
            words += [word(w) for w in fiche["cible_note"]]
            reading += ", précisé « " + " · ".join(shown(w) for w in fiche["cible_note"]) + " »"
        sats = []
        if fiche.get("qty_cible"):
            q = fiche["qty_cible"]; sats = [(90, q)]
            reading += " ; satellite Quantité " + ("plein : tous ceux que je choisis" if q == "plein" else str(q))
        rings.append(("CIBLE", val, words, reading, sats))
    # 3-4 Forme, Ampleur
    aoe = fiche.get("aoe") or s.get("area_of_effect")
    if aoe and not fiche.get("no_aoe"):
        sil, sats, nom, gr = FORMES[aoe["type"]]
        size = ft2m(aoe["size"] * (2 if gr == "DIAMETRE" else 1)); unit, u = "METRES", "m"
        if size >= 1000: size, unit, u = rnd(size / 1000), "KILOMETRES", "km"
        rings.append(("FORME", sil, [], nom, sats))
        lab = {"DIAMETRE": "de diamètre", "COTE": "de côté", "LONGUEUR": "de long"}[gr]
        rings.append(("AMPLEUR", size, [gr, unit], f"{size} {u} {lab}"))
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
        rings.append(("LOCALISATION", loc[0], [loc[1]] if loc[1] else [], loc[2]))
    # 7 Condition
    if fiche.get("cond"):
        cw = [word(w) for w in fiche["cond"]]
        rd = " ; ".join(f"« {shown(w)} »" for w in fiche["cond"])
        rings.append(("CONDITION", len(cw), cw, rd + sat_reading(fiche.get("cond_sats")), place_sats(fiche.get("cond_sats"))))
    # 8 Impact
    imp = fiche.get("impact")
    if imp is None and (dmg or s.get("heal_at_slot_level")):
        if dmg:
            table = dmg.get("damage_at_slot_level") or dmg.get("damage_at_character_level") or {}
            d = table.get(str(level)) or (list(table.values())[0] if table else None)
            med = MEDIUM.get(dtype)
            if d: imp = (rnd(dice_avg(d)), med, f"{d} en moyenne")
        else:
            d = s["heal_at_slot_level"].get(str(level)) or list(s["heal_at_slot_level"].values())[0]
            imp = (rnd(dice_avg(d)), None, d.replace("MOD", "3") + " en moyenne, avec un modificateur de +3")
    if imp:
        v, med, why = imp if len(imp) == 3 else (*imp, "")
        meds = med if isinstance(med, list) else ([med] if med else [])
        add = fiche.get("impact_add", [])
        words = ([word(m) for m in meds] if meds else ["VIE"]) + [word(a) for a in add]
        nat = ((", " + " · ".join(shown(m) for m in meds)) if meds else " de vie") + ((" · " if meds else ", ") + " · ".join(shown(a) for a in add) if add else "")
        head = "plein" if v == "plein" else f"intensité {v}"
        rings.append(("IMPACT", v, words, head + nat + (f" ({why})" if why else "") + sat_reading(fiche.get("impact_sats")),
                      place_sats(fiche.get("impact_sats"))))
    # 9 Quantité
    if fiche.get("qty"):
        rings.append(("QUANTITE", fiche["qty"], [], f"{fiche['qty']} instances du sort"))
    # 10 Composante
    if fiche.get("comp"):
        mat = (s.get("material") or "").lower()
        consumed = fiche.get("consumed", "consume" in mat)
        cw = [word(w) for w in fiche["comp"]] + (["CONSOMME"] if consumed else [])
        c_ = cost(s); val = None; rd = ", ".join(shown(w) for w in fiche["comp"]) + (", consommé" if consumed else ", accompagnant")
        if c_:
            val = c_[0]; cw.append(word(c_[1])); rd = f"valeur {c_[0]} pièce{'s' if c_[0] > 1 else ''} de {c_[1]} ; " + rd
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
    # 12 Cosmétique
    if fiche.get("cosm"):
        v, w = fiche["cosm"]
        rings.append(("COSMETIQUE", v, [word(w)], f"{w.lower()}, " + ("au maximum" if v == "plein" else f"degré {v}")))
    # une valeur qui demanderait plus de quatre formes est arrondie à la plus proche qui s'écrit simplement
    def nforms(n): return len(SP.val(n, "up")[0])
    for i, r in enumerate(rings):
        v = r[1]
        if isinstance(v, int) and nforms(v) > 4:
            best = min((x for x in range(max(1, v - v // 4), v + v // 4 + 2) if nforms(x) <= 4), key=lambda x: (abs(x - v), x))
            rings[i] = (r[0], best, r[2], r[3] + f" ; arrondi de {v} à {best} pour s'écrire en {nforms(best)} formes", *r[4:])
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
    svg, rows = SP.build(core, pol, rings, r0, split)
    return dict(idx=idx, fr=fr, en=s["name"], level=level, ecole=ecole, fam=fam, verb=verb, core=core, rings=rings, split=split,
                bsplit=SP.PART[0], svg=svg, rows=rows, r0=r0, notes=notes, dnd=dnd_line(s, fr), pol=pol)

def glyph_key(f):
    return (repr(f["core"]), repr([(r[0], r[1], tuple(r[2]), repr(r[4:5])) for r in f["rings"]]), repr(f["split"]))

def build_forms(idx, fiche):
    """toutes les formes d'un sort ; puis, pour un sort qui existe aussi dans les règles de 2024,
    ses formes de 2024 qui donnent un glyphe différent (un glyphe identique est le même sort)"""
    forms = _forms(idx, fiche)
    if fiche.get("src") == "pf1": return forms
    seen = {glyph_key(f) for f in forms}
    for ed, base, key in (("2024", SRD24, "v24"), ("3.5", SRD35, "v35"), ("PF1", PF1, "vpf")):
        if ed == fiche.get("src") or (fiche.get("src") == "3.5" and ed == "2024"): continue
        v = fiche.get(key, {} if ed == "2024" else None)   # 3.5 et Pathfinder 1 n'entrent qu'école par école, après relecture   # la 3.5 n'entre qu'école par école, après relecture
        if v is None: continue
        src_idx = v.get("src_idx", idx)
        if src_idx not in base: continue
        fe = {**fiche, **{k: x for k, x in v.items() if k not in ("name", "alt")}, "src": {"PF1": "pf1"}.get(ed, ed), "src_idx": src_idx}
        # la famille et la combinaison de la version d'origine se conservent, même si l'autre édition type autrement ses dégâts
        if not fiche.get("grimoire") and forms[0]["fam"] in ("H", "A") and "fam" not in fe:
            fe["fam"] = forms[0]["fam"]
            if fe["fam"] == "H" and not fe.get("comb") and idx not in SRD:
                fe["comb"] = forms[0].get("comb")      # sort venu de la 3.5 : sa combinaison d'origine
            elif fe["fam"] == "H" and not fe.get("comb"):
                d0 = SRD.get(idx, {}).get("damage") or {}; d0 = d0[0] if isinstance(d0, list) else d0
                fe["comb"] = DAMAGE_COMBO.get((d0.get("damage_type") or {}).get("name")) or ECOLES[SRD[idx]["school"]["name"]][2]
        if "options" in v and v["options"] is None: fe.pop("options", None)
        # en 3.5, la portée lue dans le texte est la vraie : une portée forcée pour la 5e ne la remplace pas
        if ed in ("3.5", "PF1") and "loc" not in v: fe.pop("loc", None)
        fe["alt"] = [dict(a, **{k: x for k, x in v.items() if k in ("impact", "impact_sats", "impact_add", "aoe", "options")}) if not a.get("grimoire") else dict(a)
                     for a in fiche.get("alt", [])]
        for a, extra in zip(fe["alt"], v.get("alt", [])): a.update(extra)
        fe.pop("v24", None); fe.pop("v35", None); fe.pop("vpf", None)
        nom = f" ({v['name']})" if v.get("name") else ""
        for f in _forms(idx, fe, single_note=False):
            if glyph_key(f) in seen: continue
            seen.add(glyph_key(f))
            f["label"] = f["label"] + f" — version {ed}" + nom
            what = ("Règles de 2024" if ed == "2024" else f"D&D 3.5, lanceur de référence de niveau {base[src_idx]['_cl']}" if ed == "3.5"
                    else f"Pathfinder 1, lanceur de référence de niveau {base[src_idx]['_cl']}")
            f["notes"] = [f"{what}{nom} : la version change ce que le glyphe inscrit."] + [n for n in f["notes"] if not n.startswith("Pas de forme")]
            forms.append(f)
    return forms

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
    m = re.search(r"(\d+)\s*(round|minute|hour|day)", dl)
    if not m: return d
    n, u = int(m.group(1)), m.group(2)
    fr = {"round": ("round", "rounds"), "minute": ("minute", "minutes"), "hour": ("heure", "heures"), "day": ("jour", "jours")}[u][0 if n == 1 else 1]
    return ("concentration, jusqu'à " if "up to" in dl else "") + f"{n} {fr}"
def dnd_line(s, fr):
    lv = "tour de magie" if s["level"] == 0 else f"niveau {s['level']}"
    rit = " (rituel)" if s.get("ritual") else ""
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
        if len(raw) >= 2 and crit != "FORME":
            # en bandeau, plusieurs satellites se centrent de part et d'autre du milieu, à intervalles égaux
            # (deux satellites : au quart et aux trois quarts, l'est et l'ouest du cercle déroulé)
            k = len(raw); xs = [0.5 + (i - (k - 1) / 2) / k for i in range(k)]
            raw = [((270 - 360 * x) % 360, sv, *rest_) for x, (d, sv, *rest_) in zip(xs, raw)]
        sats = [((90 if d == "NS" or d % 360 == 270 else d), SP.val(sv, pol)[0], (x[0] if x else "")) for d, sv, *x in raw]
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
    for ed, base, key in (("5.2", SRD24, "v24"), ("3.5", SRD35, "v35"), ("pf1", PF1, "vpf")):
        v = fiche.get(key, {} if ed == "5.2" else None)
        if v is None or (src is not None and not (src == "3.5" and ed == "pf1")): continue
        ids = [v.get("src_idx", idx)] + [o.get("src_idx") for o in (v.get("options") or []) if o.get("src_idx")]
        if any(i in base for i in ids): out.add(ed)
    return sorted(out)
