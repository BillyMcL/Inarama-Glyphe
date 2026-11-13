"""SRD 3.5 (Open Game License 1.0a) : lecture des sorts et mise au format interne du moteur.

Les valeurs qui dépendent du niveau du lanceur sont calculées pour le lanceur de référence :
le plus petit lanceur capable de lancer le sort (niveau du sort × 2 − 1 pour un mage ou un prêtre).
"""
import os, re, glob

UNIV = {"Wish": "Conjuration", "Limited Wish": "Conjuration", "Prestidigitation": "Transmutation", "Arcane Mark": "Transmutation", "Permanency": "Abjuration"}
ECOLES35 = {"Abjuration", "Conjuration", "Divination", "Enchantment", "Evocation", "Illusion", "Necromancy", "Transmutation"}
TYPES = {"acid": "Acid", "fire": "Fire", "cold": "Cold", "electricity": "Lightning", "sonic": "Thunder"}
PAL = {0: 1, 1: 2, 2: 4, 3: 5, 4: 7}

def idx_of(name):
    n = name.lower().replace("’", "").replace("'", "")
    return re.sub(r"[^a-z0-9]+", "-", n).strip("-")

def _caster_level(levels):
    """niveau du sort retenu et niveau du lanceur de référence"""
    for cls in ("Sor/Wiz", "Clr", "Drd"):
        if cls in levels: L = levels[cls]; return L, max(1, 2 * L - 1)
    if "Brd" in levels: L = levels["Brd"]; return L, max(1, 3 * L - 2)
    for cls in ("Pal", "Rgr"):
        if cls in levels: L = levels[cls]; return L, PAL.get(L, 2 * L)
    if levels: L = min(levels.values()); return L, max(1, 2 * L - 1)
    return None, None

def _feet(rng, CL):
    r = rng.strip()
    m = re.match(r"(Close|Medium|Long)", r)
    if m: return {"Close": 25 + 5 * (CL // 2), "Medium": 100 + 10 * CL, "Long": 400 + 40 * CL}[m.group(1)]
    m = re.match(r"(\d+) ft\.?/level", r)
    if m: return int(m.group(1)) * CL
    m = re.match(r"(\d+) ft", r)
    if m: return int(m.group(1))
    return None

def _range(rng, CL):
    r = (rng or "").strip()
    if not r or r.lower().startswith("see text"): return "Special"
    if r.lower().startswith("personal or touch") or r.lower().startswith("touch"): return "Touch"
    if r.lower().startswith("personal"): return "Self"
    if r.lower().startswith("unlimited"): return "Unlimited"
    m = re.match(r"(\d+) miles?", r)
    if m: return f"{m.group(1)} miles"
    f = _feet(r, CL)
    return f"{f} feet" if f is not None else "Special"

UNIT = {"round": "round", "rounds": "round", "min.": "minute", "minute": "minute", "minutes": "minute",
        "hour": "hour", "hours": "hour", "day": "day", "days": "day"}
def _duration(d, CL):
    t = (d or "").replace("(D)", "").strip()
    tl = t.lower()
    if not t or tl.startswith("see text"): return "Special"
    if tl.startswith("instantaneous"): return "Instantaneous"
    if tl.startswith("permanent"): return "Until dispelled"
    conc = tl.startswith("concentration")
    m = re.search(r"(\d+|one) (rounds|round|min\.|minutes|minute|hours|hour|days|day)(/level| per level)?", tl)     # le pluriel d'abord : « 10 minutes/level » se multiplie bien par le niveau
    if not m: return "Concentration" if conc else "Special"
    n = 1 if m.group(1) == "one" else int(m.group(1))
    if m.group(3): n *= CL
    u = UNIT[m.group(2)]
    return ("Up to " if conc else "") + f"{n} {u}{'s' if n > 1 else ''}"

def _cast(c):
    t = (c or "1 standard action").lower()
    if "action" in t: return "1 action"
    m = re.match(r"(\d+|one) (round|rounds|minute|minutes|hour|hours)", t)
    if m:
        n = 1 if m.group(1) == "one" else int(m.group(1))
        return f"{n} {m.group(2).rstrip('s')}{'s' if n > 1 else ''}"
    if "full round" in t: return "1 round"
    return "1 action"

def _area(fields, rng_feet):
    s = " ".join(fields.get(k, "") for k in ("area", "effect", "target or area", "target, effect, or area", "area or target")).lower()
    m = re.search(r"cylinder \((\d+)-ft\.? radius", s)
    if m: return {"type": "cylinder", "size": int(m.group(1))}
    m = re.search(r"(\d+)-ft\.?-radius", s)
    if m: return {"type": "sphere", "size": int(m.group(1))}
    if "cone" in s and rng_feet: return {"type": "cone", "size": rng_feet}
    m = re.search(r"(\d+)-ft\.?[- ]line", s)
    if m: return {"type": "line", "size": int(m.group(1))}
    if "line" in s and rng_feet: return {"type": "line", "size": rng_feet}
    m = re.search(r"(\d+)-ft\.? cube", s)
    if m: return {"type": "cube", "size": int(m.group(1))}
    return None

def _damage(text, L, CL):
    t = text.lower()
    m = re.search(r"(\d+)d(\d+) points? of (\w+ )?damage per (?:caster )?level(?:[^(]*\(maximum (\d+)d\d+\))?", t)
    if m:
        n = int(m.group(1)) * CL
        if m.group(4): n = min(n, int(m.group(4)))
        dice, typ = f"{n}d{m.group(2)}", (m.group(3) or "").strip()
    else:
        m = re.search(r"(\d+)d(\d+) points? of (\w+ )?damage per two (?:caster )?levels(?:[^(]*\(maximum (\d+)d\d+\))?", t)
        if m:
            n = max(1, int(m.group(1)) * (CL // 2))
            if m.group(4): n = min(n, int(m.group(4)))
            dice, typ = f"{n}d{m.group(2)}", (m.group(3) or "").strip()
        else:
            m = re.search(r"(\d+)d(\d+)(?: points?)? of (\w+ )?damage", t)
            if not m: return None
            dice, typ = f"{m.group(1)}d{m.group(2)}", (m.group(3) or "").strip()
    name = TYPES.get(typ)
    return {"damage_type": {"name": name} if name else {}, "damage_at_slot_level": {str(L): dice}}

def _heal(text, CL):
    m = re.search(r"cures? (\d+)d(\d+) points of damage \+1 point per caster level \(maximum \+(\d+)\)", text.lower())
    if not m: return None
    return f"{m.group(1)}d{m.group(2)} + {min(CL, int(m.group(3)))}"

def _parse(datadir):
    raw = {}
    for f in sorted(glob.glob(os.path.join(datadir, "spells-*.md"))):
        t = open(f, encoding="utf-8").read()
        for blk in re.split(r"\n## ", t)[1:]:
            lines = blk.split("\n")
            name = lines[0].strip()
            school = lines[2].replace("\\", "").strip() if len(lines) > 2 else ""
            fields = {k.lower(): v.strip() for k, v in re.findall(r"\*\*([^*]+):\*\*\s*(.*)", blk)}
            body = "\n".join(l for l in lines[3:] if not l.startswith("**"))
            raw[idx_of(name)] = dict(name=name, school=school, fields=fields, text=body)
    # « fonctionne comme X, sauf que… » : les champs absents viennent du sort de base
    def base_of(r):
        m = re.search(r"functions like _([^_]+)_", r["text"])
        if not m: return None
        b = m.group(1).strip().rstrip(",").lower()
        for pre in ("mass ", "greater ", "lesser "):
            if b.startswith(pre): b = b[len(pre):] + ", " + pre.strip()
        return idx_of(b)
    for _ in range(3):
        for k, r in raw.items():
            b = base_of(r)
            if b in raw and b != k:
                for fk, fv in raw[b]["fields"].items():
                    r["fields"].setdefault(fk, fv)
    return raw

def load(datadir):
    out = {}
    for k, r in _parse(datadir).items():
        f = r["fields"]
        levels = {}
        for part in f.get("level", "").split(","):
            m = re.match(r"\s*(.+?)\s+(\d+)\s*$", part)
            if m: levels[m.group(1).strip()] = int(m.group(2))
        L, CL = _caster_level(levels)
        sch = r["school"].split(" ")[0]
        if sch == "Universal": sch = UNIV.get(r["name"], sch)   # école universelle : rattachée à l'école 5e la plus proche
        if L is None or sch not in ECOLES35: continue
        sub = re.findall(r"\(([^)]+)\)", r["school"]); desc = re.findall(r"\[([^\]]+)\]", r["school"])
        rng = _range(f.get("range"), CL)
        rf = _feet(f.get("range", ""), CL)
        text = r["text"]
        mat = ""
        for m in re.finditer(r"_(?:Arcane )?(?:Material Component|Focus|Material Components)_?:?_?\s*(.*)", text):
            if re.search(r"\d[\d,]* gp", m.group(1)): mat = m.group(1); break
        xp = re.search(r"_XP Cost:?_?:?\s*([\d,]+) XP", text)
        if not xp and r["name"] == "Wish": xp = re.search(r"([\d,]+) XP", "5,000 XP")   # « 5,000 XP or more » : le minimum
        rec = dict(index=k, name=r["name"], level=L, school={"name": sch}, casting_time=_cast(f.get("casting time")),
                   range=rng, duration=_duration(f.get("duration"), CL), concentration="concentration" in f.get("duration", "").lower(),
                   ritual=False, material=mat or None, desc=[text], _ed="3.5", _cl=CL, _sub=sub, _descr=desc,
                   _xp=int(xp.group(1).replace(",", "")) if xp else None, _fields=f)
        a = _area(f, rf)
        if a: rec["area_of_effect"] = a
        h = _heal(text, CL)
        if h: rec["heal_at_slot_level"] = {str(L): h}
        else:
            d = _damage(text, L, CL)
            if d: rec["damage"] = d
        out[k] = rec
    return out
