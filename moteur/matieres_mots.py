# -*- coding: utf-8 -*-
"""Matières et apparences sorties du cercle d'Impact (relecture de novembre 2026, passe 2).

Dans l'Impact il ne reste que ce que le sort fait. La chaîne qui paralyse, la toile qui entrave, les ailes qui portent ne sont
pas l'effet : ce sont sa matière ou son apparence. Décision sort par sort, d'après le texte :
  cosm        le mot quitte l'Impact et rejoint la Cosmétique (ce que l'on voit)
  cosm_plus   mot ajouté à la Cosmétique sans avoir été dans l'Impact
  cible       le mot quitte l'Impact et précise la Cible (la part de l'être que le sort touche)
  cible_plus  mot ajouté à la Cible
  ote         le mot ne disait rien de plus : il disparaît
  rempl       {mot: [mots]} le vrai effet à la place de la matière (règle 3 : écrire ce que le sort fait)
  forme       une chose créée dont la silhouette compte (un fouet, une chaîne tendue) : satellite de Forme en ligne, annoté
  forme_cercle  le mot annote le cercle de Forme déjà inscrit (un pont)
  sat_cible, sat_cond  le mot devient un satellite Cible ou Condition de son cercle d'Impact
  sats        satellites typés ajoutés au cercle d'Impact retouché : (critère, valeur, [mots])
  sym         symboles d'éléments ajoutés au cercle d'Impact retouché
  plus        cercles d'Impact ajoutés à la suite : (valeur, [mots], [satellites typés])
"""
ARME = {"rempl": {"fouet": ["arme"]}, "forme": "fouet"}
TABLE = {
 # ailes
 "sky-steed": {"rempl": {"aile": ["vol"]}},
 "dragon-wings": {"cosm": ["aile"]},
 "angelic-wings": {"cosm": ["aile", "lumière"]},
 "shield-of-wings": {"cosm": ["aile"]},
 "shadow-dragon-aspect": {"cosm": ["aile", "gueule", "dragon"]},
 "angelic-aspect-lesser": {"cosm": ["aile"]},
 "wing-bounty": {"cible": ["aile"], "rempl": {"baie": ["nourriture"]}, "cosm_plus": ["baie"]},
 "wing-thorns": {"cible": ["aile"]},
 "wooden-wing-shield": {"rempl": {"aile": ["bouclier"]}, "cible_plus": ["aile"]},
 # chaînes
 "imprisonment": {"cosm": ["chaîne"]},
 "binding": {"cosm": ["chaîne"]},
 "chains-of-light": {"cosm": ["chaîne"]},
 "barbed-chains": {"cosm": ["chaîne"]},
 "incorporeal-chains": {"rempl": {"chaîne": ["entrave"]}, "cosm_plus": ["chaîne"]},
 "chain-of-perdition": {"rempl": {"chaîne": ["choc", "saisie", "entrave"]}, "forme": "chaîne"},
 "shadow-barbs": {"rempl": {"chaîne": ["arme"]}, "forme": "chaîne", "plus": [("plein", ["obscurité"], [])]},
 # fouets
 "river-whip": ARME, "lightning-lash": ARME, "whip-of-spiders": ARME, "hellmouth-lash": ARME, "silk-to-steel": ARME,
 "rock-whip": {**ARME, "ote": ["roche"], "sym": ["terre"]},
 "ghost-whip": {**ARME, "cosm": ["spectre"]},
 "tamers-lash": {"rempl": {"fouet": ["arme", "dressage"]}, "forme": "fouet", "sat_cible": ["bête"]},
 "spell-scourge": {"ote": ["fouet"]},
 "blade-lash": {"rempl": {"fouet": ["allonge"]}},
 "tangling-creepers": {"ote": ["fouet"], "cosm": ["liane"]},
 # gueules
 "blood-feast": {"cosm": ["gueule"]},
 "gluttons-jaws": {"cosm": ["gueule"]},
 # lianes
 "vinetrap": {"cosm": ["liane"]}, "tanglefoot": {"cosm": ["liane"]}, "tripvine": {"cosm": ["liane"]},
 "anchored-step": {"cosm": ["liane"]}, "grasping-vine": {"cosm": ["liane"]}, "vine-strike": {"cosm": ["liane"]},
 "murderous-vine": {"cosm": ["liane"]}, "jatembes-ire": {"cosm": ["liane"]},
 # masques
 "mask-of-terror": {"cosm": ["masque"]}, "sepulchral-mask": {"cosm": ["masque"]},
 # toiles
 "web": {"cosm": ["toile"]}, "phantasmal-web": {"cosm": ["toile"]}, "web-bolt": {"cosm": ["toile"]}, "web-shelter": {"cosm": ["toile"]},
 "web-cloud": {"cosm": ["toile"], "ote": ["nuage", "égarement"]},
 "guards-and-wards": {"rempl": {"toile": ["entrave"], "porte": ["verrou"]}},
 # voiles : « voile » est la chose que l'on voit ; ce qui estompe s'écrit « flou »
 "sudden-shift": {"rempl": {"voile": ["flou"]}},
 "isolation": {"ote": ["voile"]},
 "fey-glamour": {"rempl": {"voile": ["déguisement"]}},
 "hologram-cage": {"rempl": {"voile": ["dissimulation"]}, "cosm": ["lumière"]},
 "shroud-of-night": {"rempl": {"voile": ["pénombre"]}, "cosm": ["nuit"]},
 "tempest-form": {"rempl": {"voile": ["flou"]}},
 "spirit-veil": {"rempl": {"voile": ["flou"]}, "cosm": ["esprit"], "plus": [("plein", ["invisibilité"], [("CONDITION", "plein", ["mort-vivant"])])]},
 "mirecloak": {"ote": ["voile"], "sat_cond": ["pénombre"]},
 # réécritures (règle 3)
 "inscrutable-mask": {"rempl": {"ombre": ["mensonge", "intimidation"], "masque": ["discrétion"]}, "cosm_plus": ["masque", "ombre"]},
 "bridge-of-vines": {"rempl": {"pont": ["passage"]}, "cosm": ["liane"], "forme_cercle": "pont"},
 "crushing-ground": {"rempl": {"gueule": ["écrasement"]}, "plus": [("plein", ["lenteur"], [])]},
 "lashing-rope": {"ote": ["fouet", "croc-en-jambe"], "plus": [("plein", ["croc-en-jambe"], [])]},
 "natures-reprisal": {"ote": ["plante", "fouet"], "rempl": {"entrave": ["poison"]}, "cosm_plus": ["plante"], "plus": [("plein", ["entrave"], [])]},
 "limp-lash": {"rempl": {"fouet": ["faiblesse"]}, "ote": ["paralysie"], "sats": [("DUREE", 1, ["chaque", "instants"])], "plus": [("plein", ["paralysie"], [])]},
 "purifying-veil": {"ote": ["voile"], "sats": [("CONDITION", "plein", ["mort-vivant"])], "cosm_plus": ["voile"], "plus": [("plein", ["flou"], [])]},
 "downpour": {"rempl": {"pluie": ["rempart"]}, "ote": ["voile"], "cosm_plus": ["pluie"], "plus": [("plein", ["flou"], [])]},
 "threefold-limb": {"rempl": {"voile": ["flou"]}, "cible": ["membre"]},
}

# ---------- tranche 2 : épine, lame, manteau, ombre, racine, tentacule, rugissement, trombe ----------
# « épine » et « lame » restent des natures de blessure (comme croc, griffe, dard) : elles ne sortent que doublées ou tenues en main.
# L'ombre de quelqu'un (clouée, volée, animée) est ce que le sort touche : la Cible. L'ombre matière du sort s'écrit par le
# symbole ténébreux de l'énergie astrale, en satellite de l'Impact (décision de Baptiste).
CHAQUE = ("DUREE", 1, ["chaque", "instants"])
OMBRE_CIBLE = {"cible": ["ombre"]}
OMBRE_ASTRALE = {"ote": ["ombre"], "sym": ["tenebreux"]}
TABLE.update({
 "spike-growth": {"ote": ["perce"]}, "wall-of-thorns": {"ote": ["perce"]},
 "life-draining-roots": {"cosm": ["racine"]}, "bramble-bush": {"cosm": ["ronce"]}, "sickening-entanglement": {"cosm": ["plante"]},
 "thorn-javelin": {"rempl": {"javelot": ["arme"]}, "forme": "javelot"},
 "flame-blade": {"rempl": {"lame": ["arme"]}, "forme": "lame"}, "twilight-knife": {"rempl": {"lame": ["arme"]}, "forme": "lame"},
 "blade-barrier": {"ote": ["taille"]}, "astral-rain": {"cosm": ["pluie"]}, "beheading-buzz-saw": {"cosm": ["disque"]}, "sun-blade": {"ote": ["lame"]},
 "fires-friend": {"cosm": ["manteau"]}, "tempest-cloak": {"cosm": ["manteau"]}, "mantle-of-the-frozen-heart": {"cosm": ["manteau"]},
 "mantle-of-the-magma-heart": {"cosm": ["manteau"]}, "mantle-of-the-melting-heart": {"rempl": {"manteau": ["rempart"]}, "cosm_plus": ["manteau"]},
 "shadow-trap": OMBRE_CIBLE, "shadow-anchor": OMBRE_CIBLE, "dark-whispers": OMBRE_CIBLE, "mischievous-shadow": OMBRE_CIBLE,
 "masochistic-shadow": OMBRE_CIBLE, "baleful-shadow-transmutation": OMBRE_CIBLE, "darkvault": OMBRE_CIBLE,
 "steal-shadow": {"cible": ["ombre"], "sats": [CHAQUE]},
 "unspeakable-shadow": {"cible": ["ombre"], "cosm": ["monstre"]},
 "searching-shadows": OMBRE_ASTRALE, "cloak-of-shadows": OMBRE_ASTRALE, "shadow-endurance": OMBRE_ASTRALE, "shadow-transmutation": OMBRE_ASTRALE,
 "protective-penumbra": OMBRE_ASTRALE, "shifting-shadows": OMBRE_ASTRALE, "armor-of-darkness": OMBRE_ASTRALE, "shadow-enchantment": OMBRE_ASTRALE,
 "umbral-infusion": OMBRE_ASTRALE, "penumbra": OMBRE_ASTRALE, "cloak-of-shadow": OMBRE_ASTRALE, "malicious-shadow": OMBRE_ASTRALE,
 "motes-of-dusk-and-dawn": OMBRE_ASTRALE,
 "shadow-step": {"sat_cond": ["ombre"]}, "shadow-jump": {"sat_cond": ["ombre"]},
 "shadow-illusion": {"ote": ["ombre"], "sym": ["tenebreux"], "sats": [("CONDITION", "plein", ["pénombre"])]},
 "fungal-hyphae": {"sat_cible": ["racine"]}, "root-reading": {"cible": ["racine"]},
 "entwined-roots": {"cosm": ["racine"]}, "take-root": {"cosm": ["racine"]},
 "elemental-confluence": {"rempl": {"racine": ["entrave"]}},          # la forme Bois : des racines encombrent le sol
 "tentacular-limbs": {"cosm": ["tentacule"]}, "blood-tentacles": {"cosm": ["tentacule"]},
 "thundering-dominance": {"cosm": ["rugissement"]}, "roar-of-the-wyrm": {"cosm": ["rugissement"]},
 "deluge": {"cosm": ["trombe"]},
 # réécritures (règle 3)
 "shadowform": {"rempl": {"ombre": ["quasi-réel"]}, "sym": ["tenebreux"]},
 "shadow-projection": {"rempl": {"forme": ["animation"]}, "cible": ["ombre"]},
 "spotlight": {"rempl": {"ombre": ["extinction"]}},
 "gray-shadow": {"cible": ["ombre"], "rempl": {"agonie": ["poison"]}, "ote": ["service"], "plus": [("plein", ["service"], [("CONDITION", "plein", ["agonie"])])]},
 "consuming-darkness": {"ote": ["ombre", "entrave"], "sym": ["tenebreux"], "plus": [("plein", ["lenteur"], [])]},
 "darklight": {"ote": ["ombre", "obscurité"], "sym": ["tenebreux"], "plus": [("plein", ["obscurité"], [])]},
 "thorn-snare": {"ote": ["entrave", "collet"], "cosm_plus": ["collet"], "sats": [CHAQUE], "plus": [("plein", ["entrave"], [])]},
 "mantle-of-the-unwavering-heart": {"rempl": {"manteau": ["vie"]}, "cosm": ["sève"], "cosm_plus": ["manteau"], "sats": [CHAQUE]},
 "field-of-razors": {"ote": ["fil"], "cosm_plus": ["champ"], "plus": [("plein", ["entrave"], [])]},
 "grasping-tentacles": {"rempl": {"tentacule": ["gêne"], "leurre": ["larcin"]}, "cosm_plus": ["tentacule"]},
})
# « taille » ne dit plus que la grandeur : ce qui tranche s'écrit « tranchant »
TRANCHANT = {"rempl": {"taille": ["tranchant"]}}
for _p in ("er-beast-claw", "slashing-gust", "er-tibias-summons", "parchment-swarm", "conjure-animals-2024", "resistance-2024"):
    TABLE[_p] = {**TABLE.get(_p, {}), **TRANCHANT}

# ---------- les sorts d'ombre et leur face lumineuse (décision de Baptiste) ----------
# Cinq sorts reçoivent la réciproque (suite : fiche « reciproque ») ; « lum » dit ce qui change dans la face lumineuse.
# Cape d'ombre reste à une face ; Infusion d'ombre n'agit que sur les morts-vivants (exception de la règle) ;
# Ombre malveillante : c'est l'ombre de la cible, donc la Cible, sans face astrale.
TABLE["penumbra"] = {**OMBRE_ASTRALE, "lum": {"rempl": {"éblouissement": ["aveuglement"]}}}
TABLE["protective-penumbra"] = {**OMBRE_ASTRALE, "lum": {"rempl": {"lumière": ["obscurité"]}}}
TABLE["shifting-shadows"] = {**OMBRE_ASTRALE, "lum": {}}
TABLE["shadow-illusion"] = {**TABLE["shadow-illusion"], "lum": {"sats": [("CONDITION", "plein", ["lumière"])]}}
TABLE["darklight"] = {**TABLE["darklight"], "lum": {"plus": [("plein", ["lumière"], [])]}}
TABLE["malicious-shadow"] = OMBRE_CIBLE

# ---------- tranche 3 : arbre, plante, pierre, roche, eau, flamme, sang ----------
# Ce qu'on devient reste dans l'Impact (« pétrification » quand c'est subi). Ce que le sort traverse ou anime va en Cible.
# Un élément qui fait la matière de l'effet s'écrit par ses symboles, sauf dans un sort hybride dont le Noyau le porte déjà.
TERRE, FEU, EAU = ["terre"], ["feu"], ["eau"]
PLANTE, BOIS, SANG = ["terre", "terre", "eau", "eau"], ["air", "terre", "terre", "eau"], ["feu", "terre", "eau", "eau"]
TABLE.update({
 "flesh-to-stone": {"rempl": {"pierre": ["pétrification"]}},
 "calcific-touch": {"rempl": {"pierre": ["pétrification"]}},
 "carry-companion": {"rempl": {"pierre": ["pétrification"]}, "cible": ["compagnon"]},
 "tree-stride": {"sat_cible": ["arbre"]}, "transport-via-plants": {"sat_cible": ["plante"]}, "see-through-stone": {"sat_cible": ["pierre"]},
 "greensight": {"sat_cible": ["plante"]}, "blood-scent": {"sat_cible": ["sang"], "ote": ["odorat"]},
 "alter-river": {"cible": ["eau"]},
 "arboreal-hammer": {"rempl": {"branche": ["animation"]}, "cible": ["arbre"]},
 "siege-of-trees": {"rempl": {"arbre": ["animation"]}, "cible_plus": ["arbre"]},
 "raging-rubble": {"rempl": {"mouvement": ["animation"]}, "cible": ["roche"]},
 "stone-throwing": {"sat_cible": ["roche"]},
 "boil-blood": {"cible": ["sang"]},
 "call-the-blood": {"rempl": {"flot": ["drain"]}, "cible": ["sang"]},
 "vampiric-exsanguination": {"cible": ["sang"]},
 "bloody-claws": {"rempl": {"sang": ["saignement"]}, "cible": ["griffe"]},
 "illuminate": {"rempl": {"flamme": ["embrasement"]}, "cible": ["lampe"]},
 "engrave-memory": {"ote": ["pierre"]},
 "clashing-rocks": {"ote": ["roche"], "sym": TERRE}, "mighty-fist-of-the-earth": {"ote": ["roche"], "sym": TERRE},
 "conjure-deadfall": {"ote": ["roche"], "rempl": {"chute": ["écrasement"]}, "sym": TERRE},
 "cave-fangs": {"ote": ["roche"], "sym": TERRE},
 "stone-discus": {"ote": ["pierre", "disque"], "sym": TERRE, "forme_prim": "disque"},
 "upheaval": {"ote": ["roche"], "sym": TERRE},
 "elemental-toss": {"ote": ["pierre"]},
 "wildfire": {"cosm": ["cendre", "flamme"], "sym": FEU},
 "burning-blossoms": {"cosm": ["arbre", "pétale"]},
 "unblinking-flame-ignition": {"ote": ["flamme"], "sym": FEU},
 "blazing-armory": {"ote": ["flamme"]}, "volcanic-eruption": {"ote": ["pierre"]}, "geyser": {"ote": ["eau"]},
 "protector-tree": {"cosm": ["arbre"], "sym": BOIS},
 "avenging-wildwood": {"cosm": ["arbre"], "ote": ["branche"]},
 "wooden-fists": {"ote": ["arbre"]},
 "sturdy-tree-fort": {"rempl": {"fort": ["abri"]}, "ote": ["arbre"], "sym": BOIS, "cosm_plus": ["arbre"]},
 "climbing-beanstalk": {"ote": ["plante"], "sym": PLANTE}, "beanstalk": {"ote": ["plante"], "sym": PLANTE},
 "verdant-sprout": {"rempl": {"fruit": ["nourriture"]}, "ote": ["plante"], "sym": PLANTE},
 "arid-refuge": {"ote": ["pierre"], "sym": TERRE},
 "mages-crawl-space": {"rempl": {"poche": ["dissimulation"]}, "sat_cible": ["pierre"]},
 "sliding-blocks": {"ote": ["pierre"]},
 "soothing-spring": {"ote": ["source", "eau"], "sym": EAU},
 "flames-of-ego": {"cosm": ["flamme"]},
 "cleansing-flames": {"ote": ["flamme"], "sym": FEU},
 "cinder-gaze": {"sat_cible": ["flamme"]},
 "unblinking-flame-revelation": {"ote": ["flamme"], "sym": FEU},
 "unblinking-flame-emblem": {"ote": ["flamme"], "sym": FEU},
 "blood-in-the-water": {"cosm": ["sang"]}, "bloodsworn-retribution": {"cosm": ["sang"]}, "charnel-house": {"cosm": ["sang"]},
 "blood-mist": {"ote": ["sang"]},
 "waves-of-blood": {"ote": ["sang"], "sym": SANG},
 "moths-supper": {"ote": ["papillon", "sang"]},
 "natures-enmity": {"cosm": ["bête", "plante"], "ote": ["nature"]},
 "invisibility-bubble": {"sat_cond": ["eau"]},
 "lotus-walk": {"sat_cible": ["eau"], "cosm": ["lotus"]},
 # réécritures (règle 3)
 "grove-of-respite": {"rempl": {"source": ["abri"]}, "cosm": ["arbre"], "sym": EAU},
 "timber": {"rempl": {"chute": ["écrasement"]}, "cosm": ["arbre"]},
 "stone-call": {"ote": ["pierre", "pluie"], "sym": TERRE, "plus": [("plein", ["gêne"], [])]},
 "scatter-scree": {"ote": ["pierre", "gêne"], "plus": [("plein", ["gêne"], [])]},
 "pummeling-rubble": {"ote": ["pierre", "poussée"], "plus": [("plein", ["poussée"], [])]},
 "lifes-flowing-river": {"ote": ["eau", "lueur", "entrave"], "plus": [("plein", ["entrave"], [])]},
 "rejuvenating-flames": {"ote": ["flamme"], "sym": FEU, "plus": [(2, [], [("SYM", "feu", None)])]},
 "shroud-of-flame": {"seul": "flamme", "ote": ["flamme", "riposte"], "sats": [CHAQUE]},
 "flame-dancer": {"ote": ["flamme", "danse"], "plus": [("plein", ["intimidation"], [("CONDITION", "plein", ["danse"])])]},
 "unblinking-flame-aura": {"rempl": {"flamme": ["vie"]}, "ote": ["vigilance"], "cosm_plus": ["flamme"], "plus": [(2, ["vigilance"], [])]},
 "rainbow-fumarole": {"cosm": ["flamme", "fumée"], "sym": FEU},
 "brow-gasher": {"rempl": {"tête": ["aveuglement"]}, "cosm": ["sang"]},
 "scouring-sand": {"rempl": {"plante": ["destruction"]}, "ote": ["éblouissement"], "sats": [("CIBLE", None, ["plante"])], "plus": [("plein", ["éblouissement"], [])]},
})

# ---------- tranche 4a : arme, bête, esprit ----------
# Ce que le sort vise ou manie va en Cible ; ce qu'on devient ou qu'on crée reste ; les esprits qui font le travail sont ce
# que l'on voit du sort (Cosmétique).
ESPRIT = {"cosm": ["esprit"]}
TABLE.update({
 "bestow-weapon-proficiency": {"sat_cible": ["arme"]}, "sunder-breaker": {"sat_cible": ["arme"]}, "hand-of-the-apprentice": {"sat_cible": ["arme"]},
 "dancing-blade": {"sat_cible": ["arme"], "rempl": {"danse": ["animation"]}, "sats": [CHAQUE]},
 "arodens-spellsword": {"cible": ["arme"], "sat_cible": ["bâton"]}, "weaponwand": {"cible": ["arme"], "sat_cible": ["bâton"]},
 "peasant-armaments": {"cible": ["outil"]}, "refine-improvised-weapon": {"cible": ["outil"]},
 "enemy-hammer": {"ote": ["arme"]},
 "weapon-of-judgment": {"cosm": ["arme"]},
 "hedging-weapons": {"rempl": {"arme": ["rempart"]}},
 "extract-poison": {"rempl": {"retrait": ["transfert"]}, "sat_cible": ["arme"], "ote": ["huile"]},
 "implement-of-destruction": {"sat_cond": ["arme"]},
 "animal-ambassador": {"cible": ["bête"]}, "share-skin": {"cible": ["bête"]},
 "jungle-mind": {"sat_cible": ["bête"]},
 "stench-of-prey": {"sat_cible": ["bête"], "ajoute": ["attirance"]},
 "primal-chorus": {"rempl": {"hurlement": ["présence"]}, "ote": ["nombre"], "sat_cible": ["bête"]},
 "beastspeak": {"ote": ["bête"], "sat_cond": ["métamorphose"]},
 "apex-companion": {"ote": ["bête"]},
 "foraging-friends": {"cosm": ["bête"]},
 "bestial-curse": {"rempl": {"bête": ["métamorphose"]}},
 "reincarnate": {"rempl": {"bête": ["hasard"]}},
 "spiritual-transport": ESPRIT, "defended-by-spirits": ESPRIT, "helpful-wood-spirits": ESPRIT, "veil-of-spirits": ESPRIT,
 "manifestation-of-spirits": ESPRIT, "ghostly-tragedy": ESPRIT, "pernicious-poltergeist": ESPRIT, "voracious-gestalt": ESPRIT,
 "spiritual-renewal": {"cosm": ["esprit"], "sats": [CHAQUE]},
 "conjure-woodland-beings-2024": {"cosm": ["esprit", "fée"]},
 "impart-mind": {"ote": ["esprit"]},
 "regale-the-lost-ones": {"sat_cible": ["esprit"]},
 "spirit-ward": {"sat_cond": ["esprit"]},
 "ancestral-form": {"rempl": {"esprit": ["rempart"]}, "ote": ["invisibilité", "immatériel"], "cosm_plus": ["esprit"],
                    "plus": [("plein", ["invisibilité", "immatériel", "vol"], [])]},
})

# ---------- tranche 4b : lieu, terrain, piège, nourriture ----------
# Le lieu est presque toujours déjà dit par la Cible (une zone) ou la Localisation (une destination).
# « piège » n'est pas un effet : l'effet attend qu'on le déclenche → satellite Condition « déclencheur » (décision de Baptiste).
DECL = ("CONDITION", "plein", ["déclencheur"])
SANS_LIEU, SANS_TERRAIN = {"ote": ["lieu"]}, {"ote": ["terrain"]}
TABLE.update({
 "teleport": SANS_LIEU, "treacherous-teleport": SANS_LIEU, "retrocognition": SANS_LIEU, "sacred-space": SANS_LIEU,
 "unseen-custodians": SANS_LIEU, "pain-of-ages": SANS_LIEU, "transcribe-moment": SANS_LIEU,
 "detect-evil-and-good": {"sat_cible": ["lieu"]}, "aversion": {"sat_cible": ["lieu"]},
 "ventriloquism": {"rempl": {"lieu": ["leurre"]}}, "shifted-steps": {"rempl": {"lieu": ["leurre"]}},
 "leashed-shackles": {"rempl": {"lieu": ["ancrage"]}},
 "remote-viewing": {"rempl": {"lieu": ["sens"]}},
 "planar-orientation": {"rempl": {"lieu": ["direction"]}, "sat_cible": ["pouvoir"]},
 "dungeonsight": {"rempl": {"plan": ["carte"]}, "ote": ["lieu"]},       # « plan » se confondait avec le plan d'existence
 "whispering-lore": {"sat_cible": ["terrain"]}, "signs-of-the-land": {"sat_cible": ["terrain"]}, "tectonic-communion": {"sat_cible": ["terrain"]},
 "commune-with-plane": {"rempl": {"terrain": ["savoir"]}, "sat_cible": ["plan"]},
 "sawtooth-terrain": {"cible": ["terrain"]},
 "find-the-path": SANS_TERRAIN, "show-the-way": SANS_TERRAIN, "sand-table": SANS_TERRAIN, "feather-step": SANS_TERRAIN,
 "safe-passage": SANS_TERRAIN, "lose-the-path": SANS_TERRAIN,
 "unfettered-pack": {"ote": ["terrain", "entrave"]},
 "coral-eruption": {"ote": ["terrain"], "cosm": ["corail"]},
 "entangle": {"rempl": {"terrain": ["gêne"]}}, "warped-terrain": {"rempl": {"terrain": ["gêne"]}},
 "glyph-of-warding": {"ote": ["piège"], "sats": [DECL]},
 "temporary-glyph": {"ote": ["piège", "éphémère"], "sats": [DECL]},
 "animus-mine": {"ote": ["piège"], "sats": [DECL]}, "temporal-ward": {"ote": ["piège"], "sats": [DECL]},
 "ephemeral-hazards": {"ote": ["piège"], "sats": [DECL]},
 "devil-snare": {"ote": ["piège"], "cosm": ["cercle"], "sats": [DECL]},
 "pollen-pods": {"ote": ["piège"], "cosm": ["graine"], "sats": [DECL]},
 "cave-fangs": {"ote": ["roche", "piège"], "sym": TERRE, "sats": [DECL]},
 "phantom-trap": {"cosm": ["piège"]},
 "unseen-engineers": {"rempl": {"édifice": ["mécanisme"]}},
 "bloatbomb": {"rempl": {"piège": ["éclatement"]}, "cible": ["cadavre"], "sats": [DECL]},
 "possession-trap": {"rempl": {"piège": ["prison"]}, "sat_cond": ["possession"]},
 "teleport-trap": {"rempl": {"piège": ["détournement"]}, "sat_cond": ["téléportation"]},
 "aram-zeys-focus": {"ote": ["piège", "mécanisme"], "ajoute": ["précision"], "sats": [("CIBLE", None, ["piège", "mécanisme"])]},
 "aram-zeys-trap-ward": {"rempl": {"magie": ["protection"]}, "sat_cible": ["piège"]},
 "dream-feast": {"sat_cond": ["sommeil"]},
 "enhance-water": {"ote": ["nourriture"]}, "blood-of-the-martyr": {"ote": ["nourriture"]}, "winters-breath": {"ote": ["nourriture"]},
 "spirit-share": {"rempl": {"contact": ["transfert"]}, "sat_cible": ["nourriture"]},
 "sweetest-solstice": {"ote": ["repas"]},
 # le coup de l'arme, quatre fois plus fort : le 4 est un multiplicateur
 "weapon-storm": {"rempl": {"répétition": ["coup"]}, "sat_cible": ["arme"], "sats": [("QUANTITE", 4, ["multiplié"])], "valeur": "plein"},
 "garden-of-death": {"rempl": {"plante": ["attirance"], "bête": ["croissance"]},
                     "sats": [("CIBLE", None, ["plante", "bête"]), ("CONDITION", "plein", ["poison"])]},
})

# ---------- tranche 5 : vingt-quatre mots de choses (argent, cadavre, champignon, danse, écrit, étoile, fer, foule, main, métal,
# miroir, mort-vivant, nuée, objet, os, spectre, spore, trésor, vermine, œil…) ----------
# L'œil que l'on crée pour voir au loin s'écrit « capteur » ; « œil » reste la part du corps. Mort-vivant reste une Condition.
def C_(*m): return {"cosm": list(m)}
def SC_(*m): return {"sat_cible": list(m)}
TABLE.update({
 "assume-appearance": SC_("cadavre"), "elemental-speech": SC_("élémentaire"), "irriseni-mirror-sight": SC_("miroir"),
 "swarmsense": SC_("nuée"), "telekinetic-projectile": SC_("objet"), "animated-assault": SC_("objet"), "horrifying-visage": SC_("objet"),
 "illusory-hoard": SC_("trésor"), "create-treasure-map": SC_("trésor"), "verminous-lure": SC_("vermine"),
 "planetarium": {"rempl": {"étoile": ["image"]}, "sat_cible": ["ciel"]},
 "starsight": {"rempl": {"étoile": ["vue"]}, "sat_cible": ["ciel"]},
 "mirror-hideaway": {"cible": ["miroir"]},
 "poltergeists-fury": {"sat_cible": ["objet"], "ote": ["tempête"]},
 "read-the-air": {"sat_cible": ["foule"], "ote": ["empreinte"]},
 "ironbloom-sprouts": {"cible": ["champignon"], "rempl": {"fer": ["nourriture"]}, "cosm_plus": ["fer"]},
 "illusory-script": {"ote": ["écrit"]}, "wordsmith": {"ote": ["écrit"]},
 "display-aversion": {"sat_cond": ["mort-vivant"]},
 "urgathoas-beacon": {"sat_cond": ["mort-vivant"], "ote": ["proie"]},
 "mirror-mantis": {"sat_cond": ["miroir"]}, "urban-grace": {"sat_cond": ["foule"]}, "face-in-the-crowd": {"sat_cond": ["foule"]},
 "magnetic-attraction": {"rempl": {"aimant": ["attraction"]}, "sat_cond": ["métal"]},
 "torpid-reanimation": {"rempl": {"déclencheur": ["animation"]}, "cible": ["cadavre"], "sats": [DECL]},
 "arcane-eye": {"rempl": {"œil": ["capteur"]}}, "prying-eyes": {"rempl": {"œil": ["capteur"]}}, "prying-eyes-greater": {"rempl": {"œil": ["capteur"]}},
 "prying-survey": {"ote": ["œil"]}, "proliferating-eyes": {"ote": ["œil"]}, "vigilant-eye": {"ote": ["œil"]}, "evil-eye": {"ote": ["œil"]},
 "shining-cord": {"rempl": {"corde": ["lien"]}, "cosm": ["argent"], "cosm_plus": ["corde"]},
 "precious-gleam": C_("argent"), "untwisting-iron-augmentation": C_("argent"),
 "carrion-mire": C_("cadavre", "membre"),
 "drop-dead": {"rempl": {"cadavre": ["leurre"]}, "cosm_plus": ["cadavre"]},
 "fungal-blisters": C_("champignon"), "cordyceps-command": C_("spore", "champignon"), "alluring-spores": C_("spore"), "fungal-exhalation": C_("spore"),
 "illusory-creature": C_("créature"),
 "dance-of-a-hundred-cuts": C_("danse"), "frenzied-revelry": C_("danse"), "dance-of-darkness": C_("danse"),
 "blanket-of-stars": C_("nuit", "étoile"), "zenith-star": C_("étoile"),
 "cold-iron-fetters": C_("fer"), "iron-stake": C_("fer"), "ironskin": C_("fer"),
 "illusory-crowd": C_("foule"), "phantom-crowd": C_("foule"), "shadow-army": C_("foule"),
 "invisibility-sphere": {"ote": ["foule"]},
 "arcane-hand": C_("main"), "grasping-earth": C_("main"), "lay-on-hands": C_("main"),
 "quivering-palm": {"cosm": ["main"], "ote": ["mot"]},
 "forge": C_("métal"), "magnetic-acceleration": C_("métal"), "lead-plating": C_("métal"),
 "wall-of-mirrors": C_("miroir"), "mirrors-misfortune": C_("miroir"), "mirror-malefactors": C_("miroir"),
 "gebs-hammer": {"ote": ["mort-vivant"]},
 "rain-of-arrows": C_("nuée"), "vomit-swarm": {"rempl": {"nuée": ["morsure"]}, "cosm_plus": ["nuée"]}, "visions-of-danger": C_("nuée", "monstre"),
 "wall-of-bone": C_("os"), "osseous-cage": C_("os"), "armor-of-bones": C_("os"),
 "painful-vibrations": {"ote": ["os"]},
 "phantasmal-revenge": C_("spectre"), "ectoplasmic-expulsion": C_("spectre"), "invoke-spirits": C_("spectre"), "tempest-of-shades": C_("spectre"),
 "ghostly-weapon": C_("spectre"), "spectral-advance": C_("spectre"),
 "phantasmal-treasure": C_("trésor"), "unexpected-windfall": C_("trésor"), "appearance-of-wealth": C_("trésor"),
 # réécritures (règle 3)
 "silverlight": {"ote": ["argent"], "plus": [("plein", ["faiblesse"], [("CONDITION", "plein", ["argent"])])]},
 "fairy-ring-retreat": {"rempl": {"champignon": ["abri"], "pré": ["passage"]}, "cosm_plus": ["champignon", "pré"]},
 "mushroom-patch": {"rempl": {"champignon": ["gêne"]}, "cosm": ["spore"], "cosm_plus": ["champignon"]},
 "impaling-spike": {"ote": ["pieu", "fer", "entrave"], "cosm_plus": ["pieu", "fer"], "plus": [("plein", ["entrave"], [])]},
 "spray-of-stars": {"ote": ["étoile", "éblouissement"], "cosm_plus": ["étoile"], "plus": [("plein", ["éblouissement"], [])]},
 "spectral-hand": {"cosm": ["main"], "sats": [("LOCALISATION", "plein", [])]},
 "warp-wood": {"ote": ["métal"]},                       # « métal » était une erreur : la Cible dit « bois »
 "flesh-puppet": {"rempl": {"mort-vivant": ["animation"]}},
 "insect-plague": {"rempl": {"nuée": ["morsure"]}, "cosm": ["insecte"], "cosm_plus": ["nuée"]},
 "swarm-skin": {"rempl": {"nuée": ["forme"]}},
 "storm-lord": {"rempl": {"temps": ["climat"]}, "ote": ["nuée"]},       # « temps » se confondait avec la durée
 "bonewall-bulwark": {"ote": ["os", "rempart", "abri"], "sats": [CHAQUE], "plus": [("plein", ["abri"], [])]},
 "swamp-of-sloth": {"rempl": {"vermine": ["morsure"]}, "ote": ["marais", "boue"], "cosm_plus": ["marais", "vermine"], "plus": [("plein", ["gêne"], [])]},
})

# ---------- paquet 6 : mots rares, dans l'ordre de la bibliothèque (première moitié) ----------
TABLE.update({
 "shamefully-overdressed": SC_("vêtement"), "commune-with-birds": SC_("oiseau"), "speak-local-language": SC_("région"),
 "beloved-of-the-forge": SC_("foyer"), "commune-with-texts": SC_("livre"), "medusas-bane": SC_("regard"), "gravity-bow": SC_("arc"),
 "saddle-surge": SC_("monture"), "skyshroud": SC_("ciel"),
 "page-bound-epiphany": {"cible": ["livre"]},
 "revelation": {"ote": ["mécanisme", "énigme"], "ajoute": ["savoir"], "sats": [("CIBLE", None, ["mécanisme", "énigme"])]},
 "bed-of-iron": {"rempl": {"sommeil": ["repos"]}, "sat_cible": ["armure"]},
 "planar-adaptation": {"rempl": {"milieu": ["adaptation"]}, "sat_cible": ["plan"]},
 "telekinetic-assembly": {"rempl": {"création": ["façonnage"]}, "sat_cible": ["mécanisme"]},
 "damnation-of-memory": {"sat_cible": ["être"], "ote": ["gemme"]},
 "kalistocrats-nightmare": {"sat_cible": ["pièce"], "cosm": ["cuivre"]},
 "village-veil": {"cible": ["village"]}, "billowing-skirt": {"cible": ["vêtement"]},
 "blood-sentinel": {"rempl": {"statue": ["animation"]}, "cible_plus": ["statuette"]},
 "alter-musical-instrument": {"ote": ["instrument"]}, "animate-rope": {"ote": ["nœud"]}, "daggermarks-exchange": {"ote": ["crachat"]},
 "dongun-shapers-touch": {"rempl": {"forme": ["façonnage"]}, "ote": ["matière"]},
 "blessing-of-the-watch": {"sat_cond": ["cité"]}, "anti-summoning-shield": {"sat_cond": ["invoqué"]},
 "sepia-snake-sigil": {"cosm": ["serpent"], "sats": [DECL]},
 "unconscious-agenda": {"rempl": {"but": ["injonction"]}, "ote": ["torpeur"], "sats": [DECL]},
 "contingent-scroll": {"rempl": {"déclencheur": ["transfert"]}, "cosm": ["parchemin"], "sats": [DECL]},
 "zone-of-truth": C_("cloche"), "heroes-feast": C_("festin"), "demiplane": C_("porte"), "astral-projection": C_("corde"),
 "accursed-glare": C_("regard"), "vengeful-comets": C_("comète"), "sealed-sending": C_("parchemin"), "ravens-flight": C_("oiseau"),
 "summon-elemental-steed": C_("char"), "sundered-serpent-coil": C_("serpent"), "diamond-spray": C_("diamant"), "scribes-binding": C_("livre"),
 "apsus-shining-scales": C_("écaille"), "light-lance": C_("phare"),
 "silt-sphere": {"cosm": ["nuage"], "ote": ["contenant"]},
 "plundered-power": {"cosm": ["sanguine"], "ote": ["nature"]},
 "shrink-item": {"ote": ["pièce"]}, "detect-relations": {"ote": ["famille"]},
 # réécritures (règle 3)
 "black-spot": {"rempl": {"équipage": ["malchance"]}},
 "blazing-rainbow": {"rempl": {"pont": ["passage"]}, "ote": ["arc"], "cosm": ["lumière"]},
 "hungry-darkness": {"rempl": {"dent": ["croc"]}, "cosm": ["ténèbres"]},
 "create-pit": {"rempl": {"trou": ["chute"]}, "cosm_plus": ["trou"]},
 "pick-your-poison": {"rempl": {"vie": ["sursis"], "vin": ["ivresse"]}},
 "storm-of-blades": {"rempl": {"épée": ["lame"]}},
 "obsidian-flow": {"ote": ["sol", "verre"], "cosm_plus": ["verre"], "plus": [("plein", ["glissade"], [])]},
 "scorching-ash-form": {"rempl": {"gaz": ["étouffement"]}, "cosm": ["cendre"]},
 "fools-gold-vc": {"rempl": {"valeur": ["apparence"]}, "cosm": ["or"]},
 "create-soul-gem": {"rempl": {"gemme": ["prison"]}, "cosm_plus": ["gemme"]},
 "true-creation": {"rempl": {"matière": ["création"]}},
 "frosthammer": {"ote": ["marteau", "chute"], "plus": [("plein", ["renversement"], [])]},
 "keyhole": {"rempl": {"serrure": ["ouverture"]}},
 "pattern-recognition": {"rempl": {"motif": ["fouille"]}, "ote": ["trouble"]},
 "tears-to-wine": {"rempl": {"vin": ["alcool"]}},
 "breadcrumbs": {"rempl": {"passage": ["piste"]}, "ote": ["traînée"]},
})

# ---------- paquet 7 : mots rares (seconde moitié) ----------
def O_(*m): return {"ote": list(m)}
TABLE.update({
 "empty-pack": SC_("contenu"), "rapid-adaptation": SC_("milieu"), "adapt-self": SC_("milieu"), "fires-pathway": SC_("brasier"),
 "pulse-of-the-city": SC_("cité"), "extract-brain": SC_("tête"), "restyle": SC_("habit"),
 "fantastic-facade": {"cible": ["ville"], "ote": ["peuple"]},
 "ravenous-portal": {"cosm": ["monstre"], "ote": ["garde"], "sats": [DECL]},
 "censure-falsehoods": {"sat_cond": ["mensonge"], "cosm": ["crapaud"]},
 "needle-of-vengeance": {"sat_cond": ["interdit"], "cosm": ["aiguille"]},
 "brine-dragon-bile": {"ote": ["blessure", "sel"]},
 "magnetic-dominion": {"ote": ["aimant"], "sats": [("CONDITION", "plein", ["métal"])]},
 "energy-aegis": {"ote": ["toutes"], "sats": [("QUANTITE", "plein", [])]},
 "shattering-gem": C_("gemme"), "chromatic-armor": O_("couleur", "toutes"), "soothing-blossoms": C_("fleur"),
 "magic-mailbox": O_("contenu"), "petal-storm": C_("pétale"), "pocket-library": C_("livre"), "seashell-of-stolen-sound": C_("coquilles"),
 "suspended-retribution": C_("épée"), "entrancing-eyes": C_("regard"), "thicket-of-knives": O_("bras", "double"),
 "portrait-of-the-artist": O_("ouvrage"), "shadow-raid": C_("silhouette"), "electric-arc": O_("éclair"), "acidic-burst": O_("coquilles"),
 "friendfetch": C_("fil"), "blazing-dive": {"cosm": ["comète"], "ote": ["chute"]}, "stormburst": O_("éclair", "vent"),
 "reapers-lantern": C_("lanterne"), "rouse-skeletons": C_("squelette"), "shadow-spy": C_("oiseau"),
 "lifes-fresh-bloom": O_("floraison"), "vital-beacon": O_("phare"), "field-of-life": O_("champ"), "mariners-curse": O_("mer"),
 "iron-gut": O_("gorge"), "elemental-gift": O_("sève"), "blackfingerss-blades": O_("scorpion"), "angel-form": O_("fiélon"),
 "buoyant-bubbles": C_("bulle"), "glass-shield": C_("verre"), "phoenix-ward": O_("phénix"), "elemental-sense": O_("aimant"),
 "the-parrots-whisper": {"cosm": ["perroquet"], "ote": ["voix"]},
 "tremor-signs": O_("vibration"), "tremorsense": O_("sol"), "albatross-curse": C_("albatros"), "indolent-haze": C_("pavot"),
 "overwhelming-memory": O_("larmes"), "coral-scourge": C_("corail"), "thermal-remedy": O_("goût", "remède"),
 "arrow-salvo": C_("arc"), "dancing-fountain": C_("source"), "grasp-of-the-deep": O_("abysse"), "vacuum": O_("souffle"),
 "deep-breath": O_("souffle"), "hippocampus-retreat": {"cosm": ["queue"], "ote": ["nage", "fuite"], "seul": "queue"},
 "shielded-arm": C_("minéral"), "vitrifying-blast": C_("verre"), "chrysopoetic-curse": C_("or"), "buzzing-bites": C_("insecte"),
 "ki-form": O_("couronne"), "diabolic-edict": O_("tâche"), "flurry-of-claws": C_("dragon"), "dragon-claws": C_("dragon"),
 "undeaths-blessing": O_("tombe"), "grasping-grave": C_("bras", "squelette"), "nymphs-token": C_("gage"), "ancestral-touch": C_("ancêtre"),
 "overstuff": O_("repas"), "natures-bounty": C_("fruit"), "dazzling-flash": C_("éclair"),
 "charged-javelin": {"cosm": ["javelot"], "ote": ["champ"]},
 "draconic-barrage": C_("dragon"), "oathkeepers-insignia": C_("gage"), "asmodean-wager": C_("gage"), "stone-lance": C_("lance"),
 "ideal-mimicry": {"cosm": ["poupée"], "ote": ["pensée"]},
 "statuette": C_("statuette"), "mosquito-blight": C_("insecte"), "unseen-heralds": C_("bouche"), "bountiful-oasis": C_("source"),
 "sky-signs": O_("ciel"),
 # réécritures (règle 3)
 "whirling-scarves": {"rempl": {"vêtement": ["flou"]}},
 "prismatic-shield": {"rempl": {"éclat": ["rempart"]}, "ote": ["prisme"]},
 "ash-cloud": {"ote": ["cendre", "fumée", "éblouissement"], "plus": [("plein", ["éblouissement"], [])]},
 "maze-of-locked-doors": {"rempl": {"passage": ["exil"], "porte": ["verrou"]}, "ote": ["serrure"]},
 "share-lore": {"rempl": {"prêt": ["partage"]}}, "halcyon-infusion": {"rempl": {"prêt": ["partage"]}},
 "befitting-attire": {"rempl": {"habit": ["apparence"]}, "cosm_plus": ["habit"]},
 "vibrant-pattern": {"rempl": {"motif": ["éblouissement"], "lumière": ["aveuglement"]}},
 "blinding-beauty": {"rempl": {"fascination": ["éblouissement"], "regard": ["aveuglement"]}},
 "worms-repast": {"rempl": {"chair": ["rongement"]}, "cosm": ["ver"]},
 "corrosive-muck": {"ote": ["flaque", "enlisement"], "plus": [("plein", ["enlisement"], [])]},
 "needle-darts": {"rempl": {"aiguille": ["perce"]}},
 "camel-spit": {"seul": "crachat", "ote": ["crachat", "éblouissement"], "plus": [("plein", ["éblouissement"], [])]},
 "glacial-heart": {"ote": ["lenteur", "statue"], "plus": [("plein", ["lenteur", "pétrification"], [])]},
 "fey-disappearance": {"rempl": {"sous-bois": ["aisance"]}},
})

# ---------- paquet 8 : l'Impact ne portait que des noms de choses (première moitié) ----------
# Un mur barre, une gemme enferme, une nuée mord : on écrit ce que la chose fait. Ce que le sort crée pour de bon (une arme,
# de la nourriture, un navire) ou ce qu'on devient (une bête) reste.
def R_(a, *b, **k): return {"rempl": {a: list(b)}, **k}
TABLE.update({
 "wall-of-stone": R_("pierre", "barrière"), "wall-of-iron": R_("fer", "barrière", cosm_plus=["fer"]),
 "prismatic-wall": R_("prisme", "barrière"), "flesh-wall": R_("mort-vivant", "barrière"),
 "stone-shield": R_("pierre", "rempart", sym=TERRE), "defending-bone": R_("os", "rempart", cosm_plus=["os"]),
 "iron-body": R_("fer", "rempart", cosm_plus=["fer"]),
 "last-azlantis-defending-sword": R_("épée", "parade", cosm_plus=["épée"]),
 "trap-the-soul": R_("gemme", "prison", cosm_plus=["gemme"]), "soul-bind": R_("gemme", "prison", cosm_plus=["gemme"]),
 "entrap-spirit": R_("miroir", "prison", cosm_plus=["miroir"]),
 "peacebond": R_("contenant", "entrave"),
 "hallucinatory-terrain": R_("terrain", "apparence", cible_plus=["terrain"]), "mirage-arcane": R_("terrain", "apparence", cible_plus=["terrain"]),
 "mirage": R_("terrain", "apparence", cible_plus=["terrain"]),
 "lay-of-the-land": {"sat_cible": ["terrain"], "ajoute": ["savoir"]},
 "arcane-sword": R_("épée", "arme"), "force-sword": R_("épée", "arme", cosm_plus=["épée"]),
 "icicle-dagger": R_("dague", "arme", forme="dague"),
 "siege-scatter": O_("roche"), "volcanic-storm": O_("roche"), "gravel-vortex": O_("pierre"),
 "molten-orb": C_("métal"), "fire-snake": O_("serpent"), "pale-flame": O_("flamme"), "burning-gaze": C_("regard"),
 "cosmic-ray": C_("ciel"), "burst-of-nettles": C_("ortie"),
 "mad-monkeys": R_("nuée", "gêne", "larcin"), "release-the-hounds": R_("nuée", "assaut"), "swarm-of-fangs": R_("nuée", "morsure"),
 "pocketful-of-vipers": R_("piège", "morsure", sats=[DECL]),
 "spiritual-squire": R_("serviteur", "service"),
 "wicker-horse": R_("plante", "transport", cosm_plus=["plante"]),
 "mage-hand": R_("main", "déplacement"),
 "pilfering-hand": R_("main", "saisie", cosm_plus=["main"]),
 "continual-flame": R_("flamme", "lumière"),
 "meld-into-stone": {"sat_cible": ["pierre"], "ajoute": ["abri"]},
 "holy-sword": R_("cercle", "protection"),
 "demand-offering": R_("offrande", "don"), "lock-gaze": R_("regard", "fascination"),
 "memorize-page": {"sat_cible": ["écrit"], "ajoute": ["souvenir"]},
 "impossible-angles": R_("motif", "égarement"),
 "twine-double": R_("corde", "quasi-réel", cosm_plus=["corde"]),
 "discern-next-of-kin": R_("famille", "parenté"), "speechreaders-sight": R_("lèvre", "parole"),
 "forest-friend": R_("forêt", "aisance", sats=[("CONDITION", "plein", ["forêt"])]),
 "bountiful-banquet": R_("festin", "nourriture"),
 "bloody-arrows": R_("sang", "saignement"),
 "fungal-infestation": R_("champignon", "fragilité"),
 "blood-crow-strike": R_("corbeau", "projectile"),
 "burning-entanglement": {"ote": ["plante"], "cosm_plus": ["plante"], "plus": [("plein", ["entrave"], [])]},
 "daybreak-arrow": R_("aube", "lumière"),
 "ash-storm": R_("cendre", "gêne"),
 "garden-of-peril": R_("champignon", "poison", cosm_plus=["champignon"]),
 "spore-burst": R_("spore", "éclatement", cosm_plus=["spore"]),
 "wall-of-clockwork": R_("mécanisme", "déchirure"),
 "baphomets-blessing": R_("taureau", "métamorphose"),
 "conjure-minor-elementals-2024": R_("terrain", "gêne"),
})

# ---------- paquet 9 : l'Impact ne portait que des noms de choses (seconde moitié) ; fin de la passe 2 ----------
TABLE.update({
 "dimensional-blade": R_("nourriture", "tranchant"),      # « plat » avait été fondu dans « nourriture » : l'arme devient plate, elle tranche
 "body-capacitance": R_("contenant", "absorption"), "bowstaff": R_("bâton", "arme"),
 "claim-identity": {"ajoute": ["apparence"], "sur": ["larcin"]},
 "crimson-breath": R_("crachat", "venin"), "swallow-poison": R_("crachat", "absorption"), "film-of-filth": R_("crachat", "nausée"),
 "drain-poison": R_("arme", "transfert", sats=[("CIBLE", None, ["arme"])]),
 "emblem-of-greed": R_("glaive", "embrasement"), "entomb": R_("tombe", "enlisement"), "golden-guise": R_("or", "métamorphose"),
 "gorums-armor": {"ajoute": ["riposte"], "sur": ["pointe"]},
 "grappling-scarf": R_("corde", "saisie", "allonge"), "hidden-spring": R_("source", "création"),
 "iron-spine": R_("fer", "perce", cosm_plus=["fer"]), "ironbeard": R_("fer", "rempart", cosm_plus=["fer"]),
 "lily-pad-stride": R_("nénuphar", "marche", cosm_plus=["nénuphar"]),
 "magnifying-chime": R_("vibration", "fracas"), "ropeweave": R_("outil", "façonnage"), "salvage": R_("épave", "réparation"),
 "sea-of-dust": R_("désert", "dessèchement"),
 "serrens-swift-girding": R_("armure", "hâte", sats=[("CIBLE", None, ["armure"])]),
 "stone-fist": R_("pierre", "durcissement", sym=TERRE),
 "sword-to-snake": R_("serpent", "morsure", sats=[DECL], cosm_plus=["serpent"]),
 "treasure-stitching": R_("ouvrage", "cache"), "scoop": R_("récipient", "port"), "blood-blaze": R_("sang", "riposte"),
 "distortion-lens": R_("lentille", "projectile", cosm_plus=["lentille"]),
 "ocular-overload": R_("éclair", "éblouissement"), "undermine-reality": R_("matière", "quasi-réel"),
 "sanguine-mist": R_("sang", "drain"),
 "vampiric-maiden": {"ote": ["tombe"], "plus": [("plein", ["entrave"], [])]},
 "enhance-victuals": {"rempl": {"festin": ["pureté"], "vin": ["qualité"]}},
 "instant-potter": R_("ouvrage", "façonnage"), "weave-wood": R_("ouvrage", "façonnage", ote=["fil"]),
 "conjured-conveyance": R_("monture", "transport"),
 "live-wire": R_("fil", "tranchant", ote=["cuivre"]),
 "efficient-apport": R_("main", "téléportation"),
 "ancestral-defense": R_("ancêtre", "protection", cosm_plus=["ancêtre"]),
 "serrate": R_("dent", "déchirure"), "diamond-dust": R_("cristal", "tranchant"),
 "swarm-form": R_("nuée", "rempart", cosm_plus=["nuée"]),
 "veil-of-ash": O_("cendre"), "puff-of-poison": O_("souffle"), "briny-bolt": C_("sel"), "sudden-bolt": O_("éclair"),
 "holy-cascade": O_("contenant"), "cinder-swarm": C_("insecte", "braise"), "vengeful-glare": C_("regard"),
 "embrace-the-pit": {"cosm": ["corne"], "ote": ["fiélon"]},
 "hellfire-plume": O_("flamme"), "dragon-breath": C_("dragon"), "hurtling-stone": O_("pierre"), "touch-of-undeath": O_("tombe"),
 "asterism": C_("étoile"), "for-love-for-lightning": O_("arme"), "suns-fury": O_("flamme"), "combustion": O_("flamme"),
 "legendary-proportions": O_("géant"),
})

# =====================================================================================================================
# PASSE 3 — les conditions écrites comme des effets (première moitié : sommeil, blessure, parole, lumière, mouvement, chant…)
# Une condition qui tient l'effet se pose en satellite Condition sur son cercle d'Impact. Quand le cercle de Condition ou de
# Durée du glyphe la dit déjà, le mot quitte seulement l'Impact.
# =====================================================================================================================
def K_(mot): return ("CONDITION", "plein", [mot])
def M_(page, **k):
    """ajoute des consignes à une page déjà dans la table"""
    t = dict(TABLE.get(page, {}))
    for a, b in k.items():
        t[a] = b if isinstance(b, (str, bool, int)) else ({**t.get(a, {}), **b} if isinstance(b, dict) else list(t.get(a, [])) + list(b))
    TABLE[page] = t
for _p, _k in {
 "geas": {"sat_cond": ["offense"]},
 "challenge-evil": {"ote": ["nausée"], "plus": [("plein", ["nausée"], [K_("fuite")])]},
 "over-the-coals": {"ote": ["dette", "ordre"], "sats": [K_("offense")], "plus": [("plein", ["injonction"], [])]},
 "bleed-for-your-master": {"sat_cond": ["blessure"]}, "die-for-your-master": {"sat_cond": ["blessure"]},
 "serenity": {"ote": ["paix", "blessure"], "ajoute": ["douleur"], "sats": [K_("combat")], "plus": [("plein", ["paix"], [])]},
 "blurred-movement": {"sat_cond": ["mouvement"]},
 "agitate": {"ote": ["mouvement"], "sats": [K_("immobilité")]},
 "suspended-retribution": {"sat_cond": ["interdit"]}, "forbidden-thought": {"sat_cond": ["interdit"]},
 "damnation": {"sat_cond": ["hostile"]},
 "blood-ward": {"rempl": {"espèce": ["protection"]}, "sat_cond": ["désigné"]},
 "beacon-of-guilt": {"rempl": {"lumière": ["marque"]}, "sat_cond": ["larcin"]},
 "penumbral-disguise": {"sat_cond": ["pénombre"]}, "dim-the-light": {"sat_cond": ["pénombre"]},
 "sleepwalking-suggestion": {"sat_cond": ["sommeil"]}, "vigilant-rest": {"sat_cond": ["sommeil"]},
 "nap-stack": {"sat_cond": ["sommeil"]}, "restful-sleep": {"sat_cond": ["sommeil"]},
 "triggered-suggestion": {"ote": ["déclencheur"], "sats": [DECL]}, "subconscious-suggestion": {"ote": ["déclencheur"], "sats": [DECL]},
 "sudden-recollection": {"ote": ["déclencheur"], "sats": [DECL]}, "auditory-hallucination": {"ote": ["déclencheur"], "sats": [DECL]},
 "implanted-projection": {"ote": ["sommeil"], "sats": [DECL]},
 "grim-stalker": {"rempl": {"sommeil": ["cauchemar"]}, "ote": ["douleur"], "sats": [DECL]},
 "deadmans-contingency": {"rempl": {"mort": ["sort"]}, "ote": ["déclencheur"]},       # le cercle de Condition dit déjà « mort »
 # déjà dit par la Condition ou la Durée du glyphe
 "blend-with-surroundings": {"rempl": {"décor": ["apparence"]}, "ote": ["immobilité"], "cosm_plus": ["décor"]},
 "pillow-talk": {"ote": ["sommeil"]}, "sleepwalk": {"ote": ["sommeil"]}, "hunters-vision": {"ote": ["proie"]},
 "return-the-favor": {"ote": ["dette"]}, "heros-defiance": {"ote": ["défi"]},
 "song-of-the-fallen": {"cosm": ["chant"], "ote": ["mort"]},
 "litany-of-eloquence": {"ote": ["parole"]}, "peacemakers-parley": {"ote": ["parole"]}, "debilitating-speech": {"ote": ["parole"]},
 "compelling-rant": {"ote": ["parole"]}, "blistering-invective": {"ote": ["parole"]},
 # ce qu'on entend ou voit
 "deathless-march": {"cosm": ["chant"]}, "girzanjes-march": {"cosm": ["chant"]}, "unfathomable-song": {"cosm": ["chant"]},
 "clawsong": {"cosm": ["chant"]}, "soothing-ballad": {"cosm": ["chant"]}, "music-of-the-spheres": {"cosm": ["musique"]},
 "concordant-choir": {"ote": ["musique"]}, "fatal-aria": {"cosm": ["musique"], "ote": ["perfection"]},
 "light-prison": {"cosm": ["lumière"]}, "mydriatic-spontaneity": {"cosm": ["lumière"]}, "radiant-globe": {"cosm": ["lumière"]},
 # mots mal choisis
 "illusion-of-calm": {"rempl": {"immobilité": ["leurre"]}},
 "swallow-your-fear": {"rempl": {"peur": ["courage"]}, "ote": ["combat"]},
 "companion-mind-link": {"rempl": {"parole": ["télépathie"]}},
 "companion-life-link": {"rempl": {"blessure": ["alerte"]}},
 "synaptic-scramble": {"sat_cible": ["parole"]}, "speak-with-plane": {"sat_cible": ["plan"]}, "sarzari-shadow-memory": {"sat_cible": ["proie"]},
 "infectious-melody": {"rempl": {"mélodie": ["contrainte"]}, "ote": ["chant"], "sat_cible": ["parole"], "cosm_plus": ["mélodie"]},
 "unwelcome-halo": {"rempl": {"lumière": ["révélation"]}, "cosm": ["halo"]},
 "titanic-anchoring": {"ote": ["immobilité"]},
 "stifling-stillness": {"ote": ["immobilité"], "plus": [("plein", ["gêne"], [])]},
 "hymn-of-peace": {"ote": ["combat"]}, "wandering-weather": {"ote": ["mouvement"]}, "wild-instinct": {"ote": ["sommeil"]},
}.items(): M_(_p, **_k)

# ---------- passe 3, seconde moitié : peur, mort, douleur ----------
for _p, _k in {
 "death-knell-aura": {"sat_cond": ["mort"]}, "redcaps-touch": {"sat_cond": ["mort"]}, "martyrs-last-blessing": {"sat_cond": ["mort"]},
 "cruel-jaunt": {"sat_cond": ["peur"]},
 "sadomasochism": {"ote": ["douleur"], "sats": [K_("blessure")]},
 "mantle-of-doubt": {"sur": ["doute"], "sats": [K_("combat")]},
 "painful-revelation": {"ote": ["illusion"], "sats": [DECL]},
 "spellcurse": {"ote": ["douleur"], "sat_cond": ["sort"]},
 "black-mark": {"sur": ["malédiction"], "sats": [K_("eau")]},       # la peur de l'eau : le manque noté au lot d'essai
 "deaths-call": {"ote": ["mort"]}, "rest-eternal": {"ote": ["mort"]},
 "temporary-resurrection": {"rempl": {"mort": ["vie"]}},
 "bane": {"ote": ["peur"]}, "bless": {"ote": ["peur"]}, "remove-fear": {"ote": ["peur"], "seul": "courage"}, "veil-of-confidence": {"ote": ["peur"]},
 "blessing-of-luck-and-resolve": {"rempl": {"peur": ["courage"]}},
 "dissonant-whispers": {"ote": ["fuite", "peur"], "plus": [("plein", ["peur", "fuite"], [])]},
 "haunting-reminder": {"rempl": {"peur": ["service"]}, "ote": ["vengeance"], "plus": [("plein", ["hantise"], [K_("trahison")])]},
 "besmaras-grasping-depths": {"ote": ["mort"]},
 "curse-of-unexpected-death": {"ote": ["mort"]},
 "deathwine": {"ote": ["mort"], "sym": ["tenebreux"]},
 "commanding-lash": {"rempl": {"douleur": ["menace"]}},
 "shared-sacrifice": {"rempl": {"douleur": ["blessure"]}},
 "mimic-undead": {"rempl": {"mort": ["apparence"]}, "ote": ["lueur"]},
 "dirge-of-doom": {"ote": ["mort"]},
 "sotto-voce": {"cosm": ["murmure"]}, "crescent-scepter": {"cosm": ["symbole"]},
}.items(): M_(_p, **_k)

# ---------- passe 4 : mots à double sens (validé par Baptiste, 16 novembre 2026) ----------
# charge = ce dont un être est chargé ; ordre = l'ordre du monde ; injonction = le commandement donné à quelqu'un ;
# élan = le mouvement unique ; ardeur = l'entrain qui renforce ; nature = le monde sauvage ; essence = ce qu'est une chose
for _p, _k in {
 "burdened-thoughts": {"rempl": {"charge": ["fardeau"]}}, "leaden-steps": {"rempl": {"charge": ["fardeau"]}},
 "linebreaker": {"ote": ["charge"], "ajoute": ["renversement"]},
 "spectral-advance": {"rempl": {"charge": ["ruée"]}}, "er-aspects-of-the-crucible-breath": {"rempl": {"charge": ["ruée"]}},
 "enhance-ability": {"rempl": {"charge": ["force"], "chute": ["adresse"]}},
 "unconscious-agenda": {"rempl": {"ordre": ["injonction"]}}, "commanding-lash": {"rempl": {"ordre": ["injonction"]}},
 "diabolic-edict": {"rempl": {"ordre": ["injonction"]}},
 "quick-sort": {"rempl": {"ordre": ["rangement"]}}, "bottomless-stomach": {"rempl": {"ordre": ["rangement"]}},
 "righteous-vigor": {"rempl": {"élan": ["ardeur"]}}, "saddle-surge": {"rempl": {"élan": ["ardeur"]}},
 "infectious-enthusiasm": {"rempl": {"élan": ["ardeur"]}}, "physical-boost": {"rempl": {"élan": ["ardeur"]}},
 "litany-of-self-interest": {"rempl": {"élan": ["ardeur"]}}, "call-to-arms": {"rempl": {"élan": ["ardeur"]}},
 "competitive-edge": {"rempl": {"élan": ["ardeur"]}}, "cinder-gaze": {"rempl": {"élan": ["ardeur"]}},
 "vicious-howl": {"rempl": {"élan": ["ardeur"]}}, "dull-ambition": {"rempl": {"élan": ["ardeur"]}},
 "detect-poison-and-disease": {"rempl": {"nature": ["essence"]}}, "diagnose-disease": {"rempl": {"nature": ["essence"]}},
 "flaming-aura": {"rempl": {"nature": ["essence"]}}, "frosty-aura": {"rempl": {"nature": ["essence"]}},
 "false-nature": {"rempl": {"nature": ["essence"]}},
 "read-the-air": {"rempl": {"usage": ["coutume"]}},
 "healing-well": {"quantite": "usage"}, "camel-spit": {"quantite": "usage"},       # un nombre de fois n'est pas un effet : cercle Quantité
 "moment-of-greatness": {"ote": ["double"], "sats": [("QUANTITE", 2, ["multiplié"])]},
 "arrow-eruption": {"rempl": {"double": ["répétition"]}},
 "conductive-weapon": {"ote": ["courant"]},       # les symboles de la combinaison Éclair disent déjà l'énergie
 "read-magic": {"rempl": {"sens": ["lecture"]}},
 "dissolution": {"rempl": {"vide": ["effacement"]}},
 "lightfingers": {"rempl": {"chute": ["désarmement"]}},
 "aspect-of-the-wolf": {"rempl": {"chute": ["force", "adresse", "renversement"]}},
 "deathless-march": {"ote": ["retour"]},
}.items(): M_(_p, **_k)

# chute = tomber de haut ; renversement = jeté à terre (validé par Baptiste, 16 novembre 2026)
for _p in ("command", "grease", "hideous-laughter", "sleet-storm", "forced-repentance", "burst-of-force", "ice-slick", "river-of-wind",
           "rope-tornado", "thundering-drums", "thunderstomp", "blade-lash", "earth-tremor", "touch-of-gracelessness", "tripvine",
           "wave-form", "carrion-mire", "shockwave", "blazing-fissure", "localized-quake"):
    M_(_p, rempl={"chute": ["renversement"]})

# ---------- passe 5, premier paquet : cercles chiffrés inexpliqués (validé par Baptiste, 16 novembre 2026) ----------
for _p, _k in {
 "rewrite-possibility": {"rempl": {"élan": ["ardeur"]}},
 "wall-of-iron": {"rempl": {"chute": ["écrasement"]}},
 "fire-sneeze": {"rempl": {"chute": ["renversement"]}},
 "umbral-weapon": {"ote": ["écho"], "sats": [K_("échec")], "cosm_plus": ["ombre"]},       # hybride : le noyau dit déjà le froid
 "duplicate-foe": {"sur": ["perte"], "sats": [CHAQUE]},
}.items(): M_(_p, **_k)

# ---------- passe 5, deuxième paquet : sorts mis de côté, relus dans leur texte (validé par Baptiste, 16 novembre 2026) ----------
_T = ("CIBLE", None, ["terrain"])
for _p, _k in {
 "cast-into-time": {"rempl": {"chute": ["exil"]}},
 "animal-feature": {"ote": ["trait"]},
 "summon-genie-lesser": {"ote": ["petit"], "sym_mot": {"vent": ["air"]}},
 "elementalism": {"rempl": {"brise": ["poussée"], "pluie": ["mouillé"]}, "ote": ["poussière", "braise"]},
 "fey-abeyance": {"cible": ["fée"], "quantite": "cloche", "quantite_lit": "emplacements de cloches", "plus_si": "cloche", "plus": [("plein", ["douleur"], [], "les cloches font souffrir les fées là où elles pendent")], "cosm_plus": ["cloche"]},
 "draw-the-lightning": {"refait": True, "plus": [
    (20, [], [], "3d12 en moyenne : la foudre traverse l'ennemi"),
    (7, [], [("CIBLE", None, ["arme"]), CHAQUE], "1d12 en moyenne ajouté à mon premier coup"),
    (13, [], [K_("orage")], "2d12 en moyenne de plus sous un ciel d'orage")]},
 "one-with-the-land": {"refait": True, "plus": [
    ("plein", ["fusion", "abri"], [_T], "fondu dans le sol ou un grand arbre, abrité"),
    ("plein", ["vibration"], [("AMPLEUR", 60, ["mètres"])], "je sens tout ce qui bouge alentour"),
    (32, [], [("AMPLEUR", 18, ["mètres"]), _T], "le terrain frappe pour moi, 5d12 en moyenne")]},
 "sebaceous-twin": {"refait": True, "plus": [
    ("plein", ["double", "parasite", "gêne"], [], "un double parasite pend à son corps"),
    (1, ["faiblesse", "nausée"], [CHAQUE], "il lui boit le sang")]},
 "life-blast": {"refait": True, "plus": [
    (18, ["vie"], [K_("mort-vivant"), K_("plante")], "1d6 par niveau aux morts-vivants, au milieu de la végétation"),
    ("plein", ["flétrissure"], [("CIBLE", None, ["plante"])], "la végétation alentour meurt")]},
 "bestial-curse": {"refait": True, "plus": [
    ("plein", ["malédiction", "métamorphose", "griffe"], [], "une forme bestiale, griffes ou crocs ; ses mains la trahissent une fois sur cinq"),
    (1, ["maladresse"], [], "gauche de 1"),
    (1, ["vulnérabilité"], [K_("argent")], "l'argent la blesse de 1 de plus")]},
 "impeccable-flow": {"refait": True, "plus": [
    (1, ["ordre", "accord"], [], "accordé à l'ordre du monde : 1 ajouté à tout"),
    (1, ["revers"], [K_("échec")], "un échec grave le retourne en 1 retranché")]},
 "juvenile-companion": {"refait": True, "fin": ["offense"], "plus": [
    ("plein", ["petit", "jeunesse", "paix", "lenteur"], [], "mon compagnon redevient petit : minuscule, moitié moins rapide, d'allure inoffensive"),
    (5, ["vulnérabilité"], [K_("coup")], "les coups le blessent de 5 de plus")]},
}.items(): M_(_p, **_k)

# ---------- passe 5, troisième paquet (validé par Baptiste, 16 novembre 2026) ----------
for _p, _k in {
 "weird": {"sur": ["peur", "confusion"], "ajoute": ["fantasme"]},
 "mariners-curse": {"sur": ["malédiction"], "plus": [(1, ["lenteur"], [K_("mer")], "en mer, loin des côtes, ralentie de 1")]},
 "thaumaturgic-circle": {"rempl": {"cercle": ["barrière"]}, "cible": ["espèce"], "forme_prim": "disque"},
 "conditional-favor": {"rempl": {"condition": ["promesse"]}, "ote": ["renversement"], "plus": [("plein", ["revers"], [K_("trahison")], "le serment rompu, le bienfait est défait")]},
 "conditional-curse": {"ote": ["condition"], "fin": ["épreuve"]},
 "cape-of-wasps": {"refait": True, "plus": [
    ("plein", ["dissimulation"], [], "l'essaim me cache des tirs"),
    (7, ["riposte", "dard", "poison"], [], "2d6 en moyenne à qui me frappe au corps à corps"),
    ("plein", ["vol"], [("LOCALISATION", 6, ["mètres"]), CHAQUE], "ou bien l'essaim me porte")]},
 "dragonvoice": {"refait": True, "plus": [
    (6, ["prestance"], [K_("dragon")], "6 ajouté à mon ascendant, face aux dragons"),
    ("plein", ["puissance"], [], "ma voix porte bien plus loin")]},
 "innocuous-shape": {"sur": ["innocence"], "plus": [("plein", ["métamorphose", "jeunesse"], [], "changée en petit animal ou en jeune personne quelconque")]},
 "claim-identity-greater": {"refait": True, "plus": [
    ("plein", ["métamorphose", "masque"], [], "la cible changée en masque de porcelaine"),
    ("plein", ["double", "identité"], [K_("masque")], "qui porte le masque devient son double")]},
 "establish-ward": {"refait": True, "plus": [
    ("plein", ["lien"], [_T], "je me lie au lieu"),
    (9, [], [_T, CHAQUE], "le terrain frappe pour moi de 2d8 en moyenne, un coup de plus par instant"),
    (1, ["lenteur"], [K_("sortie")], "hors du domaine, je suis ralenti de 1")]},
 "mystic-carriage": {"quantite": "passager", "quantite_lit": "passagers", "cible_plus": ["passager"]},
}.items(): M_(_p, **_k)

# ---------- passe 5, dernier paquet (validé par Baptiste, 16 novembre 2026) ----------
TABLE["unblinking-flame-emblem"].pop("sym", None)       # le feu passe sur le cercle de la brûlure
for _p, _k in {
 "asmodean-wager": {"rempl": {"perte": ["revers"]}},
 "seek-shelter": {"rempl": {"peur": ["contrainte"]}},
 "remember-the-lost": {"rempl": {"offense": ["hantise"]}, "ote": ["mort"], "sat_cond": ["nom"], "cosm_plus": ["esprit"]},
 "call-spirit": {"rempl": {"mort": ["appel"]}, "sats": [K_("mort")], "quantite": "question", "quantite_lit": "questions", "plus_si": "question",
                 "plus": [("plein", ["question"], [], "une question par minute")]},
 "old-salts-curse": {"ote": ["eau"], "sur": ["malédiction"], "plus": [("plein", ["chancellement"], [K_("mer")], "au large, elle chancelle en plus")]},
 "etheric-shards": {"cercle": {
    "invisibilité": {"sur": ["invisibilité"], "plus": [(5, ["lame"], [K_("mouvement")], "1d8 en moyenne à qui bouge dans la zone"), (1, ["saignement"], [], "et la plaie saigne")]},
    "lame": {"sur": ["lame"], "sats": [K_("mouvement")], "plus": [("plein", ["lenteur"], [], "la zone ralentit qui la traverse")]}}},
 "geyser": {"cercle": {"projection": {"ote": ["eau", "projection"], "plus": [("plein", ["projection", "chute", "renversement"], [], "projetée en l'air, elle retombe à terre")]}}},
 "barbed-chains": {"rempl": {"chaîne": ["arme"]}, "ote": ["peur"], "valeur": 4, "forme": "chaîne",
                   "plus": [("plein", ["renversement"], [], "ou bien elle fait tomber"), ("plein", ["peur"], [], "qui est touché prend peur")]},
 "sepulchral-mask": {"sur": ["remords"], "plus": [(1, ["volonté"], [], "1 ajouté à ma volonté")]},
 "tempest-cloak": {"sats": [K_("projectile")], "plus": [("plein", ["gêne"], [("SYM", "air", [])], "les vents gênent l'approche")]},
 "unblinking-flame-emblem": {"rempl": {"sceau": ["marque"]}, "cosm_plus": ["sceau"],
                             "plus": [(4, [], [("SYM", "feu", [])], "1d6 en moyenne de feu en plus à chaque coup qui la touche")]},
 "guards-and-wards": {"rempl": {"brouillard": ["dissimulation"]}, "plus_si": "brouillard", "cosm_plus": ["brouillard", "toile"], "cercle": {
    "mur": {"rempl": {"porte": ["illusion"]}, "valeur": "plein", "sats": [("CIBLE", None, ["porte"]), ("QUANTITE", 6, [])]},
    "piège": {"ote": ["piège"], "sats": [DECL]},
    "scrutation": {"ote": ["illusion"]}}},
 "cursed-earth": {"cercle": {
    "famine": {"sur": ["famine"], "sats": [("CIBLE", None, ["plante"])]},
    "éveil": {"sur": ["éveil"], "sats": [("CIBLE", None, ["cadavre"]), K_("mort-vivant")]},
    "maladie": {"sur": ["maladie"], "sats": [("DUREE", 1, ["chaque", "jours"])]}}},
}.items(): M_(_p, **_k)

# ---------- après vérification : Impact sans mot, conditions en double, mots d'élément, doubles sens (validé par Baptiste, 16 novembre 2026) ----------
for _p, _k in {
 "sundering-shards": {"refait": True, "plus": [(4, ["lame"], [K_("destruction")], "1d6 en moyenne à qui tenait l'objet brisé, et à ses voisins")]},
 "barkskin": {"rempl": {"faille": ["vulnérabilité"]}, "sat_cond": ["feu"]},
 "fire-shield": {"ote": ["feu"], "sym": FEU},       # comme la forme ardente porte les symboles de la Glace : la résistance se lit avec l'énergie qu'elle arrête
 "meteor-swarm": {"ote": ["feu"]}, "moonbeam": {"ote": ["feu"]}, "symbol-of-storms": {"ote": ["vent"]},
 "flame-vortex": {"rempl": {"vent": ["gêne"]}, "sats": [("CIBLE", None, ["vol"])]},
 "elemental-annihilation-wave": {"rempl": {"vent": ["gêne"]}},
 "blood-feast": {"ote": ["sang"], "sym": SANG}, "er-flame-grant-me-strength": {"ote": ["flamme"], "sym": FEU},
 "thought-echo": {"rempl": {"écho": ["pensée", "leurre"]}}, "echo-jump": {"rempl": {"écho": ["double"]}},
 "interstellar-void": {"ote": ["vide"]},
}.items(): M_(_p, **_k)

# ---------- tri après vérification : la matière déjà dite par la Cosmétique quitte l'Impact (règle 2) ----------
for _p, _m in {'ice-storm': ['grêle'], 'incendiary-cloud': ['fumée'], 'conjure-animals-2024': ['meute', 'esprit'], 'plague-storm': ['nuage'], 'dust-of-twilight': ['poussière'],
               'hallucinogenic-smoke': ['fumée'], 'parchment-swarm': ['parchemin'], 'armor-of-darkness': ['clarté'], 'inhibiting-patterns': ['couleur'], 'reflective-scales': ['écaille'],
               'scintillating-safeguard': ['étincelle'], 'magical-fetters': ['menotte'], 'message-rune': ['rune'], 'synchronize': ['sceau'], 'cloak-of-colors': ['couleur'],
               'bracing-tendrils': ['vrille'], 'cloak-of-light': ['halo'], 'luring-wail': ['plainte'], 'spellmasters-ward': ['rune'], 'er-elden-stars': ['étoile']}.items():
    M_(_p, ote=_m)
M_("wall-of-flesh", rempl={"chair": ["barrière"]})       # comme l'autre Mur de chair : l'effet est la barrière, la chair est ce qu'on voit

# ---------- Elden Ring : règles par mot (validé par Baptiste, 16 novembre 2026) ----------
# Presque aucun sort d'Elden Ring n'avait de Cosmétique : ce qu'on voit était écrit dans l'Impact.
ER_COSM = ["dragon", "cristal", "noir", "œil", "esprit", "fil", "spectre", "nuage", "nuée", "éclat", "masse", "fleur", "bulle", "papillon", "plume", "arbre",
           "serpent", "étoile", "roche", "pilier", "tête", "bras", "main", "ours", "torrent", "lumière", "gardien",
           "pluie", "vague", "trombe", "éruption", "embrasement", "traînée", "sillage", "jaillissement", "lancer", "flaque", "brasier", "foyer"]
ER_DURE = ["flaque", "brasier", "foyer", "souvenir", "pulsation"]       # la zone qui blesse encore après le coup
ER_OTE = ["souvenir", "pulsation", "éclatement"]       # l'éclatement est dit par la Forme (sphère)
ER_REMPL = {"délai": ["différé"], "réplique": ["répétition"], "onde": ["choc"]}
ER_ARMES = ["lance", "flèche", "marteau", "glaive"]       # l'arme que le sort fabrique : règle des armes créées
def er(t):
    """la fiche de relecture d'une page d'Elden Ring : ses règles propres, complétées des règles par mot"""
    t = dict(t or {})
    propres = set(t.get("garde", [])) | set(t.get("rempl", {})) | set(t.get("cercle", {}))
    for k in ("ote", "cible", "sat_cible", "sat_cond", "cosm", "arme_forme"): propres |= set(t.get(k, []))
    t["cosm"] = list(t.get("cosm", [])) + [w for w in ER_COSM if w not in propres]
    t["dure"] = list(t.get("dure", [])) + [w for w in ER_DURE if w not in propres]
    t["ote"] = list(t.get("ote", [])) + [w for w in ER_OTE if w not in propres]
    t["rempl"] = {**{k: v for k, v in ER_REMPL.items() if k not in propres}, **t.get("rempl", {})}
    t["arme_forme"] = list(t.get("arme_forme", [])) + [w for w in ER_ARMES if w not in propres]
    return t
for _p in ("er-magic-glintblade", "er-glintblade-phalanx", "er-carian-slicer", "er-carian-greatsword", "er-carian-piercer", "er-adulas-moonblade",
           "er-carian-retaliation", "er-black-blade", "er-furious-blade-of-ansbach"):
    M_(_p, arme_forme=["lame"])       # ces sorts fabriquent une vraie lame
for _p, _k in {
 "er-tibias-summons": {"sat_cible": ["squelette"]},       # une créature invoquée, non un aspect : l'effet passe par elle (satellite Cible)
 "er-rancorcall": {"sat_cible": ["esprit"]}, "er-watchful-spirit": {"sat_cible": ["esprit"]},
 "er-magma-shot": {"cercle": {"éclatement": {"ote": ["éclatement"], "forme_prim": "sphere"}}},
 "er-fleeting-microcosm": {"garde": ["pulsation"], "ote": ["pulsation"]},       # il bat une seule fois : pas de retour à chaque instant
 "er-rain-of-fire": {"cosm": ["pluie"], "ote": ["braise"]},       # ce qu'on voit est la pluie ; le feu est dit par le noyau
 "er-messmers-orb": {"ote": ["cristal"]},       # l'orbe est une forme : le cercle Forme porte déjà la sphère
 "er-midras-flame-of-frenzy": {"cercle": {"cristal": {"ote": ["cristal"], "forme_prim": "sphere"}}},
 "er-aspects-of-the-crucible-breath": {"garde": ["fleur"]},       # ce que le lanceur devient reste en Impact
}.items(): M_(_p, **_k)
M_("er-poison-mist", rempl={"nuage": ["poison"]}, cosm_plus=["nuage"])       # le nuage est ce qu'on voit, l'effet est le poison
# le saut du lanceur est un mouvement : il prend son propre cercle, à part du coup chiffré
for _p in ("er-frozen-lightning-spear", "er-black-blade", "er-messmers-orb"):
    M_(_p, ote=["bond"], plus=[("plein", ["saut"], [], "le lanceur bondit sur sa cible")])
# derniers restes d'Elden Ring (validé par Baptiste, 16 novembre 2026)
for _p, _k in {
 "er-shatter-earth": {"ote": ["sol"]},
 "er-rock-blaster": {"rempl": {"trou": ["perce"]}},
 "er-assassins-approach": {"sat_cible": ["pas"]},
 "er-death-lightning": {"ote": ["éclair"]},       # hybride de Foudre : le noyau dit déjà l'énergie
 "er-rennalas-full-moon": {"rempl": {"faille": ["vulnérabilité"]}, "sat_cond": ["magie"]},
 "er-rannis-dark-moon": {"rempl": {"faille": ["vulnérabilité"]}, "sat_cond": ["magie"]},
 "er-roar-of-rugalea": {"ote": ["arrêt"], "quantite": "réplique", "quantite_lit": "répliques"},       # « arrêt » venait de « final » : le dernier éclat
}.items(): M_(_p, **_k)

# ---------- lexique : six mots entrés à la demande de Baptiste (16 novembre 2026) : parasite, famine, épreuve, promesse, allumage, néant ----------
for _p in ("elementalism", "druidcraft", "prestidigitation"): M_(_p, rempl={"flamme": ["allumage"]})
M_("call-the-void", rempl={"vide": ["néant"]})

# ---------- lexique : faille / faiblesse / vulnérabilité (validé par Baptiste, 16 novembre 2026) ----------
for _p in ("fungal-infestation", "weaken-earth", "vitrifying-blast", "elemental-betrayal", "wish-twisted-form", "dread-secret", "hallowed-ground", "pest-form"):
    M_(_p, rempl={"faille": ["vulnérabilité"]})
for _p in ("thought-worm-i", "pernicious-poison", "litany-of-order", "litany-of-righteousness", "silverlight", "litany-of-vengeance", "symbol-of-vulnerability"):
    M_(_p, rempl={"faiblesse": ["vulnérabilité"]})

# ---------- effets retrouvés dans les textes d'origine (passe comparative, validé par Baptiste, 16 novembre 2026) ----------
# Ce que le sort produit vraiment et que le glyphe avait laissé de côté. Rien de ce qui dépend de la résistance de la cible ne s'inscrit.
_R = lambda why, *s: ("plein", ["renversement"], list(s), why)
for _p, _k in {
 "earthquake": {"sur": ["séisme", "ruine", "fissure"], "plus": [_R("à chaque instant, ceux qui sont au sol sont jetés à terre", CHAQUE)]},
 "tsunami": {"sur": ["recul"], "ajoute": ["renversement"]},
 "battering-blast": {"sur": ["recul"], "plus": [_R("repoussée, elle tombe")]},
 "siege-scatter": {"toujours": True, "plus": [("plein", ["renversement", "recul"], [], "renversés et rejetés au bord de la zone")]},
 "sirocco": {"sur": ["chaleur"], "plus": [_R("le vent brûlant plaque au sol")]},
 "cave-fangs": {"toujours": True, "plus": [_R("les stalagmites renversent")]},
 "clashing-rocks": {"sur": ["écrasement"], "plus": [_R("pris entre les rocs, jeté à terre")]},
 "winds-of-vengeance": {"sur": ["vol"], "plus": [(22, ["riposte", "renversement"], [], "5d8 en moyenne à qui me frappe au corps à corps, cinglé par les vents")]},
}.items(): M_(_p, **_k)
for _p, _k in {
 "tidal-surge": {"sur": ["vague"], "plus": [("plein", ["recul", "renversement"], [], "repoussés, et les plus petits jetés à terre")]},
 "rovagugs-fury": {"sur": ["secousse"], "plus": [_R("la secousse fait tomber")]},
 "seismic-fissure": {"sur": ["fissure"], "plus": [("plein", ["chute"], [], "ceux qui se tiennent là tombent dans la faille"), _R("ceux qui la bordent sont jetés à terre")]},
 "upheaval": {"sur": ["séisme"], "plus": [_R("pris dans l'effondrement, jeté à terre")]},
 "stormburst": {"toujours": True, "plus": [_R("la bourrasque jette à terre")]},
 "telekinetic-bombardment": {"sur": ["projectile"], "plus": [_R("les décombres jettent à terre")]},
 "bridge-of-vines": {"sur": ["passage"], "plus": [("plein", ["renversement"], [K_("intrus")], "les lianes font tomber qui n'est pas des miens")]},
 "lifes-flowing-river": {"sur": ["entrave"], "plus": [_R("le courant renverse")]},
 "heaving-earth": {"sur": ["secousse"], "plus": [("plein", ["recul", "renversement"], [], "repoussée et jetée à terre")]},
 "untwisting-iron-roots": {"sur": ["secousse"], "plus": [_R("déséquilibrés, ils tombent"), ("plein", ["gêne"], [], "le sol reste couvert de décombres")]},
}.items(): M_(_p, **_k)
# « surprise » : la cible est prise au dépourvu, sa garde baissée (mot entré à la demande de Baptiste)
_S = lambda why: ("plein", ["surprise"], [], why)
for _p, _k in {
 "impending-doom": {"sur": ["présage"], "plus": [_S("sa mort entrevue la prend au dépourvu")]},
 "entangle-fate": {"sur": ["destin"], "plus": [_S("son destin emmêlé, elle ne voit plus venir les coups")]},
 "natures-enmity": {"sur": ["lenteur"], "plus": [_S("harcelée par les bêtes, elle ne se garde plus")]},
 "distracting-chatter": {"sur": ["vacarme"], "plus": [_S("le vacarme la distrait")]},
 "shadow-projectile": {"sur": ["projectile"], "plus": [_S("elle ne sait lequel des deux traits éviter")]},
 "worms-repast": {"sur": ["rongement"], "plus": [_S("la douleur la distrait tant que les vers la rongent")]},
 "swampcall": {"sur": ["enlisement"], "plus": [_S("à demi enfoncée, elle ne se garde plus")]},
 "frog-tongue": {"sur": ["colle"], "plus": [_S("collée à la langue, elle ne se garde plus")]},
 "crushing-ground": {"sur": ["écrasement"], "plus": [_S("prise dans le sol qui se referme")]},
}.items(): M_(_p, **_k)
M_("shifting-sand", sur=["trace"], plus=[("plein", ["entrave"], [CHAQUE], "à chaque instant, le sable empêtre ceux qui s'y trouvent")])
# terrain pénible : le sort laisse un sol (ou un air) où l'on avance mal
_G = lambda why, *s: ("plein", ["gêne"], list(s), why)
for _p, _why in {
 "ice-storm": "les grêlons encombrent le sol", "insect-plague": "la nuée gêne la marche", "earthquake": "le sol bouleversé",
 "volcanic-storm": "la cendre épaisse", "gravel-vortex": "le gravier qui tombe", "burning-sands": "un sable profond qui remue sans cesse",
 "sawtooth-terrain": "les membres qui cinglent encombrent la zone", "coral-eruption": "le corail hérisse le sol", "phantom-crowd": "la foule encombre le passage",
 "cyclone-rondo": "le tourbillon freine qui le traverse", "telekinetic-bombardment": "les décombres jonchent le sol", "rouse-skeletons": "les squelettes encombrent la zone",
 "bramble-bush": "les ronces encombrent le sol", "rubble-step": "le sol s'éboule derrière ses pas", "rainbow-fumarole": "les vapeurs gênent la marche",
 "whirlpool": "les vagues tournoyantes", "earthworks": "les buttes encombrent le sol",
}.items(): M_(_p, toujours=True, plus=[_G(_why)])
for _p, _k in {
 "impossible-angles": {"toujours": True, "plus": [("plein", ["gêne", "nausée"], [], "désorientés, ils avancent mal et le cœur leur tourne")]},
 "tar-pool": {"toujours": True, "plus": [("plein", ["entrave"], [], "le goudron empêtre qui s'y attarde")]},
 "magnetic-repulsion": {"toujours": True, "plus": [_G("qui porte du métal peine à m'approcher", K_("métal"))]},
 "ash-cloud": {"toujours": True, "plus": [_G("le nuage freine ce qui vole", ("CIBLE", None, ["vol"]))]},
 "punishing-winds": {"toujours": True, "plus": [_G("les vents freinent ce qui vole", ("CIBLE", None, ["vol"]))]},
 "agile-feet": {"toujours": True, "plus": [("plein", ["aisance"], [], "le terrain pénible ne le freine plus")]},
 "zephyrs-fleetness": {"toujours": True, "plus": [("plein", ["aisance"], [], "le terrain pénible ne les freine plus")]},
}.items(): M_(_p, **_k)
# nausée : le cœur qui tourne, que le texte donnait en plus de l'effet principal
for _p, _why in {
 "unadulterated-loathing": "près de ce qu'elle abhorre, le cœur lui tourne", "phantasmal-web": "les araignées imaginées soulèvent le cœur",
 "skin-tag": "l'esprit lui fait courir un frisson sous la peau", "symbol-of-exsanguination": "tant que le sang coule", "cosmic-ray": "irradiée, elle est prise de nausée",
 "holy-whisper": "la parole sainte soulève le cœur des êtres hostiles", "pain-strike": "la douleur lui soulève le cœur", "silverlight": "ceux que l'argent blesse",
 "garden-of-peril": "les spores des champignons", "nauseating-trail": "qui traverse les vapeurs", "instrument-of-agony": "celui que l'arme frappe",
 "iron-spine": "à chaque mouvement, les pointes la transpercent", "mirecloak": "celui qui a frappé", "cast-into-time": "au retour",
 "gasping-marsh": "le gaz des marais", "grisly-growths": "à la vue des excroissances", "mercurial-stride": "le mercure qui l'a traversée",
}.items(): M_(_p, toujours=True, plus=[("plein", ["nausée"], [], _why)])
M_("waters-of-lamashtu", refait=True, plus=[
    ("plein", ["poison", "nausée"], [("SYM", "eau", [])], "une eau qui a l'air pure : qui la boit est pris de vomissements"),
    ("plein", ["difformité", "faiblesse"], [], "ou bien son esprit est rongé et son corps déformé")])
# une allure de vol accordée par le sort, que le glyphe ne disait pas (allure : Localisation + « chaque · instants »)
_V = lambda m, why: ("plein", ["vol"], [("LOCALISATION", m, ["mètres"]), CHAQUE], why)
for _p, _k in {
 "cloud-shape": {"toujours": True, "plus": [_V(9, "le nuage que je suis devenu vole")]},
 "divine-vessel": {"toujours": True, "plus": [_V(18, "des ailes me portent")]},
 "ki-form": {"toujours": True, "plus": [("plein", ["vol"], [], "je vole aussi vite que je marche")]},
 "unblinking-flame-ignition": {"toujours": True, "plus": [("plein", ["vol"], [], "la flamme me porte, aussi vite que je marche"), ("plein", ["vision", "obscurité", "invisibilité"], [], "je vois dans le noir et je vois l'invisible")]},
}.items(): M_(_p, **_k)
# saignement et force vitale volée (« drain »), que le texte donnait en plus
_SG = lambda why, *s: ("plein", ["saignement"], list(s), why)
for _p, _k in {
 "brow-gasher": {"toujours": True, "plus": [_SG("l'entaille au front saigne dans les yeux")]},
 "fungal-infestation": {"cercle": {"champignon": {"rempl": {"champignon": ["fragilité", "saignement"]}}}},
 "touch-of-bloodletting": {"toujours": True, "plus": [_SG("ses plaies se rouvrent et saignent", CHAQUE), ("plein", ["épuisement"], [], "vidée de ses forces tant qu'elle saigne")]},
 "hungry-darkness": {"toujours": True, "plus": [_SG("sortie du nuage, elle saigne encore", CHAQUE)]},
 "rend-body-i": {"toujours": True, "plus": [_SG("le membre arraché laisse une plaie qui saigne", CHAQUE)]},
 "sawtooth-terrain": {"toujours": True, "plus": [_SG("les lames ouvrent des plaies qui saignent")]},
 "enervation": {"rempl": {"faiblesse": ["drain"]}}, "orb-of-the-void": {"rempl": {"vie": ["drain"]}},
 "lash-of-the-astradaemon": {"toujours": True, "plus": [("plein", ["drain"], [], "chaque coup de griffe lui prend de sa force vitale")]},
 "scourge-of-the-horsemen": {"toujours": True, "plus": [("plein", ["drain"], [], "leur force vitale arrachée")]},
 "breath-of-life": {"toujours": True, "plus": [("plein", ["faiblesse"], [], "on en revient affaibli, un jour durant")]},
 "temporary-resurrection": {"toujours": True, "plus": [("plein", ["faiblesse"], [], "on en revient affaibli")]},
 "metabolic-molting": {"toujours": True, "plus": [("plein", ["faiblesse"], [], "on en revient affaibli")]},
}.items(): M_(_p, **_k)
# chancellement (ne peut plus faire qu'un geste) et effroi, que le texte donnait en plus
_CH = lambda why, *s: ("plein", ["chancellement"], list(s), why)
for _p, _k in {
 "waves-of-ecstasy": {"toujours": True, "plus": [_CH("passé l'étourdissement, elles chancellent encore")]},
 "phantasmal-asphyxiation": {"toujours": True, "plus": [_CH("le souffle lui manque"), ("plein", ["inconscience"], [], "puis elle perd connaissance")]},
 "painful-revelation": {"toujours": True, "plus": [_CH("la douleur la fait chanceler")]},
 "rebuke": {"toujours": True, "plus": [_CH("sous la semonce, ils chancellent")]},
 "ride-the-lightning": {"toujours": True, "plus": [_CH("ceux que l'éclair traverse chancellent")]},
 "fleshworm-infestation": {"toujours": True, "plus": [("plein", ["maladresse", "chancellement"], [CHAQUE], "les vers la rongent : gauche et chancelante")]},
 "staggering-fall": {"toujours": True, "plus": [_CH("le souffle coupé par la chute")]},
 "debilitating-speech": {"toujours": True, "plus": [("plein", ["panique", "effroi"], [], "les plus faibles paniquent, les autres sont effrayés")]},
 "grim-stalker": {"toujours": True, "plus": [("plein", ["effroi"], [], "à chaque blessure, le traqueur bondit plus près")]},
 "unleash-pandemonium": {"toujours": True, "plus": [("plein", ["surdité", "effroi"], [], "assourdis, ils entendent encore les hurlements")]},
 "unsettling-knowledge": {"toujours": True, "plus": [("plein", ["effroi"], [], "ce qu'elle apprend l'effraie")]},
}.items(): M_(_p, **_k)
M_("ghost-brand", toujours=True, plus=[(11, ["lame", "saignement"], [], "à la fin, l'objet ressort de la chair : 3d6 en moyenne, et la plaie saigne")])
# éblouissement, aveuglement, fatigue, épuisement, entrave, surdité : dernières familles de la passe comparative
_P = lambda mots, why, *s: ("plein", mots, list(s), why)
for _p, _k in {
 "fiery-body": [_P(["éblouissement"], "qui ne détourne pas le regard de mon corps de feu")],
 "snapdragon-fireworks": [_P(["éblouissement"], "l'éclat de la fusée")], "gritty-wheeze": [_P(["éblouissement"], "le sable dans les yeux")],
 "control-sand": [_P(["éblouissement"], "la tempête de sable autour de moi")], "pollen-pods": [_P(["éblouissement", "stupeur"], "le pollen brouille la vue et l'esprit")],
 "signal-skyrocket": [_P(["éblouissement"], "l'éclat de la fusée")], "zenith-star": [_P(["éblouissement"], "le halo qui la marque")],
 "fear-the-sun": [_P(["aveuglement"], "la vive lumière l'aveugle un instant", K_("lumière")), _P(["éblouissement"], "puis elle l'éblouit tant qu'elle y reste", K_("lumière"))],
 "suns-disdain": [_P(["aveuglement"], "la vive lumière l'aveugle un instant", K_("lumière")), _P(["éblouissement"], "puis elle l'éblouit tant qu'elle y reste", K_("lumière"))],
 "prismatic-wall": [_P(["aveuglement"], "qui s'approche du mur")], "wall-of-silver": [_P(["aveuglement"], "les êtres hostiles qui le traversent")],
 "gloomblind-bolts": [_P(["aveuglement"], "les ténèbres lui couvrent la peau")], "firefall": [_P(["aveuglement"], "ceux qui regardaient le feu")],
 "cinder-swarm": [_P(["aveuglement"], "les braises dans les yeux")], "dazzling-flash": [_P(["aveuglement"], "un instant aveuglés, puis éblouis")],
 "outbreak": [_P(["fatigue"], "secoués de toux")], "call-the-void": [_P(["fatigue", "étouffement", "silence"], "près de moi, on ne peut ni respirer ni parler")],
 "dust-of-twilight": [_P(["fatigue"], "la poussière pèse sur ceux qu'elle couvre")], "night-terrors": [_P(["fatigue"], "après une nuit sans repos")],
 "boneshatter": [_P(["épuisement"], "la douleur des os qui se fêlent")],
 "searching-shadows": [_P(["entrave"], "les ombres saisissent ce qu'elles cherchent")], "maw-of-chaos": [_P(["entrave"], "pris dans les fils effilochés du réel")],
 "obsidian-flow": [_P(["entrave"], "pris dans le verre qui refroidit")],
 "unusual-anatomy": [_P(["vision", "obscurité"], "je vois dans le noir")],
 "mad-monkeys": [_P(["surdité", "nausée"], "le vacarme des singes")], "wronged-monks-wrath": [_P(["surdité"], "le fracas assourdit")],
}.items(): M_(_p, toujours=True, plus=_k)
M_("blood-boil", rempl={"fatigue": ["épuisement"]})       # le texte dit épuisée, plus grave que fatiguée

# ---------- portée : « jusqu'à X mètres » est une Ampleur, non une Localisation (règle de Baptiste, 16 novembre 2026) ----------
AMPLEUR = {'angelic-wings', 'arcane-eye', 'arcane-sight', 'arcane-sight-greater', 'armor-of-darkness', 'ashen-path', 'bloodstone-mirror', 'bullhorn', 'burst-with-light',
           'cloak-of-light', 'darkvision', 'detect-creator', 'door-to-beyond', 'elemental-absorption', 'elemental-sense', 'elemental-sentinel', 'empathic-link',
           'er-assassins-approach', 'fires-pathway', 'flames-of-ego', 'fungal-hyphae', 'grasping-vine', 'grave-impressions', 'guardians-aegis', 'heatvision', 'hologram-cage',
           'hyperfocus', 'infectious-enthusiasm', 'levitate', 'life-connection', 'lifes-flowing-river', 'moths-supper', 'mystic-carriage', 'return-beacon', 'rewinding-step',
           'scrying-ripple', 'sentry-skull', 'shifting-form', 'speaking-sky', 'telekinesis', 'tempest-of-shades', 'tentacular-limbs', 'tether', 'tree-stride', 'tremorsense',
           'true-seeing', 'winning-streak'}
M_("seamantle", refait=True, plus=[
    ("plein", ["nage"], [], "une colonne d'eau m'enveloppe : je m'y déplace comme en nageant"),
    ("plein", ["abri"], [], "elle me protège des coups"),
    ("plein", ["extinction"], [], "elle arrête le feu et l'éteint au contact"),
    ("plein", ["coup"], [("AMPLEUR", 9, ["mètres"])], "je frappe d'un bras d'eau, jusqu'à 9 m")])
M_("fluid-form", refait=True, plus=[
    (10, ["rempart"], [], "mon corps comme liquide : les coups qui ne tranchent pas glissent dessus"),
    ("plein", ["allonge"], [("AMPLEUR", 3, ["mètres"])], "mes bras s'allongent, jusqu'à 3 m"),
    ("plein", ["passage"], [], "je passe par les fissures"),
    ("plein", ["nage"], [("LOCALISATION", 18, ["mètres"]), CHAQUE], "je nage"),
    ("plein", ["souffle"], [], "je respire l'eau comme l'air")])
# le lanceur (ou la cible) peut aller moins loin que le maximum : Ampleur ; un mouvement fixe reste une Localisation (règle de Baptiste)
AMPLEUR |= {'blink', 'fated-confrontation', 'blazing-dive', 'flowing-strike', 'flame-vortex', 'rouse-skeletons', 'earthbind', 'warping-pull', 'dive-and-breach',
            'airlift', 'hippocampus-retreat', 'dimensional-steps', 'unfolding-wind-crash', 'rising-surf', 'jump'}

# ---------- sorts à plusieurs usages au choix : complétés ou découpés en formes (validé par Baptiste, 16 novembre 2026) ----------
# Règle de Baptiste : une vulnérabilité ou une résistance ne veut rien dire seule — il faut dire à quoi (satellite Condition).
ALLURE = {"phantom-steed"}       # la distance est la vitesse du coursier
_AL = lambda m: [("LOCALISATION", m, ["mètres"]), CHAQUE]
for _p, _k in {
 "elemental-gift": {"cercle": {"vitesse": {"sur": ["vitesse"], "plus": [("plein", ["vol"], [], "il vole aussi vite qu'il marche")]},
                               "aplomb": {"sur": ["aplomb"], "plus": [("plein", ["gêne"], [], "le sol autour de lui gêne les autres")]}}},
 "tempest-form": {"cercle": {"nage": {"sur": ["nage"], "ajoute": ["invisibilité"]},
                             "voile": {"rempl": {"voile": ["flou"]}, "plus": [("plein", ["vol"], [], "je flotte dans l'air")]},
                             "souplesse": {"sur": ["souplesse"], "plus": [("plein", ["vol", "invisibilité"], [], "je vole, invisible dans les airs")]}}},
 "mantle-of-the-frozen-heart": {"cercle": {"griffe": {"sur": ["griffe"], "plus": [("plein", ["escalade"], [], "je grimpe comme je marche")]},
                                           "vitesse": {"sur": ["vitesse"], "plus": [("plein", ["aisance"], [K_("glace")], "la glace ne me gêne plus")]}}},
 "element-embodied": {"cercle": {"givre": {"ote": ["givre"], "sats": [K_("glace")]},
    "brûlure": {"ote": ["brûlure"], "sats": [CHAQUE]},
    "oiseau": {"ote": ["oiseau"], "sats": [("CIBLE", None, ["vol"])]}, "courant": {"ote": ["courant"], "sats": [("CIBLE", None, ["nage"])]},
    "chaleur": {"ote": ["chaleur"], "sats": [K_("feu")]},
    "vol": {"sur": ["vol"], "sats": _AL(24)}, "nage": {"sur": ["nage"], "sats": _AL(24)}, "creuser": {"sur": ["creuser"], "sats": _AL(6)}}},
 "elemental-motion": {"cercle": {"creuser": {"sur": ["creuser"], "sats": _AL(3)}}},
 "geniekind": {"sat_cond": ["foudre", "glace", "acide"], "cercle": {"chaleur": {"ote": ["chaleur"], "sats": [K_("feu")]},
    "vol": {"sur": ["vol"], "sats": _AL(18)}, "nage": {"sur": ["nage"], "sats": _AL(18)}, "creuser": {"sur": ["creuser"], "sats": _AL(18)}}},
 "rapid-adaptation": {"sat_cond": ["chaleur"], "cercle": {"givre": {"ote": ["givre"], "sats": [K_("glace")]},"flair": {"sur": ["flair"], "sats": [("AMPLEUR", 9, ["mètres"])]}}},
 "phantom-limb": {"cercle": {"nage": {"sur": ["nage"], "sats": _AL(18)}, "vol": {"sur": ["vol"], "sats": _AL(18)}}},
 "temporary-graft": {"cercle": {"nage": {"sur": ["nage"], "sats": _AL(12)}, "vol": {"sur": ["vol"], "sats": _AL(12)}}},
 "fire-shield": {"cercle": {"froid": {"ote": ["froid"], "sats": [K_("glace")]}, "feu": {"ote": ["feu"], "sats": [K_("feu")]}}},       # la résistance dit à quoi, par un satellite Condition
}.items(): M_(_p, **_k)
TABLE["fire-shield"].pop("sym", None); TABLE["fire-shield"]["ote"] = [w for w in TABLE["fire-shield"].get("ote", []) if w != "feu"]

# ---------- une résistance ou une vulnérabilité dit toujours à quoi (règle de Baptiste, 16 novembre 2026) ----------
_KK = lambda *m: ("CONDITION", "plein", list(m))
_VU = lambda *sats: {"rempl": {"faille": ["vulnérabilité"]}, "sats": list(sats)}
for _p, _k in {
 "barkskin": {"cercle": {"résistance": {"sur": ["résistance"], "sats": [_KK("choc", "perce")]}}},       # aux coups qui cognent et qui percent
 "gaseous-form": {"cercle": {"résistance": {"sur": ["résistance"], "sats": [K_("coup")]}}},
 "righteous-might": {"cercle": {"résistance": {"sur": ["résistance"], "sats": [K_("coup")]}}},
 "hallow": {"cercle": {"résistance": {"sur": ["résistance"], "sats": [_KK("énergie", "choix")]}, "vulnérabilité": {"sur": ["vulnérabilité"], "sats": [_KK("énergie", "choix")]}}},
 "thought-worm-i": {"cercle": {"faiblesse": {"rempl": {"faiblesse": ["vulnérabilité"]}, "sats": [("CIBLE", None, ["psyché"])]}}},
 "symbol-of-vulnerability": {"cercle": {"faiblesse": {"rempl": {"faiblesse": ["vulnérabilité"]}, "sats": [_KK("magie", "énergie")]}}},
 "pest-form": {"cercle": {"faille": _VU(K_("coup"))}}, "weaken-earth": {"cercle": {"faille": _VU(K_("coup"))}},
 "vitrifying-blast": {"cercle": {"faille": _VU(_KK("son", "choc"))}},
 "wish-twisted-form": {"cercle": {"faille": _VU(_KK("énergie", "choix"))}},
 "hallowed-ground": {"cercle": {"faille": _VU(K_("vie"))}},
 "elemental-gift": {"cercle": {"nage": {"sur": ["nage"], "sats": [K_("feu")]}}},
}.items(): M_(_p, **_k)
for _p, _k in {
 "fungal-infestation": {"cercle": {"faille": _VU(_KK("feu", "tranchant"))}},       # tant que le poison la ronge, le feu et les lames la blessent davantage
 "death-ward": {"cercle": {"résistance": {"sur": ["résistance"], "sym": ["tenebreux"]}}},       # contre l'énergie de la face ténébreuse
 "phantasmal-revenge": {"cercle": {"résistance": {"refait": True}}},       # ce cercle disait ce qu'elle subit en résistant : cela ne s'inscrit pas
}.items(): M_(_p, **_k)
# « bienveillant » entre au lexique (décision de Baptiste) : le pendant d'« hostile »
M_("litany-of-righteousness", cercle={"faiblesse": {"rempl": {"faiblesse": ["vulnérabilité"]}, "sats": [K_("bienveillant")]}})
# ce que reçoit l'hostile, ce que reçoit le bienveillant : chacun son cercle, chacun sa condition
TABLE["holy-whisper"] = {"refait": True, "plus": [
    ("plein", ["nausée"], [K_("hostile")], "la parole sainte soulève le cœur des êtres hostiles"),
    (9, [], [K_("hostile")], "2d8 en moyenne aux pires d'entre eux : êtres d'outre-plan, dragons, morts-vivants"),
    (2, ["ardeur"], [K_("bienveillant")], "2 ajouté aux coups des bienveillants, un instant")]}
TABLE["wake-of-light"] = {"refait": True, "cosm_plus": ["sillage"], "plus": [
    ("plein", ["aisance"], [K_("bienveillant")], "les bienveillants marchent sur la brume : le terrain pénible ne les freine plus"),
    ("plein", ["gêne"], [K_("hostile")], "la brume épaisse freine les hostiles")]}

# ── ordre des effets : les cercles d'Impact se lisent du centre vers l'extérieur, dans l'ordre où les effets se produisent ──
M_("dazzling-flash", ordre=["aveuglement", "éblouissement"])
M_("life-link", ordre=["regain", "partage"])
M_("sawtooth-terrain", ordre=["pointe", "saignement", "gêne"])

# ── effets au choix ou selon les cas (2026-11-16) : une forme par choix du lanceur ; un satellite Condition quand les circonstances décident ──
TABLE["cape-of-wasps"] = {"cercle": {
    "garde": {"refait": True, "plus": [("plein", ["dissimulation"], [], "l'essaim me cache des tirs"), (7, ["riposte", "dard", "poison"], [], "2d6 en moyenne à qui me frappe au corps à corps")]},
    "porteur": {"refait": True, "plus": [("plein", ["vol"], [("LOCALISATION", 6, ["mètres"]), CHAQUE], "l'essaim me porte, et ne me cache plus")]}}}
TABLE["barbed-chains"] = {"cosm": ["chaîne"], "rempl": {"chaîne": ["arme"]}, "ote": ["peur"], "valeur": 4, "forme": "chaîne",
    "cercle": {"renversement": {"ote": ["chaîne"], "forme": "chaîne"}},
    "plus": [("plein", ["peur"], [], "qui est touché prend peur")]}
M_("prismatic-spray", sat_cond=["rouge"])
TABLE["waters-of-lamashtu"] = {"refait": True, "plus": [("plein", ["difformité", "faiblesse"], [("SYM", "eau", [])], "une eau qui a l'air pure : qui la boit a l'esprit rongé et le corps déformé")]}
M_("call-the-blood", plus=[
    ("plein", ["nausée"], [("CONDITION", "plein", ["vivant"]), ("CIBLE", 1, [])], "vivant, j'en ai la nausée"),
    ("plein", ["hâte", "vigueur"], [("CONDITION", "plein", ["mort-vivant"]), ("CIBLE", 1, [])], "mort-vivant, j'y gagne force d'emprunt et vitesse")])
TABLE["impending-doom"] = {"toujours": True, "ordre": ["surprise", "effroi", "présage"], "plus": [
    ("plein", ["surprise"], [], "sa mort entrevue la prend au dépourvu"), (2, ["effroi"], [], "puis la peur monte")]}

# ── « imparable » (2026-11-16) : le sort ne laisse à la cible aucun moyen de s'y soustraire ni d'y résister ──
# page : (éditions concernées, cercles annotés). Éditions : 5e, 2024, 3.5, pf1, pf2, pf2r. Vérifié sur le texte d'origine de chaque édition.
_T = "5e 2024 3.5 pf1 pf2 pf2r"
IMPARABLE = {k: (set(e.split()), ou) for k, (e, ou) in {
 "power-word-kill": (_T, "premier"), "power-word-stun": (_T, "premier"), "power-word-blind": ("3.5 pf1 pf2 pf2r", "premier"), "maze": (_T, "premier"),
 "irresistible-dance": ("5e 3.5", "premier"), "forcecage": ("5e 2024 3.5", "premier"), "sleep": ("5e", "premier"), "color-spray": ("5e", "premier"),
 "divine-word": ("3.5", "premier"), "mark-of-justice": ("3.5 pf1", "premier"), "geas": ("3.5 pf1", "premier"),
 "waves-of-fatigue": ("3.5 pf1", "premier"), "scintillating-pattern": ("3.5 pf1", "premier"),
 "faerie-fire": ("3.5 pf1 pf2 pf2r", "premier"), "ice-storm": ("3.5 pf1", "chiffrés"), "symbol-of-vulnerability": ("pf1", "premier"),
 "reprobation": ("pf1", "premier"), "siphon-magic": ("pf1", "premier"), "litany-of-madness": ("pf1", "premier"), "litany-of-vengeance": ("pf1", "premier"),
 "sands-of-time": ("pf1", "premier"), "hags-seasoning": ("pf1", "premier"), "litany-of-eloquence": ("pf1", "premier"), "pernicious-poison": ("pf1", "premier"),
 "shared-suffering": ("pf1", "premier"), "litany-of-weakness": ("pf1", "premier"), "ill-omen": ("pf1", "premier"), "time-shudder": ("pf1", "premier"),
 "unbearable-brightness": ("pf1", "premier"), "euphoric-tranquility": ("pf1", "premier"),
 "fatal-aria": ("pf2 pf2r", "premier"), "elemental-betrayal": ("pf2 pf2r", "premier"), "dread-aura": ("pf2 pf2r", "premier"), "dirge-of-doom": ("pf2 pf2r", "premier"),
 "menacing-lament": ("pf2 pf2r", "premier"), "destructive-aura": ("pf2 pf2r", "premier"),
 "magic-missile": (_T, "premier"), "force-bolt": ("pf2 pf2r", "premier"),
}.items()}

# ── répétition (2026-11-17) : la source dit que la blessure ou le soin revient à chaque instant tant que le sort dure ──
# page : éditions concernées. Lot 1 : D&D 5 (et sa version 2024) et D&D 3.5, relus sur le texte d'origine ;
# les mêmes sorts dans Pathfinder 1 et 2 quand leur texte dit la même chose (sinon la version ne différerait que par un oubli).
_D5 = "5e 2024"; _PF = " pf1 pf2 pf2r"
REPETE = {k: set(e.split()) for k, e in {
 "flaming-sphere": _D5 + " 3.5" + _PF, "moonbeam": _D5, "spiritual-weapon": _D5 + " 3.5" + _PF, "call-lightning": _D5 + " 3.5" + _PF, "spirit-guardians": _D5,
 "vampiric-touch": _D5, "black-tentacles": _D5 + " 3.5 pf1", "control-water": _D5, "faithful-hound": _D5 + " 3.5 pf1", "wall-of-fire": _D5 + " 3.5" + _PF,
 "cloudkill": _D5 + " 3.5 pf1 pf2 pf2r", "insect-plague": _D5, "blade-barrier": _D5 + " pf2", "forbiddance": _D5, "sunbeam": _D5 + " 3.5 pf1", "wall-of-thorns": _D5,
 "arcane-sword": _D5 + " 3.5 pf1", "incendiary-cloud": _D5 + " 3.5 pf1", "heat-metal": _D5, "acid-fog": "3.5 pf1", "sympathetic-vibration": "3.5 pf1",
 # Pathfinder 1, relu sur le texte d'origine (2026-11-17)
 **{k: "pf1" for k in """terrible-remorse wreath-of-blades gebs-hammer ball-lightning burning-gaze contagious-flame elemental-aura firestream flashfire
   gusting-sphere hungry-darkness icy-prison lightning-lash scouring-winds spiritual-ally steam-ray-fusillade symbol-of-storms trial-of-fire-and-acid
   burning-sands fleshworm-infestation soothing-mud swarm-of-fangs boiling-blood excruciating-deformation polar-midnight snapdragon-fireworks
   strangling-hair tar-ball transmute-blood-to-acid aura-of-cannibalism blood-of-the-martyr fire-sneeze veil-of-ash jatembes-ire slough poison""".split()},
 # Pathfinder 2, relu sur le texte d'origine (2026-11-17) ; les quatre derniers : un mal persistant, qui dure jusqu'à cesser de lui-même
 **{k: "pf2 pf2r" for k in """ash-cloud petal-storm visions-of-danger shadow-army gasping-marsh spirit-link positive-attunement lifes-fresh-bloom
   field-of-life corrosive-muck devouring-void cinder-swarm rust-cloud phantom-orchestra whirlpool buzzing-bites hymn-of-healing ki-form
   sepulchral-mask interstellar-void diamond-dust door-to-beyond darklight invoke-spirits rouse-skeletons dancing-fountain flammable-fumes
   unblinking-flame-ignition enervation whispers-of-the-void blood-vendetta savor-the-sting incendiary-aura implement-of-destruction over-the-coals""".split()},
 "acid-arrow": "pf2",
}.items()}
REPETE_PREMIER = {"aura-of-cannibalism", "shadow-army", "ki-form", "sepulchral-mask", "flammable-fumes", "unblinking-flame-ignition"}       # seul le premier cercle chiffré revient à chaque instant
REPETE_SUITE = {"acid-arrow"}       # le premier coup ne revient pas : seul le cercle suivant (le mal persistant) porte le satellite
# ── la répétition par la distance (2026-11-17) : la blessure revient à chaque pas franchi, satellite Localisation 3 « chaque · mètres » et Quantité 2 « fractionné » (3/2 = 1,5 m) ──
REPETE_DISTANCE = {k: set(e.split()) for k, e in {"spike-growth": _D5 + " 3.5 pf1", "spike-stones": "3.5 pf1 pf2 pf2r", "binding-earth": "pf1", "coral-eruption": "pf2 pf2r"}.items()}
