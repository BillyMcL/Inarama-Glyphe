"""La concentration écrite sur les glyphes (décisions du 23 novembre 2026).

Sorts concernés, lus dans la source de chaque jeu :
- D&D 5 (5e et 2024) : les sorts que la source marque « concentration » ;
- D&D 3.5 et Pathfinder 1 : les sorts dont la durée commence par « concentration » (seule ou suivie d'autre chose :
  « concentration, up to 1 min./level », « concentration + 1 round/level ») ;
- Pathfinder 2 (les deux éditions) : les sorts « maintenus » (« sustained » dans la durée de la source, seule ou suivie
  d'une limite : « sustained up to 1 minute ») : le maintenu s'écrit comme la concentration ;
- Elden Ring : aucun.
Toutes les formes du sort dans ce jeu changent (base, Arcane, hybrides, arts rares). Un sort dont la source est ambiguë (la
concentration ou le maintien dans un cas seulement, ou à un niveau ou un rang de lancement seulement) n'est pas changé : il
est listé (AMBIGUS).

Écriture (celle des formes combinées) : le mot CONCENTRATION dans le cercle de Condition (« parole · concentration »),
ajouté aux mots du cercle sans rien retirer ; sans cercle de Condition, un cercle de Condition est ajouté à sa place dans
l'ordre des cercles. La valeur du cercle compte ses conditions : elle est égale à son nombre de mots. Phrase : le début est
régénéré, sans parenthèse ajoutée (le mot suffit). Les formes qui portaient déjà CONCENTRATION dans leur Condition prennent
la même écriture (valeur = nombre de mots, parenthèse retirée : NORMALISEES ; les formes combinées le font dans
combinees.cercle). Une forme qui l'écrit ailleurs (Durée « tant que · concentration », satellite) n'est pas changée (DEJA).
Appliqué tout à la fin de la chaîne (après B13) ; les formes touchées sont redessinées par le moteur.
"""
import re, os, json
import spells as SP

FAITS, DEJA, AMBIGUS, NORMALISEES = [], [], set(), []
_STATUT = {}
NIVEAU_SEUL = re.compile(r"doesn't require concentration|without requiring your concentration", re.I)
RANG_SEUL = re.compile(r"no longer need to \{@action sustain|no longer need to sustain", re.I)
_PF2 = None


def _pf2_brut():
    """durée et intensification de chaque sort de Pathfinder 2 dans la source : {(index, remanié): (durée, intensifié)}"""
    global _PF2
    if _PF2 is None:
        import pf2
        p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "donnees", "pf2", "sorts-pf2.json")
        _PF2 = {}
        for x in json.load(open(p, encoding="utf-8")):
            _PF2.setdefault((pf2.idx_of(x["name"]), bool(x.get("remaster"))), (x.get("duration"), x.get("heightened")))
    return _PF2


def _code(f):
    d = f["dnd"]
    return ("er" if d.startswith("Elden Ring") else "pf2r" if d.startswith("Pathfinder 2 (version") else "pf2" if d.startswith("Pathfinder 2")
            else "pf1" if d.startswith("Pathfinder 1") else "3.5" if "D&amp;D 3.5" in d else "2024" if "2024" in d else "5e")


def _index(cle, code):
    from fiches import FICHES
    fi = FICHES.get(cle, {})
    if (fi.get("src") or "5e") == code: return fi.get("src_idx", cle)
    v = fi.get({"2024": "v24", "3.5": "v35", "pf1": "vpf", "pf2": "vp2", "pf2r": "vr"}.get(code, ""))
    return (v or {}).get("src_idx", cle)


def _source(cle, jeu):
    import convert as C
    code = {"5e": "5e", "2024": "2024", "3.5": "3.5", "PF1": "pf1"}.get(jeu, jeu)
    return {"5e": C.SRD, "2024": C.SRD24, "3.5": C.SRD35, "pf1": C.PF1, "pf2": C.PF2, "pf2r": C.PF2R}[code].get(_index(cle, code))


def statut(cle, code):
    """« oui », « ambigu » ou None : la concentration (ou le maintien) du sort dans ce jeu, lue dans la source"""
    k = (cle, code)
    if k in _STATUT: return _STATUT[k]
    s, r = None, _source(cle, code)
    if r is None: pass
    elif code in ("5e", "2024"):
        txt = " ".join(r.get("desc") or []) + " " + " ".join(r.get("higher_level") or [])
        if r.get("concentration"): s = "ambigu" if NIVEAU_SEUL.search(txt) else "oui"
    elif code in ("3.5", "pf1"):
        d = ((r.get("_fields") or {}).get("duration") or "").strip().lower()
        if "concentrat" in d:
            s = "oui" if d.startswith("concentration") and not re.search(r"\bor\b|/1 minute", d) else "ambigu"
    elif code in ("pf2", "pf2r") and not r.get("_rituel"):
        d, h = _pf2_brut().get((_index(cle, code), code == "pf2r"), (None, None))
        e = json.dumps(d or {}, ensure_ascii=False).lower()
        if (isinstance(d, dict) and d.get("sustained")) or "sustain" in e:
            s = "ambigu" if (re.search(r"\bor\b", e) or RANG_SEUL.search(json.dumps(h or {}, ensure_ascii=False))) else "oui"
    _STATUT[k] = s
    return s


def _ailleurs(f):
    """où la concentration est déjà écrite hors du cercle de Condition (None si nulle part)"""
    for r in f["rings"]:
        if r[0] == "CONDITION": continue
        if "CONCENTRATION" in r[2]: return r[0]
        for s in (r[4] if len(r) > 4 and r[4] else []):
            if len(s) > 2 and isinstance(s[2], str) and "CONCENTRATION" in s[2].split(): return f"satellite ({r[0]})"
    return None


def _decoupe(r):
    """(parenthèse, reste) de la phrase d'un cercle de Condition, d'après la tête que le moteur écrit pour ses mots"""
    import corrections as K, phase4b as P, constats as B13
    with K._Accentue(): t0 = P._tete_b9("CONDITION", r[1], list(r[2]))
    if r[3].startswith(t0):
        apres = r[3][len(t0):]
        par = K.parenthese("x" + apres) if apres.startswith(" (") else ""
        return par, apres[len(par):]
    _, par, reste = B13._decoupe(r[3])
    return par, reste


def _cercle(r, ajout_mot, garder_par):
    """le cercle de Condition écrit avec la concentration (r : le cercle existant, ou None)"""
    import convert as C, corrections as K, phase4b as P
    C.word("CONCENTRATION")
    if r is None: ws, par, reste, sats = ["CONCENTRATION"], "", "", None
    else:
        par, reste = _decoupe(r)
        ws = list(r[2])
        if ajout_mot:       # « sans » se lit avec tous les mots qui le suivent : la concentration se place avant lui
            k = ws.index("SANS") if "SANS" in ws else len(ws)
            ws = ws[:k] + ["CONCENTRATION"] + ws[k:]
        sats = r[4] if len(r) > 4 else None
    with K._Accentue():
        rd = P._tete_b9("CONDITION", len(ws), ws) + (par if garder_par else "") + reste
    return ("CONDITION", len(ws), ws, rd, sats) if sats is not None else ("CONDITION", len(ws), ws, rd)


def appliquer(cle, formes):
    import corrections as K, combinees as CB
    out = []
    for f in formes:
        if K.est_elden_ring(f) or f.get("combinee"): out.append(f); continue
        code = _code(f)
        jeu = {"5e": "5e", "2024": "2024", "3.5": "3.5", "pf1": "PF1", "pf2": "PF2", "pf2r": "PF2"}[code]
        rings = list(f["rings"])
        i = next((j for j, r in enumerate(rings) if r[0] == "CONDITION"), None)
        if i is not None and "CONCENTRATION" in rings[i][2]:          # déjà écrite dans la Condition : même écriture partout
            nv = _cercle(rings[i], False, False)
            if nv != rings[i]:
                rings[i] = nv; NORMALISEES.append((cle, jeu, f["label"]))
                f = CB._redessiner(f, rings)
            out.append(f); continue
        st = statut(cle, code)
        if st is None: out.append(f); continue
        if st == "ambigu":
            AMBIGUS.add((cle, jeu, f["fr"])); out.append(f); continue
        ou = _ailleurs(f)
        if ou:
            DEJA.append((cle, jeu, f["label"], ou)); out.append(f); continue
        if i is not None:
            rings[i] = _cercle(rings[i], True, True); quoi = "modifié"
        else:
            ordre = list(SP.NAMES)
            j = next((j for j, r in enumerate(rings) if ordre.index(r[0]) > ordre.index("CONDITION")), len(rings))
            rings.insert(j, _cercle(None, True, True)); quoi = "ajouté"
        FAITS.append((cle, jeu, f["label"], quoi))
        out.append(CB._redessiner(f, rings))
    return out
