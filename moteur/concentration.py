"""La concentration écrite sur les glyphes (décision du 23 novembre 2026).

Sorts concernés, lus dans la source de chaque jeu :
- D&D 5 (5e et 2024) : les sorts que la source marque « concentration » ;
- D&D 3.5 et Pathfinder 1 : les sorts dont la durée commence par « concentration » (seule ou suivie d'autre chose :
  « concentration, up to 1 min./level », « concentration + 1 round/level ») ;
- Pathfinder 2 : aucun (le sort « maintenu » est une autre contrainte) ; Elden Ring : aucun.
Toutes les formes du sort dans ce jeu changent (base, Arcane, hybrides). Un sort dont la source est ambiguë (la
concentration dans un cas seulement, ou à un niveau de lancement seulement) n'est pas changé : il est listé (AMBIGUS).

Écriture (celle des formes combinées) : le mot CONCENTRATION dans le cercle de Condition (« parole · concentration »),
ajouté aux mots du cercle sans rien retirer ni changer sa valeur ; sans cercle de Condition, un cercle de Condition est
ajouté à sa place dans l'ordre des cercles. Une forme qui écrit déjà la concentration (mot ou satellite) n'est pas
changée : elle est listée (DEJA). Phrase : le début est régénéré, la parenthèse est gardée et reçoit « concentration ».
Appliqué tout à la fin de la chaîne (après B13) ; les formes touchées sont redessinées par le moteur.
"""
import re, collections
import spells as SP

FAITS, DEJA, AMBIGUS, COMBINEES = [], [], set(), []      # (clé, jeu, libellé, « modifié » ou « ajouté ») ; (clé, jeu, libellé, où)
_STATUT = {}
NIVEAU_SEUL = re.compile(r"doesn't require concentration|without requiring your concentration", re.I)


def _source(cle, jeu):
    import convert as C
    from fiches import FICHES
    fi = FICHES.get(cle, {})
    base = {"5e": C.SRD, "2024": C.SRD24, "3.5": C.SRD35, "PF1": C.PF1}[jeu]
    src = fi.get("src")
    code = {"5e": None, "2024": "2024", "3.5": "3.5", "PF1": "pf1"}[jeu]
    if (src or None) == code: idx = fi.get("src_idx", cle)
    else:
        v = fi.get({"2024": "v24", "3.5": "v35", "PF1": "vpf"}.get(jeu, ""))
        idx = (v or {}).get("src_idx", cle) if (v is not None or jeu == "2024") else cle
    return base.get(idx)


def statut(cle, jeu):
    """« oui », « ambigu » ou None : la concentration du sort dans ce jeu, lue dans la source"""
    k = (cle, jeu)
    if k in _STATUT: return _STATUT[k]
    s, r = None, _source(cle, jeu) if jeu in ("5e", "2024", "3.5", "PF1") else None
    if r is not None and jeu in ("5e", "2024"):
        txt = " ".join(r.get("desc") or []) + " " + " ".join(r.get("higher_level") or [])
        if r.get("concentration"): s = "ambigu" if NIVEAU_SEUL.search(txt) else "oui"
    elif r is not None:
        d = ((r.get("_fields") or {}).get("duration") or "").strip().lower()
        if "concentrat" in d:
            s = "oui" if d.startswith("concentration") and not re.search(r"\bor\b|/1 minute", d) and " and " not in d.split("concentration")[0] else "ambigu"
    _STATUT[k] = s
    return s


def _deja(f):
    for r in f["rings"]:
        if "CONCENTRATION" in r[2]: return r[0]
        for s in (r[4] if len(r) > 4 and r[4] else []):
            if len(s) > 2 and isinstance(s[2], str) and "CONCENTRATION" in s[2].split(): return f"satellite ({r[0]})"
    return None


def _cercle(r, k):
    """le cercle de Condition avec la concentration (r : le cercle existant, ou None)"""
    import convert as C, corrections as K, phase4b as P, constats as B13
    if r is None:
        ws, v, par, reste = ["CONCENTRATION"], 1, "", ""
    else:
        ws, v = list(r[2]) + ["CONCENTRATION"], r[1]
        with K._Accentue(): t0 = P._tete_b9("CONDITION", v, list(r[2]))       # la tête d'une Condition contient elle-même des « ; »
        rd0 = r[3]
        if rd0.startswith(t0):
            apres = rd0[len(t0):]
            par = K.parenthese("x" + apres) if apres.startswith(" (") else ""
            reste = apres[len(par):]
        else:
            _, par, reste = B13._decoupe(rd0)
    C.word("CONCENTRATION")
    par = f" ({par[2:-1]} ; concentration)" if par else " (concentration)"
    with K._Accentue():
        rd = P._tete_b9("CONDITION", v, ws) + par + reste
    return ("CONDITION", v, ws, rd, *r[4:]) if r is not None else ("CONDITION", v, ws, rd)


def appliquer(cle, formes):
    import corrections as K, combinees as CB, constats as B13
    out = []
    for f in formes:
        if K.est_elden_ring(f): out.append(f); continue
        jeu = B13.jeu(f)
        st = statut(cle, jeu) if jeu in ("5e", "2024", "3.5", "PF1") else None
        if st is None: out.append(f); continue
        if st == "ambigu":
            AMBIGUS.add((cle, jeu, f["fr"])); out.append(f); continue
        ou = _deja(f)
        if ou:
            DEJA.append((cle, jeu, f["label"], ou)); out.append(f); continue
        if f.get("combinee"):
            COMBINEES.append((cle, jeu, f["label"])); out.append(f); continue
        rings, quoi = list(f["rings"]), None
        i = next((j for j, r in enumerate(rings) if r[0] == "CONDITION"), None)
        if i is not None:
            rings[i] = _cercle(rings[i], (cle, None)); quoi = "modifié"
        else:
            ordre = list(SP.NAMES)
            j = next((j for j, r in enumerate(rings) if ordre.index(r[0]) > ordre.index("CONDITION")), len(rings))
            rings.insert(j, _cercle(None, (cle, None))); quoi = "ajouté"
        FAITS.append((cle, jeu, f["label"], quoi))
        out.append(CB._redessiner(f, rings))
    return out
