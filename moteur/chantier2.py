"""Chantier d'écriture 2 (27 novembre 2026) : réécriture des glyphes en dix lots (A à J), d'après l'inventaire du chantier
d'écriture (Claude outputs, 00_en_cours/inventaire_chantier_ecriture.md) et les règles validées par l'utilisateur.

Données : donnees/phase4b/B15_chantier2_lot<X>.csv, un fichier par lot, une ligne par cercle changé, forme par forme
(clé, jeu, libellé). Les lots s'appliquent l'un après l'autre, dans l'ordre des lettres, tout à la fin de la chaîne (après le
chantier du 24 novembre, moteur/ecriture.py) : les lignes d'un lot visent l'état laissé par les lots précédents.

Une ligne donne le cercle ENTIER après correction (critère, valeur, mots, satellites, phrase de lecture) : le moteur ne
devine rien. Colonnes :
  action         modifier | ajouter avant | ajouter après | retirer
  cercle, numero le cercle visé (ou le cercle à côté duquel on ajoute) : critère et rang parmi les cercles de ce critère (0…)
  cercle_actuel  ce cercle tel qu'il est (« DUREE 1 MINUTES ») : s'il ne correspond pas, la construction s'arrête
  cercle_nouveau le critère du cercle ajouté (vide : celui de la colonne « cercle »)
  valeur         « plein », un nombre, ou « vide » (cercle sans valeur)
  mots           les mots du cercle, séparés par des espaces (lexique fermé : donnees/lexique_1001.json)
  satellites     liste JSON de satellites [position, valeur, texte, options] ; une position « auto » : la règle de
                 symétrie du moteur (_resats) place tous les satellites du cercle ; « garder » : ceux du cercle actuel
  lecture        la phrase entière du cercle ; « garder » : la phrase actuelle
  raison, inventaire  pourquoi (règle, source) et le numéro de l'inventaire
Deuxième passe (28 novembre 2026) : deux actions de plus sur la forme entière (colonne « nouvelle_forme ») :
  créer la forme     une forme de plus, copiée de la forme visée (une forme par choix au lancement) ; ses cercles
                     se changent par des lignes qui visent son nouveau libellé, dans le même lot, après la ligne de création
  renommer la forme  le libellé de la forme change
et les formes combinées (B12) : leurs lignes visent les cercles COMMUNS (numéro parmi les cercles communs de ce critère) ;
la forme est redessinée par le dessin des formes combinées (combinees.py).
Une ligne qui ne s'accorde pas avec la forme arrête la construction (ValueError) : rien n'est contourné. Elden Ring n'est
jamais touché. Les formes touchées sont redessinées par le moteur (placement des symboles, répartition, dessin, nombres,
fautes), comme celles du chantier du 24 novembre.
"""
import os, csv, glob, json, re, collections

D = os.path.dirname(os.path.abspath(__file__))
FICHIERS = sorted(glob.glob(os.path.join(D, "..", "donnees", "phase4b", "B15_chantier2_lot*.csv")))
if os.environ.get("CHANTIER2_CSV") is not None:          # essais : une autre liste de fichiers (séparés par « ; »)
    FICHIERS = [p for p in os.environ["CHANTIER2_CSV"].split(";") if p.strip()]
LOTS = []            # [(lot, {(clé, forme): [lignes]})] dans l'ordre des fichiers
for _p in FICHIERS:
    _L = collections.defaultdict(list)
    for _l in csv.DictReader(open(_p, encoding="utf-8-sig"), delimiter=";"):
        if not (_l.get("cle") or "").strip(): continue
        _l = {k: (v or "") for k, v in _l.items()}
        _L[(_l["cle"], _l["forme"])].append(_l)
    LOTS.append((os.path.basename(_p), _L))
CLES = {k[0] for _, L in LOTS for k in L}
FAITS, VU = [], set()
ACTIONS = ("modifier", "ajouter avant", "ajouter après", "retirer")
FORMES_ACTIONS = ("créer la forme", "renommer la forme", "noter")      # « noter » : la colonne « lecture » s'ajoute aux notes de la forme
CREEES = []          # (lot, clé, forme modèle, forme créée)


def _valeur(t):
    t = t.strip()
    if t == "vide": return None
    if t == "plein": return "plein"
    return int(t)


def _mots(t):
    import convert as C, lint as LI
    ws = t.split()
    hors = [w for w in ws if LI.MILLE_ET_UN is not None and w not in LI.MILLE_ET_UN]
    if hors: raise ValueError(f"chantier 2 : hors lexique : {hors}")
    return [C.word(w) for w in ws]


def _sats(t, r):
    import convert as C, lint as LI
    t = t.strip()
    if t == "garder": return list(r[4]) if r is not None and len(r) > 4 and r[4] else []
    if not t: return []
    out, auto = [], False
    for s in json.loads(t):
        pos, v = s[0], s[1]
        if isinstance(v, list) and len(v) == 2 and v[0] == "sym": v = ("sym", v[1])
        if pos == "auto": auto = True
        x = [pos, v]
        if len(s) > 2:
            for w in str(s[2]).split()[1:] if str(s[2]).split()[:1] and str(s[2]).split()[0] in LI.CRITERES else str(s[2]).split():
                if LI.MILLE_ET_UN is not None and w not in LI.MILLE_ET_UN: raise ValueError(f"chantier 2 : hors lexique (satellite) : {w}")
                C.word(w)
            x.append(s[2])
        if len(s) > 3: x.append(s[3])
        out.append(tuple(x))
    if auto: out = C._resats(out)
    return out


def _cercle(l, r, crit):
    v = _valeur(l["valeur"]); ws = _mots(l["mots"]); ss = _sats(l["satellites"], r)
    rd = r[3] if l["lecture"].strip() == "garder" else l["lecture"].strip()
    if not rd: raise ValueError(f"chantier 2 : cercle sans phrase ({l['cle']}, {l['forme']}, {crit})")
    return (crit, v, ws, rd, ss) if ss else (crit, v, ws, rd)


def _cercles(g, rows, k):
    import constats as B13
    par = collections.defaultdict(list)
    for l in rows: par[(l["cercle"], int(l["numero"]))].append(l)
    pris = set()
    ps = list(g.get("poles_impacts") or [])
    out, nps, cpt, ii = [], [], collections.Counter(), 0
    for r in g["rings"]:
        n = cpt[r[0]]; cpt[r[0]] += 1
        ls = par.get((r[0], n), [])
        pris.add((r[0], n))
        pole = ps[ii] if r[0] == "IMPACT" and ii < len(ps) else (ps[0] if ps else None)
        for l in ls:
            if l["cercle_actuel"].strip() != B13.decrit(r):
                raise ValueError(f"chantier 2 : cercle actuel « {B13.decrit(r)} » ≠ « {l['cercle_actuel']} » ({k}, {g['label']})")
        av = [l for l in ls if l["action"] == "ajouter avant"]
        ap = [l for l in ls if l["action"] == "ajouter après"]
        mod = [l for l in ls if l["action"] == "modifier"]
        ret = [l for l in ls if l["action"] == "retirer"]
        if len(mod) + len(ret) > 1: raise ValueError(f"chantier 2 : deux changements du même cercle ({k}, {g['label']}, {r[0]} {n})")
        for l in av:
            c = l["cercle_nouveau"].strip() or r[0]
            out.append(_cercle(l, None, c))
            if c == "IMPACT": nps.append(pole)
        if ret:
            if r[0] == "IMPACT": ii += 1
        else:
            out.append(_cercle(mod[0], r, r[0]) if mod else r)
            if r[0] == "IMPACT": nps.append(pole); ii += 1
        for l in ap:
            c = l["cercle_nouveau"].strip() or r[0]
            out.append(_cercle(l, None, c))
            if c == "IMPACT": nps.append(pole)
    manque = set(par) - pris
    if manque: raise ValueError(f"chantier 2 : cercles introuvables {manque} ({k}, {g['label']})")
    return out, (tuple(nps) if ps else g.get("poles_impacts"))


def _combinee(f, ls, cle, lot):
    """une forme combinée (B12) : les lignes visent ses cercles communs ; redessinée comme combinees.forme la dessine"""
    import combinees as CB, combos as KB, convert as C, spells as SP, phase4b as P, fautes as FT
    cb = f["combinee"]
    g = dict(f, rings=list(cb["communs"]), poles_impacts=None)
    communs, _ = _cercles(g, ls, cle)
    communs = [r if len(r) >= 5 else (*r[:4], []) for r in communs]      # un cercle de forme combinée porte toujours sa liste de satellites
    noyaux = [(n["combinaison"], list(n["cercles"])) for n in cb["noyaux"]]
    ecole, hemi, pole = cb["ecole"], cb["hemisphere"], cb["pole"]
    niveau = f["level"]
    crits = []
    for r in sorted(communs + [r for _, rs in noyaux for r in rs], key=lambda r: CB.RANG[r[0]]):
        if r[0] not in crits: crits.append(r[0])
    n_imp = sum(1 for r in communs if r[0] == "IMPACT") + sum(1 for _, rs in noyaux for r in rs if r[0] == "IMPACT")
    split, _ = P.split_poles(crits, hemi[0], niveau, [pole] * n_imp)
    def p_of(crit):
        if crit == "IMPACT": return "up" if pole == "lumineux" else "down"
        return "up" if crit in split[0] else "down"
    undet = []
    def des(rs):
        out = []
        for r in rs:
            a, ok = CB.anneau(r, p_of(r[0]))
            if not ok: undet.append(r[0])
            out.append(a)
        return out
    g_com = des(communs)
    g_noy = [(comb, SP.hyb(*KB.COMBOS[comb]), des(rs)) for comb, rs in noyaux]
    part = ([c for c in split[0] if c in undet], [c for c in split[1] if c in undet])
    lab_ecole = C.word(C.norm(ecole))
    nom = f"{f['fr']} — {f['label']}"
    dec = CB.dessin(lab_ecole, g_com, g_noy, True, nom); epu = CB.dessin(lab_ecole, g_com, g_noy, False, nom)
    svg = (SP.compose(dec, split, always=True), SP.compose(epu, part, always=False))
    svg_b = (CB.bande(nom, lab_ecole, g_noy, communs, split, part, pole, True), CB.bande(nom, lab_ecole, g_noy, communs, split, part, pole, False))
    rows = []
    for comb, rs in noyaux: rows += [(str(CB.RANG[r[0]]), f"{SP.NAMES[r[0]][1]} — Noyau {comb}", r[3]) for r in rs]
    rows.append(("1", "École", ecole))
    rows += [(str(CB.RANG[r[0]]), SP.NAMES[r[0]][1], r[3]) for r in communs]
    FAITS.append((lot, cle, f["label"]))
    rings = [x for _, rs in noyaux for x in rs] + communs
    return dict(f, rings=rings, svg=svg, rows=rows, split=split, bsplit=part, combinee=dict(cb, communs=communs, bande=svg_b))


def _forme(f, ls, cle, lot):
    import combinees as CB, corrections as K, constats as B13
    if K.est_elden_ring(f): raise ValueError(f"chantier 2 : Elden Ring n'est jamais touché ({cle}, {f['label']})")
    if f.get("combinee"):
        if any(l["action"] not in ACTIONS for l in ls): raise ValueError(f"chantier 2 : action inconnue ({cle})")
        return _combinee(f, ls, cle, lot)
    if any(l["jeu"] != B13.jeu(f) for l in ls): raise ValueError(f"chantier 2 : jeu {B13.jeu(f)} ({cle}, {f['label']})")
    autres = [l for l in ls if l["action"] not in ACTIONS]
    if autres: raise ValueError(f"chantier 2 : action inconnue {[l['action'] for l in autres]}")
    rings, ps = _cercles(f, ls, cle)
    FAITS.append((lot, cle, f["label"]))
    return CB._redessiner(dict(f, poles_impacts=ps), rings)


def appliquer(cle, formes):
    if cle not in CLES: return formes
    import corrections as K
    for lot, L in LOTS:
        out, vus, rang = [], set(), 0
        for f in formes:
            r0 = rang
            if not K.est_elden_ring(f) and not f.get("cree_4b"): rang += 1
            ls = L.get((cle, f["label"]))
            if not ls: out.append(f); continue
            if f["label"] in vus: raise ValueError(f"chantier 2 : deux formes « {f['label']} » ({cle})")
            vus.add(f["label"]); VU.add((lot, cle, f["label"]))
            lf = [l for l in ls if l["action"] not in FORMES_ACTIONS]
            g = _forme(f, lf, cle, lot) if lf else f
            ren = [l for l in ls if l["action"] == "renommer la forme"]
            if ren: g = dict(g, label=ren[0]["nouvelle_forme"].strip())
            nts = [l["lecture"].strip() for l in ls if l["action"] == "noter"]
            if nts: g = dict(g, notes=list(g.get("notes") or []) + nts)
            out.append(g)
            for l in [l for l in ls if l["action"] == "créer la forme"]:
                nom = l["nouvelle_forme"].strip()
                if nom in vus or any(x["label"] == nom for x in formes): raise ValueError(f"chantier 2 : forme « {nom} » déjà là ({cle})")
                nf = dict(f, label=nom, cree_4b=[r0, "chantier d'écriture 2 : une forme par choix au lancement"])
                ln = L.get((cle, nom), [])
                vus.add(nom); VU.add((lot, cle, nom))
                out.append(_forme(nf, ln, cle, lot) if ln else nf)
                CREEES.append((lot, cle, f["label"], nom))
        formes = out
    return formes


def manquantes():
    """les formes du chantier que la construction n'a pas rencontrées"""
    return sorted({(lot, k[0], k[1]) for lot, L in LOTS for k in L} - VU)
