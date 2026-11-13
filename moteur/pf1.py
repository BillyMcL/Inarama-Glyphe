"""Pathfinder 1 (Open Game License 1.0a, Paizo) : lecture des sorts et mise au format interne du moteur.

Source des données : relevé d'Archives of Nethys (SpellTable-pf1e, licence MIT), tous les sorts, légaux ou non en
Pathfinder Society (le tri se fait à la relecture, dans fiches.py), Technology Guide écarté. Les valeurs « par niveau » sont calculées au lanceur de référence :
le plus petit lanceur capable du sort.
"""
import json, re
from srd35 import idx_of, _range, _duration, _cast, _feet, _damage, _heal, TYPES

FULL = {"sorcerer/wizard", "cleric/oracle", "druid", "witch", "shaman", "psychic", "cleric", "oracle", "wizard"}
NPC = {"adept", "red mantiss assasin", "sahirafiyun"}          # classe de PNJ et classes de prestige : pas de référence
SIX = {"bard", "inquisitor", "magus", "alchemist", "summoner", "unchained summoner", "skald", "hunter", "investigator",
       "occultist", "mesmerist", "spiritualist", "warpriest", "red mantiss assasin", "sahirafiyun"}
FOUR = {"paladin", "ranger", "antipaladin", "bloodrager", "medium"}
SCH = {"abjuration": "Abjuration", "conjuration": "Conjuration", "divination": "Divination", "enchantment": "Enchantment",
       "evocation": "Evocation", "illusion": "Illusion", "necromancy": "Necromancy", "transmutation": "Transmutation"}
EXCLU = ("Technology Guide",)

def _cl(cls, L):
    if cls in FULL: return max(1, 2 * L - 1)
    if cls in SIX: return max(1, 3 * L - 2)
    if cls in FOUR: return max(1, 3 * L - 2)
    return max(1, 2 * L - 1)

def caster(access):
    """(niveau du sort, niveau du lanceur de référence, classe) : la classe qui lance le sort le plus tôt"""
    best = None
    for cls, L in access.get("Level", []):
        if cls in NPC: continue
        c = (_cl(cls, L), L, cls)
        if best is None or c < best: best = c
    if best is None:
        for ways in access.values():
            for _, L in ways:
                c = (max(1, 2 * L - 1), L, "autre")
                if best is None or c < best: best = c
    return (best[1], best[0], best[2]) if best else (None, None, None)

def _area(txt, rng_feet):
    s = (txt or "").lower()
    m = re.search(r"cylinder \((\d+)-ft\.? radius", s)
    if m: return {"type": "cylinder", "size": int(m.group(1))}
    m = re.search(r"(\d+)[- ](?:ft\.?|foot)[- ]radius", s)
    if m: return {"type": "sphere", "size": int(m.group(1))}
    m = re.search(r"(\d+)[- ](?:ft\.?|foot)[- ]cone", s) or (re.search(r"\bcone\b", s) and None)
    if m: return {"type": "cone", "size": int(m.group(1))}
    if re.search(r"cone-shaped", s) and rng_feet: return {"type": "cone", "size": rng_feet}
    m = re.search(r"(\d+)[- ](?:ft\.?|foot)[- ]line", s)
    if m: return {"type": "line", "size": int(m.group(1))}
    m = re.search(r"(\d+)[- ](?:ft\.?|foot)[- ]cube", s)
    if m: return {"type": "cube", "size": int(m.group(1))}
    return None

def _heal_pf(text, CL):
    m = re.search(r"cures? (\d+)d(\d+) points of damage ?\+ ?1 point per (?:caster )?level \(maximum \+ ?(\d+)\)", text.lower())
    if not m: return None
    return f"{m.group(1)}d{m.group(2)} + {min(CL, int(m.group(3)))}"

def load(path, prev=None):
    """prev : sorts déjà lus d'une autre édition (3.5), qui prêtent leur zone quand le relevé ne la donne pas"""
    out = {}
    for x in json.load(open(path, encoding="utf-8")):
        if any(b in x["Source"] for b in EXCLU): continue      # tous les sorts, légaux ou non en Pathfinder Society ; le tri se fait à la relecture
        sch = SCH.get(x["School"])
        if not sch: continue
        L, CL, cls = caster(x.get("access_ways", {}))
        if L is None: continue
        k = idx_of(x["Name"])
        rng = _range(x.get("Range", "").replace("ft.", "ft.").capitalize(), CL)
        rf = _feet(x.get("Range", "").capitalize(), CL)
        dur = _duration(x.get("Duration", "").capitalize(), CL)
        desc = x.get("Description", "")
        comp = x.get("Components", "")
        mat = ""
        m = re.search(r"(?:M|F)(?:/DF)? \(([^)]*\d[\d,]* gp[^)]*)\)", comp)
        if m: mat = m.group(1)
        area_src = " ".join(str(x.get(f, "")) for f in ("Effect", "Target")) + " " + desc[:400]
        rec = dict(index=k, name=x["Name"], level=L, school={"name": sch}, casting_time=_cast(x.get("Casting time")),
                   range=rng, duration=dur, concentration="concentration" in x.get("Duration", "").lower(),
                   ritual=False, material=mat or None, desc=[desc], _ed="pf1", _cl=CL, _cls=cls, _sub=x.get("Subschool"),
                   _descr=x.get("Descriptors"), _xp=None, _book=re.split(r" pg\.", x["Source"])[0], _short=x.get("Short description", ""),
                   _target=x.get("Target"), _effect=x.get("Effect"), _url=x.get("Url aon"),
                   _fields={"target": x.get("Target"), "effect": x.get("Effect"), "range": x.get("Range"), "duration": x.get("Duration"), "components": x.get("Components")})
        a = _area(area_src, rf)
        if a: rec["area_of_effect"] = a
        if "area_of_effect" not in rec and prev and k in prev and prev[k].get("area_of_effect"):
            rec["area_of_effect"] = prev[k]["area_of_effect"]
        h = _heal_pf(desc, CL)
        if h: rec["heal_at_slot_level"] = {str(L): h}
        else:
            dmg = _damage(desc, L, CL)
            if dmg: rec["damage"] = dmg
        out[k] = rec
    return out
