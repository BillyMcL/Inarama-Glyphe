"""Chantier d'écriture (24 novembre 2026) : les correctifs d'écriture des glyphes, en cinq lots, validés par l'utilisateur.

  lot 1  les cercles « plein » de cause A (un même cercle pour des sorts sans rapport) ;
  lot 2  les zones sans Forme ni taille ;
  lot 3  le jet renouvelé (« fin : chaque · instants · sursaut ») ;
  lot 4  les mécaniques des bonus ;
  lot 5  les petits correctifs de la liste de fin (jumelles, puissance fractionnée, Conditions…).

Données : donnees/phase4b/B14_ecriture_lot*.csv, une ligne par cercle touché, forme par forme (clé, jeu, libellé), Arcane et
hybrides compris, au format de B13 (donnees/phase4b/B13_constats.csv) ; une action de plus : « retirer » (le cercle s'en va).
Appliqué tout à la fin de la chaîne (après la concentration). Les formes touchées sont redessinées par le moteur, comme celles
de B13. Une ligne qui ne s'accorde pas avec la forme arrête la construction (ValueError) : rien n'est contourné.
"""
import os, re, csv, glob, collections
import constats as B13

D = os.path.dirname(os.path.abspath(__file__))
FICHIERS = sorted(glob.glob(os.path.join(D, "..", "donnees", "phase4b", "B14_ecriture_lot*.csv")))
if os.environ.get("ECRITURE_CSV") is not None:          # essais : une autre liste de fichiers (séparés par « ; »)
    FICHIERS = [p for p in os.environ["ECRITURE_CSV"].split(";") if p.strip()]
LIGNES = collections.defaultdict(list)
for _p in FICHIERS:
    for _l in csv.DictReader(open(_p, encoding="utf-8-sig"), delimiter=";"):
        if not (_l.get("cle") or "").strip(): continue
        _l = {k: (v or "") for k, v in _l.items()}
        LIGNES[(_l["cle"], _l["forme"])].append(_l)
CLES = {k[0] for k in LIGNES}
FAITS, RETRAITS, VU = [], [], set()
ACTIONS = ("modifier", "ajouter avant", "ajouter après", "retirer")


UNITES = {("VOLUME", "METRES", "CUBES"): "m³", ("VOLUME", "DECAMETRES", "CUBES"): "dam³", ("VOLUME", "HECTOMETRES", "CUBES"): "hm³",
          ("VOLUME", "KILOMETRES", "CUBES"): "km³", ("LONGUEUR", "METRES"): "m de long", ("LONGUEUR", "KILOMETRES"): "km de long",
          ("SURFACE", "METRES"): "m²", ("DIAMETRE", "METRES"): "m de diamètre"}


def _sat2(txt):
    """comme constats._sat ; en plus « p:2 » : un satellite de proportion d'une Forme (sans texte)"""
    txt = txt.strip()
    if txt.startswith("p:") or txt.startswith("q:"):          # proportion d'une Forme ; Quantité d'une Cible (écriture du moteur)
        v = txt[2:].strip(); return ("SYM", "plein" if v == "plein" else int(v))
    return B13._sat(txt)


def _ajoute2(l, k):
    """un cercle ajouté d'un autre critère que le cercle visé (colonne « cercle_ajoute ») : FORME, AMPLEUR ou un autre"""
    import convert as C
    crit = l["cercle_ajoute"].strip()
    v = B13._valeur(l["valeur"], None); ws = B13._mots(l["mots"], [])
    if l["satellites_a_retirer"].strip(): raise ValueError("écriture : satellite à retirer sur un cercle ajouté")
    sats = [_sat2(x) for x in l["satellites_a_ajouter"].split(";") if x.strip()]
    if crit == "FORME":
        sats = C._resats(sats) if sats else []
        rd = B13._forme_nom(v, sats) + ("" if not ws else " « " + " · ".join(C.shown(w) for w in ws) + " »")
        if l["parenthese"].strip(): rd += f" ({l['parenthese'].strip()})"
        return ("FORME", v, ws, rd, sats)
    if crit == "AMPLEUR":
        u = UNITES.get(tuple(ws))
        if u is None: raise ValueError(f"écriture : unité d'Ampleur non prévue {ws}")
        rd = f"{v} {u}" + (f" ; {l['parenthese'].strip()}" if l["parenthese"].strip() else "")
        if sats: raise ValueError("écriture : satellite sur une Ampleur ajoutée")
        return ("AMPLEUR", v, ws, rd)
    sats = C._resats(sats) if sats else []
    rd = B13._lecture(crit, v, ws, sats, "", l["parenthese"].strip(), True, k)
    return (crit, v, ws, rd, sats) if sats else (crit, v, ws, rd)


def _lu(r, l):
    """la colonne « lecture », si elle est remplie, donne la phrase entière du cercle (lectures que le moteur ne sait pas refaire :
    objet annoté, Quantité pleine, disque, plan, calotte…)"""
    t = (l.get("lecture") or "").strip()
    return r if not t else (*r[:3], t, *r[4:])


def _forme_lue(l):
    """une Forme dont la phrase est donnée : la primitive n'a pas à être une des cinq du moteur"""
    import convert as C
    v = B13._valeur(l["valeur"], None); ws = B13._mots(l["mots"], [])
    sats = [_sat2(x) for x in l["satellites_a_ajouter"].split(";") if x.strip()]
    sats = C._resats(sats) if sats else []
    return ("FORME", v, ws, l["lecture"].strip(), sats)


def _modifie(r, l, k):
    """comme constats._modifie, avec les satellites « p: » et « q: »"""
    if any(x.strip().startswith(("p:", "q:")) for x in (l["satellites_a_ajouter"] + ";" + l["satellites_a_retirer"]).split(";")):
        import convert as C
        crit = r[0]
        v = B13._valeur(l["valeur"], r[1]); ws = B13._mots(l["mots"], r[2])
        sats = list(r[4]) if len(r) > 4 and r[4] else []
        for x in [x for x in l["satellites_a_retirer"].split(";") if x.strip()]:
            y = _sat2(x)
            i = next((j for j, s_ in enumerate(sats) if (len(y) == 2 and len(s_) >= 2 and s_[1] == y[1] and not (len(s_) > 2 and s_[2])) or (len(y) > 2 and B13._meme_sat(s_, y))), None)
            if i is None: raise ValueError(f"écriture : satellite à retirer absent ({k[0]}, {x})")
            sats.pop(i)
        sats += [_sat2(x) for x in l["satellites_a_ajouter"].split(";") if x.strip()]
        sats = C._resats(sats) if sats else []
        if not (l.get("lecture") or "").strip(): raise ValueError(f"écriture : satellite « p: »/« q: » sans phrase donnée ({k[0]})")
        return (crit, v, ws, l["lecture"].strip(), sats)
    return B13._modifie(r, l, k)


def _ajout(r, l, k):
    if l.get("cercle_ajoute", "").strip() == "FORME" and (l.get("lecture") or "").strip(): return _forme_lue(l)
    if l.get("cercle_ajoute", "").strip(): return _lu(_ajoute2(l, k), l)
    return _lu(B13._ajoute(r, l, k), l)


def _cercles(g, rows, k):
    """comme constats.cercles, avec l'action « retirer »"""
    par = collections.defaultdict(list)
    for l in rows: par[(l["cercle"], int(l["numero"]))].append(l)
    pris = set()
    ps = list(g.get("poles_impacts") or [])
    out, nps, cpt, ii = [], [], collections.Counter(), 0
    for r in g["rings"]:
        n = cpt[r[0]]; cpt[r[0]] += 1
        ls = par.get((r[0], n), [])
        pris.add((r[0], n))
        pole = ps[ii] if r[0] == "IMPACT" and ii < len(ps) else None
        av = [l for l in ls if l["action"] == "ajouter avant"]
        ap = [l for l in ls if l["action"] == "ajouter après"]
        mod = [l for l in ls if l["action"] == "modifier"]
        ret = [l for l in ls if l["action"] == "retirer"]
        if len(mod) + len(ret) > 1: raise ValueError(f"écriture : deux changements du même cercle ({k[0]}, {g['label']}, {r[0]} {n})")
        if ls and ls[0]["cercle_actuel"].strip() and B13.decrit(r) != ls[0]["cercle_actuel"].strip():
            raise ValueError(f"écriture : cercle actuel « {B13.decrit(r)} » ≠ « {ls[0]['cercle_actuel']} » ({k[0]}, {g['label']})")
        for l in av:
            out.append(_ajout(r, l, k))
            if out[-1][0] == "IMPACT": nps.append(pole)
        if ret:
            if r[0] == "IMPACT": ii += 1
        else:
            rr = _lu(_modifie(r, mod[0], k), mod[0]) if mod else r
            if r[0] == "FORME" and any(l["cercle"] == "FORME" for l in ap): rr = B13._sans_taille(rr)
            out.append(rr)
            if r[0] == "IMPACT": nps.append(pole); ii += 1
        for l in ap:
            out.append(_ajout(r, l, k))
            if out[-1][0] == "IMPACT": nps.append(pole)
    manque = set(par) - pris
    if manque: raise ValueError(f"écriture : cercles introuvables {manque} ({k[0]}, {g['label']})")
    return out, (tuple(nps) if ps else g.get("poles_impacts"))


_DIT = re.compile(r" ; ce que l'effet touche \(« ([^»]*) »\) est dit par la Cible")
def _sans_accent(w):
    import unicodedata
    return "".join(c for c in unicodedata.normalize("NFD", w.lower()) if unicodedata.category(c) != "Mn")


def _dit_par_la_cible(rings):
    """la fin « ce que l'effet touche (« … ») est dit par la Cible » ne garde que les mots que la Cible dit encore ; sans eux, elle
    s'en va (une Cible changée par le chantier ne doit pas laisser une phrase fausse)"""
    cible = next((r for r in rings if r[0] == "CIBLE"), None)
    mots = {_sans_accent(w) for w in (cible[2] if cible else [])}
    out = []
    for r in rings:
        m = _DIT.search(r[3]) if r[0] == "IMPACT" else None
        if m:
            noms = [n for n in m.group(1).split(" · ") if _sans_accent(n) in mots]
            rd = r[3][:m.start()] + (f" ; ce que l'effet touche (« {' · '.join(noms)} ») est dit par la Cible" if noms else "") + r[3][m.end():]
            if rd != r[3]: r = (r[0], r[1], r[2], rd, *r[4:])
        out.append(r)
    return out


def forme(f, ls, cle):
    import combinees as CB
    k = (cle, None)
    g = f
    vb = [l for l in ls if l["action"] == "changer le verbe"]
    if vb: g = B13._verbe(g, vb[0])
    rows = [l for l in ls if l["action"] in ACTIONS]
    autres = [l for l in ls if l not in vb and l not in rows]
    if autres: raise ValueError(f"écriture : action inconnue {[l['action'] for l in autres]}")
    rings, ps = _cercles(g, rows, k) if rows else (g["rings"], g.get("poles_impacts"))
    rings = _dit_par_la_cible(rings)
    g = dict(g, poles_impacts=ps)
    FAITS.append((cle, f["label"], sorted({l["lot"] for l in ls})))
    return CB._redessiner(g, rings)


def appliquer(cle, formes):
    if cle not in CLES: return formes
    out, vus = [], set()
    for i, f in enumerate(formes):
        ls = LIGNES.get((cle, f["label"]))
        if not ls: out.append(f); continue
        if f["label"] in vus: raise ValueError(f"écriture : deux formes « {f['label']} » ({cle})")
        vus.add(f["label"]); VU.add((cle, f["label"]))
        if any(l["jeu"] != B13.jeu(f) for l in ls): raise ValueError(f"écriture : jeu {B13.jeu(f)} ({cle}, {f['label']})")
        if any(l["action"] == "retirer la forme" for l in ls):
            RETRAITS.append((cle, i, f)); continue
        out.append(forme(f, ls, cle))
    return out


def manquantes():
    """les formes du chantier que la construction n'a pas rencontrées"""
    return sorted(set(LIGNES) - VU)
