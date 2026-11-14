"""Pathfinder 2 (édition d'origine sous Open Game License 1.0a, version remaniée sous licence ORC, Paizo) :
lecture des sorts et mise au format interne du moteur.

Source des données : relevé Pf2eTools (code sous licence MIT), les deux éditions ensemble ; chaque entrée remaniée porte
« remaster ». Les sorts focalisés et les rituels sont lus mais ne sont pas encore traités. Le rang vaut le niveau ; un tour
de magie vaut 0. La version remaniée n'a plus d'écoles : un sort qui n'existe que là reçoit la sienne dans ecoles-remanie.json.
"""
import json, re, os
from srd35 import idx_of

SCH = {"abjuration": "Abjuration", "conjuration": "Conjuration", "divination": "Divination", "enchantment": "Enchantment",
       "evocation": "Evocation", "illusion": "Illusion", "necromancy": "Necromancy", "transmutation": "Transmutation"}
DMG = {"fire": "Fire", "cold": "Cold", "electricity": "Lightning", "sonic": "Thunder", "acid": "Acid", "poison": "Poison",
       "negative": "Necrotic", "void": "Necrotic", "positive": "Radiant", "vitality": "Radiant", "mental": "Psychic", "force": "Force",
       "bludgeoning": "Bludgeoning", "piercing": "Piercing", "slashing": "Slashing", "good": "Radiant", "evil": "Necrotic",
       "spirit": "Force"}

def _flat(e):
    if isinstance(e, str): return e
    if isinstance(e, list): return " ".join(_flat(x) for x in e)
    if isinstance(e, dict):
        if e.get("type") == "successDegree": return " ".join(f"[{k}] {_flat(v)}" for k, v in e["entries"].items())
        return " ".join(_flat(v) for k, v in e.items() if k in ("entries", "items", "name", "entry", "rows"))
    return str(e)
def _clean(t): return re.sub(r"\s+", " ", re.sub(r"\{@\w+ ([^}|]+)[^}]*\}", r"\1", t))

def _traits(x): return [t.lower() for t in x.get("traits", []) if isinstance(t, str)]
def focalise(x): return bool(x.get("focus") or x.get("type") == "Focus")
def tour(x): return "cantrip" in _traits(x) or x.get("type") == "Cantrip"
def rarete(x):
    t = _traits(x)
    return "rare" if ("rare" in t or "unique" in t) else "peu courant" if "uncommon" in t else "courant"

def _cast(c):
    if not c or c.get("unit") in ("action", "reaction", "free", "varies"): return "1 action"
    n = c.get("number", 1); u = c["unit"]
    return f"{n} {u}{'s' if n > 1 else ''}"
def _range(r):
    if not r: return "Self"
    u = r.get("unit"); n = r.get("number", 1)
    if u == "touch": return "Touch"
    if u == "feet": return f"{n} feet" if n else "Self"
    if u == "mile": return f"{n} mile{'s' if n > 1 else ''}"
    if u == "planetary": return "Unlimited"
    return "Special"
def _duration(d):
    if not d: return "Instantaneous"
    u = d.get("unit"); n = d.get("number", 1); sus = "Up to " if d.get("sustained") else ""
    if u == "unlimited": return "Concentration" if d.get("sustained") else "Until dispelled"
    if u == "turn": return "1 round"
    if u in ("round", "minute", "hour", "day"): return f"{sus}{n} {u}{'s' if n > 1 else ''}"
    e = (d.get("entry") or "").lower()
    if "daily preparations" in e: return "24 hours"
    return "Special"
def _area(a):
    if not a: return None
    e = (a.get("entry") or "").lower()
    m = re.search(r"(\d+)-foot[- ](burst|emanation|cone|line|cube)", e)
    if not m: return None
    return {"type": {"burst": "sphere", "emanation": "sphere", "cone": "cone", "line": "line", "cube": "cube"}[m.group(2)], "size": int(m.group(1))}
def _damage(txt, L):
    m = re.search(r"(\d+d\d+(?:\s*\+\s*\d+)?) (?:points of )?(\w+) damage", txt)
    if not m or m.group(2).lower() not in DMG: return None
    return {"damage_type": {"name": DMG[m.group(2).lower()]}, "damage_at_slot_level": {str(L): m.group(1).replace(" ", "")}}

def load(path):
    """renvoie (origine, remanié) : deux dictionnaires de sorts ordinaires, clés en nom anglais normalisé"""
    ecoles = {}
    p2 = os.path.join(os.path.dirname(path), "ecoles-remanie.json")
    if os.path.exists(p2): ecoles = json.load(open(p2, encoding="utf-8"))
    raw = json.load(open(path, encoding="utf-8"))
    out = ({}, {})
    for x in raw:                                   # l'école des sorts d'origine, pour leurs homonymes remaniés
        if not x.get("remaster"):
            s_ = next((SCH[t] for t in _traits(x) if t in SCH), None)
            if s_: ecoles.setdefault(idx_of(x["name"]), s_)
    for x in raw:
        if focalise(x): continue
        k = idx_of(x["name"]); rem = bool(x.get("remaster"))
        sch = next((SCH[t] for t in _traits(x) if t in SCH), None) or ecoles.get(k)
        if not sch or k in out[rem]: continue
        L = 0 if tour(x) else x["level"]
        desc = _clean(_flat(x["entries"]))
        comp = x.get("components")
        comps = sorted({c for g in comp for c in g}) if comp else None      # version remaniée : composantes non données
        rec = dict(index=k, name=x["name"], level=L, school={"name": sch}, casting_time=_cast(x.get("cast")),
                   range=_range(x.get("range")), duration=_duration(x.get("duration")), concentration=bool((x.get("duration") or {}).get("sustained")),
                   ritual=False, material=x.get("cost"), desc=[desc], components=comps, _ed="pf2r" if rem else "pf2", _cl=None, _xp=None,
                   _book=x["source"], _rarete=rarete(x), _rang=x["level"], _traits=_traits(x), _cibles=x.get("targets"),
                   _fields={"target": x.get("targets"), "area": (x.get("area") or {}).get("entry"), "components": None})
        a = _area(x.get("area"))
        if a: rec["area_of_effect"] = a
        d = _damage(desc, L)
        if d: rec["damage"] = d
        out[rem][k] = rec
    return out
