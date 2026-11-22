# -*- coding: utf-8 -*-
"""Satellites longs (chantier « nombres », décision du 22 novembre 2026).

Un nombre qui ne s'écrit pas en produit (spells.val l'écrit alors en addition de 9, en plus de cinq formes) est arrondi au
produit le plus proche, écrit dans le même cercle, jamais avec plus de deux fois la même forme ; à égalité, vers le bas.
Ce sont surtout des durées « par niveau » multipliées par le niveau de lanceur minimum (srd35._duration : 11, 13 ou 17,
des nombres premiers). Le calcul des durées n'est pas touché : l'arrondi se fait en fin de chaîne (corrections.appliquer),
Elden Ring excepté. Le nombre arrondi s'écrit comme tous les nombres en produit du moteur (spells.val, spells.sat_label).
La phrase garde la valeur du jeu : « arrondi de 110 à 108 pour s'écrire 9 × 4 × 3 « fois » » (formule de corrections)."""
import itertools, re
import spells as SP

# table validée (valeur d'aujourd'hui → produit le plus proche)
TABLE = {255: 252, 170: 168, 130: 126, 110: 108, 102: 100, 91: 90, 85: 84, 78: 80, 66: 64, 59: 60}
# jamais plus de deux fois la même forme, pour tous les nombres (décision du 22 novembre 2026) : 64 s'écrit 4 · 4 · 2 · 2 et
# non 4 · 4 · 4 comme le ferait spells.best_factors. Limité aux satellites de la table : les cercles de main qui écrivent
# déjà 64 en 4 · 4 · 4 ne bougent pas ici.
FORMES = {64: [4, 4, 2, 2]}


class Produit(int):
    """un nombre qui porte ses formes (lues par spells.val)"""
    def __new__(cls, n, facteurs):
        o = int.__new__(cls, n); o.facteurs = list(facteurs); return o
    def __repr__(self): return f"{int(self)}({'·'.join(map(str, self.facteurs))})"
    def __str__(self): return str(int(self))
    def __format__(self, spec): return format(int(self), spec)
MAX_FORMES = 5
FAITS = []          # (cle, libellé, cercle, satellite ?, avant, après)


def nformes(n): return len(SP.val(n, "up")[0])


def facteurs(n):
    """les formes d'un produit (deux fois la même au plus), ou None"""
    for size in range(1, 6):
        for c in itertools.combinations_with_replacement([9, 7, 5, 4, 3, 2], size):
            p = 1
            for x in c: p *= x
            if p == n and max(c.count(y) for y in c) <= 2: return list(c)
    return None


def produit_proche(n):
    """la règle : le produit le plus proche ; à égalité, vers le bas"""
    for d in range(0, n):
        for m in (n - d, n + d):
            if m > 0 and facteurs(m) and nformes(m) <= MAX_FORMES: return m
    return n


for _a, _b in TABLE.items():          # la table et la règle disent la même chose
    assert produit_proche(_a) == _b, (_a, produit_proche(_a), _b)


def _fois(n): return " × ".join(str(x) for x in (getattr(n, "facteurs", None) or SP.best_factors(n)))


def _phrase_sat(rd, v, n):
    """la phrase du cercle : le nombre du satellite remplacé ; la valeur du jeu dite par l'arrondi"""
    dit = f", arrondi de {v} à {n} pour s'écrire {_fois(n)} « fois »"
    # « satellite Ampleur 255 « litres » », « satellite Durée 130 « ans » »
    m = re.search(rf"(satellite [^;«]*?){v}( « [^»]*»)?", rd)
    if m: return rd[:m.start()] + m.group(1) + str(n) + (m.group(2) or "") + dit + rd[m.end():]
    # « durée maximale : 110 minutes »
    m = re.search(rf"(durée maximale : ){v}( [^\s;,]+)", rd)
    if m: return rd[:m.start()] + m.group(1) + str(n) + m.group(2) + dit + rd[m.end():]
    raise ValueError(f"nombre {v} introuvable dans la phrase : {rd}")


def _phrase_cercle(rd, v, n):
    if not rd.startswith(f"{v} "): raise ValueError(f"nombre {v} introuvable au début de la phrase : {rd}")
    tete, sep, reste = rd.partition(" : ")
    tete = str(n) + tete[len(str(v)):]
    return tete + sep + reste + f" ; arrondi de {v} à {n} pour s'écrire en {nformes(n)} formes"


# ---------- répétitions : jamais plus de deux fois la même forme, pour tous les nombres (chantier « repetitions », ----------
# décision du 22 novembre 2026). Elden Ring compris, pour ce chantier seulement. Un nombre écrit avec trois fois la même
# forme ou plus prend son écriture conforme exacte s'il en a une (même avec une forme de plus) ; sinon il est arrondi au
# produit conforme le plus proche de sa VRAIE valeur (celle que la phrase dit dans « arrondi de X à Y » ; les prix de
# Composante, déjà en platine, n'en ont pas), à égalité vers le bas. La règle générale de découpage du moteur
# (spells.best_factors) ne change pas : un nombre porte ses formes quand ce découpage n'est pas conforme.
def conformes(n):
    """l'écriture conforme exacte d'un produit (5 formes au plus, deux fois la même au plus), la plus courte, ou None"""
    if n in SP.PRIM: return [n]
    if n == 6: return [3, 3]
    if n == 8: return [4, 4]
    for size in range(2, 6):
        for c in itertools.combinations_with_replacement([9, 7, 5, 4, 3, 2], size):
            p = 1
            for x in c: p *= x
            if p == n and max(c.count(y) for y in c) <= 2: return list(c)
    return None


def regle(n):
    for d in range(0, n):
        for m in (n - d, n + d):
            if m > 0 and conformes(m): return m


# (valeur écrite aujourd'hui, vraie valeur) → nouvelle valeur ; table validée, vérifiée contre la règle au chargement
REPET = {(3087, 3203): 3240, (3087, 3136): 3150, (3087, 3054): 3024, (5103, 5663): 5670, (5103, 5534): 5670, (5103, 4804): 4860,
         (3645, 3540): 3528, (2187, 2182): 2160, (2187, 2135): 2160, (2187, 2145): 2160, (1458, 1423): 1440, (1458, 1434): 1440,
         (1458, 1438): 1440, (1458, 1440): 1440, (1372, 1358): 1350, (1125, 1112): 1120, (875, 849): 840, (686, 692): 700,
         (375, 368): 360, (256, 255): 252, (128, 130): 126, (500, 500): 504, (250, 250): 252, (125, 125): 126}
ECRITURES = {3240: [9, 9, 5, 4, 2], 3150: [9, 7, 5, 5, 2], 3024: [9, 7, 4, 4, 3], 5670: [9, 9, 7, 5, 2], 4860: [9, 9, 5, 4, 3],
             3528: [9, 7, 7, 4, 2], 2160: [9, 5, 4, 4, 3], 1440: [9, 5, 4, 4, 2], 1350: [9, 5, 5, 3, 2], 1120: [7, 5, 4, 4, 2],
             840: [7, 5, 4, 3, 2], 700: [7, 5, 5, 4], 360: [9, 5, 4, 2], 252: [9, 7, 4], 126: [9, 7, 2], 504: [9, 7, 4, 2],
             64: [4, 4, 2, 2], 192: [4, 4, 3, 2, 2], 448: [7, 4, 4, 2, 2], 729: [9, 9, 3, 3]}
GARDE = (64, 192, 448, 729)                      # valeur gardée, seule l'écriture change
ADDITIONS = {29: [9, 9, 7, 4], 31: [9, 9, 7, 4, 2], 34: [9, 9, 7, 5, 4]}       # valeur gardée, addition conforme
for (_e, _v), _n in REPET.items():
    assert regle(_v) == _n and conformes(_n) == ECRITURES[_n], (_e, _v, _n)
for _g in GARDE: assert conformes(_g) == ECRITURES[_g], _g
for _a, _t in ADDITIONS.items(): assert sum(_t) == _a and len(_t) <= 5 and max(_t.count(x) for x in _t) <= 2
REPET_FAITS = []        # (cle, libellé, cercle, satellite ?, écrit, vraie, nouveau, écriture avant, écriture après)


class Somme(int):
    """un nombre écrit en addition qui porte ses formes (lues par spells.val)"""
    def __new__(cls, n, termes):
        o = int.__new__(cls, n); o.termes = list(termes); return o
    def __repr__(self): return f"{int(self)}({'+'.join(map(str, self.termes))})"
    def __str__(self): return str(int(self))
    def __format__(self, spec): return format(int(self), spec)


def ecriture(n):
    """les formes d'un nombre telles que le moteur les dessine : ('×' ou '+', [formes])"""
    if getattr(n, "termes", None): return "+", list(n.termes)
    if getattr(n, "facteurs", None): return "×", list(n.facteurs)
    if n in SP.PRIM: return "×", [n]
    if n == 6: return "×", [3, 3]
    if n == 8: return "×", [4, 4]
    f = SP.best_factors(n)
    if f: return "×", f
    t, r = [], n
    while r >= 9: t.append(9); r -= 9
    if r: t += {6: [3, 3], 8: [4, 4]}.get(r, [r])
    return "+", t


def fautif(n):
    if not isinstance(n, int) or isinstance(n, bool): return False
    _, fs = ecriture(n)
    return len(fs) > MAX_FORMES or max(fs.count(x) for x in fs) >= 3


def _porte(n):
    """le nombre conforme n, qui porte ses formes si le découpage du moteur ne les donne pas"""
    fs = ECRITURES[n]
    return n if SP.best_factors(n) == fs or (n in SP.PRIM and fs == [n]) else Produit(n, fs)


def _repet(v, rd, f, crit, sat):
    """(nouvelle valeur, nouvelle phrase) d'un nombre fautif"""
    if v in ADDITIONS: return Somme(v, ADDITIONS[v]), rd                    # même valeur : la phrase ne change pas
    m = re.search(rf"arrondi de (\d+) à {v} pour s'écrire en \d+ formes", rd)
    vraie = int(m.group(1)) if m else v
    if v in GARDE:
        n = Produit(v, ECRITURES[v])
        if m: rd = rd[:m.start()] + f"arrondi de {vraie} à {v} pour s'écrire en {len(ECRITURES[v])} formes" + rd[m.end():]
        return n, rd
    if (v, vraie) not in REPET: raise ValueError(f"nombre hors table : {v} (vraie valeur {vraie}) — {f['label']} — {crit}")
    n0 = REPET[(v, vraie)]; n = _porte(n0)
    dit = f"arrondi de {vraie} à {n0} pour s'écrire en {len(ECRITURES[n0])} formes"
    if m:
        if n0 == vraie:                                                     # l'écriture conforme est exacte : plus d'arrondi
            rd = re.sub(rf" ; arrondi de {vraie} à {v} pour s'écrire en \d+ formes", "", rd)
        else: rd = rd[:m.start()] + dit + rd[m.end():]
    else: rd = rd + " ; " + dit                                              # prix de Composante : la vraie valeur est dans la tête
    rd = re.sub(rf"\bintensité {v}\b", f"intensité {n0}", rd)               # un Impact dit la valeur écrite dans sa tête
    return n, rd


def arrondir(f, er=False):
    """la forme avec ses nombres longs arrondis (Elden Ring excepté) et ses répétitions corrigées (Elden Ring compris)"""
    rings, chg = [], False
    for r in f["rings"]:
        v, rd = r[1], r[3]
        sats = list(r[4]) if len(r) > 4 and r[4] else []
        if not er and isinstance(v, int) and not isinstance(v, bool) and nformes(v) > MAX_FORMES:
            n = TABLE[v]
            rd = _phrase_cercle(rd, v, n); FAITS.append((f.get("idx"), f["label"], r[0], False, v, n)); v = n; chg = True
        for j, s in enumerate(sats):
            sv = s[1]
            if not er and isinstance(sv, int) and not isinstance(sv, bool) and nformes(sv) > MAX_FORMES:
                n = TABLE[sv]
                if n in FORMES: n = Produit(n, FORMES[n])
                rd = _phrase_sat(rd, sv, n); FAITS.append((f.get("idx"), f["label"], r[0], True, sv, n))
                sats[j] = (s[0], n, *s[2:]); chg = True
        if fautif(v):
            av = ecriture(v); n, rd = _repet(v, rd, f, r[0], False)
            REPET_FAITS.append((f.get("idx"), f["label"], r[0], False, int(v), int(n), av, ecriture(n))); v = n; chg = True
        for j, s in enumerate(sats):
            if fautif(s[1]):
                av = ecriture(s[1]); n, rd = _repet(s[1], rd, f, r[0], True)
                REPET_FAITS.append((f.get("idx"), f["label"], r[0], True, int(s[1]), int(n), av, ecriture(n)))
                sats[j] = (s[0], n, *s[2:]); chg = True
        n, rd2 = _vraie(v, rd)
        if n is not None:
            VRAIES_FAITS.append((f.get("idx"), f["label"], r[0], int(v), int(n), ecriture(v), ecriture(n))); v, rd, chg = n, rd2, True
        rings.append((r[0], v, r[2], rd, sats, *r[5:]) if len(r) > 4 else (r[0], v, r[2], rd))
    if not chg: return f
    svg, rows = SP.build(f["core"], f["pol"], rings, f["r0"], f["split"], officiants=f["officiants"], impacts=f.get("poles_impacts"))
    return dict(f, rings=rings, svg=svg, rows=rows, bsplit=SP.PART[0])


# ---------- vraies valeurs : les arrondis faits avec la limite de 4 formes (chantier « vraies_valeurs », 22 novembre 2026) ----------
# Ces nombres étaient déjà conformes, mais arrondis avec la limite de 4 formes : on repart de la vraie valeur (« arrondi de X
# à Y ») et on prend le produit conforme le plus proche (5 formes au plus, deux fois la même au plus ; égalité vers le bas).
# Elden Ring compris, pour ce chantier seulement. (Les satellites « vie · répartir » 124 : corrections.GRANDS, 124 → 126.)
VRAIES = {(3969, 4189): 4050, (1764, 1853): 1890, (3969, 4168): 4050, (1575, 1527): 1512, (1764, 1812): 1800, (810, 800): 800,
          (1215, 1201): 1200, (2025, 2008): 2016}
ECRITURES.update({4050: [9, 9, 5, 5, 2], 1890: [9, 7, 5, 3, 2], 1512: [9, 7, 4, 3, 2], 1800: [9, 5, 5, 4, 2], 800: [5, 5, 4, 4, 2],
                  1200: [5, 5, 4, 4, 3], 2016: [9, 7, 4, 4, 2]})
for (_e, _v), _n in VRAIES.items():
    assert regle(_v) == _n and conformes(_n) == ECRITURES[_n], (_e, _v, _n)
VRAIES_FAITS = []       # (cle, libellé, cercle, écrit, nouveau, écriture avant, écriture après)


def _vraie(v, rd):
    """(nouvelle valeur, nouvelle phrase) d'un cercle arrondi avec la limite de 4 formes, ou (None, rd)"""
    if not isinstance(v, int) or isinstance(v, bool): return None, rd
    m = re.search(rf"arrondi de (\d+) à {int(v)} pour s'écrire en \d+ formes", rd)
    if not m or (int(v), int(m.group(1))) not in VRAIES: return None, rd
    vraie = int(m.group(1)); n0 = VRAIES[(int(v), vraie)]
    if n0 == vraie: rd = re.sub(rf" ; arrondi de {vraie} à {int(v)} pour s'écrire en \d+ formes", "", rd)     # écriture exacte
    else: rd = rd[:m.start()] + f"arrondi de {vraie} à {n0} pour s'écrire en {len(ECRITURES[n0])} formes" + rd[m.end():]
    return _porte(n0), rd
