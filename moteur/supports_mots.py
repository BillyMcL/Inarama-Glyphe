"""Supports : ce sur quoi l'effet agit ne se dit pas dans l'Impact, mais dans la Cible (arcane §6.1).
Première tranche, décidée avec Baptiste le 15 novembre 2026 : les facultés et les parts de l'être.
Les choses et les êtres (arme, bête, pierre…) dépendent du verbe et de la page : ils ne sont pas traités ici."""
# facultés : support quand l'Impact les chiffre (un bonus, un malus) ou les donne en plein
FACULTES = {"APTITUDE", "ENDURANCE", "ADRESSE", "PRESTANCE", "RAISON", "LUCIDITE", "VOLONTE", "GARDE", "RESISTANCE", "COUP", "FRAPPE"}
# « force » : la faculté sur ces pages seulement ; ailleurs c'est l'énergie de force (mur de force, coup de force)
FORCE = {"enhance-ability", "death-knell", "enticing-adulation", "enemys-heart", "song-of-strength", "psychic-leech", "hallow"}
# parts de l'être
PARTS = {"AME", "PSYCHE", "CORPS", "MEMBRE", "MEMBRES", "VISAGE", "CŒUR", "PEAU", "VITAL", "MEMOIRE", "BRAS"}
# pages où le mot dit ce que le sort produit ou fait, non ce qu'il touche : il reste dans l'Impact
SAUF = {
 "GARDE": {"hallow", "cape-of-wasps", "ravenous-portal"},
 "FRAPPE": {"spiritual-guardian"},
 "COUP": {"symbol-of-striking", "bladed-dash", "tail-strike"},
 "CORPS": {"reincarnate", "true-resurrection", "false-resurrection", "reincarnate-spy", "cyclic-reincarnation", "recorporeal-incarnation"},
 "MEMBRE": {"threefold-limb", "carrion-mire"},
 "AME": {"sealed-life"},
 "MEMOIRE": {"shadow-spy"},
 "APTITUDE": {"recorporeal-incarnation"},
}
SEULES = {"BRAS": {"straitjacket", "shielded-arm"}}
# Seconde tranche : choses et êtres. Le mot n'est un support que sur ces pages, où il nomme ce que l'effet touche
# (l'arme qu'on affûte, la bête qu'on dresse, l'objet qu'on déplace). Partout ailleurs il dit ce que le sort produit,
# la forme qu'il donne, ce qu'il révèle ou l'instrument dont il se sert, et il reste dans l'Impact. Tri page par page.
CHOSES = {
 "adroit-retrieval": {'OBJET'},
 "alchemical-allocation": {'POTION'},
 "align-weapon": {'ARME'},
 "alpha-instinct": {'BETE'},
 "amplify-elixir": {'POTION'},
 "animal-purpose-training": {'BETE'},
 "anthropomorphic-animal": {'BETE'},
 "apport-object": {'OBJET'},
 "arodens-magic-army": {'ARME'},
 "artistic-flourish": {'OUVRAGE'},
 "atavism": {'BETE'},
 "augment-summoning": {'INVOQUE'},
 "aura-of-inviolate-ownership": {'OBJET'},
 "authenticating-gaze": {'ECRIT'},
 "badgers-ferocity": {'ARME'},
 "bite-the-hand": {'INVOQUE'},
 "blade-lash": {'ARME'},
 "blade-of-light": {'ARME'},
 "blade-snare": {'ARME'},
 "brittle-portal": {'OBJET'},
 "call-animal": {'BETE'},
 "call-weapon": {'ARME'},
 "clear-grove": {'PLANTE'},
 "companion-mind-link": {'BETE'},
 "control-summoned-creature": {'INVOQUE'},
 "crafters-fortune": {'OUVRAGE'},
 "daywalker": {'MORTVIVANT'},
 "defoliate": {'PLANTE'},
 "detect-psychic-significance": {'OBJET'},
 "efficient-apport": {'OBJET'},
 "effortless-armor": {'ARMURE'},
 "er-bloodflame-blade": {'ARME'},
 "er-electrify-armament": {'ARME'},
 "er-poison-armament": {'ARME'},
 "er-vykes-dragonbolt": {'ARME'},
 "eroding-ray": {'OBJET'},
 "final-sacrifice": {'INVOQUE'},
 "firebrand": {'ARME'},
 "forest-friend": {'PLANTE'},
 "guardian-armor": {'ARMURE'},
 "hammer-of-mending": {'OBJET'},
 "heart-of-the-metal": {'ARME'},
 "hide-weapon": {'ARME'},
 "hollow-blades": {'ARME'},
 "know-the-enemy": {'CREATURE'},
 "lead-blades": {'ARME'},
 "lightfingers": {'OBJET'},
 "litany-of-defense": {'ARMURE'},
 "lock-item": {'OBJET'},
 "locksight": {'SERRURE'},
 "masters-mutation": {'INVOQUE'},
 "meticulous-match": {'OBJET'},
 "necromantic-burden": {'MORTVIVANT'},
 "necrostasis": {'MORTVIVANT'},
 "object-memory": {'OBJET'},
 "peacebond": {'ARME'},
 "phantom-ship": {'EQUIPAGE'},
 "plant-voice": {'PLANTE'},
 "pup-shape": {'BETE'},
 "putrefy-food-and-drink": {'NOURRITURE'},
 "remarkable-legerdemain": {'OBJET'},
 "retrieve-item": {'OBJET'},
 "runic-impression": {'ARME'},
 "salvage": {'NAVIRE'},
 "sanctify-weapons": {'ARME'},
 "sea-steed": {'MONTURE'},
 "serrens-armor-lock": {'ARMURE'},
 "shambling-horror": {'CADAVRE'},
 "sky-steed": {'MONTURE'},
 "spirit-object": {'OBJET'},
 "stoke-the-inner-fire": {'ARME'},
 "summoner-conduit": {'INVOQUE'},
 "suns-fury": {'ARME'},
 "swipe": {'OBJET'},
 "telekinetic-volley": {'OBJET'},
 "thoughtful-gift": {'OBJET'},
 "touch-injection": {'POTION'},
 "track-ship": {'NAVIRE'},
 "trade-items": {'OBJET'},
 "transmute-golem": {'GOLEM'},
 "transmute-metal-to-wood": {'METAL'},
 "transmute-potion-to-poison": {'POTION'},
 "unbroken-panoply": {'ARME'},
 "weaken-earth": {'PIERRE'},
 "weapon-surge": {'ARME'},
 "weapons-against-evil": {'ARME'},
 "wilderness-soldiers": {'PLANTE'},
}
def support(page, mot):
    if mot in CHOSES.get(page, ()): return True
    if mot == "FORCE": return page in FORCE
    if mot not in FACULTES and mot not in PARTS: return False
    if page in SAUF.get(mot, ()): return False
    if mot in SEULES and page not in SEULES[mot]: return False
    return True
