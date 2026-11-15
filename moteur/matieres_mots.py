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
