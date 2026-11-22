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


def arrondir(f, er=False):
    """la forme avec ses nombres longs arrondis (cercles et satellites) ; rien d'autre ne change"""
    if er: return f
    rings, chg = [], False
    for r in f["rings"]:
        v, rd = r[1], r[3]
        if isinstance(v, int) and not isinstance(v, bool) and nformes(v) > MAX_FORMES:
            n = TABLE[v]
            rd = _phrase_cercle(rd, v, n); FAITS.append((f.get("idx"), f["label"], r[0], False, v, n)); v = n; chg = True
        sats = list(r[4]) if len(r) > 4 and r[4] else []
        for j, s in enumerate(sats):
            sv = s[1]
            if isinstance(sv, int) and not isinstance(sv, bool) and nformes(sv) > MAX_FORMES:
                n = TABLE[sv]
                if n in FORMES: n = Produit(n, FORMES[n])
                rd = _phrase_sat(rd, sv, n); FAITS.append((f.get("idx"), f["label"], r[0], True, sv, n))
                sats[j] = (s[0], n, *s[2:]); chg = True
        rings.append((r[0], v, r[2], rd, sats, *r[5:]) if len(r) > 4 else (r[0], v, r[2], rd))
    if not chg: return f
    svg, rows = SP.build(f["core"], f["pol"], rings, f["r0"], f["split"], officiants=f["officiants"], impacts=f.get("poles_impacts"))
    return dict(f, rings=rings, svg=svg, rows=rows, bsplit=SP.PART[0])
