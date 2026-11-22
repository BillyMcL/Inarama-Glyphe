# -*- coding: utf-8 -*-
"""Fautes des phrases de lecture (dernier lot du chantier d'écriture, décision du 22 novembre 2026).

Les phrases sont corrigées une fois produites, à la fin de la chaîne (corrections.appliquer), et non là où le moteur
les fabrique : les couches de correction (4a, 4b, B3 à B11) reconnaissent encore les phrases d'origine par leur texte
(« satellite symbole de le feu », parenthèses gardées), et les changer à la source les aurait désaccordées.
Seul le texte des phrases change : aucun cercle, aucun dessin."""
import re

L = r"A-Za-zÀ-ÖØ-öø-ÿŒœ"                      # lettres
AV = rf"(?<![{L}'’])"                           # début de mot
AP = rf"(?![{L}\-])"                            # fin de mot (un trait d'union prolonge le mot)

# a) deux phrases types du moteur
TYPES = [("symbole du feu", rf"{AV}de le feu{AP}", "du feu"),
         ("pièces d'or", rf"{AV}de or{AP}", "d'or")]

# d) une phrase de Bénédiction de chance et de résolution (avant les paires : « la courage » y devient « la peur »)
PHRASES = [("mieux armée contre la courage", "mieux armée contre la peur")]

# c) articles du mauvais genre laissés devant un mot qu'une règle a remplacé
PAIRES = [("une abri", "un abri"), ("une ancrage", "un ancrage"), ("un ans", "un an"), ("un jours", "un jour"),
          ("un aspiration", "une aspiration"), ("un barrière", "une barrière"), ("une bâton", "un bâton"),
          ("un chance", "une chance"), ("un malchance", "une malchance"), ("une choc", "un choc"),
          ("la courage", "le courage"), ("du direction", "de la direction"), ("un direction", "une direction"),
          ("la drain", "le drain"), ("la duel", "le duel"), ("une déplacement", "un déplacement"),
          ("un gloire", "une gloire"), ("une hasard", "un hasard"), ("la voile", "le voile"), ("le lance", "la lance"),
          ("une lien", "un lien"), ("du lumière", "de la lumière"), ("un maladie", "une maladie"),
          ("un marque", "une marque"), ("une monstre", "un monstre"), ("une mouvement", "un mouvement"),
          ("une mécanisme", "un mécanisme"), ("un nourriture", "une nourriture"), ("le nourriture", "la nourriture"),
          ("un odeur", "une odeur"), ("une partage", "un partage"), ("un porte", "une porte"),
          ("au précision", "à la précision"), ("une rempart", "un rempart"), ("le riposte", "la riposte"),
          ("une signal", "un signal"), ("ta sort", "ton sort"), ("la temps", "le temps"), ("le terre", "la terre"),
          ("le tête", "la tête"), ("une trou", "un trou"), ("une écrit", "un écrit"), ("sa essence", "son essence"),
          ("sous tous les direction", "sous toutes les directions")]

# b) élision : « la »/« le » devant une voyelle (aucun h muet relevé : haut, halo, hantise sont aspirés) ;
#    « l' » devant une consonne, selon le genre du mot
VOY = "aeiouyéèêëàâîïôûœæAEIOUYÉÈÊËÀÂÎÏÔÛŒÆ"
L_CONS = {"solidité": "la", "chance": "la", "peau": "la", "pouvoir": "le", "rangement": "le", "symbole": "le",
          "durcissement": "le"}

COMPTE = {}                                      # famille → nombre de phrases corrigées


def _maj(s, modele):
    return s[:1].upper() + s[1:] if modele[:1].isupper() else s


def corriger(t, compter=True):
    if not t: return t
    avant = t
    fam = {}
    for nom, motif, r in TYPES:
        t2 = re.sub(motif, r, t)
        if t2 != t: fam[nom] = 1; t = t2
    for a, b in PHRASES:
        if a in t: t = t.replace(a, b); fam["Bénédiction de chance et de résolution"] = 1
    for a, b in PAIRES:
        motif = AV + "(" + re.escape(a) + "|" + re.escape(a[:1].upper() + a[1:]) + ")" + AP
        t2 = re.sub(motif, lambda m: _maj(b, m.group(1)), t)
        if t2 != t: fam["articles du mauvais genre"] = 1; t = t2
    t2 = re.sub(AV + rf"([Ll][ae]) (?=[{VOY}][{L}])", lambda m: m.group(1)[0] + "'", t)    # (ni « à » ni « y » seuls)
    if t2 != t: fam["élision devant une voyelle"] = 1; t = t2
    t2 = re.sub(AV + r"([Ll])'(" + "|".join(L_CONS) + ")" + AP,
                lambda m: _maj(L_CONS[m.group(2)], m.group(1)) + " " + m.group(2), t)
    if t2 != t: fam["« l' » devant une consonne"] = 1; t = t2
    if compter and t != avant:
        for k in fam: COMPTE[k] = COMPTE.get(k, 0) + 1
    return t


def corriger_forme(f):
    """la forme avec ses phrases de lecture corrigées (lignes de lecture : (numéro, critère, phrase))"""
    rows = f.get("rows")
    if not rows: return f
    nr = [(n, c, corriger(l)) for n, c, l in rows]
    return f if nr == [tuple(r) for r in rows] else dict(f, rows=nr)
