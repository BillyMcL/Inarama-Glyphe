"""Mots de forme : une géométrie ne s'écrit pas en mot, elle s'inscrit par le cercle Forme (arcane §6.2).
Table des mots retirés des annotations, de la primitive qui les remplace, et des pages où le mot dit une chose
et non une forme (là, il reste un mot). Décisions de Baptiste, 15 novembre 2026."""
A = lambda n: ("angle", n)           # courbure, ouverture : neuf unités par quart de tour ; 36 = tour complet (plein)
# primitive : (silhouette, proportions, nom lu, famille)
PRIM = {
 "ligne": (1, [1], "ligne"),
 "plan": (2, [1], "plan"),
 "cylindre": (9, [1, 1], "cylindre"),
 "sphere": ("plein", [1], "sphère"),
 "coquille": ("plein", [1, A(36)], "calotte fermée (coquille)"),
 "dome": ("plein", [1, A(18)], "calotte d'un demi-tour (dôme)"),
 "disque": (9, [1], "disque"),
 "anneau": (2, [1, 1, A(36)], "paroi courbe fermée (anneau)"),
 "cube": (4, [1], "cube"),
 "helice": (1, [1, A(36), 1], "hélice"),
 "cone": (3, [2, 1], "cône (hauteur 2, rayon 1)"),
 "prisme": (5, [1, 1], "prisme pentagonal : un éclat, un fragment"),
}
SATELLITE = {"prisme"}               # forme de la chose lancée, non de la zone : toujours en satellite de Forme de son cercle
# mot -> (primitive, pages où il est une forme [None = toutes], pages où il reste une chose)
GEO = {
 "MUR": ("plan", None, {"slick-walls", "phantom-prison", "guards-and-wards"}),
 "RIDEAU": ("plan", None, set()),
 "NAPPE": ("plan", None, set()),
 "RAYON": ("ligne", None, set()),
 "LIGNE": ("ligne", None, set()),
 "JET": ("ligne", None, {"fire-seeds"}),                       # le jet d'un gland : lancer, non tracer
 # « trait » : forme pour un trait d'énergie ; chose pour une flèche, une munition, un attribut de bête
 "TRAIT": ("ligne", {"gloomblind-bolts", "divine-lance", "phase-bolt", "force-bolt", "er-frenzied-burst", "moonrise-arrow", "inner-radiance-torrent"}, set()),
 "COLONNE": ("cylindre", None, set()),
 "PILIER": ("cylindre", {"rising-water"}, set()),
 "SPHERE": ("sphere", None, set()),
 "GLOBE": ("sphere", None, set()),
 "BOULE": ("sphere", None, {"fold-metal"}),
 "ORBE": ("sphere", None, set()),
 "EXPLOSION": ("sphere", None, set()),                          # sphère annotée « explosion » sur le cercle Forme
 "BULLE": ("coquille", {"personal-ocean"}, set()),
 "DOME": ("dome", None, set()),
 "CERCLE": ("disque", {"teleportation-circle", "unbreaking-wave-barrier"}, set()),
 "DISQUE": ("disque", {"healing-well"}, set()),
 "ANNEAU": ("anneau", None, set()),
 "CUBE": ("cube", None, set()),
 "SPIRALE": ("helice", None, set()),
 "VRILLE": ("helice", {"er-whirl-o-flame"}, set()),
 "GERBE": ("cone", None, set()),
 # « souffle » : cône quand c'est un souffle craché ; chose quand c'est l'haleine, le vent, la respiration
 "SOUFFLE": ("cone", {"fire-breath", "poison-breath", "elemental-breath", "dragon-breath", "er-glintstone-breath",
                      "vile-dog-transformation", "summon-draconic-legion"}, set()),
 # « éclat » : prisme quand c'est un fragment (verre, glace, pierre) ; le mot reste quand c'est une lueur vive
 "ECLAT": ("prisme", {"chord-of-shards", "etheric-shards", "pinecone-bomb", "shield-of-shards", "torrent-of-elemental-rage", "shattering-gem",
                      "reflective-scales", "elemental-confluence", "glass-sand", "frigid-flurry", "exploding-earth", "winter-bolt"}, set()),
 "TOURBILLON": ("tourbillon", None, set()),                     # cylindre + hélice : forme composée
 "TORNADE": ("tourbillon", None, set()),
 "CYCLONE": ("tourbillon", None, set()),
}
ANNOTE = {"EXPLOSION"}               # le mot reste, mais en annotation du cercle (ou du satellite) de Forme
# cas particuliers : (page, mot) -> primitive
CAS = {("cleansing-fire", "CERCLE"): "anneau"}
GEO["CERCLE"][1].add("cleansing-fire")
# tailles connues par la source : (page, mot) -> (valeur, [mots de l'Ampleur])
TAILLE = {
 ("vile-dog-transformation", "SOUFFLE"): (3, ["longueur", "mètres"]),
 ("deitys-strike", "LIGNE"): (9, ["longueur", "mètres"]),
 ("sliding-blocks", "CUBE"): (3, ["volume", "mètres", "cubes"]),          # six cubes de 1,5 m de côté : 3,4 m³ chacun
}
# quand la forme était le seul mot de l'Impact et que le glyphe hybride a besoin d'un mot d'action : le mot qui dit l'effet
REMPLACE = {("illusory-wall", "MUR"): "fantasme", ("wall-of-metal", "MUR"): "barrière"}
# « trait » n'a plus qu'un sens, l'attribut (d'une bête, d'un lieu). Une flèche s'écrit « flèche » ; ce qu'on lance sans arc, « projectile ».
TRAIT_ATTRIBUT = {"animal-feature", "create-demiplane-lesser"}
TRAIT_PROJECTILE = {"hedging-weapons", "sickening-entanglement"}
def trait(page):
    """mot qui remplace « trait » sur cette page, ou None s'il reste (attribut) ou devient une ligne (trait d'énergie)"""
    if page in TRAIT_ATTRIBUT or page in (GEO["TRAIT"][1] or ()): return None
    return "projectile" if page in TRAIT_PROJECTILE else "flèche"
def forme_de(page, mot):
    """primitive que ce mot inscrit sur cette page, ou None s'il y reste un mot"""
    g = GEO.get(mot)
    if not g: return None
    prim, seules, sauf = g
    if page in sauf or (seules is not None and page not in seules): return None
    return CAS.get((page, mot), prim)
