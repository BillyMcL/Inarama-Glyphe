"""Répertoire des cercles (base du barème) : un relevé, rien n'est écrit dans la bibliothèque ni dans le site.

    python outils/repertoire_cercles.py <dossier de sortie> [<dossier du moteur du barème>]

Un cercle = (type, valeur, mots dans l'ordre, satellites avec position, valeur, texte, options). Le cercle d'Interaction
(le niveau) est exclu du répertoire ; le Noyau n'est pas un cercle, il est noté à part pour chaque forme.
Écrit repertoire_cercles.json, repertoire_cercles.csv, paires_cercles.json et les comptes du bilan (repertoire_comptes.json).
Le second argument (facultatif) est le dossier « moteur » où se trouve bareme.py (branche bareme) : l'apport du barème actuel
à chaque cercle y est mesuré. Sans lui, cette partie est laissée vide.
"""
import os, sys, json, collections, statistics, itertools, re
ICI = os.path.dirname(os.path.abspath(__file__))
MOT = os.path.join(ICI, "..", "moteur")
sys.path.insert(0, MOT); os.chdir(MOT)
import convert as C, corrections as K, spells as SP
from fiches import FICHES
OUT = sys.argv[1] if len(sys.argv) > 1 else "."
B = None
if len(sys.argv) > 2:
    sys.path.insert(0, os.path.abspath(sys.argv[2]))
    import bareme as B

SYSTEME = {"5.1": "D&D 5", "5.2": "D&D 5", "3.5": "3.5", "pf1": "PF1", "pf2": "PF2", "pf2r": "PF2"}
JEU = {"5.1": "5e", "5.2": "2024", "3.5": "3.5", "pf1": "PF1", "pf2": "PF2", "pf2r": "PF2 remaniée"}
SYSTEMES = ["D&D 5", "3.5", "PF1", "PF2"]
ORDRE = list(SP.NAMES)
REGLES = {"CIBLE": ("cibles", "budget", "psyché", "cible profonde", "cible-objet", "limitation"), "FORME": ("zone",), "AMPLEUR": ("zone",),
          "LOCALISATION": ("distance",), "DUREE": ("durée", "fin «", "incantation longue", "état d'un instant", "sort long"),
          "CONDITION": ("condition ou exigence", "occasion", "condition qui ouvre", "seuil de vie", "concentration"),
          "COMPOSANTE": ("Composante", "contrecoup"), "QUANTITE": ("quantité",)}


NOM_SORTE = {"blessure": "2.1 montant", "état": "2.1 état (prix du degré sur l'échelle)", "outil": "2.1 prix fixe (outil, déplacement)",
             "seuil": "2.1 seuil (lever, garder, dissiper)", "être": "2.1 être appelé (puissance)", "forme prise": "2.1 forme prise",
             "souhait": "2.1 souhait", "inconnu": "2.1 aucun mot connu (défaut 3,0)"}


def fragments(detail):
    """les règles nommées d'un détail de calcul : « nom§fragment complet » (le fragment garde ses nombres, pour voir ce qui change)"""
    out = set()
    for d in detail:
        if d.startswith("effet ") or d.startswith("2.3 plusieurs effets"): continue
        d = re.sub(r" → .*$", "", d)                       # le total des rabais
        if d.startswith(("2.4 ajouts : ", "2.5 rabais : ")):
            sec, corps = d.split(" : ", 1); frags = [(sec + " : ", x) for x in corps.split(" ; ")]
        else: frags = [("", d)]
        for sec, frag in frags:
            if frag.startswith("plafond"): continue
            nom = re.sub(r"\s*[+−-]\d.*$", "", frag)
            nom = re.sub(r" \d+ :.*$", "", nom).strip()        # « seuil de vie 32 : −20 % » → « seuil de vie »
            nom = re.sub(r"Composante [\d.]+ po", "Composante N po", nom)
            out.add(sec + nom + "§" + frag)
    return out


def source(f):
    d = f["dnd"]
    return ("er" if d.startswith("Elden Ring") else "pf2r" if d.startswith("Pathfinder 2 (version") else "pf2" if d.startswith("Pathfinder 2")
            else "pf1" if d.startswith("Pathfinder 1") else "3.5" if "D&amp;D 3.5" in d else "5.2" if "2024" in d else "5.1")


def jv(x):
    """une valeur sous une forme qu'on peut comparer et écrire (les tuples de symboles en listes)"""
    return json.loads(json.dumps(x, ensure_ascii=False, default=repr))


def cle_cercle(r):
    sats = tuple(json.dumps(jv([s[0], s[1], s[2] if len(s) > 2 else None, dict(sorted((s[3] if len(s) > 3 and s[3] else {}).items()))]),
                            ensure_ascii=False) for s in (r[4] if len(r) > 4 and r[4] else []))
    return (r[0], json.dumps(jv(r[1]), ensure_ascii=False), tuple(r[2]), sats)


def noyau(f):
    v = f["verb"]
    parts = v.split(" · ")
    if f["fam"] == "H" or f.get("combinee"):
        comb = parts[2] if len(parts) > 2 else None
        n = dict(famille="formes combinées" if f.get("combinee") else "hybride", ecole=parts[0], hemisphere=parts[1] if len(parts) > 1 else None,
                 combinaison=comb, pole=list(f["poles_impacts"]) if f.get("poles_impacts") else None)
        if f.get("combinee"): n["noyaux"] = [x["combinaison"] for x in f["combinee"]["noyaux"]]
    else:
        n = dict(famille="art rare" if f["fam"] == "R" else "Arcane", verbe=v, ecole=f.get("ecole"), pole="ténébreux" if f.get("pol") == "down" else "lumineux")
    return n


def cle_noyau(f):
    return json.dumps([f["fam"], f["verb"], jv(f["core"]), jv(f.get("poles_impacts")), bool(f.get("combinee"))], ensure_ascii=False)


# ---------------------------------------------------------------- relevé des formes
formes, cercles, lectures = [], {}, collections.defaultdict(set)
usage = collections.defaultdict(list)          # clé de cercle -> [(index de forme)]
bar = collections.defaultdict(lambda: dict(prix=[], delta=[], regles=collections.Counter(), sans=collections.Counter()))
ecart_interaction = collections.Counter()
for cle, fi in FICHES.items():
    for f in K.appliquer(cle, C.build_forms(cle, fi)):
        if K.est_elden_ring(f): continue
        src = source(f)
        inter = next((r[1] for r in f["rings"] if r[0] == "INTERACTION"), None)
        niv = int(f["level"])
        if isinstance(inter, int): ecart_interaction[(SYSTEME[src], inter - niv)] += 1
        idx = len(formes)
        cs = [cle_cercle(r) for r in f["rings"] if r[0] != "INTERACTION"]
        formes.append(dict(cle=cle, sort=f["fr"], jeu=JEU[src], systeme=SYSTEME[src], forme=f["label"], niveau=niv, interaction=inter,
                           noyau=noyau(f), _noyau=cle_noyau(f), _cercles=cs))
        for r, k in zip([r for r in f["rings"] if r[0] != "INTERACTION"], cs):
            usage[k].append(idx); lectures[k].add(r[3])
        if B is None: continue
        plein = B.cout(f)
        for i, r in enumerate(f["rings"]):
            if r[0] == "INTERACTION": continue
            k = cle_cercle(r); b = bar[k]
            if plein is None:
                b["sans"]["forme sans cercle d'Impact : pas de coût"] += 1; continue
            if r[0] == "IMPACT":
                p, sorte, regle, *_ = B.prix_impact(r)
                b["prix"].append(round(p, 2)); b["regles"][NOM_SORTE.get(sorte, sorte)] += 1
            sans = B.cout(dict(f, rings=[x for j, x in enumerate(f["rings"]) if j != i]))
            if sans is None:
                b["sans"]["seul cercle d'Impact : la forme n'a plus de coût sans lui"] += 1; continue
            b["delta"].append(round(plein["cout"] - sans["cout"], 2))
            if r[0] != "IMPACT":            # les règles de ce cercle : celles qui disparaissent ou changent quand on le retire
                for nom in fragments(plein["detail"]) - fragments(sans["detail"]):
                    b["regles"][nom.split("§")[0]] += 1

# ---------------------------------------------------------------- identifiants
def tri(k):
    t, v, ws, sats = k
    vv = json.loads(v)
    return (ORDRE.index(t) if t in ORDRE else 99, 0 if isinstance(vv, (int, float)) else 1 if vv == "plein" else 2,
            vv if isinstance(vv, (int, float)) else 0, str(vv), ws, sats)
ids = {k: f"C{i + 1:05d}" for i, k in enumerate(sorted(usage, key=tri))}


def resume(xs):
    if not xs: return None
    c = collections.Counter(xs)
    return dict(min=min(xs), max=max(xs), courant=c.most_common(1)[0][0], n=len(xs))


rep = []
for k in sorted(usage, key=tri):
    t, v, ws, sats = k
    fs = [formes[i] for i in sorted(set(usage[k]))]
    par = {}
    for s in SYSTEMES:
        g = [x for x in fs if x["systeme"] == s]
        if not g: continue
        nivs = collections.Counter(x["niveau"] for x in g)
        ex, vus = [], set()
        for x in g:
            if x["cle"] in vus: continue
            vus.add(x["cle"]); ex.append(dict(sort=x["sort"], jeu=x["jeu"], forme=x["forme"], niveau=x["niveau"]))
            if len(ex) == 5: break
        par[s] = dict(formes=len(g), sorts=len({x["cle"] for x in g}), niveaux={str(n): c for n, c in sorted(nivs.items())},
                      niveau_du_milieu=statistics.median([x["niveau"] for x in g]), exemples=ex)
    nu = (t, v, (), ())
    sans_sat = (t, v, ws, ())
    e = dict(id=ids[k], type=t, valeur=json.loads(v), mots=list(ws), satellites=[json.loads(s) for s in sats],
             lectures=sorted(lectures[k]), nu=ids.get(nu) if nu != k else None, sans_satellites=ids.get(sans_sat) if (sats and sans_sat != k) else None,
             systemes=par)
    if B is not None:
        b = bar[k]
        if t == "COSMETIQUE": e["bareme"] = dict(isolable=False, raison="le barème ne lit pas la Cosmétique")
        else:
            e["bareme"] = dict(isolable=bool(b["delta"] or b["prix"]), prix=resume(b["prix"]) if t == "IMPACT" else None, apport=resume(b["delta"]),
                               regles=dict(b["regles"].most_common()), non_isole=dict(b["sans"]))
    rep.append(e)

# ---------------------------------------------------------------- paires
groupes = collections.defaultdict(dict)        # (noyau, multiset sans un cercle) -> {forme: cercle retiré ou None}
for i, x in enumerate(formes):
    ms = sorted(ids[k] for k in x["_cercles"])
    groupes[(x["_noyau"], tuple(ms))][i] = None
    for j in set(range(len(ms))):
        reste = tuple(ms[:j] + ms[j + 1:])
        groupes[(x["_noyau"], reste)].setdefault(i, ms[j])
paires, hors, jumelles = [], [], 0
def categorie(a, b):
    if a["systeme"] != b["systeme"]: return "entre systèmes"
    if a["cle"] == b["cle"] and a["jeu"] == b["jeu"]: return "a"
    if a["cle"] == b["cle"]: return "b"
    return "c"
for (nk, reste), ent in groupes.items():
    it = sorted(ent.items())
    for (i, x), (j, y) in itertools.combinations(it, 2):
        if x == y:
            if x is None: jumelles += 1
            continue
        if x is None and y is None: continue
        a, b = formes[i], formes[j]
        cat = categorie(a, b)
        p = dict(categorie=cat, a=i, b=j, cercle_a=x, cercle_b=y, ecart_niveau=b["niveau"] - a["niveau"])
        (hors if cat == "entre systèmes" else paires).append(p)
# paires qui ne diffèrent que par le Noyau
par_ms = collections.defaultdict(list)
for i, x in enumerate(formes): par_ms[tuple(sorted(ids[k] for k in x["_cercles"]))].append(i)
noyau_seul = []
for ms, lst in par_ms.items():
    for i, j in itertools.combinations(lst, 2):
        a, b = formes[i], formes[j]
        if a["_noyau"] == b["_noyau"] or a["systeme"] != b["systeme"]: continue
        noyau_seul.append(dict(categorie=categorie(a, b), a=i, b=j, noyau_a=a["noyau"], noyau_b=b["noyau"], ecart_niveau=b["niveau"] - a["niveau"]))

# ---------------------------------------------------------------- écritures
F = [{k: v for k, v in x.items() if not k.startswith("_")} for x in formes]
json.dump(dict(_lisez_moi="Répertoire des cercles de la bibliothèque (hors Elden Ring), relevé sur main (33016e2). Un cercle = type, valeur, mots "
                          "dans l'ordre, satellites (position, valeur, texte, options) ; le cercle d'Interaction (le niveau) est exclu. "
                          "nu : le même type et la même valeur sans mot ni satellite ; sans_satellites : le même cercle sans ses satellites. "
                          "systemes : par système (D&D 5 = 5e et 2024 ; 3.5 ; PF1 ; PF2 = les deux éditions), formes, sorts, niveaux, "
                          "niveau du milieu (médiane), exemples. bareme : ce que donne le barème de la branche bareme (8ce0a16), version "
                          "actuelle : prix (cercles d'Impact : prix propre du cercle), apport (coût de la forme moins le coût de la même forme "
                          "sans ce cercle), règles appliquées ; non_isole : les formes où l'apport ne peut pas se mesurer.", cercles=rep),
          open(os.path.join(OUT, "repertoire_cercles.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(dict(_lisez_moi="Paires de formes : même Noyau, mêmes cercles sauf un (cercle_a dans la forme a, cercle_b dans la forme b ; null : "
                          "absent). Catégories : a = même sort, même jeu ; b = même sort, deux jeux du même système (5e et 2024 ; PF2 d'origine et "
                          "remaniée) ; c = sorts différents du même système. ecart_niveau = niveau de b − niveau de a. paires_noyau : mêmes "
                          "cercles, Noyau différent (même système). entre_systemes : pour information seulement. Les formes sont données par "
                          "leur index dans « formes ».", formes=F, paires=paires, paires_noyau=noyau_seul, entre_systemes=hors),
          open(os.path.join(OUT, "paires_cercles.json"), "w", encoding="utf-8"), ensure_ascii=False)
import csv
with open(os.path.join(OUT, "repertoire_cercles.csv"), "w", encoding="utf-8-sig", newline="") as fh:
    w = csv.writer(fh, delimiter=";")
    w.writerow(["identifiant", "type", "valeur", "mots", "satellites", "phrase", "cercle nu"] + [f"formes {s}" for s in SYSTEMES]
               + [f"niveau du milieu {s}" for s in SYSTEMES] + ["barème actuel"])
    for e in rep:
        sats = " | ".join(f"{s[0]}:{s[1]}{(' ' + s[2]) if s[2] else ''}" for s in e["satellites"])
        ph = e["lectures"][0] + (f" (+{len(e['lectures']) - 1} variantes)" if len(e["lectures"]) > 1 else "")
        b = e.get("bareme") or {}
        if not b: bt = ""
        elif not b.get("isolable"): bt = b.get("raison") or "non isolable : " + "; ".join(b.get("non_isole", {}))
        else:
            parts = []
            if b.get("prix"): parts.append(f"prix {b['prix']['min']} à {b['prix']['max']} (courant {b['prix']['courant']})")
            if b.get("apport"): parts.append(f"apport {b['apport']['min']} à {b['apport']['max']} (courant {b['apport']['courant']})")
            if b.get("regles"): parts.append("règle : " + next(iter(b["regles"])))
            bt = " ; ".join(parts)
        w.writerow([e["id"], e["type"], e["valeur"], " ".join(e["mots"]), sats, ph, e["nu"] or ""]
                   + [e["systemes"].get(s, {}).get("formes", 0) for s in SYSTEMES]
                   + [e["systemes"].get(s, {}).get("niveau_du_milieu", "") for s in SYSTEMES] + [bt])
# comptes pour le bilan
types = collections.Counter(e["type"] for e in rep)
nsys = collections.defaultdict(collections.Counter)
for e in rep: nsys[e["type"]][len(e["systemes"])] += 1
sans_dnd = collections.Counter(e["type"] for e in rep if "D&D 5" not in e["systemes"])
pc = collections.Counter(); pt = collections.Counter()
avec_paire = set()
for p in paires:
    pc[p["categorie"]] += 1
    for c in (p["cercle_a"], p["cercle_b"]):
        if c: avec_paire.add(c)
    t = rep[int((p["cercle_a"] or p["cercle_b"])[1:]) - 1]["type"]
    pt[(p["categorie"], t)] += 1
sans_paire = [e["id"] for e in rep if e["id"] not in avec_paire]
json.dump(dict(cercles=len(rep), formes=len(formes), types=dict(types), systemes_par_type={t: dict(v) for t, v in nsys.items()}, sans_dnd=dict(sans_dnd),
               paires=dict(pc), paires_par_type={f"{a}|{t}": n for (a, t), n in pt.items()}, entre_systemes=len(hors), noyau_seul=len(noyau_seul),
               noyau_seul_cat=dict(collections.Counter(p["categorie"] for p in noyau_seul)), jumelles=jumelles,
               sans_paire=len(sans_paire), sans_paire_par_type=dict(collections.Counter(rep[int(i[1:]) - 1]["type"] for i in sans_paire)),
               sans_paire_ids=sans_paire, ecart_interaction={f"{s}|{d}": n for (s, d), n in ecart_interaction.items()}),
          open(os.path.join(OUT, "repertoire_comptes.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("formes", len(formes), "| cercles", len(rep), "| paires", dict(pc), "| entre systèmes", len(hors), "| Noyau seul", len(noyau_seul), "| sans paire", len(sans_paire))
