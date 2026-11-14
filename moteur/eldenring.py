"""Elden Ring (FromSoftware, Bandai Namco) : lecture du relevé des sorts et mise au format interne du moteur.

Elden Ring n'a ni niveaux de sort, ni dés, ni portées chiffrées : ses grandeurs ne se laissent pas reporter telles quelles.
Le relevé donnees/eldenring/sorts-eldenring.json est donc un relevé propre à la bibliothèque. Il ne contient aucun texte du jeu :
pour chaque sort, son nom d'origine, sa famille (sorcellerie ou incantation), son origine (jeu de base ou extension), et ce que
la transposition a retenu : un niveau équivalent de 0 à 9 (le rang du sort parmi ceux du jeu), une école, une classe de portée
(contact, 9 m, 18 m, 36 m, 72 m) et la durée en secondes quand le jeu en donne une. L'Impact se règle dans les fiches, par
comparaison avec les sorts déjà inscrits. Tous les sorts gardent la Condition « parole », par adaptation à Inarama.
"""
import json

def load(path):
    out = {}
    for x in json.load(open(path, encoding="utf-8")):
        rec = dict(index=x["index"], name=x["name"], level=x["level"], school={"name": x["school"]}, casting_time="1 action",
                   range=x["range"], duration=x["duration"], concentration=x["duration"] == "Concentration", ritual=False,
                   material=None, desc=[""], _ed="er", _cl=None, _xp=None,
                   _kind="sorcellerie" if x["kind"] == "S" else "incantation",
                   _origine="extension Shadow of the Erdtree" if x.get("dlc") else "jeu de base")
        if x.get("dtype"): rec["damage"] = {"damage_type": {"name": x["dtype"]}}
        out[x["index"]] = rec
    return out
