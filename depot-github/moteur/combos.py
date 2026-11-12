"""Les 35 combinaisons (magie/alchimie.md) : nom -> (Feu, Air, Terre, Eau)"""
COMBOS = {
 "Feu": (4,0,0,0), "Éclair": (3,1,0,0), "Magnétisme": (3,0,1,0), "Vapeur ardente": (3,0,0,1), "Foudre": (2,2,0,0),
 "Verre": (2,1,1,0), "Orage": (2,1,0,1), "Obsidienne": (2,0,2,0), "Bronze": (2,0,1,1), "Geyser": (2,0,0,2),
 "Plasma": (1,3,0,0), "Fumée noire": (1,2,1,0), "Ammoniac": (1,2,0,1), "Acier": (1,1,2,0), "Énergie pure": (1,1,1,1),
 "Acide sulfurique": (1,1,0,2), "Lave": (1,0,3,0), "Sel gemme": (1,0,2,1), "Sang": (1,0,1,2), "Eau thermale": (1,0,0,3),
 "Air": (0,4,0,0), "Poussière": (0,3,1,0), "Brume": (0,3,0,1), "Sable": (0,2,2,0), "Pollen": (0,2,1,1),
 "Tempête": (0,2,0,2), "Roche": (0,1,3,0), "Bois": (0,1,2,1), "Glace": (0,1,1,2), "Chlore gazeux": (0,1,0,3),
 "Terre": (0,0,4,0), "Boue": (0,0,3,1), "Plante": (0,0,2,2), "Mercure": (0,0,1,3), "Eau": (0,0,0,4),
}
def code(c):
    f, a, t, e = COMBOS[c]
    return " ".join(f"{n}{l}" for n, l in ((f, "F"), (a, "A"), (t, "T"), (e, "E")) if n)
# école D&D -> (école d'Inarama, hémisphère, combinaison par défaut)
ECOLES = {
 "Abjuration": ("Abjuration", "H", "Acier"), "Divination": ("Divination", "H", "Verre"),
 "Illusion": ("Illusion", "H", "Plasma"), "Conjuration": ("Invocation", "H", "Air"),
 "Enchantment": ("Enchantement", "G", "Pollen"), "Transmutation": ("Transmutation", "G", "Roche"),
 "Evocation": ("Évocation", "G", "Éclair"), "Necromancy": ("Nécromancie", "G", "Sang"),
}
# type de dégâts élémentaire -> combinaison (règle : un élément en jeu appelle la Magie hybride)
DAMAGE_COMBO = {"Fire": "Feu", "Cold": "Glace", "Lightning": "Foudre", "Thunder": "Orage", "Acid": "Acide sulfurique", "Poison": "Ammoniac"}
MEDIUM = {"Fire": "FEU", "Cold": "FROID", "Lightning": "FOUDRE", "Thunder": "TONNERRE", "Acid": "ACIDE", "Poison": "POISON",
          "Necrotic": "NECROSE", "Radiant": "LUMIERE", "Psychic": "ESPRIT", "Force": None,
          "Bludgeoning": "CHOC", "Piercing": "PERCE", "Slashing": "TAILLE"}
