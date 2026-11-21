"""Couche de corrections de la phase 4a.

Elle s'applique en toute fin de construction, sur les formes déjà construites
(cercles et phrases de lecture compris), juste après convert.build_forms et
avant le contrôle d'unicité de site.py. Les corrections décidées sont dans
donnees/phase4/ ; ce module ne décide rien.

Une forme se retrouve par sa clé de sort et son rang : sa position parmi les
formes de ce sort, à partir de 0, Elden Ring exclu (ses sorts ont leurs propres
clés « er-… » et ne sont jamais touchés).

Étape 1 : le module lit l'état cible, retrouve chaque forme et compare
« origine » aux cercles actuels. Une forme dont l'origine ne correspond pas
n'est pas touchée.

Étape 2 : pour chaque forme retrouvée, la liste « cercles » remplace tous les
cercles, dans l'ordre donné. Un cercle « inchangé » reprend tel quel le cercle
actuel (phrase et satellites compris). Un cercle « modifié » garde pour
l'instant sa « lecture_d_origine », un cercle « ajouté » n'a pas encore de
phrase : les phrases viennent à l'étape 3. Les satellites des cercles
« modifié » et « ajouté » sont placés par la règle du moteur (_place) ; les
grands nombres décidés s'écrivent par multiplication (_grands) ; puis la passe
supports du moteur est appliquée à la forme (_supports). Aucune autre passe de
la construction ordinaire n'est rejouée. La répartition lumineux/ténébreux
des formes hybrides et des arts rares est recalculée par la règle du moteur
(split_hybrid, split_rare), puis le glyphe est redessiné (spells.build).

    python corrections.py    → compte rendu
"""
import os, json
import spells as SP
import phase4b as P4B

D = os.path.dirname(os.path.abspath(__file__))
P4 = os.path.join(D, "..", "donnees", "phase4")
CIBLE = json.load(open(os.path.join(P4, "A_etat_cible_final.json"), encoding="utf-8"))["formes"]
PAR_CLE = {(x["cle"], x["rang"]): x for x in CIBLE}

ETAPE = int(os.environ.get("PHASE4_ETAPE", "7"))     # étapes de la phase 4a appliquées (2 : cercles ; 3 : phrases ; 4 : verbes ; 5 : éléments ; 6 : niveaux et retraits)
_vues = {}        # (cle, rang) → (forme construite, cercles actuels) pour chaque forme de l'état cible retrouvée
_faites = {}      # (cle, rang) → nombre de cercles changés (modifiés + ajoutés + retirés)


def est_elden_ring(forme):
    return forme["dnd"].startswith("Elden Ring")


def _norm(x):
    """une valeur comparable à celle du fichier JSON (tuples en listes)"""
    return json.loads(json.dumps(x, ensure_ascii=False, default=repr))


def cercles_actuels(forme):
    """les cercles d'une forme construite, comme le fichier les écrit : [cercle, valeur, mots]"""
    return [[r[0], _norm(r[1]), _norm(list(r[2]))] for r in forme["rings"]]


def satellite_moteur(s):
    """un satellite du fichier {position, valeur, texte, options} → le tuple du moteur (position, valeur[, texte[, options]])"""
    v = s["valeur"]
    if isinstance(v, dict) and "sym" in v:
        v = ("sym", v["sym"])
    t = (s["position"], v, s["texte"], s["options"])
    if not s["options"]:
        t = t[:3]
        if not s["texte"] and not isinstance(v, tuple):
            t = t[:2]
    return t


def repartition(f, crits):
    """la répartition des cercles entre les deux pôles, par la règle du moteur"""
    import convert as C
    if f.get("regle_4b"):                     # phase 4b : règle des pôles (Impact par cercle)
        return P4B.repartition(f, crits)
    if f["fam"] == "H":
        return C.split_hybrid(crits, "H" if "Hodolin" in f["verb"] else "G", f["level"])
    if f["fam"] == "R":
        return C.split_rare(crits)
    return f["split"]


CRITERES = {"CIBLE", "FORME", "AMPLEUR", "DUREE", "LOCALISATION", "CONDITION", "IMPACT", "QUANTITE", "COMPOSANTE", "INTERACTION", "COSMETIQUE"}


def _transcrire(c):
    """les mots d'un cercle passent par convert.word, comme ceux d'une fiche : transcription en Alde pour le dessin.
    Cela n'ajoute rien au lexique fermé (donnees/lexique_1001.json) : un mot qui n'en est pas est signalé par lint."""
    import convert as C
    for w in c["mots"]:
        C.word(w)
    for s in c["satellites"]:
        for w in s["texte"].split():
            if w not in CRITERES:
                C.word(w)


# Grands nombres (décision du 20 novembre) : un satellite trop long à dessiner s'écrit par multiplication, les formes
# multipliées dans le satellite lui-même (spells.best_factors, cinq formes au plus, jamais trois fois la même), avec
# l'annotation « fois ». (annotation, valeur du fichier) → valeur écrite ; une valeur différente est un arrondi.
GRANDS = {("AMPLEUR KILOMETRES", 1400): 1400,          # 7 × 5 × 5 × 4 × 2
          ("VIE REPARTIR", 68): 70,                    # 7 × 5 × 2
          ("VIE REPARTIR", 117): 120,                  # 5 × 4 × 3 × 2
          ("VIE REPARTIR", 124): 120}                  # 5 × 4 × 3 × 2
ARRONDIS = {}     # (cle, rang) → [(annotation, valeur du fichier, valeur écrite)] : pour la phrase de lecture (étape 3)


def _grands(sats, k):
    out = []
    for st in sats:
        t = st[2] if len(st) > 2 else ""
        n = GRANDS.get((t, st[1]))
        if n is None:
            out.append(st); continue
        ARRONDIS.setdefault(k, []).append((t, st[1], n))
        crit = len(st) > 3 and st[3] and st[3].get("crit")
        t2 = t if crit else t + " FOIS"        # un satellite d'un autre critère reçoit « fois » au dessin (spells.sat_label)
        out.append((st[0], n, t2, *st[3:]))
    return out


# ---------- étape 3 : phrases de lecture ----------
# Les formules sont celles de convert.build_spell, critère par critère ; les satellites se lisent comme convert.sat_reading.
PHRASES = {}      # (cle, rang) → [(cercle, état, phrase d'origine, phrase nouvelle)] : pour le compte rendu


def _accents():
    """l'orthographe accentuée des mots, relevée dans les textes du moteur (fiches et tables de mots) : l'état cible écrit
    les mots normalisés (sans accents). Le mot le plus souvent écrit l'emporte ; la table du moteur (ACCENTS) reste prioritaire."""
    import re, glob, collections, convert as C
    vu = collections.defaultdict(collections.Counter)
    for p in glob.glob(os.path.join(D, "*.py")):
        if os.path.basename(p) in ("corrections.py",): continue
        for t in re.findall(r"[a-zàâäçéèêëîïôöùûüœ]+(?:-[a-zàâäçéèêëîïôöùûüœ]+)*", open(p, encoding="utf-8").read()):
            vu[C.norm(t)][t] += 1           # toutes les orthographes, sans accent comprises (« entrave » contre « entravé »)
    out = {}
    for n, c in vu.items():
        t = c.most_common(1)[0][0]
        if t != n.lower(): out[n] = t
    return out
_ACC = None


class _Accentue:
    """le temps d'écrire les phrases d'une forme corrigée, la table d'affichage du moteur connaît aussi les mots relevés"""
    def __enter__(self):
        global _ACC
        import convert as C
        if _ACC is None: _ACC = _accents()
        self.ajout = {n: t for n, t in _ACC.items() if n not in C.ACCENTS}
        C.ACCENTS.update(self.ajout)
    def __exit__(self, *a):
        import convert as C
        for n in self.ajout: C.ACCENTS.pop(n, None)


def parenthese(lecture):
    """la parenthèse de lecture d'une phrase (« plein, lueur · mouvement (quatre lueurs mobiles) ») : celle qui suit la tête,
    avant le premier « ; » ; parenthèses imbriquées comprises. Renvoie '' s'il n'y en a pas."""
    i, j = lecture.find(" ("), lecture.find(" ; ")
    if i < 0 or (0 <= j < i): return ""
    n = 0
    for k in range(i + 1, len(lecture)):
        n += {"(": 1, ")": -1}.get(lecture[k], 0)
        if n == 0: return lecture[i:k + 1]
    return lecture[i:]


def _tete(crit, v, mots):
    import convert as C
    m = " · ".join(C.shown(w) for w in mots)
    if crit == "IMPACT":
        return ("plein" if v == "plein" else f"intensité {v}") + (f", {m}" if mots else ", sans nature : la force brute du verbe")
    if crit == "CIBLE":
        t = "vide : la trame elle-même" if v is None else C.CIBLES.get(v, str(v))
        return t + (f", précisé « {m} »" if mots else "")
    if crit == "CONDITION":
        return " ; ".join(f"« {C.shown(w)} »" for w in mots) or str(v)
    if crit == "DUREE":
        u = next((w for w in mots if w in C.UNIT_FR), None)
        fin = [w for w in mots if w != u]
        t = (C.fr_time(v, u) if u else ("jusqu'à dissipation" if v == "plein" else str(v)))
        return t + (f" ; fin : « {' · '.join(C.shown(w) for w in fin)} »" if fin else "")
    if crit == "QUANTITE":
        return f"{v} « {m} »" if mots else f"{v} instances du sort"
    if crit == "COMPOSANTE" and mots[:1] == ["CONTREPARTIE"]:
        reste = " · ".join(C.shown(w) for w in mots[1:])
        return f"{v} : contrepartie" + (f", « {reste} »" if reste else "")
    return f"{C.vshow(v) if v != 'plein' else 'plein'}" + (f", {m}" if mots else "")


def _explique(crit, v, ws, sats, ring_mots):
    """l'explication que le moteur attache à certains satellites, selon la règle qui les pose (convert : emprunt_et_rythme,
    _repete, _allure, energies_et_cibles)"""
    import convert as C
    if crit == "DUREE" and v == 1 and ws == ["CHAQUE", "INSTANTS"]:
        allure = any(len(st) > 2 and str(st[2]).split()[:1] == ["LOCALISATION"] and "METRES" in str(st[2]).split() for st in sats)
        return " : une allure" if allure else " : l'effet revient à chaque instant"
    if crit == "DUREE" and v == "plein" and not ws and ring_mots[:1] == ["VIE"]:
        return " : d'emprunt, elle ne dure que ce que dure le sort"
    if crit == "QUANTITE" and v == "plein" and not ws: return " : en entier"
    if crit == "QUANTITE" and v == 1 and not ws and ring_mots[:1] == ["VIE"]: return " : une seule à la fois, elle ne s'ajoute pas à une autre"
    if crit == "CIBLE" and v == 1 and not ws: return " : soi, celui qui lance"
    if crit == "CIBLE" and v in (2, 3) and not ws: return f" : {C.CIBLES[v]}"
    return ""


def _lecture_sats(sats, k, ring_mots=()):
    """la lecture des satellites d'un cercle, comme convert.sat_reading ; symboles groupés comme energies_et_cibles"""
    ring_mots = list(ring_mots)
    import convert as C, combos as KB
    out, elems = "", []
    for st in sats:
        v = st[1]; t = st[2] if len(st) > 2 and st[2] else ""; o = st[3] if len(st) > 3 and st[3] else {}
        if isinstance(v, tuple) and v[0] == "sym":
            if v[1] in ("feu", "air", "terre", "eau"): elems.append(v[1])
            else: out += f" ; satellite : symbole de {C.SYM_FR[v[1]]}"
            continue
        ws = t.split()
        crit = o.get("crit") or (ws[0] if ws and ws[0] in SP.NAMES else None)
        if ws and ws[0] == crit: ws = ws[1:]
        ws = [w for w in ws if w != "FOIS"]
        if crit == "INTERACTION":
            out += f" ; satellite Interaction {v} : seulement les sorts dont l'Interaction ne dépasse pas {v}"; continue
        val = "" if (v is None and crit) else C.vshow(v)        # un satellite sans valeur ne dit que son critère et ses mots
        out += f" ; satellite {SP.NAMES[crit][1] if crit else ''}{' ' if crit and val else ''}{val}".rstrip() + (f" « {' · '.join(C.shown(w) for w in ws)} »" if ws else "")
        out += _explique(crit, v, ws, sats, ring_mots)
        for (t0, n0, n1) in ARRONDIS.get(k, []):
            if t0 == t and n1 == v:
                f_ = " × ".join(str(x) for x in SP.best_factors(v))
                out += (f" : {v} s'écrit {f_} « fois »" if n0 == n1 else f", arrondi de {n0} à {n1} pour s'écrire {f_} « fois »")
    if elems:
        cnt = tuple(elems.count(e) for e in ("feu", "air", "terre", "eau"))
        nom = next((n for n, c in KB.COMBOS.items() if tuple(c) == cnt), None) if len(elems) > 1 else None
        de = lambda e: "du feu" if e == "feu" else "de " + C.SYM_FR[e]
        out += (f" ; satellites : les symboles de la combinaison {nom}" if nom
                else f" ; satellite : symbole {de(elems[0])}" if len(elems) == 1
                else " ; satellites : symboles " + ", ".join(de(e) for e in elems))
    return out


def _arrondi_garde(lecture, v):
    """un arrondi déjà dit par la phrase d'origine (« arrondi de 170 à 168 pour s'écrire en 4 formes ») se garde quand la
    valeur écrite est toujours la valeur arrondie"""
    import re
    m = re.search(r" ; arrondi de (\d+) à (\d+) pour s'écrire en \d+ formes", lecture)
    return m.group(0) if m and isinstance(v, int) and int(m.group(2)) == v else ""


LIBRES = {}       # (cle, rang) → [(phrase d'origine, partie libre gardée)] : phrases sans parenthèse dont une description est gardée


def _tetes(crit, v, mots):
    """les débuts que le moteur écrit pour ce cercle (il en a parfois deux : un Impact sans mot dit ou non « sans nature »)"""
    t = {_tete(crit, v, mots)}
    if crit == "IMPACT" and not mots: t.add("plein" if v == "plein" else f"intensité {v}")
    if crit == "IMPACT" and mots == ["VIE"] and v != "plein": t.add(f"intensité {v} de vie")
    if crit == "CIBLE" and mots:           # une Cible-objet : « objet annoté « potion » » (convert.build_spell, cible_obj)
        import convert as C
        reste = " · ".join(C.shown(w) for w in mots[1:])
        t.add(f"objet annoté « {C.shown(mots[0])} »" + (f", précisé « {reste} »" if reste else ""))
    return t


def _libre(lecture, r0):
    """la partie libre d'une phrase d'origine sans parenthèse : ce que le moteur n'écrit pas lui-même pour le cercle
    d'origine r0 (ni son début, ni ses satellites, ni ses fins). Vide : la phrase est purement générée."""
    import re
    reste = lecture
    def meme(a, b):          # même tête, à l'ordre des mots près (le moteur range parfois les mots autrement que le cercle)
        a = a.replace(" », précisé « ", " · ")         # deux « précisé » de suite (passe supports) = un seul
        if a == b: return True
        pa, _, ma = a.partition(", "); pb, _, mb = b.partition(", ")
        return pa == pb and sorted(ma.split(" · ")) == sorted(mb.split(" · "))
    for t in sorted(_tetes(r0[0], r0[1], r0[2]), key=len, reverse=True):
        tete = reste[:len(t)] if " ; " in t else reste.split(" ; ")[0]      # une tête qui contient « ; » (Condition, fin de Durée)
        if meme(tete, t):
            reste = reste[len(tete):]; break
    libres = []
    for seg in [s for s in reste.split(" ; ") if s]:
        if re.match(r"(satellites? |satellite :|ce que l'effet touche|arrondi de \d+ à|l'énergie \(|le tourbillon est inscrit|fin : )", seg):
            continue
        libres.append(seg)
    return " ; ".join(libres)


def _fins(f, c, i, k, rings):
    """les fins que le moteur écrit lui-même, par ses règles : énergie dite par le noyau (REDIT), tourbillon en Forme"""
    import re, convert as C
    out = ""
    w = NOYAU_DIT.get((k[0], k[1], i))
    if w is None and c["etat"] == "modifié":
        m = re.search(r"l'énergie \(« ([^»]+) »\) est dite par le noyau", c["lecture_d_origine"])
        sats = rings[i][4] if len(rings[i]) > 4 and rings[i][4] else []
        if m and f["fam"] == "H" and not any(isinstance(st[1], tuple) for st in sats): w = C.norm(m.group(1))
    if w: out += f" ; l'énergie (« {C.shown(w)} ») est dite par le noyau"
    if c["etat"] == "modifié" and "le tourbillon est inscrit par les cercles Forme" in c["lecture_d_origine"] and any(r[0] == "FORME" for r in rings):
        out += " ; le tourbillon est inscrit par les cercles Forme (zone, puis hélice)"
    return out


def _phrases(rings, x, k, f):
    """étape 3 : un cercle ajouté reçoit sa phrase ; un cercle modifié, un début régénéré et la parenthèse d'origine ;
    sans parenthèse, la partie libre de la phrase d'origine (une description) est gardée entre parenthèses"""
    out = []
    for i, (r, c) in enumerate(zip(rings, x["cercles"])):
        if c["etat"] == "inchangé":
            out.append(r); continue
        sats = list(r[4]) if len(r) > 4 and r[4] else []
        lo = c["lecture_d_origine"]
        p = ""
        if c["etat"] == "modifié":
            p = parenthese(lo)
            if not p:
                # le cercle d'origine : celui qui portait cette phrase ; à défaut, chaque cercle d'origine de même critère
                cands = [g for g in f["rings"] if g[0] == r[0] and g[3] == lo] or [g for g in f["rings"] if g[0] == r[0]]
                libs = [_libre(lo, g) for g in cands] or [lo]
                lib = min(libs, key=len)
                if lib:
                    p = f" ({lib})"; LIBRES.setdefault(k, []).append((lo, lib))
        neuve = (_tete(r[0], r[1], r[2]) + p + _lecture_sats(sats, k, r[2])
                 + (_arrondi_garde(lo, r[1]) if c["etat"] == "modifié" else "") + _fins(f, c, i, k, rings))
        if c["etat"] == "modifié":
            # un même satellite déjà expliqué dans la phrase d'origine garde l'explication que le moteur lui avait donnée
            # (la règle qui l'a posé : « une allure, non un élan » pour une mesure sortie de l'Impact, etc.)
            orig = {s.split(" : ")[0]: s for s in lo.split(" ; ") if s.startswith("satellite ") and " : " in s}
            neuve = " ; ".join(orig.get(s.split(" : ")[0], s) if s.startswith("satellite ") else s for s in neuve.split(" ; "))
        PHRASES.setdefault(k, []).append((r[0], c["etat"], lo, neuve))
        out.append((r[0], r[1], r[2], neuve, sats))
    return out


LEVEES = {}       # (cle, rang) → nombre d'Impacts où « aptitude » nomme un état levé et reste dans l'Impact


def _supports(cle, rings, k=None):
    """la passe du moteur (convert.supports) : ce sur quoi l'effet agit quitte l'Impact pour la Cible ; un seul Impact :
    le cercle Cible ; plusieurs : un satellite Cible de l'Impact concerné. Exceptions du moteur gardées (supports_mots).
    Exception de la phase 4a : sur un Impact qui porte un satellite de seuil « IMPACT APTITUDE », « aptitude » nomme un
    état que le sort lève (une faculté diminuée), comme « aveuglement » ou « poison » : ce n'est pas un support, il reste."""
    import convert as C
    C._PAGE[0] = cle
    gardes = {}
    rings = list(rings)
    for i, r in enumerate(rings):
        sats = r[4] if len(r) > 4 and r[4] else []
        if r[0] == "IMPACT" and "APTITUDE" in r[2] and any(len(st) > 2 and str(st[2]).split()[:2] == ["IMPACT", "APTITUDE"] for st in sats):
            gardes[i] = r[2].index("APTITUDE")
            rings[i] = (r[0], r[1], [w for w in r[2] if w != "APTITUDE"], *r[3:])
    if gardes and k is not None: LEVEES[k] = len(gardes)
    out = C.supports(rings)
    for i, pos in gardes.items():          # le mot retrouve sa place parmi les mots de l'Impact
        r = out[i]; ws = list(r[2]); ws.insert(pos, "APTITUDE")
        out[i] = (r[0], r[1], ws, *r[3:])
    return out


NOYAU_DIT = {}    # (cle, rang, indice du cercle) → mot de l'énergie que le noyau dit déjà


def _noyau(f, rings, x, k):
    """règle du moteur pour un sort hybride (convert, REDIT) : une énergie que la combinaison du noyau dit déjà n'est pas
    répétée sur l'Impact ; son symbole n'est pas posé, et la lecture dit « l'énergie (« … ») est dite par le noyau »"""
    import re, convert as C
    if f["fam"] != "H": return rings
    m = re.search(r"· ([^·(]+?) \(", f["verb"])
    if not m: return rings
    comb = m.group(1).strip(); red = C.REDIT.get(comb, set()) | {C.norm(comb)}
    MOT = {"feu": "FEU", "air": "AIR", "terre": "TERRE", "eau": "EAU"}
    out = []
    for i, (r, c) in enumerate(zip(rings, x["cercles"])):
        sats = list(r[4]) if len(r) > 4 and r[4] else []
        dits = [st for st in sats if isinstance(st[1], tuple) and st[1][1] in MOT and MOT[st[1][1]] in red]
        if r[0] == "IMPACT" and c["etat"] != "inchangé" and dits:
            NOYAU_DIT[(k[0], k[1], i)] = MOT[dits[0][1][1]]
            reste = [st for st in sats if st not in dits]
            r = (r[0], r[1], r[2], r[3], _place(reste))
        out.append(r)
    return out


def _place(sats):
    """placement des satellites par la règle du moteur (convert._resats, comme place_sats) : un seul au nord ou au sud,
    deux de part et d'autre, trois et plus en étoile. Appliqué aux seuls cercles « modifié » et « ajouté »."""
    import convert as C
    return C._resats(sats) if sats else sats


def _cercles(f, x):
    """étape 2 : les cercles de l'état cible, dans l'ordre ; renvoie (cercles, nombre de cercles changés)"""
    restants = list(f["rings"])
    out, changes = [], 0
    for c in x["cercles"]:
        if c["etat"] == "inchangé":
            r = next(r for r in restants if r[0] == c["cercle"] and _norm(r[1]) == c["valeur"] and _norm(list(r[2])) == c["mots"])
            restants.remove(r)
            out.append(r)
            continue
        changes += 1
        _transcrire(c)
        lecture = c["lecture_d_origine"] if c["etat"] == "modifié" else ""
        sats = [satellite_moteur(s) for s in c["satellites"]]
        out.append((c["cercle"], c["valeur"], list(c["mots"]), lecture, _place(sats)))
    retires = len(restants) - sum(c["etat"] == "modifié" for c in x["cercles"])     # un cercle modifié remplace un cercle actuel
    return out, changes + max(0, retires), len(restants)


def _redessine(f, rings):
    crits = list(dict.fromkeys(r[0] for r in rings))
    split = repartition(f, crits)
    svg, rows = SP.build(f["core"], f["pol"], rings, f["r0"], split, officiants=f["officiants"], impacts=f.get("poles_impacts"))
    return dict(f, rings=rings, split=split, svg=svg, rows=rows, bsplit=SP.PART[0])


# ---------- étapes 4, 5, 6 : verbes, éléments des formes hybrides, niveaux et formes en trop ----------
import csv as _csv
def _lire(nom):
    p = os.path.join(P4, nom)
    return list(_csv.DictReader(open(p, encoding="utf-8-sig"), delimiter=";")) if os.path.exists(p) else []
VERBES = {(l["cle"], int(l["rang"])): l for l in _lire("A1_verbes.csv")}
ELEMENTS = {(l["cle"], int(l["rang"])): l for l in _lire("A2a_hybride_changements_element.csv")}
A4 = [l for l in _lire("A4_niveaux_formes.csv") if l["action"] in ("corriger le niveau", "corriger la lecture", "retirer la forme")]
FAITS = {"verbe": [], "element": [], "niveau": [], "lecture": [], "retrait": []}      # (cle, rang) appliqués
REFUS = {"verbe": [], "element": [], "niveau": [], "lecture": [], "retrait": []}      # (ligne, raison)


def _a4(f, k):
    """les lignes d'A4 qui visent cette forme : par « cle, rang » quand la ligne les donne, sinon par sort et forme"""
    import re
    out = []
    for l in A4:
        m = re.search(r"\(cle ([^,]+), rang (\d+)\)", l["forme"])
        if (m and (m.group(1), int(m.group(2))) == k) or (not m and l["sort"] == f["fr"] and l["forme"] == f["label"]):
            out.append(l)
    return out


def _verbe(g, l, k):
    """étape 4 : le verbe du Noyau d'une forme arcane devient verbe_nouveau (contrôle : verbe_actuel)"""
    import convert as C
    if l["verbe_actuel"] != g["verb"] or g["fam"] != "A":
        REFUS["verbe"].append((l, f"verbe actuel « {g['verb']} »")); return g
    vk, vn = next(key for key, nom in C.VERBS.items() if nom == l["verbe_nouveau"])
    FAITS["verbe"].append(k)
    return dict(g, core=SP.verb(vk, vn), pol="down" if vn else "up",
                verb=f"{C.VERBS[(vk, vn)]} · {C.VERB_GROUP[vk].lower()} {'−' if vn else '+'}")


def _element(g, l, k):
    """étape 5 : la combinaison du Noyau d'une forme hybride devient element_nouveau ; pôle donné : Hodolin (Noyau
    lumineux) ou Galombar (Noyau ténébreux), comme le moteur les relie (split_hybrid) ; contrôles : noyau et élément actuels"""
    import convert as C, combos as KB, re
    m = re.match(r"(.+) · (Hodolin|Galombar) · (.+) \(", g["verb"])
    if g["fam"] != "H" or l["noyau_actuel"] != g["verb"] or not m or m.group(3) != l["element_actuel"]:
        REFUS["element"].append((l, f"noyau actuel « {g['verb']} »")); return g
    if l["element_nouveau"] not in KB.COMBOS:
        REFUS["element"].append((l, f"combinaison inconnue « {l['element_nouveau']} »")); return g
    ecole, hemi = m.group(1), m.group(2)
    if l["pole"]: hemi = {"lumineux": "Hodolin", "ténébreux": "Galombar"}[l["pole"]]
    comb = l["element_nouveau"]; f_, a_, t_, e_ = KB.COMBOS[comb]
    notes = [n.replace(f"combinaison {l['element_actuel']}", f"combinaison {comb}", 1) if i == 0 else n for i, n in enumerate(g["notes"])]
    FAITS["element"].append(k)
    return dict(g, core=SP.hyb(f=f_, a=a_, t=t_, e=e_, label=C.norm(ecole)), verb=f"{ecole} · {hemi} · {comb} ({KB.code(comb)})", notes=notes,
                element_par_defaut=False)        # l'élément est maintenant donné (étape 7 : plus d'élément d'école)


def _niveau_lecture(g, ls, k):
    """étape 6 : le niveau corrigé (et le cercle Interaction, qui vaut niveau + 1) ; une lecture corrigée"""
    import re
    for l in ls:
        if l["action"] == "corriger le niveau":
            a, b = [int(x) for x in re.findall(r"\d+", l["detail"])[:2]]
            if g["level"] != a:
                REFUS["niveau"].append((l, f"niveau actuel {g['level']}")); continue
            rings = []
            for r in g["rings"]:
                if r[0] == "INTERACTION" and r[1] == a + 1:
                    rd = re.sub(rf"^{a + 1} : sort de niveau {a}\b", f"{b + 1} : sort de niveau {b}", r[3])
                    r = (r[0], b + 1, r[2], rd, *r[4:])
                rings.append(r)
            g = dict(g, level=b, rings=rings); FAITS["niveau"].append(k)
        elif l["action"] == "corriger la lecture":
            av, ap = re.findall(r"« ([^»]+) »", l["detail"])[:2]
            if not any(av in r[3] for r in g["rings"]):
                REFUS["lecture"].append((l, "texte « " + av + " » absent")); continue
            g = dict(g, rings=[(r[0], r[1], r[2], r[3].replace(av, ap), *r[4:]) for r in g["rings"]]); FAITS["lecture"].append(k)
    return g


def appliquer(cle, formes):
    """reçoit les formes construites d'un sort et les rend corrigées ; les formes sont retrouvées par leur rang d'origine,
    et les formes retirées le sont en dernier"""
    rang, out = 0, []
    for f in formes:
        if est_elden_ring(f):
            out.append(_symboles(f))          # règle de dessin : elle vaut aussi pour Elden Ring
            continue
        k = (cle, rang)
        rang += 1
        g, change = f, False
        x = PAR_CLE.get(k)
        if x is not None:
            _vues[k] = (f, cercles_actuels(f))
            if _norm(x["origine"]) == cercles_actuels(f):          # sinon : ne pas appliquer (signalé par bilan())
                rings, n, _ = _cercles(f, x)
                rings = [(r[0], r[1], r[2], r[3], _grands(r[4], k)) if c["etat"] != "inchangé" and len(r) > 4 and r[4] else r
                         for r, c in zip(rings, x["cercles"])]          # grands nombres : cercles modifiés et ajoutés seulement
                with _Accentue():
                    if ETAPE >= 3:
                        rings = _noyau(f, rings, x, k)
                        rings = _phrases(rings, x, k, f)
                    rings = _supports(cle, rings, k)
                _faites[k] = n
                g, change = dict(f, rings=rings), True
        if ETAPE >= 4 and k in VERBES:
            g2 = _verbe(g, VERBES[k], k); change |= g2 is not g; g = g2
        if ETAPE >= 5 and k in ELEMENTS:
            g2 = _element(g, ELEMENTS[k], k); change |= g2 is not g; g = g2
        retirer = False
        if ETAPE >= 6:
            ls = _a4(f, k)
            g2 = _niveau_lecture(g, [l for l in ls if l["action"] != "retirer la forme"], k); change |= g2 is not g; g = g2
            if any(l["action"] == "retirer la forme" for l in ls):
                retirer = True; FAITS["retrait"].append(k)
        if not retirer:                       # phase 4b (couche voisine phase4b.py) : formes existantes de B3
            g2, retirer = P4B.existante(g, k); change |= g2 is not g; g = g2
        g2 = P4B.relecture(g, k, True); change |= g2 is not g; g = g2       # B6 : modèle et formes hybrides créées
        b4 = P4B.b4(k)                        # étape 7 : formes nouvelles (B4)
        remplace = [b for b in b4 if b["action"] == "remplacer la forme modèle"]
        if remplace:                          # les formes nouvelles et leurs jumelles prennent la place du modèle et de ses jumelles
            nouvelles = []
            for b in remplace:
                nf = P4B.nouvelle(g, b, k)
                if nf is not None: nouvelles += [nf] + (P4B.jumelles(nf, k) if nf["fam"] == "A" else [])
            if nouvelles:
                retirer = True; P4B.FAITS["retrait"].append(k)
        else:
            for b in b4:
                g2 = P4B.renomme(g, b); change |= g2 is not g; g = g2
            nouvelles = P4B.creer(g, k)       # phase 4b : formes créées d'après ce modèle, placées juste après lui
            for b in b4:                      # « ajouter » : la forme nouvelle (et ses jumelles) après le modèle
                nf = P4B.nouvelle(g, b, k)
                if nf is not None: nouvelles += [nf] + (P4B.jumelles(nf, k) if nf["fam"] == "A" else [])
        g2 = P4B.relecture(g, k, False); change |= g2 is not g; g = g2      # B6 : forme d'Arcane modèle seulement
        if not retirer:
            if change:
                rings, touche = _placer(g["rings"])
                PLACES.extend((g["idx"], g["label"], c) for c in touche)
                out.append(_redessine(g, rings))
            else:
                out.append(_symboles(f))
        for nf in nouvelles:
            rings, touche = _placer(nf["rings"])
            PLACES.extend((nf["idx"], nf["label"], c) for c in touche)
            out.append(_redessine(nf, rings))
    return out


# ---------- placement des symboles à côté d'autres satellites (règle de dessin, après toutes les corrections) ----------
PLACES = []         # (cle, libellé de la forme, critère du cercle) des cercles replacés
def _placer(rings):
    import convert as C
    out, touche = [], []
    for r in rings:
        s = r[4] if len(r) > 4 and r[4] else None
        p = C.placer_symboles(s) if s else None
        if p is not None and p != list(s):
            out.append((*r[:4], p, *r[5:])); touche.append(r[0])
        else:
            out.append(r)
    return out, touche
def _symboles(f):
    """une forme que rien d'autre ne change : seuls les angles bougent ; la répartition des pôles est gardée"""
    rings, touche = _placer(f["rings"])
    if not touche: return f
    PLACES.extend((f["idx"], f["label"], c) for c in touche)
    svg, rows = SP.build(f["core"], f["pol"], rings, f["r0"], f["split"], officiants=f["officiants"], impacts=f.get("poles_impacts"))
    return dict(f, rings=rings, svg=svg, rows=rows, bsplit=SP.PART[0])


def bilan():
    """retrouvées, origines conformes, et le détail de chaque écart"""
    introuvables = [k for k in PAR_CLE if k not in _vues]
    ecarts = []
    for k, x in PAR_CLE.items():
        if k not in _vues:
            continue
        f, actuels = _vues[k]
        controle = [c for c, a, b in (("sort", x["sort"], f["fr"]), ("forme", x["forme"], f["label"]), ("niveau", x["niveau"], f["level"])) if a != b]
        if _norm(x["origine"]) != actuels or controle:
            ecarts.append(dict(cle=k[0], rang=k[1], sort=x["sort"], forme=x["forme"], controle=controle,
                               attendu=x["origine"], actuel=actuels))
    return dict(total=len(PAR_CLE), retrouvees=len(_vues), introuvables=introuvables,
                conformes=len(_vues) - len(ecarts), ecarts=ecarts)


if __name__ == "__main__":
    import sys
    sys.path.insert(0, D)
    import convert as C
    from fiches import FICHES
    for k, fi in FICHES.items():
        appliquer(k, C.build_forms(k, fi))
    b = bilan()
    print(f"état cible : {b['total']} formes ; retrouvées {b['retrouvees']} ; introuvables {len(b['introuvables'])} ; "
          f"origine conforme {b['conformes']} ; écarts {len(b['ecarts'])}")
    print(f"étape 2 : {len(_faites)} formes recevant leurs cercles ; {sum(_faites.values())} cercles changés")
    for k in b["introuvables"]:
        print("  introuvable :", k)
    for e in b["ecarts"]:
        print(f"  écart : {e['cle']} rang {e['rang']} · {e['sort']} [{e['forme']}]" + (f" · contrôle {e['controle']}" if e["controle"] else ""))
        print("     attendu :", json.dumps(e["attendu"], ensure_ascii=False))
        print("     actuel  :", json.dumps(e["actuel"], ensure_ascii=False))
