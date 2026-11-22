"""B13 : les constats notés en route (relectures de sorts, Eau consacrée, bonus en chiffre brut, écriture de la garde).

Données : donnees/phase4b/B13_constats.csv, écrit forme par forme d'après l'état de main (62c3812) : chaque ligne vise une
forme précise (clé, jeu, libellé), Arcane et hybrides compris ; rien n'est appliqué en dehors des formes listées.
Appliqué tout à la fin de la chaîne (après fautes.py et les formes combinées) ; les formes touchées sont redessinées par le
moteur (placement des symboles, répartition, dessin, nombres, fautes), comme les formes de B12.

Règles validées (22 novembre 2026) :
- un bonus à un jet s'écrit en degré : la moitié du bonus arrondie au-dessus ; une caractéristique : 2 points = 1 de
  bonus ; au-delà de +19 : plein. Un montant (dégâts, points de vie, dureté) reste un montant ;
- la garde : PROTECTION = un bonus à la défense, en degré ; REMPART = un montant retranché à chaque coup ; RESISTANCE = la
  moitié arrêtée, degré 5 ; IMMUNITE = plus rien ne passe, plein ; BARRIERE = ce qui arrête tout (mur, zone), plein. La vie
  d'emprunt garde l'écriture existante (mot VIE et satellite de Durée plein « d'emprunt », comme Simulacre de vie) ;
- une caractéristique du lanceur ne s'écrit pas ; quand tout l'effet en dépend, on la prend à 3.

Phrases : le début est régénéré ; la parenthèse est celle de la colonne « parenthese », ou l'actuelle si elle est vide ; la
lecture des satellites est gardée telle quelle quand ils ne changent pas, sinon réécrite (les fins « … est dit par la
Cible », « … est dite par le noyau » sont gardées).
Une ligne qui ne s'accorde pas avec la forme arrête la construction (ValueError) : rien n'est contourné.

Décisions ajoutées après B13 (22 novembre 2026) : les deux formes « version PF2 remaniée » d'Orbe aqueux sont retirées
(identiques à la version PF2) ; sur toute la bibliothèque hors Elden Ring, un Impact 2 dont la phrase dit un bonus de 2
(« +2 », « 2 ajouté ») passe au degré 1 (les +2 écrits 2 avaient échappé au relevé des bonus bruts).
"""
import os, csv, re, collections
import spells as SP

D = os.path.dirname(os.path.abspath(__file__))
FICHIER = os.path.join(D, "..", "donnees", "phase4b", "B13_constats.csv")
LIGNES = collections.defaultdict(list)
for _l in (csv.DictReader(open(FICHIER, encoding="utf-8-sig"), delimiter=";") if os.path.exists(FICHIER) else []):
    LIGNES[(_l["cle"], _l["forme"])].append(_l)
CLES = {k[0] for k in LIGNES}
FAITS, RETRAITS = [], []        # (clé, libellé) des formes changées ; (clé, place dans la liste, forme) des formes retirées
VU = set()
JEU = {"5.1": "5e", "5.2": "2024", "3.5": "3.5", "pf1": "PF1", "pf2": "PF2", "pf2r": "PF2", "er": "Elden Ring"}
AJOUTS = ("ajouter après", "ajouter avant")
# Décision de l'utilisateur (22 novembre 2026), après B13 : les deux formes « version PF2 remaniée » d'Orbe aqueux deviennent
# identiques à la version PF2 (le cube venait d'une mauvaise lecture de « une case de 3 m ») ; comme toujours quand deux
# versions donnent le même glyphe, on n'en garde qu'une : elles sont retirées, leurs lignes de B13 sont sans objet.
RETIREES_DECISION = {("aqueous-orb", "Forme arcane — version PF2 remaniée"), ("aqueous-orb", "Forme hybride — version PF2 remaniée")}


def jeu(f):
    d = f["dnd"]
    s = ("er" if d.startswith("Elden Ring") else "pf2r" if d.startswith("Pathfinder 2 (version") else "pf2" if d.startswith("Pathfinder 2")
         else "pf1" if d.startswith("Pathfinder 1") else "3.5" if "D&amp;D 3.5" in d else "5.2" if "2024" in d else "5.1")
    return JEU[s]


def _vs(v): return "plein" if v == "plein" else str(v)
def decrit(r): return " ".join([r[0]] + ([_vs(r[1])] if r[1] is not None else []) + list(r[2]))
def _valeur(txt, garde):
    return garde if txt == "garder" else "plein" if txt == "plein" else int(txt)


def _mots(txt, garde):
    import convert as C, lint as LI
    if txt.strip() == "garder": return list(garde)
    ws = txt.split()
    hors = [w for w in ws if LI.MILLE_ET_UN is not None and w not in LI.MILLE_ET_UN]
    if hors: raise ValueError(f"B13 : hors lexique : {hors}")
    return [C.word(w) for w in ws]


def _sat(txt):
    """« sym:feu » : symbole d'énergie ; « valeur|TEXTE » : satellite du moteur (critère = premier mot du texte)"""
    import convert as C, lint as LI
    txt = txt.strip()
    if txt.startswith("sym:"): return ("SYM", ("sym", txt[4:].strip()), "")
    v, t = txt.split("|", 1)
    v = v.strip(); t = t.strip()
    hors = [w for w in t.split()[1:] if LI.MILLE_ET_UN is not None and w not in LI.MILLE_ET_UN]
    if hors: raise ValueError(f"B13 : hors lexique (satellite) : {hors}")
    for w in t.split()[1:]: C.word(w)
    return ("SYM", "plein" if v == "plein" else int(v) if v else None, t, {"crit": t.split()[0]})


def _meme_sat(s, x):
    if isinstance(x[1], tuple): return s[1] == x[1]
    return len(s) > 2 and s[2] == x[2] and s[1] == x[1]


def _forme_nom(v, sats):
    import convert as C
    n = len(sats or [])
    for sil, ss, nom, _ in C.FORMES.values():
        if sil == v and len(ss) == n: return nom
    raise ValueError(f"B13 : primitive de Forme inconnue ({v})")


def _tete(crit, v, ws, ancienne):
    """le début de phrase régénéré ; un Impact sans mot écrit « intensité N » seul quand c'était déjà son écriture"""
    import convert as C, phase4b as P
    if crit == "IMPACT" and not ws and re.fullmatch(r"intensité \d+|plein", ancienne or ""):
        return "plein" if v == "plein" else f"intensité {v}"
    if crit == "AMPLEUR":
        if ws[-3:] == ["VOLUME", "METRES", "CUBES"]: return f"{v} m³"
        raise ValueError(f"B13 : Ampleur non prévue : {ws}")
    if crit == "FORME": raise ValueError("B13 : tête de Forme")
    return P._tete_b9(crit, v, ws)


def _decoupe(rd):
    """(tête, parenthèse, reste) d'une phrase de lecture"""
    import corrections as K
    par = K.parenthese(rd)
    if par:
        i = rd.index(par); return rd[:i], par, rd[i + len(par):]
    j = rd.find(" ; ")
    return (rd, "", "") if j < 0 else (rd[:j], "", rd[j:])


def _lecture(crit, v, ws, sats, ancienne, parenthese, sats_changent, k):
    import corrections as K
    tete0, par0, reste0 = _decoupe(ancienne) if ancienne else ("", "", "")
    par = f" ({parenthese})" if parenthese else par0
    if crit == "AMPLEUR" and parenthese:            # la parenthèse dit la taille : l'ancienne « taille d'origine » s'en va
        reste0 = re.sub(r" ; taille d'origine : [^;]*", "", reste0)
    with K._Accentue():
        tete = _tete(crit, v, ws, tete0)
        if not sats_changent: return tete + par + reste0
        fins = "".join(" ; " + s for s in reste0.split(" ; ") if s and not s.startswith("satellite"))
        rm = ["VIE"] + [w for w in ws if w != "VIE"] if "VIE" in ws else ws     # vie d'emprunt : l'explication de Simulacre de vie
        return tete + par + K._lecture_sats(sats, k, rm) + fins


def _modifie(r, l, k):
    import convert as C
    crit = r[0]
    v = _valeur(l["valeur"], r[1]); ws = _mots(l["mots"], r[2])
    sats = list(r[4]) if len(r) > 4 and r[4] else []
    ret = [_sat(x) for x in l["satellites_a_retirer"].split(";") if x.strip()]
    aj = [_sat(x) for x in l["satellites_a_ajouter"].split(";") if x.strip()]
    for x in ret:
        i = next((j for j, s in enumerate(sats) if _meme_sat(s, x)), None)
        if i is None: raise ValueError(f"B13 : satellite à retirer absent ({k[0]}, {x})")
        sats.pop(i)
    sats += aj
    change = bool(ret or aj)
    if change and sats: sats = C._resats(sats)
    if crit == "FORME":                 # Orbe aqueux PF2 remaniée : la primitive change (sphère et non cube), satellites gardés
        rd = _forme_nom(v, sats) + ("" if not ws else " « " + " · ".join(C.shown(w) for w in ws) + " »")
    else:
        rd = _lecture(crit, v, ws, sats, r[3], l["parenthese"].strip(), change, k)
    return (crit, v, ws, rd, sats) if sats or len(r) > 4 else (crit, v, ws, rd)     # même forme de cercle qu'avant (clé de glyphe)


def _ajoute(r, l, k):
    import convert as C
    if l["cercle"] == "FORME":          # « ajouter juste après le cercle Forme un cercle AMPLEUR … ; parenthèse : … »
        m = re.match(r"ajouter juste après le cercle Forme un cercle AMPLEUR (\d+) ([A-Z ]+?)\s*(?:\(|;)", l["note"])
        p = re.search(r"parenthèse : (.+)$", l["note"])
        if not m or not p: raise ValueError(f"B13 : Ampleur illisible ({l['note']})")
        v, ws = int(m.group(1)), _mots(m.group(2), [])
        return ("AMPLEUR", v, ws, _lecture("AMPLEUR", v, ws, [], "", p.group(1).strip(), False, k))
    crit = l["cercle"]
    v = _valeur(l["valeur"], None); ws = _mots(l["mots"], [])
    if l["satellites_a_retirer"].strip(): raise ValueError("B13 : satellite à retirer sur un cercle ajouté")
    sats = [_sat(x) for x in l["satellites_a_ajouter"].split(";") if x.strip()]
    sats = C._resats(sats) if sats else []
    rd = _lecture(crit, v, ws, sats, "", l["parenthese"].strip(), True, k)
    return (crit, v, ws, rd, sats) if sats else (crit, v, ws, rd)


def _sans_taille(r):
    """la Forme qui reçoit son Ampleur ne dit plus « taille non donnée par la source » (comme une forme du moteur avec sa taille)"""
    rd = r[3].replace(" (taille non donnée par la source)", "")
    return (*r[:3], rd, *r[4:])


def cercles(g, rows, k):
    par = collections.defaultdict(list)
    for l in rows: par[(l["cercle"], int(l["numero"]))].append(l)
    pris = set()
    ps = list(g.get("poles_impacts") or [])
    out, nps, cpt, ii = [], [], collections.Counter(), 0
    for r in g["rings"]:
        n = cpt[r[0]]; cpt[r[0]] += 1
        ls = par.get((r[0], n), [])
        pris.add((r[0], n))
        pole = ps[ii] if r[0] == "IMPACT" and ii < len(ps) else None      # un Impact ajouté prend le pôle de son voisin
        av = [l for l in ls if l["action"] == "ajouter avant"]
        ap = [l for l in ls if l["action"] == "ajouter après"]
        mod = [l for l in ls if l["action"] == "modifier"]
        if len(mod) > 1: raise ValueError(f"B13 : deux modifications du même cercle ({k[0]}, {g['label']})")
        for l in av:
            out.append(_ajoute(r, l, k))
            if out[-1][0] == "IMPACT": nps.append(pole)
        rr = _modifie(r, mod[0], k) if mod else r
        if r[0] == "FORME" and any(l["cercle"] == "FORME" for l in ap): rr = _sans_taille(rr)
        out.append(rr)
        if r[0] == "IMPACT": nps.append(pole); ii += 1
        for l in ap:
            out.append(_ajoute(r, l, k))
            if out[-1][0] == "IMPACT": nps.append(pole)
    manque = set(par) - pris
    if manque: raise ValueError(f"B13 : cercles introuvables {manque} ({k[0]}, {g['label']})")
    return out, (tuple(nps) if ps else g.get("poles_impacts"))


def _verbe(g, l):
    import convert as C
    if g["verb"] != l["cercle_actuel"] or g["fam"] != "A": raise ValueError(f"B13 : verbe actuel « {g['verb']} »")
    cible = l["note"].replace("verbe ", "", 1).strip()
    nom = cible.split(" · ")[0]
    vk, vn = next(key for key, n in C.VERBS.items() if n == nom and f"{n} · {C.VERB_GROUP[key[0]].lower()} {'−' if key[1] else '+'}" == cible)
    return dict(g, core=SP.verb(vk, vn), pol="down" if vn else "up", verb=cible)


def forme(f, ls, cle):
    import combinees as CB
    k = (cle, None)
    g = f
    vb = [l for l in ls if l["action"] == "changer le verbe"]
    if vb: g = _verbe(g, vb[0])
    rows = [l for l in ls if l["action"] == "modifier" or l["action"] in AJOUTS]
    autres = [l for l in ls if l not in vb and l not in rows]
    if autres: raise ValueError(f"B13 : action inconnue {[l['action'] for l in autres]}")
    rings, ps = cercles(g, rows, k) if rows else (g["rings"], g.get("poles_impacts"))
    g = dict(g, poles_impacts=ps)
    FAITS.append((cle, f["label"]))
    return CB._redessiner(g, rings)


# Les « +2 » écrits 2 (décision de l'utilisateur, 22 novembre 2026, après B13) : sur toute la bibliothèque hors Elden Ring,
# un cercle d'Impact de valeur 2 dont la phrase dit un bonus de 2 (« +2 » ou « 2 ajouté ») passe au degré 1, comme les
# autres bonus bruts du lot D. Relevé sur main : 35 cercles. Seul le début de la phrase change (la parenthèse reste).
PLUS2 = []          # (clé, libellé, ancienne phrase, nouvelle phrase)
_BONUS2 = re.compile(r"(?<![\d,])\+2(?![\d,])|(?<![\d,])2 ajouté")


def plus2(f, cle):
    import corrections as K, combinees as CB
    if K.est_elden_ring(f): return f
    rings, faits = [], []
    for r in f["rings"]:
        if r[0] == "IMPACT" and r[1] == 2 and _BONUS2.search(r[3]):
            sats = list(r[4]) if len(r) > 4 and r[4] else []
            rd = _lecture("IMPACT", 1, list(r[2]), sats, r[3], "", False, (cle, None))
            faits.append((cle, f["label"], r[3], rd))
            r = (r[0], 1, r[2], rd, *r[4:])
        rings.append(r)
    if not faits: return f
    PLUS2.extend(faits)
    return CB._redessiner(f, rings)


def appliquer(cle, formes):
    return [plus2(f, cle) for f in _b13(cle, formes)]


def _b13(cle, formes):
    if cle not in CLES: return formes
    out, vus = [], set()
    for i, f in enumerate(formes):
        ls = LIGNES.get((cle, f["label"]))
        if not ls: out.append(f); continue
        if f["label"] in vus: raise ValueError(f"B13 : deux formes « {f['label']} » ({cle})")
        vus.add(f["label"]); VU.add((cle, f["label"]))
        if any(l["jeu"] != jeu(f) for l in ls): raise ValueError(f"B13 : jeu {jeu(f)} ({cle}, {f['label']})")
        if any(l["action"] == "retirer la forme" for l in ls) or (cle, f["label"]) in RETIREES_DECISION:
            RETRAITS.append((cle, i, f)); continue
        out.append(forme(f, ls, cle))
    return out


def manquantes():
    """les formes de B13 que la construction n'a pas rencontrées"""
    return sorted(set(LIGNES) - VU)
