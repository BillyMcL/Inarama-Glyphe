"""Fiches de conversion : ce que les données D&D ne disent pas (nom français, famille, verbe ou combinaison, cible, médium…).
Clés : fr, grimoire (titre d'un sort déjà validé), fam (A arcane / H hybride / R art rare), verb (pictogramme, négatif ?),
comb, why, art, cible, cible_obj, qty_cible, qty, cond, impact (valeur, médium, pourquoi), comp, consumed, cosm, loc, no_loc,
dur, forme, no_aoe, notes."""
V = lambda k, n=False: (k, n)
FICHES = {
# ===== Tours de magie =====
"acid-splash": dict(fr="Aspersion acide", cible=3, qty_cible=2),
"chill-touch": dict(fr="Contact glacial", verb=V("existence", True), cible=3, notes=["Malgré son nom, un dégât nécrotique : aucun élément, donc Arcane."]),
"dancing-lights": dict(fr="Lumières dansantes", verb=V("existence"), qty=4, cosm=("plein", "LUMIERE")),
"druidcraft": dict(fr="Druidisme", comb="Plante", why="la nature et les plantes", cible="plein"),
"eldritch-blast": dict(fr="Décharge occulte", verb=V("existence", True), cible=3, notes=["Dégât de force : la force brute de Détruire, sans médium."]),
"fire-bolt": dict(fr="Trait de feu", cible=3),
"guidance": dict(fr="Assistance", verb=V("intensite"), cible=2, impact=(3, "AIDE", "1d4")),
"light": dict(fr="Lumière", verb=V("visibilite"), cible=1, cible_obj=["OBJET"], cosm=("plein", "LUMIERE")),
"mage-hand": dict(fr="Main de mage", verb=V("mouvement"), cible=1, cible_obj=["OBJET"]),
"mending": dict(fr="Réparation", verb=V("ordre"), cible=1, cible_obj=["OBJET"]),
"message": dict(fr="Message", verb=V("relation"), cible=2),
"minor-illusion": dict(fr="Illusion mineure", verb=V("existence"), aoe={"type": "cube", "size": 5}, cosm=("plein", "IMAGE")),
"poison-spray": dict(fr="Bouffée de poison", cible=3),
"prestidigitation": dict(fr="Prestidigitation", verb=V("nature"), cible=1, cible_obj=["OBJET"]),
"produce-flame": dict(fr="Flammes", cible=1),
"ray-of-frost": dict(fr="Rayon de givre", cible=3),
"resistance": dict(fr="Résistance", verb=V("ordre"), cible=2, impact=(3, "GARDE", "1d4")),
"sacred-flame": dict(fr="Flamme sacrée", verb=V("existence", True), cible=3, notes=["Dégât radiant : de la lumière, pas du feu ; l'élément n'est pas en jeu."]),
"shillelagh": dict(fr="Gourdin magique", comb="Bois", why="le bois du gourdin", cible=1, cible_obj=["BATON"]),
"shocking-grasp": dict(fr="Poigne électrique", cible=3),
"spare-the-dying": dict(fr="Épargner les mourants", grimoire="Épargner les mourants"),
"thaumaturgy": dict(fr="Thaumaturgie", verb=V("intensite"), cible=1),
"true-strike": dict(fr="Coup au but", verb=V("visibilite"), cible=3),
"vicious-mockery": dict(fr="Moquerie cruelle", verb=V("existence", True), cible=3),
# ===== Niveau 1 =====
"alarm": dict(fr="Alarme", verb=V("visibilite"), cible="plein", cond=["INTRUS"]),
"animal-friendship": dict(fr="Amitié avec les animaux", verb=V("relation"), cible=3, cible_obj=["BETE"]),
"bane": dict(fr="Fléau", verb=V("intensite", True), cible=3, qty_cible=3, impact=(3, "CHANCE", "1d4")),
"bless": dict(fr="Bénédiction", verb=V("intensite"), cible=2, qty_cible=3, impact=(3, "CHANCE", "1d4")),
"burning-hands": dict(fr="Mains brûlantes", cible="plein"),
"charm-person": dict(fr="Charme-personne", grimoire="Charme-personne"),
"color-spray": dict(fr="Couleurs dansantes", verb=V("visibilite", True), cible="plein", impact=(33, None, "6d10 points de vie de créatures aveuglées")),
"command": dict(fr="Injonction", verb=V("relation"), cible=3, impact=("plein", "MOT", "un mot obéi entièrement")),
"comprehend-languages": dict(fr="Compréhension des langues", verb=V("visibilite"), cible=1),
"create-or-destroy-water": dict(fr="Création ou destruction d'eau", comb="Eau", why="l'eau"),
"cure-wounds": dict(fr="Soins", verb=V("existence"), cible=2, notes=["Comme la planche Soins : Créer rend au corps la forme qu'il porte."]),
"detect-evil-and-good": dict(fr="Détection du mal et du bien", verb=V("visibilite"), cible=9, notes=["Célestes, fiélons, morts-vivants : des êtres qui relèvent d'un plan (Cible 9)."]),
"detect-magic": dict(fr="Détection de la magie", grimoire="Détection de la magie"),
"detect-poison-and-disease": dict(fr="Détection des poisons et maladies", verb=V("visibilite"), cible=1, cible_obj=["POISON", "MALADIE"]),
"disguise-self": dict(fr="Déguisement", verb=V("visibilite", True), cible=1, cosm=("plein", "IMAGE")),
"divine-favor": dict(fr="Faveur divine", verb=V("intensite"), cible=1),
"entangle": dict(fr="Enchevêtrement", comb="Plante", why="les plantes", cible="plein"),
"expeditious-retreat": dict(fr="Repli expéditif", verb=V("mouvement"), cible=1),
"faerie-fire": dict(fr="Lueurs féeriques", verb=V("visibilite"), cible="plein", cosm=("plein", "LUMIERE")),
"false-life": dict(fr="Simulacre de vie", verb=V("existence"), cible=1),
"feather-fall": dict(fr="Feuille morte", verb=V("force", True), cible=2, qty_cible=5, cond=["CHUTE"]),
"find-familiar": dict(fr="Appel de familier", grimoire="Appel de familier"),
"floating-disk": dict(fr="Disque flottant", verb=V("existence"), forme=[("FORME", 9, [], "disque", [(90, "plein")]), ("AMPLEUR", 1, ["DIAMETRE", "METRES"], "1 m de diamètre")]),
"fog-cloud": dict(fr="Nappe de brouillard", comb="Brume", why="le brouillard", cible="plein"),
"goodberry": dict(fr="Baies nourricières", comb="Plante", why="les baies", cible=1, cible_obj=["BAIES"], qty_cible=9, impact=(1, None, "1 point de vie par baie"),
                  notes=["D&amp;D donne dix baies ; arrondi à 9 pour une seule forme."]),
"grease": dict(fr="Graisse", verb=V("existence"), cible="plein"),
"guiding-bolt": dict(fr="Éclair traçant", verb=V("existence", True), cible=3),
"healing-word": dict(fr="Mot de guérison", verb=V("existence"), cible=2),
"hellish-rebuke": dict(fr="Représailles infernales", cible=3, cond=["COUP"]),
"heroism": dict(fr="Héroïsme", verb=V("intensite"), cible=2, impact=(3, "COURAGE", "un courage qui se renouvelle (+3, le modificateur du lanceur)")),
"hideous-laughter": dict(fr="Fou rire", verb=V("ordre", True), cible=3),
"hunters-mark": dict(fr="Marque du chasseur", verb=V("visibilite"), cible=3, impact=(4, None, "1d6 à chaque coup")),
"identify": dict(fr="Identification", verb=V("visibilite"), cible=1, cible_obj=["OBJET"], comp=["PERLE"]),
"illusory-script": dict(fr="Écriture illusoire", verb=V("visibilite", True), cible=1, cible_obj=["ECRIT"], comp=["ENCRE"]),
"inflict-wounds": dict(fr="Blessure", verb=V("existence", True), cible=3, notes=["Comme la planche Blessure : 3d10 nécrotiques, 17 en moyenne."]),
"jump": dict(fr="Saut", verb=V("intensite"), cible=2, impact=(3, "SAUT", "la distance de saut triplée")),
"longstrider": dict(fr="Grande foulée", verb=V("mouvement"), cible=2, impact=(3, "PAS", "+3 m de vitesse")),
"mage-armor": dict(fr="Armure de mage", verb=V("existence"), cible=2, impact=(3, "GARDE", "une armure de force sur qui n'en porte pas (CA 13 + Dex : +3)")),
"magic-missile": dict(fr="Projectile magique", verb=V("existence", True), cible=3, impact=(3, None, "1d4 + 1 ; 3 comme sur la planche"), qty=3),
"protection-from-evil-and-good": dict(fr="Protection contre le mal et le bien", verb=V("relation", True), cible=2, comp=["ARGENT", "FER"]),
"purify-food-and-drink": dict(fr="Purification de nourriture et d'eau", verb=V("qualite"), cible=1, cible_obj=["NOURRITURE"], aoe={"type": "sphere", "size": 5}),
"sanctuary": dict(fr="Sanctuaire", verb=V("relation", True), cible=2, cond=["ATTAQUE"]),
"shield": dict(fr="Bouclier", grimoire="Bouclier"),
"shield-of-faith": dict(fr="Bouclier de la foi", verb=V("intensite"), cible=2, impact=(2, "GARDE", "plus difficile à atteindre (+2 à la CA)")),
"silent-image": dict(fr="Image silencieuse", grimoire="Image silencieuse"),
"sleep": dict(fr="Sommeil", verb=V("intensite", True), cible="plein", impact=(23, None, "5d8 points de vie de créatures endormies")),
"speak-with-animals": dict(fr="Communication avec les animaux", verb=V("relation"), cible=1),
"thunderwave": dict(fr="Vague tonnante", grimoire="Vague tonnante"),
"unseen-servant": dict(fr="Serviteur invisible", verb=V("existence")),
}

# ----- variantes des sorts du lot 1 : les deux pratiques inscrivent le même sort -----
FICHES["shield"]["alt"] = [dict(fam="A", verb=V("ordre"), cible=1, cond=["COUP"], impact=(5, "GARDE", "un écran qui détourne le coup (+5 à la CA)"), label="Forme arcane")]
FICHES["silent-image"]["alt"] = [dict(fam="A", verb=V("existence"), aoe={"type": "cube", "size": 15}, cosm=("plein", "IMAGE"), label="Forme arcane")]
FICHES["charm-person"]["alt"] = [dict(fam="A", verb=V("relation"), cible=3, label="Forme arcane")]
FICHES["thunderwave"]["alt"] = [dict(fam="H", comb="Orage", why="le tonnerre", cible="plein", label="Forme hybride")]

# ===== Niveau 2 =====
FICHES.update({
"acid-arrow": dict(fr="Flèche acide", cible=3),
"aid": dict(fr="Aide", verb=V("intensite"), cible=2, qty_cible=3, impact=(5, None, "+5 points de vie maximum")),
"alter-self": dict(fr="Modification d'apparence", verb=V("nature"), cible=1),
"animal-messenger": dict(fr="Messager animal", verb=V("relation"), cible=2, notes=["Une bête consentante : un allié."]),
"arcane-lock": dict(fr="Verrou magique", verb=V("ordre"), cible=1, cible_obj=["PORTE"], comp=["OR"]),
"arcanists-magic-aura": dict(fr="Aura magique", verb=V("visibilite", True), cible=1, cible_obj=["OBJET"]),
"augury": dict(fr="Augure", verb=V("visibilite"), comp=["OSSELETS"]),
"barkskin": dict(fr="Peau d'écorce", comb="Bois", why="l'écorce", cible=2, impact=(16, "GARDE", "une peau dure comme l'écorce (CA d'au moins 16)")),
"blindness-deafness": dict(fr="Cécité/surdité", verb=V("visibilite", True), cible=3),
"blur": dict(fr="Flou", verb=V("visibilite", True), cible=1),
"branding-smite": dict(fr="Châtiment marquant", verb=V("existence", True), cible=3, cond=["COUP"]),
"calm-emotions": dict(fr="Apaisement des émotions", verb=V("ordre"), cible="plein"),
"continual-flame": dict(fr="Flamme éternelle", comb="Feu", why="la flamme", cible=1, cible_obj=["OBJET"], comp=["RUBIS"]),
"darkness": dict(fr="Ténèbres", verb=V("visibilite", True), cible="plein"),
"darkvision": dict(fr="Vision dans le noir", verb=V("visibilite"), cible=2),
"detect-thoughts": dict(fr="Détection des pensées", verb=V("visibilite"), cible=3),
"enhance-ability": dict(fr="Amélioration des facultés", verb=V("intensite"), cible=2),
"enlarge-reduce": dict(fr="Agrandissement/rapetissement", grimoire="Agrandissement", label="Agrandir",
                       alt=[dict(grimoire="Rapetissement", label="Rapetisser")]),
"enthrall": dict(fr="Discours captivant", verb=V("relation"), cible=3),
"find-steed": dict(fr="Appel de destrier", verb=V("trame"), cible=7),
"find-traps": dict(fr="Détection des pièges", verb=V("visibilite"), cible=1, cible_obj=["PIEGE"]),
"flame-blade": dict(fr="Lame de feu", cible=1),
"flaming-sphere": dict(fr="Sphère de feu", cible="plein", aoe={"type": "sphere", "size": 2.5}),
"gentle-repose": dict(fr="Doux repos", grimoire="Doux repos"),
"gust-of-wind": dict(fr="Bourrasque", comb="Air", why="le vent", cible="plein"),
"heat-metal": dict(fr="Chauffer le métal", cible=1, cible_obj=["METAL"]),
"hold-person": dict(fr="Immobilisation de personne", grimoire="Immobilisation de personne"),
"invisibility": dict(fr="Invisibilité", grimoire="Invisibilité"),
"knock": dict(fr="Déblocage", verb=V("relation", True), cible=1, cible_obj=["SERRURE"]),
"lesser-restoration": dict(fr="Restauration partielle", grimoire="Restauration partielle"),
"levitate": dict(fr="Lévitation", grimoire="Lévitation"),
"locate-animals-or-plants": dict(fr="Localisation d'animaux ou de plantes", verb=V("visibilite"), cible=4, loc=(8, "KILOMETRES", "8 km (5 miles)")),
"locate-object": dict(fr="Localisation d'objet", verb=V("visibilite"), cible=4, loc=(300, "METRES", "300 m")),
"magic-mouth": dict(fr="Bouche magique", verb=V("existence"), cible=1, cible_obj=["OBJET"], cond=["PASSAGE"], comp=["JADE"]),
"magic-weapon": dict(fr="Arme magique", verb=V("intensite"), cible=1, cible_obj=["ARME"], impact=(1, "ARME", "+1")),
"mirror-image": dict(fr="Image miroir", grimoire="Image miroir"),
"misty-step": dict(fr="Foulée brumeuse", grimoire="Foulée brumeuse"),
"moonbeam": dict(fr="Rayon de lune", verb=V("existence", True), cible="plein"),
"pass-without-trace": dict(fr="Passage sans trace", verb=V("visibilite", True), cible=2, impact=(10, "DISCRETION", "+10 en discrétion")),
"prayer-of-healing": dict(fr="Prière de guérison", verb=V("existence"), cible=2, qty_cible=6),
"protection-from-poison": dict(fr="Protection contre le poison", comb="Ammoniac", why="le poison", cible=2),
"ray-of-enfeeblement": dict(fr="Rayon affaiblissant", verb=V("intensite", True), cible=3),
"rope-trick": dict(fr="Corde enchantée", fam="R", art="spatiomancie", verb=V("existence"), cible=1, cible_obj=["CORDE"],
                   notes=["Un espace extradimensionnel : de la spatiomancie."]),
"scorching-ray": dict(fr="Rayon ardent", grimoire="Rayon ardent",
                      alt=[dict(fam="H", comb="Feu", why="le feu", cible=3, qty_cible=3, label="Forme hybride")]),
"see-invisibility": dict(fr="Détection de l'invisibilité", verb=V("visibilite"), cible=1),
"shatter": dict(fr="Fracassement", cible="plein"),
"silence": dict(fr="Silence", verb=V("visibilite", True), cible="plein"),
"spider-climb": dict(fr="Pattes d'araignée", verb=V("force"), cible=2),
"spike-growth": dict(fr="Croissance d'épines", comb="Plante", why="les épines", cible="plein"),
"spiritual-weapon": dict(fr="Arme spirituelle", verb=V("existence"), cible=3),
"suggestion": dict(fr="Suggestion", verb=V("relation"), cible=3),
"warding-bond": dict(fr="Lien de protection", verb=V("relation"), cible=2, comp=["PLATINE"]),
"web": dict(fr="Toile d'araignée", verb=V("existence"), cible="plein"),
"zone-of-truth": dict(fr="Zone de vérité", verb=V("visibilite"), cible="plein"),
# ===== Niveau 3 =====
"animate-dead": dict(fr="Animation des morts", grimoire="Animation des morts"),
"beacon-of-hope": dict(fr="Lueur d'espoir", verb=V("intensite"), cible=2),
"bestow-curse": dict(fr="Malédiction", verb=V("qualite", True), cible=3),
"blink": dict(fr="Clignotement", fam="R", art="spatiomancie", verb=V("identite", True), cible=1, notes=["Un pied dans le plan éthéré : le corps se scinde entre deux places."]),
"call-lightning": dict(fr="Appel de la foudre", cible="plein"),
"clairvoyance": dict(fr="Clairvoyance", grimoire="Clairvoyance"),
"conjure-animals": dict(fr="Invocation d'animaux", verb=V("trame"), cible=7),
"counterspell": dict(fr="Contresort", verb=V("flux"), cond=["SORT"], notes=["Cible vide : c'est la trame elle-même, le sort adverse, qui est bue."]),
"create-food-and-water": dict(fr="Création de nourriture et d'eau", verb=V("existence"),
                              alt=[dict(fam="H", comb="Eau", why="l'eau", label="Forme hybride")]),
"daylight": dict(fr="Lumière du jour", verb=V("visibilite"), cible="plein", cosm=("plein", "LUMIERE")),
"dispel-magic": dict(fr="Dissipation de la magie", grimoire="Dissipation de la magie"),
"fear": dict(fr="Terreur", verb=V("force", True), cible="plein"),
"fireball": dict(fr="Boule de feu", cible="plein",
                 alt=[dict(fam="A", verb=V("existence", True), impact=(28, "FEU", "8d6 ; la planche commentée"), label="Forme arcane",
                           notes=["La version de la planche : Détruire, avec le feu en médium."])]),
"fly": dict(fr="Vol", verb=V("mouvement"), cible=2),
"gaseous-form": dict(fr="Forme gazeuse", comb="Brume", why="le corps fait brume", cible=2),
"glyph-of-warding": dict(fr="Glyphe de garde", verb=V("ordre"), cible="plein", cond=["PASSAGE"], comp=["DIAMANT"]),
"haste": dict(fr="Hâte", grimoire="Hâte"),
"hypnotic-pattern": dict(fr="Motif hypnotique", verb=V("mouvement", True), cible="plein", aoe={"type": "cube", "size": 30}, cosm=("plein", "IMAGE")),
"lightning-bolt": dict(fr="Éclair", grimoire="Éclair"),
"magic-circle": dict(fr="Cercle magique", verb=V("relation", True), cible=9, comp=["ARGENT", "FER"]),
"major-image": dict(fr="Image majeure", verb=V("existence"), aoe={"type": "cube", "size": 20}, cosm=("plein", "IMAGE"),
                    alt=[dict(fam="H", comb="Plasma", why="la lumière et le son de l'image", label="Forme hybride")]),
"mass-healing-word": dict(fr="Mot de guérison de groupe", verb=V("existence"), cible=2, qty_cible=6),
"meld-into-stone": dict(fr="Fusion dans la pierre", grimoire="Fusion dans la pierre"),
"nondetection": dict(fr="Antidétection", verb=V("visibilite", True), cible=2, comp=["DIAMANT"]),
"phantom-steed": dict(fr="Coursier fantôme", verb=V("existence")),
"plant-growth": dict(fr="Croissance végétale", comb="Plante", why="les plantes", cible="plein", aoe={"type": "sphere", "size": 100}),
"protection-from-energy": dict(fr="Protection contre l'énergie", verb=V("relation", True), cible=2),
"remove-curse": dict(fr="Délivrance des malédictions", verb=V("qualite"), cible=2),
"revivify": dict(fr="Retour à la vie", verb=V("existence"), cible=7, impact=(1, None, "revient avec 1 point de vie"), comp=["DIAMANT"]),
"sending": dict(fr="Communication à distance", verb=V("relation"), cible=2),
"sleet-storm": dict(fr="Tempête de neige", comb="Glace", why="la neige et le verglas", cible="plein"),
"slow": dict(fr="Lenteur", grimoire="Lenteur"),
"speak-with-dead": dict(fr="Communication avec les morts", verb=V("relation"), cible=7),
"speak-with-plants": dict(fr="Communication avec les plantes", comb="Plante", why="les plantes", cible="plein"),
"spirit-guardians": dict(fr="Esprits gardiens", verb=V("trame"), cible="plein", aoe={"type": "sphere", "size": 15}, impact=(14, "LUMIERE", "3d8 radiants")),
"stinking-cloud": dict(fr="Nuage puant", comb="Ammoniac", why="le gaz toxique", cible="plein"),
"tiny-hut": dict(fr="Petite hutte", verb=V("existence")),
"tongues": dict(fr="Don des langues", verb=V("relation"), cible=2),
"vampiric-touch": dict(fr="Caresse du vampire", verb=V("flux"), cible=3),
"water-breathing": dict(fr="Respiration aquatique", comb="Eau", why="l'eau", cible=2, qty_cible=9, notes=["Dix créatures dans D&amp;D ; arrondi à 9."]),
"water-walk": dict(fr="Marche sur l'onde", comb="Eau", why="l'eau", cible=2, qty_cible=9, notes=["Dix créatures dans D&amp;D ; arrondi à 9."]),
"wind-wall": dict(fr="Mur de vent", comb="Air", why="le vent", cible="plein"),
# ===== Niveau 4 =====
"arcane-eye": dict(fr="Œil magique", verb=V("visibilite")),
"banishment": dict(fr="Bannissement", grimoire="Bannissement"),
"black-tentacles": dict(fr="Tentacules noirs", verb=V("existence"), cible="plein"),
"blight": dict(fr="Flétrissement", verb=V("qualite", True), cible=3),
"compulsion": dict(fr="Coercition", verb=V("force"), cible=3),
"confusion": dict(fr="Confusion", grimoire="Confusion"),
"conjure-minor-elementals": dict(fr="Invocation d'élémentaires mineurs", comb="Air", why="les élémentaires", cible=9),
"conjure-woodland-beings": dict(fr="Invocation d'êtres sylvestres", verb=V("trame"), cible=9),
"control-water": dict(fr="Contrôle de l'eau", comb="Eau", why="l'eau", cible="plein"),
"death-ward": dict(fr="Protection contre la mort", verb=V("ordre"), cible=2, cond=["MORT"]),
"dimension-door": dict(fr="Porte dimensionnelle", grimoire="Porte dimensionnelle"),
"divination": dict(fr="Divination", verb=V("visibilite"), comp=["ENCENS"]),
"dominate-beast": dict(fr="Domination de bête", verb=V("relation"), cible=3, cible_obj=["BETE"]),
"fabricate": dict(fr="Fabrication", verb=V("nature"), cible=1, cible_obj=["MATIERE"]),
"faithful-hound": dict(fr="Molosse fidèle", verb=V("existence"), cond=["INTRUS"]),
"fire-shield": dict(fr="Bouclier de feu", cible=1, cond=["COUP"], label="Bouclier ardent",
                    alt=[dict(comb="Glace", why="le froid", impact=(9, "FROID", "2d8"), label="Bouclier glacé")]),
"freedom-of-movement": dict(fr="Liberté de mouvement", verb=V("mouvement"), cible=2),
"giant-insect": dict(fr="Insecte géant", verb=V("intensite"), cible=1, cible_obj=["INSECTE"]),
"greater-invisibility": dict(fr="Invisibilité supérieure", verb=V("visibilite", True), cible=2),
"guardian-of-faith": dict(fr="Gardien de la foi", verb=V("trame"), cible="plein", impact=(20, "LUMIERE", "20 radiants")),
"hallucinatory-terrain": dict(fr="Terrain hallucinatoire", verb=V("visibilite", True), cible="plein"),
"ice-storm": dict(fr="Tempête de grêle", comb="Glace", why="la grêle", cible="plein", impact=(14, "FROID", "4d6 de froid (et 2d8 contondants)")),
"locate-creature": dict(fr="Localisation de créature", verb=V("visibilite"), cible=4, loc=(300, "METRES", "300 m")),
"phantasmal-killer": dict(fr="Assassin imaginaire", verb=V("existence", True), cible=3),
"polymorph": dict(fr="Métamorphose", grimoire="Métamorphose"),
"private-sanctum": dict(fr="Sanctuaire privé", verb=V("relation", True), cible="plein"),
"resilient-sphere": dict(fr="Sphère résiliente", verb=V("existence"), cible=3, aoe={"type": "sphere", "size": 5}),
"secret-chest": dict(fr="Coffre secret", fam="R", art="spatiomancie", verb=V("visibilite", True), cible=1, cible_obj=["COFFRE"], comp=["COFFRE"],
                     notes=["Le coffre est caché dans le plan éthéré : de la spatiomancie."]),
"stone-shape": dict(fr="Façonnage de la pierre", comb="Roche", why="la pierre", cible=1, cible_obj=["PIERRE"]),
"stoneskin": dict(fr="Peau de pierre", comb="Roche", why="la pierre", cible=2, comp=["DIAMANT"]),
"wall-of-fire": dict(fr="Mur de feu", cible="plein"),
})

# ===== Niveaux 5 à 9 =====
FICHES.update({
"animate-objects": dict(fr="Animation des objets", verb=V("nature"), cible=1, cible_obj=["OBJET"], qty_cible=9, notes=["Dix objets dans D&amp;D ; arrondi à 9."]),
"antilife-shell": dict(fr="Coquille antivie", verb=V("force", True), cible="plein"),
"arcane-hand": dict(fr="Main magique", verb=V("existence"), cible=3, impact=(18, None, "4d8 de force")),
"awaken": dict(fr="Éveil", verb=V("nature"), cible=1, cible_obj=["BETE"], comp=["AGATE"]),
"cloudkill": dict(fr="Brume mortelle", cible="plein"),
"commune": dict(fr="Communion", verb=V("relation"), cible=9, notes=["Une divinité : hors barème dans le canon, la Cible 9 est ce qui s'en approche le plus."]),
"commune-with-nature": dict(fr="Communion avec la nature", comb="Plante", why="la nature", cible="plein", loc=(5, "KILOMETRES", "5 km (3 miles)")),
"cone-of-cold": dict(fr="Cône de froid", cible="plein"),
"conjure-elemental": dict(fr="Invocation d'élémentaire", grimoire="Invocation d'élémentaire"),
"contact-other-plane": dict(fr="Contact avec un autre plan", verb=V("relation"), cible=9),
"contagion": dict(fr="Contagion", grimoire="Contagion"),
"creation": dict(fr="Création", verb=V("existence"), cible=1, cible_obj=["OBJET"]),
"dispel-evil-and-good": dict(fr="Dissipation du mal et du bien", verb=V("trame", True), cible=9),
"dominate-person": dict(fr="Domination de personne", verb=V("relation"), cible=3),
"dream": dict(fr="Songe", verb=V("relation"), cible=2, loc=("plein", None, "n'importe où sur le même plan")),
"flame-strike": dict(fr="Colonne de flamme", cible="plein"),
"geas": dict(fr="Quête", verb=V("relation"), cible=3),
"greater-restoration": dict(fr="Restauration supérieure", verb=V("qualite"), cible=2, comp=["DIAMANT"]),
"hallow": dict(fr="Sanctification", verb=V("qualite"), cible="plein", comp=["ENCENS"]),
"hold-monster": dict(fr="Immobilisation de monstre", verb=V("mouvement", True), cible=3),
"insect-plague": dict(fr="Fléau d'insectes", verb=V("existence"), cible="plein"),
"legend-lore": dict(fr="Mythes et légendes", verb=V("visibilite"), comp=["ENCENS"]),
"mass-cure-wounds": dict(fr="Soins de groupe", verb=V("existence"), cible=2, qty_cible=6, no_aoe=True),
"mislead": dict(fr="Double illusoire", verb=V("identite", True), cible=1),
"modify-memory": dict(fr="Modification de mémoire", verb=V("nature"), cible=3),
"passwall": dict(fr="Passe-muraille", fam="R", art="spatiomancie", verb=V("existence"), cible=1, cible_obj=["MUR"], notes=["Un passage creusé dans l'espace d'un mur : de la spatiomancie."]),
"planar-binding": dict(fr="Lien planaire", verb=V("relation"), cible=9, comp=["JOYAU"]),
"raise-dead": dict(fr="Rappel à la vie", verb=V("existence"), cible=7, comp=["DIAMANT"]),
"reincarnate": dict(fr="Réincarnation", verb=V("nature"), cible=7, comp=["HUILE"]),
"scrying": dict(fr="Scrutation", verb=V("visibilite"), cible=4, loc=("plein", None, "n'importe où sur le même plan"), comp=["CRISTAL"]),
"seeming": dict(fr="Apparence trompeuse", verb=V("visibilite", True), cible=2, qty_cible=9),
"telekinesis": dict(fr="Télékinésie", verb=V("mouvement"), cible=3, no_aoe=True),
"telepathic-bond": dict(fr="Lien télépathique", grimoire="Lien télépathique"),
"teleportation-circle": dict(fr="Cercle de téléportation", fam="R", art="spatiomancie", verb=V("relation"), cible="plein", comp=["CRAIE", "ENCRE"]),
"tree-stride": dict(fr="Voyage par les arbres", fam="R", art="spatiomancie", verb=V("mouvement"), cible=1, notes=["D'un arbre à l'autre : de la spatiomancie qui prend appui sur les plantes."]),
"wall-of-force": dict(fr="Mur de force", grimoire="Mur de force"),
"wall-of-stone": dict(fr="Mur de pierre", comb="Roche", why="la pierre"),
"blade-barrier": dict(fr="Barrière de lames", verb=V("existence"), cible="plein"),
"chain-lightning": dict(fr="Chaîne d'éclairs", cible=3, qty_cible=4),
"circle-of-death": dict(fr="Cercle de mort", verb=V("existence", True), cible="plein", comp=["PERLE"]),
"conjure-fey": dict(fr="Invocation de fée", verb=V("trame"), cible=9),
"contingency": dict(fr="Contingence", verb=V("ordre"), cible=1, cond=["DECLENCHEUR"], comp=["STATUETTE"]),
"create-undead": dict(fr="Création de mort-vivant", comb="Sang", why="le sang rendu aux morts, comme pour l'Animation des morts", cible=7, qty_cible=3, comp=["ONYX"]),
"disintegrate": dict(fr="Désintégration", grimoire="Désintégration"),
"eyebite": dict(fr="Mauvais œil", verb=V("qualite", True), cible=3),
"find-the-path": dict(fr="Découverte du chemin", verb=V("visibilite"), cible=4, comp=["OSSELETS"]),
"flesh-to-stone": dict(fr="Chair en pierre", grimoire="Chair en pierre"),
"forbiddance": dict(fr="Interdiction", verb=V("relation", True), cible="plein", aoe={"type": "cube", "size": 200}, comp=["RUBIS"],
                    notes=["D&amp;D donne une surface de 40 000 pieds carrés ; ramenée à un cube de 60 m de côté."]),
"freezing-sphere": dict(fr="Sphère glacée", cible="plein"),
"globe-of-invulnerability": dict(fr="Globe d'invulnérabilité", verb=V("relation", True), notes=["Cible vide : c'est la trame, les sorts eux-mêmes, qui est tenue à l'écart."]),
"guards-and-wards": dict(fr="Protections et sceaux", verb=V("ordre"), cible="plein", aoe={"type": "cube", "size": 50}, comp=["ARGENT"],
                         notes=["D&amp;D donne une surface de 2 500 pieds carrés ; ramenée à un cube de 15 m de côté."]),
"harm": dict(fr="Mise à mal", verb=V("existence", True), cible=3),
"heal": dict(fr="Guérison", verb=V("existence"), cible=2),
"heroes-feast": dict(fr="Festin des héros", verb=V("existence"), cible=2, qty_cible=9, comp=["COUPE"], notes=["Douze convives dans D&amp;D ; arrondi à 9."]),
"instant-summons": dict(fr="Convocation instantanée", fam="R", art="spatiomancie", verb=V("mouvement"), cible=1, cible_obj=["OBJET"], cond=["MOT"], comp=["SAPHIR"]),
"irresistible-dance": dict(fr="Danse irrésistible", verb=V("ordre", True), cible=3),
"magic-jar": dict(fr="Possession", verb=V("identite", True), cible=1, comp=["GEMME"]),
"mass-suggestion": dict(fr="Suggestion de groupe", verb=V("relation"), cible=3, qty_cible=9, notes=["Douze créatures dans D&amp;D ; arrondi à 9."]),
"move-earth": dict(fr="Façonnage de la terre", comb="Terre", why="la terre"),
"planar-ally": dict(fr="Allié planaire", verb=V("trame"), cible=9),
"programmed-illusion": dict(fr="Illusion programmée", verb=V("existence"), cond=["DECLENCHEUR"], cosm=("plein", "IMAGE"), comp=["JADE"]),
"sunbeam": dict(fr="Rayon de soleil", verb=V("existence", True), cible="plein"),
"transport-via-plants": dict(fr="Voie végétale", fam="R", art="spatiomancie", verb=V("relation"), cible=1, notes=["Deux plantes liées en un passage : de la spatiomancie."]),
"true-seeing": dict(fr="Vision lucide", verb=V("visibilite"), cible=2, comp=["ONGUENT"]),
"wall-of-ice": dict(fr="Mur de glace", cible="plein"),
"wall-of-thorns": dict(fr="Mur d'épines", comb="Plante", why="les épines", cible="plein"),
"wind-walk": dict(fr="Marche sur le vent", comb="Air", why="le corps fait nuée", cible=2, qty_cible=9, notes=["Dix créatures dans D&amp;D ; arrondi à 9."]),
"word-of-recall": dict(fr="Mot de rappel", fam="R", art="spatiomancie", verb=V("mouvement"), cible=2, qty_cible=5, no_aoe=True),
"arcane-sword": dict(fr="Épée magique", verb=V("existence"), cible=3, comp=["EPEE"]),
"conjure-celestial": dict(fr="Invocation de céleste", verb=V("trame"), cible=9),
"delayed-blast-fireball": dict(fr="Boule de feu à explosion retardée", cible="plein", cond=["CONTACT"]),
"divine-word": dict(fr="Mot divin", verb=V("trame", True), cible=3),
"etherealness": dict(fr="Forme éthérée", fam="R", art="spatiomancie", verb=V("mouvement"), cible=1),
"finger-of-death": dict(fr="Doigt de mort", verb=V("existence", True), cible=3),
"fire-storm": dict(fr="Tempête de feu", cible="plein"),
"forcecage": dict(fr="Cage de force", verb=V("existence"), cible=3, comp=["RUBIS"]),
"magnificent-mansion": dict(fr="Manoir somptueux", fam="R", art="spatiomancie", verb=V("existence"), no_aoe=True),
"mirage-arcane": dict(fr="Mirage", verb=V("visibilite", True), cible="plein"),
"plane-shift": dict(fr="Changement de plan", fam="R", art="spatiomancie", verb=V("mouvement"), cible=2, qty_cible=8, comp=["DIAPASON"]),
"prismatic-spray": dict(fr="Embruns prismatiques", verb=V("existence", True), cible="plein", cosm=("plein", "COULEURS"),
                        notes=["Sept rayons de sept natures : aucun élément ne domine, l'Arcane les porte tous par la lumière."]),
"project-image": dict(fr="Projection d'image", verb=V("existence"), cosm=("plein", "IMAGE"), comp=["STATUETTE"]),
"regenerate": dict(fr="Régénération", verb=V("existence"), cible=2),
"resurrection": dict(fr="Résurrection", verb=V("existence"), cible=7, comp=["DIAMANT"]),
"reverse-gravity": dict(fr="Inversion de la gravité", verb=V("force", True), cible="plein"),
"sequester": dict(fr="Séquestration", verb=V("visibilite", True), cible=1, comp=["DIAMANT"]),
"simulacrum": dict(fr="Simulacre", comb="Glace", why="la neige dont le double est fait", comp=["RUBIS"]),
"symbol": dict(fr="Symbole", grimoire="Symbole"),
"teleport": dict(fr="Téléportation", grimoire="Téléportation"),
"animal-shapes": dict(fr="Formes animales", verb=V("nature"), cible=2, qty_cible=9),
"antimagic-field": dict(fr="Champ antimagie", verb=V("relation", True), notes=["Cible vide : la trame elle-même est tenue à l'écart."]),
"antipathy-sympathy": dict(fr="Antipathie/sympathie", verb=V("force", True), cible=1, cible_obj=["OBJET"], label="Antipathie",
                           alt=[dict(verb=V("force"), label="Sympathie")]),
"clone": dict(fr="Clone", verb=V("identite", True), cible=2, comp=["DIAMANT"]),
"control-weather": dict(fr="Contrôle du climat", comb="Tempête", why="le temps qu'il fait", cible="plein", loc=(8, "KILOMETRES", "8 km (5 miles)")),
"demiplane": dict(fr="Demi-plan", fam="R", art="spatiomancie", verb=V("existence")),
"dominate-monster": dict(fr="Domination de monstre", verb=V("relation"), cible=3),
"earthquake": dict(fr="Tremblement de terre", comb="Terre", why="la terre", cible="plein"),
"feeblemind": dict(fr="Débilité", verb=V("intensite", True), cible=3),
"glibness": dict(fr="Éloquence", verb=V("intensite"), cible=1),
"holy-aura": dict(fr="Aura sacrée", verb=V("ordre"), cible=2, comp=["RELIQUAIRE"]),
"incendiary-cloud": dict(fr="Nuage incendiaire", cible="plein"),
"maze": dict(fr="Labyrinthe", fam="R", art="spatiomancie", verb=V("trame", True), cible=3),
"mind-blank": dict(fr="Esprit impénétrable", verb=V("visibilite", True), cible=2),
"power-word-stun": dict(fr="Mot de pouvoir étourdissant", verb=V("mouvement", True), cible=3, impact=(150, None, "150 points de vie ou moins")),
"sunburst": dict(fr="Explosion solaire", verb=V("existence", True), cible="plein"),
"astral-projection": dict(fr="Projection astrale", verb=V("identite", True), cible=2, qty_cible=8, comp=["JACINTHE"]),
"foresight": dict(fr="Prémonition", fam="R", art="chronomancie", verb=V("visibilite"), cible=2, notes=["Voir l'instant d'après : la perception, domaine de la chronomancie."]),
"gate": dict(fr="Portail", fam="R", art="spatiomancie", verb=V("relation"), cible=9, comp=["DIAMANT"]),
"imprisonment": dict(fr="Emprisonnement", verb=V("mouvement", True), cible=3, comp=["STATUETTE"]),
"mass-heal": dict(fr="Guérison de groupe", verb=V("existence"), cible=2),
"meteor-swarm": dict(fr="Nuée de météores", comb="Lave", why="le feu et la roche des météores", cible="plein", qty=4),
"power-word-kill": dict(fr="Mot de pouvoir mortel", verb=V("existence", True), cible=3, impact=(100, None, "100 points de vie ou moins")),
"prismatic-wall": dict(fr="Mur prismatique", verb=V("relation", True), cosm=("plein", "COULEURS")),
"shapechange": dict(fr="Changement de forme", verb=V("nature"), cible=1, comp=["DIADEME"]),
"storm-of-vengeance": dict(fr="Tempête vengeresse", cible="plein"),
"time-stop": dict(fr="Arrêt du temps", fam="R", art="chronomancie", verb=V("mouvement", True), cible=1,
                  notes=["Ancrer, et non Corrompre : ici le temps s'arrête vraiment, comme on l'avait réservé à ce verbe."]),
"true-polymorph": dict(fr="Métamorphose suprême", verb=V("nature"), cible=3),
"true-resurrection": dict(fr="Résurrection suprême", verb=V("existence"), cible=7, comp=["DIAMANT"]),
"weird": dict(fr="Ennemi subconscient", verb=V("existence", True), cible="plein", impact=(22, "ESPRIT", "4d10 psychiques")),
})

# ===== Deuxième passe : le même sort dans l'autre pratique =====
A = lambda k, n=False, **kw: {"fam": "A", "verb": V(k, n), "label": "Forme arcane", **kw}
H = lambda comb, why, **kw: {"fam": "H", "comb": comb, "why": why, "label": "Forme hybride", **kw}
SANG = "le fluide vital"
VIE = "le sang qu'on retire"
LUM = "la lumière"
ILL = "la lumière qui trompe l'œil"
ALT2 = {
 # --- l'élément porté comme médium par l'énergie pure : forme arcane ---
 "acid-splash": [A("existence", True)], "fire-bolt": [A("existence", True)], "poison-spray": [A("existence", True)],
 "ray-of-frost": [A("existence", True)], "shocking-grasp": [A("existence", True)], "produce-flame": [A("existence")],
 "burning-hands": [A("existence", True)], "hellish-rebuke": [A("existence", True)], "acid-arrow": [A("existence", True)],
 "flame-blade": [A("existence")], "flaming-sphere": [A("existence")],
 "heat-metal": [A("nature", notes=["Le canon le dit lui-même : Transformer avec le feu réchauffe."])],
 "shatter": [A("existence", True)], "cone-of-cold": [A("existence", True)], "flame-strike": [A("existence", True)],
 "chain-lightning": [A("existence", True)], "freezing-sphere": [A("existence", True)], "wall-of-fire": [A("existence")],
 "delayed-blast-fireball": [A("existence", True)], "fire-storm": [A("existence", True)], "fire-shield": [A("force", True)],
 "continual-flame": [A("existence", cosm=("plein", "LUMIERE"), notes=["Une flamme sans chaleur : de la lumière, que l'Arcane sait créer seul."])],
 "gust-of-wind": [A("force", True, notes=["Une poussée sans vent : la force directionnelle seule."])],
 "wind-wall": [A("force", True)],
 "protection-from-poison": [A("relation", True)],
 "speak-with-plants": [A("relation")],
 "commune-with-nature": [A("visibilite")],
 "lightning-bolt": [A("existence", True, cible="plein")],
 "clairvoyance": [A("visibilite", cible=4)],
 # --- une combinaison naturelle porte l'effet : forme hybride ---
 "cure-wounds": [H("Sang", SANG)], "healing-word": [H("Sang", SANG)], "prayer-of-healing": [H("Sang", SANG)],
 "mass-healing-word": [H("Sang", SANG)], "mass-cure-wounds": [H("Sang", SANG)], "heal": [H("Sang", SANG)],
 "mass-heal": [H("Sang", SANG)], "regenerate": [H("Sang", SANG)], "false-life": [H("Sang", SANG)],
 "revivify": [H("Sang", SANG)], "raise-dead": [H("Sang", SANG)], "resurrection": [H("Sang", SANG)], "true-resurrection": [H("Sang", SANG)],
 "spare-the-dying": [H("Sang", SANG, cible=2)],
 "chill-touch": [H("Sang", VIE)], "inflict-wounds": [H("Sang", VIE)], "vampiric-touch": [H("Sang", VIE)],
 "harm": [H("Sang", VIE)], "finger-of-death": [H("Sang", VIE)], "circle-of-death": [H("Sang", VIE)],
 "blight": [H("Plante", "la sève qui se flétrit")],
 "light": [H("Plasma", LUM)], "dancing-lights": [H("Plasma", LUM)], "faerie-fire": [H("Plasma", LUM)], "daylight": [H("Plasma", LUM)],
 "guiding-bolt": [H("Plasma", LUM)], "moonbeam": [H("Plasma", LUM)], "sunbeam": [H("Feu", "le feu du soleil")],
 "sunburst": [H("Feu", "le feu du soleil")], "sacred-flame": [H("Feu", "la flamme")],
 "minor-illusion": [H("Plasma", ILL)], "disguise-self": [H("Plasma", ILL)], "blur": [H("Plasma", ILL)],
 "invisibility": [H("Plasma", ILL, cible=2)], "greater-invisibility": [H("Plasma", ILL)], "mirror-image": [H("Plasma", ILL, cible=1, impact=(3, "IMAGE", "trois doubles"))],
 "hypnotic-pattern": [H("Plasma", ILL)], "color-spray": [H("Plasma", ILL)], "hallucinatory-terrain": [H("Plasma", ILL)],
 "seeming": [H("Plasma", ILL)], "mislead": [H("Plasma", ILL)], "programmed-illusion": [H("Plasma", ILL)],
 "project-image": [H("Plasma", ILL)], "mirage-arcane": [H("Plasma", ILL)],
 "silence": [H("Air", "l'air qui ne porte plus le son")],
 "fly": [H("Air", "l'air qui porte")], "feather-fall": [H("Air", "l'air qui porte")], "jump": [H("Air", "l'air qui porte")],
 "levitate": [H("Air", "l'air qui porte", cible=2, notes=["La version arcane est celle du grimoire."])],
 "sleep": [H("Pollen", "ce qui se respire et assoupit")], "calm-emotions": [H("Pollen", "ce qui se respire et apaise")],
 "meld-into-stone": [H("Roche", "la pierre", cible=1)],
 "gentle-repose": [H("Sel gemme", "le sel qui conserve", cible=4, cible_obj=["CORPS"], comp=["SEL"])],
 "purify-food-and-drink": [H("Eau", "l'eau purifiée")],
}
for k, alts in ALT2.items():
    FICHES[k].setdefault("alt", [])
    FICHES[k]["alt"] += alts

# ===== Passe d'encodage fin — lot 1 : Enchantement =====
# Ce qui fait d'un sort un sort à part s'inscrit dans le glyphe : nature de l'effet (Impact), restrictions de cible (Condition),
# conditions de fin (annotation de la Durée), seuils (satellite annoté de la Condition).
P = "plein"
LOT1 = {
"vicious-mockery": dict(impact=(3, ["ESPRIT", "MALADRESSE"], "1d4 en moyenne, puis une attaque maladroite"), cond=["ECOUTE"]),
"animal-friendship": dict(cible_obj=[], cond=["BETE", "INSTINCT"], impact=(P, ["CHARME"], "charmée entièrement"), fin=["OFFENSE"]),
"bane": dict(impact=(3, ["CHANCE", "COUP", "RESISTANCE"], "les coups moins sûrs, la résistance amoindrie (1d4 retranché aux attaques et aux sauvegardes)")),
"bless": dict(impact=(3, ["CHANCE", "COUP", "RESISTANCE"], "les coups plus sûrs, la résistance affermie (1d4 ajouté aux attaques et aux sauvegardes)")),
"charm-person": dict(grimoire=None, fam="H", comb="Pollen", why="ce qui se respire et charme", cible=3,
                     cond=["HUMANOIDE"], impact=(P, ["CHARME"], "charmée entièrement"), fin=["OFFENSE"]),
"command": dict(cond=["COMPREHENSION", "VIVANT"]),
"heroism": dict(impact=(3, ["VIE", "TEMPORAIRE"], "un courage qui se renouvelle sans cesse (+3 points de vie temporaires par tour)"), impact_sats=[(P, ["INTREPIDITE"])]),
"hideous-laughter": dict(cond=["RAISON"], impact=(P, ["RIRE", "CHUTE"], "à terre, secouée de rire")),
"sleep": dict(impact=(23, ["SOMMEIL", "VIE"], "5d8 points de vie de créatures endormies"), cond=["VIVANT"], fin=["BLESSURE", "REVEIL"]),
"animal-messenger": dict(cond=["BETE", "MINUSCULE"], impact=(P, ["MESSAGE"], "le message porté"), impact_sats=[(25, ["MOTS"])]),
"calm-emotions": dict(cond=["HUMANOIDE"], impact=(P, ["CALME", "CHARME", "PEUR", "HOSTILITE"], "charme et peur suspendus, ou hostilité éteinte")),
"enthrall": dict(qty_cible=P, cond=["ECOUTE"], impact=(P, ["CAPTIVATION"], "l'attention prise"), fin=["SILENCE"]),
"hold-person": dict(grimoire=None, verb=V("mouvement", True), cible=3, cond=["HUMANOIDE"], impact=(P, ["PARALYSIE"], "paralysée")),
"suggestion": dict(cond=["ECOUTE", "COMPREHENSION"], impact=(P, ["CONDUITE"], "la conduite suggérée, suivie")),
"zone-of-truth": dict(impact=(P, ["VERITE"], "aucun mensonge délibéré")),
"compulsion": dict(qty_cible=P, cond=["ECOUTE"], impact=(P, ["MARCHE"], "la marche dans la direction désignée")),
"confusion": dict(grimoire=None, verb=V("ordre", True), cible=P, impact=(P, ["FOLIE"], "conduite livrée au hasard")),
"dominate-beast": dict(cible_obj=[], cond=["BETE"], impact=(P, ["DOMINATION", "LIEN"], "charmée, liée par télépathie")),
"dominate-person": dict(cond=["HUMANOIDE"], impact=(P, ["DOMINATION", "LIEN"], "charmée, liée par télépathie")),
"geas": dict(cond=["COMPREHENSION"], impact=(P, ["SERMENT"], "le service imposé"), impact_sats=[(28, ["ESPRIT"])]),
"hold-monster": dict(cond=["VIVANT"], impact=(P, ["PARALYSIE"], "paralysée")),
"modify-memory": dict(cond=["SOUVENIR"], cond_sats=[(1, ["JOUR"])], impact=(P, ["MEMOIRE"], "un souvenir effacé, ravivé ou réécrit"), fin=["BLESSURE"]),
"irresistible-dance": dict(impact=(P, ["DANSE"], "la danse sur place")),
"mass-suggestion": dict(qty_cible=12, notes=[], cond=["ECOUTE", "COMPREHENSION"], impact=(P, ["CONDUITE"], "la conduite suggérée, suivie")),
"antipathy-sympathy": dict(cible=P, cible_obj=[], cond=["ESPECE"], impact=(P, ["REPULSION", "PEUR"], "fuir la cible, effrayée")),
"dominate-monster": dict(impact=(P, ["DOMINATION", "LIEN"], "charmée, liée par télépathie")),
"feeblemind": dict(impact=(14, ["ESPRIT"], "4d6 en moyenne"), impact_sats=[(P, ["INTELLECT"])], dur=(P, None)),
"power-word-stun": dict(cond=["PAROLE", "SEUIL"], cond_sats=[(150, ["VIE"])], impact=(P, ["ETOURDISSEMENT"], "étourdie")),
"power-word-kill": dict(cond=["PAROLE", "SEUIL"], cond_sats=[(100, ["VIE"])], impact=(P, ["MORT"], "morte")),
}
for k, upd in LOT1.items():
    FICHES[k].update(upd)
    for key in ("grimoire", "cible_obj"):
        if not FICHES[k].get(key): FICHES[k].pop(key, None)
FICHES["antipathy-sympathy"]["alt"][0]["impact"] = (P, ["ATTRACTION"], "rester près de la cible, irrésistiblement")

# ===== lot 2 : Divination =====
def apply(lot):
    for k, upd in lot.items():
        alt_upd = upd.pop("_alt", None)
        FICHES[k].update(upd)
        for key in ("grimoire", "cible_obj", "notes"):
            if key in FICHES[k] and not FICHES[k][key]: FICHES[k].pop(key)
        if alt_upd:
            for a, au in zip(FICHES[k].get("alt", []), alt_upd): a.update(au)
LOT2 = {
"guidance": dict(impact=(3, ["CHANCE", "APTITUDE"], "un coup de pouce à ce qu'on entreprend (1d4 ajouté à un test)"), fin=["USAGE"]),
"true-strike": dict(impact=(P, ["FAILLE"], "la défense percée à jour"), fin=["COUP"]),
"comprehend-languages": dict(impact=(P, ["SENS", "LANGUE"], "le sens littéral de toute langue")),
"detect-evil-and-good": dict(cible_note=["ABERRATION", "CELESTE", "ELEMENTAIRE", "FEE", "FIELON", "MORTVIVANT"], impact=(P, ["PRESENCE", "LIEU"], "présence et position")),
"detect-magic": dict(impact=(P, ["AURA", "ECOLE"], "l'aura et l'école de la magie")),
"detect-poison-and-disease": dict(cible=P, cible_obj=[], impact=(P, ["POISON", "MALADIE", "NATURE"], "présence, position et nature")),
"hunters-mark": dict(cond=["COUP"], impact=(4, ["VIE"], "1d6 à chaque coup"), impact_sats=[(P, ["TRAQUE"])]),
"identify": dict(impact=(P, ["PROPRIETE", "ENCHANTEMENT"], "propriétés et sorts en cours")),
"speak-with-animals": dict(impact=(P, ["PAROLE", "BETE"], "parler aux bêtes")),
"augury": dict(impact=(P, ["PRESAGE"], "bonheur, malheur, les deux ou rien"), impact_sats=[(30, ["MINUTES", "AVENIR"])]),
"detect-thoughts": dict(cond=["LANGAGE"], impact=(P, ["PENSEE"], "les pensées de surface, puis profondes"), loc=(9, "METRES", "9 m")),
"find-traps": dict(cible=P, cible_obj=[], impact=(P, ["PIEGE", "PRESENCE"], "la présence d'un piège et sa nature générale")),
"locate-animals-or-plants": dict(cible_note=["BETE", "PLANTE"], impact=(P, ["DIRECTION", "DISTANCE"], "direction et distance du plus proche")),
"locate-object": dict(cond=["VU", "SANSPLOMB"], impact=(P, ["DIRECTION", "OBJET"], "la direction de l'objet")),
"locate-creature": dict(cond=["VU", "SANSEAUVIVE"], impact=(P, ["DIRECTION", "CREATURE"], "la direction de la créature")),
"see-invisibility": dict(impact=(P, ["INVISIBLE", "ETHERE"], "voir l'invisible et l'Éthéré")),
"clairvoyance": dict(grimoire=None, fam="H", comb="Verre", why="le verre qui voit au loin", cible=4, comp=["VERRE"],
                     loc=(2, "KILOMETRES", "2 km (1 mile)"), cond=["LIEUCONNU"], impact=(P, ["VUE", "OUIE"], "voir ou entendre par le capteur")),
"tongues": dict(impact=(P, ["LANGUE", "PAROLE"], "comprendre et être compris")),
"arcane-eye": dict(impact=(P, ["OEIL", "VISION"], "un œil invisible et mobile")),
"divination": dict(impact=(P, ["REPONSE"], "une réponse véridique"), impact_sats=[(7, ["JOURS"])]),
"commune": dict(qty=3, cible_note=["DIVINITE"], impact=(P, ["REPONSE", "OUI", "NON"], "trois réponses par oui ou non")),
"contact-other-plane": dict(qty=5, impact=(P, ["REPONSE"], "cinq réponses"), impact_sats=[(21, ["ESPRIT", "FOLIE"])]),
"commune-with-nature": dict(qty=3, cond=["NATURE"], impact=(P, ["SAVOIR", "TERRAIN"], "trois faits sur le pays alentour")),
"legend-lore": dict(cond=["RENOMMEE"], impact=(P, ["LEGENDE"], "le savoir légendaire")),
"scrying": dict(impact=(P, ["VUE", "OUIE"], "voir et entendre la cible")),
"telepathic-bond": dict(cond=["RAISON"], impact=(P, ["LIEN", "PENSEE"], "un lien télépathique entre tous")),
"find-the-path": dict(cond=["LIEUCONNU"], impact=(P, ["CHEMIN"], "le chemin le plus court")),
"true-seeing": dict(impact=(P, ["VISION", "VERITE"], "voir les choses telles qu'elles sont")),
"foresight": dict(impact=(P, ["AVENIR", "VIGILANCE"], "jamais surprise, toujours avantagée")),
}
apply(LOT2)
FICHES["clairvoyance"]["alt"][0]["comp"] = []

# ===== lots 3 à 8 : Abjuration, Invocation, Évocation, Illusion, Nécromancie, Transmutation =====
# mots en minuscules accentuées : affichés tels quels, translittérés en Alde sans accents ; jamais d'espace (trait d'union)
VIV = ["vivant"]
LOT3 = {  # Abjuration
"resistance": dict(impact=(3, ["garde", "résistance"], "une résistance affermie un instant (1d4 ajouté à une sauvegarde)"), fin=["usage"]),
"alarm": dict(impact=(P, ["alerte"], "une alerte mentale ou sonore")),
"mage-armor": dict(impact=(3, ["garde"], "défense de base 13 + Dex"), cond=["sans-armure"], fin=["armure"]),
"protection-from-evil-and-good": dict(impact=(P, ["garde", "aberration", "céleste", "élémentaire", "fée", "fiélon", "mort-vivant"], "ni attaque franche, ni charme, ni peur, ni possession")),
"sanctuary": dict(impact=(P, ["détournement"], "l'assaillant doit changer de cible"), fin=["agression"]),
"shield": dict(impact=(5, ["garde", "projectile"], "+5 à la défense, insensible au projectile magique")),
"shield-of-faith": dict(impact=(2, ["garde", "foi"], "+2 à la défense")),
"aid": dict(impact=(5, ["vie", "maximum"], "+5 aux points de vie maximum et actuels")),
"arcane-lock": dict(impact=(P, ["verrou", "mot-de-passe"], "infranchissable, sauf au mot de passe")),
"lesser-restoration": dict(impact=(P, ["maladie", "aveuglement", "surdité", "paralysie", "poison"], "une maladie ou un état levé")),
"pass-without-trace": dict(qty_cible=P, impact=(10, ["discrétion", "sans-trace"], "+10 en discrétion, aucune trace")),
"protection-from-poison": dict(impact=(P, ["poison", "résistance"], "le poison neutralisé, puis la résistance")),
"warding-bond": dict(impact=(1, ["garde", "résistance"], "mieux gardée et plus résistante (+1 à la CA et aux sauvegardes)"), impact_sats=[(P, ["partage"])], fin=["distance"]),
"beacon-of-hope": dict(qty_cible=P, impact=(P, ["espoir", "guérison"], "l'espoir qui raffermit, les soins pleinement reçus (avantage aux sauvegardes de Sagesse et contre la mort)")),
"counterspell": dict(impact=(3, ["sort", "interruption"], "un sort de niveau 3 ou moins échoue")),
"dispel-magic": dict(impact=(3, ["sort", "dissipation"], "les sorts de niveau 3 ou moins prennent fin")),
"glyph-of-warding": dict(impact=(23, ["piège", "explosion"], "5d8 en moyenne"), impact_sats=[(P, ["sort"])]),
"magic-circle": dict(cible_note=["céleste", "élémentaire", "fée", "fiélon", "mort-vivant"], impact=(P, ["barrière"], "ni entrer, ni charmer, ni effrayer")),
"nondetection": dict(impact=(P, ["divination"], "insaisissable à la divination")),
"protection-from-energy": dict(impact=(P, ["résistance", "acide", "froid", "feu", "foudre", "tonnerre"], "résistance à une énergie au choix")),
"remove-curse": dict(impact=(P, ["malédiction"], "toutes les malédictions levées")),
"banishment": dict(impact=(P, ["exil", "demi-plan"], "renvoyée sur son plan, ou dans un demi-plan")),
"death-ward": dict(impact=(1, ["vie"], "tombe à 1 au lieu de 0"), fin=["usage"]),
"freedom-of-movement": dict(impact=(P, ["liberté", "entrave"], "rien ne ralentit ni n'entrave")),
"private-sanctum": dict(impact=(P, ["son", "vue", "divination", "passage"], "les protections au choix")),
"stoneskin": dict(impact=(P, ["résistance", "coup"], "résistance aux coups non magiques")),
"antilife-shell": dict(impact=(P, ["barrière", "vivant"], "les vivants tenus au dehors")),
"dispel-evil-and-good": dict(impact=(P, ["garde", "renvoi"], "défense contre l'outre-plan, renvoi possible")),
"greater-restoration": dict(impact=(P, ["charme", "pétrification", "malédiction", "épuisement"], "un mal profond levé")),
"planar-binding": dict(cible_note=["céleste", "élémentaire", "fée", "fiélon"], impact=(P, ["service"], "liée à ton service")),
"forbiddance": dict(impact=(P, ["passage", "plan"], "nul voyage magique vers la zone"), impact_sats=[(28, ["lumière", "nécrose"])]),
"globe-of-invulnerability": dict(impact=(5, ["sort", "barrière"], "les sorts de niveau 5 ou moins sans effet")),
"guards-and-wards": dict(impact=(P, ["brouillard", "porte", "toile", "confusion"], "les sceaux du lieu")),
"antimagic-field": dict(impact=(P, ["magie", "suspension"], "toute magie suspendue")),
"holy-aura": dict(qty_cible=P, impact=(P, ["garde", "lumière"], "une lumière qui protège de tout (avantage aux sauvegardes)"), impact_sats=[(P, ["aveuglement"])]),
"mind-blank": dict(impact=(P, ["esprit", "divination", "charme"], "l'esprit inviolable")),
"imprisonment": dict(impact=(P, ["prison"], "l'une des prisons au choix")),
"prismatic-wall": dict(impact=(P, ["prisme"], "sept couches de couleurs")),
}
LOT4 = {  # Invocation
"mage-hand": dict(impact=(P, ["main"], "une main spectrale"), impact_sats=[(5, ["kilogrammes"])]),
"produce-flame": dict(impact_add=["lumière"]),
"entangle": dict(impact=(P, ["entrave", "terrain"], "entravée, terrain difficile")),
"find-familiar": dict(impact=(P, ["familier", "lien"], "un esprit à forme animale, lié")),
"floating-disk": dict(impact=(P, ["port"], "un disque qui porte"), impact_sats=[(225, ["kilogrammes"])]),
"fog-cloud": dict(impact=(P, ["brouillard", "obscurité"], "zone fortement obscurcie"), fin=["vent"]),
"grease": dict(impact=(P, ["glissade", "chute"], "terrain glissant, chute")),
"unseen-servant": dict(impact=(P, ["serviteur"], "une force invisible qui sert")),
"find-steed": dict(impact=(P, ["monture", "lien"], "un esprit-destrier lié")),
"web": dict(impact=(P, ["toile", "entrave"], "toile collante")),
"conjure-animals": dict(cible_note=["fée", "bête"], impact=(2, ["bête"], "une bête de puissance 2")),
"create-food-and-water": dict(impact=(20, ["nourriture", "kilogrammes"], "20 kg de nourriture"), impact_sats=[(112, ["litres", "eau"])]),
"revivify": dict(cond=["mort"], cond_sats=[(1, ["minute"])], impact=(1, ["vie"], "revient avec 1 point de vie")),
"sleet-storm": dict(impact=(P, ["verglas", "chute", "obscurité"], "verglas, chute, obscurité")),
"spirit-guardians": dict(impact_sats=[(P, ["lenteur"])]),
"stinking-cloud": dict(cond=["souffle"], impact=(P, ["nausée"], "pliée en deux à vomir")),
"black-tentacles": dict(impact_sats=[(P, ["entrave"])]),
"conjure-minor-elementals": dict(impact=(2, ["élémentaire"], "un élémentaire de puissance 2")),
"conjure-woodland-beings": dict(impact=(2, ["fée"], "une fée de puissance 2")),
"faithful-hound": dict(impact_sats=[(P, ["alerte"])]),
"guardian-of-faith": dict(impact_sats=[(60, ["limite"])]),
"secret-chest": dict(impact=(P, ["éthéré", "cache"], "le coffre caché dans l'Éthéré")),
"cloudkill": dict(fin=["vent"]),
"insect-plague": dict(impact_add=["insectes"]),
"mass-cure-wounds": dict(cond=VIV),
"teleportation-circle": dict(cond=["sceau"], impact=(P, ["portail"], "un portail vers le cercle connu")),
"tree-stride": dict(cond=["arbre"], impact=(P, ["arbre", "passage"], "d'arbre en arbre"), impact_sats=[(150, ["mètres"])]),
"conjure-elemental": dict(impact=(5, ["élémentaire"], "un élémentaire de puissance 5")),
"conjure-fey": dict(impact=(6, ["fée"], "une fée de puissance 6")),
"heroes-feast": dict(qty_cible=12, impact=(P, ["festin", "vie", "intrépidité"], "guéri, immunisé, fortifié")),
"instant-summons": dict(impact=(P, ["rappel"], "l'objet revient en main")),
"planar-ally": dict(cond=["connu"], impact=(P, ["céleste", "élémentaire", "fiélon"], "un serviteur envoyé par l'entité")),
"transport-via-plants": dict(cond=["vu"], impact=(P, ["plante", "passage"], "de plante en plante")),
"wall-of-thorns": dict(impact_add=["épines"]),
"word-of-recall": dict(cond=["sanctuaire"], impact=(P, ["sanctuaire", "rappel"], "retour au sanctuaire")),
"conjure-celestial": dict(impact=(4, ["céleste"], "un céleste de puissance 4")),
"magnificent-mansion": dict(impact=(P, ["demeure"], "une demeure extradimensionnelle")),
"plane-shift": dict(impact=(P, ["plan", "passage"], "vers un autre plan")),
"demiplane": dict(impact=(P, ["demi-plan", "porte"], "une porte vers un demi-plan")),
"incendiary-cloud": dict(impact_add=["fumée"], fin=["vent"]),
"maze": dict(impact=(P, ["labyrinthe"], "bannie dans un labyrinthe")),
"gate": dict(impact=(P, ["portail", "plan"], "un portail vers un autre plan")),
"mass-heal": dict(cond=VIV, impact_add=["maladie", "aveuglement"]),
"storm-of-vengeance": dict(impact_add=["foudre", "acide", "grêle"], impact_sats=[(P, ["surdité"])]),
}
LOT5 = {  # Évocation
"dancing-lights": dict(impact=(P, ["lueur", "mobile"], "quatre lueurs mobiles")),
"fire-bolt": dict(impact_add=["embrasement"]),
"ray-of-frost": dict(impact_sats=[(3, ["lenteur", "mètres"])]),
"shocking-grasp": dict(impact_sats=[(P, ["stupeur"])]),
"burning-hands": dict(impact_add=["embrasement"]),
"cure-wounds": dict(cond=VIV), "healing-word": dict(cond=VIV), "prayer-of-healing": dict(cond=VIV), "mass-healing-word": dict(cond=VIV),
"divine-favor": dict(cond=["coup"]),
"faerie-fire": dict(impact=(P, ["contour", "révélation"], "contours lumineux, nul invisible")),
"guiding-bolt": dict(impact_sats=[(P, ["marque"])]),
"thunderwave": dict(impact=(9, ["tonnerre"], "2d8 en moyenne"), impact_sats=[(3, ["recul", "mètres"])]),
"acid-arrow": dict(impact_sats=[(5, ["acide", "différé"])]),
"branding-smite": dict(impact_sats=[(P, ["révélation"])]),
"continual-flame": dict(impact=(P, ["flamme", "sans-chaleur"], "une flamme froide et inextinguible")),
"darkness": dict(impact=(P, ["ténèbres", "opacité"], "des ténèbres que rien ne perce")),
"flame-blade": dict(impact_add=["lame"]),
"gust-of-wind": dict(impact=(P, ["vent", "recul"], "repoussée le long de la ligne"), impact_sats=[(5, ["mètres"])]),
"moonbeam": dict(impact_sats=[(P, ["forme-vraie"])]),
"shatter": dict(impact_add=["fracas"]),
"spiritual-weapon": dict(impact_add=["arme"]),
"daylight": dict(impact=(P, ["jour", "dissipation"], "la lumière du jour, qui dissipe les ténèbres")),
"fireball": dict(impact_add=["embrasement"]),
"lightning-bolt": dict(impact=(28, ["foudre", "embrasement"], "8d6 en moyenne")),
"sending": dict(impact=(P, ["message"], "un message et sa réponse"), impact_sats=[(25, ["mots"])]),
"tiny-hut": dict(impact=(P, ["abri", "barrière"], "un dôme que rien ne franchit"), impact_sats=[(9, ["occupants"])]),
"wind-wall": dict(impact_add=["vent", "projectile"]),
"fire-shield": dict(impact_sats=[(P, ["résistance", "froid"])], _alt=[dict(impact_sats=[(P, ["résistance", "feu"])]), dict()]),
"ice-storm": dict(impact_add=["grêle"], impact_sats=[(9, ["choc"])]),
"resilient-sphere": dict(impact=(P, ["prison", "barrière"], "une sphère que rien ne traverse")),
"wall-of-fire": dict(impact_add=["mur"]),
"arcane-hand": dict(impact_add=["main", "poussée", "étreinte"]),
"cone-of-cold": dict(impact_sats=[(P, ["statue"])]),
"flame-strike": dict(impact_sats=[(14, ["lumière"])]),
"hallow": dict(impact=(P, ["sanctuaire", "garde"], "un lieu sanctifié")),
"wall-of-force": dict(impact=(P, ["barrière", "force"], "un mur invisible et indestructible")),
"wall-of-stone": dict(impact=(P, ["pierre", "mur"], "un mur de pierre")),
"blade-barrier": dict(impact_add=["lames"]),
"contingency": dict(impact=(P, ["sort", "différé"], "un sort tenu en réserve")),
"freezing-sphere": dict(impact_sats=[(P, ["gel", "eau"])]),
"heal": dict(cond=VIV, impact_add=["aveuglement", "surdité", "maladie"]),
"sunbeam": dict(impact_sats=[(P, ["aveuglement"])]),
"wall-of-ice": dict(impact_add=["mur"]),
"arcane-sword": dict(impact_add=["épée"]),
"delayed-blast-fireball": dict(impact_sats=[(P, ["croissance"])]),
"divine-word": dict(qty_cible=P, cond=["écoute"], impact=(P, ["surdité", "aveuglement", "étourdissement", "mort"], "selon la vie qui reste")),
"fire-storm": dict(impact_add=["embrasement"]),
"forcecage": dict(impact=(P, ["prison", "cage"], "une cage de force")),
"prismatic-spray": dict(impact=(35, ["feu", "acide", "foudre", "poison", "froid", "pétrification", "bannissement"], "10d6 en moyenne, selon la couleur")),
"earthquake": dict(impact=(P, ["séisme", "fissure"], "le sol tremble et se fend")),
"sunburst": dict(impact_sats=[(P, ["aveuglement"])]),
"meteor-swarm": dict(impact_sats=[(70, ["choc"])]),
}
LOT6 = {  # Illusion
"minor-illusion": dict(impact=(P, ["son", "image"], "un son ou une image")),
"color-spray": dict(impact=(32, ["aveuglement", "vie"], "6d10 points de vie de créatures aveuglées")),
"disguise-self": dict(impact=(P, ["apparence"], "une autre apparence")),
"illusory-script": dict(impact=(P, ["écriture", "secret"], "un texte lisible des seuls élus")),
"arcanists-magic-aura": dict(impact=(P, ["fausse-aura"], "la divination trompée")),
"blur": dict(impact=(P, ["flou"], "une silhouette floue, difficile à frapper (désavantage pour qui l'attaque)")),
"invisibility": dict(impact=(P, ["invisibilité"], "invisible"), fin=["attaque"]),
"greater-invisibility": dict(impact=(P, ["invisibilité"], "invisible, même en attaquant")),
"magic-mouth": dict(impact=(P, ["message"], "une bouche qui parle"), impact_sats=[(25, ["mots"])]),
"silence": dict(impact=(P, ["silence", "surdité"], "nul son")),
"fear": dict(impact=(P, ["peur", "fuite"], "lâche tout et fuit")),
"hypnotic-pattern": dict(impact=(P, ["charme", "fascination"], "charmée, immobile"), fin=["blessure"]),
"major-image": dict(impact=(P, ["image", "son", "odeur", "chaleur"], "une illusion complète")),
"phantom-steed": dict(impact=(P, ["monture"], "un coursier quasi réel"), impact_sats=[(30, ["mètres"])]),
"hallucinatory-terrain": dict(impact=(P, ["terrain"], "un autre paysage")),
"phantasmal-killer": dict(impact_add=["peur"]),
"creation": dict(impact=(P, ["matière", "ombre"], "un objet tiré de l'ombre")),
"dream": dict(cond=["sommeil"], impact_add=["rêve", "message"]),
"mislead": dict(impact=(P, ["double", "invisibilité"], "un double, et soi invisible")),
"seeming": dict(impact=(P, ["apparence"], "une autre apparence pour chacun")),
"programmed-illusion": dict(impact=(P, ["image", "scénario"], "une scène qui se joue au signal")),
"mirage-arcane": dict(impact=(P, ["terrain", "toucher"], "un paysage qu'on peut toucher")),
"project-image": dict(impact=(P, ["double", "vue"], "un double lointain qui voit pour toi")),
"simulacrum": dict(cond=["bête", "humanoïde"], impact=(P, ["double", "glace"], "un double de neige")),
"weird": dict(impact_add=["peur"]),
}
LOT7 = {  # Nécromancie
"chill-touch": dict(impact_sats=[(P, ["sans-guérison"])]),
"spare-the-dying": dict(cond=VIV, impact=(P, ["stabilité"], "le mourant stabilisé")),
"false-life": dict(impact=(7, ["vie", "temporaire"], "1d4 + 4 en moyenne")),
"blindness-deafness": dict(impact=(P, ["aveuglement", "surdité"], "aveugle ou sourde")),
"gentle-repose": dict(impact=(P, ["conservation"], "ni pourriture ni éveil")),
"ray-of-enfeeblement": dict(impact=(P, ["faiblesse"], "moitié des dégâts de force")),
"animate-dead": dict(impact=(P, ["mort-vivant", "service"], "un squelette ou un zombi à ton service")),
"bestow-curse": dict(impact=(P, ["malédiction"], "une malédiction au choix")),
"speak-with-dead": dict(qty=5, impact=(P, ["réponse", "mort"], "cinq réponses du cadavre")),
"vampiric-touch": dict(impact_sats=[(6, ["vie"])]),
"blight": dict(cond=VIV, impact_add=["dessèchement"]),
"raise-dead": dict(cond=["mort"], cond_sats=[(10, ["jours"])], impact=(1, ["vie"], "revient avec 1 point de vie")),
"create-undead": dict(cond=["nuit"], impact=(P, ["goule", "service"], "des goules à ton service")),
"eyebite": dict(impact=(P, ["sommeil", "panique", "maladie"], "l'un des trois maux")),
"harm": dict(impact_sats=[(P, ["maximum"])]),
"magic-jar": dict(impact=(P, ["possession", "âme"], "l'âme logée dans le réceptacle")),
"finger-of-death": dict(impact_sats=[(P, ["zombi"])]),
"resurrection": dict(cond=["mort"], cond_sats=[(100, ["ans"])], impact=(P, ["vie"], "tous ses points de vie")),
"clone": dict(impact=(P, ["clone", "âme"], "un double qui recueille l'âme")),
"astral-projection": dict(impact=(P, ["astral", "cordon"], "le corps astral, relié")),
"true-resurrection": dict(cond=["mort"], cond_sats=[(200, ["ans"])], impact=(P, ["vie", "corps"], "tous ses points de vie, un corps neuf au besoin")),
}
LOT8 = {  # Transmutation
"druidcraft": dict(impact=(P, ["nature", "présage"], "un petit prodige naturel")),
"mending": dict(impact=(P, ["réparation"], "la brisure réparée")),
"message": dict(impact=(P, ["murmure"], "un murmure et sa réponse")),
"prestidigitation": dict(impact=(P, ["tour"], "un tour mineur")),
"shillelagh": dict(impact=(5, ["arme", "bois"], "1d8 en moyenne")),
"thaumaturgy": dict(impact=(P, ["prodige"], "un signe surnaturel")),
"create-or-destroy-water": dict(impact=(40, ["eau", "litres"], "40 litres créés ou détruits")),
"expeditious-retreat": dict(impact=(P, ["course"], "courir sans cesse plus vite")),
"feather-fall": dict(impact=(18, ["chute", "mètres"], "une chute lente comme une plume (18 m par round)")),
"goodberry": dict(impact=(1, ["vie", "nourriture"], "1 point de vie et un jour de vivres")),
"purify-food-and-drink": dict(impact=(P, ["poison", "maladie"], "purifiés")),
"alter-self": dict(impact=(P, ["apparence", "adaptation", "arme"], "l'une des trois métamorphoses")),
"barkskin": dict(impact_add=["écorce"]),
"darkvision": dict(impact=(18, ["vision", "obscurité"], "voir dans le noir à 18 m")),
"enhance-ability": dict(impact=(P, ["aptitude"], "une aptitude renforcée")),
"heat-metal": dict(impact_sats=[(P, ["lâcher"])]),
"knock": dict(impact=(P, ["ouverture"], "une fermeture levée")),
"levitate": dict(impact=(6, ["mètres", "élévation"], "jusqu'à 6 m"), _alt=[dict(impact=(6, ["mètres", "élévation"], "jusqu'à 6 m"))]),
"rope-trick": dict(impact=(P, ["abri", "extradimension"], "un abri au bout de la corde")),
"spider-climb": dict(impact=(P, ["escalade"], "marcher aux murs et aux plafonds")),
"spike-growth": dict(impact=(5, ["perce", "épines"], "2d4 tous les 1,5 m")),
"blink": dict(impact=(P, ["éthéré"], "glisser dans l'Éthéré au hasard")),
"fly": dict(impact=(18, ["vol", "mètres"], "18 m de vol")),
"gaseous-form": dict(impact=(P, ["brume", "résistance"], "une brume résistante")),
"meld-into-stone": dict(_alt=[dict(impact=(P, ["pierre"], "fondu dans la pierre"))]),
"plant-growth": dict(impact=(P, ["croissance"], "végétation foisonnante")),
"speak-with-plants": dict(impact=(P, ["parole", "plante"], "parler aux plantes")),
"water-breathing": dict(impact=(P, ["souffle", "eau"], "respirer sous l'eau")),
"water-walk": dict(impact=(P, ["marche", "liquide"], "marcher sur les liquides")),
"control-water": dict(impact_add=["inondation", "partage", "tourbillon"]),
"fabricate": dict(impact=(P, ["fabrication"], "un objet tiré de la matière brute")),
"giant-insect": dict(cible=2, cible_obj=[], cible_note=["insecte"], impact=(P, ["gigantisme"], "des insectes géants qui t'obéissent")),
"stone-shape": dict(impact=(P, ["façonnage"], "la pierre façonnée")),
"animate-objects": dict(impact=(P, ["animation"], "des objets qui vivent et obéissent")),
"awaken": dict(cible_obj=[], cible_note=["bête", "plante"], impact=(10, ["raison", "parole"], "l'intelligence 10 et une langue")),
"passwall": dict(impact=(P, ["passage"], "un passage dans la paroi")),
"telekinesis": dict(impact=(P, ["déplacement"], "déplacer par la pensée")),
"disintegrate": dict(impact=(75, ["vie", "poussière"], "10d6 + 40 en moyenne, réduite en poussière à 0")),
"move-earth": dict(impact=(P, ["terrassement"], "la terre remodelée")),
"wind-walk": dict(impact=(90, ["vol", "mètres", "nuage"], "nuée volant à 90 m")),
"etherealness": dict(impact=(P, ["éthéré"], "dans les confins de l'Éthéré")),
"regenerate": dict(impact_sats=[(1, ["vie", "tour"])], impact_add=["membre"]),
"reverse-gravity": dict(impact=(P, ["gravité", "inversion"], "la chute vers le haut")),
"sequester": dict(impact=(P, ["cache", "suspension"], "caché, hors du temps")),
"animal-shapes": dict(impact=(4, ["bête"], "des bêtes de puissance 4")),
"control-weather": dict(cond=["ciel"], impact=(P, ["climat"], "le temps qu'il fait, changé")),
"glibness": dict(impact=(15, ["persuasion", "vérité"], "15 au minimum, toujours cru")),
"shapechange": dict(impact=(P, ["forme", "créature"], "la forme d'une créature vue")),
"true-polymorph": dict(impact=(P, ["créature", "objet"], "créature ou objet, l'un en l'autre")),
}
for lot in (LOT3, LOT4, LOT5, LOT6, LOT7, LOT8): apply(lot)

# ===== Seuils : Impact plein (le sort adverse entièrement contré), seuil chiffré en satellite =====
apply({
"counterspell": dict(impact=(P, ["sort", "interruption"], "le sort adverse échoue"), impact_sats=[(3, ["seuil", "niveau"])]),
"dispel-magic": dict(impact=(P, ["sort", "dissipation"], "les sorts prennent fin"), impact_sats=[(3, ["seuil", "niveau"])]),
"globe-of-invulnerability": dict(impact=(P, ["sort", "barrière"], "les sorts sans effet à l'intérieur"), impact_sats=[(5, ["seuil", "niveau"])]),
"magnificent-mansion": dict(comp=["ivoire"]),
})

# ===== Une forme par option : ce que l'arcaniste choisit au lancement est un autre glyphe =====
def O(label, **kw): return dict(label=label, **kw)
def opts(k, *o): FICHES[k]["options"] = list(o)
I = lambda *w, why="": dict(impact=(P, list(w), why))
opts("alarm", O("Alarme mentale", **I("alerte", "pensée", why="un tintement dans l'esprit")), O("Alarme sonore", **I("alerte", "son", why="une clochette audible")))
opts("calm-emotions", O("Apaisement", **I("calme", "charme", "peur", why="charme et peur suspendus")), O("Indifférence", **I("calme", "hostilité", why="l'hostilité éteinte")))
opts("minor-illusion", O("Son", cosm=("plein", "son"), **I("son", why="un son")), O("Image", **I("image", why="l'image d'un objet")))
opts("alter-self", O("Adaptation aquatique", **I("adaptation", "eau", why="branchies et palmes")), O("Changement d'apparence", **I("apparence", why="un autre visage")), O("Armes naturelles", **I("arme", "griffe", why="griffes, crocs, cornes")))
opts("enhance-ability", O("Endurance de l'ours", impact=(7, ["endurance", "vie"], "2d6 points de vie temporaires")), O("Force du taureau", **I("force", "charge", why="plus forte, deux fois plus chargée (avantage en Force)")),
     O("Grâce du félin", **I("grâce", "chute", why="plus agile, aucune chute ne la blesse (avantage en Dextérité)")), O("Splendeur de l'aigle", **I("splendeur", why="plus rayonnante (avantage en Charisme)")),
     O("Ruse du renard", **I("ruse", why="plus vive d'esprit (avantage en Intelligence)")), O("Sagesse du hibou", **I("sagesse", why="plus sage et plus perspicace (avantage en Sagesse)")))
opts("eyebite", O("Sommeil", **I("sommeil", why="endormie")), O("Panique", **I("panique", "fuite", why="effrayée, elle fuit")), O("Malaise", **I("malaise", why="mal en point, tout lui coûte (désavantage aux attaques et aux tests)")))
opts("protection-from-energy", *[O(n, **I("résistance", w, why=f"résistance {d}")) for n, w, d in
     [("Acide", "acide", "à l'acide"), ("Froid", "froid", "au froid"), ("Feu", "feu", "au feu"), ("Foudre", "foudre", "à la foudre"), ("Tonnerre", "tonnerre", "au tonnerre")]])
opts("control-water", O("Inondation", **I("inondation", why="l'eau monte de 6 m")), O("Partage des eaux", **I("partage", why="un passage à sec")),
     O("Détournement du courant", **I("courant", why="le flot change de sens")), O("Tourbillon", impact=(9, ["tourbillon", "choc"], "2d8 en moyenne")))
opts("bestow-curse", O("Faiblesse", **I("malédiction", "aptitude", why="une faculté affaiblie (désavantage sur une caractéristique)")), O("Maladresse", **I("malédiction", "maladresse", why="maladroite face à toi (désavantage contre toi)")),
     O("Torpeur", **I("malédiction", "torpeur", why="figée de torpeur, un instant sur deux")), O("Châtiment", impact=(5, ["malédiction", "nécrose"], "1d8 à chacun de tes coups")))
opts("imprisonment", *[O(n, **I("prison", w, why=d)) for n, w, d in [("Ensevelissement", "ensevelissement", "enfouie sous la terre"), ("Enchaînement", "chaînes", "enchaînée au sol"),
     ("Prison close", "demi-plan", "enclose dans un demi-plan"), ("Confinement minuscule", "gemme", "rétrécie dans une gemme"), ("Sommeil", "sommeil", "endormie")]])
opts("blindness-deafness", O("Cécité", **I("aveuglement", why="aveugle")), O("Surdité", **I("surdité", why="sourde")))
opts("lesser-restoration", *[O(n, **I(w, why=d)) for n, w, d in [("Maladie", "maladie", "une maladie levée"), ("Cécité", "aveuglement", "la cécité levée"),
     ("Surdité", "surdité", "la surdité levée"), ("Paralysie", "paralysie", "la paralysie levée"), ("Poison", "poison", "l'empoisonnement levé")]])
opts("greater-restoration", O("Épuisement", impact=(1, ["épuisement"], "un niveau d'épuisement retiré")), O("Charme ou pétrification", **I("charme", "pétrification", why="l'effet levé")),
     O("Malédiction", **I("malédiction", why="la malédiction levée")), O("Faculté", **I("aptitude", why="une faculté rendue")), O("Vie maximum", **I("vie", "maximum", why="le maximum rendu")))
opts("create-or-destroy-water", O("Création", impact=(40, ["eau", "litres", "création"], "40 litres créés")), O("Destruction", impact=(40, ["eau", "litres", "destruction"], "40 litres détruits")))
opts("druidcraft", O("Présage du temps", **I("présage", "climat")), O("Floraison", **I("floraison")), O("Effet sensoriel", **I("sensation")), O("Flamme", **I("flamme")))
opts("prestidigitation", O("Effet sensoriel", **I("sensation")), O("Flamme", **I("flamme")), O("Nettoyage", **I("propreté")), O("Saveur et température", **I("saveur", "chaleur")),
     O("Marque", **I("marque")), O("Babiole", **I("babiole")))
opts("thaumaturgy", O("Voix tonnante", **I("voix")), O("Flammes", **I("flamme")), O("Tremblements", **I("tremblement")), O("Son", **I("son")), O("Porte", **I("porte")), O("Regard", **I("regard")))
opts("glyph-of-warding", O("Runes explosives", impact=(23, ["piège", "explosion"], "5d8 en moyenne"), impact_sats=[]), O("Glyphe de sort", impact=(P, ["piège", "sort"], "un sort enfermé"), impact_sats=[]))
opts("contagion", *[O(n, **I("maladie", w, why=d)) for n, w, d in [("Mal aveuglant", "aveuglement", "aveugle"), ("Fièvre des ordures", "faiblesse", "le corps affaibli (désavantage en Force)"),
     ("Chair pourrissante", "pourriture", "la chair qui pourrit"), ("Feu de l'esprit", "démence", "l'esprit en fièvre"), ("Crises", "convulsion", "secouée de spasmes"), ("Mort visqueuse", "hémorragie", "le sang qui fuit")]])
for k, w in (("conjure-animals", "bête"), ("conjure-minor-elementals", "élémentaire"), ("conjure-woodland-beings", "fée")):
    opts(k, O(f"Un être de puissance 2", impact=(2, [w], "puissance 2")), O("Deux êtres de puissance 1", impact=(1, [w], "puissance 1"), impact_sats=[(2, ["nombre"])]),
         O("Quatre êtres de puissance ½", impact=(2, [w, "fractionné"], "puissance ½"), impact_sats=[(4, ["nombre"])]),
         O("Huit êtres de puissance ¼", impact=(4, [w, "fractionné"], "puissance ¼"), impact_sats=[(8, ["nombre"])]))
opts("hallow", *[O(n, impact_sats=[(P, ws)]) for n, ws in [("Courage", ["courage"]), ("Ténèbres", ["ténèbres"]), ("Lumière du jour", ["jour"]), ("Protection contre l'énergie", ["résistance"]),
     ("Vulnérabilité à l'énergie", ["vulnérabilité"]), ("Repos éternel", ["repos"]), ("Interférence extradimensionnelle", ["passage"]), ("Peur", ["peur"]), ("Silence", ["silence"]), ("Langues", ["langue"])]])
opts("telekinesis", O("Créature", cible=3, **I("déplacement", why="déplacer une créature")), O("Objet", cible=1, cible_obj=["objet"], **I("déplacement", why="déplacer un objet")))
# formes géométriques au choix : droit ou en anneau, mur ou sphère, sphère ou panneaux
for k, ln, ring in (("blade-barrier", 100, 30), ("wall-of-fire", 60, 10), ("wall-of-thorns", 60, 10)):
    opts(k, O("Mur droit", aoe={"type": "line", "size": ln}), O("Mur en anneau", aoe={"type": "cylinder", "size": ring}))
opts("prismatic-wall", O("Mur", aoe={"type": "line", "size": 90}), O("Sphère", aoe={"type": "sphere", "size": 15}))
FICHES["wall-of-force"].pop("grimoire", None); FICHES["wall-of-force"].update(verb=V("existence"))
PAN = [("FORME", 2, [], "plan : dix panneaux contigus", [(90, 1)]), ("AMPLEUR", 90, ["SURFACE", "METRES"], "90 m² : dix panneaux de 3 m")]
for k in ("wall-of-force", "wall-of-ice"):
    opts(k, O("Sphère ou dôme", aoe={"type": "sphere", "size": 10}), O("Panneaux", no_aoe=True, forme=PAN))

# ===== Règles de 2024 (SRD 5.2) =====
# Chaque sort commun reçoit ses formes de 2024 ; celles dont le glyphe ne change pas sont écartées (même sort).
# V24 corrige ce que les données de 2024 ne disent pas en champs structurés (soins, dégâts d'un autre type, zones).
ENERGIES = [("Acide", "acide", "Acide sulfurique"), ("Froid", "froid", "Glace"), ("Feu", "feu", "Feu"),
            ("Foudre", "foudre", "Foudre"), ("Poison", "poison", "Ammoniac"), ("Tonnerre", "tonnerre", "Orage")]
V24 = {
"animate-objects": dict(qty_cible=3),
"antipathy-sympathy": dict(cible=1, cible_obj=["objet"], no_aoe=True, impact_sats=[(36, ["mètres"])]),
"arcane-sword": dict(impact=(29, None, "4d12 + 3 en moyenne")),
"contagion": dict(grimoire=None, verb=V("qualite", True), cible=3, options=None, impact=(50, ["nécrose", "poison", "faiblesse"], "11d8 en moyenne, puis la faiblesse")),
"banishment": dict(grimoire=None, verb=V("trame", True), cible=9, loc=(9, "METRES", "9 m")),
"cure-wounds": dict(impact=(12, None, "2d8 + 3 en moyenne")),
"healing-word": dict(impact=(8, None, "2d4 + 3 en moyenne")),
"mass-cure-wounds": dict(impact=(26, None, "5d8 + 3 en moyenne")),
"mass-healing-word": dict(impact=(8, None, "2d4 + 3 en moyenne")),
"prayer-of-healing": dict(qty_cible=5, impact=(9, ["vie", "repos"], "2d8 en moyenne et un court repos")),
"darkvision": dict(impact=(45, ["vision", "obscurité"], "voir dans le noir à 45 m")),
"enhance-ability": dict(options=[O(n, **I("aptitude", w)) for n, w in [("Force", "force"), ("Dextérité", "dextérité"), ("Intelligence", "intelligence"), ("Sagesse", "sagesse"), ("Charisme", "charisme")]]),
"false-life": dict(impact=(9, ["vie", "temporaire"], "2d4 + 4 en moyenne")),
"flame-strike": dict(impact_sats=[(18, ["lumière"])]),
"ice-storm": dict(impact=(14, ["froid"], "4d6 en moyenne"), impact_sats=[(11, ["choc"])]),
"jump": dict(impact=(9, ["saut", "mètres"], "bonds de 9 m")),
"power-word-kill": dict(impact_sats=[(78, ["esprit"])]),
"prismatic-spray": dict(impact=(42, ["feu", "acide", "foudre", "poison", "froid", "pétrification", "bannissement"], "12d6 en moyenne, selon la couleur")),
"ray-of-enfeeblement": dict(impact=(P, ["faiblesse"], "le corps affaibli (désavantage en Force)"), impact_sats=[(5, ["blessure"])]),
"sleep": dict(aoe={"type": "sphere", "size": 5}, impact=(P, ["sommeil"], "neutralisée, puis endormie")),
"color-spray": dict(impact=(P, ["aveuglement"], "aveuglée jusqu'à ton prochain tour")),
"storm-of-vengeance": dict(aoe={"type": "sphere", "size": 300}),
"vicious-mockery": dict(impact=(4, ["esprit", "maladresse"], "1d6 en moyenne, puis une attaque maladroite")),
"weird": dict(impact_sats=[(28, ["esprit"])]),
"feeblemind": dict(src_idx="befuddlement", name="Befuddlement", dur=None, impact=(65, ["esprit"], "10d12 en moyenne"), impact_sats=[(P, ["incantation"])]),
"branding-smite": dict(src_idx="shining-smite", name="Shining Smite", impact_sats=[(P, ["révélation", "marque"])]),
}
for k in ("conjure-animals", "conjure-minor-elementals", "conjure-woodland-beings", "conjure-fey", "conjure-celestial", "conjure-elemental", "true-strike", "resistance"):
    FICHES[k]["v24"] = None          # en 2024 ce sont d'autres sorts : entrées séparées
for k, v in V24.items(): FICHES[k]["v24"] = v

E24 = dict(src="2024")
NEW24 = {
# --- entrées séparées : même nom, autre sort ---
"conjure-animals-2024": dict(E24, src_idx="conjure-animals", fr="Invocation d'animaux (2024)", verb=V("trame"), cible="plein", aoe={"type": "sphere", "size": 10},
    impact=(17, ["taille"], "3d10 en moyenne"), impact_add=["meute", "esprit"]),
"conjure-minor-elementals-2024": dict(E24, src_idx="conjure-minor-elementals", fr="Invocation d'élémentaires mineurs (2024)", comb="Air", why="les esprits élémentaires",
    cible="plein", aoe={"type": "sphere", "size": 15}, no_loc=True, cond=["coup"], impact=(9, ["acide", "froid", "feu", "foudre"], "2d8 à chaque coup"), impact_sats=[(P, ["terrain"])]),
"conjure-woodland-beings-2024": dict(E24, src_idx="conjure-woodland-beings", fr="Invocation d'êtres sylvestres (2024)", verb=V("trame"), cible="plein",
    aoe={"type": "sphere", "size": 10}, no_loc=True, impact=(23, None, "5d8 en moyenne"), impact_add=["esprit", "fée"]),
"conjure-fey-2024": dict(E24, src_idx="conjure-fey", fr="Invocation de fée (2024)", verb=V("trame"), cible=3, impact=(23, ["esprit", "peur"], "3d12 + 3 en moyenne, puis la peur")),
"conjure-celestial-2024": dict(E24, src_idx="conjure-celestial", fr="Invocation de céleste (2024)", verb=V("trame"), cible="plein", aoe={"type": "cylinder", "size": 10},
    impact=(29, ["vie"], "4d12 + 3 en moyenne pour qui est soigné"), impact_sats=[(39, ["lumière"])]),
"conjure-elemental-2024": dict(E24, src_idx="conjure-elemental", fr="Invocation d'élémentaire (2024)", fam="H", cible="plein", aoe={"type": "sphere", "size": 5},
    options=[O(n, comb=c, why=f"l'esprit de {n.lower()}", impact=(36, [w], "8d8 en moyenne"), impact_sats=[(P, ["entrave"])]) for n, w, c in
             [("Air", "foudre", "Foudre"), ("Terre", "tonnerre", "Orage"), ("Feu", "feu", "Feu"), ("Eau", "froid", "Glace")]]),
"resistance-2024": dict(E24, src_idx="resistance", fr="Résistance (2024)", verb=V("ordre"), cible=2, fin=["usage"],
    options=[O(n, impact=(3, ["garde", w], "1d4 retranché aux dégâts")) for n, w in
    [("Acide", "acide"), ("Choc", "choc"), ("Froid", "froid"), ("Feu", "feu"), ("Foudre", "foudre"), ("Nécrose", "nécrose"),
     ("Perforation", "perce"), ("Poison", "poison"), ("Radiance", "lumière"), ("Tranchant", "taille"), ("Tonnerre", "tonnerre")]]),
"true-strike-2024": dict(E24, src_idx="true-strike", fr="Coup au but (2024)", verb=V("intensite"), cible=3, no_loc=True, impact=(P, ["arme", "lumière"], "une attaque d'arme guidée, radiante au choix")),
# --- sorts nouveaux du SRD 5.2 ---
"aura-of-life": dict(E24, fr="Aura de vie", verb=V("nature", True), cible=2, qty_cible=P, aoe={"type": "sphere", "size": 30}, no_loc=True,
    impact=(P, ["résistance", "nécrose", "vie"], "résistance à la nécrose, maximum préservé"), impact_sats=[(1, ["vie", "mourant"])]),
"charm-monster": dict(E24, fr="Charme-monstre", fam="H", comb="Pollen", why="ce qui se respire et charme", cible=3, impact=(P, ["charme"], "charmée entièrement"), fin=["offense"],
    alt=[A("relation")]),
"chromatic-orb": dict(E24, fr="Orbe chromatique", fam="A", verb=V("existence", True), cible=3, comp=["diamant"],
    options=[O(n, comb=c, why=f"l'orbe de {w}", impact=(14, [w], "3d8 en moyenne"), impact_sats=[(P, ["rebond"])]) for n, w, c in ENERGIES],
    alt=[dict(fam="H", label="Forme hybride")]),
"dissonant-whispers": dict(E24, fr="Murmures dissonants", verb=V("force", True), cible=3, impact_add=["fuite"]),
"divine-smite": dict(E24, fr="Châtiment divin", verb=V("existence", True), cible=3, no_loc=True, cond=["coup"], impact_sats=[(5, ["fiélon", "mort-vivant"])],
    alt=[H("Feu", "le feu sacré")]),
"dragons-breath": dict(E24, fr="Souffle du dragon", fam="A", verb=V("nature"), cible=2,
    options=[O(n, comb=c, why=f"le souffle de {w}", impact=(11, [w], "3d6 en moyenne"), impact_sats=[(5, ["cône", "mètres"])]) for n, w, c in ENERGIES[:5]],
    alt=[dict(fam="H", label="Forme hybride")]),
"elementalism": dict(E24, fr="Élémentalisme", fam="H", cible="plein", aoe={"type": "cube", "size": 5},
    options=[O("Appel de l'air", comb="Air", why="l'air", **I("brise")), O("Appel de la terre", comb="Terre", why="la terre", **I("poussière", "écriture")),
             O("Appel du feu", comb="Feu", why="le feu", **I("braise", "flamme")), O("Appel de l'eau", comb="Eau", why="l'eau", **I("bruine", "brume")),
             O("Façonnage des éléments", fam="A", verb=V("nature"), **I("façonnage", "élément"))]),
"ensnaring-strike": dict(E24, fr="Frappe piégeante", comb="Plante", why="les lianes", cible=3, no_loc=True, cond=["coup"],
    impact=(P, ["entrave"], "entravée par des lianes"), impact_sats=[(4, ["perce"])]),
"hex": dict(E24, fr="Maléfice", verb=V("qualite", True), cible=3, cond=["coup"], impact=(4, ["nécrose"], "1d6 à chaque coup"),
    options=[O(n, impact_sats=[(P, ["maladresse", w])]) for n, w in [("Force", "force"), ("Dextérité", "dextérité"), ("Constitution", "constitution"),
             ("Intelligence", "intelligence"), ("Sagesse", "sagesse"), ("Charisme", "charisme")]],
    alt=[H("Sang", "le sang maudit")]),
"ice-knife": dict(E24, fr="Couteau de glace", comb="Glace", why="l'éclat de glace", cible=3, impact=(6, ["perce"], "1d10 en moyenne"), impact_sats=[(7, ["froid"])],
    alt=[A("existence", True)]),
"mind-spike": dict(E24, fr="Pique mentale", verb=V("visibilite"), cible=3, impact_sats=[(P, ["traque"])]),
"phantasmal-force": dict(E24, fr="Force fantasmagorique", verb=V("existence"), cible=3, aoe={"type": "cube", "size": 10}, impact=(9, ["esprit", "illusion"], "2d8 en moyenne"),
    alt=[H("Plasma", ILL)]),
"power-word-heal": dict(E24, fr="Mot de pouvoir guérisseur", verb=V("existence"), cible=2, cond=["parole"],
    impact=(P, ["vie", "charme", "peur", "paralysie", "poison", "étourdissement"], "tous ses points de vie, les maux levés"), alt=[H("Sang", "le fluide vital")]),
"ray-of-sickness": dict(E24, fr="Rayon empoisonné", cible=3, impact_sats=[(P, ["empoisonnement"])], alt=[A("existence", True)]),
"searing-smite": dict(E24, fr="Châtiment brûlant", cible=3, no_loc=True, cond=["coup"], impact_sats=[(4, ["brûlure"])], alt=[A("existence", True)]),
"sorcerous-burst": dict(E24, fr="Explosion ensorcelée", fam="A", verb=V("existence", True), cible=3,
    options=[O(n, comb=c, why=f"l'énergie de {w}", impact=(5, [w], "1d8 en moyenne"), impact_sats=[(3, ["relance"])]) for n, w, c in ENERGIES]
            + [O("Esprit", only_base=True, impact=(5, ["esprit"], "1d8 en moyenne"), impact_sats=[(3, ["relance"])])],
    alt=[dict(fam="H", label="Forme hybride")]),
"starry-wisp": dict(E24, fr="Feu stellaire", verb=V("existence", True), cible=3, impact_sats=[(P, ["révélation"])], alt=[H("Plasma", LUM)]),
"summon-dragon": dict(E24, fr="Invocation de dragon", verb=V("trame"), cible=9, comp=["effigie"], impact=(P, ["dragon", "esprit"], "un esprit draconique allié")),
"tsunami": dict(E24, fr="Tsunami", comb="Eau", why="le raz-de-marée", cible="plein", aoe={"type": "line", "size": 300},
    impact=(33, ["choc"], "6d10 en moyenne"), impact_sats=[(15, ["recul", "mètres"])]),
"vitriolic-sphere": dict(E24, fr="Sphère vitriolique", cible="plein", aoe={"type": "sphere", "size": 20}, impact_sats=[(13, ["acide", "différé"])], alt=[A("existence", True)]),
}
FICHES.update(NEW24)

# ===== D&D 3.5 (SRD 3.5, OGL) — lot 1 : Enchantement =====
# Lanceur de référence : le plus petit lanceur capable du sort.
# Dés de vie (DV) : ramenés à des points de vie moyens, comme les dégâts — un DV vaut un d8, soit 4,5 points de vie, arrondi à l'entier.
def F35(base, fr, **kw):
    f = {k: v for k, v in FICHES[base].items() if k not in ("v24", "v35", "src", "src_idx", "grimoire", "notes")}
    f.update(src="3.5", fr=fr); f.update(kw); return f
CMD35 = [O(n, **I("mot", w, why=d)) for n, w, d in [("Approche", "approche", "venir à moi"), ("Lâche", "lâcher", "lâcher ce qu'elle tient"),
         ("À terre", "chute", "tomber à terre"), ("Fuis", "fuite", "fuir"), ("Halte", "halte", "rester immobile")]]
V35 = {
"bane": dict(qty_cible=P, impact=(1, ["chance", "coup", "peur"], "les coups moins sûrs, la peur plus proche (1 retranché aux attaques et aux sauvegardes contre la peur)")),
"bless": dict(qty_cible=P, impact=(1, ["chance", "coup", "peur"], "les coups plus sûrs, la peur tenue à distance (1 ajouté aux attaques et aux sauvegardes contre la peur)")),
"charm-person": {}, "suggestion": {}, "confusion": {}, "dominate-person": {},
"irresistible-dance": {}, "power-word-stun": {}, "dominate-monster": {}, "power-word-kill": {},
"enthrall": {}, "hideous-laughter": {}, "zone-of-truth": {}, "animal-messenger": {},
"command": dict(options=CMD35 + [dict(o, label=o["label"] + " — suprême", src_idx="command-greater", qty_cible=9) for o in CMD35]),
"sleep": dict(options=[O("Sommeil", impact=(18, ["sommeil", "vie"], "jusqu'à 18 points de vie de créatures endormies (4 DV)")),
                       O("Sommeil profond", src_idx="deep-slumber", impact=(45, ["sommeil", "vie"], "jusqu'à 45 points de vie de créatures endormies (10 DV)"))]),
"hold-person": dict(options=[O("Immobilisation de personne"), O("Immobilisation de personnes", src_idx="hold-person-mass", qty_cible=P)]),
"hold-monster": dict(options=[O("Immobilisation de monstre"), O("Immobilisation de monstres", src_idx="hold-monster-mass", qty_cible=P)]),
"charm-monster": dict(options=[O("Charme-monstre"), O("Charme-monstre de groupe", src_idx="charm-monster-mass", impact=(135, ["charme", "vie"], "jusqu'à 135 points de vie de créatures charmées (30 DV)"))]),
"aid": dict(qty_cible=None, impact=(8, ["vie", "temporaire"], "1d8 + 3 en moyenne"), impact_sats=[(1, ["courage"])]),
"calm-emotions": dict(cond=[], options=None, impact=(P, ["calme", "fureur", "peur", "confusion"], "fureur, peur et confusion suspendues")),
"heroism": dict(impact=(2, ["courage", "coup", "résistance", "aptitude"], "plus sûre en tout ce qu'elle tente (+2 aux attaques, sauvegardes et compétences)"), impact_sats=[]),
"modify-memory": dict(cond_sats=[], impact_sats=[(5, ["minutes"])]),
"feeblemind": dict(impact=(P, ["intellect", "charisme"], "Intelligence et Charisme ramenés à 1"), impact_sats=[]),
"geas": dict(src_idx="geas-quest", name="Geas/Quest", dur=(11, "JOURS"), fin=["accomplissement"], impact_sats=[(11, ["blessure", "jour"])]),
"mass-suggestion": dict(src_idx="suggestion-mass", name="Suggestion, Mass", qty_cible=11),
"dominate-beast": dict(src_idx="dominate-animal", name="Dominate Animal"),
"antipathy-sympathy": dict(src_idx="antipathy", alt=[dict(src_idx="sympathy")]),
}
for k, v in V35.items(): FICHES[k]["v35"] = v
SYM = lambda fr, **kw: {**dict(src="3.5", fr=fr, verb=V("visibilite"), cible=P, aoe={"type": "sphere", "size": 60}, cond=["déclencheur"],
                            dur=(P, None), fin=["déclenchement"]), **kw}
NEW35 = {
"daze": dict(src="3.5", fr="Hébétement", verb=V("ordre", True), cible=3, cond=["humanoïde", "seuil"], cond_sats=[(18, ["vie"])], impact=(P, ["hébétude"], "hébétée, elle reste sans rien faire un instant")),
"daze-monster": dict(src="3.5", fr="Hébétement de monstre", verb=V("ordre", True), cible=3, cond=["vivant", "seuil"], cond_sats=[(27, ["vie"])], impact=(P, ["hébétude"], "hébétée, elle reste sans rien faire un instant")),
"lullaby": dict(src="3.5", fr="Berceuse", verb=V("intensite", True), cible=P, impact=(5, ["torpeur", "vigilance"], "moins vigilante, plus prompte au sommeil (5 retranché à la Perception, 2 aux sauvegardes contre le sommeil)"),
    alt=[H("Pollen", "ce qui se respire et assoupit")]),
"calm-animals": dict(src="3.5", fr="Apaisement des animaux", verb=V("ordre"), cible=P, cond=["bête", "instinct"], impact=(27, ["calme", "vie"], "jusqu'à 27 points de vie d'animaux apaisés (2d4 + 1 DV)")),
"charm-animal": F35("charm-person", "Charme-animal", cond=["bête"]),
"confusion-lesser": F35("confusion", "Confusion mineure", cible=3),
"hypnotism": dict(src="3.5", fr="Hypnose", verb=V("relation"), cible=P, cond=["vivant"], impact=(23, ["fascination", "vie"], "jusqu'à 23 points de vie de créatures fascinées (2d4 DV)")),
"animal-trance": dict(src="3.5", fr="Transe animale", verb=V("relation"), cible=P, cond=["bête", "instinct"], impact=(32, ["fascination", "vie"], "jusqu'à 32 points de vie d'animaux fascinés (2d6 DV)")),
"hold-animal": F35("hold-person", "Immobilisation d'animal", cond=["bête"]),
"touch-of-idiocy": dict(src="3.5", fr="Contact débilitant", verb=V("intensite", True), cible=3, impact=(4, ["intellect", "sagesse", "charisme"], "1d6 retranché à chacune")),
"good-hope": dict(src="3.5", fr="Espoir", verb=V("intensite"), cible=2, qty_cible=7, impact=(2, ["espoir", "coup", "résistance", "aptitude", "blessure"], "l'espoir qui porte en toute chose (+2 aux attaques, dégâts, sauvegardes et tests)")),
"prayer": dict(src="3.5", fr="Prière", verb=V("intensite"), cible=P, impact=(1, ["chance", "coup", "résistance", "aptitude", "blessure"], "+1 aux alliés, 1 retranché aux ennemis")),
"rage": dict(src="3.5", fr="Rage", verb=V("intensite"), cible=2, qty_cible=1, impact=(2, ["fureur", "force", "constitution"], "+2 en Force et en Constitution, la garde baissée")),
"crushing-despair": dict(src="3.5", fr="Désespoir foudroyant", verb=V("intensite", True), cible=P, impact=(2, ["désespoir", "coup", "résistance", "aptitude", "blessure"], "le désespoir qui pèse sur toute chose (2 retranché aux attaques, dégâts, sauvegardes et tests")),
"geas-lesser": F35("geas", "Quête mineure", cond=["compréhension", "seuil"], cond_sats=[(32, ["vie"])], impact_sats=[(2, ["aptitude", "jour"])]),
"mind-fog": dict(src="3.5", fr="Brume mentale", verb=V("intensite", True), cible=P, impact=(10, ["brume", "sagesse", "volonté"], "10 retranché à la Sagesse et à la volonté")),
"song-of-discord": dict(src="3.5", fr="Chant de discorde", verb=V("relation", True), cible=P, impact=(2, ["discorde", "fractionné"], "une chance sur deux de frapper son voisin")),
"heroism-greater": F35("heroism", "Héroïsme suprême", impact=(4, ["courage", "coup", "résistance", "aptitude"], "bien plus sûre en tout ce qu'elle tente (+4 aux attaques, sauvegardes et compétences)"),
    impact_sats=[(11, ["vie", "temporaire"]), (P, ["intrépidité"])]),
"insanity": F35("confusion", "Aliénation mentale", cible=3, dur=(P, None)),
"power-word-blind": F35("power-word-stun", "Mot de pouvoir aveuglant", dur=(P, "VIE"), cond_sats=[(200, ["vie"])], impact=(P, ["aveuglement"], "aveuglée")),
"demand": F35("sending", "Exigence", impact=(P, ["message", "conduite"], "un message et la conduite suggérée")),
"binding": dict(src="3.5", fr="Entrave", verb=V("mouvement", True), cible=3, dur=(P, None),
    options=[O(n, **I("entrave", w, why=d)) for n, w, d in [("Enchaînement", "chaînes", "enchaînée sur place"), ("Sommeil", "sommeil", "endormie"),
             ("Sommeil enchaîné", "torpeur", "endormie et enchaînée"),
             ("Immobilisation", "paralysie", "paralysée"), ("Emprisonnement", "prison", "enfermée sous terre"), ("Rétrécissement", "gemme", "rétrécie dans une gemme")]]),
"symbol-of-sleep": SYM("Symbole de sommeil", cond=["déclencheur", "seuil"], cond_sats=[(45, ["vie"])], impact=(P, ["sommeil"], "un sommeil profond")),
"symbol-of-persuasion": SYM("Symbole de persuasion", impact=(P, ["charme"], "charmée")),
"symbol-of-stunning": SYM("Symbole d'étourdissement", impact=(P, ["étourdissement"], "étourdie")),
"symbol-of-insanity": SYM("Symbole d'aliénation", impact=(P, ["folie"], "aliénée à jamais")),
}
FICHES.update(NEW35)

# ===== D&D 3.5 — lot 2 : Divination =====
# Alignement : le système moral universel est écarté (ce qui est bon à Galombar ne l'est pas à Hodolin), pas les sorts. Ils se transposent :
#  bien / mal  → bienveillance / hostilité envers le lanceur : Cible 2 (allié) / Cible 3 (ennemi), relatives par nature ;
#  loi / chaos → l'énergie astrale lumineuse (l'Étoile) / ténébreuse (l'Abysse), et ce qui en est chargé.
AURA = (P, ["aura", "présence", "force"], "présence, nombre et force des auras")
V35b = {
"detect-magic": {}, "comprehend-languages": {}, "identify": {}, "speak-with-animals": {}, "augury": {}, "detect-thoughts": {},
"locate-object": {}, "see-invisibility": {}, "speak-with-plants": {}, "tongues": {}, "arcane-eye": {}, "divination": {},
"locate-creature": {}, "telepathic-bond": {}, "find-the-path": {}, "legend-lore": {}, "true-seeing": {},
"guidance": dict(impact=(1, ["chance", "aptitude"], "un léger coup de pouce à ce qu'on entreprend (1 ajouté à un test)")),
"true-strike": dict(impact=(20, ["faille", "coup"], "20 ajouté à la prochaine attaque")),
"find-traps": dict(impact=(1, ["piège", "fouille"], "la moitié du niveau ajoutée à la fouille des pièges")),
"scrying": dict(loc=(P, None, "n'importe où")),
"commune": dict(qty=9),
"commune-with-nature": dict(loc=(14, "KILOMETRES", "14 km (9 miles)")),
"contact-other-plane": dict(qty=4, impact_sats=[(8, ["intellect", "charisme"])]),
"foresight": dict(impact=(2, ["avenir", "vigilance", "garde"], "jamais surprise, 2 ajouté à la défense")),
"detect-poison-and-disease": dict(src_idx="detect-poison", name="Detect Poison", impact=(P, ["poison", "présence"], "la présence du poison, puis sa nature")),
"detect-evil-and-good": dict(src_idx="detect-evil", cible_note=[], notes=[], impact=AURA,
    options=[O("Hostilité", cible=3, qty_cible=P), O("Bienveillance", src_idx="detect-good", cible=2, qty_cible=P),
             O("Lumineux", src_idx="detect-law", cible=P, cible_note=["lumineux"]), O("Ténébreux", src_idx="detect-chaos", cible=P, cible_note=["ténébreux"])]),
"clairvoyance": dict(src_idx="clairaudience-clairvoyance", name="Clairaudience/Clairvoyance",
    options=[O("Clairaudience", impact=(P, ["ouïe"], "entendre par le capteur")), O("Clairvoyance", impact=(P, ["vue"], "voir par le capteur"))]),
}
for k, v in V35b.items(): FICHES[k]["v35"] = v
DET = lambda fr, *w, why="", **kw: {**dict(src="3.5", fr=fr, verb=V("visibilite"), cible=P, impact=(P, list(w), why)), **kw}
NEW35b = {
"know-direction": dict(src="3.5", fr="Orientation", verb=V("visibilite"), cible=1, impact=(P, ["nord"], "la direction du nord")),
"read-magic": dict(src="3.5", fr="Lecture de la magie", verb=V("visibilite"), cible=1, cible_obj=["écrit"], impact=(P, ["sens", "magie"], "les écrits magiques déchiffrés")),
"detect-animals-or-plants": DET("Détection des animaux ou des plantes", options=[O("Animaux", **I("présence", "bête", why="présence, nombre et position d'une espèce animale")),
    O("Plantes", **I("présence", "plante", why="présence, nombre et position d'une espèce végétale"))]),
"detect-secret-doors": DET("Détection des passages secrets", "passage", "secret", why="présence, nombre et position des passages dérobés"),
"detect-snares-and-pits": DET("Détection des collets et des fosses", "piège", "nature", why="les pièges naturels, fosses et éboulis"),
"detect-undead": DET("Détection des morts-vivants", "aura", "présence", "force", cible=9, cible_note=["MORTVIVANT"], why="présence, nombre et force des auras"),
"status": dict(src="3.5", fr="Rapport", verb=V("relation"), cible=2, impact=(P, ["lien", "état", "direction"], "position et état des compagnons")),
"arcane-sight": dict(src="3.5", fr="Vision magique", verb=V("visibilite"), cible=1, impact=(P, ["aura", "force"], "les auras magiques et leur force"), impact_sats=[(36, ["mètres"])]),
"arcane-sight-greater": dict(src="3.5", fr="Vision magique suprême", verb=V("visibilite"), cible=1, impact=(P, ["aura", "force", "sort"], "les auras, et les sorts actifs sur chacun"), impact_sats=[(36, ["mètres"])]),
"detect-scrying": DET("Détection de la scrutation", "capteur", "scrutation", why="les capteurs magiques, parfois le scrutateur"),
"discern-lies": dict(src="3.5", fr="Détection du mensonge", verb=V("visibilite"), cible=3, impact=(P, ["mensonge"], "le mensonge délibéré décelé")),
"prying-eyes": dict(src="3.5", fr="Yeux indiscrets", verb=V("visibilite"), qty=12, impact=(P, ["OEIL", "vision", "rapport"], "des yeux volants qui reviennent faire rapport")),
"prying-eyes-greater": dict(src="3.5", fr="Yeux indiscrets suprêmes", verb=V("visibilite"), qty=18, impact=(P, ["OEIL", "vision", "vérité", "rapport"], "des yeux volants qui voient les choses telles qu'elles sont")),
"analyze-dweomer": dict(src="3.5", fr="Analyse d'enchantement", verb=V("visibilite"), cible=1, cible_obj=["objet"], comp=["gemme"], impact=(P, ["propriété", "enchantement"], "propriétés et sorts en cours")),
"stone-tell": dict(src="3.5", fr="Pierre parlante", comb="Roche", why="la pierre", cible=P, impact=(P, ["parole", "pierre"], "parler aux pierres"), alt=[A("relation")]),
"scrying-greater": F35("scrying", "Scrutation suprême", impact=(P, ["vue", "ouïe", "sort"], "voir et entendre la cible, et lancer des détections à travers")),
"vision": F35("legend-lore", "Vision", comp=[], impact=(P, ["légende", "vision"], "le savoir légendaire, en une vision")),
"discern-location": dict(src="3.5", fr="Localisation infaillible", verb=V("visibilite"), cible=4, impact=(P, ["lieu", "nom"], "le nom exact du lieu où se trouve la cible")),
"moment-of-prescience": dict(src="3.5", fr="Moment de prescience", fam="R", art="chronomancie", verb=V("visibilite"), cible=1, impact=(15, ["avenir", "chance"], "un instant d'avenir entrevu, au moment décisif (15 ajouté à un seul jet)"), fin=["usage"]),
}
FICHES.update(NEW35b)

# ===== D&D 3.5 — lot 3 : Abjuration =====
# Un sort « contre » l'alignement est un seul sort en trois formes, qui ne diffèrent que par la catégorie visée (Condition) :
# l'hostile (contre le mal comme contre le bien : même glyphe), le lumineux (contre la loi), le ténébreux (contre le chaos).
SEP = V("relation", True)
GARDE = lambda n: (n, ["garde", "résistance"], f"mieux gardée et plus résistante ({n} ajouté à la CA et aux sauvegardes)")
EN35 = [("Acide", "acide"), ("Froid", "froid"), ("Foudre", "foudre"), ("Feu", "feu"), ("Tonnerre", "tonnerre")]
TRI = lambda hos, lum, ten: [O("Contre l'hostile", src_idx=hos, cond=["hostile"]), O("Contre le lumineux", src_idx=lum, cond=["lumineux"]),
                            O("Contre le ténébreux", src_idx=ten, cond=["ténébreux"])]
V35c = {
"alarm": {}, "sanctuary": {}, "shield": dict(impact=(4, ["garde", "projectile"], "4 ajouté à la défense, insensible au projectile magique")), "shield-of-faith": {}, "arcane-lock": {}, "dispel-magic": {}, "nondetection": {},
"freedom-of-movement": {}, "remove-curse": {}, "antilife-shell": {}, "antimagic-field": {}, "guards-and-wards": {},
"banishment": {}, "sequester": {}, "mind-blank": {}, "imprisonment": {},
"resistance": dict(impact=(1, ["garde", "résistance"], "une résistance affermie (1 ajouté aux sauvegardes)"), fin=[]),
"glyph-of-warding": dict(options=[O("Glyphe explosif", impact=(9, ["piège", "explosion"], "2d8 en moyenne"), impact_sats=[]),
                                  O("Glyphe de sort", impact=(P, ["piège", "sort"], "un sort enfermé"), impact_sats=[(3, ["seuil", "niveau"])]),
                                  O("Glyphe explosif suprême", src_idx="glyph-of-warding-greater", impact=(23, ["piège", "explosion"], "5d8 en moyenne"), impact_sats=[]),
                                  O("Glyphe de sort suprême", src_idx="glyph-of-warding-greater", impact=(P, ["piège", "sort"], "un sort enfermé"), impact_sats=[(6, ["seuil", "niveau"])])]),
"protection-from-energy": dict(impact_sats=[(60, ["plafond"])]),
"stoneskin": dict(impact=(10, ["garde", "coup"], "10 retranché à chaque coup d'arme"), impact_sats=[(70, ["plafond"])]),
"forbiddance": dict(impact_sats=[(21, ["hostile"])]),
"globe-of-invulnerability": dict(options=[O("Globe d'invulnérabilité", impact_sats=[(4, ["seuil", "niveau"])]),
                                          O("Globe d'invulnérabilité partielle", src_idx="globe-of-invulnerability-lesser", impact_sats=[(3, ["seuil", "niveau"])])]),
"protection-from-evil-and-good": dict(src_idx="protection-from-evil", comp=[], impact=GARDE(2), impact_sats=[(P, ["contrôle"]), (P, ["invoqué"])],
                                      options=TRI("protection-from-evil", "protection-from-law", "protection-from-chaos")),
"magic-circle": dict(src_idx="magic-circle-against-evil", comp=[], cible=P, cible_note=[], impact=GARDE(2), impact_sats=[(P, ["contrôle"]), (P, ["invoqué", "barrière"])],
                     options=TRI("magic-circle-against-evil", "magic-circle-against-law", "magic-circle-against-chaos")),
"dispel-evil-and-good": dict(src_idx="dispel-evil", cible=1, impact=(4, ["garde"], "4 ajouté à la défense"), impact_sats=[(P, ["renvoi"]), (P, ["dissipation"])],
                             options=TRI("dispel-evil", "dispel-law", "dispel-chaos")),
"holy-aura": dict(impact=GARDE(4), options=[O("Aura sacrée — contre l'hostile", cond=["hostile"], impact_sats=[(25, ["magie"]), (P, ["aveuglement"])]),
                  O("Aura impie — contre l'hostile", src_idx="unholy-aura", cond=["hostile"], impact_sats=[(25, ["magie"]), (4, ["force", "faiblesse"])]),
                  O("Manteau du chaos — contre le lumineux", src_idx="cloak-of-chaos", cond=["lumineux"], impact_sats=[(25, ["magie"]), (P, ["confusion"])]),
                  O("Bouclier de la loi — contre le ténébreux", src_idx="shield-of-law", cond=["ténébreux"], impact_sats=[(25, ["magie"]), (P, ["lenteur"])])]),
"private-sanctum": dict(src_idx="mages-private-sanctum", name="Mage's Private Sanctum"),
"prismatic-wall": dict(options=[O("Mur", aoe={"type": "line", "size": 60}), O("Sphère", src_idx="prismatic-sphere", aoe={"type": "sphere", "size": 10})]),
}
for k, v in V35c.items(): FICHES[k]["v35"] = v
NEW35c = {
"endure-elements": dict(src="3.5", fr="Endurance aux énergies destructives", verb=SEP, cible=2, impact=(P, ["chaleur", "froid", "climat"], "à l'aise par tout climat")),
"entropic-shield": dict(src="3.5", fr="Bouclier entropique", verb=SEP, cible=1, impact=(5, ["garde", "trait", "fractionné"], "une chance sur cinq de manquer à distance")),
"hide-from-animals": dict(src="3.5", fr="Invisibilité pour les animaux", verb=V("visibilite", True), cible=2, cond=["bête"], impact=(P, ["dissimulation"], "ni vue, ni ouïe, ni odorat"), fin=["agression"]),
"hide-from-undead": dict(src="3.5", fr="Invisibilité pour les morts-vivants", verb=V("visibilite", True), cible=2, cond=["MORTVIVANT"], impact=(P, ["dissimulation"], "ni vue, ni ouïe, ni odorat"), fin=["agression"]),
"hold-portal": dict(src="3.5", fr="Verrouillage", verb=V("ordre"), cible=1, cible_obj=["porte"], impact=(P, ["verrou"], "fermée comme à clé")),
"remove-fear": dict(src="3.5", fr="Délivrance de la peur", verb=V("qualite"), cible=2, impact=(4, ["courage", "peur"], "4 ajouté contre la peur, la peur suspendue")),
"obscure-object": dict(src="3.5", fr="Camouflage d'objet", verb=V("visibilite", True), cible=1, cible_obj=["objet"], impact=(P, ["divination"], "insaisissable à la scrutation")),
"protection-from-arrows": dict(src="3.5", fr="Protection contre les projectiles", verb=SEP, cible=2, impact=(10, ["garde", "trait"], "10 retranché à chaque coup à distance"), impact_sats=[(30, ["plafond"])]),
"resist-energy": dict(src="3.5", fr="Résistance aux énergies destructives", verb=SEP, cible=2,
    options=[O(n, impact=(10, ["résistance", w], "10 retranché à chaque coup")) for n, w in EN35]),
"shield-other": dict(src="3.5", fr="Protection d'autrui", verb=V("relation"), cible=2, comp=["anneau", "platine"], impact=(1, ["garde", "résistance", "partage"], "1 ajouté, la moitié de ses blessures pour moi")),
"undetectable-alignment": dict(src="3.5", fr="Intention indétectable", verb=V("visibilite", True), cible=2, impact=(P, ["hostile", "astral", "divination"], "hostilité et charge astrale insaisissables")),
"explosive-runes": dict(src="3.5", fr="Runes explosives", verb=V("existence", True), cible=1, cible_obj=["écrit"], cond=["lecture"], impact=(21, ["force", "explosion"], "6d6 en moyenne")),
"antiplant-shell": dict(src="3.5", fr="Coquille antivégétale", verb=V("force", True), cible=P, impact=(P, ["barrière", "plante"], "les plantes tenues au dehors")),
"dimensional-anchor": dict(src="3.5", fr="Ancre dimensionnelle", verb=V("mouvement", True), cible=3, impact=(P, ["passage", "plan"], "nul voyage extradimensionnel")),
"fire-trap": dict(src="3.5", fr="Piège de feu", fam="H", comb="Feu", why="le feu", cible=1, cible_obj=["objet"], cond=["ouverture"], comp=["or"], impact=(10, ["feu", "explosion"], "1d4 + 7 en moyenne")),
"repel-vermin": dict(src="3.5", fr="Répulsif", verb=V("force", True), cible=P, impact=(P, ["barrière", "vermine"], "la vermine tenue au dehors"), impact_sats=[(7, ["douleur"])]),
"spell-immunity": dict(src="3.5", fr="Immunité contre les sorts", verb=SEP, cible=2,
    options=[O("Immunité contre les sorts", impact=(1, ["immunité", "sort"], "un sort désigné sans effet"), impact_sats=[(4, ["seuil", "niveau"])]),
             O("Immunité contre les sorts suprême", src_idx="spell-immunity-greater", impact=(3, ["immunité", "sort"], "trois sorts désignés sans effet"), impact_sats=[(8, ["seuil", "niveau"])])]),
"atonement": dict(src="3.5", fr="Pénitence", verb=V("qualite"), cible=2, comp=["chapelet"], cond=["repentir"], impact=(P, ["faute", "pardon"], "la faute levée, les dons rendus")),
"break-enchantment": dict(src="3.5", fr="Délivrance", verb=V("qualite"), cible=2, qty_cible=9, impact=(P, ["enchantement", "transmutation", "malédiction"], "libérée des sorts et des malédictions")),
"dismissal": dict(src="3.5", fr="Renvoi", verb=V("trame", True), cible=9, impact=(P, ["exil"], "renvoyée sur son plan"), impact_sats=[(5, ["égarement", "fractionné"])]),
"spell-resistance": dict(src="3.5", fr="Résistance à la magie", verb=SEP, cible=2, impact=(21, ["résistance", "magie"], "résistance à la magie de 21")),
"dispel-magic-greater": dict(src="3.5", fr="Dissipation suprême", verb=SEP, cible=P, impact=(P, ["sort", "dissipation", "malédiction"], "les sorts prennent fin, malédictions comprises")),
"repulsion": dict(src="3.5", fr="Répulsion", verb=V("force", True), cible=P, comp=["fer"], impact=(P, ["répulsion"], "nul ne peut s'approcher")),
"spell-turning": dict(src="3.5", fr="Renvoi des sorts", verb=V("force", True), cible=1, impact=(9, ["sort", "renvoi"], "1d4 + 6 niveaux de sorts renvoyés")),
"dimensional-lock": dict(src="3.5", fr="Verrou dimensionnel", verb=V("mouvement", True), cible=P, impact=(P, ["passage", "plan"], "nul voyage extradimensionnel dans la zone")),
"protection-from-spells": dict(src="3.5", fr="Protection contre les sorts", verb=SEP, cible=2, qty_cible=3, comp=["diamant"], consumed=True, impact=(8, ["résistance", "sort"], "une résistance accrue à la magie (8 ajouté aux sauvegardes contre les sorts)")),
"repel-metal-or-stone": dict(src="3.5", fr="Répulsion du métal et de la pierre", verb=V("force", True), cible=1, cible_obj=["métal", "pierre"], impact=(P, ["répulsion"], "repoussés jusqu'au bout de la portée")),
"freedom": dict(src="3.5", fr="Liberté", verb=V("mouvement"), cible=2, impact=(P, ["libération", "entrave", "prison"], "délivrée de toute entrave, même emprisonnée")),
"mages-disjunction": dict(src="3.5", fr="Disjonction", verb=V("ordre", True), cible=P, impact=(P, ["magie", "disjonction"], "sorts défaits, objets magiques éteints")),
}
FICHES.update(NEW35c)

# ===== D&D 3.5 — lot 4 : Invocation =====
# Règle des échelons : des variantes qui ne diffèrent que par les chiffres (intensité, quantité, seuil) sont un même sort, une page,
# une forme par échelon ; si l'effet change, entrée séparée.
# Êtres convoqués : puissance = facteur de puissance estimé de la meilleure créature de chaque liste 3.5 (même échelle que la 5e).
ROM = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
CR35 = [0.5, 1, 2, 4, 5, 7, 9, 11, 12]
def _pw(p, w):
    return (2, w + ["fractionné"], "puissance ½") if p == 0.5 else (p, w, f"puissance {p}")
def SUMMON(prefix, kinds):
    out = []
    for n in range(1, 10):
        ch = [(n, 1)] + ([(n - 1, 2)] if n >= 2 else []) + ([(n - 2, 4)] if n >= 3 else [])
        for lab, w in kinds:
            for r, q in ch:
                p = CR35[r - 1]; ps = "½" if p == 0.5 else str(p)
                o = O(f"Rang {ROM[n-1]} — {q} être{'s' if q > 1 else ''} de puissance {ps}" + (f" — {lab}" if lab else ""),
                      src_idx=f"{prefix}-{ROM[n-1].lower()}", impact=_pw(p, list(w)))
                if q > 1: o["impact_sats"] = [(q, ["nombre"])]
                out.append(o)
    return out
CURE = lambda: [O("Soins mineurs", src_idx="cure-minor-wounds", impact=(1, None, "1 point de vie")),
                O("Soins légers", src_idx="cure-light-wounds", impact=(6, None, "1d8 + 1 en moyenne")),
                O("Soins modérés", src_idx="cure-moderate-wounds", impact=(12, None, "2d8 + 3 en moyenne")),
                O("Soins importants", src_idx="cure-serious-wounds", impact=(19, None, "3d8 + 5 en moyenne")),
                O("Soins intensifs", src_idx="cure-critical-wounds", impact=(25, None, "4d8 + 7 en moyenne"))]
CUREM = lambda: [O("Soins légers de groupe", src_idx="cure-light-wounds-mass", qty_cible=9, impact=(14, None, "1d8 + 9 en moyenne")),
                 O("Soins modérés de groupe", src_idx="cure-moderate-wounds-mass", qty_cible=11, impact=(20, None, "2d8 + 11 en moyenne")),
                 O("Soins importants de groupe", src_idx="cure-serious-wounds-mass", qty_cible=13, impact=(27, None, "3d8 + 13 en moyenne")),
                 O("Soins intensifs de groupe", src_idx="cure-critical-wounds-mass", qty_cible=15, impact=(33, None, "4d8 + 15 en moyenne"))]
V35d = {
"acid-splash": {}, "grease": {}, "mage-armor": {}, "unseen-servant": {}, "acid-arrow": {}, "web": {}, "create-food-and-water": {},
"phantom-steed": {}, "sleet-storm": {}, "stinking-cloud": {}, "dimension-door": {}, "raise-dead": {}, "secret-chest": {},
"tree-stride": {}, "wall-of-stone": {},
"black-tentacles": dict(impact=(8, ["étreinte", "choc"], "une étreinte qui broie sans relâche (1d6 + 4 en moyenne par tour)")),
"cloudkill": dict(impact=(P, ["mort", "poison"], "les plus faibles tués"), impact_sats=[(27, ["seuil", "vie"]), (3, ["constitution"])]),
"insect-plague": dict(impact=(P, ["nuée", "insectes"], "des nuées de criquets"), impact_sats=[(3, ["nombre"])]),
"wall-of-thorns": dict(impact=(P, ["épine", "mur"], "un mur de ronces qui déchire et entrave")),
"heal": dict(impact=(110, None, "10 par niveau, soit 110 points de vie, et les maux levés")),
"heroes-feast": {}, "transport-via-plants": {}, "word-of-recall": {}, "instant-summons": {}, "plane-shift": {},
"regenerate": {}, "resurrection": {}, "incendiary-cloud": {}, "maze": {}, "gate": dict(comp=[]), "storm-of-vengeance": {},
"teleportation-circle": {}, "true-resurrection": {},
"cure-wounds": dict(src_idx="cure-light-wounds", name="Cure Wounds", options=CURE()),
"mass-cure-wounds": dict(src_idx="cure-light-wounds-mass", name="Mass Cure Wounds", no_aoe=True, options=CUREM()),
"mass-heal": dict(src_idx="heal-mass", name="Mass Heal", impact=(170, None, "10 par niveau, soit 170 points de vie chacun")),
"lesser-restoration": dict(src_idx="restoration-lesser", options=[
    O("Faculté", impact=(P, ["aptitude", "fatigue"], "une faculté rendue, la fatigue levée")),
    O("Maladie", src_idx="remove-disease", impact=(P, ["maladie"], "toutes les maladies levées")),
    O("Cécité", src_idx="remove-blindness-deafness", impact=(P, ["aveuglement"], "la cécité levée")),
    O("Surdité", src_idx="remove-blindness-deafness", impact=(P, ["surdité"], "la surdité levée")),
    O("Paralysie", src_idx="remove-paralysis", impact=(P, ["paralysie"], "la paralysie levée")),
    O("Poison", src_idx="neutralize-poison", impact=(P, ["poison"], "le poison neutralisé"))]),
"greater-restoration": dict(src_idx="restoration", options=[
    O("Restauration", impact=(1, ["aptitude", "niveau"], "un niveau perdu rendu")),
    O("Restauration suprême", src_idx="restoration-greater", comp=[], impact=(P, ["aptitude", "niveau"], "tous les niveaux perdus rendus"))]),
"teleport": dict(options=[O("Téléportation"), O("Téléportation suprême", src_idx="teleport-greater")]),
"planar-ally": dict(src_idx="planar-ally-lesser", options=[O("Allié planaire mineur", impact=(27, ["être", "vie"], "jusqu'à 27 points de vie (6 DV)")),
    O("Allié planaire", src_idx="planar-ally", impact=(54, ["être", "vie"], "jusqu'à 54 points de vie (12 DV)")),
    O("Allié planaire majeur", src_idx="planar-ally-greater", impact=(81, ["être", "vie"], "jusqu'à 81 points de vie (18 DV)"))]),
"planar-binding": dict(src_idx="planar-binding-lesser", comp=[], options=[O("Lien planaire mineur", impact=(27, ["service", "vie"], "jusqu'à 27 points de vie (6 DV)")),
    O("Lien planaire", src_idx="planar-binding", impact=(54, ["service", "vie"], "jusqu'à 54 points de vie (12 DV)")),
    O("Lien planaire majeur", src_idx="planar-binding-greater", impact=(81, ["service", "vie"], "jusqu'à 81 points de vie (18 DV)"))]),
"create-or-destroy-water": dict(src_idx="create-water", name="Create Water", options=None, impact=(8, ["eau", "litres", "création"], "8 litres créés")),
"fog-cloud": dict(options=[O("Nappe de brouillard"), O("Brume de dissimulation", src_idx="obscuring-mist")]),
"faithful-hound": dict(src_idx="mages-faithful-hound", name="Mage's Faithful Hound", impact=(10, ["morsure"], "2d6 + 3 en moyenne")),
"magnificent-mansion": dict(src_idx="mages-magnificent-mansion", name="Mage's Magnificent Mansion"),
}
for k, v in V35d.items(): FICHES[k]["v35"] = v
INV = lambda **kw: {**dict(src="3.5", verb=V("trame")), **kw}
NEW35d = {
"summon-monster-i": INV(fr="Convocation de monstres", cible=9, options=SUMMON("summon-monster", [("lumineux", ["être", "lumineux"]), ("ténébreux", ["être", "ténébreux"])])),
"summon-natures-ally-i": INV(fr="Convocation d'alliés naturels", cible=7, cible_note=["bête"], options=SUMMON("summon-natures-ally", [("", ["bête"])])),
"summon-instrument": INV(fr="Convocation d'instrument", cible=1, cible_obj=["instrument"], impact=(P, ["instrument"], "un instrument de musique")),
"mount": INV(fr="Monture", cible=7, impact=(P, ["monture", "cheval"], "un cheval ou un poney sellé")),
"summon-swarm": INV(fr="Convocation de nuées", cible=P, options=[O(n, impact=(P, ["nuée", w], d)) for n, w, d in
    [("Chauves-souris", "chauve-souris", "une nuée de chauves-souris"), ("Rats", "rat", "une nuée de rats"), ("Araignées", "araignée", "une nuée d'araignées")]]),
"creeping-doom": INV(fr="Fléau rampant", cible=P, qty=6, impact=(P, ["nuée", "mille-pattes"], "six nuées de mille-pattes")),
"elemental-swarm": dict(src="3.5", fr="Nuée d'élémentaires", fam="H", cible=P, options=[O(n, comb=c, why=f"les élémentaires de {d}", impact=(9, ["élémentaire"], "2d4 grands, puis 1d4 énormes, puis un supérieur"))
    for n, c, d in [("Air", "Air", "l'air"), ("Terre", "Terre", "la terre"), ("Feu", "Feu", "feu"), ("Eau", "Eau", "l'eau")]]),
"shambler": dict(src="3.5", fr="Tertres errants", comb="Plante", why="les plantes", cible=P, impact=(50, ["tertre", "vie"], "des tertres de 50 points de vie chacun (11 DV)"), impact_sats=[(5, ["nombre"])]),
"delay-poison": dict(src="3.5", fr="Ralentissement du poison", verb=V("nature", True), cible=2, impact=(P, ["poison", "sursis"], "le poison sans effet jusqu'au terme")),
"glitterdust": dict(src="3.5", fr="Poussière scintillante", verb=V("visibilite"), cible=P, impact=(P, ["aveuglement", "invisible"], "aveuglées, l'invisible révélé")),
"heal-mount": dict(src="3.5", fr="Guérison de la monture", verb=V("existence"), cible=2, cond=["monture"], impact=(P, ["vie", "maladie", "aveuglement"], "sa monture entièrement guérie"), alt=[H("Sang", "le fluide vital")]),
"sepia-snake-sigil": dict(src="3.5", fr="Sceau du serpent", verb=V("mouvement", True), cible=1, cible_obj=["écrit"], cond=["lecture"], comp=["ambre"], impact=(P, ["paralysie", "serpent"], "le lecteur figé dans l'ambre")),
"secure-shelter": dict(src="3.5", fr="Abri", verb=V("existence"), cible=P, impact=(P, ["abri", "chaumière"], "une chaumière solide")),
"solid-fog": dict(src="3.5", fr="Brouillard dense", comb="Brume", why="le brouillard", cible=P, impact=(P, ["brouillard", "obscurité", "lenteur"], "zone obscurcie où l'on avance à peine")),
"acid-fog": dict(src="3.5", fr="Brouillard acide", comb="Acide sulfurique", why="l'acide", cible=P, impact=(7, ["acide", "brouillard", "lenteur"], "un brouillard qui ronge sans relâche (2d6 en moyenne par tour)")),
"fire-seeds": dict(src="3.5", fr="Graines de feu", comb="Feu", why="le feu", cible=1, cible_obj=["graine"],
    options=[O("Glands explosifs", impact=(39, ["feu", "jet"], "11d6 en moyenne, en quatre glands")), O("Baies explosives", impact=(16, ["feu", "explosion"], "1d8 + 11 en moyenne par baie"), impact_sats=[(8, ["nombre"])])]),
"wall-of-iron": dict(src="3.5", fr="Mur de fer", comb="Acier", why="le métal du mur", cible=P, comp=["fer", "or"], impact=(P, ["fer", "mur"], "un mur de fer"), impact_sats=[(35, ["chute"])]),
"phase-door": dict(src="3.5", fr="Passage dimensionnel", fam="R", art="spatiomancie", verb=V("mouvement"), cible=1, impact=(P, ["passage", "éthéré"], "un passage à travers la paroi")),
"teleport-object": dict(src="3.5", fr="Téléportation d'objet", verb=V("mouvement"), cible=1, cible_obj=["objet"], impact=(P, ["téléportation"], "l'objet envoyé au loin")),
"trap-the-soul": dict(src="3.5", fr="Piège à âme", verb=V("mouvement", True), cible=3, comp=["gemme"], impact=(P, ["âme", "gemme"], "l'être enfermé dans la gemme")),
"refuge": dict(src="3.5", fr="Refuge", fam="R", art="spatiomancie", verb=V("mouvement"), cible=1, cible_obj=["objet"], cond=["mot"], comp=["gemme"], impact=(P, ["retour", "demeure"], "son porteur ramené à ta demeure")),
}
FICHES.update(NEW35d)

# ===== D&D 3.5 — lot 5 : Évocation =====
LUMH = lambda: [H("Plasma", LUM)]
WORD = lambda lab, idx, who, *w: O(lab, src_idx=idx, cond=[who], impact=(P, list(w) + ["mort"], "selon la vie qui reste, jusqu'à la mort"))
SMITE = lambda lab, idx, who, w, d: O(lab, src_idx=idx, cond=[who], impact=(14, [w], f"3d8 en moyenne, puis {d}"))
V35e = {k: {} for k in ["dancing-lights", "light", "ray-of-frost", "burning-hands", "divine-favor", "faerie-fire", "floating-disk", "magic-missile",
    "produce-flame", "shocking-grasp", "continual-flame", "flame-blade", "flaming-sphere", "gust-of-wind", "scorching-ray", "shatter",
    "spiritual-weapon", "daylight", "fireball", "lightning-bolt", "tiny-hut", "wind-wall", "fire-shield", "ice-storm", "resilient-sphere",
    "wall-of-fire", "wall-of-ice", "cone-of-cold", "flame-strike", "sending", "wall-of-force", "blade-barrier", "chain-lightning", "contingency",
    "freezing-sphere", "delayed-blast-fireball", "forcecage", "prismatic-spray", "sunbeam", "earthquake", "fire-storm", "sunburst", "meteor-swarm"]}
V35e.update({
"darkness": dict(options=[O("Ténèbres"), O("Ténèbres profondes", src_idx="deeper-darkness")]),
"meteor-swarm": dict(impact=(21, ["feu"], "6d6 en moyenne par météore"), impact_sats=[(7, ["choc"])]),
"fire-shield": dict(impact=(11, ["feu"], "1d6 + 7 en moyenne"), alt=[dict(impact=(11, ["froid"], "1d6 + 7 en moyenne"))]),
"call-lightning": dict(options=[O("Appel de la foudre"), O("Appel de la tempête", src_idx="call-lightning-storm")]),
"arcane-sword": dict(src_idx="mages-sword", name="Mage's Sword"),
"arcane-hand": dict(src_idx="interposing-hand", impact_add=[], options=[
    O("Main interposée", impact=(4, ["main", "garde"], "4 ajouté à la défense contre un adversaire")),
    O("Main puissante", src_idx="forceful-hand", impact=(P, ["main", "poussée"], "l'adversaire repoussé")),
    O("Main agrippante", src_idx="grasping-hand", impact=(P, ["main", "étreinte"], "l'adversaire agrippé")),
    O("Poing serré", src_idx="clenched-fist", impact=(16, ["main", "choc"], "1d8 + 11 en moyenne")),
    O("Main broyeuse", src_idx="crushing-hand", impact=(19, ["main", "étreinte", "broyage"], "2d6 + 12 en moyenne, à chaque étreinte"))]),
"divine-word": dict(src_idx="holy-word", cond=[], options=[
    WORD("Mot sacré — contre l'hostile", "holy-word", "hostile", "surdité", "aveuglement", "paralysie"),
    WORD("Blasphème — contre l'hostile", "blasphemy", "hostile", "hébétude", "faiblesse", "paralysie"),
    WORD("Mot de chaos — contre le lumineux", "word-of-chaos", "lumineux", "surdité", "étourdissement", "confusion"),
    WORD("Décret — contre le ténébreux", "dictum", "ténébreux", "surdité", "lenteur", "paralysie")]),
"hallow": dict(cond=["hostile"], options=[O("Sanctification", impact_sats=[(4, ["mort-vivant", "faiblesse"])]),
                                          O("Sanctification impie", src_idx="unhallow", impact_sats=[(4, ["mort-vivant", "force"])])]),
})
for k, v in V35e.items(): FICHES[k]["v35"] = v
NEW35e = {
"flare": dict(src="3.5", fr="Lueur", verb=V("visibilite"), cible=3, impact=(P, ["éblouissement"], "éblouie une minute"), alt=LUMH()),
"consecrate": dict(src="3.5", fr="Consécration", verb=V("qualite"), cible=P, comp=["argent"],
    options=[O("Consécration — lumineux", impact=(1, ["mort-vivant", "lumineux"], "1 retranché aux morts-vivants")),
             O("Profanation — ténébreux", src_idx="desecrate", impact=(1, ["mort-vivant", "ténébreux"], "1 ajouté aux morts-vivants"))]),
"sound-burst": dict(src="3.5", fr="Cacophonie", cible=P, impact_sats=[(P, ["étourdissement"])]),
"helping-hand": dict(src="3.5", fr="Main secourable", verb=V("relation"), cible=4, impact=(P, ["guide", "main"], "une main fantôme qui ramène la personne cherchée")),
"invisibility-purge": dict(src="3.5", fr="Purge d'invisibilité", verb=V("visibilite"), cible=P, aoe={"type": "sphere", "size": 25}, impact=(P, ["invisible", "révélation"], "tout l'invisible rendu visible")),
"searing-light": dict(src="3.5", fr="Lumière brûlante", verb=V("existence", True), cible=3, impact=(9, ["lumière"], "2d8 en moyenne"), impact_sats=[(18, ["mort-vivant"])], alt=LUMH()),
"divine-power": dict(src="3.5", fr="Force divine", verb=V("intensite"), cible=1, impact=(6, ["force", "coup"], "6 ajouté à la Force, l'attaque d'un guerrier"), impact_sats=[(7, ["vie", "temporaire"])]),
"holy-sword": dict(src="3.5", fr="Arme sacrée", verb=V("intensite"), cible=1, cible_obj=["arme"], cond=["hostile"], impact=(5, ["arme"], "5 ajouté à l'arme"), impact_sats=[(7, ["blessure"]), (P, ["cercle"])]),
"imbue-with-spell-ability": dict(src="3.5", fr="Transfert de sorts", verb=V("relation"), cible=2, impact=(P, ["sort", "transfert"], "des sorts confiés à autrui"), impact_sats=[(4, ["seuil", "niveau"])]),
"shout": dict(src="3.5", fr="Cri", cible=P, impact=(18, ["tonnerre"], "5d6 en moyenne"), impact_sats=[(P, ["surdité"])]),
"shout-greater": dict(src="3.5", fr="Cri suprême", cible=P, impact=(35, ["tonnerre"], "10d6 en moyenne"), impact_sats=[(P, ["surdité"]), (P, ["étourdissement"])]),
"holy-smite": dict(src="3.5", fr="Châtiment sacré", verb=V("existence", True), cible=P, options=[
    SMITE("Châtiment sacré — contre l'hostile", "holy-smite", "hostile", "aveuglement", "aveuglée"),
    SMITE("Fléau impie — contre l'hostile", "unholy-blight", "hostile", "nausée", "nauséeuse"),
    SMITE("Marteau du chaos — contre le lumineux", "chaos-hammer", "lumineux", "lenteur", "ralentie"),
    SMITE("Colère de l'ordre — contre le ténébreux", "orders-wrath", "ténébreux", "hébétude", "hébétée")]),
"sympathetic-vibration": dict(src="3.5", fr="Vibration sympathique", verb=V("existence", True), cible=1, cible_obj=["structure"], impact=(11, ["vibration", "choc"], "une vibration qui ébranle sans relâche (2d10 par tour)")),
"polar-ray": dict(src="3.5", fr="Rayon polaire", cible=3),
"telekinetic-sphere": F35("resilient-sphere", "Sphère télékinésique", impact=(P, ["prison", "barrière", "apesanteur"], "une sphère close, son contenu presque sans poids")),
"whirlwind": dict(src="3.5", fr="Tornade", comb="Tempête", why="le cyclone", cible=P, impact=(11, ["choc", "tourbillon"], "3d6 en moyenne, emportée")),
"implosion": dict(src="3.5", fr="Implosion", verb=V("existence", True), cible=3, qty=4, impact=(P, ["mort"], "la créature s'effondre sur elle-même")),
"miracle": dict(src="3.5", fr="Miracle", verb=V("trame"), cible=9, cible_note=["DIVINITE"], impact=(P, ["intercession"], "la puissance priée intercède"), impact_sats=[(8, ["seuil", "niveau"])]),
}
FICHES.update(NEW35e)

# ===== D&D 3.5 — lot 6 : Illusion =====
# Plans de l'Ombre et de la Lumière : transposés en hémisphères ténébreux et lumineux ; leur énergie est l'énergie astrale.
# Un sort lié à l'une des deux énergies a toujours sa réciproque : l'une n'existe pas sans l'autre.
ILLH = lambda: [H("Plasma", ILL)]
# L'un n'existe pas sans sa réciproque : chaque sort d'ombre a sa forme lumineuse et sa forme ténébreuse.
ASTR = [("lumineux", "lumineuse"), ("ténébreux", "ténébreuse")]
SHADOW = lambda base, rows: [O(f"{lab} — {e}", src_idx=idx, impact=(n, [e], f"{n} cinquième{'s' if n > 1 else ''} de réalité, tirée de l'énergie {ef}"),
                               impact_sats=[(lv, ["seuil", "niveau"]), (5, ["fractionné"])]) for lab, idx, n, lv in rows for e, ef in ASTR]
V35f = {k: {} for k in ["disguise-self", "silent-image", "magic-mouth", "silence", "illusory-script", "major-image", "hallucinatory-terrain",
    "phantasmal-killer", "dream", "mislead", "project-image", "weird", "simulacrum"]}
V35f.update({
"color-spray": dict(impact=(P, ["inconscience", "aveuglement", "étourdissement"], "selon la vie qui reste")),
"hypnotic-pattern": dict(impact=(36, ["fascination", "vie"], "jusqu'à 36 points de vie de créatures fascinées (2d4 + 3 DV)")),
"blur": dict(impact=(5, ["flou", "fractionné"], "une chance sur cinq d'être manquée")),
"mirror-image": dict(impact=(4, ["image"], "1d4 + 1 doubles")),
"minor-illusion": dict(src_idx="ghost-sound", name="Ghost Sound", options=None, cosm=(P, "son"), impact=(P, ["son"], "un son illusoire")),
"invisibility": dict(options=[O("Invisibilité"), O("Sphère d'invisibilité", src_idx="invisibility-sphere", aoe={"type": "sphere", "size": 10}),
                              O("Invisibilité de groupe", src_idx="invisibility-mass", qty_cible=P)]),
"greater-invisibility": dict(src_idx="invisibility-greater", name="Invisibility, Greater"),
"programmed-illusion": dict(src_idx="programmed-image", name="Programmed Image"),
"mirage-arcane": dict(src_idx="mirage-arcana", name="Mirage Arcana"),
"seeming": dict(options=[O("Apparence trompeuse"), O("Voile", src_idx="veil", qty_cible=P)]),
})
for k, v in V35f.items(): FICHES[k]["v35"] = v
IMG = lambda fr, *w, **kw: {**dict(src="3.5", fr=fr, verb=V("existence"), cosm=(P, "IMAGE"), impact=(P, ["image"] + list(w), "une image, avec " + ", ".join(w)), alt=ILLH()), **kw}
NEW35f = {
"ventriloquism": dict(src="3.5", fr="Ventriloquie", verb=V("visibilite", True), cible=1, impact=(P, ["voix", "lieu"], "la voix qui semble venir d'ailleurs"), alt=[H("Air", "l'air qui porte la voix")]),
"minor-image": IMG("Image imparfaite", "son"),
"persistent-image": IMG("Image persistante", "son", "odeur", "chaleur", "scénario"),
"permanent-image": IMG("Image permanente", "son", "odeur", "chaleur", comp=["jade"]),
"misdirection": dict(src="3.5", fr="Détournement", verb=V("visibilite", True), cible=1, impact=(P, ["aura", "leurre"], "les détections lisent un autre objet"), alt=ILLH()),
"phantom-trap": dict(src="3.5", fr="Piège illusoire", verb=V("visibilite", True), cible=1, cible_obj=["mécanisme"], comp=["pyrite"], impact=(P, ["piège", "faux-semblant"], "un piège qui n'existe pas")),
"displacement": dict(src="3.5", fr="Déplacement", verb=V("visibilite", True), cible=2, impact=(2, ["leurre", "fractionné"], "une chance sur deux d'être manquée"), alt=ILLH()),
"illusory-wall": dict(src="3.5", fr="Mur illusoire", verb=V("existence"), cible=P, cosm=(P, "IMAGE"), impact=(P, ["mur", "image"], "un mur qu'on traverse"), alt=ILLH()),
"rainbow-pattern": dict(src="3.5", fr="Motif chatoyant", verb=V("mouvement", True), cible=P, cosm=(P, "COULEURS"), impact=(108, ["fascination", "vie"], "jusqu'à 108 points de vie de créatures fascinées (24 DV)"), alt=ILLH()),
"scintillating-pattern": dict(src="3.5", fr="Motif scintillant", verb=V("ordre", True), cible=P, cosm=(P, "COULEURS"), impact=(68, ["confusion", "étourdissement", "vie"], "jusqu'à 68 points de vie de créatures frappées (15 DV)"), alt=ILLH()),
"zone-of-silence": dict(src="3.5", fr="Zone de silence", verb=V("visibilite", True), cible=P, impact=(P, ["silence", "secret"], "nul son ne sort de la zone"), alt=[H("Air", "l'air qui ne porte plus le son")]),
"false-vision": dict(src="3.5", fr="Vision mensongère", verb=V("visibilite", True), cible=P, comp=["jade"], impact=(P, ["divination", "leurre"], "la scrutation voit une fausse image"), alt=ILLH()),
"nightmare": dict(src="3.5", fr="Cauchemar", verb=V("relation", True), cible=3, loc=(P, None, "illimitée"), cond=["sommeil"], impact=(6, ["esprit", "fatigue"], "1d10 en moyenne, le repos ruiné")),
"screen": dict(src="3.5", fr="Écran", verb=V("visibilite", True), cible=P, impact=(P, ["divination", "vue", "leurre"], "ni vue ni scrutation ne voient la vérité"), alt=ILLH()),
"shadow-walk": dict(src="3.5", fr="Traversée astrale", fam="R", art="spatiomancie", verb=V("mouvement"), cible=2,
    options=[O(f"Par le flux {e}", cond=[e], impact=(P, [e, "passage"], f"un voyage rapide par le flux {e}")) for e, _ in ASTR]),
"shadow-conjuration": dict(src="3.5", fr="Invocation astrale", verb=V("existence"), cible=P,
    options=SHADOW("shadow-conjuration", [("Invocation astrale", "shadow-conjuration", 1, 3), ("Invocation astrale suprême", "shadow-conjuration-greater", 3, 6), ("Invocation astrale ultime", "shades", 4, 8)])),
"shadow-evocation": dict(src="3.5", fr="Évocation astrale", verb=V("existence", True), cible=P,
    options=SHADOW("shadow-evocation", [("Évocation astrale", "shadow-evocation", 1, 4), ("Évocation astrale suprême", "shadow-evocation-greater", 3, 7)])),
}
FICHES.update(NEW35f)

# ===== D&D 3.5 — lot 7 : Nécromancie =====
# Énergie négative → « nécrose », énergie positive → « vie » (pas le ténébreux et le lumineux : on soigne dans les deux hémisphères).
# Niveaux perdus → un niveau vaut un DV, soit 4,5 points de vie ; « durable » quand la perte peut devenir définitive.
SANGH = lambda: [H("Sang", "le sang qu'on retire")]
NEC = lambda **kw: {**dict(src="3.5", verb=V("existence", True), cible=3), **kw}
V35g = {k: {} for k in ["chill-touch", "ray-of-enfeeblement", "blindness-deafness", "gentle-repose", "speak-with-dead", "vampiric-touch",
    "animate-dead", "bestow-curse", "contagion", "death-ward", "fear", "blight", "magic-jar", "eyebite", "clone", "astral-projection"]}
V35g.update({
"false-life": dict(impact=(9, ["vie", "temporaire"], "1d10 + 3 en moyenne")),
"harm": dict(impact=(110, ["nécrose"], "10 par niveau, soit 110 points de vie retirés")),
"finger-of-death": dict(impact=(P, ["mort"], "morte"), impact_sats=[(24, ["nécrose"])]),
"circle-of-death": dict(impact=(124, ["mort", "vie"], "jusqu\'à 124 points de vie de créatures tuées (1d4 DV par niveau)")),
"inflict-wounds": dict(src_idx="inflict-light-wounds", name="Inflict Wounds", options=[
    O("Blessure mineure", src_idx="inflict-minor-wounds", impact=(1, ["nécrose"], "1 point de vie")),
    O("Blessure légère", impact=(6, ["nécrose"], "1d8 + 1 en moyenne")),
    O("Blessure modérée", src_idx="inflict-moderate-wounds", impact=(12, ["nécrose"], "2d8 + 3 en moyenne")),
    O("Blessure grave", src_idx="inflict-serious-wounds", impact=(19, ["nécrose"], "3d8 + 5 en moyenne")),
    O("Blessure critique", src_idx="inflict-critical-wounds", impact=(25, ["nécrose"], "4d8 + 7 en moyenne"))]),
"create-undead": dict(options=[O("Création de mort-vivant"), O("Création de mort-vivant dominant", src_idx="create-greater-undead")]),
})
for k, v in V35g.items(): FICHES[k]["v35"] = v
NEW35g = {
"inflict-light-wounds-mass": NEC(fr="Blessure de groupe", alt=SANGH(), options=[
    O("Blessure légère de groupe", qty_cible=9, impact=(14, ["nécrose"], "1d8 + 9 en moyenne")),
    O("Blessure modérée de groupe", src_idx="inflict-moderate-wounds-mass", qty_cible=11, impact=(20, ["nécrose"], "2d8 + 11 en moyenne")),
    O("Blessure grave de groupe", src_idx="inflict-serious-wounds-mass", qty_cible=13, impact=(27, ["nécrose"], "3d8 + 13 en moyenne")),
    O("Blessure critique de groupe", src_idx="inflict-critical-wounds-mass", qty_cible=15, impact=(33, ["nécrose"], "4d8 + 15 en moyenne"))]),
"disrupt-undead": NEC(fr="Destruction de mort-vivant", cond=["MORTVIVANT"], impact=(4, ["vie"], "1d6 en moyenne, aux seuls morts-vivants")),
"touch-of-fatigue": NEC(fr="Contact de fatigue", verb=V("intensite", True), options=[O("Contact de fatigue", **I("fatigue", why="fatiguée")),
    O("Rayon d'épuisement", src_idx="ray-of-exhaustion", **I("épuisement", why="épuisée"))]),
"waves-of-fatigue": NEC(fr="Vagues de fatigue", verb=V("intensite", True), cible=P, cond=["vivant"], options=[O("Vagues de fatigue", **I("fatigue", why="fatiguées")),
    O("Vagues d'épuisement", src_idx="waves-of-exhaustion", **I("épuisement", why="épuisées"))]),
"cause-fear": NEC(fr="Frayeur", verb=V("force", True), cond=["vivant", "seuil"], cond_sats=[(23, ["vie"])], impact=(P, ["peur"], "effrayée"),
    options=[O("Frayeur"), O("Effroi", src_idx="scare", qty_cible=P)]),
"curse-water": dict(src="3.5", fr="Eau consacrée", verb=V("qualite"), cible=1, cible_obj=["eau"], comp=["argent"],
    options=[O("Eau bénite — lumineux", src_idx="bless-water", impact=(P, ["eau", "lumineux"], "une eau chargée d'énergie lumineuse")),
             O("Eau maudite — ténébreux", impact=(P, ["eau", "ténébreux"], "une eau chargée d'énergie ténébreuse"))]),
"deathwatch": dict(src="3.5", fr="Regard funeste", verb=V("visibilite"), cible=P, impact=(P, ["vie", "état"], "l'état de chaque mourant")),
"doom": NEC(fr="Malédiction funeste", verb=V("intensite", True), impact=(2, ["peur", "coup", "résistance", "aptitude"], "2 retranché, secouée")),
"command-undead": dict(src="3.5", fr="Contrôle des morts-vivants", verb=V("relation"), cible=3, cond=["MORTVIVANT"], options=[
    O("Injonction aux morts-vivants", impact=(P, ["amitié"], "un mort-vivant amical")),
    O("Contrôle des morts-vivants", src_idx="control-undead", impact=(117, ["domination", "vie"], "jusqu'à 117 points de vie de morts-vivants commandés (26 DV)"))]),
"death-knell": NEC(fr="Glas", cond=["mourant"], impact=(P, ["mort"], "achevée, sa vie prise"), impact_sats=[(5, ["vie", "temporaire"]), (2, ["force"])]),
"ghoul-touch": NEC(fr="Caresse de la goule", verb=V("mouvement", True), cond=["humanoïde"], impact=(P, ["paralysie"], "paralysée"), impact_sats=[(P, ["nausée"])]),
"spectral-hand": dict(src="3.5", fr="Main spectrale", verb=V("existence"), cible=1, impact=(P, ["main", "contact"], "les sorts de contact portés au loin"), impact_sats=[(3, ["vie"])]),
"halt-undead": NEC(fr="Immobilisation des morts-vivants", verb=V("mouvement", True), qty_cible=3, cond=["MORTVIVANT"], impact=(P, ["paralysie"], "immobile")),
"enervation": NEC(fr="Énervation", options=[O("Énervation", impact=(11, ["vie"], "1d4 niveaux perdus pour un temps, soit 11 points de vie")),
    O("Absorption d'énergie", src_idx="energy-drain", impact=(23, ["vie", "durable"], "2d4 niveaux perdus, soit 23 points de vie retirés pour de bon"))]),
"poison": dict(src="3.5", fr="Empoisonnement", fam="H", comb="Ammoniac", why="le venin", cible=3, impact=(6, ["poison", "constitution"], "1d10 maintenant, 1d10 une minute plus tard")),
"mark-of-justice": NEC(fr="Marque de la justice", verb=V("qualite", True), cond=["transgression"], impact=(P, ["malédiction", "marque"], "maudite si elle transgresse")),
"slay-living": NEC(fr="Mise à mort", cond=["vivant"], impact=(P, ["mort"], "morte"), impact_sats=[(20, ["nécrose"])], alt=SANGH()),
"destruction": NEC(fr="Destruction", comp=["symbole"], impact=(P, ["mort", "anéantissement"], "morte, sa dépouille consumée"), impact_sats=[(35, ["nécrose"])]),
"undeath-to-death": NEC(fr="Mort des morts-vivants", cible=P, cond=["MORTVIVANT"], comp=["diamant"], impact=(124, ["destruction", "vie"], "jusqu\'à 124 points de vie de morts-vivants détruits (1d4 DV par niveau)")),
"horrid-wilting": NEC(fr="Flétrissure", cible=P, cond=["vivant"], impact=(53, ["dessèchement"], "15d6 en moyenne")),
"soul-bind": NEC(fr="Âme liée", verb=V("mouvement", True), cible=7, comp=["saphir"], impact=(P, ["âme", "gemme"], "l'âme enfermée dans la gemme")),
"wail-of-the-banshee": NEC(fr="Plainte d'outre-tombe", cible=P, qty_cible=17, cond=["écoute"], impact=(P, ["mort"], "morte")),
"symbol-of-pain": SYM("Symbole de douleur", impact=(4, ["douleur", "coup", "aptitude"], "la douleur gêne tout geste (4 retranché aux attaques et aux tests)")),
"symbol-of-fear": SYM("Symbole de terreur", impact=(P, ["panique"], "paniquée")),
"symbol-of-weakness": SYM("Symbole de faiblesse", impact=(11, ["force", "faiblesse"], "3d6 en moyenne retirés à la Force")),
"symbol-of-death": SYM("Symbole de mort", cond=["déclencheur", "seuil"], cond_sats=[(150, ["vie"])], impact=(P, ["mort"], "mortes")),
}
FICHES.update(NEW35g)

# ===== D&D 3.5 — lot 8 : Transmutation =====
T35 = lambda **kw: {**dict(src="3.5"), **kw}
ABIL = [("bears-endurance", "Endurance de l'ours", "constitution"), ("bulls-strength", "Force du taureau", "force"), ("cats-grace", "Grâce du félin", "dextérité"),
        ("eagles-splendor", "Splendeur de l'aigle", "charisme"), ("foxs-cunning", "Ruse du renard", "intelligence"), ("owls-wisdom", "Sagesse du hibou", "sagesse")]
V35h = {k: {} for k in "mage-hand message purify-food-and-drink entangle expeditious-retreat feather-fall goodberry jump longstrider pass-without-trace shillelagh alter-self barkskin darkvision heat-metal knock levitate rope-trick spider-climb blink gaseous-form glibness haste meld-into-stone slow spike-growth water-breathing water-walk polymorph reincarnate stone-shape awaken fabricate passwall telekinesis animate-objects control-water disintegrate flesh-to-stone move-earth wind-walk control-weather reverse-gravity animal-shapes shapechange time-stop".split()}
V35h.update({
"enhance-ability": dict(src_idx="bears-endurance", options=[O(n, src_idx=k, impact=(4, ["aptitude", w], f"4 ajouté en {w}")) for k, n, w in ABIL]
                        + [O(n + " de groupe", src_idx=k + "-mass", qty_cible=11, impact=(4, ["aptitude", w], f"4 ajouté en {w}")) for k, n, w in ABIL]),
"enlarge-reduce": dict(src_idx="enlarge-person", alt=[dict(src_idx="reduce-person")], options=[O("individuel"),
    O("de groupe", only=0, src_idx="enlarge-person-mass", qty_cible=7), O("de groupe", only=1, src_idx="reduce-person-mass", qty_cible=7)]),
"magic-weapon": dict(options=[O("Arme magique"), O("Arme magique suprême", src_idx="magic-weapon-greater", impact=(1, ["arme"], "+1 par quatre niveaux"))]),
"mending": dict(options=[O("Réparation"), O("Restauration d'objet", src_idx="make-whole", **I("réparation", "entier", why="l'objet rendu entier"))]),
"plant-growth": dict(options=[O("Croissance végétale"), O("Élagage", src_idx="diminish-plants", **I("élagage", why="la végétation ramenée au tiers")),
                              O("Rabougrissement", src_idx="diminish-plants", **I("rabougrissement", why="les cultures appauvries"))]),
"fly": dict(options=[O("Vol"), O("Vol prolongé", src_idx="overland-flight")]),
"true-polymorph": dict(src_idx="polymorph-any-object", name="Polymorph Any Object"),
"etherealness": dict(options=[O("Forme éthérée"), O("Passage éthéré", src_idx="ethereal-jaunt")]),
})
for k, v in V35h.items(): FICHES[k]["v35"] = v
NEW35h = {
"open-close": T35(fr="Ouverture/fermeture", cible=1, cible_obj=["porte"], options=[O("Ouverture", verb=V("relation", True), **I("ouverture")), O("Fermeture", verb=V("relation"), **I("fermeture"))]),
"virtue": T35(fr="Vertu", verb=V("intensite"), cible=2, impact=(1, ["vie", "temporaire"], "1 point de vie temporaire")),
"animate-rope": T35(fr="Animation de corde", verb=V("nature"), cible=1, cible_obj=["corde"], impact=(P, ["nœud", "entrave"], "la corde qui noue et entrave")),
"bless-weapon": T35(fr="Arme bénie", verb=V("intensite"), cible=1, cible_obj=["arme"], cond=["hostile"], impact=(1, ["arme"], "+1 contre l'hostile")),
"align-weapon": T35(fr="Arme orientée", verb=V("nature"), cible=1, cible_obj=["arme"], options=[O(f"Contre {l}", **I("arme", w, why=f"l'arme qui frappe {l}")) for l, w in [("l'hostile", "hostile"), ("le lumineux", "lumineux"), ("le ténébreux", "ténébreux")]]),
"erase": T35(fr="Effacement", verb=V("existence", True), cible=1, cible_obj=["écrit"], impact=(P, ["effacement"], "l'écrit effacé")),
"magic-fang": T35(fr="Morsure magique", verb=V("intensite"), cible=2, options=[O("Morsure magique", impact=(1, ["arme", "naturelle"], "+1 à une arme naturelle")),
    O("Morsure magique suprême", src_idx="magic-fang-greater", impact=(1, ["arme", "naturelle", "toutes"], "+1 à toutes ses armes naturelles"))]),
"magic-stone": T35(fr="Pierre magique", verb=V("intensite"), cible=1, cible_obj=["pierre"], impact=(5, ["projectile"], "1d6 + 1 en moyenne"), impact_sats=[(3, ["nombre"])]),
"magic-vestment": T35(fr="Armure magique", verb=V("intensite"), cible=1, cible_obj=["armure"], impact=(1, ["garde"], "+1")),
"reduce-animal": T35(fr="Rapetissement d'animal", verb=V("intensite", True), cible=2, cond=["bête"], impact=(P, ["rapetissement"], "taille réduite de moitié")),
"chill-metal": T35(fr="Refroidir le métal", comb="Glace", why="le froid", cible=1, cible_obj=["METAL"], impact=(5, ["froid"], "2d4 au plus fort"), alt=[A("nature")]),
"pyrotechnics": T35(fr="Pyrotechnie", comb="Feu", why="le feu transformé", cible=P, options=[O("Feux d'artifice", **I("aveuglement", why="aveuglées")), O("Fumée", **I("fumée", "obscurité", why="un nuage étouffant"))]),
"soften-earth-and-stone": T35(fr="Ramollissement de la terre et de la pierre", comb="Boue", why="la boue", cible=P, impact=(P, ["boue", "argile"], "terre en boue, pierre en argile")),
"tree-shape": T35(fr="Forme d'arbre", comb="Bois", why="le bois", cible=1, impact=(P, ["arbre", "forme"], "un arbre que rien ne distingue")),
"warp-wood": T35(fr="Distorsion du bois", comb="Bois", why="le bois", cible=1, cible_obj=["bois"], qty_cible=3, impact=(P, ["gauchissement"], "le bois tordu")),
"whispering-wind": T35(fr="Murmure du vent", comb="Air", why="le vent", cible=P, impact=(P, ["message", "vent"], "un message porté par le vent")),
"wood-shape": T35(fr="Façonnage du bois", comb="Bois", why="le bois", cible=1, cible_obj=["bois"], impact=(P, ["façonnage"], "le bois façonné")),
"flame-arrow": T35(fr="Flèches enflammées", comb="Feu", why="le feu", cible=1, cible_obj=["projectile"], impact=(4, ["feu"], "1d6 par trait"), impact_sats=[(50, ["nombre"])]),
"keen-edge": T35(fr="Arme acérée", verb=V("intensite"), cible=1, cible_obj=["arme"], impact=(2, ["faille"], "une lame qui trouve deux fois plus souvent la faille (zone de critique doublée)")),
"quench": T35(fr="Extinction des feux", comb="Eau", why="l'eau", cible=P, impact=(P, ["extinction", "feu"], "tous les feux éteints"), impact_sats=[(18, ["élémentaire"])]),
"sculpt-sound": T35(fr="Sculpteur de sons", verb=V("nature"), cible=2, qty_cible=7, impact=(P, ["son", "transformation"], "les sons changés")),
"secret-page": T35(fr="Page secrète", verb=V("visibilite", True), cible=1, cible_obj=["écrit"], impact=(P, ["écrit", "déguisement"], "la page qui montre autre chose")),
"shrink-item": T35(fr="Rétrécissement d'objet", verb=V("intensite", True), cible=1, cible_obj=["objet"], impact=(1, ["taille", "seizième"], "un seizième de sa taille")),
"snare": T35(fr="Collet", comb="Plante", why="la liane", cible=1, cible_obj=["corde"], cond=["passage"], impact=(P, ["entrave", "collet"], "pris au collet")),
"air-walk": T35(fr="Marche dans les airs", comb="Air", why="l'air qui porte", cible=2, impact=(P, ["vol", "marche"], "marcher sur l'air"), alt=[A("mouvement")]),
"command-plants": T35(fr="Contrôle des plantes", comb="Plante", why="les plantes", cible=3, cond=["plante"], options=[O("Injonction aux plantes", **I("amitié", why="des plantes amicales")),
    O("Contrôle des plantes", src_idx="control-plants", impact=(135, ["domination", "vie"], "jusqu'à 135 points de vie de plantes commandées (30 DV)"))]),
"giant-vermin": T35(fr="Vermine géante", verb=V("intensite"), cible=1, cible_obj=["vermine"], qty_cible=3, impact=(P, ["croissance"], "la vermine devenue géante")),
"mnemonic-enhancer": T35(fr="Amélioration de mémoire", verb=V("intensite"), cible=1, comp=["ivoire"], options=[O("Préparation", **I("mémoire", "sort", why="trois niveaux de sorts en plus")),
    O("Rétention", **I("mémoire", "rappel", why="un sort lancé retenu"))]),
"rusting-grasp": T35(fr="Rouille", verb=V("qualite", True), cible=1, cible_obj=["fer"], impact=(P, ["rouille"], "le fer rongé"), impact_sats=[(11, ["rouille"])]),
"spike-stones": T35(fr="Pierres acérées", comb="Roche", why="la pierre", cible=P, impact=(5, ["perce", "pierre"], "1d8 à chaque pas")),
"animal-growth": T35(fr="Croissance animale", verb=V("intensite"), cible=2, cond=["bête"], qty_cible=4, impact=(8, ["force", "taille"], "8 ajouté à la Force, taille doublée")),
"baleful-polymorph": T35(fr="Métamorphose funeste", verb=V("nature", True), cible=3, impact=(P, ["bête", "métamorphose"], "changée en petite bête")),
"control-winds": T35(fr="Contrôle des vents", comb="Air", why="le vent", cible=P, impact=(P, ["vent"], "le vent commandé")),
"disrupting-weapon": T35(fr="Arme destructrice", verb=V("intensite"), cible=1, cible_obj=["arme"], cond=["MORTVIVANT"], impact=(P, ["destruction"], "le mort-vivant frappé détruit")),
"righteous-might": T35(fr="Force du colosse", verb=V("intensite"), cible=1, impact=(8, ["force", "taille"], "8 ajouté à la Force, taille doublée")),
"transmute-rock-to-mud": T35(fr="La pierre en boue", comb="Boue", why="la boue", cible=P, **I("boue", why="la roche devenue boue")),
"transmute-mud-to-rock": T35(fr="La boue en pierre", comb="Roche", why="la pierre", cible=P, **I("pierre", why="la boue durcie en pierre")),
"ironwood": T35(fr="Bois de fer", comb="Bois", why="le bois", cible=1, cible_obj=["bois"], impact=(P, ["acier", "bois"], "un bois aussi dur que l'acier")),
"liveoak": T35(fr="Chêne animé", comb="Bois", why="le chêne", cible=1, cible_obj=["chêne"], impact=(P, ["gardien", "arbre"], "un chêne gardien")),
"mages-lucubration": T35(fr="Lucubration", verb=V("intensite"), cible=1, impact=(P, ["mémoire", "sort"], "un sort lancé rappelé"), impact_sats=[(5, ["seuil", "niveau"])]),
"repel-wood": T35(fr="Répulsion du bois", verb=V("force", True), cible=1, cible_obj=["bois"], impact=(P, ["répulsion"], "le bois repoussé")),
"spellstaff": T35(fr="Bâton à sort", verb=V("relation"), cible=1, cible_obj=["bâton"], impact=(P, ["sort", "réserve"], "un sort gardé dans le bâton")),
"stone-to-flesh": T35(fr="Pierre en chair", verb=V("nature"), cible=2, cond=["pétrification"], impact=(P, ["chair"], "la pierre rendue à la chair")),
"transformation": T35(fr="Transformation", verb=V("intensite"), cible=1, impact=(4, ["force", "dextérité", "constitution", "garde"], "4 ajouté partout"), impact_sats=[(P, ["sort", "interdit"])]),
"animate-plants": T35(fr="Animation des plantes", comb="Plante", why="les plantes", cible=1, cible_obj=["plante"], qty_cible=4, impact=(P, ["animation"], "les plantes qui attaquent")),
"changestaff": T35(fr="Bâton sylvanien", comb="Bois", why="le bois", cible=1, cible_obj=["bâton"], impact=(P, ["sylvanien", "gardien"], "le bâton devenu sylvanien")),
"statue": T35(fr="Statue", verb=V("nature"), cible=2, impact=(P, ["pierre", "forme"], "changée en statue, à volonté")),
"transmute-metal-to-wood": T35(fr="Métal en bois", comb="Bois", why="le bois", cible=P, impact=(P, ["métal", "bois"], "tout le métal changé en bois")),
"iron-body": T35(fr="Corps de fer", verb=V("nature"), cible=1, impact=(15, ["garde", "fer"], "15 retranché à chaque coup"), impact_sats=[(P, ["immunité"])]),
"temporal-stasis": T35(fr="Stase temporelle", fam="R", art="chronomancie", verb=V("mouvement", True), cible=3, comp=["gemme"], impact=(P, ["stase"], "le temps arrêté pour elle")),
}
FICHES.update(NEW35h)

# ===== D&D 3.5 — école universelle (rattachée à l'école 5e la plus proche) =====
# Souhait : tracé comme Miracle — un sort qui reproduit tout sort jusqu'à un seuil de niveau, ou exauce au-delà.
FICHES["wish"] = dict(fr="Souhait", verb=V("trame"), impact=(P, ["souhait"], "un souhait exaucé"), impact_sats=[(8, ["seuil", "niveau"])])
V35u = {
"prestidigitation": {},
"wish": dict(options=[O("Souhait"), O("Souhait limité", src_idx="limited-wish", impact_sats=[(6, ["seuil", "niveau"])])]),
}
for k, v in V35u.items(): FICHES[k]["v35"] = v
FICHES.update({
"arcane-mark": dict(src="3.5", fr="Marque du mage", verb=V("existence"), cible=1, cible_obj=["surface"], impact=(P, ["marque", "rune"], "ta rune personnelle, visible ou non")),
"permanency": dict(src="3.5", fr="Permanence", verb=V("ordre"), cible=1, impact=(P, ["sort", "permanence"], "un sort rendu permanent")),
})

# ===== Emplacement de sort =====
# Un sort qui stocke, reproduit, imite ou prolonge un autre sort porte un satellite-emplacement sur l'Impact : vide dans la
# bibliothèque, il reçoit au lancement le glyphe du sort concerné.
SLOT = (None, ["sort"])
def _slot(d, base=()):
    """ajoute l'emplacement à la fiche et à chacune de ses options (une option sans satellites propres hérite de ceux de la fiche)"""
    if not d: return
    own = [s for s in d.get("impact_sats", list(base)) if s != SLOT]
    if "impact_sats" in d or "impact" in d or base: d["impact_sats"] = own + [SLOT]
    for o in d.get("options") or []:
        o["impact_sats"] = [s for s in o.get("impact_sats", own) if s != SLOT] + [SLOT]
for k in ["wish", "miracle", "contingency", "spellstaff", "imbue-with-spell-ability", "permanency", "mages-lucubration", "shadow-conjuration", "shadow-evocation"]:
    _slot(FICHES[k]); _slot(FICHES[k].get("v35"), base=FICHES[k].get("impact_sats", []))
_g = lambda o: "sort" in o.get("label", "").lower()
for d in (FICHES["glyph-of-warding"], FICHES["glyph-of-warding"].get("v35")):
    for o in d.get("options") or []:
        if _g(o): o["impact_sats"] = [s for s in o.get("impact_sats", []) if s != SLOT] + [SLOT]

# ===== Relecture =====
# Aura magique (3.5) = l'Aura magique de la 5e ; Création mineure et majeure = échelons de Création.
FICHES["arcanists-magic-aura"]["v35"] = dict(src_idx="magic-aura", name="Magic Aura")
FICHES["creation"]["v35"] = dict(src_idx="minor-creation", options=[
    O("Création mineure", cible_obj=["plante"], impact=(7, ["création", "volume"], "7 pieds cubes de matière végétale")),
    O("Création majeure", src_idx="major-creation", cible_obj=["minéral"], impact=(9, ["création", "volume"], "9 pieds cubes de matière végétale ou minérale"))])
# Création (5e) tire son objet du plan de l'Ombre : énergie astrale, donc une forme lumineuse et une forme ténébreuse
FICHES["creation"]["options"] = [O(f"Forme {ef}", impact=(P, ["matière", e], f"un objet tiré de l'énergie {ef}")) for e, ef in ASTR]
# formes 3.5 dont les données ne disent pas l'effet
for k, v in {"divine-favor": dict(impact=(1, ["chance", "coup", "blessure"], "+1 aux attaques et aux dégâts")),
             "heat-metal": dict(impact=(5, ["feu"], "jusqu'à 2d4 au plus fort")),
             "spiritual-weapon": dict(impact=(6, None, "1d8 + 1 en moyenne, de force")),
             "wind-wall": dict(impact=(P, ["vent", "trait"], "les projectiles déviés")),
             "dream": dict(impact=(P, ["rêve", "message"], "un message en songe")),
             "arcane-sword": dict(impact=(14, None, "4d6 en moyenne, de force")),
             "produce-flame": dict(impact=(5, ["feu"], "1d6 + 1 en moyenne"))}.items():
    FICHES[k]["v35"] = {**(FICHES[k].get("v35") or {}), **v}

# ===== Pathfinder 1 (OGL, Paizo) =====
# Sorts légaux en Pathfinder Society seulement (canon et équilibré), Technology Guide écarté.
# Les sorts communs reprennent l'encodage de leur version 3.5 ; ce qui touche trop à Golarion est mis de côté pour relecture.
import convert as _C
def PFV(school):
    """versions Pathfinder 1 des sorts déjà présents d'une école : même encodage que leur version 3.5"""
    for k, f in FICHES.items():
        if f.get("src") == "pf1" or "vpf" in f: continue
        sk = f.get("src_idx", k)
        rec = _C.PF1.get(sk) if f.get("src") == "3.5" else None
        v = f.get("v35")
        if f.get("src") == "3.5":
            if not rec or rec["school"]["name"] != school: continue
            opts = [o for o in f.get("options") or [] if o.get("src_idx", sk) in _C.PF1]
            f["vpf"] = {"options": opts} if f.get("options") else {}
        elif v is not None:
            sk = v.get("src_idx", k)
            if sk not in _C.PF1 or _C.PF1[sk]["school"]["name"] != school: continue
            nv = dict(v); nv.pop("name", None)
            if v.get("options"): nv["options"] = [o for o in v["options"] if o.get("src_idx", sk) in _C.PF1]
            f["vpf"] = nv
PF1_RELECTURE = {}      # sorts écartés : effet qui dépend du monde de Golarion, ou pure mécanique de jeu
# Règles : un nom propre de Golarion s'efface, le sort garde son sens ; un effet qui dépend du monde de Golarion est écarté ;
# une mécanique de jeu (jets, actions, compétences, attaques d'opportunité, initiative…) ne s'écrit pas : on garde l'esprit du sort.
EP = lambda fr, verb, cible, words, v=None, why="", **kw: {**dict(src="pf1", fr=fr, verb=verb, cible=cible, impact=(P if v is None else v, list(words), why)), **kw}
REL, NREL, INT, NINT, ORD, NORD = V("relation"), V("relation", True), V("intensite"), V("intensite", True), V("ordre"), V("ordre", True)

# --- Pathfinder 1, lot 1 : Enchantement (niveaux 0 à 2) ---
PF1_RELECTURE.update({
"pugwampis-grace": "repose sur la malchance des pugwampis, créature propre à Golarion",
"slave-to-sin": "repose sur les sept péchés de la magie runique de Thassilon (Golarion)",
"spirit-call": "renforce les sorts liés à l'esprit d'un chaman ou au domaine d'un prêtre : pure mécanique de classe",
"toilsome-chant": "prolonge l'« inspiration de compétence » du barde : pure mécanique de classe",
})
NEWPF_ENCH1 = {
"abadars-truthtelling": EP("Vérité imposée", REL, 2, ["vérité", "ordre"], why="ne peut mentir, l'ordre visible sur elle"),
"blessing-of-the-watch": EP("Bénédiction du guet", INT, 2, ["chance", "cité"], why="une bénédiction qui tient tant qu'on reste dans sa cité", qty_cible=P),
"egorian-diplomacy": EP("Persuasion contrainte", REL, 3, ["contrainte", "oubli"], why="contrainte, puis oublie la rencontre"),
"tieldlaras-feint": EP("Feinte troublante", NINT, 3, ["désir", "distraction"], why="distraite par des pensées de désir"),
"unwitting-ally": EP("Allié involontaire", REL, 3, ["alliance"], why="tenue pour alliée un instant"),
"adoration": EP("Adoration", INT, 1, ["charme", "admiration"], why="admirée de qui la regarde"),
"alluring-light": EP("Lumière attirante", REL, P, ["attraction", "lumière"], why="les créatures s'approchent"),
"animal-purpose-training": EP("Dressage soudain", NAT := V("nature"), 3, ["dressage", "bête"], why="un animal reçoit un nouveau rôle"),
"aphasia": EP("Aphasie", NREL, 3, ["langage"], why="ne comprend plus aucune langue"),
"beguiling-gift": EP("Présent ensorcelé", REL, 3, ["présent", "usage"], why="accepte l'objet offert et s'en sert"),
"bungle": EP("Maladresse", NINT, 3, ["maladresse"], why="sa prochaine entreprise tourne à l'échec", cond=["humanoïde"]),
"call-animal": EP("Appel d'animal", REL, 4, ["appel", "bête"], why="un animal vient à toi"),
"challenge-evil": EP("Défi à l'hostile", REL, 3, ["défi", "nausée"], why="nauséeuse si elle refuse le combat", cond=["hostile"]),
"charm-fey": EP("Charme-fée", REL, 3, ["charme"], why="charmée entièrement", cond=["fée"], fin=["offense"]),
"compel-hostility": EP("Hostilité forcée", REL, 1, ["provocation"], why="les ennemis t'attaquent plutôt que tes alliés"),
"compel-tongue": EP("Langue imposée", REL, 2, ["langue", "contrainte"], why="ne parle et n'écrit que la langue donnée"),
"compulsive-liar": EP("Menteur compulsif", NREL, 3, ["vérité", "mensonge"], why="ne peut dire vrai"),
"crime-of-opportunity": EP("Crime d'opportunité", REL, 3, ["crime"], why="pousse à commettre un délit"),
"deja-vu": EP("Déjà-vu", NORD, 3, ["répétition"], why="refait ce qu'elle vient de faire"),
"delusional-pride": EP("Orgueil délirant", NINT, 3, ["orgueil", "coup", "aptitude"], 2, "2 retranché, mais mieux protégée des charmes"),
"demand-offering": EP("Offrande exigée", REL, 3, ["offrande"], why="te donne l'objet qu'elle tient"),
"fairness": EP("Équité", REL, 3, ["échange", "justice"], why="commercer équitablement", qty_cible=1, cond=["humanoïde"]),
"forbid-action": EP("Interdiction d'agir", NREL, 3, ["interdit"], why="ne peut accomplir le geste interdit", cond=["COMPREHENSION"]),
"fumbletongue": EP("Langue embrouillée", NREL, 3, ["parole"], why="ne parle plus intelligiblement"),
"haunting-reminder": EP("Rappel obsédant", V("force", True), 3, ["peur", "représailles"], why="la crainte de tes représailles"),
"haze-of-dreams": EP("Brume de rêves", NINT, 3, ["rêve", "lenteur"], why="ralentie par des rêves éveillés"),
"ill-omen": EP("Mauvais présage", NINT, 3, ["malchance"], why="tout tourne au pire"),
"implant-urge": EP("Pulsion implantée", REL, 3, ["pulsion", "but"], why="un but inconscient"),
"intensify-psyche": EP("Psyché exacerbée", INT, P, ["émotion"], why="les émotions amplifiées"),
"keep-watch": EP("Veille", INT, 2, ["veille", "repos"], why="veiller sans fatigue toute la nuit", qty_cible=1),
"knights-calling": EP("Appel du chevalier", REL, 3, ["défi", "approche"], why="vient à toi et te combat"),
"litany-of-sloth": EP("Litanie de paresse", NINT, 3, ["vigilance", "torpeur"], why="ne saisit plus aucune ouverture"),
"lock-gaze": EP("Regard captif", REL, 3, ["regard"], why="ne regarde que toi"),
"make-lost": EP("Égarement", NREL, 3, ["égarement"], why="perdent leur chemin", qty_cible=1),
"memorize-page": EP("Page mémorisée", INT, 2, ["mémoire", "page"], why="une page apprise par cœur"),
"memory-lapse": EP("Trou de mémoire", NREL, 3, ["mémoire", "oubli"], why="oublie le dernier instant"),
"moment-of-greatness": EP("Instant de grandeur", INT, 2, ["courage", "doublement"], 2, "l'élan qui l'anime doublé", qty_cible=P),
"murderous-command": EP("Ordre meurtrier", REL, 3, ["meurtre", "allié"], why="pousse à tuer son allié", cond=["vivant"]),
"opportunistic-loyalty": EP("Loyauté opportune", REL, 1, ["alliance", "sort"], why="tenu pour allié des sorts d'autrui"),
"rally-point": EP("Point de ralliement", INT, P, ["ralliement"], why="le lieu soutient les alliés", cond=["allié"]),
"reveal-secrets": EP("Secrets révélés", V("visibilite"), 3, ["secret"], why="trahit ce qu'elle sait du sujet"),
"stalwart-resolve": EP("Résolution", V("ordre"), 2, ["vigueur", "intégrité"], why="ne sent plus ses faiblesses"),
"swallow-your-fear": EP("Ravaler sa peur", INT, 2, ["peur", "combat"], why="plus efficace sous l'emprise de la peur", qty_cible=1),
"tactical-acumen": EP("Sens tactique", INT, P, ["position", "coup", "garde"], 1, "+1 grâce à la position"),
"telempathic-projection": EP("Projection télempathique", REL, 3, ["attitude", "émotion"], why="son attitude infléchie"),
"unbreakable-heart": EP("Cœur inébranlable", INT, 2, ["courage", "résistance"], 4, "+4 contre les émotions sombres"),
"unnatural-lust": EP("Désir contre nature", REL, 3, ["désir"], why="poussée à embrasser quelqu'un"),
"unprepared-combatant": EP("Combattant pris de court", NINT, 3, ["vivacité", "réflexe"], why="lent à réagir"),
"wartrain-mount": EP("Monture aguerrie", V("nature"), 3, ["dressage", "combat"], why="un animal dressé au combat"),
"wrath": EP("Courroux", INT, 1, ["coup", "blessure"], 1, "+1 contre une créature désignée"),
"alpha-instinct": EP("Instinct dominant", INT, 1, ["bête", "ascendant"], why="ascendant sur les animaux"),
"anonymous-interaction": EP("Anonymat", NREL, 3, ["oubli", "visage"], why="oublient qui tu es et ce que tu as dit", qty_cible=3),
"arcane-disruption": EP("Perturbation arcanique", NREL, 3, ["sort", "gêne"], why="lancer devient difficile autour d'elle"),
"aura-of-distraction": EP("Aura de distraction", NINT, P, ["concentration"], why="la concentration troublée"),
"aura-of-the-unremarkable": EP("Aura de banalité", V("visibilite", True), P, ["banalité"], why="tes actes paraissent anodins"),
"aversion": EP("Aversion", V("force", True), 3, ["aversion", "lieu"], why="évite un objet ou un lieu"),
"babble": EP("Babil", NINT, 3, ["nausée", "fascination"], why="nauséeuse, et ses voisins fascinés"),
"bestow-insight": EP("Intuition accordée", INT, 2, ["savoir-faire"], why="un savoir-faire prêté"),
"bestow-weapon-proficiency": EP("Maîtrise d'arme accordée", INT, 2, ["arme", "maîtrise"], why="maîtrise d'une arme"),
"bleed-for-your-master": EP("Saigner pour son maître", REL, 2, ["blessure", "transfert"], why="le compagnon prend les blessures du maître", cond=["compagnon"]),
"blessing-of-luck-and-resolve": EP("Bénédiction de chance et de résolution", INT, 2, ["chance", "peur"], why="mieux armée contre la peur"),
"blood-rage": EP("Rage sanguinaire", INT, 2, ["fureur", "force"], 2, "rage : force accrue, garde baissée", qty_cible=2),
"burdened-thoughts": EP("Pensées pesantes", NINT, 3, ["charge", "lenteur"], why="écrasée comme sous une lourde charge"),
"cacophonous-call": EP("Appel cacophonique", NINT, 3, ["nausée", "son"], why="nauséeuse"),
"castigate": EP("Réprimande", V("force", True), 3, ["peur", "prostration"], why="secouée, puis tétanisée", cond=["COMPREHENSION"]),
"charitable-impulse": EP("Élan charitable", REL, 3, ["charité", "paix"], why="aide autrui plutôt que de frapper", cond=["humanoïde"]),
"cognitive-block": EP("Blocage cognitif", NREL, 3, ["sort", "pensée"], why="ses sorts exigent une pensée claire"),
"compassionate-ally": EP("Allié compatissant", REL, 3, ["compassion", "soin"], why="court aider un allié blessé"),
"confess": EP("Aveux", REL, 3, ["vérité", "aveu"], why="répond vrai ou souffre", impact_sats=[(4, ["esprit"])], cond=["COMPREHENSION"]),
"contagious-zeal": EP("Zèle contagieux", INT, 2, ["zèle", "vie", "contagion"], why="élan et vie qui passent de proche en proche"),
"covetous-urge": EP("Convoitise", REL, 3, ["vol", "convoitise"], why="poussée à voler", cond=["seuil"], cond_sats=[(32, ["vie"])]),
"curse-of-keeping": EP("Malédiction de possession", V("qualite", True), 3, ["malédiction", "possession"], why="ne peut se défaire de ses biens"),
"deflect-blame": EP("Faute rejetée", REL, 3, ["blâme"], why="un autre accusé de tes actes"),
"delay-pain": EP("Douleur différée", NINT, 2, ["douleur"], why="la douleur ignorée"),
"emotive-block": EP("Blocage émotif", NREL, 3, ["sort", "émotion"], why="ses sorts exigent une émotion"),
"false-belief": EP("Fausse croyance", V("nature"), 2, ["mémoire", "faux"], why="un faux souvenir implanté"),
"heckle": EP("Huées", NREL, 3, ["hostilité", "attitude"], why="tous deviennent plus hostiles"),
"hidden-presence": EP("Présence cachée", V("visibilite", True), 3, ["présence", "oubli"], why="ne remarquent pas ta présence", qty_cible=1),
"hold-fey": EP("Immobilisation de fée", V("mouvement", True), 3, ["paralysie"], why="paralysée", cond=["fée"]),
"hoodwink": EP("Embrouille", NORD, 3, ["sens", "confusion"], why="tous leurs sens faussés", qty_cible=3),
"id-insinuation-i": EP("Insinuation", NORD, 3, ["confusion", "ça"], why="confuse tant que tu te concentres",
    options=[O(f"Échelon {r}", src_idx=f"id-insinuation-{r.lower()}", qty_cible=q) for r, q in [("I", 1), ("II", 2), ("III", 3), ("IV", 4)]]),
"inflict-pain": EP("Infliger la douleur", NINT, 3, ["douleur", "coup", "aptitude"], 4, "4 retranché à ses coups et à ses entreprises",
    options=[O("Infliger la douleur"), O("Infliger la douleur de groupe", src_idx="inflict-pain-mass", qty_cible=P)]),
"investigative-mind": EP("Esprit d'enquêteur", INT, 1, ["enquête", "clairvoyance"], why="l'esprit qui voit juste"),
"jealous-rage": EP("Rage jalouse", NINT, 3, ["jalousie", "orgueil"], why="un orgueil blessé et envieux"),
"litany-of-eloquence": EP("Litanie d'éloquence", REL, 3, ["fascination", "parole"], why="fascinée un instant"),
"mantle-of-calm": EP("Manteau de calme", ORD, 1, ["calme", "fureur"], why="apaise la rage de qui t'attaque"),
"miasmal-dread": EP("Effroi méphitique", V("force", True), P, ["peur", "brume"], why="un nuage verdâtre qui démoralise"),
"mindlocked-messenger": EP("Messager scellé", REL, 2, ["message", "secret"], why="un message pour son seul destinataire"),
"oppressive-boredom": EP("Ennui accablant", NINT, 3, ["ennui"], why="reste un moment sans rien faire"),
"passing-fancy": EP("Lubie passagère", REL, 3, ["conversation"], why="tu choisis le sujet de la conversation"),
"peacemakers-parley": EP("Pourparlers", REL, P, ["paix", "parole"], why="apaise des créatures hostiles", cond=["COMPREHENSION"]),
"psychic-leech": EP("Sangsue psychique", V("flux"), 3, ["fatigue", "force"], why="sa vigueur prise pour la tienne"),
"psychonaut-manifestation": EP("Manifestation psychonaute", NORD, 1, ["aptitude", "hasard"], 4, "+4 à une aptitude au hasard, 2 retranché à une autre"),
"puzzle-box": EP("Casse-tête", NREL, 3, ["usage", "oubli"], why="oublie comment se servir des objets"),
"qualm": EP("Scrupule", NINT, 3, ["scrupule", "aptitude"], why="pénalisée tant qu'elle n'a pas frappé"),
"reckless-infatuation": EP("Engouement irréfléchi", REL, 3, ["attachement"], why="reste près d'un autre"),
"reinvigorating-wind": EP("Vent revigorant", INT, P, ["vigueur", "vent"], why="un vent qui ranime les alliés", alt=[H("Air", "le vent")]),
"righteous-vigor": EP("Vigueur vertueuse", INT, 2, ["coup", "élan"], why="chaque coup réussi renforce le suivant"),
"seducers-eyes": EP("Regard séducteur", INT, 1, ["charme", "séduction"], why="plus persuasif auprès de qui te trouve beau"),
"sensory-overload": EP("Surcharge sensorielle", NINT, 3, ["sens", "concentration"], why="agir demande un effort"),
"shamefully-overdressed": EP("Honteusement vêtu", REL, 3, ["vêtement", "honte"], why="ôte son équipement"),
"tactical-miscalculation": EP("Erreur tactique", NINT, 3, ["vigilance", "erreur"], why="laisse passer toutes les ouvertures"),
"thought-worm-i": EP("Ver de pensée", NINT, 3, ["volonté", "esprit"], why="plus vulnérable aux sorts de l'esprit"),
"touch-of-mercy": EP("Toucher de miséricorde", V("qualite"), 3, ["miséricorde"], why="ses coups n'assomment plus que sans tuer"),
"unadulterated-loathing": EP("Dégoût absolu", V("force", True), 3, ["dégoût"], why="évite une autre créature"),
"vexing-miscalculation": EP("Erreur vexante", NINT, 3, ["précision", "faille"], why="ses coups ne trouvent plus la faille"),
}
FICHES.update(NEWPF_ENCH1)
PFV("Enchantment")

# --- Pathfinder 1, lot 1 (suite) : Enchantement, niveaux 3 à 9 ---
PF1_RELECTURE.update({
"instant-enemy": "fait de la cible un « ennemi juré » du rôdeur : pure mécanique de classe",
"terrain-bond": "fait du terrain un « terrain de prédilection » du rôdeur : pure mécanique de classe",
"heroic-finale": "agit dans le rayon d'une « représentation bardique » : pure mécanique de classe",
"stunning-finale": "agit dans le rayon d'une « représentation bardique » : pure mécanique de classe",
"frozen-note": "agit dans le rayon d'une « représentation bardique » : pure mécanique de classe",
"languid-bomb-admixture": "modifie les bombes de l'alchimiste : pure mécanique de classe",
"litany-of-dependability": "fait prendre la moyenne du prochain jet de dés : pure mécanique de jeu",
"bleaching-resistance": "protège du « Blanchiment » des gnomes de Golarion : dépend de leur monde",
})
SYMP = lambda fr, **kw: {**SYM(fr, **kw), "src": "pf1"}
def ECH(k, *rows):
    """échelons d'un même sort sur sa page : rows = (étiquette, src_idx, surcharge)"""
    FICHES[k]["options"] = [O(lab, src_idx=sk, **kw) for lab, sk, kw in rows]
NEWPF_ENCH2 = {
"animal-ambassador": EP("Ambassadeur animal", V("nature"), 2, ["bête", "message", "raison"], why="un animal doué de raison le temps de porter ton message"),
"apparent-treachery": EP("Trahison apparente", NREL, 3, ["soupçon"], why="tenus pour traîtres par leurs alliés", qty_cible=7),
"battle-trance": EP("Transe guerrière", INT, 1, ["férocité", "vie", "esprit"], why="féroce, plus de vie, l'esprit fermé aux charmes"),
"bereave": EP("Deuil", NREL, P, ["alliance"], why="nul n'y compte plus comme allié"),
"bite-the-hand": EP("Mordre la main", REL, 3, ["invoqué", "révolte"], why="l'être invoqué se retourne contre son maître",
    options=[O("Mordre la main"), O("Mordre la main de groupe", src_idx="bite-the-hand-mass", qty_cible=P)]),
"champions-bout": EP("Duel de champions", NREL, 3, ["duel"], why="nul ne peut s'interposer", qty_cible=2),
"companion-mind-link": EP("Lien du compagnon", REL, 2, ["lien", "bête", "parole"], why="parler à son compagnon animal", cond=["compagnon"]),
"control-summoned-creature": EP("Maîtrise d'invoqué", REL, 3, ["invoqué", "domination"], why="un être invoqué par autrui t'obéit"),
"curse-of-disgust": EP("Malédiction du dégoût", V("qualite", True), 3, ["malédiction", "nausée"], why="nauséeuse à la vue de ce qui la dégoûte"),
"daze-mass": EP("Hébétement de groupe", NORD, 3, ["hébétude"], why="privées d'action", cond=["humanoïde"], qty_cible=P),
"demanding-message": EP("Message impérieux", REL, 3, ["message", "conduite"], why="un message et une suggestion",
    options=[O("Message impérieux", qty_cible=5), O("Message impérieux de groupe", src_idx="demanding-message-mass", qty_cible=11)]),
"ego-whip-i": EP("Fouet de l'ego", NINT, 3, ["ego", "esprit"], 2, "2 retranché à l'esprit, chancelante", options=[
    O(f"Fouet de l'ego {r}", src_idx=f"ego-whip-{r.lower()}", impact=(n, ["ego", "esprit"], f"{n} retranché à l'esprit, chancelante")) for r, n in [("I", 2), ("II", 4), ("III", 6), ("IV", 8), ("V", 10)]]),
"false-alibi": EP("Faux alibi", V("nature"), 3, ["mémoire", "alibi"], why="un souvenir réécrit"),
"fleeting-memory": EP("Mémoire fugace", NREL, 3, ["mémoire", "trou"], why="un trou dans la mémoire",
    options=[O("Mémoire fugace"), O("Mémoire fugace de groupe", src_idx="fleeting-memory-mass", qty_cible=15)]),
"gullibility": EP("Crédulité", NINT, 3, ["crédulité"], why="croit tout ce qu'on lui dit"),
"hollow-heroism": EP("Héroïsme creux", INT, 2, ["courage", "révocation"], 2, "héroïsme que tu peux retirer à tout instant",
    options=[O("Héroïsme creux"), O("Héroïsme creux suprême", src_idx="hollow-heroism-greater", impact=(4, ["courage", "révocation"], "héroïsme suprême que tu peux retirer"))]),
"implanted-projection": EP("Projection implantée", REL, 3, ["attitude", "émotion", "dormance"], why="son attitude infléchie plus tard"),
"inveigle-person": EP("Enjôlement", REL, 3, ["amitié"], why="amicale envers tous", options=[O("Enjôlement de personne", cond=["humanoïde"]),
    O("Enjôlement de monstre", src_idx="inveigle-monster", cond=["vivant"])]),
"lovers-vengeance": EP("Vengeance de l'amant", INT, 2, ["fureur", "vengeance"], why="la rage contre qui a blessé l'aimé"),
"mad-sultans-melody": EP("Mélodie démente", REL, 3, ["fascination", "son"], why="une cacophonie qui fascine", qty_cible=4),
"malicious-spite": EP("Rancune malveillante", REL, 3, ["rancune", "complot"], why="complote contre un autre"),
"martial-marionette": EP("Marionnette martiale", V("mouvement"), 3, ["membres", "contrôle"], why="ses membres en partie à toi"),
"mind-maze": EP("Labyrinthe mental", NORD, 3, ["labyrinthe", "errance"], why="erre comme dans un dédale"),
"mind-swap": EP("Échange d'esprit", V("identite"), 3, ["esprit", "échange"], why="vos esprits échangés pour un temps"),
"nixies-lure": EP("Leurre de la nixe", REL, P, ["attraction", "chant"], why="un chant qui attire"),
"out-of-sight": EP("Loin des yeux", V("visibilite", True), 1, ["oubli", "absence"], why="on t'oublie dès que tu disparais"),
"overlook": EP("Insignifiance", V("visibilite", True), 1, ["discrétion"], why="petit et sans importance aux yeux de tous"),
"overwhelming-grief": EP("Chagrin accablant", NINT, 3, ["chagrin"], why="paralysée de chagrin"),
"pillow-talk": EP("Confidences d'oreiller", V("visibilite"), 3, ["sommeil", "réponse"], why="répond en dormant", cond=["sommeil"]),
"seeds-of-influence": EP("Graines d'influence", NINT, 3, ["influence", "esprit"], why="plus vulnérable à tes sorts de l'esprit",
    options=[O("Graines d'influence"), O("Graines d'influence suprêmes", src_idx="seeds-of-influence-greater", impact=(P, ["influence", "esprit", "dissipation"], "et ses protections dissipées"))]),
"sequester-thoughts": EP("Pensées recluses", V("visibilite", True), 2, ["mémoire", "effacement"], why="un sujet effacé de sa mémoire"),
"sleepwalking-suggestion": EP("Suggestion somnambule", REL, 3, ["sommeil", "conduite"], why="agit pendant son sommeil"),
"smug-narcissism": EP("Narcissisme suffisant", NINT, 3, ["narcissisme"], why="distraite par elle-même"),
"stage-fright": EP("Trac", V("force", True), 3, ["peur", "trac"], 4, "paralysée de trac", qty_cible=5),
"symbol-of-laughter": SYMP("Symbole de fou rire", impact=(P, ["rire"], "secoués de rire")),
"synaptic-pulse": EP("Pulsation synaptique", NORD, P, ["étourdissement"], why="étourdies",
    options=[O("Pulsation synaptique"), O("Pulsation synaptique suprême", src_idx="synaptic-pulse-greater")]),
"synaptic-scramble": EP("Brouillage synaptique", NORD, 3, ["parole", "hasard"], why="ne communique plus, agit au hasard"),
"terrible-remorse": EP("Remords terrible", REL, 3, ["remords", "blessure"], why="se blesse elle-même"),
"they-know": EP("Ils savent", V("force", True), 3, ["secret", "peur"], why="croit qu'un autre connaît son secret"),
"triggered-suggestion": EP("Suggestion différée", REL, 3, ["conduite", "déclencheur"], why="une suggestion qui attend son signal", cond=["déclencheur"]),
"untold-wonder": EP("Merveille indicible", ORD, 2, ["émotion", "renversement"], why="les émotions qui l'abattaient la portent"),
"utter-contempt": EP("Mépris absolu", NREL, 3, ["mépris", "attitude"], 2, "son attitude dégradée de deux degrés"),
"antithetical-constraint": EP("Contrainte antithétique", NREL, 3, ["entrave", "coup"], why="ne peut frapper qu'une sorte d'ennemi"),
"cowards-lament": EP("Plainte du lâche", NINT, 3, ["lâcheté"], why="affaiblie si elle ne t'attaque pas"),
"crime-wave": EP("Vague de crimes", REL, 3, ["crime"], why="poussées à commettre des délits", qty_cible=10),
"curse-of-the-outcast": EP("Malédiction du paria", V("qualite", True), 3, ["malédiction", "rejet"], why="indispose tous ceux qu'elle approche"),
"debilitating-portent": EP("Présage débilitant", NINT, 3, ["présage", "faiblesse"], why="ses coups et ses sorts diminués de moitié"),
"debilitating-speech": EP("Discours débilitant", NINT, 3, ["parole", "dénigrement"], why="rabaissée par tes mots", qty_cible=7),
"envious-urge": EP("Pulsion envieuse", REL, 3, ["envie", "vol"], why="volent ou désarment les autres", qty_cible=10),
"forced-repentance": EP("Repentir forcé", REL, 3, ["repentir", "chute"], why="à terre, confessant ses fautes", cond=["hostile"]),
"forgetful-slumber": EP("Sommeil d'oubli", NINT, 3, ["sommeil", "oubli"], why="endormie, ses souvenirs récents perdus"),
"foster-hatred": EP("Haine attisée", REL, 3, ["haine"], why="haïr une sorte de créature", qty_cible=P),
"life-of-crime": EP("Vie de crime", V("qualite", True), 3, ["malédiction", "crime"], why="devient une criminelle forcenée"),
"litany-of-madness": EP("Litanie de folie", NORD, 3, ["folie"], why="confuse", cond=["COMPREHENSION"]),
"lost-passage": EP("Passage égaré", NREL, P, ["égarement", "chemin"], why="ceux qui traversent la zone s'égarent",
    options=[O("Passage égaré"), O("Contrée égarée", src_idx="lost-locale")]),
"mindwipe": EP("Effacement de l'esprit", NREL, 3, ["mémoire", "vie"], 11, "une part de l'esprit effacée, soit 11 points de vie"),
"moonstruck": EP("Lunatique", NORD, 3, ["fureur", "folie"], why="enragée et confuse", cond=["humanoïde"]),
"shadow-of-doubt": EP("Ombre du doute", NINT, 3, ["doute"], why="une aura de doute née de ses fautes", qty_cible=3),
"sleepwalk": EP("Somnambulisme", V("mouvement"), 3, ["sommeil", "marche"], why="marche pendant son sommeil", cond=["inconscience"]),
"stay-the-hand": EP("Main retenue", NREL, 3, ["coup", "arrêt"], why="ne peut frapper au corps à corps"),
"symbol-of-distraction": SYMP("Symbole de distraction", impact=(P, ["fascination"], "fascinés")),
"apathy": EP("Apathie", NINT, 3, ["apathie"], why="perd tout intérêt pour ses passions"),
"befuddled-combatant": EP("Combattant hébété", V("qualite", True), 3, ["malédiction", "faiblesse"], why="ses coups et ses pouvoirs affaiblis"),
"burst-of-glory": EP("Éclat de gloire", INT, P, ["gloire", "courage", "vie"], why="alliés plus forts, plus braves, plus vivants"),
"compelling-rant": EP("Diatribe", REL, P, ["parole", "crédulité"], why="on croit tout tant que tu parles", qty_cible=P),
"contagious-suggestion": EP("Suggestion contagieuse", REL, 3, ["conduite", "contagion"], why="une suggestion qui se transmet"),
"dahaks-release": EP("Libération de la fureur", V("flux", True), 3, ["fureur", "destruction"], why="libère toute sa colère"),
"denounce": EP("Dénonciation", NREL, P, ["attitude", "accusation"], why="l'attitude de tous dégradée", cond=["COMPREHENSION"]),
"die-for-your-master": EP("Mourir pour son maître", REL, 2, ["blessure", "transfert", "mort"], why="le compagnon meurt à la place du maître", cond=["compagnon"]),
"foe-to-friend": EP("D'ennemi à ami", REL, 3, ["détournement"], why="son coup détourné"),
"grand-destiny": EP("Grand destin", INT, 2, ["destin", "chance"], 4, "4 ajouté à une entreprise"),
"hymn-of-mercy": EP("Hymne de miséricorde", V("qualite"), P, ["miséricorde"], why="les coups n'assomment plus que sans tuer"),
"pessimism": EP("Pessimisme", NINT, 3, ["pessimisme"], why="ne voit que le pire"),
"planeslayers-call": EP("Appel du tueur de plans", INT, P, ["outre-plan", "coup"], why="alliés plus forts contre les êtres d'outre-plan"),
"pox-of-rumors": EP("Vérole de rumeurs", V("qualite", True), 3, ["malédiction", "rumeur"], why="les rumeurs la poursuivent"),
"seek-shelter": EP("Mise à l'abri", V("force", True), P, ["peur", "abri"], why="les plus faibles courent s'abriter", cond=["seuil"], cond_sats=[(18, ["vie"])]),
"serenity": EP("Sérénité", ORD, 3, ["paix", "blessure"], why="la violence blesse qui s'y livre", qty_cible=9),
"touch-of-slumber": EP("Toucher de sommeil", NINT, 2, ["sommeil"], why="s'endort", cond=["paix"]),
"cloak-of-dreams": EP("Manteau de rêves", NINT, P, ["sommeil", "rêve"], why="qui t'approche s'endort"),
"lost-legacy": EP("Héritage perdu", V("qualite", True), 3, ["malédiction", "oubli"], why="ne laisse aucune trace dans les mémoires"),
"overwhelming-presence": EP("Présence écrasante", REL, 3, ["soumission"], why="s'inclinent devant toi", qty_cible=16),
"phobia": EP("Phobie", V("force", True), 3, ["peur", "folie"], why="une peur irrationnelle jusqu'à la folie"),
"pied-piping": EP("Joueur de flûte", REL, P, ["attraction", "chant"], why="des créatures semblables te suivent"),
"primal-regression": EP("Régression primale", NINT, 3, ["bestialité"], why="devenue bête, sans raison", qty_cible=5),
"psychic-surgery": EP("Chirurgie psychique", V("qualite"), 2, ["esprit", "guérison"], why="l'esprit guéri de ses blessures"),
"repress-memory": EP("Mémoire refoulée", NREL, 1, ["mémoire", "oubli"], why="un savoir retiré de ta mémoire"),
"symbol-of-strife": SYMP("Symbole de discorde", impact=(P, ["discorde"], "s'entre-attaquent")),
"unconscious-agenda": EP("Dessein inconscient", REL, 3, ["but", "inconscient"], why="un ordre enfoui dans l'esprit", cond=["humanoïde"]),
"vengeful-outrage": EP("Indignation vengeresse", REL, 3, ["vengeance", "destruction"], why="poussée à détruire un ennemi"),
"waves-of-ecstasy": EP("Vagues d'extase", NINT, P, ["extase", "étourdissement"], why="étourdies de plaisir"),
"euphoric-tranquility": EP("Tranquillité euphorique", ORD, 3, ["amitié", "paix"], why="devient amicale"),
"symbol-of-debauchery": SYMP("Symbole de débauche", impact=(P, ["désir"], "pris de désir les uns pour les autres")),
"divide-mind": EP("Esprit scindé", V("identite", True), 1, ["esprit", "partage"], why="l'esprit partagé, plus solide"),
"heroic-invocation": EP("Invocation héroïque", INT, 2, ["courage", "coup"], why="alliés plus forts et plus braves", qty_cible=P),
"mind-swap-major": EP("Échange d'esprit suprême", V("identite"), 3, ["esprit", "échange", "permanence"], why="vos esprits échangés pour toujours", cond=["race"]),
}
FICHES.update(NEWPF_ENCH2)
# échelons de sorts déjà créés au demi-lot précédent
ECH("thought-worm-i", ("Ver de pensée I", "thought-worm-i", {}), ("Ver de pensée II", "thought-worm-ii", {}), ("Ver de pensée III", "thought-worm-iii", {}), ("Ver de pensée IV", "thought-worm-iv", {}))
ECH("cacophonous-call", ("Appel cacophonique", "cacophonous-call", {}), ("Appel cacophonique de groupe", "cacophonous-call-mass", dict(qty_cible=13)))
ECH("castigate", ("Réprimande", "castigate", {}), ("Réprimande de groupe", "castigate-mass", dict(qty_cible=13)))
ECH("compel-tongue", ("Langue imposée", "compel-tongue", {}), ("Langue imposée de groupe", "compel-tongue-mass", dict(qty_cible=9)))
ECH("forbid-action", ("Interdiction d'agir", "forbid-action", {}), ("Interdiction d'agir suprême", "forbid-action-greater", dict(qty_cible=9)))
ECH("passing-fancy", ("Lubie passagère", "passing-fancy", {}), ("Lubie passagère de groupe", "passing-fancy-mass", dict(qty_cible=9)))
ECH("wrath", ("Courroux", "wrath", {}), ("Courroux partagé", "shared-wrath", dict(cible=2, qty_cible=10)))
ECH("blessing-of-luck-and-resolve", ("Bénédiction de chance et de résolution", "blessing-of-luck-and-resolve", {}),
    ("Bénédiction de chance et de résolution de groupe", "blessing-of-luck-and-resolve-mass", dict(qty_cible=10)))
for k in ("thought-worm-i",): FICHES[k]["fr"] = "Ver de pensée"
FICHES["ego-whip-i"]["fr"] = "Fouet de l'ego"
FICHES["id-insinuation-i"]["fr"] = "Insinuation"
FICHES["hypnotism"]["vpf"] = dict(options=[O("Hypnose"), O("Hypnose suprême", src_idx="hypnotism-greater", impact=(P, ["fascination", "conduite"], "plus de créatures fascinées, plus de requêtes"))])
FICHES["song-of-discord"]["vpf"] = dict(options=[O("Chant de discorde"), O("Chant de discorde suprême", src_idx="song-of-discord-greater", impact=(P, ["discorde"], "s'entre-attaquent à coup sûr"))])
FICHES["charm-person"]["vpf"] = dict(options=[O("Charme-personne"), O("Charme-personne de groupe", src_idx="charm-person-mass", qty_cible=P)])

def pf_couverts():
    """tous les sorts Pathfinder 1 déjà rangés (entrée propre, version, échelon) ou écartés"""
    done = set(PF1_RELECTURE) | set(globals().get("PF1_MEME", {}))
    for k, f in FICHES.items():
        done.add(f.get("src_idx", k))
        for v in (f, f.get("v35") or {}, f.get("vpf") or {}, f.get("v24") or {}):
            if v.get("src_idx"): done.add(v["src_idx"])
            for o in v.get("options") or []:
                if o.get("src_idx"): done.add(o["src_idx"])
            for a in v.get("alt") or []:
                if isinstance(a, dict) and a.get("src_idx"): done.add(a["src_idx"])
    return done

# --- Pathfinder 1, lot 2 : Illusion ---
PF1_RELECTURE.update({
"exquisite-accompaniment": "entretient la « représentation bardique » : pure mécanique de classe",
"shadowbard": "lance une « représentation bardique » : pure mécanique de classe",
"inner-focus": "dispense du focaliseur divin des sorts : pure mécanique de jeu",
})
VIS, NVIS, EXI = V("visibilite"), V("visibilite", True), V("existence")
IL = lambda fr, verb, cible, words, v=None, why="", **kw: EP(fr, verb, cible, words, v, why, **{"alt": ILLH(), **kw})
NEWPF_ILL = {
"haunted-fey-aspect": IL("Aspect féerique hanté", EXI, 1, ["image", "effroi"], why="des illusions troublantes autour de toi"),
"vacuous-vessel": IL("Récipient vide", NVIS, 1, ["vide"], why="le contenant paraît vide", cible_obj=["récipient"]),
"alter-musical-instrument": EP("Instrument changé", V("nature"), 1, ["son", "instrument"], why="sonne comme un autre instrument", cible_obj=["instrument"]),
"blend": IL("Fondu", NVIS, 1, ["couleur", "camouflage"], why="tes couleurs prises au décor"),
"blurred-movement": IL("Mouvement flou", NVIS, 1, ["flou", "mouvement"], why="flou tant que tu bouges"),
"clarion-call": EP("Appel du clairon", INT, 2, ["voix", "portée"], why="ta voix porte au loin"),
"dark-whispers": EP("Murmures obscurs", REL, 2, ["murmure", "ombre"], why="des murmures portés par les ombres", qty_cible=1),
"darting-duplicate": IL("Double fuyant", EXI, P, ["double", "leurre"], why="un double qui attire les coups"),
"dazzling-blade": IL("Lame éblouissante", INT, 1, ["éclat", "arme"], why="une arme éblouissante", cible_obj=["arme"],
    options=[O("Lame éblouissante"), O("Lames éblouissantes", src_idx="dazzling-blade-mass", qty_cible=5)]),
"decrepit-disguise": IL("Déguisement décrépit", NVIS, 1, ["valeur", "déguisement"], why="l'objet semble sans valeur", cible_obj=["objet"]),
"disguise-weapon": IL("Arme déguisée", NVIS, 1, ["arme", "déguisement"], why="l'arme a l'air d'autre chose", cible_obj=["arme"]),
"echo": EP("Écho", INT, P, ["son", "écho"], why="un son qui se répète", alt=[H("Air", "l'air qui porte le son")]),
"hide-bruises": IL("Contusions cachées", NVIS, 2, ["blessure", "dissimulation"], why="ses blessures dissimulées"),
"illusion-of-calm": IL("Illusion de calme", NVIS, 1, ["immobilité"], why="tu sembles immobile"),
"incessant-buzzing": IL("Bourdonnement incessant", EXI, P, ["guêpe", "distraction"], why="des guêpes illusoires qui distraient"),
"invigorate": EP("Revigoration", INT, 2, ["fatigue", "vigueur"], why="la fatigue oubliée un temps",
    options=[O("Revigoration"), O("Revigoration de groupe", src_idx="invigorate-mass", qty_cible=5)]),
"jitterbugs": IL("Fourmis dans les jambes", NINT, 3, ["nervosité", "adresse"], why="nerveuse et maladroite"),
"lose-the-trail": IL("Piste perdue", NVIS, 2, ["trace", "fuite"], why="tes traces effacées", qty_cible=1),
"mask-dweomer": IL("Sort masqué", NVIS, 1, ["sort", "aura"], why="un sort caché à la détection",
    options=[O("Sort masqué"), O("Sorts masqués", src_idx="mask-dweomer-communal", qty_cible=P)]),
"mirror-mantis": IL("Tueur au miroir", V("force", True), 3, ["miroir", "peur"], why="un assassin surgit dans chaque reflet"),
"negative-reaction": EP("Mauvaise impression", NREL, 3, ["influence"], why="ne peut plus influencer quiconque"),
"oneiric-horror": IL("Horreur onirique", V("existence", True), 3, ["cauchemar", "fatigue"], why="distraite et fatiguée par son cauchemar",
    options=[O("Horreur onirique"), O("Horreur onirique suprême", src_idx="oneiric-horror-greater", impact=(P, ["cauchemar", "fatigue", "force"], "et sa force entamée"))]),
"open-and-shut": IL("Ouvert et fermé", NVIS, 1, ["porte", "doute"], why="nul ne sait si la porte est ouverte", cible_obj=["porte"]),
"paranoia": EP("Paranoïa", NREL, 3, ["méfiance", "hostilité"], why="hostile à tous"),
"quintessence": IL("Quintessence", NVIS, 1, ["défaut", "perfection"], why="ses défauts et ses dégâts masqués"),
"secret-sign": IL("Signe secret", NVIS, 1, ["marque", "message"], why="une marque invisible", cible_obj=["objet"]),
"shadow-claws": EP("Griffes d'ombre", EXI, 1, ["griffe", "force"], why="des griffes qui lacèrent et affaiblissent"),
"shadow-trap": EP("Piège d'ombre", V("mouvement", True), 3, ["ombre", "entrave"], why="clouée par son ombre"),
"shadow-weapon": EP("Arme d'ombre", EXI, 1, ["arme", "quasi-réel"], why="une arme quasi réelle"),
"shadowfade": IL("Fondu dans l'ombre", NVIS, 2, ["vision", "obscurité"], why="invisible à qui voit dans le noir"),
"thought-echo": EP("Écho de pensée", NVIS, 3, ["pensée", "écho"], why="ses pensées de surface masquées"),
"absurdity": IL("Absurdité", NINT, 3, ["absurde", "menace"], why="les menaces paraissent une farce", qty_cible=3),
"appearance-of-life": IL("Apparence de vie", NVIS, P, ["mort-vivant", "vie"], why="les morts-vivants semblent vivants",
    options=[O("Apparence de vie"), O("Apparence de vie suprême", src_idx="appearance-of-life-greater", cible=2, impact=(P, ["mort-vivant", "vie", "sens"], "vivant pour tous les sens"))]),
"hallucination": None,
"body-double": IL("Sosie", V("identite"), 3, ["apparence", "échange"], why="l'un prend l'allure de l'autre", qty_cible=2),
"chameleon-stride": IL("Pas du caméléon", NVIS, 1, ["camouflage"], why="presque invisible dans le décor",
    options=[O("Pas du caméléon"), O("Pas du caméléon suprême", src_idx="chameleon-stride-greater", cible=P)]),
"display-aversion": IL("Spectacle répulsif", V("force", True), P, ["répulsion", "mort-vivant"], why="une illusion qui repousse les vampires"),
"familiar-figment": IL("Double du familier", EXI, 2, ["double", "compagnon"], why="un double illusoire du familier", cond=["compagnon"]),
"ghostly-disguise": IL("Déguisement spectral", NVIS, 1, ["spectre", "apparence"], why="tu ressembles à ton propre fantôme"),
"haunting-mists": EP("Brumes hantées", V("force", True), P, ["peur", "sagesse"], why="secoués, la sagesse entamée", alt=[H("Brume", "la brume")]),
"hidden-blades": IL("Lames cachées", NVIS, 1, ["arme", "invisibilité"], why="l'arme rendue invisible", cible_obj=["arme"]),
"hide-campsite": IL("Camp caché", NVIS, P, ["camp", "trace"], why="nulle trace du campement"),
"illusory-maze": IL("Labyrinthe illusoire", EXI, P, ["labyrinthe", "verre"], why="un dédale de verre mouvant"),
"implant-false-reading": IL("Fausse empreinte", NVIS, 1, ["empreinte", "faux"], why="de fausses impressions psychiques", cible_obj=["objet"]),
"invisibility-bubble": IL("Bulle d'invisibilité", NVIS, 2, ["invisibilité", "eau"], why="invisible, même sous l'eau", options=[O("Bulle d'invisibilité"),
    O("Bulle d'invisibilité géante", src_idx="invisibility-bubble-giant"), O("Bulles d'invisibilité", src_idx="invisibility-bubble-mass", qty_cible=P)]),
"mad-hallucination": IL("Hallucination démente", NINT, 3, ["démence", "esprit"], why="l'esprit égaré", cond=["humanoïde"]),
"minor-dream": EP("Petit songe", REL, 2, ["rêve", "message"], why="un court message en songe", loc=(P, None, "illimitée"), cond=["sommeil"]),
"muffle-sound": IL("Son étouffé", NVIS, 2, ["silence", "discrétion"], why="tes alliés plus silencieux", qty_cible=3),
"obscured-script": IL("Écriture brouillée", NVIS, 1, ["écrit", "brouillage"], why="le texte difficile à déchiffrer", cible_obj=["écrit"]),
"peerless-integrity": IL("Intégrité sans faille", NVIS, 2, ["hostile", "astral", "divination"], why="intentions et charge astrale cachées", qty_cible=P),
"phantasmal-affliction": IL("Mal imaginaire", V("existence", True), 3, ["maladie", "illusion"], why="se croit atteinte d'un mal"),
"placebo-effect": EP("Effet placebo", V("qualite"), 2, ["mal", "suspension"], why="un mal suspendu un temps"),
"planetarium": IL("Planétarium", VIS, P, ["ciel", "étoile"], why="le ciel nocturne projeté"),
"raiment-of-command": IL("Parure d'autorité", NVIS, 1, ["autorité"], why="une allure d'autorité"),
"searching-shadows": EP("Ombres fureteuses", VIS, P, ["ombre", "recherche"], why="les ombres cherchent pour toi"),
"shadow-anchor": EP("Ancre d'ombre", V("mouvement", True), 3, ["ombre", "attache"], why="retenue par son ombre"),
"shadowmind": EP("Esprit d'ombre", NVIS, 3, ["obscurité"], why="voit l'obscurité partout", qty_cible=3),
"shifted-steps": IL("Pas déplacés", NVIS, 3, ["son", "lieu"], why="ses bruits semblent venir d'ailleurs"),
"silent-table": IL("Table silencieuse", NVIS, P, ["silence", "secret"], why="nul son ne s'échappe de la table", alt=[H("Air", "l'air qui ne porte plus le son")]),
"symbol-of-mirroring": SYMP("Symbole des miroirs", impact=(P, ["image", "double"], "des doubles illusoires")),
"sympathetic-aura": IL("Aura sympathique", NVIS, P, ["aura", "faux-semblant"], why="toutes les auras voisines travesties", cible_obj=["objet"]),
"trail-of-the-rose": EP("Sillage de la rose", VIS, 1, ["parfum", "sillage"], why="une rose qui laisse un sillage parfumé", cible_obj=["rose"]),
"twilight-haze": EP("Brume crépusculaire", NVIS, P, ["brume", "vue"], why="une brume illusoire qui voile la vue"),
"umbral-weapon": EP("Arme ombreuse", EXI, 1, ["arme", "écho"], why="une ombre de l'arme frappe quand elle manque", cible_obj=["arme"]),
"undetectable-trap": IL("Piège indétectable", NVIS, 1, ["piège", "dissimulation"], why="un piège presque introuvable", cible_obj=["piège"]),
"adjustable-disguise": IL("Déguisement modulable", NVIS, 1, ["apparence", "changement"], why="un déguisement qui change à volonté"),
"air-of-authority": IL("Air d'autorité", NVIS, 1, ["autorité", "supérieur"], why="on te prend pour son supérieur"),
"aura-alteration": IL("Aura altérée", NVIS, 1, ["aura", "faux-semblant", "état"], why="ses auras toutes travesties"),
"cackling-skull": EP("Crâne ricanant", EXI, 1, ["message", "peur"], why="un crâne qui parle et effraie", cible_obj=["crâne"]),
"deceitful-veneer": IL("Vernis trompeur", NVIS, 3, ["mensonge"], why="semble mentir effrontément"),
"dreadscape": IL("Paysage d'effroi", NVIS, 3, ["cauchemar", "décor"], why="le monde comme un cauchemar", qty_cible=3),
"dream-dalliance": IL("Badinage onirique", V("existence", True), 3, ["rêve", "psyché"], why="un fantasme accroché à sa psyché"),
"false-future": IL("Faux avenir", NVIS, 1, ["avenir", "divination"], why="les présages montrent ce que tu choisis"),
"fearsome-duplicate": IL("Double effrayant", EXI, P, ["double", "menace"], why="un double menaçant de toi"),
"geomessage": EP("Message gravé", NVIS, 1, ["message", "surface"], why="un message caché dans une surface", cible_obj=["surface"]),
"hallucinatory-decor": IL("Décor hallucinatoire", NVIS, P, ["décor", "bâtiment"], why="l'aspect d'un bâtiment changé"),
"horrific-doubles": IL("Doubles horrifiques", EXI, 1, ["image", "horreur"], why="des doubles dérangeants"),
"illusion-of-treachery": IL("Illusion de trahison", NVIS, 3, ["trahison", "coupable"], why="un autre semble t'attaquer",
    options=[O("Illusion de trahison"), O("Illusion de trahison suprême", src_idx="illusion-of-treachery-greater", impact=(P, ["trahison", "coupable", "dissimulation"], "et tes gestes cachés"))]),
"illusory-poison": IL("Poison illusoire", V("existence", True), 1, ["poison", "illusion"], why="un poison imaginaire sur l'arme", cible_obj=["arme"]),
"impossible-angles": IL("Angles impossibles", NORD, P, ["géométrie"], why="la géométrie du lieu tordue"),
"instant-fake": IL("Contrefaçon", EXI, 1, ["copie", "objet"], why="une copie éphémère d'un objet", cible_obj=["objet"]),
"isolate": IL("Isolement", NVIS, 3, ["isolement"], why="invisible et muette pour ses alliés"),
"loathsome-veil": IL("Voile répugnant", NINT, P, ["nausée"], why="les plus faibles nauséeux"),
"mindscape-door": EP("Porte de l'esprit", V("relation"), P, ["passage", "esprit"], why="une porte vers un monde intérieur"),
"mirage": IL("Paysage trompeur", NVIS, P, ["terrain"], why="un paysage illusoire"),
"phantasmal-asphyxiation": IL("Asphyxie fantasmatique", V("existence", True), 3, ["souffle"], why="croit ne plus pouvoir respirer"),
"phantasmal-reminder": IL("Souvenir fantasmatique", V("existence", True), 3, ["blessure", "souvenir"], 18, "revit une blessure, 1d6 par niveau"),
"quieting-weapons": IL("Armes silencieuses", NVIS, 1, ["arme", "silence"], why="des armes muettes qui font taire", cible_obj=["arme"]),
"respectful-quiet": IL("Silence respectueux", NVIS, P, ["silence"], why="muets, mais entendant"),
"selective-invisibility": IL("Invisibilité choisie", NVIS, 1, ["invisibilité", "exception"], why="invisible sauf pour un seul"),
"shadow-jaunt": EP("Saut d'ombre", V("mouvement"), 1, ["téléportation", "image"], why="disparaître en laissant une image"),
"shroud-of-innocuity": IL("Voile d'innocuité", NVIS, 2, ["apparence", "banalité"], why="des gens ordinaires", qty_cible=3),
"stolen-light": IL("Lumière volée", VIS, 1, ["image", "gemme"], why="des images gardées dans une gemme", cible_obj=["gemme"]),
"sunstalker": IL("Traqueur solaire", NVIS, 2, ["invisibilité", "soleil"], why="invisible en plein soleil"),
"synesthesia": IL("Synesthésie", NORD, 3, ["sens", "confusion"], why="les sens mêlés", options=[O("Synesthésie"),
    O("Synesthésie de groupe", src_idx="synesthesia-mass", qty_cible=P)]),
"twine-double": EP("Double de ficelle", EXI, 1, ["double", "ficelle"], why="un double de toi fait de tissu et de ficelle"),
"vision-of-hell": IL("Vision infernale", V("force", True), P, ["enfer", "peur"], why="un paysage infernal qui effraie"),
"wall-of-nausea": IL("Mur de nausée", NINT, P, ["nausée", "mur"], why="qui traverse le mur est pris de nausée"),
"dream-council": EP("Conseil des rêves", REL, 2, ["rêve", "conseil"], why="parler à plusieurs dormeurs", loc=(P, None, "illimitée"), qty_cible=P, cond=["sommeil"]),
"minor-phantom-object": EP("Objet fantôme", EXI, 1, ["objet", "quasi-réel"], why="un objet semi-réel", options=[O("Objet fantôme mineur"),
    O("Objet fantôme majeur", src_idx="major-phantom-object", impact=(P, ["objet", "quasi-réel", "minéral"], "un objet semi-réel, même minéral"))]),
"phantasmal-putrefaction": IL("Putréfaction fantasmatique", V("existence", True), 3, ["pourriture"], why="croit sa chair pourrir", qty_cible=10),
"shadow-barbs": EP("Barbelés d'ombre", EXI, 1, ["chaîne", "épine"], why="une chaîne hérissée d'ombre"),
"shadow-step": EP("Pas d'ombre", V("mouvement"), 1, ["téléportation", "ombre"], why="d'une ombre à l'autre"),
"shadowform": EP("Forme d'ombre", V("nature"), 2, ["corps", "ombre"], why="un corps d'ombre qui encaisse moins"),
"shocking-image": IL("Images électriques", EXI, 1, ["image", "foudre"], 4, "des doubles qui foudroient en disparaissant"),
"telepathic-silence": EP("Silence télépathique", NREL, P, ["télépathie", "silence"], why="nulle télépathie dans la zone"),
"wandering-star-motes": IL("Étoiles errantes", VIS, 3, ["lumière", "contour"], why="sa silhouette révélée, sa lumière errante", alt=LUMH()),
"cloak-of-shadows": EP("Manteau d'ombres", V("relation", True), 1, ["lumière", "protection"], why="les ombres te gardent de la lumière"),
"deceptive-redundancy": IL("Redondance trompeuse", NVIS, 1, ["sort", "dissipation"], why="tes sorts protégés de la dissipation"),
"fable-tapestry": EP("Tapisserie de fable", EXI, P, ["légende", "héros"], why="un héros de légende appelé"),
"illusory-hoard": IL("Trésor illusoire", NVIS, 3, ["trésor", "intact"], why="croit son trésor intact"),
"phantasmal-web": IL("Toile fantasmatique", V("mouvement", True), 3, ["toile", "entrave"], why="prise dans une toile illusoire", qty_cible=9),
"psychic-asylum": EP("Asile psychique", V("ordre"), 1, ["esprit", "retraite"], why="un long travail mené dans un monde intérieur"),
"shadow-endurance": EP("Endurance d'ombre", V("relation", True), 1, ["protection", "ombre"], why="des volutes d'ombre qui protègent"),
"symbol-of-striking": SYMP("Symbole de frappe", impact=(P, ["coup"], "frappés au passage")),
"village-veil": IL("Voile du village", NVIS, P, ["valeur", "village"], why="le lieu paraît sans intérêt"),
"baleful-shadow-transmutation": IL("Métamorphose d'ombre funeste", V("nature", True), 3, ["ombre", "métamorphose"], why="croit son corps transformé"),
"dirge-of-the-victorious-knights": IL("Charge des chevaliers spectraux", V("existence", True), P, ["cavalier", "piétinement"], why="des chevaliers spectraux qui piétinent"),
"dream-reality": IL("Réalité rêvée", NVIS, 3, ["rêve", "réalité"], why="se croit en train de rêver"),
"night-terrors": IL("Terreurs nocturnes", V("existence", True), 3, ["cauchemar", "repos"], why="son repos ruiné de rêves sombres"),
"shadow-transmutation": EP("Métamorphose d'ombre", V("nature"), 1, ["ombre", "métamorphose"], why="un corps changé par l'énergie astrale",
    options=[O("Métamorphose d'ombre"), O("Métamorphose d'ombre suprême", src_idx="shadow-transmutation-greater", impact=(P, ["ombre", "métamorphose", "créature"], "un corps changé en toute créature"))]),
"subjective-reality": EP("Réalité subjective", NVIS, 1, ["illusion", "réalité"], why="ce que tu tiens pour illusion n'a plus prise"),
"familiar-double": IL("Image du familier", EXI, 2, ["double", "compagnon", "lointain"], why="ton image qui suit ton familier", cond=["compagnon"]),
"lunar-veil": EP("Voile lunaire", NVIS, P, ["lumière", "lune"], why="la lumière éteinte, les lycanthropes ramenés"),
"phantasmal-revenge": IL("Vengeance fantasmatique", V("existence", True), 7, ["vengeance", "fantôme"], why="un fantôme traque son meurtrier", cond=["mort"]),
"vision-of-lamashtu": IL("Vision cauchemardesque", V("existence", True), 3, ["cauchemar", "sort"], why="un cauchemar, puis un sort au réveil", loc=(P, None, "illimitée")),
"mantle-of-doubt": EP("Manteau de doute", NINT, 1, ["doute"], why="le doute paralyse qui t'attaque"),
"microcosm": EP("Microcosme", NREL, 3, ["esprit", "prison"], why="enfermés à jamais dans un monde intérieur", qty_cible=P),
"psychic-image": IL("Image psychique", EXI, 1, ["double", "sort"], why="un double de toi qui lance tes sorts"),
}
del NEWPF_ILL["hallucination"]
NEWPF_ILL["auditory-hallucination"] = IL("Hallucination", EXI, 3, ["fantasme"], why="un fantasme perçu par les sens", qty_cible=1, options=[
    O("Hallucination auditive", **I("fantasme", "son", why="un fantasme sonore")),
    O("Hallucination audiovisuelle", src_idx="audiovisual-hallucination", **I("fantasme", "son", "image", why="un fantasme sonore et visible")),
    O("Hallucination complexe", src_idx="complex-hallucination", **I("fantasme", "sens", why="un fantasme pour tous les sens")),
    O("Hallucination scénarisée", src_idx="scripted-hallucination", **I("fantasme", "sens", "scénario", why="qui suit son scénario")),
    O("Hallucination déclenchée", src_idx="triggered-hallucination", **I("fantasme", "sens", "déclencheur", why="qui attend son signal")),
    O("Hallucination permanente", src_idx="permanent-hallucination", **I("fantasme", "sens", "permanence", why="à jamais"))])
# ombre : énergie astrale, donc une forme lumineuse et une forme ténébreuse (règle de réciprocité)
for k, f in NEWPF_ILL.items():
    if _C.PF1[k].get("_sub") == "shadow":
        v, w, why = f["impact"]
        if f.get("options"):
            f["options"] = [dict(o, label=f"{o['label']} — {e}", impact=(o.get("impact", f["impact"])[0], list(o.get("impact", f["impact"])[1]) + [e], o.get("impact", f["impact"])[2]))
                            for o in f["options"] for e, _ in ASTR]
        else:
            f["options"] = [O(f"Forme {ef}", impact=(v, list(w) + [e], why)) for e, ef in ASTR]
FICHES.update(NEWPF_ILL)
PFV("Illusion")
FICHES["invisibility"]["vpf"] = dict(options=[O("Invisibilité"), O("Disparition", src_idx="vanish"), O("Sphère d'invisibilité", src_idx="invisibility-sphere", aoe={"type": "sphere", "size": 10}),
    O("Invisibilité de groupe", src_idx="invisibility-mass", qty_cible=P)])
FICHES["disguise-self"]["vpf"] = dict(options=[O("Déguisement"), O("Déguisement d'autrui", src_idx="disguise-other", cible=2)])
FICHES["arcanists-magic-aura"]["vpf"] = dict(src_idx="magic-aura", options=[O("Aura magique"), O("Aura magique suprême", src_idx="magic-aura-greater", cible=3)])
FICHES["false-vision"]["vpf"] = dict(options=[O("Vision mensongère"), O("Vision mensongère suprême", src_idx="false-vision-greater", cible=2)])
FICHES["simulacrum"]["vpf"] = dict(options=[O("Simulacre"), O("Simulacre mineur", src_idx="simulacrum-lesser")])

# --- Pathfinder 1, lot 3 : Divination ---
PF1_RELECTURE.update({
"cultural-adaptation-taldan": "imite une culture de Golarion (Taldor) : dépend de leur monde",
"karmic-blessing": "fait d'une compétence une « compétence de classe » : pure mécanique de jeu",
"lend-judgment": "prête un « jugement » d'inquisiteur : pure mécanique de classe",
"lend-judgment-greater": "prête les « jugements » d'inquisiteur : pure mécanique de classe",
"sense-spirit-magic": "repose sur les esprits du chaman : pure mécanique de classe",
"sure-casting": "augmente le niveau de lanceur contre la résistance à la magie : pure mécanique de jeu",
"twisted-futures": "annule les capacités « deux jets, le meilleur » : pure mécanique de jeu",
"cleromancy": "fait jouer des dés au lanceur : pure mécanique de jeu",
"embrace-destiny": "garde un jet de dé pour plus tard : pure mécanique de jeu",
"threefold-sight": "fait jeter trois dés : pure mécanique de jeu",
"calculated-luck": "repose sur la « Voie des Nombres » de Golarion et sur des jets de dés",
"enemy-insight": "repose sur les « ennemis jurés » du rôdeur : pure mécanique de classe",
"hunters-lore": "permet des tests de connaissance non formés : pure mécanique de jeu",
"coordinated-effort": "accorde un « don d'équipe » : pure mécanique de jeu",
"awaken-the-devoured": "vise les daémons d'Abaddon, propres à la cosmologie de Golarion",
"harrowing-greater": "repose sur le jeu de cartes du Harrow, propre à Golarion",
"early-judgment": "montre le sort qui attend l'âme dans l'au-delà de Golarion : dépend de leur monde",
})
DIV = lambda fr, cible, words, v=None, why="", **kw: EP(fr, VIS, cible, words, v, why, **kw)
NEWPF_DIV = {
"detect-psychic-significance": DIV("Détection de l'empreinte psychique", P, ["empreinte", "objet"], why="les objets chargés de souvenirs"),
"enhanced-diplomacy": EP("Parole persuasive", INT, 2, ["éloquence"], why="plus persuasive ou plus intimidante"),
"sift": DIV("Tamisage", P, ["examen"], why="examiner la zone à distance"),
"anticipate-peril": DIV("Danger pressenti", 2, ["danger", "vigilance"], why="pressent le danger"),
"authenticating-gaze": DIV("Regard authentificateur", 1, ["authenticité", "écrit"], why="voit le faux dans les livres et les parchemins"),
"build-trust": EP("Confiance", REL, 3, ["confiance"], why="la confiance gagnée"),
"carrion-compass": DIV("Boussole de charogne", 3, ["direction", "maître"], why="le mort-vivant mène à son maître", cond=["MORTVIVANT"]),
"commune-with-birds": DIV("Communion avec les oiseaux", P, ["oiseau", "réponse"], why="les oiseaux répondent à ta question"),
"cultural-adaptation": DIV("Adaptation culturelle", 1, ["coutume"], why="les usages du lieu compris"),
"deadeyes-lore": DIV("Savoir du pisteur", 1, ["piste"], why="suivre une piste sans ralentir"),
"detect-aberration": DIV("Détection des aberrations", 9, ["aura", "présence", "force"], why="présence, nombre et force", cible_note=["ABERRATION"]),
"detect-charm": DIV("Détection des charmes", P, ["charme", "possession"], why="charmes, contraintes et possessions décelés"),
"detect-metal": DIV("Détection du métal", P, ["métal"], why="objets et créatures de métal"),
"detect-the-faithful": DIV("Détection des fidèles", P, ["foi"], why="les fidèles de ta foi"),
"diagnose-disease": DIV("Diagnostic", 3, ["maladie", "nature"], why="la maladie décelée et nommée"),
"discern-next-of-kin": DIV("Parentèle", 3, ["famille"], why="ce qu'elle pense de sa famille"),
"halfling-vengeance": EP("Vengeance du petit", INT, 2, ["arme", "faille"], why="un petit qui frappe là où ça fait mal", cond=["petit"],
    options=[O("Vengeance du petit"), O("Vengeance des petits", src_idx="halfling-vengeance-mass", qty_cible=10)]),
"heightened-awareness": DIV("Vigilance accrue", 1, ["mémoire", "esprit"], why="mémoire et esprit plus vifs"),
"know-peerage": DIV("Savoir nobiliaire", 2, ["noblesse", "savoir"], why="le savoir des lignages nobles"),
"know-the-enemy": DIV("Connais ton ennemi", 1, ["savoir", "créature"], why="tout savoir d'une créature"),
"kreightons-perusal": DIV("Lecture éclair", 1, ["livre", "savoir"], why="un livre compris d'un coup d'œil", cible_obj=["livre"]),
"linked-legacy": EP("Héritage partagé", REL, 2, ["savoir", "partage"], why="un savoir partagé en un instant", qty_cible=3),
"locate-portal": DIV("Localisation des portails", P, ["portail"], why="les portails à portée"),
"locksight": DIV("Œil du serrurier", 1, ["serrure"], why="l'état d'une serrure à distance"),
"mental-block": EP("Blocage mental", NREL, 3, ["savoir-faire", "blocage"], why="privée de tout son savoir-faire"),
"mind-thrust-i": EP("Poussée mentale", V("existence", True), 3, ["esprit"], 4, "1d6 par niveau", options=[
    O(f"Poussée mentale {r}", src_idx=f"mind-thrust-{r.lower()}", impact=(n, ["esprit"] + x, d)) for r, n, x, d in [
    ("I", 4, [], "1d6 en moyenne"), ("II", 14, [], "3d8 en moyenne"), ("III", 23, [], "5d8 en moyenne"), ("IV", 32, ["fatigue"], "7d8 en moyenne, puis fatiguée"),
    ("V", 41, ["épuisement"], "9d8 en moyenne, puis épuisée"), ("VI", 50, ["épuisement", "étourdissement"], "11d8 en moyenne, épuisée et étourdie")]]),
"mindlink": EP("Lien mental", REL, 2, ["pensée", "partage"], why="beaucoup d'idées transmises en un instant"),
"natures-paths": DIV("Chemins de la nature", 2, ["chemin"], why="le meilleur chemin à travers le pays"),
"object-reading": DIV("Lecture d'objet", 1, ["empreinte", "passé"], why="l'histoire laissée sur un objet", cible_obj=["objet"]),
"petulengros-validation": DIV("Origine révélée", 1, ["origine"], why="à qui appartenait le morceau manquant"),
"pierce-facade": DIV("Façade percée", 2, ["déguisement"], why="voit à travers les déguisements"),
"planar-orientation": DIV("Orientation planaire", 1, ["lieu", "pouvoir"], why="les lieux de pouvoir du plan"),
"play-instrument": EP("Musicien d'un jour", INT, 1, ["musique"], why="jouer comme un musicien"),
"preserve-grace": EP("Grâce préservée", INT, 2, ["conscience", "guidance"], why="une conscience qui avertit", cond=["allié"]),
"psychic-reading": DIV("Lecture psychique", 3, ["pensée"], why="ses pensées de surface sur un sujet", cond=["humanoïde"]),
"read-weather": DIV("Lecture du temps", 1, ["climat", "avenir"], why="le temps des deux jours à venir"),
"residual-tracking": DIV("Pistage résiduel", 1, ["trace", "apparence"], why="l'allure de qui a laissé l'empreinte", cible_obj=["empreinte"]),
"reveal-mirage": DIV("Mirage révélé", 1, ["mirage"], why="le faux paysage vu de loin"),
"rumormonger": DIV("Colporteur", P, ["rumeur"], why="suivre une rumeur dans sa course"),
"rune-trace": DIV("Trace de rune", 1, ["rune", "savoir"], why="une rune lue sans la déclencher", cible_obj=["rune"]),
"secret-speech": EP("Parole secrète", REL, 2, ["message", "secret"], why="des messages cachés dans la conversation"),
"see-alignment": DIV("Vision des intentions", 1, ["aura", "lueur"], why="ce qui porte la charge choisie luit", options=[
    O("Hostilité", cible_note=["hostile"]), O("Lumineux", cible_note=["lumineux"]), O("Ténébreux", cible_note=["ténébreux"])]),
"sense-fear": DIV("Perception de la peur", 1, ["peur"], why="qui a peur alentour"),
"share-language": EP("Langue partagée", REL, 2, ["langue"], why="comprend la langue choisie",
    options=[O("Langue partagée"), O("Langues partagées", src_idx="share-language-communal", qty_cible=P)]),
"skim": DIV("Lecture rapide", 1, ["lecture"], 4, "lire quatre fois plus vite"),
"speak-local-language": EP("Parler du pays", REL, 2, ["langue", "région"], why="parler la langue de la région"),
"speechreaders-sight": DIV("Lecture sur les lèvres", 1, ["lèvres"], why="lire sur les lèvres de loin"),
"starsight": DIV("Vue des étoiles", 1, ["ciel", "étoile"], why="le ciel nocturne vu sans voile"),
"tap-inner-beauty": EP("Beauté intérieure", INT, 1, ["charisme"], 2, "+2 en charisme"),
"timely-inspiration": EP("Inspiration opportune", INT, 2, ["inspiration"], why="une seconde chance après l'échec"),
"true-appraisal": DIV("Juste estimation", 1, ["valeur"], why="la juste valeur des choses"),
"true-skill": EP("Vrai savoir-faire", INT, 1, ["savoir-faire"], why="ton savoir-faire grandi le temps d'un geste"),
"whispering-lore": DIV("Savoir murmuré", 1, ["savoir", "terrain"], why="le pays te souffle son savoir"),
"analyze-aura": DIV("Analyse d'aura", 3, ["aura", "état"], why="ses auras lues une à une"),
"ancestral-communion": DIV("Communion ancestrale", 1, ["ancêtre", "savoir"], why="les esprits des ancêtres consultés"),
"anticipate-thoughts": DIV("Pensées anticipées", 3, ["pensée", "garde", "coup"], why="ses gestes devinés"),
"aquatic-trail": DIV("Piste aquatique", P, ["piste", "eau"], why="suivre une piste sous l'eau"),
"aram-zeys-focus": DIV("Œil du désamorceur", 1, ["piège", "mécanisme"], why="les pièges compris et désamorcés"),
"beastspeak": EP("Parole de la bête", REL, 1, ["parole", "bête", "métamorphose"], why="parler sous forme animale"),
"beloved-of-the-forge": DIV("Aimé de la forge", 1, ["direction", "foyer"], why="le chemin de ton atelier"),
"blood-biography": DIV("Biographie du sang", 1, ["sang", "savoir"], why="une vie lue dans son sang", cible_obj=["sang"]),
"create-treasure-map": DIV("Carte au trésor", 7, ["trésor", "carte"], why="une carte tirée d'un cadavre", cond=["mort"]),
"detect-anxieties": DIV("Détection des angoisses", P, ["angoisse"], why="ce qui inquiète chacun"),
"detect-desires": DIV("Détection des désirs", P, ["désir"], why="ce que chacun désire"),
"detect-mindscape": DIV("Détection des mondes intérieurs", P, ["esprit", "monde"], why="les mondes intérieurs alentour"),
"detect-relations": DIV("Détection de la parenté", 3, ["famille", "sang"], why="qui est parent de qui", qty_cible=3),
"determine-depth": DIV("Mesure de l'épaisseur", 1, ["épaisseur"], why="l'épaisseur exacte d'une paroi", cible_obj=["paroi"]),
"eagle-eye": DIV("Œil d'aigle", P, ["capteur", "hauteur"], why="un œil magique haut dans le ciel"),
"elemental-speech": EP("Parole élémentaire", REL, 1, ["parole", "élémentaire"], why="parler aux élémentaires"),
"enchantment-sight": DIV("Vision des enchantements", 1, ["enchantement"], why="les charmes actifs sur chacun"),
"focused-scrutiny": DIV("Examen attentif", 3, ["examen"], why="tout percevoir de quelqu'un"),
"follow-aura": DIV("Suivre l'aura", 1, ["aura", "piste"], why="suivre la trace d'une charge", options=[
    O("Hostilité", cible_note=["hostile"]), O("Lumineux", cible_note=["lumineux"]), O("Ténébreux", cible_note=["ténébreux"])]),
"gallant-inspiration": EP("Inspiration galante", INT, 2, ["inspiration"], 5, "2d4 ajouté après l'échec"),
"guiding-star": DIV("Étoile guide", 1, ["direction", "distance"], why="sait toujours où se trouve le lieu de lancement"),
"hunters-eye": DIV("Œil du chasseur", 3, ["perception", "traque"], why="impossible à perdre de vue"),
"hypercognition": DIV("Hypercognition", 1, ["mémoire", "savoir"], why="tout ce que tu sais, rappelé d'un coup"),
"lay-of-the-land": DIV("Configuration du pays", 1, ["terrain"], why="la géographie alentour"),
"locate-weakness": DIV("Point faible", 1, ["faille"], why="trouver le point faible"),
"mindshock": EP("Choc mental", V("existence", True), 1, ["esprit", "coup"], why="des coups chargés d'énergie psychique"),
"open-book": DIV("Livre ouvert", 3, ["savoir", "permanence"], why="plus facile à percer à jour"),
"pack-empathy": EP("Empathie de meute", REL, 2, ["lien", "émotion"], why="un lien empathique entre alliés", qty_cible=3),
"page-bound-epiphany": DIV("Épiphanie de la page", 1, ["livre", "savoir"], why="un livre rempli du savoir du monde"),
"perfect-placement": DIV("Placement parfait", 2, ["position", "garde"], why="chacun à sa juste place", qty_cible=3),
"replay-tracks": DIV("Traces revécues", 1, ["piste", "passé"], why="revoir ce qui a laissé les traces"),
"revelation": DIV("Révélation", 1, ["mécanisme", "énigme"], why="une énigme comprise"),
"riversight": DIV("Vue de la rivière", P, ["eau", "vue"], why="voir le long d'un cours d'eau", cible_obj=["eau"]),
"seed-spies": DIV("Graines espionnes", P, ["graine", "espion"], why="des graines qui espionnent pour toi"),
"seek-thoughts": DIV("Recherche des pensées", P, ["pensée"], why="qui pense à quoi"),
"sense-vitals": DIV("Organes vitaux", 1, ["faille", "vital"], why="voir les points vitaux"),
"sensory-amplifier": EP("Amplificateur sensoriel", INT, P, ["vue"], why="la vue de chacun aiguisée"),
"share-memory": EP("Mémoire partagée", REL, 2, ["mémoire", "partage"], why="un souvenir partagé"),
"spell-gauge": DIV("Jauge des sorts", 3, ["sort"], why="quelques-uns de ses sorts révélés"),
"storm-sight": DIV("Vue de l'orage", P, ["orage", "vue"], why="sentir à travers la tempête"),
"track-ship": DIV("Traque du navire", 4, ["navire", "piste"], why="suivre un navire sur la carte"),
"voluminous-vocabulary": EP("Vocabulaire immense", REL, 2, ["langue"], 1, "une ou plusieurs langues"),
"wild-instinct": DIV("Instinct sauvage", 1, ["perception", "sommeil"], why="vigilant même endormi"),
"aerial-tracks": DIV("Pistes aériennes", P, ["piste", "air"], why="suivre ce qui vole"),
"akashic-communion": DIV("Communion akashique", 1, ["savoir", "mémoire"], why="puiser dans la mémoire du monde"),
"aura-sight": DIV("Vue des auras", 1, ["aura", "hostile", "astral"], why="intentions et charges astrales visibles"),
"beacon-of-luck": EP("Phare de chance", INT, P, ["chance"], why="une vague de chance pour tes alliés"),
"discern-value": DIV("Discerner la valeur", P, ["valeur"], why="ce qui vaut le plus"),
"domination-link": DIV("Lien de domination", P, ["domination", "maître"], why="qui contrôle qui"),
"find-fault": DIV("Défaut trouvé", 3, ["faille"], 5, "ses faiblesses révélées"),
"gilded-whispers": DIV("Murmures dorés", 1, ["écoute", "pièce"], why="une pièce qui écoute pour toi", cible_obj=["pièce"]),
"glimpse-of-truth": DIV("Éclair de vérité", 1, ["vérité", "vision"], why="voir vrai un instant"),
"insect-spies": DIV("Insectes espions", P, ["insecte", "espion"], why="des scarabées espions",
    options=[O("Insectes espions"), O("Insectes espions suprêmes", src_idx="insect-spies-greater", impact=(P, ["insecte", "espion", "sens"], "et leurs sens partagés"))]),
"irriseni-mirror-sight": DIV("Vue par les miroirs", 1, ["miroir", "vue"], why="voir par un miroir lointain"),
"litany-of-sight": DIV("Litanie de la vue", 1, ["invisible"], why="voir l'invisible à courte portée"),
"mark-of-obvious-ethics": DIV("Marque d'intention", 2, ["hostile", "astral", "marque"], why="ses intentions et sa charge visibles de tous"),
"meticulous-match": DIV("Comparaison minutieuse", 1, ["identité", "objet"], why="deux choses identiques ou non", qty_cible=2),
"mind-probe": DIV("Sonde mentale", 3, ["mémoire", "réponse"], why="ses souvenirs interrogés"),
"mnemonic-siphon": EP("Siphon mnémonique", V("flux"), 1, ["sort", "vol"], why="voler les sorts de qui porte l'objet", cible_obj=["objet"]),
"named-bullet": EP("Projectile nommé", INT, 1, ["projectile", "désigné"], why="un projectile qui cherche une sorte de créature", cible_obj=["projectile"],
    options=[O("Projectile nommé"), O("Projectile nommé suprême", src_idx="named-bullet-greater", impact=(P, ["projectile", "désigné", "blessure"], "et plus meurtrier"))]),
"pierce-disguise": DIV("Déguisement percé", 1, ["déguisement", "magie"], why="voir à travers les déguisements magiques"),
"retrocognition": DIV("Rétrocognition", P, ["passé", "lieu"], why="les échos des événements passés"),
"reveal-emotions": DIV("Émotions révélées", P, ["émotion"], why="l'état d'âme de chacun"),
"sand-table": DIV("Table de sable", P, ["carte", "terrain"], why="un modèle du pays et de ses habitants"),
"see-beyond": DIV("Vue au-delà", 1, ["perception", "éthéré"], why="voir l'invisible et l'éthéré"),
"see-through-stone": DIV("Regard de pierre", 2, ["pierre", "transparence"], why="voir à travers la roche"),
"share-senses": DIV("Sens partagés", 2, ["sens", "compagnon"], why="percevoir par ton familier", cond=["compagnon"]),
"signs-of-the-land": DIV("Signes du pays", 1, ["terrain", "savoir"], 3, "trois choses sur le pays"),
"speak-with-plane": EP("Parole au plan", REL, 9, ["parole", "plan"], why="parler à un plan conscient"),
"spirit-bonds": EP("Liens d'esprit", REL, 2, ["lien", "message"], why="des liens qui portent un message", qty_cible=2),
"symbol-of-revelation": SYMP("Symbole de révélation", verb=VIS, impact=(P, ["illusion", "révélation"], "les illusions révélées")),
"vicarious-view": DIV("Vue par procuration", 4, ["capteur"], why="un capteur planté pour espionner"),
"witness": DIV("Témoin", 3, ["vue", "ouïe"], why="voir et entendre par ses sens"),
"ancestral-memory": DIV("Mémoire ancestrale", 1, ["ancêtre", "savoir"], 5, "les ancêtres soufflent leur savoir"),
"battlemind-link": EP("Lien de bataille", REL, 2, ["lien", "garde", "coup"], why="toi et un allié plus forts ensemble"),
"find-quarry": DIV("Trouver la proie", 4, ["présence"], why="savoir si une créature est dans les parages"),
"foretell-failure": DIV("Échec prédit", 1, ["avenir", "échec"], why="savoir si une entreprise échouera"),
"litany-of-truth": DIV("Litanie de vérité", 3, ["illusion", "dissipation"], why="les illusions sur elle arrachées"),
"percieve-betrayal": DIV("Perception de la trahison", 1, ["trahison"], why="sentir l'intention de trahir"),
"questing-stone": DIV("Pierre de quête", 1, ["capteur", "pierre"], why="une pierre devenue capteur", cible_obj=["pierre"]),
"soulseeker": DIV("Chercheur d'âme", 7, ["âme", "lieu"], why="où se trouve une âme"),
"thoughtsense": DIV("Sens des pensées", 1, ["pensée", "présence"], why="sentir les êtres conscients"),
"trace-teleport": DIV("Trace de téléportation", P, ["téléportation", "origine"], why="d'où et vers où l'on s'est téléporté"),
"traveling-dream": DIV("Rêve voyageur", P, ["rêve", "capteur"], why="voir au loin pendant ton sommeil"),
"unerring-tracker": DIV("Pisteur infaillible", 1, ["piste"], why="suivre une piste sans faillir"),
"watchful-animal": DIV("Animal vigilant", 2, ["capteur", "compagnon"], why="espionner par ton compagnon", cond=["compagnon"]),
"commune-with-plane": DIV("Communion avec le plan", 1, ["plan", "terrain"], why="le relief du plan"),
"commune-with-texts": DIV("Communion avec les textes", P, ["livre", "savoir"], why="trouver le bon passage d'une bibliothèque"),
"dream-scan": DIV("Lecture de rêve", 3, ["rêve", "pensée"], why="lire les pensées d'un dormeur", loc=(P, None, "illimitée"), cond=["sommeil"]),
"dungeonsight": DIV("Vue des souterrains", 1, ["plan", "lieu"], why="le plan des lieux"),
"jungle-mind": DIV("Esprit de la jungle", P, ["bête", "savoir"], why="savoir par l'esprit des bêtes"),
"locate-gate": DIV("Localisation des portes", P, ["portail", "plan"], why="les portails proches"),
"mask-from-divination": EP("Masque contre la divination", NVIS, 2, ["divination"], why="caché à la divination"),
"remote-viewing": DIV("Vision à distance", 4, ["lieu", "lointain"], why="des impressions d'un lieu lointain"),
"symbol-of-scrying": SYMP("Symbole de scrutation", verb=VIS, impact=(P, ["capteur"], "un capteur s'éveille")),
"synapse-overload": EP("Surcharge synaptique", V("existence", True), 3, ["esprit", "chancellement"], 32, "1d6 par niveau, chancelante"),
"telepathy": EP("Télépathie", REL, 1, ["pensée", "parole"], why="parler par la pensée"),
"truespeak": EP("Vraie parole", REL, 1, ["parole", "esprit"], why="parler à tout être doué d'esprit"),
"contact-nalfeshnee": EP("Contact démoniaque", REL, 9, ["savoir", "démon"], why="consulter un savant démon"),
"prophetic-lore": DIV("Savoir prophétique", 1, ["prophétie"], why="prophétiser sur un sujet"),
"sarzari-shadow-memory": DIV("Mémoire de l'assassin", 1, ["cible", "savoir"], why="tout savoir pour frapper une cible"),
"speak-with-waves": EP("Parole des eaux", REL, 1, ["parole", "eau"], why="parler à l'eau", alt=[H("Eau", "l'eau")]),
"tectonic-communion": DIV("Communion tectonique", 1, ["terrain", "savoir"], why="savoir de la terre sur une vaste étendue"),
"grasp": EP("Prise sûre", INT, 1, ["prise", "escalade"], why="des mains qui ne lâchent pas la paroi"),
"threefold-form": EP("Forme triple", V("identite"), 1, ["double", "triple"], why="trois toi en trois lieux"),
}
FICHES.update(NEWPF_DIV)
PFV("Divination")
for k, extra in [("see-invisibility", O("Coup d'œil sur le caché", src_idx="glimpse-the-hidden", cible=2)), ("tongues", O("Langues partagées", src_idx="tongues-communal", qty_cible=P))]:
    base = FICHES[k].get("vpf") or {}
    FICHES[k]["vpf"] = {**base, "options": (base.get("options") or [O(FICHES[k]["fr"])]) + [extra]}
FICHES["detect-magic"]["vpf"] = dict(options=[O("Détection de la magie"), O("Détection de la magie suprême", src_idx="detect-magic-greater", impact=(P, ["aura", "école", "sort"], "et les sorts eux-mêmes")),
    O("Œil de l'identificateur", src_idx="identifiers-eye", cible=2)])
FICHES["detect-undead"]["vpf"] = dict(options=[O("Détection des morts-vivants"), O("Sens de la non-vie", src_idx="undeath-sense", cible=2)])

# --- Pathfinder 1, lot 4 : Abjuration ---
PF1_MEME = {}   # sorts PF1 qui donnent exactement le même glyphe qu'une page existante (ex. « contre le bien » = forme « contre l'hostile »)
def ADDPF(k, *extra):
    """ajoute des formes Pathfinder 1 (versions partagées, variantes) à la version PF1 d'une page"""
    base = FICHES[k].get("vpf") or {}
    cur = base.get("options") or FICHES[k].get("options") or [O(FICHES[k]["fr"])]
    FICHES[k]["vpf"] = {**base, "options": list(cur) + list(extra)}
PF1_RELECTURE.update({
"aura-of-greater-courage": "renforce l'« aura de courage » du paladin : pure mécanique de classe",
"bestow-auras": "transmet les auras du paladin : pure mécanique de classe",
"defile-armor": "ne vaut que pendant le « jugement » ou le « châtiment » : pure mécanique de classe",
"charons-dispensation": "protège du Styx et de son passeur, propres à la cosmologie de Golarion",
"counterbalancing-aura": "repose sur la neutralité d'alignement, sans équivalent dans nos charges : à revoir",
"dispel-balance": "repose sur la neutralité d'alignement, sans équivalent dans nos charges : à revoir",
"fallback-strategy": "accorde un nouveau jet de dé : pure mécanique de jeu",
"grace": "évite les « attaques d'opportunité » : pure mécanique de jeu",
"line-in-the-sand": "multiplie les « attaques d'opportunité » : pure mécanique de jeu",
"litany-of-duty": "accorde un nouveau jet de sauvegarde : pure mécanique de jeu",
"scales-of-deflection": "joue sur la « CA de contact » : pure mécanique de jeu",
"warding-weapon": "permet de lancer sans « attaque d'opportunité » : pure mécanique de jeu",
"abjuring-step": "permet de lancer sans « attaque d'opportunité » : pure mécanique de jeu",
"hex-glyph": "inscrit un « maléfice » de sorcière : pure mécanique de classe",
"hex-glyph-greater": "inscrit un « maléfice » de sorcière : pure mécanique de classe",
})
PF1_MEME.update({"protection-from-good": "protection-from-evil-and-good", "protection-from-good-communal": "protection-from-evil-and-good",
    "magic-circle-against-good": "magic-circle", "dispel-good": "dispel-evil-and-good", "shield-companion-acg": "shield-other"})
GA = lambda fr, cible, words, v=None, why="", **kw: EP(fr, SEP, cible, words, v, why, **kw)
DISP = V("trame", True)
TRIPF = lambda: [O("Contre l'hostile", cond=["hostile"]), O("Contre le lumineux", cond=["lumineux"]), O("Contre le ténébreux", cond=["ténébreux"])]
NEWPF_ABJ = {
"abeyance": EP("Suspension", DISP, 3, ["malédiction", "suspension"], why="une malédiction mise en sommeil"),
"ablative-sphere-garundi": GA("Sphère ablative", 1, ["sphère", "garde"], why="une sphère qui encaisse à ta place"),
"absolution": EP("Absolution", V("qualite"), 2, ["enchantement", "pardon"], why="délivrée des charmes, ses actes sous leur emprise pardonnés"),
"absorb-rune-i": EP("Absorption de rune", DISP, 1, ["rune", "absorption"], why="une rune magique absorbée, à déplacer ou dissiper", cible_obj=["rune"], options=[
    O(f"Absorption de rune {r}", src_idx=f"absorb-rune-{r.lower()}", impact_sats=[(n, ["seuil", "niveau"])]) for r, n in [("I", 3), ("II", 5), ("III", 8)]]),
"alleviate-corruption": EP("Corruption atténuée", V("qualite"), 2, ["corruption", "risque"], why="une corruption affaiblie, au péril du lanceur"),
"allied-cloak": GA("Cape alliée", 1, ["cape", "garde", "aide"], why="une cape qui te garde et te prête main-forte"),
"animus-mine": GA("Mine mentale", 1, ["esprit", "piège"], 9, "qui touche ton esprit en paie le prix", options=[
    O("Mine mentale"), O("Mine mentale suprême", src_idx="animus-mine-greater", impact=(P, ["esprit", "piège", "étourdissement"], "qui touche ton esprit est étourdi"))]),
"anti-incorporeal-shell": GA("Coquille anti-intangible", 1, ["intangible", "barrière"], why="les êtres intangibles tenus à trois mètres"),
"antitoxin-touch": GA("Toucher antitoxique", 2, ["poison"], why="à l'abri du poison qui frôle"),
"aram-zeys-trap-ward": GA("Garde contre les pièges", 1, ["piège", "magie"], why="les pièges magiques ne mordent pas"),
"arcana-theft": EP("Vol d'arcane", DISP, 3, ["sort", "vol"], why="un sort dissipé sur elle et repris pour toi"),
"arodens-spellbane": GA("Fléau des sorts", P, ["sort", "interdit"], why="les sorts choisis ne prennent pas ici"),
"aura-of-inviolate-ownership": GA("Aura de propriété", 1, ["objet", "vol"], why="tes affaires impossibles à dérober"),
"ban-corruption": EP("Corruption bannie", DISP, 3, ["corruption", "don"], why="les dons de la corruption arrachés"),
"banish-seeming": EP("Apparence bannie", DISP, 3, ["illusion", "métamorphose"], why="illusion ou forme d'emprunt dissipée"),
"banishing-blade": EP("Lame de bannissement", INT, 1, ["arme", "repousser"], why="chaque coup repousse l'adversaire", cible_obj=["arme"]),
"bestow-grace": GA("Grâce accordée", 2, ["grâce", "résistance"], why="ta grâce devient sa garde"),
"blade-snare": GA("Piège à lames", P, ["arme", "piège"], why="un piège invisible qui saisit les armes"),
"blessing-of-liberty": GA("Bénédiction de liberté", 2, ["liberté", "entrave"], why="moins facile à entraver"),
"blood-salvation": GA("Salut du sang", 1, ["immunité", "zone"], why="tes propres sorts de zone t'épargnent"),
"book-ward": GA("Garde du livre", 1, ["livre", "feu", "acide", "eau"], why="un livre à l'abri du feu, de l'acide et de l'eau", cible_obj=["livre"]),
"bullet-shield": GA("Bouclier contre les balles", 1, ["garde", "balle"], 4, "4 ajouté à la défense contre les armes à poudre"),
"bullet-ward": GA("Garde de balles", 1, ["balle", "interception"], why="des balles d'adamantium qui interceptent les tirs"),
"calm-air": EP("Air apaisé", NINT, P, ["vent"], why="le vent apaisé"),
"cast-out": EP("Expulsion", DISP, 3, ["dissipation"], 18, "2d8 + 9 en moyenne et un effet dissipé"),
"caustic-safeguard": GA("Sauvegarde caustique", 1, ["objet", "acide"], why="qui touche l'objet est brûlé par l'acide", cible_obj=["objet"]),
"circle-of-clarity": GA("Cercle de clarté", P, ["illusion", "dissimulation"], why="illusions et cachettes peinent ici"),
"clay-skin": GA("Peau d'argile", 2, ["garde", "coup"], 5, "5 retranché à chaque coup"),
"cloak-of-shade": GA("Manteau d'ombre", 2, ["soleil", "chaleur"], why="à l'abri du soleil et de la chaleur"),
"cloak-of-winds": GA("Manteau de vents", 2, ["vent", "garde", "trait"], why="un écran de vent qui dévie les traits"),
"conditional-favor": EP("Faveur conditionnelle", V("ordre"), 2, ["sort", "condition", "renversement"], why="un bienfait qui se retourne si l'on rompt la condition", impact_sats=[(None, ["sort"])]),
"conjuration-foil": GA("Contre-téléportation", P, ["téléportation"], why="les téléportations alentour troublées"),
"corruption-resistance": GA("Résistance à la charge", 2, ["résistance", "charge"], why="les coups chargés de la charge choisie amoindris", options=TRIPF()),
"covetous-aura": EP("Aura de convoitise", V("flux"), P, ["sort", "vol", "bienfait"], why="les bienfaits lancés alentour te nourrissent"),
"crimson-confession": EP("Aveu cramoisi", V("ordre"), 1, ["marque", "rouge"], why="qui touche devient rouge", cible_obj=["objet"], cond=["déclencheur"]),
"darkvault": GA("Voûte d'ombre", P, ["ombre", "lumière"], why="l'ombre que la lumière ne perce plus"),
"death-from-below": GA("Mort d'en bas", 2, ["garde", "grand"], why="plus difficile à frapper pour les plus grands"),
"deflection": GA("Déviation", 1, ["coup", "renvoi"], why="les coups manqués reviennent sur leur auteur"),
"devil-snare": GA("Piège à fiélons", P, ["cercle", "extérieur", "piège"], why="un cercle invisible qui retient les êtres d'ailleurs"),
"diminished-detection": GA("Détection amoindrie", 1, ["divination", "zone"], why="les divinations de zone te ciblent mal"),
"disrupt-link": EP("Lien rompu", NREL, 3, ["lien", "compagnon"], why="le lien avec son compagnon tranché"),
"disrupt-silence": EP("Silence rompu", DISP, P, ["silence"], why="les silences magiques brisés"),
"draconic-suppression": EP("Suppression draconique", NINT, 3, ["souffle", "magie"], why="le dragon privé de son souffle et affaibli", cond=["DRAGON"]),
"dragon-turtle-shell": GA("Carapace de tortue-dragon", 1, ["carapace", "coup"], why="les crocs et griffes amoindris comme ceux d'un petit"),
"dream-shield": GA("Bouclier de rêve", 2, ["rêve", "esprit"], why="l'esprit gardé dans le sommeil"),
"dweomer-retaliation": EP("Riposte de la trame", V("flux"), 3, ["sort", "riposte", "vie"], why="un sort contré te rend de la vie et blesse son lanceur"),
"enchantment-foil": GA("Leurre contre l'enchantement", 1, ["enchantement", "leurre"], why="l'enchanteur croit réussir"),
"enshroud-thoughts": GA("Pensées voilées", 1, ["pensée", "mémoire"], why="pensées et souvenirs inviolables"),
"erase-impressions": EP("Effacer les empreintes", DISP, 1, ["empreinte", "effacement"], why="les traces psychiques d'un objet effacées", cible_obj=["objet"]),
"escaping-ward": GA("Garde de l'esquive", 1, ["esquive", "grand"], why="se glisser loin des grandes créatures"),
"expend": EP("Épuisement des dons", DISP, P, ["don", "épuisement"], why="leurs dons magiques à usage compté dépensés en vain"),
"fastidiousness": GA("Propreté", 1, ["propreté", "eau"], why="toi et ton équipement propres et secs"),
"firebelly": GA("Ventre de feu", 1, ["feu", "souffle", "résistance"], why="cracher le feu et ne plus le craindre"),
"firewalkers-meditation": GA("Méditation du marcheur de feu", 1, ["feu", "douleur", "résistance"], why="endurant au feu et à la douleur un jour durant"),
"fools-forbiddance": EP("Interdit des fous", V("ordre", True), P, ["confusion", "approche"], why="qui approche perd la raison"),
"forest-friend": EP("Ami de la forêt", REL, P, ["plante", "forêt"], why="les plantes aident au lieu d'entraver"),
"free-spirit": EP("Esprit libre", V("mouvement"), 2, ["liberté", "ivresse"], why="libre de tout mouvement, mais ivre"),
"gird-ally": GA("Allié ceint", P, ["invoqué", "garde"], why="tes êtres invoqués mieux gardés"),
"globe-of-tranquil-water": GA("Globe d'eau tranquille", P, ["pluie", "barrière"], why="aucune pluie, naturelle ou magique, n'y tombe"),
"guardian-monument-lesser": GA("Monument gardien", P, ["monument", "garde", "coup"], 2, "2 retranché à chaque coup pour les habitants alentour", cible_obj=["monument"], options=[
    O("Monument gardien"), O("Monument gardien suprême", src_idx="guardian-monument-greater", impact=(4, ["monument", "garde", "coup"], "4 retranché à chaque coup pour les habitants alentour"))]),
"guarding-knowledge": GA("Savoir protecteur", 1, ["savoir", "résistance"], 4, "ce que tu sais d'une créature te garde de ses pouvoirs"),
"harvest-season": EP("Saison des moissons", V("nature"), 1, ["plante", "croissance", "éclat"], why="une plante qui pousse d'un coup et éclate", cible_obj=["plante"]),
"healing-warmth": GA("Chaleur guérisseuse", 1, ["feu", "vie"], why="le feu absorbé rendu en soins"),
"hedging-weapons": GA("Armes gardiennes", 1, ["arme", "garde", "trait"], why="des armes flottantes qui te gardent puis frappent"),
"hex-ward": GA("Garde contre les maléfices", 2, ["maléfice", "résistance"], 4, "4 ajouté contre les maléfices"),
"holy-shield": GA("Bouclier sacré", 2, ["bouclier", "partage"], why="ton bouclier garde aussi un autre"),
"homeward-bound": EP("Retour au foyer", V("mouvement"), 3, ["plan", "retour"], why="renvoyée sur son plan d'origine"),
"hymn-of-peace": EP("Hymne de paix", NINT, P, ["paix", "agression"], why="nul ne peut frapper autrui"),
"impenetrable-veil": GA("Voile impénétrable", 2, ["dissimulation", "divination", "perception"], why="caché même aux sens aveugles et à la divination"),
"intellect-fortress-i": GA("Forteresse de l'intellect", P, ["émotion", "peur", "suspension"], why="émotions et peurs suspendues", options=[
    O("Forteresse de l'intellect I"), O("Forteresse de l'intellect II", src_idx="intellect-fortress-ii", impact=(P, ["émotion", "peur", "suspension", "esprit"], "et les assauts de l'esprit amoindris")),
    O("Forteresse de l'intellect III", src_idx="intellect-fortress-iii", impact=(P, ["émotion", "peur", "suspension", "esprit", "délivrance"], "et leurs restes effacés"))]),
"lament-of-summers-last-breath": GA("Dernier souffle de l'été", 2, ["chaleur", "froid"], why="un manteau d'air d'été qui brûle les êtres du froid"),
"life-bubble": GA("Bulle de vie", 2, ["climat", "air", "pression"], why="à l'abri des milieux hostiles", qty_cible=P),
"magnetic-field": GA("Champ magnétique", 1, ["métal", "attraction"], why="le métal attiré vers toi"),
"marks-of-forbiddance": EP("Marques d'interdit", NREL, 3, ["marque", "agression"], why="deux êtres qui peinent à s'attaquer", qty_cible=2),
"medusas-bane": GA("Fléau du regard", 1, ["regard", "renvoi"], why="insensible aux regards, qui se retournent"),
"mental-barrier-i": GA("Barrière mentale", 1, ["garde"], 4, "4 ajouté à la défense", options=[O(f"Barrière mentale {r}", src_idx=f"mental-barrier-{r.lower()}", impact=(n, ["garde"], d),
    **({"impact_sats": [(q, ["vital", "fractionné"])]} if q else {}))
    for r, n, q, d in [("I", 4, 0, "4 ajouté à la défense"), ("II", 6, 0, "6 ajouté à la défense"), ("III", 8, 0, "8 ajouté à la défense"),
                       ("IV", 8, 4, "8 ajouté ; une chance sur quatre de protéger les points vitaux"), ("V", 8, 2, "8 ajouté ; une chance sur deux de protéger les points vitaux")]]),
"miserable-pity": GA("Pitié misérable", 2, ["pitié"], why="trop pitoyable pour qu'on la frappe"),
"nereids-grace": GA("Grâce de la néréide", 1, ["grâce", "garde"], why="ta grâce te garde quand tu ne portes pas d'armure"),
"nine-lives": GA("Neuf vies", 1, ["chance", "évitement"], 9, "neuf fois échapper au malheur"),
"node-of-blasting": EP("Nœud explosif", V("ordre"), 1, ["piège", "esprit"], why="qui touche l'objet est frappé dans son esprit", cible_obj=["objet"]),
"numerological-resistance": GA("Résistance calculée", P, ["résistance", "énergie"], why="tes alliés plus résistants aux énergies"),
"oath-of-peace": GA("Serment de paix", 1, ["paix", "garde", "coup"], 5, "5 ajouté à la défense, 10 retranché aux coups hostiles, sans frapper"),
"obscure-poison": EP("Poison voilé", NVIS, 2, ["poison"], why="un poison plus difficile à déceler"),
"painful-revelation": EP("Révélation douloureuse", V("ordre"), P, ["illusion", "douleur"], why="qui perce l'illusion en souffre"),
"paladins-sacrifice": EP("Sacrifice du champion", REL, 2, ["sacrifice", "partage"], why="ce qui la frappe te frappe à sa place"),
"peace-bond": GA("Rune de paix", 2, ["rune", "paix"], why="tes propres sorts l'épargnent"),
"peacebond": EP("Lien de paix", V("ordre", True), 3, ["arme", "fourreau"], why="son arme scellée au fourreau", options=[
    O("Lien de paix"), O("Lien de paix suprême", src_idx="peacebond-greater", qty_cible=P, impact=(P, ["arme", "scellement"], "toutes leurs armes scellées"))]),
"planar-aegis": GA("Égide planaire", 1, ["énergie", "riposte"], why="une énergie qui te garde et riposte"),
"pressure-adaptation": GA("Adaptation à la pression", 2, ["pression"], why="habituée vite aux profondeurs"),
"primal-scream": EP("Cri primal", DISP, 1, ["enchantement", "paralysie", "délivrance"], why="délivrée d'un cri des charmes et paralysies"),
"protection-from-natural-attacks": GA("Protection contre les crocs", 2, ["garde", "croc"], 5, "5 retranché à chaque coup de croc, de griffe ou de corne"),
"protection-from-spores": GA("Protection contre les spores", 2, ["spore", "champignon"], why="le corps défendu contre les spores"),
"punishing-armor": GA("Armure punitive", 1, ["énergie", "riposte"], why="les coups qui assomment reviennent sur leur auteur"),
"quell-energy": EP("Énergie étouffée", NINT, 3, ["énergie"], why="privée de puiser dans une énergie"),
"radiation-ward": GA("Garde contre le rayonnement", 2, ["rayonnement"], why="à l'abri du rayonnement"),
"recentering-drone": EP("Bourdon apaisant", V("qualite"), P, ["apaisement", "mal"], why="leurs maux amoindris"),
"rite-of-bodily-purity": GA("Rite de pureté du corps", 2, ["maladie", "poison", "drogue"], 2, "2 ajouté contre maladies et poisons, un jour"),
"rite-of-centered-mind": GA("Rite de l'esprit centré", 2, ["esprit", "résistance"], 1, "1 ajouté contre les assauts de l'esprit, un jour"),
"rune-of-warding": EP("Rune de garde", V("ordre"), P, ["rune", "porte", "garde"], why="une rune visible qui garde un passage", cond=["PASSAGE"]),
"sacrificial-oath": EP("Serment sacrificiel", REL, 2, ["sacrifice", "partage", "durée"], why="tu prends ses blessures longtemps"),
"sanctify-armor": EP("Armure sanctifiée", INT, 1, ["armure", "garde"], 5, "jusqu'à 5 ajouté à la défense", cible_obj=["armure"]),
"sealed-life": GA("Vie scellée", 2, ["vie", "transfert"], why="nul ne lui prend ni ne lui donne sa force vitale", options=[
    O("Vie scellée"), O("Vie scellée suprême", src_idx="sealed-life-greater", impact=(P, ["vie", "transfert", "mort", "âme"], "et la mort et le vol d'âme sans prise"))]),
"seers-bane": GA("Fléau des devins", 2, ["divination", "riposte"], why="insaisissable, et qui la cherche en souffre"),
"selective-alarm": EP("Alarme sélective", VIS, P, ["alerte", "désigné"], why="une alarme pour certains seulement", cond=["INTRUS"]),
"shield-of-fortification": GA("Bouclier de fortification", 2, ["vital", "fractionné"], 4, "une chance sur quatre de protéger les points vitaux", options=[
    O("Bouclier de fortification"), O("Bouclier de fortification suprême", src_idx="shield-of-fortification-greater", impact=(2, ["vital", "fractionné"], "une chance sur deux de protéger les points vitaux"))]),
"shield-speech": EP("Parole gardée", NVIS, 2, ["parole", "secret"], why="parler sans être entendu des autres", options=[
    O("Parole gardée"), O("Parole gardée de groupe", src_idx="shield-speech-greater", qty_cible=P)]),
"shock-shield": GA("Bouclier électrique", 1, ["garde", "foudre"], why="un bouclier de force qui éclate en foudre"),
"siphon-magic": EP("Siphon de magie", V("flux"), 3, ["sort", "transfert"], why="un sort ôté d'un autre et pris pour toi"),
"soothe-construct": EP("Apaisement de l'artefact", V("qualite"), 3, ["artefact", "fureur"], why="un artefact animé moins enclin à la fureur", cond=["ARTEFACT"]),
"soul-vault": GA("Coffre de l'âme", 1, ["âme", "mort"], why="l'âme gardée après la mort"),
"source-severance": GA("Source tranchée", P, ["magie", "suspension", "source"], why="une seule source de magie suspendue"),
"spell-absorption": EP("Absorption de sort", V("flux"), 1, ["sort", "absorption"], why="l'énergie du sort contré rend un emplacement", impact_sats=[(None, ["sort"])], options=[
    O("Absorption de sort"), O("Absorption de sort suprême", src_idx="spell-absorption-greater", impact=(P, ["sort", "absorption", "puissance"], "même des sorts puissants"))]),
"spell-scourge": EP("Fouet des sorts", V("force", True), 3, ["fouet", "sort"], why="un fouet qui arrache les sorts de l'esprit"),
"spellcrash-lesser": EP("Fracas de sort", V("existence", True), 3, ["sort", "perte"], why="un sort préparé arraché", impact_sats=[(None, ["sort"])], options=[
    O(f"{lab}", src_idx=k, impact_sats=[(None, ["sort"]), (n, ["seuil", "niveau"])]) for lab, k, n in [("Fracas de sort mineur", "spellcrash-lesser", 3), ("Fracas de sort", "spellcrash", 5), ("Fracas de sort suprême", "spellcrash-greater", 7)]]),
"sphere-of-warding": GA("Sphère de garde", P, ["intangible", "possession"], why="les intangibles chassés des corps volés"),
"spite": EP("Dépit", V("ordre"), 1, ["sort", "riposte"], why="un sort de contact rendu à qui te frappe", impact_sats=[(None, ["sort"])]),
"stabilize-pressure": GA("Pression stabilisée", 2, ["pression", "instant"], why="ajustée d'un coup à la pression"),
"stave-off-corruption": GA("Corruption contenue", 2, ["corruption"], why="la corruption arrêtée dans sa course"),
"strand-of-the-tangled-knot": GA("Fil du nœud emmêlé", 1, ["coup", "écart"], why="le prochain coup s'égare"),
"stunning-barrier": GA("Barrière étourdissante", 1, ["garde", "étourdissement"], 1, "1 ajouté, qui frappe est étourdi", options=[
    O("Barrière étourdissante"), O("Barrière étourdissante suprême", src_idx="stunning-barrier-greater", impact=(2, ["garde", "étourdissement"], "2 ajouté, ceux qui frappent sont étourdis"))]),
"sunder-breaker": GA("Brise-briseur", 2, ["arme", "riposte"], why="l'arme qui brise son équipement est blessée"),
"suppress-charms-and-compulsions": EP("Charmes suspendus", DISP, P, ["charme", "contrainte"], why="charmes et contraintes suspendus"),
"suppress-primal-magic": EP("Magie sauvage apaisée", DISP, P, ["magie", "sauvage"], why="la magie sauvage du lieu apaisée"),
"surmount-affliction": EP("Mal surmonté", DISP, 1, ["mal", "suspension"], why="un mal suspendu un moment"),
"symbol-of-dispelling": SYMP("Symbole de dissipation", verb=DISP, impact=(P, ["sort", "dissipation"], "toute magie dissipée")),
"symbol-of-sealing": SYMP("Symbole de scellement", verb=SEP, impact=(P, ["mur", "force"], "un mur de force se dresse")),
"symbol-of-vulnerability": SYMP("Symbole de vulnérabilité", verb=NINT, impact=(P, ["faiblesse"], "chacun affaibli")),
"tactical-formation": GA("Formation", P, ["formation", "garde"], why="gardés tant qu'ils tiennent les rangs"),
"talisman-of-reprieve": GA("Talisman de répit", 1, ["plan", "charge"], why="protège d'une face du plan astral", cible_obj=["talisman"], options=[
    O("Talisman de répit lumineux", cond=["lumineux"]), O("Talisman de répit ténébreux", cond=["ténébreux"])]),
"thaumaturgic-circle": GA("Cercle thaumaturgique", P, ["cercle", "espèce"], why="un cercle de protection contre une espèce choisie"),
"theft-ward": GA("Garde contre le vol", 1, ["vol", "vigilance"], why="sentir la main qui prend ton bien"),
"thought-shield-i": GA("Bouclier de pensée", 1, ["esprit", "résistance"], 4, "4 ajouté contre les assauts de l'esprit", options=[
    O(f"Bouclier de pensée {r}", src_idx=f"thought-shield-{r.lower()}", impact=(n, ["esprit", "résistance"] + x, d)) for r, n, x, d in [
    ("I", 4, [], "4 ajouté contre les assauts de l'esprit"), ("II", 6, [], "6 ajouté"), ("III", 8, ["étourdissement"], "8 ajouté, qui lit tes pensées est étourdi"),
    ("IV", 8, ["étourdissement", "écrasement"], "et plus longtemps, l'écrasement psychique repoussé"), ("V", 8, ["étourdissement", "écrasement", "durée"], "et de façon durable")]]),
"tough-crowd": GA("Public difficile", P, ["enchantement", "illusion"], 4, "4 ajouté contre charmes et illusions"),
"tower-of-iron-will-i": GA("Tour de volonté de fer", P, ["esprit", "barrière"], why="une barrière contre la magie de l'esprit", options=[
    O(f"Tour de volonté de fer {r}", src_idx=f"tower-of-iron-will-{r.lower()}") for r in ["I", "II", "III", "IV", "V"]]),
"true-form": EP("Vraie forme", DISP, 3, ["métamorphose"], why="rendue à sa vraie forme"),
"unbreakable-construct": EP("Artefact infrangible", INT, 3, ["artefact", "solidité"], why="un artefact animé plus solide", cond=["ARTEFACT"]),
"undeath-ward": GA("Garde contre la non-vie", P, ["mort-vivant", "barrière"], why="une barrière qui repousse les morts-vivants"),
"unholy-ward": GA("Garde contre le sacré", 2, ["résistance", "bienveillant"], why="les coups de l'énergie bienveillante amoindris"),
"veil-of-heaven": GA("Voile des cieux", 1, ["garde", "extérieur"], why="protégé des êtres d'ailleurs hostiles", cond=["hostile"]),
"veil-of-positive-energy": GA("Voile de vie", 1, ["vie", "garde", "mort-vivant"], 2, "2 ajouté contre les morts-vivants"),
"vestment-of-the-champion": EP("Parure du champion", INT, 1, ["armure", "bouclier"], 5, "jusqu'à 5 ajouté à l'armure ou au bouclier", cible_obj=["armure"]),
"vigilant-rest": GA("Repos vigilant", 2, ["sommeil", "perception"], why="un dormeur qui perçoit encore"),
"wall-of-silver": GA("Mur d'argent", P, ["mur", "hostile"], why="un mur qui n'arrête que l'hostile", cond=["hostile"]),
"wall-of-suppression": GA("Mur de suppression", P, ["mur", "magie", "suspension"], why="un mur qui éteint la magie qui le traverse"),
"ward-of-the-season": GA("Garde de la saison", 2, ["saison"], why="la force d'une saison", options=[O(f"Garde {s}", cond=[c]) for s, c in [("du printemps", "printemps"), ("de l'été", "été"), ("de l'automne", "automne"), ("de l'hiver", "hiver")]]),
"ward-shield": EP("Bouclier de garde", INT, 1, ["bouclier", "magie", "zone"], why="un bouclier qui repousse la magie", cible_obj=["bouclier"]),
"ward-the-faithful": GA("Garde des fidèles", P, ["foi", "garde"], why="les fidèles de ta foi mieux gardés"),
"wave-shield": GA("Bouclier de vague", 1, ["eau", "garde", "feu"], why="l'eau amortit un coup ou une flamme"),
"winter-feathers": GA("Plumes d'hiver", 2, ["plume", "froid"], why="un oiseau gardé du froid un jour", cond=["bête"]),
"with-the-wind": GA("Avec le vent", 2, ["vent", "ancrage"], why="le vent ne l'emporte pas"),
"woodland-rune": EP("Rune des bois", V("ordre"), P, ["rune", "lenteur"], why="une rune qui ralentit qui passe", cond=["PASSAGE"]),
"word-of-resolve": GA("Parole de résolution", 2, ["charme", "peur", "délivrance"], why="secouer un charme ou une peur"),
"wreath-of-blades": GA("Couronne de lames", 1, ["dague", "garde"], why="quatre dagues de mithral qui tournent et frappent"),
"waterproof": GA("Imperméable", 2, ["eau"], why="l'eau glisse sur elle"),
}
FICHES.update(NEWPF_ABJ)
PFV("Abjuration")
ADDPF("alarm", O("Alarme de sortie", src_idx="escape-alarm", cond=["DÉPART"]), O("Alarme contre l'invisible", src_idx="invisibility-alarm", cond=["invisible"]))
ADDPF("nondetection", O("Antidétection mineure", src_idx="nondetection-lesser", impact=(P, ["divination", "zone"], "insaisissable aux divinations de zone")),
    O("Antidétection partagée", src_idx="nondetection-communal", qty_cible=P), O("Atelier secret", src_idx="nexs-secret-workshop", cible=P))
ADDPF("freedom-of-movement", O("Nage libre", src_idx="free-swim", cond=["eau"]))
ADDPF("shield-other", O("Protection du compagnon", src_idx="shield-companion-aa", cond=["compagnon"]), O("Œil vigilant", src_idx="watchful-eye", cond=["vue"]))
for k, ck in [("endure-elements", "endure-elements-communal"), ("protection-from-arrows", "protection-from-arrows-communal"), ("resist-energy", "resist-energy-communal"),
              ("protection-from-energy", "protection-from-energy-communal"), ("stoneskin", "stoneskin-communal"), ("mind-blank", "mind-blank-communal")]:
    ADDPF(k, O(f"{FICHES[k]['fr']} partagée", src_idx=ck, qty_cible=P))
ADDPF("spell-immunity", O("Immunité contre les sorts partagée", src_idx="spell-immunity-communal", qty_cible=P,
        impact=(1, ["immunité", "sort"], "un sort désigné sans effet"), impact_sats=[(4, ["seuil", "niveau"])]),
    O("Immunité contre les sorts suprême partagée", src_idx="spell-immunity-greater-communal", qty_cible=P,
        impact=(3, ["immunité", "sort"], "trois sorts désignés sans effet"), impact_sats=[(8, ["seuil", "niveau"])]))
ADDPF("protection-from-evil-and-good", *[O(f"{lab} — partagée", src_idx=k, cond=[c], qty_cible=P) for lab, k, c in
    [("Contre l'hostile", "protection-from-evil-communal", "hostile"), ("Contre le lumineux", "protection-from-law-communal", "lumineux"), ("Contre le ténébreux", "protection-from-chaos-communal", "ténébreux")]])

# --- Pathfinder 1, lot 5 : Nécromancie ---
PF1_RELECTURE.update({
"hex-vulnerability": "réutilise un « maléfice » de sorcière : pure mécanique de classe",
"hunters-howl": "repose sur les « ennemis jurés » du rôdeur : pure mécanique de classe",
"ki-leech": "remplit la « réserve de ki » sur un coup critique : pure mécanique de classe",
"oracles-burden": "transmet la « malédiction d'oracle » : pure mécanique de classe",
"mathematical-curse": "repose sur la « Voie des Nombres » de Golarion et sur des bonus de calcul",
"daemon-ward": "protège des daémons d'Abaddon, propres à la cosmologie de Golarion",
})
NE, NQ, ID = V("existence", True), V("qualite", True), V("identite")
NC = lambda fr, cible, words, v=None, why="", **kw: EP(fr, NE, cible, words, v, why, **kw)
CU = lambda fr, cible, words, v=None, why="", **kw: EP(fr, NQ, cible, words, v, why, **kw)
NEWPF_NEC = {
"absorb-toxicity": EP("Absorption de toxicité", V("flux"), 1, ["poison", "maladie", "contagion"], why="tu absorbes un mal puis le transmets"),
"accursed-glare": CU("Regard maudit", 3, ["regard", "malédiction"], why="une malédiction jetée d'un regard"),
"advanced-scurvy": CU("Scorbut avancé", 3, ["maladie", "scorbut"], why="un scorbut déjà avancé"),
"aggravate-affliction": CU("Mal aggravé", 3, ["mal", "aggravation"], why="ses maux frappent de nouveau"),
"akashic-form": EP("Forme akashique", ID, 1, ["corps", "mémoire", "retour"], why="ton corps copié dans la mémoire du monde, et restauré"),
"aura-of-doom": EP("Aura funeste", NINT, P, ["peur"], why="secoués à ton approche"),
"banshee-blast": NC("Souffle de la banshie", P, ["cri", "panique"], 23, "1d4 par niveau, puis panique", aoe={"type": "cone", "size": 30}),
"barrow-haze": EP("Brume des tertres", NVIS, P, ["brume"], why="une brume qui aveugle les autres"),
"bed-of-iron": GA("Lit de fer", 2, ["sommeil", "armure"], why="dormir en armure sans peine"),
"besmaras-grasping-depths": NC("Profondeurs agrippantes", P, ["mort", "eau", "noyade"], why="les morts sans repos tirent vers le fond"),
"black-mark": CU("Marque noire", 3, ["eau", "peur", "malédiction"], why="peur de l'eau, et les bêtes marines contre elle"),
"black-spot": CU("Tache noire", 3, ["malédiction", "marin"], why="la malédiction redoutée des gens de mer"),
"bleed": NC("Saignement", 3, ["sang", "agonie"], why="une créature stabilisée se remet à mourir", cond=["mourant"]),
"bloatbomb": NC("Bombe de chair", 3, ["cadavre", "piège", "explosion"], why="un faible tué, son cadavre piégé"),
"blood-boil": NC("Sang bouillant", 3, ["sang", "constitution", "fatigue"], why="le sang qui bout, le corps épuisé"),
"blood-in-the-water": EP("Sang dans l'eau", INT, P, ["sang", "frénésie"], why="la frénésie du sang attisée"),
"bloodbath": NC("Bain de sang", P, ["sang"], why="toi et tes ennemis saignez"),
"bloodsworn-retribution": EP("Châtiment juré par le sang", INT, 1, ["serment", "sang"], why="ton sang versé pour tenir un serment"),
"bloody-arrows": EP("Flèches sanglantes", INT, 1, ["trait", "sang"], why="des traits qui font saigner", cible_obj=["trait"]),
"bloody-claws": EP("Griffes sanglantes", INT, 2, ["griffe", "sang"], why="des griffes qui font saigner"),
"bone-fists": EP("Poings d'os", INT, P, ["os", "garde", "croc"], 1, "des pointes d'os, 1 ajouté à la défense"),
"boneshaker": EP("Secoue-os", ID, 3, ["os", "contrôle"], why="son squelette commandé un instant"),
"boneshatter": NC("Brise-os", 3, ["os", "fracture"], why="ses os fêlés et éclatés"),
"brow-gasher": EP("Entaille au front", INT, 1, ["arme", "sang", "front"], why="une plaie au front qui aveugle de sang", cible_obj=["arme"]),
"calamitous-flailing": CU("Gesticulation calamiteuse", 3, ["coup", "écart", "fractionné"], 5, why="ses coups s'égarent souvent"),
"calm-spirit": EP("Esprit apaisé", V("qualite"), 3, ["esprit", "hantise"], why="une hantise ou un esprit retenu", cond=["MORTVIVANT"]),
"catatonia": EP("Catatonie", NE, 2, ["mort", "apparence"], why="d'apparence morte"),
"companion-life-link": EP("Lien vital du compagnon", REL, 2, ["lien", "blessure"], why="tu sens ses blessures et l'appelles", cond=["compagnon"]),
"conditional-curse": CU("Malédiction conditionnelle", 3, ["malédiction", "condition"], why="ne se lève qu'en remplissant la condition"),
"corpse-lanterns": EP("Lanternes de cadavre", EXI, P, ["lumière", "nécrose"], why="des lueurs maladives"),
"crafters-nightmare": EP("Cauchemar de l'artisan", EXI, P, ["esprit", "trouble"], why="un esprit frappeur qui gâche l'ouvrage et les sorts"),
"curse-item": CU("Objet maudit", 1, ["objet", "défaut"], why="un objet qui faillit", cible_obj=["objet"]),
"curse-of-befouled-fortune": CU("Chance souillée", 3, ["chance", "malédiction"], why="la chance ne la sert plus"),
"curse-of-unexpected-death": CU("Malédiction de la mort subite", 3, ["mort", "malédiction", "hasard"], why="la mort peut venir à tout instant"),
"cursed-earth": CU("Terre maudite", P, ["terre", "mort", "maladie"], why="plantes mortes, vivants malades, morts relevés"),
"cursed-treasure": CU("Trésor maudit", 1, ["objet", "malédiction"], why="le prochain qui touche est maudit", cible_obj=["objet"]),
"daywalker": EP("Marcheur du jour", ID, 2, ["mort-vivant", "vivant", "apparence"], why="un mort-vivant à l'allure vivante", cond=["MORTVIVANT"]),
"deadly-juggernaut": EP("Colosse mortel", INT, 1, ["force", "mort"], why="plus fort à chaque mort donnée"),
"death-candle": NC("Chandelle de mort", 3, ["vie", "feu", "élémentaire"], why="un élémentaire de feu hurlant tiré de sa vie"),
"death-clutch": NC("Étreinte de mort", 3, ["cœur", "mort"], why="le cœur arraché"),
"death-knell-aura": EP("Aura de glas", V("flux"), P, ["âme", "mort", "vie"], why="nourrie des âmes qui meurent alentour", options=[
    O("Aura de glas"), O("Aura de glas suprême", src_idx="death-knell-aura-greater", impact=(P, ["âme", "mort", "vie", "agonie"], "et les mourants partent plus vite"))]),
"deathwine": EP("Vin de mort", NE, 1, ["potion", "nécrose"], why="une potion changée en flaque de nécrose", cible_obj=["potion"]),
"decollate": EP("Décollation", ID, 2, ["tête"], why="la tête ôtée sans dommage"),
"decompose-corpse": NC("Décomposition", 1, ["cadavre", "os"], why="un cadavre réduit à un squelette propre", cible_obj=["cadavre"]),
"defending-bone": GA("Os défenseur", 1, ["os", "garde"], why="un os flottant pare les coups"),
"defoliate": NC("Défoliation", P, ["plante", "nécrose"], why="une boule de nécrose qui tue les plantes"),
"depilate": CU("Dépilation", 3, ["poil", "laideur"], why="chauve et sans charme une semaine"),
"divine-transfer": EP("Transfert divin", REL, 2, ["vie", "partage", "garde"], why="ta vie donnée, et la garde contre l'hostile"),
"dress-corpse": EP("Toilette du mort", ID, 1, ["cadavre", "indice"], why="les indices d'un cadavre maquillés", cible_obj=["cadavre"]),
"empathy-conduit": EP("Conduit d'empathie", REL, 2, ["lien", "compagnon", "sort"], why="toucher l'un à travers l'autre", cond=["compagnon"]),
"entrap-spirit": EP("Esprit piégé", V("ordre", True), 3, ["esprit", "miroir"], why="un esprit enfermé dans un miroir", cond=["MORTVIVANT"]),
"epidemic": CU("Épidémie", 3, ["maladie", "contagion"], why="une maladie qui se répand vite"),
"explosion-of-rot": NC("Explosion de pourriture", P, ["pourriture", "chancellement"], P, "une explosion de pourriture"),
"familiar-melding": EP("Fusion avec le familier", ID, 2, ["compagnon", "possession"], why="posséder ton familier", cond=["compagnon"]),
"feast-on-fear": EP("Festin de peur", V("flux"), P, ["peur", "panique", "vie"], why="leur panique te nourrit"),
"fester": CU("Purulence", 3, ["soins", "rejet"], why="les soins ont peine à prendre", options=[O("Purulence"), O("Purulence de groupe", src_idx="fester-mass", qty_cible=P)]),
"flesh-puppet": EP("Pantin de chair", REL, 3, ["mort-vivant", "déguisement", "contrôle"], why="un zombie sous allure humaine", cond=["MORTVIVANT"],
    options=[O("Pantin de chair"), O("Horde de pantins", src_idx="flesh-puppet-horde", qty_cible=P)]),
"flesh-wall": EP("Mur de chair", EXI, P, ["mur", "mort-vivant"], why="un mur de zombies"),
"frigid-souls": EP("Âmes glacées", DISP, P, ["froid", "garde"], why="les protections contre le froid défaites"),
"fungal-infestation": CU("Infestation fongique", 3, ["champignon", "sang"], why="chaque coup la fait saigner"),
"garrulous-grin": CU("Sourire bavard", 3, ["doute"], why="le doute semé en elle"),
"gebs-hammer": NC("Marteau de chair", 3, ["mort-vivant", "projectile"], why="les restes des morts-vivants lancés d'un bloc"),
"grasping-corpse": EP("Cadavre agrippeur", EXI, 1, ["cadavre", "saisie"], why="un cadavre qui agrippe ou fait tomber", cible_obj=["cadavre"]),
"grave-words": EP("Paroles d'outre-tombe", REL, 1, ["cadavre", "parole"], why="un cadavre qui babille", cible_obj=["cadavre"]),
"grim-stalker": EP("Traqueur sinistre", EXI, 3, ["sommeil", "tourment"], why="une créature qui trouble son sommeil"),
"haunting-choir": NC("Chœur hanté", P, ["esprit", "douleur", "chant"], why="des esprits chantent la douleur"),
"healing-thief": EP("Voleur de soins", V("flux"), 3, ["soins", "vol", "fractionné"], 2, why="la moitié de ses soins pour toi"),
"hibernate": EP("Hibernation", NINT, 2, ["catalepsie"], why="plongée dans un sommeil de mort"),
"howling-agony": NC("Agonie hurlante", 3, ["douleur", "cri"], why="la douleur la fait hurler"),
"hydrophobia": CU("Hydrophobie", 3, ["eau", "peur"], why="terrifiée par l'eau", qty_cible=P),
"interrogation": NC("Interrogatoire", 3, ["douleur", "question"], why="répondre ou souffrir", options=[
    O("Interrogatoire"), O("Interrogatoire suprême", src_idx="interrogation-greater", impact=(P, ["douleur", "question", "durée"], "plus de questions, plus de douleur"))]),
"itching-curse": CU("Malédiction de démangeaison", 3, ["démangeaison"], 1, "1 retranché à tout ce qu'elle tente"),
"khains-army": EP("Armée de goules", EXI, P, ["mort-vivant", "goule"], why="une escouade de goules chargées de nécrose"),
"languid-venom": EP("Venin langoureux", V("ordre"), 2, ["poison", "retard"], why="un poison retardé et caché", options=[
    O("Venin langoureux"), O("Venin conditionnel", src_idx="contingent-venom", cond=["déclencheur"])]),
"lash-of-the-astradaemon": EP("Griffes avaleuses d'âmes", INT, 1, ["griffe", "nécrose", "vie"], why="des griffes qui volent la vie durable"),
"life-blast": EP("Souffle de sève", V("flux"), P, ["plante", "vie"], why="la vie des plantes lancée en souffle"),
"life-pact": EP("Pacte de vie", REL, P, ["vie", "partage"], why="les liés donnent leur vie au mourant"),
"lipstitch": CU("Lèvres cousues", 3, ["lèvre", "silence"], why="les lèvres cousues"),
"litany-of-admonition": EP("Litanie de remontrance", NINT, 3, ["faute", "chancellement"], why="ses fautes la font chanceler"),
"litany-of-weakness": EP("Litanie de faiblesse", NINT, 3, ["fatigue"], why="fatiguée un instant"),
"mark-of-spite": NC("Marque de dépit", 3, ["marque", "partage"], why="tes blessures frappent la marquée"),
"masochistic-shadow": NC("Ombre masochiste", 3, ["ombre", "vie"], why="son ombre affamée de sa vie"),
"massacre": NC("Massacre", P, ["mort"], why="une ligne de mort", aoe={"type": "line", "size": 60}),
"mind-over-matter": EP("L'esprit sur la matière", V("qualite"), 1, ["faculté", "transfert"], why="un mal déplacé d'une faculté à l'autre"),
"mischievous-shadow": CU("Ombre espiègle", 3, ["ombre", "trouble"], why="son ombre contrarie ses gestes"),
"nap-stack": EP("Sieste empilée", INT, 2, ["sommeil", "repos"], why="deux heures valent une nuit"),
"natures-ravages": NC("Ravages de la nature", 1, ["cadavre", "pourriture"], why="un cadavre vieilli de jours", cible_obj=["cadavre"], options=[
    O("Ravages de la nature"), O("Ravages de la nature suprêmes", src_idx="natures-ravages-greater", impact=(P, ["cadavre", "pourriture", "années"], "un cadavre vieilli d'années"))]),
"necromantic-burden": CU("Fardeau nécromantique", 3, ["mort-vivant", "contrôle"], why="morts-vivants plus durs à tenir", cond=["MORTVIVANT"]),
"necrostasis": EP("Nécrostase", NINT, 3, ["mort-vivant", "chancellement"], why="un mort-vivant qui chancelle", cond=["MORTVIVANT"]),
"oath-of-justice": EP("Serment de justice", V("ordre"), 2, ["serment", "lien"], why="un serment scellé entre deux êtres", qty_cible=2),
"object-possession-lesser": EP("Possession d'objet", ID, 1, ["objet", "âme", "animation"], why="ton âme anime un objet", cible_obj=["objet"], options=[
    O("Possession d'objet mineure"), O("Possession d'objet", src_idx="object-possession", impact=(P, ["objet", "âme", "animation", "grand"], "un objet plus grand")),
    O("Possession d'objet suprême", src_idx="object-possession-greater", impact=(P, ["objet", "âme", "animation", "artefact"], "un objet puissant, ou un artefact animé")),
    O("Possession d'un objet", src_idx="possess-object", impact=(P, ["objet", "âme", "animation", "durée"], "un objet animé longuement"))]),
"old-salts-curse": CU("Malédiction du vieux loup de mer", 3, ["malédiction", "nausée", "eau"], why="malade à jamais, pire au large"),
"orb-of-the-void": NC("Orbe du néant", 3, ["sphère", "vie"], why="une sphère qui vole la vie durable"),
"outbreak": CU("Flambée", P, ["maladie", "contagion"], why="les malades deviennent très contagieux"),
"overwhelming-poison": EP("Poison écrasant", INT, 1, ["poison"], why="un poison plus dur à combattre", cible_obj=["poison"]),
"parasitic-soul": EP("Âme parasite", ID, 3, ["âme", "corps"], why="une âme captive jetée dans un nouveau corps"),
"pernicious-poison": CU("Poison pernicieux", 3, ["poison", "faiblesse"], 4, "4 retranché contre le poison"),
"persuasive-goad": NC("Aiguillon persuasif", 3, ["douleur", "intimidation"], 4, "1d6 qui assomment, et elle plie plus volontiers"),
"phantom-blood": EP("Sang fantôme", INT, 1, ["vie", "constitution"], why="de la vie quand le corps défaille"),
"phantom-limb": EP("Membre fantôme", EXI, 2, ["membre", "esprit"], why="un membre de pensée remplace le perdu"),
"plague-bearer": CU("Porteur de peste", 3, ["maladie", "contagion"], why="porteuse de nombreuses maladies"),
"plague-carrier": CU("Porteur de fièvre", 3, ["maladie", "coup"], why="ses coups portent la fièvre"),
"plague-storm": CU("Tempête de peste", P, ["maladie", "nuage"], why="un nuage qui infecte"),
"positive-pulse": EP("Pulsation de vie", V("flux"), P, ["vie", "mort-vivant"], 4, "blesse les morts-vivants, fortifie les vivants", options=[
    O("Pulsation de vie"), O("Pulsation de vie suprême", src_idx="positive-pulse-greater", impact=(14, ["vie", "mort-vivant"], "une vaste pulsation"))]),
"possession": EP("Possession d'un corps", ID, 3, ["âme", "corps", "contrôle"], why="ton âme dans son corps", options=[
    O("Possession"), O("Possession suprême", src_idx="possession-greater", impact=(P, ["âme", "corps", "contrôle", "disparition"], "et ton corps disparaît")),
    O("Possession d'observation", src_idx="riding-possession", impact=(P, ["âme", "corps", "observation"], "voir par ses yeux sans la mener")),
    O("Possession à vue", src_idx="marionette-possession", impact=(P, ["âme", "corps", "contrôle", "vue"], "tant qu'elle reste en vue"))]),
"possession-trap": GA("Piège à possession", 1, ["possession", "piège"], why="qui tente de te posséder est pris"),
"pox-pustules": CU("Pustules", 3, ["pustule", "nausée"], 4, "nauséeuse, 4 retranché à l'adresse"),
"preserve": GA("Conservation", 1, ["pourriture"], why="rien ne pourrit ni ne se gâte", cible_obj=["objet"]),
"psychic-crush-i": NC("Écrasement psychique", 3, ["esprit", "mort"], why="l'esprit écrasé jusqu'à l'agonie", options=[
    O(f"Écrasement psychique {r}", src_idx=f"psychic-crush-{r.lower()}", impact=(P, ["esprit", "mort"], f"l'esprit écrasé, ou {d} en moyenne")) for r, d in [("I", 19), ("II", 28), ("III", 37), ("IV", 46), ("V", 55)]]),
"purge-spirit": NC("Purge d'esprit", 3, ["esprit", "chancellement"], 32, "1d6 par niveau, puis chancelant", cond=["MORTVIVANT"]),
"ray-of-sickening": CU("Rayon d'écœurement", 3, ["nausée"], why="un rayon qui écœure"),
"reapers-coterie": EP("Confrérie du faucheur", INT, 1, ["arme", "mort"], why="plus meurtrière à chaque ennemi abattu", cible_obj=["arme"]),
"red-hand-of-the-killer": CU("Main rouge du tueur", P, ["meurtre", "marque"], why="la main du meurtrier tachée de rouge"),
"repair-undead": EP("Réparation de mort-vivant", V("existence"), 2, ["nécrose", "mort-vivant"], 7, "1d8 + 3 en moyenne", cond=["MORTVIVANT"], options=[
    O("Réparation de mort-vivant"), O("Réparation de morts-vivants de groupe", src_idx="repair-undead-mass", qty_cible=9)]),
"rest-eternal": EP("Repos éternel", V("ordre"), 1, ["mort", "sceau"], why="nul ne pourra la ramener", cond=["mort"]),
"restful-sleep": EP("Sommeil réparateur", V("existence"), P, ["sommeil", "vie"], why="le sommeil rend plus de vie"),
"restore-corpse": EP("Corps restauré", V("existence"), 1, ["cadavre", "chair"], why="un squelette retrouve sa chair", cible_obj=["cadavre"]),
"retribution": CU("Rétribution", 3, ["vengeance", "faiblesse"], why="qui t'a frappé en pâtit"),
"retributive-reparations": CU("Réparations rétributives", 1, ["objet", "fatigue"], why="qui prend l'objet s'épuise", cible_obj=["objet"]),
"rotting-alliance": NC("Alliance pourrissante", P, ["pourriture", "proximité"], why="se flétrir à rester ensemble"),
"sadomasochism": EP("Sadomasochisme", REL, 1, ["douleur", "démoralisation"], why="plus blessé, mais tes ennemis perdent cœur"),
"sands-of-time": NC("Sables du temps", 3, ["âge"], why="vieillie pour un temps"),
"scarify": EP("Scarification", V("qualite"), 2, ["cicatrice", "blessure"], why="des blessures changées en cicatrices"),
"scourge-of-the-horsemen": NC("Fléau des cavaliers", P, ["âme", "vie", "acide"], why="l'âme déchirée et la chair rongée"),
"sculpt-corpse": EP("Corps sculpté", ID, 1, ["cadavre", "apparence"], why="un cadavre à l'allure d'un autre", cible_obj=["cadavre"]),
"sessile-spirit": EP("Esprit assoupi", NINT, 3, ["esprit", "sommeil"], why="un esprit mis en sommeil"),
"shadow-projection": EP("Projection d'ombre", ID, 1, ["ombre", "forme"], why="devenir une ombre"),
"share-skin": EP("Peau partagée", ID, 3, ["bête", "possession"], why="posséder un animal", cond=["bête"], options=[
    O("Peau partagée"), O("Peau partagée suprême", src_idx="share-skin-greater", cond=[])]),
"shared-sacrifice": EP("Sacrifice partagé", REL, 2, ["lien", "douleur", "partage"], why="ta douleur passe par elle"),
"sharesister": EP("Sœur de partage", REL, 2, ["vie", "partage", "don"], why="ta vie durable donnée pour la fortifier"),
"siphon-might": EP("Siphon de force", V("flux"), 3, ["force", "transfert"], why="sa force passe à un autre"),
"skeleton-crew": EP("Équipage squelette", EXI, P, ["cadavre", "squelette", "équipage"], why="des cadavres changés en équipage obéissant"),
"skin-tag": CU("Marque de peau", 1, ["nourriture", "lien"], why="qui mange te devient familier", cible_obj=["nourriture"]),
"skinsend": EP("Peau envoyée", ID, 1, ["peau", "possession"], why="ta propre peau envoyée comme un être"),
"soulswitch": EP("Échange d'âme", ID, 2, ["âme", "compagnon", "échange"], why="ton âme et celle du familier échangées", cond=["compagnon"]),
"spawn-ward": GA("Garde contre les rejetons", 2, ["vie", "sang", "mort-vivant"], why="ni vidée, ni saignée, ni changée en rejeton"),
"speak-with-haunt": EP("Parole à la hantise", REL, 1, ["hantise", "question"], why="la hantise répond"),
"speak-with-soul": EP("Parole à l'âme", REL, 1, ["âme", "parole"], why="longue conversation avec une âme"),
"spellcurse": NC("Malédiction des sorts", 3, ["sort", "douleur"], 4, "1d6 par sort qui l'affecte"),
"stricken-heart": NC("Cœur frappé", 3, ["cœur", "chancellement"], 7, "2d6 en moyenne, puis chancelante"),
"suffocation": NC("Suffocation", 3, ["souffle", "mort"], why="l'air volé jusqu'à la mort", options=[O("Suffocation"), O("Suffocation de groupe", src_idx="suffocation-mass", qty_cible=P)]),
"summoner-conduit": EP("Conduit de l'invocateur", REL, 3, ["invoqué", "partage"], why="les blessures de son invoqué la frappent"),
"sweat-poison": EP("Sueur empoisonnée", EXI, 1, ["poison", "peau"], why="ta peau sécrète un poison"),
"symbol-of-exsanguination": SYMP("Symbole d'exsanguination", verb=NE, impact=(P, ["sang"], "chacun saigne")),
"temporary-resurrection": EP("Résurrection temporaire", V("existence"), 1, ["mort", "retour", "jour"], why="ramenée à la vie un jour", cond=["mort"]),
"torpid-reanimation": EP("Réanimation différée", EXI, 1, ["cadavre", "déclencheur"], why="les morts se lèvent au signal", cond=["déclencheur"]),
"touch-of-blindness": CU("Toucher aveuglant", 3, ["cécité"], why="les yeux couverts de ténèbres"),
"touch-of-bloodletting": NC("Toucher de saignée", 3, ["sang", "blessure"], why="ses plaies saignent à flots"),
"toxic-gift": EP("Don toxique", V("flux"), 3, ["poison", "transfert"], why="le poison en toi passe en elle"),
"toxic-rupture": NC("Rupture toxique", 3, ["poison"], why="son propre poison se retourne"),
"umbral-strike": NC("Frappe ombreuse", 3, ["froid", "nécrose"], why="un trait d'énergie sombre"),
"undeath-inversion": EP("Inversion de non-vie", ID, 3, ["mort-vivant", "vie", "nécrose"], why="la nécrose la blesse, la vie la soigne", cond=["MORTVIVANT"]),
"undines-curse": CU("Malédiction d'Ondine", 3, ["souffle"], why="ne respire plus d'elle-même"),
"unliving-rage": EP("Rage du non-vivant", INT, 2, ["rage", "mort-vivant"], why="la rage d'un mort-vivant", cond=["MORTVIVANT"]),
"unsettling-presence": CU("Présence troublante", P, ["méfiance", "répulsion"], why="méfiants et repoussés"),
"unshakable-chill": CU("Froid tenace", 3, ["froid"], why="saisie d'un froid profond"),
"unwilling-shield": EP("Bouclier malgré lui", REL, 3, ["blessure", "partage"], why="elle partage les blessures que tu reçois"),
"vampiric-hunger": EP("Faim vampirique", ID, 2, ["croc", "sang", "faim"], why="les crocs et la faim d'un vampire"),
"vampiric-shadow-shield": GA("Bouclier d'ombre vampirique", 1, ["nécrose", "riposte", "vie"], why="qui frappe est rongé et te nourrit"),
"venomous-bolt": EP("Trait venimeux", INT, 1, ["trait", "poison"], why="un trait qui empoisonne", cible_obj=["trait"]),
"virulent-miasma": EP("Miasme virulent", NVIS, P, ["brume", "maladie"], why="une brume qui rend malade"),
"wall-of-blindness-deafness": EP("Mur de cécité et de surdité", NVIS, P, ["mur", "sens"], why="qui traverse perd un sens", options=[
    O("Mur de cécité", impact=(P, ["mur", "cécité"], "qui traverse est aveuglé")), O("Mur de surdité", impact=(P, ["mur", "surdité"], "qui traverse est assourdi"))]),
"wall-of-bone": EP("Mur d'os", EXI, P, ["mur", "os", "saisie"], why="un mur d'os qui blesse et agrippe"),
"withdraw-affliction": EP("Mal retiré", V("flux"), 3, ["mal", "transfert"], why="un mal retiré et donné à un autre"),
"wither-limb": NC("Membre flétri", 3, ["membre"], why="un membre rendu inutile"),
}
FICHES.update(NEWPF_NEC)
PFV("Necromancy")
ADDPF("animate-dead", O("Animation des morts mineure", src_idx="animate-dead-lesser", qty_cible=1))
ADDPF("astral-projection", O("Projection astrale mineure", src_idx="astral-projection-lesser", qty_cible=1))
ADDPF("false-life", O("Simulacre de vie suprême", src_idx="false-life-greater"))
ADDPF("bestow-curse", O("Malédiction majeure", src_idx="curse-major"), O("Malédiction suprême", src_idx="bestow-curse-greater"))
ADDPF("contagion", O("Contagion suprême", src_idx="contagion-greater"))

# --- Pathfinder 1, lot 6 : Évocation ---
PF1_RELECTURE.update({
"arbitrament": "frappe selon la distance à la neutralité d'alignement, sans équivalent dans nos charges : à revoir",
"ardors-onslaught": "vise les créatures neutres d'alignement, sans équivalent dans nos charges : à revoir",
"arcane-concordance": "accorde des « dons de métamagie » : pure mécanique de jeu",
"borrow-fortune": "fait relancer un jet de dé : pure mécanique de jeu",
"brilliant-inspiration": "fait garder le meilleur de deux jets : pure mécanique de jeu",
"saving-finale": "« final » de barde qui fait relancer un jet : pure mécanique de classe",
"deadly-finale": "« final » de barde : pure mécanique de classe",
"screech": "provoque des « attaques d'opportunité » : pure mécanique de jeu",
"caging-bomb-admixture": "modifie les « bombes » de l'alchimiste : pure mécanique de classe",
"lightning-lash-bomb-admixture": "modifie les « bombes » de l'alchimiste : pure mécanique de classe",
"contingent-action": "déclenche une « action préparée » : pure mécanique de jeu",
"fire-of-entanglement": "s'ajoute au « châtiment » du paladin : pure mécanique de classe",
"fire-of-judgment": "s'ajoute au « châtiment » du paladin : pure mécanique de classe",
"fire-of-vengeance": "s'ajoute au « châtiment » du paladin : pure mécanique de classe",
"smite-abomination": "imite le « châtiment » du paladin : pure mécanique de classe",
"judgment-light": "s'ajoute au « jugement » de l'inquisiteur : pure mécanique de classe",
"imbue-hex": "transmet un « maléfice » de sorcière : pure mécanique de classe",
"imbue-with-elemental-might": "transmet l'« assaut élémentaire » d'un domaine : pure mécanique de classe",
"talismanic-implement": "investit un sort dans un « instrument » d'occultiste : pure mécanique de classe",
"bestow-planar-infusion-i": "accorde une « infusion planaire », propre à la cosmologie de Golarion",
"bestow-planar-infusion-ii": "accorde une « infusion planaire », propre à la cosmologie de Golarion",
"bestow-planar-infusion-iii": "accorde une « infusion planaire », propre à la cosmologie de Golarion",
})
PF1_MEME.update({"profane-nimbus": "sacred-nimbus", "unholy-sword": "holy-sword"})
FO, NF = V("force"), V("force", True)
EV = lambda fr, cible, words, v=None, why="", **kw: EP(fr, NF, cible, words, v, why, **kw)
NEWPF_EVO = {
"admonishing-ray": EV("Rayon de remontrance", 3, ["force", "assommer"], 9, "des rayons qui assomment sans tuer"),
"aggressive-thundercloud": EV("Nuée d'orage agressive", P, ["nuage", "foudre"], 11, "3d6 en moyenne", options=[
    O("Nuée d'orage agressive"), O("Nuée d'orage agressive suprême", src_idx="aggressive-thundercloud-greater", impact=(21, ["nuage", "foudre"], "6d6 en moyenne"))]),
"agonize": EV("Supplice", 3, ["douleur", "extérieur", "obéissance"], why="la douleur plie un être d'ailleurs", cond=["EXTERIEUR"]),
"air-geyser": EV("Geyser d'air", 3, ["air", "projection"], 7, "2d6 en moyenne, projetée en l'air"),
"alaznists-jinx": CU("Maléfice de brûlure", 3, ["sort", "brûlure"], why="chaque sort lancé la brûle"),
"apsus-shining-scales": GA("Écailles brillantes", 1, ["écaille", "garde", "souffle"], 5, "5 ajouté à l'armure, crocs bienveillants"),
"archons-aura": EP("Aura d'archonte", NINT, P, ["aura", "faiblesse"], why="tes ennemis frappent et se gardent moins bien"),
"archons-trumpet": EV("Trompette d'archonte", P, ["son", "paralysie"], why="une sonnerie qui paralyse"),
"augmenting-wall": EP("Mur renforçant", FO, P, ["mur", "énergie"], why="un mur d'énergie élémentaire qui renforce ou blesse"),
"ball-lightning": EV("Boules de foudre", P, ["foudre", "sphère"], 11, "3d6 par boule"),
"battering-blast": EV("Souffle martelant", 3, ["force", "recul"], 11, "une boule de force qui repousse"),
"beacon-of-guilt": EP("Phare de culpabilité", VIS, 1, ["objet", "vol", "lumière"], why="qui prend l'objet s'illumine", cible_obj=["objet"]),
"betraying-sting": EV("Piqûre de trahison", P, ["trahison", "mort"], why="frappe qui te croyait ami"),
"biting-words": EV("Mots mordants", 3, ["parole"], 4, "1d6 en moyenne par les mots"),
"blast-of-wind": EV("Souffle de vent", P, ["vent", "recul"], why="un vent qui fait d'eux des fétus", aoe={"type": "line", "size": 60}),
"blazing-rainbow": EP("Arc-en-ciel flamboyant", FO, P, ["arc", "lumière", "pont"], why="un arc de flèches de lumière ou un pont"),
"blinding-ray": EV("Rayon aveuglant", 3, ["soleil", "cécité"], why="des rayons de soleil qui aveuglent"),
"blistering-invective": EV("Invective brûlante", P, ["parole", "peur", "feu"], why="des insultes qui démoralisent et brûlent"),
"blood-crow-strike": EP("Frappe des corbeaux de sang", INT, 1, ["corbeau", "feu", "nécrose"], why="tes poings font naître des corbeaux de feu"),
"blood-song": EP("Chant de sang", V("flux"), P, ["sang", "don"], why="ton sang offert pour donner des pouvoirs"),
"burn-corruption": EV("Corruption brûlée", P, ["vie", "démon", "feu"], why="la vie du lieu récurée, surtout la démoniaque"),
"burning-arc-keleshite": EV("Arc brûlant", 3, ["feu", "rebond"], 9, "un arc de feu qui rebondit"),
"burning-entanglement": EP("Enchevêtrement ardent", V("nature"), P, ["plante", "feu", "fumée"], why="des plantes qui saisissent et brûlent"),
"burning-gaze": EV("Regard brûlant", 3, ["regard", "feu"], 4, "1d6 en moyenne d'un regard"),
"burst-bonds": EV("Liens brisés", 1, ["entrave", "rupture"], 18, "les entraves frappées", cible_obj=["entrave"]),
"burst-of-force": EV("Explosion de force", P, ["force", "chute"], why="un souffle de force qui renverse"),
"burst-of-radiance": EP("Éclat radieux", VIS, P, ["lumière", "cécité"], why="un éclat qui aveugle"),
"call-the-void": EP("Appel du vide", NE, 1, ["vide", "aura"], why="une aura de néant"),
"campfire-wall": GA("Mur du feu de camp", P, ["feu", "abri"], why="un abri autour du feu de camp"),
"chain-of-perdition": EP("Chaîne de perdition", FO, P, ["chaîne", "force"], why="une chaîne de force flottante"),
"chains-of-fire": EV("Chaînes de feu", 3, ["feu", "rebond"], P, "un feu qui saute d'une cible à l'autre"),
"channel-the-gift": EP("Don canalisé", V("flux"), 2, ["sort", "don"], why="ton énergie nourrit ses sorts", impact_sats=[(None, ["sort"])]),
"chord-of-shards": EV("Accord d'éclats", 3, ["musique", "éclat"], 7, "2d6 en moyenne"),
"cleansing-fire": EV("Feu purificateur", P, ["feu", "cercle", "dissipation"], why="un cercle de feu qui purge l'hostile"),
"cold-ice-strike": EV("Frappe de glace", P, ["glace"], 39, "1d6 par niveau", aoe={"type": "cone", "size": 30}),
"contagious-flame": EV("Flamme contagieuse", 3, ["feu", "rayon", "rebond"], 14, "4d6 par rayon, qui sautent"),
"contingent-scroll": EP("Parchemin conditionnel", V("ordre"), 2, ["parchemin", "déclencheur"], why="un parchemin qui se lit de lui-même", cond=["déclencheur"], impact_sats=[(None, ["sort"])]),
"controlled-fireball": EV("Boule de feu maîtrisée", P, ["feu", "épargne"], P, "les alliés épargnés en secret"),
"cosmic-ray": EV("Rayon cosmique", 3, ["cosmos", "rayon"], why="un rayon d'énergie des étoiles"),
"creeping-ice": EP("Glace rampante", EXI, P, ["glace", "extension"], why="une nappe de glace qui s'étend"),
"damnation": EV("Damnation", 3, ["sort", "hostile", "châtiment"], why="punie pour ses sorts hostiles"),
"dancing-darkness": EP("Ténèbres dansantes", NVIS, P, ["ténèbres", "sphère"], 4, "quatre sphères de ténèbres flottantes"),
"daybreak-arrow": EP("Flèche de l'aube", INT, 1, ["trait", "aube"], why="des traits chargés d'aube", cible_obj=["trait"]),
"deadeyes-arrow": EP("Flèche du guetteur", FO, 1, ["trait", "foudre", "signal"], why="un trait de foudre qui blesse ou signale"),
"deadmans-contingency": EP("Disposition du mort", V("ordre"), 1, ["mort", "déclencheur"], why="une volonté qui s'accomplit à ta mort", cond=["mort"]),
"deafening-song-bolt": EV("Trait de chant assourdissant", 3, ["chant", "surdité"], 16, "3d10 et sourde"),
"decapitate": EP("Décapitation", INT, 1, ["arme", "tête"], why="un coup terrible qui tranche la tête", cible_obj=["arme"]),
"defensive-shock": GA("Choc défensif", 1, ["foudre", "riposte"], why="la foudre frappe qui te frappe"),
"detonate": EV("Détonation", P, ["énergie", "explosion"], 32, "1d8 par niveau autour de toi"),
"discordant-blast": EV("Souffle discordant", P, ["son", "recul"], 11, "3d6 en moyenne, qui repousse"),
"discovery-torch": EP("Torche de découverte", VIS, 1, ["lumière", "révélation"], why="une lueur qui fait tout remarquer", cible_obj=["objet"]),
"distracting-cacophony": EV("Cacophonie distrayante", P, ["bruit", "sort"], why="un vacarme où il est dur de lancer"),
"distressing-tone": EV("Ton affligeant", P, ["son", "nausée"], why="un son qui écœure"),
"dousing-rain": EP("Pluie étouffante", NINT, P, ["pluie", "feu", "foudre"], why="le feu éteint, la foudre attisée"),
"draconic-reservoir": GA("Réservoir draconique", 2, ["énergie", "absorption"], why="l'énergie absorbée et rendue au coup"),
"dread-bolt": EV("Trait de charge", 3, ["charge"], 9, "un trait contre la charge choisie", options=[
    O("Trait d'écœurement — contre l'hostile", src_idx="dread-bolt", cond=["hostile"], impact=(9, ["charge", "nausée"], "un trait qui écœure l'hostile")),
    O("Trait de cécité — contre l'hostile", src_idx="spear-of-purity", cond=["hostile"], impact=(9, ["charge", "cécité"], "un trait qui aveugle l'hostile")),
    O("Trait d'hébétude — contre le ténébreux", src_idx="arrow-of-law", cond=["ténébreux"], impact=(9, ["charge", "hébétude"], "un trait qui hébète le ténébreux")),
    O("Trait de lenteur — contre le lumineux", src_idx="shard-of-chaos", cond=["lumineux"], impact=(9, ["charge", "lenteur"], "un trait qui ralentit le lumineux"))]),
"ear-piercing-scream": EV("Cri perçant", 3, ["son", "hébétude"], 4, "1d6 en moyenne, hébétée"),
"ectoplasmic-eruption": EV("Éruption d'ectoplasme", P, ["ectoplasme", "entrave", "éthéré"], 21, "6d6, entravés, l'éthéré rejeté"),
"ectoplasmic-hand": EP("Main d'ectoplasme", EXI, P, ["main", "ectoplasme"], why="une main fantôme qui obéit"),
"ectoplasmic-snare": EP("Collet d'ectoplasme", FO, 3, ["ectoplasme", "lien"], why="un filament qui la retient à toi"),
"elemental-aura": GA("Aura élémentaire", 1, ["énergie", "aura"], why="une aura d'énergie qui brûle les proches"),
"elemental-touch": EP("Toucher élémentaire", INT, 1, ["énergie", "toucher"], 4, "ton toucher porte l'énergie"),
"emergency-force-sphere": GA("Sphère de force d'urgence", 1, ["force", "dôme"], why="un dôme de force jailli d'un coup"),
"etheric-shards": EV("Éclats éthériques", P, ["éclat", "invisible", "lenteur"], why="des éclats invisibles qui blessent et ralentissent"),
"explode-head": EV("Tête explosée", 3, ["tête", "explosion"], why="la tête d'un faible éclate et blesse alentour"),
"extreme-buoyancy": EP("Flottaison extrême", V("mouvement"), 3, ["eau", "remontée"], why="remontée d'un coup à la surface"),
"fiery-runes": EP("Runes de feu", INT, 1, ["arme", "rune", "feu"], why="une arme chargée de runes de feu", cible_obj=["arme"]),
"final-sacrifice": EV("Ultime sacrifice", 3, ["invoqué", "explosion"], why="l'être invoqué explose", cond=["invoqué"]),
"fire-breath": EV("Souffle de feu", P, ["feu", "souffle"], 14, "un cône de flammes à volonté", aoe={"type": "cone", "size": 15}),
"fire-snake": EV("Serpent de feu", P, ["feu", "serpent"], 39, "un chemin de feu sinueux"),
"fires-friend": GA("Ami du feu", 1, ["feu", "manteau"], why="un manteau de flammes qui blesse les ennemis"),
"firestream": EV("Torrent de feu", P, ["feu", "jet"], why="un jet de feu", aoe={"type": "line", "size": 30}),
"flashfire": EV("Feu soudain", P, ["feu", "fumée"], why="des feux fumants qui jaillissent"),
"flickering-lights": EP("Lumières vacillantes", NVIS, P, ["lumière", "vacillement"], why="une lumière qui ne tient pas"),
"flurry-of-snowballs": EV("Rafale de boules de neige", P, ["neige", "froid"], 14, "4d6 en moyenne", aoe={"type": "cone", "size": 15}),
"force-hook-charge": EP("Crochet de force", V("mouvement"), 3, ["force", "crochet"], why="un crochet de force qui te tire vers elle"),
"force-punch": EV("Poing de force", 3, ["force", "recul"], why="un coup de force qui repousse"),
"force-sword": EP("Épée de force", FO, 1, ["épée", "force"], why="une épée longue faite de force"),
"forceful-strike": EP("Frappe puissante", INT, 1, ["coup", "recul"], why="un coup qui projette"),
"frigid-touch": EV("Toucher glacé", 3, ["froid", "chancellement"], 14, "4d6 en moyenne, chancelante"),
"frost-fall": EV("Chute de givre", P, ["givre", "froid"], why="la zone couverte d'un givre glacé"),
"furious-fire-barrage": EV("Barrage de feu furieux", P, ["feu", "boule"], why="des boules de feu jetées sans fin"),
"gentle-breeze": GA("Brise légère", 2, ["vent", "gaz", "chaleur"], why="une brise contre nuées, gaz et chaleur"),
"gozrehs-trident": EP("Trident de foudre", FO, 1, ["trident", "foudre"], why="un trident fourchu de foudre"),
"gusting-sphere": EV("Sphère de bourrasque", P, ["vent", "sphère"], why="une boule de vent qui bouscule"),
"heatstroke": EV("Coup de chaleur", 3, ["chaleur", "fatigue"], why="assommée par la chaleur"),
"holy-whisper": EV("Murmure sacré", P, ["murmure", "hostile"], why="écœure l'hostile, soutient le bienveillant", aoe={"type": "cone", "size": 30}),
"horn-of-pursuit": EP("Cor de poursuite", FO, P, ["son", "lointain"], 3, "trois notes entendues à des lieues"),
"hungry-darkness": EV("Ténèbres affamées", P, ["ténèbres", "dent"], why="des ténèbres pleines de dents"),
"hydraulic-push": EV("Poussée hydraulique", 3, ["eau", "recul"], why="une vague qui repousse"),
"hydraulic-torrent": EV("Torrent hydraulique", P, ["eau", "recul"], why="un torrent qui emporte", aoe={"type": "line", "size": 60}),
"ice-slick": EV("Verglas", P, ["glace", "chute"], why="une glace qui blesse et fait tomber"),
"icy-prison": EV("Prison de glace", 3, ["glace", "prison"], why="la glace l'enserre et la blesse", options=[O("Prison de glace"), O("Prison de glace de groupe", src_idx="icy-prison-mass", qty_cible=P)]),
"incorporeal-chains": EV("Chaînes de l'intangible", 3, ["chaîne", "intangible"], why="des chaînes qui saisissent l'intangible"),
"jolting-portent": CU("Présage électrisant", 3, ["foudre", "destin"], why="la foudre la frappe à chaque geste"),
"ki-shout": EV("Cri du souffle", 3, ["son", "étourdissement"], 46, "1d6 par niveau, étourdie"),
"last-azlantis-defending-sword": EP("Épée défensive", FO, 1, ["épée", "garde"], why="une épée de force qui défend", options=[
    O("Épée défensive"), O("Épées défensives", src_idx="last-azlantis-defending-sword-mass", qty_cible=P)]),
"lead-anchor": EP("Ancre de plomb", V("mouvement"), 3, ["eau", "coulée"], why="coulée vers les profondeurs"),
"leashed-shackles": EP("Entraves en laisse", V("ordre", True), 3, ["entrave", "lieu"], why="tenue à un lieu"),
"light-lance": EP("Lance de lumière", FO, P, ["lumière", "phare"], why="un phare de lumière qui monte"),
"light-prison": EV("Prison de lumière", 3, ["lumière", "prison"], why="qui force la cage est brûlé et aveuglé"),
"lightning-arc": EV("Arc de foudre", P, ["foudre", "ligne"], 39, "1d6 par niveau", aoe={"type": "line", "size": 60}),
"lightning-lash": EP("Fouet de foudre", FO, 1, ["fouet", "foudre"], why="un fouet de foudre crépitant"),
"litany-of-order": CU("Litanie de l'ordre", 3, ["ténébreux", "faiblesse"], why="le ténébreux plus vulnérable aux lumineux", cond=["ténébreux"]),
"litany-of-righteousness": CU("Litanie de droiture", 3, ["hostile", "faiblesse"], why="l'hostile plus vulnérable aux bienveillants", cond=["hostile"]),
"litany-of-thunder": EV("Litanie du tonnerre", 3, ["tonnerre", "surdité", "confusion"], why="sourde et confuse"),
"mages-decree": EP("Décret du mage", REL, P, ["message", "lointain"], why="un message entendu à des lieues"),
"martial-telekinesis": EP("Télékinésie martiale", FO, 3, ["force", "bousculade"], why="bousculer et désarmer à distance"),
"molten-orb": EV("Orbe de métal fondu", 3, ["métal", "feu"], 7, "2d6, et la brûlure qui dure"),
"moonrise-arrow": EP("Flèche du lever de lune", INT, 1, ["trait", "argent", "lumière"], why="des traits de lumière d'argent", cible_obj=["trait"]),
"morning-sun": EP("Soleil du matin", VIS, P, ["soleil", "sphère"], why="une sphère de lumière solaire"),
"motes-of-dusk-and-dawn": EP("Grains d'aube et de crépuscule", VIS, P, ["lumière", "ombre"], 4, "quatre grains de lumière ou d'ombre"),
"mydriatic-spontaneity": EV("Mydriase", 3, ["lumière", "douleur"], why="migraine et yeux à vif", options=[O("Mydriase"), O("Mydriase de groupe", src_idx="mydriatic-spontaneity-mass", qty_cible=P)]),
"neutral-buoyancy": EP("Flottaison neutre", V("mouvement"), 2, ["eau", "aisance"], why="à l'aise entre deux eaux"),
"night-of-blades": EV("Nuit de lames", P, ["lame", "mur"], why="un mur de petites lames noires"),
"numerological-evocation": EV("Rayons calculés", 3, ["énergie", "rayon"], why="des rayons d'énergie élémentaire"),
"pain-strike": EV("Frappe de douleur", 3, ["douleur", "durée"], 4, "1d6 qui assomme, à chaque instant", options=[O("Frappe de douleur"), O("Frappe de douleur de groupe", src_idx="pain-strike-mass", qty_cible=P)]),
"pale-flame": EP("Flamme pâle", FO, 1, ["feu", "plante", "pâle"], why="une flamme pâle qui brûle surtout les plantes"),
"path-of-the-winds": EV("Chemin des vents", P, ["vent", "chemin"], why="des vents qui dégagent ta route"),
"piercing-shriek": EV("Hurlement perçant", 3, ["son", "chancellement"], why="un son qui fait chanceler"),
"pilfering-hand": EP("Main chapardeuse", FO, 1, ["main", "objet"], why="saisir un objet de loin", cible_obj=["objet"]),
"pinecone-bomb": EV("Bombe de pomme de pin", P, ["éclat", "explosion"], 9, "une pomme de pin qui explose", cible_obj=["pomme"]),
"poison-breath": EV("Souffle empoisonné", P, ["poison", "souffle"], why="un cône de poison", aoe={"type": "cone", "size": 60}),
"protective-penumbra": GA("Pénombre protectrice", 2, ["ombre", "lumière"], why="une ombre qui garde de la lumière"),
"pyrotechnic-eruption": EV("Éruption pyrotechnique", 3, ["feu", "répétition"], why="des flammes qui brûlent encore et encore"),
"rebuke": EV("Semonce", P, ["colère", "son"], 22, "1d8 par deux niveaux"),
"reflexive-barrier": GA("Barrière réflexe", 1, ["force", "garde"], 5, "un éclat de force qui garde"),
"rend-body-i": EV("Corps déchiré", 3, ["force", "membre"], why="la force arrache les membres", options=[
    O(f"Corps déchiré {r}", src_idx=f"rend-body-{r.lower()}", impact=(n, ["force", "membre"] + x, d)) for r, n, x, d in [
    ("I", 32, [], "1d6 par niveau en moyenne"), ("II", 46, [], "plus lourd"), ("III", 55, ["nausée"], "nauséeuse tant qu'elle saigne"), ("IV", 64, ["nausée", "amputation"], "un membre peut tomber")]]),
"resounding-blow": EP("Coup retentissant", INT, 1, ["coup", "tonnerre"], 4, "1d6 de plus par coup"),
"revealing-light": EP("Lumière révélatrice", VIS, 1, ["lumière", "dissimulation"], why="une lumière où l'on ne se cache pas", cible_obj=["objet"]),
"ricochet-shot": EP("Tir en ricochet", INT, 1, ["trait", "rebond"], why="des traits qui ricochent", cible_obj=["trait"]),
"ride-the-lightning": EP("Chevaucher la foudre", ID, 1, ["foudre", "forme"], why="devenir la foudre"),
"river-of-wind": EV("Rivière de vent", P, ["vent", "chute"], 14, "4d6 qui assomment, renversés ou poussés", aoe={"type": "line", "size": 120}),
"rope-tornado": EV("Tornade furieuse", P, ["vent", "chute"], why="des vents qui jettent à terre"),
"runic-overload": EV("Surcharge runique", P, ["rune", "explosion"], why="les runes chargées jusqu'à l'explosion"),
"sacred-nimbus": GA("Nimbe sacré", 1, ["aura", "riposte", "hostile"], why="frappe l'hostile qui te frappe, te garde de lui", cond=["hostile"]),
"sacred-space": GA("Espace consacré", P, ["sacré", "lieu"], why="un lieu sanctifié"),
"sanctify-corpse": GA("Corps sanctifié", 1, ["cadavre", "repos"], why="un corps qui ne se relèvera pas", cible_obj=["cadavre"]),
"scouring-winds": EV("Vents récurants", P, ["vent", "sable"], 11, "3d6 à chaque instant, la vue bouchée"),
"screaming-flames": EV("Flammes hurlantes", P, ["feu", "cri"], why="une vague de flammes qui hurlent", aoe={"type": "cone", "size": 30}),
"sheet-lightning": EV("Nappe d'éclairs", P, ["foudre", "hébétude"], why="tous hébétés"),
"shield-of-darkness": GA("Bouclier de ténèbres", 1, ["ténèbres", "dissimulation"], why="tout entier caché dans le noir"),
"shield-of-the-dawnflower": GA("Bouclier de l'aube", 1, ["soleil", "garde", "feu"], why="un bouclier de soleil qui brûle", options=[
    O("Bouclier de l'aube"), O("Bouclier de l'aube suprême", src_idx="shield-of-the-dawnflower-greater", impact=(P, ["soleil", "garde", "feu", "éclat"], "plus ardent"))]),
"shifting-shadows": EP("Ombres changeantes", NVIS, P, ["ombre", "apparence"], why="l'allure de chacun brouillée"),
"shining-cord": EP("Corde brillante", REL, 3, ["corde", "argent", "prévision"], why="une corde d'argent qui trahit ses gestes"),
"shroud-of-darkness": EP("Linceul de ténèbres", NVIS, 3, ["ténèbres", "vue"], why="la vue voilée"),
"siege-scatter": EV("Éparpillement de siège", P, ["roche", "terre"], why="une salve de roche et de terre"),
"sign-of-wrath": EV("Signe de colère", P, ["symbole", "recul"], why="un symbole géant qui repousse"),
"silverlight": EP("Lumière d'argent", FO, P, ["lumière", "argent"], why="une lumière d'argent qui blesse ceux que l'argent blesse"),
"sirocco": EV("Sirocco", P, ["vent", "chaleur", "fatigue"], 14, "4d6, fatigués, jetés à terre"),
"snowball": EV("Boule de neige", 3, ["neige", "froid"], 4, "1d6 par deux niveaux"),
"sonic-scream": EV("Cri sonique", P, ["son"], why="un cône de son à volonté", aoe={"type": "cone", "size": 15}),
"sonic-thrust": EV("Poussée sonique", P, ["son", "recul"], why="le son repousse"),
"spark": EV("Étincelle", 1, ["feu", "étincelle"], why="un objet inflammable s'allume", cible_obj=["objet"]),
"spellcasting-contract-lesser": EP("Contrat de magie", REL, 2, ["contrat", "sort"], why="tes sorts prêtés par contrat", impact_sats=[(None, ["sort"])], options=[
    O(lab, src_idx=k, impact_sats=[(None, ["sort"]), (n, ["seuil", "niveau"])]) for lab, k, n in [("Contrat de magie mineur", "spellcasting-contract-lesser", 3), ("Contrat de magie", "spellcasting-contract", 6), ("Contrat de magie suprême", "spellcasting-contract-greater", 9)]]),
"spirit-bound-blade": EP("Lame liée à l'esprit", INT, 1, ["arme", "émotion", "intangible"], why="une arme qui touche l'intangible, mue par une émotion", cible_obj=["arme"]),
"spiritual-ally": EP("Allié spirituel", EXI, 1, ["allié", "force"], why="un allié divin à tes côtés"),
"spiritual-squire": EP("Écuyer spirituel", EXI, 1, ["écuyer", "force"], why="un écuyer de force qui t'assiste"),
"spontaneous-immolation": EV("Immolation spontanée", 3, ["feu", "embrasement"], 11, "3d6 en moyenne, en feu"),
"spotlight": EP("Projecteur", VIS, P, ["lumière", "ombre"], why="une lumière mobile qui éteint le reste"),
"steam-ray-fusillade": EV("Fusillade de vapeur", 3, ["vapeur", "rayon"], why="des rayons de vapeur, même sous l'eau"),
"stormbolts": EV("Éclairs de tempête", P, ["foudre", "étourdissement"], 90, "1d8 par niveau"),
"suppressing-stone": GA("Pierre de suppression", 1, ["pierre", "esprit"], why="une pierre qui garde l'esprit", cible_obj=["pierre"]),
"symbol-of-storms": SYMP("Symbole de tempête", verb=NF, impact=(P, ["vent", "foudre"], "vents et éclairs")),
"tamers-lash": EP("Fouet du dompteur", FO, 1, ["fouet", "son", "bête"], why="un fouet de son qui effraie les bêtes"),
"telekinetic-charge": EP("Charge télékinétique", V("mouvement"), 2, ["force", "projection"], why="un allié lancé à travers les airs"),
"telekinetic-projectile": EV("Projectile télékinétique", 3, ["objet", "projection"], 4, "1d6 en moyenne"),
"telekinetic-storm": EV("Tempête télékinétique", P, ["force", "étourdissement"], 60, "1d6 par niveau, hébétés et étourdis"),
"telekinetic-strikes": EP("Frappes télékinétiques", INT, 2, ["force", "poing"], why="des poings chargés de force"),
"thundering-drums": EV("Tambours tonnants", P, ["tonnerre", "chute"], 32, "1d8 par niveau, renversés", aoe={"type": "cone", "size": 15}),
"thunderstomp": EV("Piétinement tonnant", 3, ["chute"], why="jetée à terre", options=[O("Piétinement tonnant"), O("Piétinement tonnant suprême", src_idx="thunderstomp-greater", qty_cible=P)]),
"touch-of-combustion": EV("Toucher de combustion", 3, ["feu", "combustion"], why="elle prend feu"),
"tracking-mark": EP("Marque de pisteur", VIS, 1, ["piste", "indice"], why="voir traces et indices"),
"transfer-familiar": EP("Familier transmis", REL, 2, ["compagnon", "maître"], why="ton familier confié à un autre", cond=["compagnon"]),
"trial-by-fire": EV("Épreuve du feu", 3, ["feu", "conviction"], why="le feu juge sa conviction"),
"trial-of-fire-and-acid": EV("Épreuve du feu et de l'acide", 3, ["feu", "acide"], why="couverte d'acide brûlant"),
"twilight-knife": EP("Couteau du crépuscule", FO, 1, ["couteau", "flottant"], why="un couteau qui frappe avec toi"),
"unbearable-brightness": EP("Éclat insoutenable", VIS, P, ["lumière", "éblouissement"], why="ton corps éblouit et aveugle"),
"unflappable-mien": GA("Mine imperturbable", 1, ["force", "recul"], why="une barrière qui repousse et blesse"),
"unwelcome-halo": EP("Halo importun", VIS, 3, ["halo", "lumière"], why="un halo qui l'empêche de se cacher"),
"vengeful-comets": GA("Comètes vengeresses", 1, ["comète", "riposte"], why="des comètes frappent qui te vise"),
"vitriolic-mist": GA("Brume vitriolique", 1, ["acide", "riposte"], why="qui frappe est rongé par l'acide"),
"volcanic-storm": EV("Tempête volcanique", P, ["roche", "feu"], 18, "5d6 en moyenne"),
"vortex": EV("Vortex", P, ["eau", "tourbillon"], why="un tourbillon dans l'eau"),
"wake-of-light": EP("Sillage de lumière", V("qualite"), P, ["lumière", "sillage"], why="aide le bienveillant, gêne l'hostile"),
"wall-of-ectoplasm": EP("Mur d'ectoplasme", FO, P, ["mur", "ectoplasme", "éthéré"], why="un mur d'esprits sur deux plans"),
"wall-of-sound": EP("Mur de son", FO, P, ["mur", "son"], why="un mur de son qui dévie et blesse"),
"wall-of-split-illumination": EP("Mur de clair-obscur", VIS, P, ["mur", "lumière", "ténèbres"], why="lumière d'un côté, ténèbres de l'autre"),
"winds-of-vengeance": EP("Vents de vengeance", ID, 1, ["vent", "vol"], why="voler et frapper avec le vent"),
"wrathful-mantle": GA("Manteau de courroux", 2, ["lumière", "résistance"], 5, "jusqu'à 5 ajouté à sa résistance"),
}
FICHES.update(NEWPF_EVO)
PFV("Evocation")
ADDPF("flaming-sphere", O("Sphère de feu suprême", src_idx="flaming-sphere-greater"))
ADDPF("flare", O("Éclat de groupe", src_idx="flare-burst", aoe={"type": "sphere", "size": 10}))
ADDPF("daylight", O("Lumière la plus vive", src_idx="brightest-light"))
ADDPF("heal", O("Purification", src_idx="cleanse"))

# --- Pathfinder 1, lot 7 : Invocation ---
_cls = "pure mécanique de classe"
PF1_RELECTURE.update({
"fey-gate": "ouvre un portail vers le Premier Monde, plan propre à la cosmologie de Golarion",
"font-of-spirit-magic": f"repose sur les « sorts d'esprit » du chaman : {_cls}",
"heros-defiance": f"permet l'« imposition des mains » du paladin : {_cls}",
"infernal-challenger": "sert l'initiation des Chevaliers infernaux, ordre propre à Golarion",
"ki-arrow": f"repose sur le « ki » et les « attaques à mains nues » du moine : {_cls}",
"replenish-ki": f"remplit la « réserve de ki » : {_cls}",
"life-conduit": f"repose sur l'eidolon du conjurateur : {_cls}",
"life-conduit-improved": f"repose sur l'eidolon du conjurateur : {_cls}",
"life-conduit-greater": f"repose sur l'eidolon du conjurateur : {_cls}",
"purified-calling": f"repose sur l'eidolon du conjurateur : {_cls}",
"rejuvenate-eidolon": f"repose sur l'eidolon du conjurateur : {_cls}",
"rejuvenate-eidolon-lesser": f"repose sur l'eidolon du conjurateur : {_cls}",
"rejuvenate-eidolon-greater": f"repose sur l'eidolon du conjurateur : {_cls}",
"restore-eidolon": f"repose sur l'eidolon du conjurateur : {_cls}",
"restore-eidolon-lesser": f"repose sur l'eidolon du conjurateur : {_cls}",
"summon-eidolon": f"repose sur l'eidolon du conjurateur : {_cls}",
"reviving-finale": f"« final » de barde : {_cls}",
"purging-finale": f"« final » de barde : {_cls}",
"song-of-kyonin": f"renforce la « représentation bardique » (et nomme un royaume de Golarion) : {_cls}",
"shadow-bomb-admixture": f"modifie les « bombes » de l'alchimiste : {_cls}",
"viper-bomb-admixture": f"modifie les « bombes » de l'alchimiste : {_cls}",
"realm-retribution": "fait « compter » les coups comme d'un alignement : pure mécanique de jeu",
"protective-spirit": "protège des « attaques d'opportunité » : pure mécanique de jeu",
"spindrift-spritz": "fait garder le meilleur de deux jets : pure mécanique de jeu",
"spindrift-spritz-mass": "fait garder le meilleur de deux jets : pure mécanique de jeu",
"summon-cacodaemon": "convoque des daémons d'Abaddon, propres à la cosmologie de Golarion",
"summon-cacodaemon-greater": "convoque des daémons d'Abaddon, propres à la cosmologie de Golarion",
"summon-ceustodaemon": "convoque des daémons d'Abaddon, propres à la cosmologie de Golarion",
"summon-derghodaemon": "convoque des daémons d'Abaddon, propres à la cosmologie de Golarion",
"summon-erodaemon": "convoque des daémons d'Abaddon, propres à la cosmologie de Golarion",
"summon-meladaemon": "convoque des daémons d'Abaddon, propres à la cosmologie de Golarion",
"summon-thanadaemon": "convoque des daémons d'Abaddon, propres à la cosmologie de Golarion",
"summon-lesser-psychopomp": "convoque des psychopompes du Cimetière, propres à la cosmologie de Golarion",
"summon-vanth": "convoque un psychopompe du Cimetière, propre à la cosmologie de Golarion",
"summon-kami": "convoque des kamis de Tian Xia, propres au monde de Golarion",
})
TP, CV, HE = V("mouvement"), V("trame"), V("existence")
CR = lambda fr, cible, words, v=None, why="", **kw: EP(fr, EXI, cible, words, v, why, **kw)
TL = lambda fr, cible, words, v=None, why="", **kw: EP(fr, TP, cible, words, v, why, **kw)
CN = lambda fr, cible, words, v=None, why="", **kw: EP(fr, CV, cible, words, v, why, **kw)
SO = lambda fr, cible, words, v=None, why="", **kw: EP(fr, HE, cible, ["vie"] + list(words), v, why, **kw)
NEWPF_CONJ = {
"ablative-barrier": GA("Barrière ablative", 2, ["force", "couche"], why="des couches de force qui encaissent"),
"abundant-ammunition": CN("Munitions abondantes", 1, ["trait", "renouveau"], why="les traits reviennent chaque instant", cible_obj=["carquois"]),
"accept-affliction": EP("Mal accepté", V("flux"), 2, ["mal", "transfert"], why="tu prends ses maux sur toi"),
"acidic-spray": CR("Jet acide", P, ["acide", "jet"], 39, "1d6 par niveau, et la brûlure qui reste", aoe={"type": "cone", "size": 60}),
"adhesive-spittle": CR("Crachat collant", 3, ["colle", "entrave"], why="un crachat qui englue"),
"air-bubble": CR("Bulle d'air", 2, ["air", "souffle"], why="une poche d'air autour de la tête"),
"alluring-spores": CR("Spores enjôleuses", P, ["spore", "charme"], why="plus sensibles à tes charmes"),
"ally-across-time": CN("Allié d'un autre temps", 1, ["double", "monde"], why="ton double d'un monde voisin vient aider", options=[
    O("Allié d'un autre temps"), O("Armée d'un autre temps", src_idx="army-across-time", impact=(P, ["double", "monde", "armée"], "plusieurs doubles"))]),
"ancestral-gift": CN("Don ancestral", 1, ["ancêtre", "arme"], why="un ancêtre t'apporte une arme fantôme"),
"anywhere-but-here": TL("N'importe où sauf ici", P, ["plan", "hasard"], why="emportés vers un plan au hasard"),
"apport-object": TL("Apport", 1, ["objet", "envoi"], why="un petit objet envoyé ou reçu", cible_obj=["objet"], options=[
    O("Apport d'objet"), O("Apport d'animal", src_idx="apport-animal", cible_obj=[], cond=["bête"])]),
"aquatic-cavalry": CN("Cavalerie aquatique", P, ["monture", "eau"], why="des hippocampes pour monture"),
"aqueous-orb": CR("Orbe aqueux", P, ["eau", "sphère"], why="une sphère d'eau qui roule et engloutit"),
"arcane-pocket": CR("Poche arcanique", 1, ["poche", "espace"], why="un espace caché dans une bourse", cible_obj=["bourse"]),
"arrow-eruption": CR("Éruption de flèches", P, ["trait", "double"], why="la flèche mortelle se multiplie"),
"ash-storm": CR("Tempête de cendres", P, ["cendre", "vue"], why="une cendre qui aveugle et ralentit"),
"balance-of-suffering": EP("Balance des souffrances", V("flux"), 3, ["vie", "transfert"], why="la vie de l'un donnée à l'autre"),
"barbed-chains": CN("Chaînes barbelées", 3, ["chaîne", "peur"], why="des chaînes infernales qui frappent et effraient"),
"bards-escape": TL("Fuite du ménestrel", P, ["fuite", "abri"], why="toi et tes alliés à l'abri d'un coup"),
"bilocation": CR("Bilocation", 1, ["double", "lieu"], why="être en deux lieux à la fois"),
"bind-sage": CN("Sage lié", 9, ["savant", "réponse"], why="un savant d'ailleurs convoqué pour répondre"),
"blaze-of-glory": SO("Flamme de gloire", P, ["bienveillant", "hostile"], why="ton dernier élan soigne le bienveillant, frappe l'hostile"),
"blessing-of-courage-and-life": GA("Bénédiction de courage et de vie", 2, ["peur", "mort"], 2, "2 ajouté contre la peur et la mort"),
"blood-mist": CR("Brume de sang", P, ["sang", "sagesse", "rage"], why="une brume qui rend fou de rage"),
"bountiful-banquet": CR("Banquet abondant", P, ["festin"], why="un festin pour beaucoup"),
"bow-spirit": CN("Esprit de l'arc", 1, ["esprit", "trait"], why="un esprit invisible tire tes flèches"),
"breath-of-life": SO("Souffle de vie", 2, ["retour"], 29, "5d8 + 1 par niveau, et rappelle un mort tout juste tombé"),
"burning-sands": CR("Sables brûlants", P, ["sable", "feu"], why="un sable brûlant qui gêne"),
"burst-of-nettles": CR("Explosion d'orties", P, ["ortie", "acide"], 14, "3d6 et 1d6 d'acide"),
"calistrias-guardian-wasps": CN("Guêpes gardiennes", P, ["guêpe", "garde"], why="un essaim qui garde la zone"),
"call-construct": TL("Appel de l'artefact", 1, ["artefact", "appel"], why="ton artefact animé te rejoint"),
"call-spirit": CN("Appel d'esprit", 1, ["esprit", "mort"], why="l'esprit d'un être se manifeste"),
"callback": TL("Rappel", 2, ["compagnon", "retour"], why="ton compagnon blessé ramené à toi", cond=["compagnon"], options=[
    O("Rappel"), O("Rappel suprême", src_idx="callback-greater", impact=(P, ["compagnon", "retour", "lointain"], "même de très loin"))]),
"cape-of-wasps": CN("Cape de guêpes", 1, ["guêpe", "garde", "vol"], why="un essaim qui te garde ou te porte"),
"carrying-wind": CR("Vent porteur", 1, ["vent", "vol"], why="un vent qui te porte"),
"caustic-eruption": CR("Éruption caustique", P, ["acide", "durée"], 46, "1d6 par niveau, et qui dure"),
"cave-fangs": CR("Crocs de la caverne", P, ["roche", "piège"], why="un piège de stalactites"),
"celestial-healing": SO("Guérison céleste", 2, ["régénération"], 1, "1 point par instant", options=[
    O("Guérison céleste"), O("Guérison céleste suprême", src_idx="celestial-healing-greater", impact=(4, ["vie", "régénération"], "4 points par instant"))]),
"chains-of-light": CR("Chaînes de lumière", 3, ["chaîne", "lumière", "paralysie"], why="des chaînes de lumière qui figent"),
"clashing-rocks": CR("Rocs qui s'entrechoquent", 3, ["roche", "écrasement"], 70, "20d6 en moyenne"),
"climbing-beanstalk": CR("Haricot grimpant", P, ["plante", "escalade"], why="une tige facile à grimper"),
"cloud-of-seasickness": CR("Nuage de mal de mer", P, ["nuage", "nausée"], why="un nuage qui donne le mal de mer"),
"cold-iron-fetters": CR("Entraves de fer froid", 3, ["fer", "lenteur"], why="des entraves qui ralentissent"),
"companion-transportation": TL("Échange avec le compagnon", 2, ["compagnon", "échange"], why="toi et ton compagnon changés de place", cond=["compagnon"]),
"conjure-black-pudding": CN("Convocation de pouding noir", P, ["vase", "acide"], why="une vase dévorante"),
"conjure-carriage": CR("Carrosse", P, ["carrosse"], why="un beau carrosse"),
"conjure-deadfall": CR("Chute de pierre", P, ["roche", "chute", "pointe"], why="un bloc hérissé tombe d'en haut"),
"corrosive-consumption": CR("Consomption corrosive", 3, ["acide", "extension"], why="une tache d'acide qui ronge"),
"corrosive-touch": CR("Toucher corrosif", 3, ["acide", "toucher"], 13, "1d4 par niveau"),
"create-armaments": CR("Armement", 1, ["arme", "armure"], why="une arme, un bouclier ou une armure"),
"create-demiplane-lesser": CR("Création de demi-plan", P, ["plan", "création"], why="un demi-plan à toi", options=[
    O("Demi-plan mineur"), O("Demi-plan", src_idx="create-demiplane", impact=(P, ["plan", "création", "trait"], "plus vaste, avec ses lois")),
    O("Demi-plan suprême", src_idx="create-demiplane-greater", impact=(P, ["plan", "création", "trait", "vastitude"], "plus vaste encore"))]),
"create-pit": CR("Fosse", P, ["fosse"], why="une fosse extradimensionnelle", options=[
    O("Fosse"), O("Fosse à pointes", src_idx="spiked-pit", impact=(P, ["fosse", "pointe"], "hérissée de pointes")),
    O("Fosse acide", src_idx="acid-pit", impact=(P, ["fosse", "acide"], "au fond d'acide")),
    O("Fosse affamée", src_idx="hungry-pit", impact=(P, ["fosse", "écrasement"], "qui se referme")),
    O("Fosse aux requins", src_idx="walk-the-plank", impact=(P, ["fosse", "eau", "requin"], "pleine d'eau et de requins")),
    O("Fosse errante", src_idx="roaming-pit", impact=(P, ["fosse", "déplacement"], "qui se déplace"))]),
"cruel-jaunt": TL("Saut cruel", 1, ["peur", "téléportation"], why="sentir la peur et surgir près d'elle"),
"curative-distillation": SO("Distillation curative", 1, ["remède"], why="un remède rendu plus fort", cible_obj=["remède"]),
"curse-of-dragonflies": CU("Malédiction des libellules", 3, ["vol", "malédiction"], why="elle vole mal"),
"cushioning-bands": GA("Bandes amortissantes", 2, ["force", "écrasement"], why="des bandes de force contre l'écrasement"),
"damnation-stride": TL("Pas de damnation", 1, ["porte", "feu"], why="un saut qui laisse une gerbe de flammes"),
"delay-disease": GA("Maladie retardée", 2, ["maladie"], why="à l'abri de la maladie un temps"),
"desperate-weapon": CR("Arme du désespoir", 1, ["arme", "fortune"], why="une arme de fortune"),
"dimensional-bounce": TL("Rebond dimensionnel", 1, ["lieu", "aller-retour"], why="sauter entre deux lieux"),
"draconic-ally": CR("Allié draconique", P, ["dragon", "serviteur"], why="un serviteur draconique fidèle"),
"dream-feast": CR("Festin de rêve", 2, ["sommeil", "nourriture"], why="nourrie pendant son sommeil"),
"duplicate-familiar": CR("Familier dédoublé", 1, ["compagnon", "double"], why="un double de ton familier", cond=["compagnon"]),
"dust-of-twilight": CR("Poussière crépusculaire", P, ["poussière", "lumière", "extinction"], why="les lumières éteintes"),
"eagle-aerie": CN("Aire des aigles", P, ["aigle", "monture"], why="des aigles géants"),
"eaglesoul": CN("Âme d'aigle", 1, ["bienveillant", "pouvoir"], why="la force d'un être d'ailleurs bienveillant"),
"entice-fey-lesser": CN("Fée enjôlée", 9, ["fée", "service"], why="une fée gagnée à ton service", cond=["FEE"], options=[
    O("Fée enjôlée mineure", impact_sats=[(27, ["vie", "plafond"])]), O("Fée enjôlée", src_idx="entice-fey", impact_sats=[(54, ["vie", "plafond"])]),
    O("Fée enjôlée suprême", src_idx="entice-fey-greater", impact_sats=[(81, ["vie", "plafond"])])]),
"ethereal-envelope": TL("Enveloppe éthérée", 1, ["éthéré", "cocon"], why="ton corps sans conscience à l'abri sur l'éthéré", options=[
    O("Enveloppe éthérée"), O("Enveloppement éthéré", src_idx="ethereal-envelopment", cible=3)]),
"euphoric-cloud": CR("Nuage euphorique", P, ["brume", "fascination"], why="une brume qui fascine"),
"evaluators-lens": CR("Lentille de l'estimateur", 1, ["lentille", "illusion"], why="une lentille de force contre les illusions"),
"expeditious-construction": CR("Construction expéditive", P, ["terre", "muret"], why="un muret de terre ou de pierre"),
"expel-blood": CR("Sang expulsé", 3, ["sang", "élémentaire"], why="son sang arraché devient un élémentaire"),
"fairy-ring-retreat": CR("Retraite du cercle des fées", P, ["champignon", "pré"], why="un cercle qui mène à un pré caché"),
"fiery-shuriken": CR("Étoiles de feu", 1, ["feu", "projectile"], why="des étoiles de feu à lancer"),
"flame-steed": CR("Destrier de flammes", P, ["monture", "feu", "fumée"], why="un destrier qui ne craint pas le feu"),
"flash-flood": CR("Crue soudaine", P, ["eau", "recul"], why="une vague qui frappe et pousse"),
"flash-forward": TL("Élan et retour", 1, ["élan", "retour"], why="frapper puis revenir d'un saut"),
"fleshwarping-swarm-drow": CN("Nuée de remodelage", P, ["nuée", "chair"], why="une nuée qui rend la chair malléable"),
"fleshworm-infestation": CN("Infestation de vers", 3, ["ver", "chair"], why="des vers qui rongent la chair"),
"force-anchor": CR("Ancre de force", 3, ["force", "intangible"], why="l'intangible ancré sur place"),
"freedoms-toast": TL("Toast à la liberté", 2, ["liberté", "téléportation"], why="libérée et déplacée d'un pas"),
"frost-mammoth": CR("Mammouth de givre", P, ["glace", "mammouth"], why="un mastodonte de glace"),
"fumblestep": CU("Pas maladroit", 3, ["maladresse", "chute"], why="un pas qui trébuche"),
"garden-of-peril": CR("Jardin du péril", P, ["champignon", "poison"], why="des champignons empoisonnés"),
"getaway": TL("Échappée", P, ["fuite", "lieu"], why="emportés vers un lieu choisi d'avance"),
"geyser": CR("Geyser", P, ["eau", "brûlure"], why="un geyser d'eau bouillante"),
"ghost-wolf": CR("Loup fantôme", P, ["monture", "fumée", "peur"], why="une monture de fumée noire qui effraie"),
"gloomblind-bolts": CR("Traits de ténèbres", 3, ["nécrose", "trait"], why="des traits qui blessent les vivants, soignent les morts"),
"glue-seal": CR("Sceau de colle", P, ["colle"], why="une surface collante"),
"grasping-tentacles": CR("Tentacules agrippants", P, ["tentacule", "ruse"], why="des tentacules qui jouent de sales tours"),
"gravel-vortex": CR("Tourbillon de gravier", P, ["gravier", "vent"], why="une grêle de pierres"),
"greater-reversion": SO("Retour", 1, ["mémoire", "retour"], why="ton corps rendu à son état gardé", options=[
    O("Retour mineur", src_idx="minor-reversion", impact=(P, ["vie", "mémoire", "retour"], "ton corps rendu à son état gardé")),
    O("Retour mineur de groupe", src_idx="minor-reversion-mass", qty_cible=P, impact=(P, ["vie", "mémoire", "retour"], "pour plusieurs")),
    O("Retour", impact=(25, ["vie", "mémoire", "retour"], "3d8 + 1 par niveau"))]),
"grove-of-respite": CR("Bosquet de répit", P, ["arbre", "source"], why="des arbres et une source"),
"guardian-armor": TL("Armure gardienne", 2, ["armure", "transfert"], why="ton armure passe sur un allié"),
"hallucinogenic-smoke": CR("Fumée hallucinogène", P, ["fumée", "désorientation"], why="une fumée qui égare", aoe={"type": "cone", "size": 15}),
"hanspurs-flotsam-vessel": CR("Radeau d'épaves", P, ["radeau"], why="un radeau de bois flotté"),
"healing-flames": SO("Flammes guérisseuses", P, ["feu", "bienveillant", "hostile"], why="soigne le bienveillant, brûle l'hostile"),
"healing-token": SO("Jeton de soins", 1, ["symbole", "conduit"], why="un symbole par où passent les soins"),
"holy-javelin": CR("Javelot sacré", 3, ["javelot", "hostile"], why="un javelot qui ronge l'hostile"),
"hostile-juxtaposition": TL("Juxtaposition hostile", 3, ["échange", "lieu"], why="elle prend ta place quand on te frappe", options=[
    O("Juxtaposition hostile"), O("Juxtaposition hostile suprême", src_idx="hostile-juxtaposition-greater", qty_cible=P)]),
"ice-crystal-teleport": TL("Téléportation du cristal de glace", 3, ["glace", "téléportation"], why="gelée puis envoyée ailleurs"),
"ice-spears": CR("Lances de glace", P, ["glace", "lance"], why="des lances de glace jaillies du sol"),
"icicle-dagger": CR("Dague de glace", 1, ["dague", "glace"], why="une dague de glace"),
"infernal-healing": SO("Guérison infernale", 2, ["régénération", "hostile"], 1, "1 point par instant, une aura hostile", options=[
    O("Guérison infernale"), O("Guérison infernale suprême", src_idx="infernal-healing-greater", impact=(4, ["vie", "régénération", "hostile"], "4 points par instant"))]),
"inspiring-recovery": SO("Rétablissement inspirant", 2, ["retour", "vigueur"], why="les soins rappellent les morts et rendent la vigueur"),
"instant-armor": CR("Armure instantanée", 1, ["armure"], why="une armure à la place de tes habits"),
"instant-portrait": CR("Portrait instantané", 1, ["portrait"], why="un portrait sur la surface touchée"),
"instant-restoration": SO("Restauration instantanée", 2, ["invoqué"], why="un être invoqué soigné", cond=["invoqué"]),
"instant-weapon": CR("Arme instantanée", 1, ["arme"], why="une arme en main"),
"interplanetary-teleport": TL("Téléportation interplanétaire", 1, ["monde", "voyage"], why="vers un autre monde"),
"invigorating-repose": SO("Repos revigorant", 1, ["retour", "force"], why="tes rappels à la vie plus forts"),
"iron-stake": CR("Pieu de fer", 3, ["fer", "pieu"], why="un pieu de fer froid"),
"jannis-jaunt": TL("Voyage du génie", 2, ["plan", "élémentaire"], why="vers un plan élémentaire"),
"jesters-jaunt": TL("Saut du bouffon", 3, ["téléportation"], why="déplacée de quelques pas"),
"joyful-rapture": SO("Ravissement joyeux", P, ["émotion", "délivrance"], why="délivrés des émotions néfastes"),
"kings-castle": TL("Roque", 2, ["échange", "allié"], why="toi et un allié changés de place"),
"knell-of-the-depths": CU("Glas des profondeurs", 3, ["eau", "noyade"], why="coule à pic et suffoque"),
"leshy-swarm": CN("Nuée de léchys", P, ["plante", "esprit"], why="des esprits végétaux à ton aide"),
"life-current": SO("Courant de vie", P, ["courant"], why="un courant qui soigne", options=[
    O("Courant de vie"), O("Courant de nécrose", src_idx="unlife-current", impact=(P, ["nécrose", "courant"], "un courant qui blesse les vivants"))]),
"life-shield": GA("Bouclier de vie", 1, ["vie", "mort-vivant", "riposte"], why="les morts-vivants qui frappent sont brûlés"),
"light-of-iomedae": EP("Lumière de la Juste", VIS, P, ["lumière", "mort-vivant"], why="les morts-vivants illuminés et affaiblis"),
"litany-of-entanglement": CN("Litanie d'enchevêtrement", 3, ["entrave"], why="entravée un instant"),
"litany-of-escape": TL("Litanie d'évasion", 2, ["fuite", "étreinte"], why="tiré d'une étreinte"),
"mad-monkeys": CN("Singes fous", P, ["singe", "nuée"], why="une nuée de singes espiègles"),
"maddening-oubliette": TL("Oubliette démente", 3, ["prison", "plan"], why="jetée dans une geôle d'un plan d'horreur"),
"martyrs-last-blessing": SO("Dernière bénédiction du martyr", P, ["mort"], why="ta mort soigne alentour"),
"masters-escape": TL("Fuite du maître", 1, ["invoqué", "échange"], why="changer de place avec ton invoqué"),
"maw-of-chaos": EP("Gueule astrale", NE, P, ["déchirure"], why="une déchirure qui ravage", options=[O(f"Gueule astrale {ef}", impact=(P, ["déchirure", e], f"une déchirure d'énergie {ef}")) for e, ef in ASTR]),
"mighty-fist-of-the-earth": CR("Poing de la terre", 3, ["roche", "poing"], 4, "un caillou lancé"),
"murderous-crow": CN("Corbeau meurtrier", 1, ["corbeau", "garde"], why="un corbeau cruel qui veille"),
"music-of-the-spheres": SO("Musique des sphères", P, ["musique", "résistance"], why="régénération et résistance"),
"nauseating-dart": CR("Dard nauséeux", 3, ["dard", "nausée"], why="un dard qui écœure"),
"nauseating-trail": CR("Traînée nauséabonde", 3, ["nuage", "trace"], why="elle laisse un nuage puant"),
"pellet-blast": CR("Mitraille", P, ["métal", "explosion"], why="une gerbe de billes de métal"),
"pernicious-pranksters": CN("Farceurs pernicieux", P, ["fée", "farce"], why="des fées qui harcèlent tes ennemis"),
"phantom-chariot": CR("Char fantôme", P, ["char", "cheval"], why="un char et quatre chevaux"),
"phantom-driver": CR("Cocher fantôme", 1, ["cocher"], why="un fantôme qui conduit"),
"phase-step": TL("Pas de phase", 2, ["porte", "téléportation"], why="un court saut pour elle"),
"pick-your-poison": SO("Poison changé", 2, ["poison", "vin"], why="un poison changé en alcool"),
"pillar-of-life": SO("Pilier de vie", P, ["pilier"], 29, "2d8 + 1 par niveau à qui le touche"),
"planar-inquiry": CN("Enquête planaire", 9, ["extérieur", "réponse"], why="un être d'ailleurs vient répondre"),
"planar-refuge": EP("Refuge planaire", V("ordre"), P, ["plan", "loi"], why="les lois de ton monde imposées ailleurs"),
"pocketful-of-vipers": CN("Poche de vipères", 1, ["vipère", "piège"], why="des vipères gardent un contenant", cible_obj=["contenant"]),
"poisonous-balm": SO("Baume empoisonné", 2, ["poison", "latence"], 19, "soins, et un venin qui attend"),
"poisonous-cloud": CR("Nuage empoisonné", P, ["brume", "poison"], why="une brume mortelle"),
"rain-of-arrows": CR("Pluie de flèches", P, ["trait", "nuée"], why="un nuage de flèches"),
"rain-of-frogs": CN("Pluie de grenouilles", P, ["grenouille", "poison"], why="une nuée de grenouilles venimeuses"),
"rampart": CR("Rempart", P, ["terre", "rempart"], why="un épais rempart de terre"),
"release-the-hounds": CN("Lâcher les chiens", P, ["loup", "nuée"], why="une meute de loups"),
"reloading-hands": CN("Mains du rechargement", 1, ["projectile", "chargement"], why="ton arme rechargée d'elle-même"),
"remove-sickness": SO("Malaise ôté", 2, ["maladie", "nausée"], why="maladie et nausée suspendues"),
"resplendent-mansion": CR("Manoir resplendissant", P, ["manoir"], why="un manoir de plusieurs étages"),
"restful-cloak": CR("Cape reposante", 1, ["cape", "abri"], why="une cape qui fait office de tente", cible_obj=["cape"]),
"resurgent-transformation": SO("Transformation résurgente", 1, ["souffle", "sursaut"], why="un second souffle au bord de la mort"),
"retrieve-item": TL("Objet rappelé", 1, ["objet", "appel"], why="un petit objet rappelé en main"),
"returning-weapon": TL("Arme qui revient", 1, ["arme", "retour"], why="l'arme lancée revient", cible_obj=["arme"],
    options=[O("Arme qui revient"), O("Armes qui reviennent", src_idx="returning-weapon-communal", qty_cible=P)]),
"rising-water": CR("Eau montante", P, ["eau", "pilier"], why="un pilier d'eau"),
"river-whip": CR("Fouet de rivière", 1, ["fouet", "eau"], why="un fouet d'eau douce"),
"rock-whip": CR("Fouet de roche", 1, ["fouet", "roche"], why="un fouet qui traverse la pierre"),
"sacred-bond": SO("Lien sacré", 2, ["lien", "distance"], why="tes soins de contact portés au loin"),
"sand-whirlwind": CR("Tourbillon de sable", 3, ["sable", "vue"], why="du sable qui gêne", options=[
    O("Tourbillon de sable"), O("Tourbillon de sable suprême", src_idx="sand-whirlwind-greater", cible=P, impact=(P, ["sable", "vue", "cécité"], "aveuglant"))]),
"sealed-sending": TL("Envoi scellé", 1, ["message", "parchemin"], why="un parchemin envoyé vers un lieu connu"),
"seamantle": GA("Manteau marin", 1, ["eau", "garde"], why="enveloppé d'eau protectrice"),
"secluded-grimoire": TL("Grimoire reclus", 1, ["livre", "éthéré"], why="ton grimoire caché sur l'éthéré", cible_obj=["livre"]),
"second-wind": SO("Second souffle", 1, ["agonie"], why="un peu de vie au plus bas"),
"shackle": CR("Menottes", 3, ["menotte"], why="des menottes à ses poignets"),
"shadow-invasion": EP("Invasion astrale", NVIS, P, ["ombre"], why="une zone qui renforce l'énergie astrale", options=[O(f"Invasion {ef}", impact=(P, [e, "renfort"], f"l'énergie {ef} renforcée")) for e, ef in ASTR]),
"signifers-rally": TL("Ralliement", P, ["allié", "rappel"], why="tes alliés ramenés à toi"),
"silver-darts": CR("Dards d'argent", P, ["argent", "dard"], 39, "1d6 par niveau", aoe={"type": "cone", "size": 30}),
"slick-walls": CR("Murs glissants", P, ["mur", "glissant"], why="des murs impossibles à grimper"),
"slipstream": CR("Courant porteur", 2, ["eau", "vitesse"], why="une vague qui porte plus vite"),
"slowing-mud": CR("Boue ralentissante", 3, ["boue", "lenteur", "cécité"], why="couverts de boue, aveugles et lents"),
"soothing-mud": SO("Boue apaisante", 2, ["boue"], why="une boue qui soigne corps et facultés"),
"solid-note": CR("Note solide", 1, ["note", "musique"], why="une note de musique tangible"),
"songbird": CR("Oiseau chanteur", P, ["musique", "bienveillant"], why="une musique venue d'un plan bienveillant"),
"soul-transfer": CN("Transfert d'âme", 1, ["âme", "réceptacle"], why="une âme passée d'un réceptacle à l'autre"),
"spectral-scout": CR("Éclaireur spectral", 1, ["bête", "éclaireur"], why="un animal spectral qui éclaire ta route"),
"spiral-ascent": TL("Spirale", 1, ["vertical"], why="téléporté droit vers le haut", options=[
    O("Spirale ascendante"), O("Spirale descendante", src_idx="spiral-descent", impact=(P, ["vertical", "descente"], "téléporté droit vers le bas"))]),
"spore-burst": CR("Explosion de spores", 2, ["spore", "poison"], why="une plante qui crache des spores", cond=["plante"]),
"stabilize": SO("Stabilisation", 2, ["agonie", "arrêt"], why="un mourant stabilisé", cond=["mourant"]),
"stone-call": CR("Appel des pierres", P, ["pierre", "pluie"], 7, "2d6 en moyenne"),
"stone-discus": CR("Disque de pierre", 3, ["pierre", "disque"], why="un disque volant"),
"stone-shield": GA("Bouclier de pierre", 1, ["pierre", "dalle"], why="une dalle jaillie du sol"),
"storm-of-blades": CR("Tempête de lames", 3, ["épée", "lancer"], why="des épées lancées"),
"storm-step": TL("Pas d'orage", 1, ["foudre", "saut"], why="un saut de foudre qui blesse au passage"),
"straitjacket": CR("Camisole", 3, ["entrave", "bras"], why="les bras liés, l'esprit délivré"),
"stumble-gap": CR("Trou piège", P, ["trou", "chute"], why="un petit trou qui fait trébucher"),
"summon-ancestral-guardian": CN("Gardien ancestral", 1, ["ancêtre", "esprit"], why="les esprits des ancêtres combattent"),
"summon-elder-worm": CN("Convocation du ver ancien", P, ["ver", "géant"], why="un ver pourpre géant"),
"summon-flight-of-eagles": CN("Envol d'aigles", P, ["aigle", "monture"], why="des aigles géants"),
"summon-froghemoth": CN("Convocation du crapaud-léviathan", P, ["batracien", "géant"], why="un monstre des marais"),
"summon-giant-ally-i": CN("Allié géant", 1, ["géant"], why="un géant à ton aide", options=[
    O(f"Allié géant {r}", src_idx=f"summon-giant-ally-{r.lower()}", impact=(P, ["géant", w], d)) for r, w, d in [("I", "colline", "géant des collines, des cavernes, des pierres…"), ("II", "feu", "géant du feu, du givre, du désert…"), ("III", "nuage", "géant des nuages ou des cendres")]]),
"summon-infernal-host": CN("Légion infernale", P, ["fiélon", "légion"], why="une légion de fiélons", cond=["hostile"]),
"summon-minor-ally": CN("Convocation d'alliés mineurs", P, ["bête", "petit"], why="un à trois petits animaux", options=[
    O("Alliés mineurs"), O("Monstres mineurs", src_idx="summon-minor-monster", impact=(P, ["être", "petit"], "un à trois petits êtres"))]),
"summon-ship": CR("Navire", P, ["navire"], why="un navire tiré d'ailleurs"),
"summon-stampede": CN("Débandade", P, ["aurochs", "piétinement"], why="un troupeau qui piétine"),
"summon-totem-creature-shoanti": CN("Animal totem", 1, ["bête", "totem"], why="les bêtes sacrées de ton clan"),
"surface-excursion": TL("Excursion en surface", P, ["surface", "retour"], why="remontés à la surface un temps"),
"swarm-of-fangs": CN("Nuée de crocs", P, ["croc", "nuée"], why="des dents volantes"),
"swipe": TL("Larcin", 3, ["objet", "vol"], why="un objet arraché à distance"),
"sylvan-hideaway": CR("Cachette sylvestre", P, ["abri", "secret"], why="une cachette extradimensionnelle"),
"symbol-of-healing": SYMP("Symbole de guérison", verb=HE, impact=(P, ["vie"], "les vivants soignés")),
"temporal-regression": TL("Régression temporelle", 1, ["temps", "balise"], why="revenir à un instant marqué"),
"thorn-javelin": CR("Javelot d'épines", 1, ["javelot", "épine", "nausée"], why="un javelot qui écœure"),
"tidal-surge": CR("Raz de marée", P, ["eau", "vague", "extinction"], why="une vague qui frappe et éteint"),
"touch-of-slime": CR("Toucher de vase", 3, ["vase", "infestation"], why="infestée de vase verte"),
"trade-items": TL("Échange d'objets", 1, ["objet", "échange"], why="ton objet contre le sien"),
"uncanny-reminder": CR("Rappel étrange", 3, ["double", "meurtre"], why="un double qui veut sa mort"),
"unleash-pandemonium": CR("Pandémonium déchaîné", P, ["vent", "chaos"], why="les vents sauvages d'un plan maudit"),
"unseen-crew": CR("Équipage invisible", P, ["équipage", "invisible"], why="des matelots invisibles"),
"urban-step": TL("Pas urbain", 1, ["porte"], why="entrer par une porte, sortir par une autre"),
"vine-strike": CR("Frappe de lianes", 1, ["liane", "épine"], why="des coups armés de lianes"),
"vinetrap": CR("Piège de lianes", 3, ["liane", "étranglement"], why="des lianes qui étouffent"),
"vomit-swarm": CN("Nuée vomie", P, ["araignée", "nuée"], why="tu vomis une nuée d'araignées"),
"walk-through-space": TL("Marche dans l'espace", 1, ["saut", "répétition"], why="de petits sauts sans fin"),
"wall-of-brine": CR("Mur de saumure", P, ["mur", "eau", "courant"], why="un mur d'eau de mer"),
"wall-of-clockwork": CR("Mur d'engrenages", P, ["mur", "engrenage"], why="un mur de rouages"),
"wall-of-lava": CR("Mur de lave", P, ["mur", "lave"], why="un mur de lave qui crache"),
"wall-of-mist": CR("Mur de brume", P, ["mur", "brume"], why="un mur de brume"),
"waters-of-lamashtu": CR("Eaux trompeuses", 1, ["poison", "eau"], why="un poison qui a l'air d'eau pure"),
"waves-of-blood": CR("Vagues de sang", P, ["sang", "vague", "nausée"], why="une vague de sang", aoe={"type": "cone", "size": 30}),
"web-shelter": CR("Abri de toile", P, ["toile", "abri"], why="un abri de toile"),
"whip-of-spiders": CN("Fouet d'araignées", 1, ["fouet", "araignée"], why="un fouet d'araignées venimeuses", options=[
    O("Fouet d'araignées"), O("Fouet de mille-pattes", src_idx="whip-of-centipedes", impact=(P, ["fouet", "mille-pattes"], "un fouet de mille-pattes")),
    O("Fouet de fourmis", src_idx="whip-of-ants", impact=(P, ["fouet", "fourmi"], "un fouet de fourmis guerrières"))]),
"wicker-horse": CR("Cheval d'osier", P, ["monture", "plante"], why="une monture de végétaux"),
"wing-bounty": CR("Ailes fructueuses", 1, ["aile", "baie"], why="des baies poussent sur tes ailes"),
"winter-grasp": CR("Étreinte de l'hiver", P, ["glace", "glissant"], why="une glace glissante"),
"wooden-phalanx": CR("Phalange de bois", P, ["bois", "golem"], why="des golems de bois"),
"word-of-beckoning": TL("Parole d'appel", 1, ["message", "téléportation"], why="un message, et le moyen de te rejoindre"),
}
FICHES.update(NEWPF_CONJ)
PFV("Conjuration")
ADDPF("grease", O("Graisse suprême", src_idx="grease-greater"))
ADDPF("delay-poison", O("Poison retardé partagé", src_idx="delay-poison-communal", qty_cible=P))
ADDPF("mount", O("Monture partagée", src_idx="mount-communal", qty_cible=P))
ADDPF("phantom-steed", O("Coursier fantôme partagé", src_idx="phantom-steed-communal", qty_cible=P))
ADDPF("instant-summons", O("Convocation instantanée suprême", src_idx="instant-summons-greater"))
ADDPF("secret-chest", O("Coffret secret", src_idx="secret-coffer"), O("Chambre forte secrète", src_idx="secret-vault"))
ADDPF("raise-dead", O("Rappel du compagnon", src_idx="raise-animal-companion", cond=["compagnon"]))
for k, pre in [("summon-monster-i", "summon-monster"), ("summon-natures-ally-i", "summon-natures-ally")]:
    FICHES[k]["vpf"] = dict(src_idx=f"{pre}-1", options=[dict(o, src_idx=f"{pre}-{ROM.index(o['src_idx'].rsplit('-', 1)[1].upper()) + 1}") for o in FICHES[k]["options"]])
ADDPF("lesser-restoration", O("Poison — suprême", src_idx="neutralize-poison-greater", impact=(P, ["poison", "certitude"], "tout poison neutralisé à coup sûr")))
FICHES.update({
"mudball": CR("Boule de boue", 3, ["boue", "cécité"], why="de la boue dans les yeux"),
"path-of-glory": SO("Chemin de gloire", P, ["lueur", "extension"], 1, "1 point par instant aux alliés dans la lueur", options=[
    O("Chemin de gloire"), O("Chemin de gloire suprême", src_idx="path-of-glory-greater", impact=(5, ["vie", "lueur", "extension"], "5 points par instant"))]),
})

# --- Pathfinder 1, lot 8 : Transmutation (1/3) ---
PF1_RELECTURE.update({
"allegro": f"s'appuie sur la « représentation bardique » : {_cls}",
"delayed-consumption": f"retarde un « extrait » d'alchimiste : {_cls}",
"bestow-grace-of-the-champion": f"accorde les pouvoirs du paladin : {_cls}",
"blade-of-bright-victory": f"repose sur l'« arme liée » du paladin : {_cls}",
"blade-of-dark-triumph": f"repose sur l'« arme liée » de l'antipaladin : {_cls}",
"blessed-fist": "évite les « attaques d'opportunité » : pure mécanique de jeu",
"borrow-skill": "emprunte des « rangs de compétence » : pure mécanique de jeu",
"bouncing-bomb-admixture": f"modifie les « bombes » de l'alchimiste : {_cls}",
"contest-of-skill": "empêche de « confirmer les critiques » : pure mécanique de jeu",
"defensive-grace": f"repose sur l'« inspiration » de l'enquêteur : {_cls}",
"devolution": f"repose sur l'eidolon du conjurateur : {_cls}",
"evolution-surge": f"repose sur l'eidolon du conjurateur : {_cls}",
"evolution-surge-lesser": f"repose sur l'eidolon du conjurateur : {_cls}",
"evolution-surge-greater": f"repose sur l'eidolon du conjurateur : {_cls}",
"dwarven-veil": "rend plus influent auprès des nains : dépend des peuples de Golarion",
})
TR = V("nature")
TM = lambda fr, cible, words, v=None, why="", **kw: EP(fr, TR, cible, words, v, why, **kw)
EN = lambda fr, cible, words, v=None, why="", **kw: EP(fr, INT, cible, words, v, why, **kw)
MV = lambda fr, cible, words, v=None, why="", **kw: EP(fr, TP, cible, words, v, why, **kw)
SH = lambda fr, cible, words, v=None, why="", **kw: EP(fr, ID, cible, words, v, why, **kw)
NEWPF_TRA1 = {
"aboleths-lung": TM("Poumon des profondeurs", 3, ["souffle", "eau", "air"], why="respire l'eau, plus l'air"),
"absorbing-inhalation": TM("Inspiration absorbante", 1, ["nuage", "souffle"], why="un nuage avalé et gardé"),
"absorbing-touch": TM("Toucher absorbant", 1, ["objet", "absorption"], why="un objet absorbé dans ton corps", cible_obj=["objet"]),
"abstemiousness": TM("Frugalité", 1, ["nourriture", "satiété"], why="un peu de nourriture qui rassasie"),
"accelerate-poison": TM("Poison accéléré", 3, ["poison", "vitesse"], why="le poison agit tout de suite"),
"acid-maw": EN("Gueule acide", 2, ["croc", "acide"], why="la morsure de ton compagnon chargée d'acide", cond=["compagnon"]),
"acute-senses": EN("Sens aiguisés", 2, ["perception"], why="des sens plus fins"),
"adhesive-blood": TM("Sang adhésif", 1, ["sang", "colle"], why="les armes collent à ton sang"),
"adjustable-polymorph": SH("Métamorphose ajustable", 1, ["forme", "changement"], why="changer de forme à volonté"),
"adroit-retrieval": EN("Prise adroite", 2, ["objet", "vitesse"], why="tirer ses affaires en un éclair"),
"age-resistance-lesser": EN("Résistance à l'âge", 1, ["âge"], why="les maux de l'âge ignorés", options=[
    O("Résistance à l'âge mineure"), O("Résistance à l'âge", src_idx="age-resistance", impact=(P, ["âge", "vieillesse"], "ceux de la vieillesse")),
    O("Résistance à l'âge suprême", src_idx="age-resistance-greater", impact=(P, ["âge", "grand âge"], "ceux du grand âge"))]),
"air-breathing": TM("Respiration aérienne", P, ["souffle", "air"], why="les êtres des eaux respirent l'air"),
"air-step": MV("Pas sur l'air", 1, ["air", "marche"], why="marcher sur l'air, mal assuré"),
"alchemical-allocation": EN("Allocation alchimique", 1, ["potion", "effet"], why="l'effet d'une potion sans la boire"),
"alchemical-tinkering": TM("Bricolage alchimique", 1, ["objet", "transformation"], why="un objet alchimique changé en un autre", cible_obj=["objet"]),
"aldori-alacrity": EN("Alacrité du duelliste", 1, ["vitesse", "esquive"], why="plus vif, plus esquivant"),
"allfood": TM("Tout-nourriture", 1, ["objet", "nourriture"], why="un objet changé en nourriture", cible_obj=["objet"]),
"alter-river": TM("Cours détourné", P, ["rivière", "courant"], why="le cours d'une rivière changé"),
"alter-winds": TM("Vents altérés", P, ["vent"], why="le vent forci ou calmé"),
"amplify-elixir": EN("Élixir amplifié", 1, ["potion", "puissance"], why="une potion plus forte ou plus longue"),
"anchored-step": TM("Pas ancré", 1, ["liane", "équilibre"], why="des lianes sous tes pieds, sûres mais lentes"),
"angelic-aspect-lesser": SH("Aspect angélique", 1, ["ange", "aspect"], why="un peu de la nature angélique", options=[
    O("Aspect angélique mineur"), O("Aspect angélique", src_idx="angelic-aspect", impact=(P, ["ange", "aspect", "aile"], "davantage, et des ailes")),
    O("Aspect angélique suprême", src_idx="angelic-aspect-greater", impact=(P, ["ange", "aspect", "aile", "gloire"], "la pleine nature angélique"))]),
"animal-aspect": SH("Aspect animal", 1, ["bête", "aspect"], why="une qualité d'animal", options=[
    O("Aspect animal"), O("Aspect animal suprême", src_idx="animal-aspect-greater", impact=(2, ["bête", "aspect"], "deux qualités d'animal"))]),
"ant-haul": EN("Force de fourmi", 2, ["charge"], 3, "porte trois fois plus", options=[O("Force de fourmi"), O("Force de fourmi partagée", src_idx="ant-haul-communal", qty_cible=P)]),
"anthropomorphic-animal": SH("Animal anthropomorphe", 2, ["bête", "bipède"], why="un animal debout comme un homme", cond=["bête"]),
"ape-walk": EN("Marche du singe", 2, ["escalade"], why="grimper comme un singe"),
"arboreal-hammer": TM("Marteau arboricole", P, ["arbre", "branche"], why="les branches frappent tes ennemis"),
"arodens-magic-army": EN("Armée enchantée", P, ["arme", "magie"], why="toutes les armes alentour enchantées"),
"arodens-spellsword": TM("Épée-bâton", 1, ["arme", "bâton", "fusion"], why="une arme fondue avec un bâton magique"),
"artificers-curse": CU("Malédiction de l'artificier", 1, ["objet", "magie", "suspension"], why="les meilleurs pouvoirs d'un objet éteints", cible_obj=["objet"]),
"aspect-of-the-bear": EN("Aspect de l'ours", 1, ["garde", "force"], 2, "2 ajouté à la défense et à la lutte"),
"aspect-of-the-falcon": EN("Aspect du faucon", 1, ["vue", "trait"], why="l'œil et la visée du faucon"),
"aspect-of-the-nightingale": EN("Aspect du rossignol", 1, ["voix"], why="une voix claire et douce"),
"aspect-of-the-stag": EN("Aspect du cerf", 1, ["vitesse", "esquive"], why="la vitesse et l'esquive du cerf"),
"aspect-of-the-wolf": EN("Aspect du loup", 1, ["force", "adresse", "chute"], 4, "4 ajouté en force et adresse, plus apte à faire tomber"),
"assume-appearance": SH("Apparence empruntée", 1, ["cadavre", "apparence"], why="prendre l'allure d'un mort"),
"atavism": EN("Atavisme", 2, ["bête", "vigueur"], why="un animal plus puissant", cond=["bête"], options=[O("Atavisme"), O("Atavisme de groupe", src_idx="atavism-mass", qty_cible=P)]),
"badgers-ferocity": EN("Férocité du blaireau", P, ["arme", "tranchant"], why="des armes affûtées tant que tu te concentres"),
"baphomets-blessing": SH("Tête de taureau", 2, ["tête", "taureau"], why="une tête de taureau"),
"beast-shape-i": SH("Forme bestiale", 1, ["bête", "forme"], why="la forme d'un animal", options=[
    O(f"Forme bestiale {r}", src_idx=f"beast-shape-{r.lower()}", impact=(P, ["bête", "forme"] + x, d)) for r, x, d in [
    ("I", [], "un animal petit ou moyen"), ("II", ["taille"], "un animal minuscule ou grand"), ("III", ["taille", "créature"], "un animal énorme ou une créature magique"), ("IV", ["taille", "créature", "pouvoir"], "et davantage de pouvoirs")]]),
"billowing-skirt": TM("Jupe gonflée", 1, ["vêtement", "chute"], why="une jupe qui freine la chute"),
"binding-earth": TM("Terre liante", 3, ["terre", "entrave"], why="la terre la tire vers le bas", options=[O("Terre liante"), O("Terre liante de groupe", src_idx="binding-earth-mass", qty_cible=P)]),
"blade-lash": EN("Lame fouet", 1, ["arme", "fouet", "chute"], why="l'arme frappe comme un fouet"),
"blade-of-light": EN("Lame de lumière", 1, ["arme", "soleil", "mort-vivant"], why="une arme chargée de soleil, fléau des morts", cible_obj=["arme"]),
"bladed-dash": MV("Ruée tranchante", 1, ["élan", "coup"], why="une ruée qui frappe au passage", options=[
    O("Ruée tranchante"), O("Ruée tranchante suprême", src_idx="bladed-dash-greater", impact=(P, ["élan", "coup", "tous"], "frappe tous ceux qu'elle croise"))]),
"blast-barrier": TM("Barrière de terre", P, ["terre", "mur"], why="un mur de terre instable"),
"blessing-of-fervor": EN("Bénédiction de ferveur", P, ["ferveur", "choix"], why="chacun choisit son élan"),
"blessing-of-the-mole": EN("Bénédiction de la taupe", P, ["vue", "ténèbres", "discrétion"], why="voir dans le noir et passer inaperçu"),
"blessing-of-the-salamander": EN("Bénédiction de la salamandre", 2, ["régénération", "feu"], why="régénère et ne craint pas le feu"),
"blood-armor": TM("Armure de sang", 1, ["sang", "garde"], why="ton sang durcit quand tu saignes"),
"blood-sentinel": TM("Sentinelle de sang", 1, ["sculpture", "compagnon"], why="une sculpture animale devenue familier"),
"bloodhound": EN("Limier", 1, ["odorat"], why="le flair d'un chien"),
"body-capacitance": TM("Capacité du corps", 1, ["foudre", "stockage"], why="la foudre reçue gardée puis rendue"),
"boiling-blood": EP("Sang ardent", NE, 3, ["sang", "feu"], why="le sang bouillonne et brûle"),
"bombers-eye": EN("Œil du lanceur", 1, ["lancer", "portée"], why="tes lancers vont plus loin"),
"bone-flense": EP("Écorchure des os", NE, 3, ["os", "sang"], why="ses os jaillissent en pointes"),
"bowstaff": TM("Arc-bâton", 1, ["arc", "bâton"], why="un arc qui sert de bâton", cible_obj=["arc"]),
"brand": CU("Marque au fer", 3, ["marque"], why="une marque à vie", options=[
    O("Marque au fer"), O("Marque au fer suprême", src_idx="brand-greater", impact=(P, ["marque", "lueur"], "qui luit près de ton symbole")),
    O("Marque du conformisme", src_idx="brand-of-conformity", impact=(P, ["marque", "langue"], "qui lui ôte ses langues")),
    O("Marque de l'entrave", src_idx="brand-of-hobbling", impact=(P, ["marque", "boiterie"], "qui l'estropie")),
    O("Marque de pistage", src_idx="brand-of-tracking", impact=(P, ["marque", "piste"], "qui te mène à elle"))]),
"break": TM("Brisure", 1, ["objet", "fêlure"], why="un objet abîmé", cible_obj=["objet"]),
"bristle": TM("Hérissement", 1, ["peau", "croc"], why="ta peau durcie se fait arme"),
"brittle-portal": TM("Portail fragile", P, ["objet", "fragilité"], why="les objets moins solides"),
"buoyancy": TM("Flottabilité", P, ["eau", "flottaison"], why="flotter sans peine"),
"burning-disarm": TM("Désarmement brûlant", 1, ["métal", "feu", "lâcher"], why="le métal rougit, il faut lâcher", cible_obj=["objet"]),
"burrow": MV("Fouissement", 2, ["terre", "creuser"], why="creuser la terre"),
"burst-of-adrenaline": EN("Sursaut d'adrénaline", 1, ["force", "fatigue"], 8, "un sursaut de corps, puis la fatigue"),
"burst-of-insight": EN("Éclair de lucidité", 1, ["esprit", "hébétude"], 8, "un sursaut d'esprit, puis l'hébétude"),
"burst-of-speed": MV("Pointe de vitesse", 1, ["vitesse", "passage"], why="filer entre les ennemis"),
"calcific-touch": EP("Toucher calcifiant", NE, 3, ["calcaire", "lenteur"], why="raidie, ralentie, malhabile"),
"call-weapon": MV("Arme appelée", 1, ["arme", "appel"], why="l'arme d'un autre vient à toi"),
"carry-companion": SH("Compagnon de poche", 2, ["compagnon", "pierre", "réduction"], why="ton compagnon réduit en figurine de pierre", cond=["compagnon"]),
"carve-passage": TM("Passage taillé", P, ["terre", "passage"], why="un passage dégagé dans la terre ou la glace"),
"caustic-blood": TM("Sang caustique", 1, ["sang", "acide"], why="qui te blesse est brûlé par ton sang"),
"cauterizing-weapon": EN("Arme cautérisante", 1, ["arme", "régénération"], why="une arme qui empêche de se régénérer", cible_obj=["arme"]),
"certain-grip": EN("Poigne assurée", 1, ["prise", "équilibre", "désarmement"], 4, "prise et équilibre assurés"),
"channel-vigor": EN("Vigueur canalisée", 1, ["vigueur", "corps"], why="ta vigueur dans une partie du corps"),
"charge-object": TM("Objet chargé", 1, ["objet", "empreinte"], why="une histoire inscrite dans un objet", cible_obj=["objet"]),
"cheetahs-sprint": MV("Course du guépard", 1, ["vitesse", "course"], why="une course fulgurante"),
"claim-identity": SH("Visage volé", 1, ["visage", "vol"], why="voler le visage d'un autre"),
"clear-grove": TM("Bosquet dégagé", P, ["plante", "dégagement"], why="la végétation écartée"),
"cloud-shape": SH("Forme de nuage", 1, ["nuage", "apparence"], why="l'allure d'un grand nuage"),
"codespeak": EP("Langue codée", REL, P, ["langue", "code"], why="une langue secrète partagée"),
"coin-shot": TM("Tir de pièces", 1, ["pièce", "projectile"], why="des pièces qui deviennent projectiles"),
"concealed-breath": EN("Souffle retenu", 1, ["souffle"], why="retenir son souffle sans mal"),
"condensed-ether": TM("Éther condensé", P, ["éthéré", "lenteur"], why="un éther lourd qui ralentit"),
"control-construct": EP("Maîtrise de l'artefact", REL, 3, ["artefact", "contrôle"], why="un artefact animé sous ta coupe", cond=["ARTEFACT"]),
"conversing-wind": EP("Vent de conversation", REL, P, ["vent", "message", "réponse"], why="un vent qui porte message et réponse"),
"countless-eyes": TM("Yeux innombrables", 1, ["œil", "vue"], why="des yeux tout autour"),
"crafters-fortune": EN("Fortune de l'artisan", 2, ["ouvrage"], 5, "un ouvrage mieux réussi", options=[
    O("Fortune de l'artisan"), O("Malédiction de l'artisan", src_idx="crafters-curse", cible=3, impact=(5, ["ouvrage", "maladresse"], "un ouvrage gâché"))]),
"create-holds": TM("Prises", P, ["prise", "paroi"], why="des prises dans la paroi"),
"crimson-breath": TM("Souffle cramoisi", 3, ["poison", "crachat"], why="un crachat de poison"),
"crusaders-edge": EN("Fil du croisé", 1, ["arme", "extérieur", "hostile"], why="une arme fléau des êtres d'ailleurs hostiles", cible_obj=["arme"]),
"cup-of-dust": EP("Coupe de poussière", NE, 3, ["soif", "déshydratation"], why="desséchée"),
"curse-of-burning-sleep": CU("Malédiction du sommeil brûlant", 3, ["sommeil", "feu"], why="prend feu en dormant"),
"dance-of-a-hundred-cuts": EN("Danse des cent coupures", 1, ["danse", "coup"], why="ta lame danse", options=[
    O("Danse des cent coupures"), O("Danse des mille coupures", src_idx="dance-of-a-thousand-cuts", impact=(P, ["danse", "coup", "vitesse"], "et la célérité"))]),
"damp-powder": TM("Poudre mouillée", 1, ["poudre", "munition"], why="ses munitions gâchées"),
"dancing-lantern": TM("Lanterne dansante", 1, ["lanterne", "suivre"], why="une lanterne qui te suit", cible_obj=["lanterne"]),
"deft-digits": TM("Doigts habiles", 1, ["gant", "animation"], why="un gant animé à distance", cible_obj=["gant"]),
"delectable-flesh": CU("Chair délectable", 3, ["chair", "faim"], why="si appétissante qu'on veut la dévorer"),
"destabilize-powder": TM("Poudre instable", 1, ["poudre", "raté"], why="son arme à poudre rate"),
"detoxify": TM("Désintoxication", 3, ["poison", "privation"], why="privée de son venin"),
"dimensional-blade": TM("Lame dimensionnelle", 1, ["arme", "plat"], why="une lame sans épaisseur qui passe les armures", cible_obj=["arme"]),
"diminish-resistance": CU("Résistance amoindrie", 3, ["résistance", "énergie"], why="moins résistante à une énergie"),
"disable-construct": EP("Artefact paralysé", NINT, 3, ["artefact", "paralysie"], why="un artefact animé figé", cond=["ARTEFACT"]),
"disfiguring-touch": CU("Toucher défigurant", 3, ["visage", "difformité"], why="défigurée"),
"dissolution": TM("Dissolution", 1, ["objet", "néant"], why="un petit objet effacé", cible_obj=["objet"]),
"divine-arrow": EN("Flèche divine", 1, ["trait", "sacré"], why="un trait chargé d'énergie sacrée", cible_obj=["trait"]),
"divine-pursuit": MV("Poursuite divine", 1, ["proie", "mouvement"], why="te déplacer comme ta proie"),
"divine-vessel": SH("Vaisseau divin", 1, ["forme", "géant", "divin"], why="une forme immense venue d'ailleurs"),
"dongun-shapers-touch": TM("Toucher du façonneur", 1, ["matière", "forme"], why="la matière façonnée un temps", cible_obj=["objet"]),
"dragonvoice": EN("Voix du dragon", 1, ["voix", "dragon"], why="parler comme un dragon"),
"drain-poison": EP("Poison drainé", V("flux"), 3, ["poison", "arme"], why="son venin pris pour ton arme"),
"dust-form": SH("Forme de poussière", 1, ["poussière", "intangible"], why="devenir poussière intangible"),
"earth-tremor": TM("Secousse", P, ["terre", "chute"], why="le sol tremble et renverse"),
"echolocation": EN("Écholocation", 1, ["son", "perception"], why="percevoir par l'écho"),
"effortless-armor": EN("Armure légère", 1, ["armure", "aisance"], why="l'armure ne ralentit plus"),
"eldritch-conduit": EP("Conduit mystique", REL, 2, ["conduit", "sort", "zone"], why="lancer tes sorts de zone depuis un autre", options=[
    O("Conduit mystique"), O("Conduit mystique suprême", src_idx="eldritch-conduit-greater", qty_cible=P)]),
"elemental-body-i": SH("Corps élémentaire", 1, ["élémentaire", "forme"], why="la forme d'un élémentaire", options=[
    O(f"Corps élémentaire {r}", src_idx=f"elemental-body-{r.lower()}", impact=(P, ["élémentaire", "forme", t], f"un élémentaire {d}")) for r, t, d in [("I", "petit", "petit"), ("II", "moyen", "moyen"), ("III", "grand", "grand"), ("IV", "énorme", "énorme")]]),
"elemental-mastery": EN("Maîtrise élémentaire", 1, ["élément", "essence"], why="ton essence élémentaire maîtrisée"),
"elude-time": TM("Temps esquivé", 1, ["temps", "suspension"], why="suspendu hors du temps"),
"emblazon-crest": TM("Blason", 1, ["blason"], why="ton blason sur tout ce que tu portes"),
"emblem-of-greed": TM("Glaive ardent", 1, ["arme", "feu", "glaive"], why="une arme changée en glaive de feu", cible_obj=["arme"]),
"empower-holy-water": EN("Eau bénite renforcée", 1, ["eau", "mort-vivant"], why="une eau plus redoutable aux morts", cible_obj=["eau"]),
"enemy-hammer": MV("Marteau d'ennemi", 3, ["projection", "arme"], why="un ennemi manié comme une arme"),
"energy-hack": TM("Énergie détournée", 1, ["énergie", "sort"], why="tes sorts prennent l'énergie qui t'a frappé"),
"enhance-water": TM("Eau améliorée", 1, ["eau", "vin"], why="de l'eau changée en boisson", cible_obj=["eau"], options=[
    O("Eau améliorée"), O("Fermentation", src_idx="ferment", impact=(P, ["boisson", "alcool"], "un liquide qui fermente"))]),
"enlightened-step": MV("Pas éclairé", 1, ["air", "marche", "vol"], why="marcher sur l'air tout un jour"),
"enter-image": SH("Entrer dans l'image", 1, ["image", "conscience"], why="ta conscience dans ton portrait"),
"entomb": TM("Mise au tombeau", P, ["caveau", "terre"], why="un caveau souterrain inviolable"),
"erode-defenses": EP("Défenses rongées", NE, 3, ["peau", "garde"], why="sa peau et sa résistance rongées"),
"eroding-ray": EP("Rayon d'érosion", NE, 3, ["objet", "rayon"], 7, "2d6 aux objets et artefacts"),
"eruptive-pustules": TM("Pustules éruptives", 1, ["acide", "riposte"], why="des pustules d'acide qui éclatent"),
"ether-step": MV("Pas d'éther", 1, ["éthéré", "esquive"], why="un pas sur l'éthéré pour esquiver"),
"ethereal-fists": EN("Poings éthérés", 1, ["éthéré", "coup"], why="tes coups touchent l'éthéré"),
"excruciating-deformation": EP("Déformation atroce", NE, 3, ["corps", "difformité"], why="le corps tordu de douleur"),
"expeditious-excavation": TM("Excavation expéditive", P, ["terre", "creuser"], why="la terre déplacée"),
"extreme-flexibility": EN("Souplesse extrême", 1, ["souplesse"], why="souple au point de glisser de toute prise"),
"eyes-of-the-void": EN("Yeux du vide", 1, ["vue", "ténèbres"], why="voir même dans les ténèbres magiques"),
"fabricate-bullets": TM("Fabrication de balles", 1, ["métal", "balle"], why="du métal changé en munitions"),
"fabricate-disguise": TM("Déguisement fabriqué", 1, ["déguisement"], why="un déguisement en un instant"),
"face-of-the-devourer": CU("Visage du dévoreur", 3, ["visage", "gueule"], why="une gueule hideuse qui mord"),
"fair-is-foul": CU("Le beau est laid", 3, ["mutation", "difformité"], why="une mutation laide ou douloureuse"),
"false-age": SH("Âge trompeur", 1, ["âge", "apparence"], why="plus jeune ou plus vieux"),
"false-face": SH("Faux visage", 1, ["visage", "identité"], why="une autre identité"),
"fear-the-sun": CU("Crainte du soleil", 3, ["lumière", "aveuglement"], why="la lumière l'aveugle"),
"feast-of-ashes": CU("Festin de cendres", 3, ["faim"], why="une faim que rien n'apaise"),
"feather-step": MV("Pas de plume", 2, ["terrain", "aisance"], why="léger sur le mauvais terrain", options=[O("Pas de plume"), O("Pas de plume de groupe", src_idx="feather-step-mass", qty_cible=P)]),
}
FICHES.update(NEWPF_TRA1)

# --- Pathfinder 1, lot 8 : Transmutation (2/3) ---
PF1_RELECTURE.update({
"first-world-revisions": "déguise un wayang en gnome du Premier Monde : dépend des peuples de Golarion",
"flexible-fury": f"échange des « pouvoirs de rage » : {_cls}",
"honeyed-tongue": "fait garder le meilleur de deux jets : pure mécanique de jeu",
"hobbling-bomb-admixture": f"modifie les « bombes » de l'alchimiste : {_cls}",
"hunters-blessing": f"accorde « ennemi juré » et « terrain de prédilection » : {_cls}",
"hunters-friend": f"partage des « capacités de classe » : {_cls}",
"imbue-with-aura": f"transmet l'« aura » du prêtre : {_cls}",
"invoke-primal-power": f"renforce la « forme animale » du druide : {_cls}",
"ja-noi-aspect": "donne l'aspect d'un oni ja noi de Tian Xia, propre au monde de Golarion",
"kiss-of-the-first-world": "puise l'énergie du Premier Monde, plan propre à la cosmologie de Golarion",
"litany-of-warding": "multiplie les « attaques d'opportunité » : pure mécanique de jeu",
"lucky-number": "ajuste les jets de dé à venir : pure mécanique de jeu",
"mutagenic-touch": f"transmet le « mutagène » de l'alchimiste : {_cls}",
"orchids-drop": f"modifie le « mutagène » de l'alchimiste : {_cls}",
"open-arms": f"détourne le « défi » ou le « châtiment » : {_cls}",
"oracles-vessel": f"transmet la « malédiction d'oracle » : {_cls}",
"paragon-surge": "accorde un « don » au choix : pure mécanique de jeu",
"planned-assault": "renforce des « actions préparées » : pure mécanique de jeu",
})
SHAPE = lambda fr, base, w, rows: SH(fr, 1, [w, "forme"], why=f"la forme {base}", options=[
    O(f"{fr} {r}", src_idx=k, impact=(P, [w, "forme"] + x, d)) for r, k, x, d in rows])
NEWPF_TRA2 = {
"fey-form-i": SHAPE("Forme féerique", "d'une fée", "fée", [(r, f"fey-form-{r.lower()}", x, d) for r, x, d in [("I", [], "une fée petite ou moyenne"), ("II", ["taille"], "une fée minuscule ou grande"), ("III", ["taille", "énorme"], "une fée infime ou énorme"), ("IV", ["taille", "pouvoir"], "une fée puissante")]]),
"form-of-the-dragon-i": SHAPE("Forme draconique", "d'un dragon", "dragon", [(r, f"form-of-the-dragon-{r.lower()}", x, d) for r, x, d in [("I", [], "un dragon moyen"), ("II", ["grand"], "un grand dragon"), ("III", ["énorme"], "un dragon énorme")]]
    + [(f"exotique {r}", f"form-of-the-exotic-dragon-{r.lower()}", ["exotique"] + x, d) for r, x, d in [("I", [], "un dragon impérial ou primordial moyen"), ("II", ["grand"], "grand"), ("III", ["énorme"], "énorme")]]
    + [(f"étrange {r}", f"form-of-the-alien-dragon-{r.lower()}", ["étrange"] + x, d) for r, x, d in [("I", [], "un dragon ésotérique ou des confins, moyen"), ("II", ["grand"], "grand")]]),
"giant-form-i": SHAPE("Forme de géant", "d'un géant", "géant", [("I", "giant-form-i", ["grand"], "un grand géant"), ("II", "giant-form-ii", ["énorme"], "un géant énorme")]),
"monstrous-physique-i": SHAPE("Physique monstrueux", "d'un humanoïde monstrueux", "monstre", [(r, f"monstrous-physique-{r.lower()}", x, d) for r, x, d in [("I", [], "petit ou moyen"), ("II", ["taille"], "minuscule ou grand"), ("III", ["taille", "énorme"], "infime ou énorme"), ("IV", ["taille", "pouvoir"], "et plus de pouvoirs")]]),
"ooze-form-i": SHAPE("Forme de vase", "d'une vase", "vase", [(r, f"ooze-form-{r.lower()}", x, d) for r, x, d in [("I", [], "une vase petite ou moyenne"), ("II", ["grand"], "grande"), ("III", ["énorme"], "énorme")]]),
"plant-shape-i": SHAPE("Forme végétale", "d'une plante", "plante", [(r, f"plant-shape-{r.lower()}", x, d) for r, x, d in [("I", [], "une plante petite ou moyenne"), ("II", ["grand"], "grande"), ("III", ["énorme"], "énorme")]]),
"magical-beast-shape": SH("Forme de créature magique", 1, ["créature", "forme"], why="la forme d'une créature magique"),
"fickle-winds": TM("Vents capricieux", P, ["vent", "garde"], why="des murs de vent qui choisissent quoi arrêter"),
"fiery-body": SH("Corps de feu", 1, ["feu", "corps"], why="un corps de flammes"),
"film-of-filth": CU("Pellicule d'ordure", 3, ["bave", "puanteur"], why="une bave putride sur la peau"),
"fins-to-feet": SH("Nageoires en pieds", 2, ["jambe", "terre"], why="des jambes pour marcher"),
"fire-trail": TM("Traînée de feu", 1, ["feu", "trace"], why="une traînée de feu derrière toi"),
"firebrand": EN("Brandon", P, ["arme", "feu"], why="des armes enflammées, épargnées par ton feu"),
"firefall": TM("Chute de feu", P, ["feu", "éruption"], 7, "un feu qui jaillit"),
"flames-of-the-faithful": EN("Flammes des fidèles", 1, ["arme", "feu"], why="une arme qui flambe", cible_obj=["arme"]),
"flash-fire": TM("Feu éclair", 1, ["poudre", "éclair"], why="une arme à poudre qui aveugle d'un éclair"),
"fleeting-defect": TM("Défaut passager", 1, ["objet", "fêlure"], why="un objet ou un artefact pris en défaut", cible_obj=["objet"]),
"flesh-to-ooze": SH("Chair en vase", 3, ["vase", "chair"], why="changée en vase"),
"fleshcurdle": EP("Chair caillée", NE, 3, ["chair", "difformité"], why="sa chair tordue la gêne"),
"flexile-curse": CU("Malédiction de souplesse", 1, ["armure", "ramollissement"], why="armure et bouclier ramollissent", cible_obj=["armure"]),
"fluid-form": SH("Forme fluide", 1, ["eau", "corps"], why="un corps d'eau"),
"forced-quiet": CU("Silence forcé", 3, ["bruit", "silence"], why="ne peut faire de bruit"),
"fractions-of-heal-and-harm": EP("Part des soins et des maux", V("flux"), 1, ["vie", "blessure"], why="ton prochain sort blessant te soigne"),
"frightful-aspect": SH("Aspect terrifiant", 1, ["peur", "grand"], why="une forme grande et terrifiante"),
"frostbite": EP("Engelure", NE, 3, ["froid", "fatigue"], 5, "1d6 + 1 par niveau, fatiguée"),
"full-pouch": TM("Bourse pleine", 1, ["objet", "double"], why="un objet alchimique dédoublé", cible_obj=["objet"]),
"funereal-weapon": EN("Arme funéraire", 1, ["arme", "mort-vivant"], why="une arme qui mord les morts", cible_obj=["arme"]),
"fungal-blisters": TM("Cloques fongiques", 1, ["champignon", "riposte"], why="des champignons qui éclatent quand on te frappe"),
"fury-of-the-sun": CU("Fureur du soleil", 3, ["chaleur", "soleil"], why="un coup de chaleur intérieur"),
"geniekind": SH("Nature de génie", 1, ["génie", "pouvoir"], why="la force d'un génie"),
"ghost-brand": TM("Marque fantôme", 1, ["objet", "marque"], why="un objet changé en marque et de nouveau en objet", cible_obj=["objet"]),
"ghostbane-dirge": CU("Chant funèbre", 3, ["intangible", "solidité"], why="l'intangible touché par les armes communes", options=[O("Chant funèbre"), O("Chant funèbre de groupe", src_idx="ghostbane-dirge-mass", qty_cible=P)]),
"glide": MV("Plané", 1, ["chute", "planer"], why="planer sans se blesser"),
"golden-guise": TM("Parure d'or", 1, ["objet", "or"], why="un objet changé en or un temps", cible_obj=["objet"]),
"gorums-armor": TM("Armure hérissée", 1, ["armure", "pointe"], why="une armure hérissée de pointes", cible_obj=["armure"]),
"grappling-scarf": TM("Écharpe grappin", 1, ["écharpe", "corde"], why="une écharpe devenue grappin", cible_obj=["écharpe"]),
"gravity-bow": EN("Arc de gravité", 1, ["arc", "poids"], why="des traits plus lourds"),
"gravity-sphere": TM("Sphère de gravité", P, ["gravité"], why="la pesanteur changée"),
"gravity-well": TM("Puits de gravité", P, ["gravité", "poids"], why="la pesanteur accrue"),
"green-caress": SH("Caresse verte", 3, ["plante", "lenteur"], why="peu à peu changée en plante"),
"greensight": EN("Vue verte", 2, ["vue", "plante"], why="voir à travers les plantes"),
"groundswell": TM("Houle de terre", 1, ["terre", "élévation"], why="le sol se soulève sous toi"),
"hags-seasoning": CU("Assaisonnement de la sorcière", 3, ["odeur", "faim"], why="une odeur qui attire les affamés"),
"hairline-fractures": TM("Fissures", 1, ["pierre", "fissure"], why="la pierre fissurée", cible_obj=["pierre"]),
"hammer-of-mending": TM("Marteau de réparation", P, ["objet", "réparation"], why="une vague qui répare objets et artefacts"),
"handy-grapnel": TM("Grappin pratique", 1, ["corde", "grappin"], why="une corde devenue grappin", cible_obj=["corde"]),
"harmless-form": SH("Forme inoffensive", 3, ["bête", "petit"], why="changée en animal inoffensif"),
"heart-of-the-mammoth": EN("Cœur du mammouth", 2, ["force", "endurance"], why="la force du mammouth"),
"heart-of-the-metal": EN("Cœur du métal", P, ["arme", "métal"], why="des armes qui frappent comme le bon métal"),
"heavy-water": TM("Eau lourde", P, ["eau", "lourdeur"], why="une eau épaisse"),
"heightened-reflexes": EN("Réflexes aiguisés", P, ["réflexe"], 10, "un réflexe fulgurant"),
"hellmouth-lash": SH("Langue fouet", 1, ["langue", "fouet", "énergie"], why="ta langue changée en fouet d'énergie"),
"hidden-knowledge": TM("Savoir caché", 1, ["mémoire", "objet"], why="un souvenir changé en objet"),
"hidden-speech": EP("Parole cachée", NVIS, P, ["message", "secret"], why="des messages cachés dans la parole"),
"hidden-spring": TM("Source cachée", P, ["eau", "source"], why="une source d'eau douce"),
"hide-weapon": TM("Arme cachée", 1, ["arme", "bras"], why="une arme cachée dans ton bras"),
"hobble": CU("Pas entravé", 3, ["lenteur"], why="ralentie"),
"hollow-blades": CU("Lames creuses", 3, ["arme", "faiblesse"], why="ses armes frappent mollement"),
"holy-ice": TM("Glace bénite", P, ["glace"], why="un mur ou des javelots d'eau bénite gelée", options=[
    O("Glace bénite — lumineux", impact=(P, ["glace", "lumineux"], "eau chargée d'énergie lumineuse, gelée en mur ou en javelots")),
    O("Glace maudite — ténébreux", src_idx="unholy-ice", impact=(P, ["glace", "ténébreux"], "eau chargée d'énergie ténébreuse, gelée en mur ou en javelots"))]),
"holy-ice-weapon": TM("Arme de glace bénite", 1, ["arme", "glace"], why="une arme d'eau bénite gelée", options=[
    O("Arme de glace bénite — lumineux", impact=(P, ["arme", "glace", "lumineux"], "une arme d'eau lumineuse gelée")),
    O("Arme de glace maudite — ténébreux", src_idx="unholy-ice-weapon", impact=(P, ["arme", "glace", "ténébreux"], "une arme d'eau ténébreuse gelée"))]),
"hostile-levitation": EP("Lévitation hostile", TP, 3, ["lévitation"], why="soulevée du sol"),
"human-potential": EN("Potentiel humain", 2, ["faculté"], 2, "2 ajouté à une faculté", options=[O("Potentiel humain"), O("Potentiel humain de groupe", src_idx="human-potential-mass", qty_cible=P)]),
"hungry-earth": TM("Terre affamée", P, ["terre", "engloutissement"], why="la terre avale"),
"huntmasters-spear": EN("Lance du maître veneur", 1, ["lance", "proie"], why="une lance meurtrière pour une proie", cible_obj=["lance"]),
"ice-armor": TM("Armure de glace", 1, ["glace", "armure"], why="une épaisse armure de glace"),
"ice-body": SH("Corps de glace", 1, ["glace", "corps"], why="un corps de glace vivante"),
"infuse-self": SH("Nature d'ailleurs", 1, ["extérieur", "forme"], why="la forme d'un être d'ailleurs"),
"inheritors-smite": EN("Coup repoussant", 1, ["coup", "recul"], why="un coup qui repousse"),
"innocence": EN("Air innocent", 1, ["innocence"], why="paraître innocent"),
"innocuous-shape": EP("Gestes anodins", NVIS, 2, ["innocence", "geste"], why="ses actes paraissent anodins"),
"instrument-of-agony": EN("Instrument d'agonie", 1, ["arme", "intimidation"], why="une arme qui intimide", cible_obj=["arme"]),
"invigorating-poison": TM("Poison revigorant", 2, ["poison", "vigueur"], why="un poison qui fortifie"),
"iron-spine": EP("Échine de fer", NE, 3, ["os", "fer"], why="ses os changés en fer acéré"),
"ironbeard": TM("Barbe de fer", 1, ["barbe", "fer"], why="une barbe de fer qui garde et frappe"),
"ironbloom-sprouts": TM("Pousses de fleur de fer", 1, ["champignon", "fer"], why="des champignons magiques"),
"irregular-size": CU("Taille irrégulière", 3, ["membre", "atrophie"], why="un membre se ratatine"),
"jury-rig": TM("Réparation de fortune", 1, ["objet", "réparation"], why="un objet cassé qui marche", cible_obj=["objet"]),
"keen-senses": EN("Sens affûtés", 2, ["perception", "vue"], 2, "des sens plus fins"),
"kinetic-reverberation": TM("Réverbération cinétique", 1, ["force", "renvoi"], why="la force du coup revient dans l'arme"),
"lead-blades": EN("Lames de plomb", 1, ["arme", "poids"], why="des armes plus lourdes"),
"liberating-command": EP("Ordre libérateur", TP, 2, ["évasion"], why="elle se libère d'un coup"),
"life-channel": EP("Canal de vie", V("flux"), P, ["nécrose", "soins"], why="ceux de la nécrose soignés par elle"),
"lighten-object": TM("Objet allégé", 1, ["objet", "poids"], why="un objet deux fois plus léger", cible_obj=["objet"], options=[O("Objet allégé"), O("Objets allégés", src_idx="lighten-object-mass", qty_cible=P)]),
"lightning-conductor": TM("Paratonnerre", 1, ["foudre", "absorption"], why="la foudre absorbée et rendue"),
"lily-pad-stride": MV("Marche sur les nénuphars", 1, ["eau", "nénuphar"], why="marcher sur l'eau de feuille en feuille"),
"linebreaker": EN("Brise-ligne", 1, ["élan", "charge"], why="une charge qui renverse"),
"liquefy": TM("Liquéfaction", 1, ["objet", "liquide"], why="un objet changé en liquide", cible_obj=["objet"]),
"litany-of-defense": EN("Litanie de défense", 1, ["armure", "garde"], why="ton armure deux fois plus sûre"),
"litany-of-vengeance": CU("Litanie de vengeance", 3, ["vengeance", "faiblesse"], 5, "tes alliés la frappent plus fort"),
"lockjaw": EN("Mâchoire bloquée", 2, ["croc", "saisie"], why="une morsure qui ne lâche pas"),
"long-arm": SH("Bras long", 1, ["bras", "allonge"], why="des bras plus longs"),
"longshot": EN("Tir lointain", 1, ["trait", "portée"], why="tirer plus loin"),
"magnifying-chime": TM("Carillon amplificateur", 1, ["objet", "son"], why="un objet qui sonne de plus en plus fort", cible_obj=["objet"]),
"enter-image-majestic": None,
"malfunction": EP("Défaillance", NINT, 3, ["artefact", "trouble"], why="un artefact animé qui déraille", cond=["ARTEFACT"]),
"mantle-of-the-magic-warriors": EN("Manteau des guerriers mystiques", P, ["bête", "esprit"], why="des esprits animaux en chacun"),
"marching-chant": EN("Chant de marche", P, ["marche", "chant"], why="marcher vite sans fatigue"),
"marids-mastery": EN("Maîtrise des eaux", 2, ["eau", "coup"], why="plus fort dans l'eau, plus faible hors d'elle"),
"mark-of-blood": EP("Marque de sang", REL, 2, ["sang", "vie", "marque"], why="ta vie déposée en elle"),
"mark-of-buoyancy": TM("Marque d'apesanteur", 1, ["objet", "poids"], why="un objet sans poids", cible_obj=["objet"]),
"martyrs-bargain": TM("Marché du martyr", 1, ["blessure", "retard"], why="tes blessures différées"),
"masters-mutation": TM("Mutation du maître", 2, ["invoqué", "mutation"], why="un être invoqué doté de nouveaux dons", cond=["invoqué"]),
"masterwork-transformation": TM("Chef-d'œuvre", 1, ["objet", "qualité"], why="un objet changé en chef-d'œuvre", cible_obj=["objet"]),
"merge-with-familiar": SH("Fusion avec le compagnon", 1, ["compagnon", "fusion"], why="ton familier fondu en toi", cond=["compagnon"]),
"miasmatic-form": SH("Forme miasmatique", 1, ["gaz", "poison"], why="un corps de gaz nocif"),
"mighty-strength": EN("Force colossale", 2, ["force"], 8, "8 ajouté à la force"),
"mirror-hideaway": TM("Cachette du miroir", P, ["miroir", "abri"], 8, "huit cachés derrière un miroir"),
"mirror-polish": TM("Poli miroir", 1, ["métal", "miroir"], why="un métal poli en miroir", cible_obj=["métal"]),
"mirror-strike": EN("Frappe miroir", 1, ["coup", "multiple"], why="un coup qui touche plusieurs ennemis"),
"mirror-transport": MV("Passage du miroir", 1, ["miroir", "porte"], why="un miroir qui sert de porte", cible_obj=["miroir"]),
"monkey-fish": EN("Singe-poisson", 1, ["escalade", "nage"], why="grimper et nager"),
"monstrous-extremities": SH("Extrémités monstrueuses", 2, ["membre", "mutation"], why="un membre devenu monstrueux"),
"natural-rhythm": EN("Rythme naturel", 1, ["coup", "rythme"], 5, "chaque coup plus fort que le précédent"),
"natures-exile": CU("Exil de la nature", 3, ["nature", "hostilité"], why="la nature lui devient étrangère"),
"negate-aroma": EP("Odeur effacée", NVIS, 2, ["odeur"], why="nul flair ne la suit"),
"oasis": TM("Oasis", P, ["eau", "détournement"], why="l'eau détournée vers un point"),
"obsidian-flow": TM("Coulée d'obsidienne", P, ["sol", "verre", "feu"], why="le sol changé en verre fondu"),
"overstimulate": EN("Surstimulation", 2, ["férocité"], why="se bat encore au bord de la mort"),
"parchment-swarm": TM("Nuée de parchemin", P, ["parchemin", "coupure"], 39, "1d6 par niveau"),
"particulate-form": SH("Forme particulaire", P, ["corps", "particule", "régénération"], why="des corps dispersés qui ne saignent plus"),
"peasant-armaments": TM("Armes paysannes", 1, ["outil", "arme"], why="des outils changés en armes"),
"perceive-cues": EN("Indices perçus", 1, ["perception", "intuition"], 5, "voir et deviner"),
"persistent-vigor": EN("Vigueur persistante", 1, ["régénération", "sang"], why="régénère et ne saigne plus"),
"phantom-hunt": EN("Chasse fantôme", 1, ["sens", "compagnon"], why="toi et ton compagnon aux sens affûtés"),
"phasic-challenge": EP("Défi de phase", REL, 3, ["duel", "phase"], why="un ennemi et un allié en duel hors de portée des autres"),
"planar-adaptation": EN("Adaptation planaire", 1, ["plan", "milieu"], why="à l'abri des dangers d'un autre plan", options=[
    O("Adaptation planaire"), O("Adaptation planaire de groupe", src_idx="planar-adaptation-mass", qty_cible=P),
    O("Adaptation à un autre monde", src_idx="planetary-adaptation", impact=(P, ["monde", "milieu"], "à l'abri d'un autre monde")),
    O("Adaptation à un autre monde de groupe", src_idx="planetary-adaptation-mass", qty_cible=P, impact=(P, ["monde", "milieu"], "à l'abri d'un autre monde"))]),
"plant-voice": TM("Voix de la plante", 2, ["plante", "parole"], why="une plante qui parle", cond=["plante"]),
"poisoned-egg": TM("Œuf empoisonné", 1, ["œuf", "poison"], why="un œuf changé en poison", cible_obj=["œuf"]),
"polar-midnight": EP("Minuit polaire", NE, P, ["froid", "ténèbres", "paralysie"], why="un froid noir qui fige"),
"polymorph-familiar": SH("Métamorphose du familier", 2, ["compagnon", "forme"], why="ton familier sous une autre forme", cond=["compagnon"]),
"polypurpose-panacea": EN("Panacée", 1, ["détente"], why="un petit plaisir au choix"),
"pouncing-fury": EN("Bond furieux", 1, ["griffe", "élan"], why="bondir et griffer"),
"pup-shape": SH("Forme de petit", 2, ["bête", "jeunesse"], why="un animal rajeuni en petit"),
"putrefy-food-and-drink": TM("Nourriture gâtée", 1, ["nourriture", "pourriture"], why="nourriture et eau gâtées"),
"quick-change": SH("Changement éclair", 1, ["forme", "vitesse"], why="changer de forme en un clin d'œil"),
"natures-exile-x": None,
}
NEWPF_TRA2 = {k: v for k, v in NEWPF_TRA2.items() if v}
FICHES.update(NEWPF_TRA2)

# --- Pathfinder 1, lot 8 : Transmutation (3/3) ---
PF1_RELECTURE.update({
"quintessence-mastery": "façonne la quintessence des Plans extérieurs, propre à la cosmologie de Golarion",
"recharge-innate-magic": "recharge les « pouvoirs magiques » raciaux : pure mécanique de jeu",
"rune-of-jandelay": "invoque l'Oliphant de Jandelay, légende propre à Golarion",
"rune-of-rule": "confère une des sept runes de domination de Thassilon (Golarion)",
"sign-of-the-dawnflower": "signale un fidèle de Sarenrae, déesse de Golarion",
"tactical-adaptation": "accorde un « don de combat » : pure mécanique de jeu",
"targeted-bomb-admixture": f"modifie les « bombes » de l'alchimiste : {_cls}",
"transmogrify": f"repose sur l'eidolon du conjurateur : {_cls}",
"unfetter": f"repose sur l'eidolon du conjurateur : {_cls}",
"universal-formula": f"imite un « extrait » d'alchimiste : {_cls}",
"virtuoso-performance": f"double la « représentation bardique » : {_cls}",
"widen-auras": f"élargit les « auras de classe » : {_cls}",
})
NEWPF_TRA3 = {
"raging-rubble": TM("Éboulis enragés", P, ["roche", "roulement"], why="des pierres qui roulent et broient"),
"rags-to-riches": EN("Haillons en richesses", 1, ["objet", "qualité"], why="un objet qui vaut un chef-d'œuvre", cible_obj=["objet"]),
"rapid-repair": EP("Réparation rapide", HE, 2, ["artefact", "régénération"], 5, "5 points par instant", cond=["ARTEFACT"]),
"ravens-flight": SH("Vol du corbeau", 1, ["oiseau", "vol"], why="une petite forme floue qui vole"),
"reboot": EP("Redémarrage", HE, 1, ["artefact", "retour"], why="un artefact détruit qui repart un temps", cond=["ARTEFACT"]),
"recoil-fire": TM("Recul violent", 1, ["poudre", "recul"], why="une arme à poudre qui recule fort"),
"redcaps-touch": EN("Toucher sanglant", 1, ["coup", "vie", "mort"], why="tuer te fortifie"),
"refine-improvised-weapon": TM("Arme raffinée", 1, ["outil", "arme"], why="un objet de fortune changé en vraie arme", cible_obj=["objet"]),
"reinforce-armaments": EN("Armement renforcé", 1, ["arme", "solidité"], why="une arme fragile rendue solide", cible_obj=["arme"], options=[O("Armement renforcé"), O("Armements renforcés", src_idx="reinforce-armaments-communal", qty_cible=P)]),
"remarkable-legerdemain": EN("Prestidigitation remarquable", 1, ["objet", "dissimulation"], why="cacher des objets avec une adresse étrange"),
"reprobation": CU("Réprobation", 3, ["marque", "foi"], why="rejetée par les fidèles"),
"resilient-reservoir": TM("Réserve résiliente", 1, ["blessure", "énergie"], why="les blessures changées en énergie"),
"resinous-skin": TM("Peau résineuse", 1, ["peau", "garde"], 5, "5 retranché aux coups perçants"),
"resist-starvation": EN("Résistance à la faim", 2, ["faim"], why="tenir sans manger"),
"resize-item": TM("Taille ajustée", 1, ["objet", "taille"], why="une arme ou armure ajustée", cible_obj=["objet"]),
"resonating-word": EP("Mot résonnant", NE, 3, ["son", "étourdissement"], why="un mot qui fait chanceler et étourdit"),
"resounding-clang": TM("Fracas retentissant", P, ["métal", "vibration"], why="tout métal vibre"),
"revenant-armor": TM("Armure revenante", 1, ["armure", "animation"], why="l'armure se bat seule quand tu tombes", cible_obj=["armure"]),
"ride-the-waves": EN("Chevaucher les vagues", 2, ["eau", "nage", "souffle"], why="nager et respirer sous l'eau"),
"rigor-mortis": EP("Rigidité", NE, 3, ["articulation", "douleur"], why="des articulations gonflées"),
"rivals-weald": SH("Bois du rival", 3, ["arbre"], why="changée en arbre"),
"ropeweave": TM("Tissage de corde", 1, ["corde", "outil"], why="une corde qui se fait outil", cible_obj=["corde"]),
"rotgut": TM("Tord-boyaux", 1, ["eau", "alcool"], why="de l'eau changée en mauvais alcool", cible_obj=["eau"]),
"rovagugs-fury": TM("Fureur de la terre", P, ["terre", "secousse"], why="un petit séisme qui renverse"),
"rubberskin": TM("Peau de caoutchouc", 1, ["peau", "rebond"], why="les chocs et chutes amortis"),
"rune-of-durability": EN("Rune de durabilité", 1, ["arme", "rune"], 2, "une arme deux fois plus solide", cible_obj=["arme"]),
"rune-of-ruin": CU("Rune de ruine", 1, ["objet", "rune", "affaiblissement"], why="un objet magique maudit et affaibli", cible_obj=["objet"]),
"sabotage-construct": EP("Artefact saboté", NQ, 3, ["artefact", "confusion"], why="un artefact animé confus", cond=["ARTEFACT"]),
"saddle-surge": EN("Élan de selle", 1, ["monture", "élan"], why="plus fort en chevauchant"),
"salvage": TM("Récupération", P, ["épave", "navire"], why="une épave reformée"),
"sanctify-weapons": EN("Armes sanctifiées", P, ["arme", "fiélon"], why="des armes qui mordent les fiélons"),
"savage-maw": SH("Gueule sauvage", 1, ["gueule", "rugissement"], why="une gueule féroce et un rugissement"),
"sawtooth-terrain": TM("Terrain en dents de scie", P, ["terrain", "pointe"], why="des membres de mante jaillis du sol"),
"scamper": EN("Gambade", 2, ["agilité"], why="ton compagnon d'une agilité folle", cond=["compagnon"]),
"scent-trail": EP("Piste odorante", VIS, P, ["odeur", "piste"], why="une piste pour tes alliés"),
"scorching-ash-form": SH("Forme de cendre brûlante", 3, ["cendre", "feu", "gaz"], why="changée en nuage de cendre"),
"scriveners-chant": TM("Chant du copiste", 1, ["plume", "copie"], why="une plume qui recopie seule", cible_obj=["plume"]),
"sculpt-simulacrum": SH("Simulacre sculpté", 2, ["simulacre", "apparence"], why="l'apparence d'un simulacre changée"),
"sculpted-cape": TM("Cape sculptée", 1, ["cape", "rigidité"], why="une cape qui se raidit et porte", cible_obj=["cape"]),
"sea-of-dust": TM("Mer de poussière", P, ["eau", "désert"], why="l'eau chassée à jamais"),
"sea-steed": EN("Monture marine", 2, ["monture", "eau"], why="ta monture faite à l'eau", options=[
    O("Monture marine"), O("Étalon marin", src_idx="sea-stallion", impact=(P, ["monture", "eau", "cavalier"], "toi et ta monture faits à l'eau"))]),
"sebaceous-twin": EP("Jumeau sébacé", NE, 3, ["double", "parasite"], why="un double parasite arraché d'elle"),
"seismic-fissure": TM("Fissure sismique", P, ["terre", "fissure"], why="une faille immense"),
"serrens-armor-lock": CU("Armure bloquée", 3, ["armure", "raideur"], why="son armure se raidit et l'enserre"),
"serrens-swift-girding": TM("Armement éclair", P, ["armure"], why="des armures endossées d'un coup"),
"shadow-body": SH("Corps astral", 1, ["corps"], why="un corps d'énergie astrale", options=[O(f"Corps astral {ef}", impact=(P, ["corps", e], f"un corps d'énergie {ef}")) for e, ef in ASTR]),
"shadowy-haven": TM("Refuge astral", P, ["abri"], why="une pièce cachée au bord d'un hémisphère", options=[O(f"Refuge {ef}", impact=(P, ["abri", e], f"au bord de l'hémisphère {ef}")) for e, ef in ASTR]),
"shapechangers-gift": SH("Don du métamorphe", 2, ["forme", "don"], why="changée en animal, humanoïde ou monstre", options=[
    O("Don du métamorphe"), O("Don du métamorphe suprême", src_idx="shapechangers-gift-greater", impact=(P, ["forme", "don", "élémentaire"], "et en élémentaire, fée ou plante"))]),
"shield-of-shards": TM("Bouclier d'éclats", 1, ["bouclier", "éclat"], why="ton bouclier en tempête d'éclats"),
"shifting-sand": TM("Sable mouvant", P, ["sable", "trace"], why="un sable qui efface les traces et emporte"),
"sickening-entanglement": TM("Enchevêtrement écœurant", P, ["plante", "sève", "nausée"], why="des plantes à sève écœurante", options=[
    O("Enchevêtrement écœurant"), O("Enchevêtrement assoiffé", src_idx="thirsting-entanglement", impact=(P, ["plante", "épine", "constitution"], "des épines qui assèchent")),
    O("Enchevêtrement épineux", src_idx="thorny-entanglement", impact=(P, ["plante", "épine", "trait"], "des plantes qui tirent des épines"))]),
"sickening-strikes": TM("Frappes infectées", 1, ["maladie", "coup"], why="tes coups transmettent ta maladie"),
"siege-of-trees": TM("Siège des arbres", 2, ["arbre", "catapulte"], why="un arbre changé en catapulte", cond=["arbre"], options=[
    O("Siège des arbres"), O("Siège des arbres suprême", src_idx="siege-of-trees-greater", impact=(P, ["arbre", "catapulte", "géant"], "même les plus grands"))]),
"silk-to-steel": TM("Soie d'acier", 1, ["écharpe", "bouclier", "fouet"], why="une écharpe en bouclier ou en fouet", cible_obj=["écharpe"]),
"sky-steed": SH("Monture céleste", 2, ["monture", "aile"], why="des ailes d'ange pour ta monture"),
"sky-swim": MV("Nage dans le ciel", 2, ["air", "nage"], why="nager dans l'air"),
"snake-staff": TM("Bâton de serpents", P, ["bois", "serpent"], why="du bois changé en serpents"),
"snapdragon-fireworks": TM("Feux d'artifice draconiques", P, ["feu", "dragon"], why="des fusées en forme de dragon"),
"snow-shape-ulfen": TM("Façonnage de la neige", P, ["neige", "forme"], why="la neige façonnée, même en armes de glace"),
"solidify-earth": TM("Terre durcie", P, ["terre", "dureté"], why="terre et pierre durcies"),
"sonic-form": SH("Forme sonore", 1, ["son", "corps"], why="un corps de son"),
"spit-venom": TM("Crachat de venin", 3, ["venin", "cécité"], why="un venin qui aveugle"),
"splinter-spell-resistance": EN("Brèche dans la résistance", 1, ["arme", "magie"], why="une arme qui ébrèche la résistance magique", cible_obj=["arme"]),
"squeeze": EN("Contorsion", 2, ["souplesse", "passage"], why="passer par d'étroits passages"),
"stabilize-powder": EN("Poudre stable", 1, ["poudre", "fiabilité"], why="une arme à poudre qui rate moins"),
"staggering-fall": EP("Chute écrasante", NF, 3, ["chute", "écrasement"], why="la chute plus rude"),
"steady-saddle": EN("Selle sûre", 1, ["selle", "équilibre"], why="une selle qui tient", cible_obj=["selle"]),
"steal-breath": EP("Souffle volé", NE, 3, ["souffle"], why="l'air arraché de ses poumons"),
"stench-of-prey": CU("Odeur de proie", 3, ["odeur", "prédateur"], why="les prédateurs s'en prennent à elle"),
"stoke-the-inner-fire": EN("Feu intérieur attisé", 1, ["chaleur", "arme"], why="ta chaleur passe dans tes armes"),
"stone-fist": EN("Poing de pierre", 1, ["poing", "pierre"], why="tes poings tuent"),
"stone-throwing": EN("Lanceur de rocs", 2, ["roche", "lancer"], why="lancer et attraper des rochers"),
"strangling-hair": SH("Cheveux étrangleurs", 1, ["cheveux", "saisie"], why="tes cheveux saisissent"),
"strong-jaw": EN("Mâchoire puissante", 2, ["croc", "puissance"], why="des crocs plus terribles"),
"sturdy-tree-fort": TM("Fort dans l'arbre", P, ["arbre", "fort"], why="un arbre qui porte un fort"),
"submerge-ship": TM("Navire submersible", 1, ["navire", "eau"], why="un navire qui plonge", cible_obj=["navire"]),
"substitute-trail": EP("Fausse piste", NVIS, 2, ["piste", "leurre"], why="ses traces passent pour d'autres"),
"sun-metal": EN("Métal solaire", 1, ["arme", "feu"], why="une arme qui s'embrase", cible_obj=["arme"]),
"suns-disdain": CU("Dédain du soleil", 3, ["lumière", "aveuglement", "faiblesse"], why="la lumière l'aveugle et la blesse", options=[O("Dédain du soleil"), O("Dédain du soleil de groupe", src_idx="suns-disdain-mass", qty_cible=P)]),
"sundering-shards": TM("Éclats brisants", 1, ["objet", "explosion"], why="l'objet brisé explose", cible_obj=["objet"]),
"surefoot-boots": EN("Bottes sûres", 1, ["botte", "équilibre"], why="des bottes qui ne glissent pas", cible_obj=["botte"]),
"swallow-poison": TM("Poison avalé", 1, ["poison", "crachat"], why="un poison avalé sans mal puis craché"),
"swarm-skin": SH("Peau de nuée", 1, ["nuée", "vermine"], why="ton corps en nuée de vermine", options=[
    O("Peau de nuée"), O("Transformation vermineuse", src_idx="verminous-transformation", impact=(P, ["nuée", "vermine", "partie"], "en partie seulement"))]),
"sword-to-snake": TM("Épée en serpent", 1, ["objet", "serpent"], why="un objet changé en serpent venimeux", cible_obj=["objet"]),
"symbol-of-slowing": SYMP("Symbole de lenteur", verb=NINT, impact=(P, ["lenteur"], "chacun ralenti")),
"tail-current": TM("Courant de traîne", P, ["eau", "courant"], why="un courant qui porte ou freine la nage"),
"tail-strike": SH("Coup de queue", 1, ["queue", "coup"], why="une queue qui frappe"),
"tailwind": TM("Vent arrière", P, ["vent", "vol"], why="un vent qui porte ou freine le vol"),
"tar-ball": TM("Boule de goudron", 3, ["goudron", "feu"], why="du goudron brûlant qui colle"),
"tar-pool": TM("Mare de goudron", P, ["goudron", "sol"], why="le sol changé en goudron brûlant"),
"tattoo-potion": TM("Potion tatouage", 1, ["potion", "tatouage"], why="une potion qui devient tatouage", cible_obj=["potion"]),
"telekinetic-assembly": MV("Assemblage télékinétique", P, ["machine", "assemblage"], why="une machine de siège montée par la pensée"),
"telekinetic-maneuver": MV("Manœuvre télékinétique", 3, ["force", "bousculade"], why="bousculer ou désarmer par la pensée"),
"telekinetic-volley": MV("Volée télékinétique", P, ["objet", "projection"], why="des objets lancés en volée"),
"temporal-divergence": EP("Divergence temporelle", TP, 1, ["temps", "choix"], why="vivre deux instants et garder l'un"),
"temporary-graft": TM("Greffe temporaire", 1, ["greffe", "membre"], why="une greffe qui te sert un temps"),
"thorn-body": TM("Corps d'épines", 1, ["épine", "riposte"], 11, "1d6 + 1 par niveau à qui te frappe"),
"threefold-aspect": SH("Aspect triple", 1, ["âge", "apparence"], why="paraître plus jeune ou plus vieux"),
"threefold-face": SH("Visage triple", 1, ["visage", "vue"], why="deux visages de plus pour mieux voir"),
"thunder-fire": TM("Tir de tonnerre", 1, ["poudre", "surdité"], why="un tir qui assourdit"),
"time-shudder": EP("Frisson du temps", TP, P, ["temps", "vitesse", "lenteur"], why="chacun accéléré ou ralenti"),
"tireless-pursuit": EN("Poursuite infatigable", 1, ["marche", "fatigue"], why="marcher vite sans fatigue", options=[O("Poursuite infatigable"), O("Poursuivants infatigables", src_idx="tireless-pursuers", qty_cible=P)]),
"touch-injection": TM("Injection", 1, ["potion", "toucher"], why="une potion ou un poison donnés d'un toucher"),
"touch-of-gracelessness": CU("Toucher de maladresse", 3, ["adresse", "chute"], why="maladroite, elle tombe"),
"touch-of-the-sea": EN("Toucher de la mer", 2, ["nage"], why="nager comme un poisson"),
"toxic-blood": TM("Sang toxique", 1, ["sang", "poison"], why="ton sang empoisonne qui te blesse"),
"transfer-tattoo": TM("Tatouage transféré", 2, ["tatouage", "transfert"], why="un tatouage magique passé à un autre"),
"transfiguring-touch": TM("Toucher transfigurant", 1, ["objet", "matière"], why="un objet changé en fer, papier ou bois", cible_obj=["objet"]),
"transmute-blood-to-acid": TM("Sang en acide", 3, ["sang", "acide"], why="son sang devenu acide"),
"transmute-golem": TM("Golem transmuté", 3, ["artefact", "golem"], why="un golem changé en un autre", cond=["ARTEFACT"]),
"transmute-potion-to-poison": TM("Potion en poison", 1, ["potion", "poison"], why="une potion bue rendue en poison"),
"treasure-stitching": TM("Broderie au trésor", 1, ["étoffe", "broderie"], why="les objets brodés sur une étoffe", cible_obj=["étoffe"]),
"tripvine": TM("Liane piège", P, ["liane", "chute"], why="une corde animée qui fait tomber"),
"twin-form": SH("Forme jumelle", 1, ["double"], why="un double que tu diriges"),
"twisted-innards": TM("Entrailles tordues", 1, ["vital", "déplacement"], why="tes points vitaux déplacés"),
"twisted-space": CU("Espace tordu", 3, ["espace", "écart"], why="ses coups partent au hasard"),
"undead-anatomy-i": SHAPE("Anatomie morte-vivante", "d'un mort-vivant", "mort-vivant", [(r, f"undead-anatomy-{r.lower()}", x, d) for r, x, d in [("I", [], "petit ou moyen"), ("II", ["taille"], "minuscule ou grand"), ("III", ["taille", "énorme"], "infime ou énorme"), ("IV", ["taille", "pouvoir"], "et plus de pouvoirs")]]),
"underbrush-decoy": EP("Leurre des fourrés", NVIS, P, ["bruissement", "leurre"], why="un bruissement qui détourne"),
"unerring-weapon": EN("Arme infaillible", 1, ["arme", "précision"], why="une arme qui ne manque guère", cible_obj=["arme"]),
"urban-grace": EN("Grâce urbaine", 1, ["foule", "aisance"], why="glisser dans la foule"),
"vengeful-stinger": SH("Dard vengeur", 1, ["dard", "queue"], why="une queue de guêpe"),
"venomous-bite": EN("Morsure venimeuse", 2, ["croc", "poison"], why="une morsure empoisonnée"),
"vermin-shape-i": SHAPE("Forme de vermine", "d'une vermine", "vermine", [("I", "vermin-shape-i", [], "petite ou moyenne"), ("II", "vermin-shape-ii", ["taille"], "minuscule ou grande")]),
"versatile-weapon": EN("Arme polyvalente", 1, ["arme", "matière"], why="une arme qui frappe comme le bon métal", cible_obj=["arme"]),
"vex-giant": EN("Tracasser le géant", 1, ["perception", "grand"], why="des sens aiguisés contre plus grand que toi"),
"vigor": EN("Vigueur", 2, ["coup"], 1, "1 de plus au prochain coup"),
"violent-accident": CU("Accident violent", 3, ["accident", "mort"], why="un accident mortel qui l'attend"),
"vocal-alteration": SH("Voix altérée", 2, ["voix"], why="une autre voix"),
"waft": MV("Envol léger", P, ["vent", "légèreté"], why="assez légers pour que le vent les porte"),
"wandering-trail": EP("Piste errante", NVIS, P, ["piste", "égarement"], why="les pistes tordues"),
"wandering-weather": TM("Temps vagabond", P, ["climat", "mouvement"], why="le temps qu'il fait, qui te suit"),
"wave-form": SH("Forme de vague", 1, ["vague", "chute"], why="une vague qui renverse tout"),
"weaken-powder": TM("Poudre affaiblie", 1, ["poudre", "portée"], why="une arme à poudre affaiblie"),
"weapon-of-awe": EN("Arme impressionnante", 1, ["arme", "crainte"], 2, "une arme qui impressionne", cible_obj=["arme"]),
"weapons-against-evil": EN("Armes contre l'hostile", P, ["arme", "lumière", "hostile"], why="des armes de pâle lumière contre l'hostile"),
"weaponwand": TM("Arme-baguette", 1, ["arme", "baguette", "fusion"], why="une baguette fondue dans ton arme"),
"wilderness-soldiers": TM("Soldats sauvages", P, ["plante", "allié"], why="les plantes combattent avec toi"),
"wind-blades": TM("Lames de vent", 2, ["vent", "lame"], why="un air durci en lames"),
"windy-escape": SH("Fuite venteuse", 1, ["vent", "intangible"], why="un coup qui passe à travers toi"),
"wing-thorns": SH("Épines d'aile", 1, ["aile", "épine", "poison"], why="des épines empoisonnées sur tes ailes"),
"winged-sword": EN("Épée ailée", 1, ["arme", "lancer"], why="une arme qu'on peut lancer", cible_obj=["arme"]),
"wizened-appearance": SH("Apparence flétrie", 3, ["âge", "apparence"], why="paraître vieille", options=[
    O("Apparence flétrie"), O("Apparence juvénile", src_idx="youthful-appearance", cible=2, impact=(P, ["jeunesse", "apparence"], "paraître jeune"))]),
"wooden-wing-shield": SH("Bouclier d'ailes de bois", 1, ["aile", "bois", "garde"], why="tes ailes changées en bouclier"),
"world-wave": MV("Vague du monde", 1, ["terre", "voyage"], why="la terre te porte au loin"),
"wrathful-weapon": EN("Arme courroucée", 1, ["arme", "charge"], why="une arme chargée contre la charge choisie", cible_obj=["arme"], options=TRIPF()),
"zephyrs-fleetness": MV("Célérité du zéphyr", P, ["vitesse", "vol"], why="tes alliés plus rapides"),
"zone-of-foul-flames": TM("Zone des flammes viciées", P, ["feu", "renvoi"], why="le feu renvoyé à qui le lance"),
"fly-mass-x": None,
}
NEWPF_TRA3 = {k: v for k, v in NEWPF_TRA3.items() if v}
FICHES.update(NEWPF_TRA3)
FICHES["beast-shape-i"]["options"].append(O("Forme partagée", src_idx="share-shape", impact=(P, ["bête", "forme", "compagnon"], "la forme de ton compagnon animal")))
PFV("Transmutation")
for k, extra in [("air-walk", [O("Marche dans les airs partagée", src_idx="air-walk-communal", qty_cible=P)]),
    ("align-weapon", [O("Arme alignée partagée", src_idx="align-weapon-communal", qty_cible=P)]),
    ("darkvision", [O("Vision dans le noir partagée", src_idx="darkvision-communal", qty_cible=P), O("Vision dans le noir suprême", src_idx="darkvision-greater")]),
    ("fly", [O("Vol de groupe", src_idx="fly-mass", qty_cible=P)]), ("knock", [O("Déblocage de groupe", src_idx="knock-mass", qty_cible=P)]),
    ("longstrider", [O("Grande foulée suprême", src_idx="longstrider-greater")]), ("polymorph", [O("Métamorphose suprême", src_idx="polymorph-greater")]),
    ("spider-climb", [O("Pattes d'araignée partagées", src_idx="spider-climb-communal", qty_cible=P)]), ("water-walk", [O("Marche sur l'onde partagée", src_idx="water-walk-communal", qty_cible=P)]),
    ("warp-wood", [O("Métal gauchi", src_idx="warp-metal", impact=(P, ["métal", "gauchissement"], "le métal gauchi"))]),
    ("enter-image", [O("Image majestueuse", src_idx="majestic-image", impact=(P, ["image", "conscience", "prestance"], "et la prestance en plus"))])]:
    if k == "enter-image": FICHES[k]["options"] = [O("Entrer dans l'image")] + extra
    else: ADDPF(k, *extra)

# --- Pathfinder 1, décisions de relecture ---
# 1. La neutralité d'alignement ne se transpose pas : les sorts qui en dépendent restent écartés.
for k in ("counterbalancing-aura", "dispel-balance", "arbitrament", "ardors-onslaught"):
    PF1_RELECTURE[k] = PF1_RELECTURE[k].replace(" : à revoir", "") + " (écarté après relecture)"
# 2. Inarama n'a pas d'armes à feu : les sorts qui ne servent qu'à elles sont écartés.
_FEU = ["bullet-shield", "bullet-ward", "coin-shot", "damp-powder", "destabilize-powder", "fabricate-bullets", "flash-fire",
        "recoil-fire", "reloading-hands", "stabilize-powder", "thunder-fire", "weaken-powder"]
# 3. Inarama n'a pas d'autres mondes : les sorts qui y mènent ou en viennent sont écartés.
_MONDES = ["interplanetary-teleport", "ally-across-time", "army-across-time", "planetary-adaptation", "planetary-adaptation-mass"]
for k in _FEU:
    FICHES.pop(k, None); PF1_RELECTURE[k] = "ne sert qu'aux armes à feu, absentes d'Inarama"
for k in _MONDES:
    FICHES.pop(k, None); PF1_RELECTURE[k] = "suppose d'autres mondes, absents de la cosmologie d'Inarama"
FICHES["planar-adaptation"]["options"] = [o for o in FICHES["planar-adaptation"]["options"] if o.get("src_idx") not in _MONDES]
FICHES["alchemical-tinkering"]["impact"] = (P, ["objet", "transformation"], "un objet alchimique changé en un autre")

# ===== Nettoyage validé : sous-systèmes, créatures, peuples =====
# Sous-systèmes de règles propres à Pathfinder : écartés. Ce qui existe hors Pathfinder (hantises, empreintes psychiques,
# ectoplasme, mémoire akashique, folie) reste.
_SOUS = {
"alleviate-corruption": "repose sur la « corruption », sous-système de règles propre à Pathfinder",
"ban-corruption": "repose sur la « corruption », sous-système de règles propre à Pathfinder",
"stave-off-corruption": "repose sur la « corruption », sous-système de règles propre à Pathfinder",
"suppress-primal-magic": "repose sur la « magie primitive », sous-système de règles propre à Pathfinder",
"alaznists-jinx": "repose sur les « fléaux des sorts » (spellblights), sous-système de règles propre à Pathfinder",
"microcosm": "repose sur les « mondes intérieurs » (mindscapes), sous-système de règles propre à Pathfinder",
"psychic-asylum": "repose sur les « mondes intérieurs » (mindscapes), sous-système de règles propre à Pathfinder",
"mindscape-door": "repose sur les « mondes intérieurs » (mindscapes), sous-système de règles propre à Pathfinder",
"detect-mindscape": "repose sur les « mondes intérieurs » (mindscapes), sous-système de règles propre à Pathfinder",
"anywhere-but-here": "mène au hasard vers les plans de la cosmologie de Golarion",
}
# Créatures : pas de vases à Inarama ; les classes de dragons de Pathfinder sont retirées (le dragon reste).
_CREA = {k: "met en jeu les vases, absentes d'Inarama" for k in ("conjure-black-pudding", "ooze-form-i", "ooze-form-ii", "ooze-form-iii", "touch-of-slime", "flesh-to-ooze")}
_CREA.update({k: "classe de dragons propre à Pathfinder (le dragon reste, sans ces titres)" for k in
    ("form-of-the-exotic-dragon-i", "form-of-the-exotic-dragon-ii", "form-of-the-exotic-dragon-iii", "form-of-the-alien-dragon-i", "form-of-the-alien-dragon-ii")})
# Peuples : mis de côté, à reprendre avec l'étude des sorts peuple par peuple.
_PEUP = {k: "propre à un peuple : à reprendre avec les sorts peuple par peuple" for k in
    ("halfling-vengeance", "halfling-vengeance-mass", "human-potential", "human-potential-mass", "guardian-monument-lesser", "guardian-monument-greater")}
for d in (_SOUS, _CREA, _PEUP):
    for k, why in d.items():
        FICHES.pop(k, None); PF1_RELECTURE[k] = why
FICHES["form-of-the-dragon-i"]["options"] = [o for o in FICHES["form-of-the-dragon-i"]["options"] if o.get("src_idx") not in _CREA]

# Êtres d'ailleurs rattachés aux plans : les « angéliques » au plan astral lumineux, les « démoniaques » (démons, diables, fiélons)
# au plan astral ténébreux ; chaque sort lié à l'un reçoit sa forme réciproque (règle de réciprocité).
AST = lambda lab, words, why: [O(f"{lab} — {e}", impact=(P, list(words) + [e], f"{why} de la face {ef} du plan astral")) for e, ef in ASTR]
FICHES["angelic-aspect-lesser"].update(fr="Aspect astral", impact=(P, ["aspect"], "un peu de la nature des êtres astraux"), options=[
    O(f"{lab} — {e}", src_idx=k, impact=(P, ["aspect", e] + x, f"{d}, de la face {ef} du plan astral")) for lab, k, x, d in [
        ("Aspect astral mineur", "angelic-aspect-lesser", [], "un peu de la nature astrale"), ("Aspect astral", "angelic-aspect", ["aile"], "davantage, et des ailes"),
        ("Aspect astral suprême", "angelic-aspect-greater", ["aile", "gloire"], "la pleine nature astrale")] for e, ef in ASTR])
FICHES["sky-steed"].update(fr="Monture ailée", impact=(P, ["monture", "aile"], "des ailes pour ta monture"), options=AST("Monture ailée", ["monture", "aile"], "des ailes d'être astral"))
FICHES["archons-aura"].update(fr="Aura astrale", options=AST("Aura astrale", ["aura", "faiblesse"], "une aura qui affaiblit tes ennemis, venue"))
FICHES["archons-trumpet"].update(fr="Trompette astrale", options=AST("Trompette astrale", ["son", "paralysie"], "une sonnerie qui paralyse, venue"))
FICHES["summon-infernal-host"].update(fr="Légion astrale", cond=[], impact=(P, ["légion"], "une légion d'êtres astraux"), options=AST("Légion astrale", ["légion"], "une légion d'êtres"))
FICHES["devil-snare"].update(fr="Piège astral", impact=(P, ["cercle", "piège"], "un cercle invisible qui retient les êtres astraux"), options=AST("Piège astral", ["cercle", "piège"], "retient les êtres"))
FICHES["sanctify-weapons"].update(fr="Armes contre les êtres astraux", impact=(P, ["arme"], "des armes qui mordent les êtres astraux"), options=[
    O(f"Contre le {e}", impact=(P, ["arme", e], f"des armes qui mordent les êtres de la face {ef} du plan astral")) for e, ef in ASTR])
FICHES["contact-nalfeshnee"].update(fr="Contact astral", impact=(9, ["savoir"], "consulter un savant être astral"), options=AST("Contact astral", ["savoir"], "consulter un savant être"))
FICHES["barbed-chains"].update(impact=(P, ["chaîne", "peur"], "des chaînes barbelées qui frappent et effraient"), options=AST("Chaînes barbelées", ["chaîne", "peur"], "des chaînes qui frappent et effraient, venues"))
FICHES["vision-of-hell"].update(fr="Vision du plan astral", impact=(P, ["vision", "peur"], "un paysage du plan astral qui accable"), options=AST("Vision du plan astral", ["vision", "peur"], "un paysage accablant"))
FICHES["eaglesoul"].update(fr="Âme astrale", impact=(P, ["pouvoir"], "la force d'un être astral"), options=AST("Âme astrale", ["pouvoir"], "la force d'un être"))
FICHES["veil-of-heaven"].update(fr="Voile astral", cond=[], impact=(P, ["garde"], "protégé des êtres astraux"), options=[
    O(f"Contre le {e}", cond=[e], impact=(P, ["garde", e], f"protégé des êtres de la face {ef} du plan astral")) for e, ef in ASTR])
FICHES["songbird"].update(fr="Chant astral", impact=(P, ["musique"], "une musique venue du plan astral"), options=AST("Chant astral", ["musique"], "une musique"))
FICHES["burn-corruption"].update(fr="Purge par le feu", impact=(P, ["vie", "feu"], "des flammes violettes qui récurent toute vie du lieu"))
# Guérison céleste et guérison infernale : un même sort, une forme lumineuse et une forme ténébreuse.
FICHES["celestial-healing"].update(fr="Guérison astrale", options=[
    O("Guérison astrale — lumineux", impact=(1, ["vie", "régénération", "lumineux"], "1 point par instant, puisé à l'énergie lumineuse")),
    O("Guérison astrale suprême — lumineux", src_idx="celestial-healing-greater", impact=(4, ["vie", "régénération", "lumineux"], "4 points par instant, puisés à l'énergie lumineuse")),
    O("Guérison astrale — ténébreux", src_idx="infernal-healing", impact=(1, ["vie", "régénération", "ténébreux"], "1 point par instant, puisé à l'énergie ténébreuse")),
    O("Guérison astrale suprême — ténébreux", src_idx="infernal-healing-greater", impact=(4, ["vie", "régénération", "ténébreux"], "4 points par instant, puisés à l'énergie ténébreuse"))])
FICHES.pop("infernal-healing", None)

# ===== Nettoyage validé (2) =====
# Ectoplasme et mémoire akashique : retirés (seuls hantises, empreintes psychiques et folie restent).
for k in ("ectoplasmic-eruption", "ectoplasmic-hand", "ectoplasmic-snare", "wall-of-ectoplasm", "fumblestep", "spirit-bound-blade"):
    FICHES.pop(k, None); PF1_RELECTURE[k] = "repose sur l'ectoplasme, notion occulte reprise par Pathfinder"
for k in ("akashic-communion", "akashic-form", "greater-reversion", "minor-reversion", "minor-reversion-mass"):
    FICHES.pop(k, None); PF1_RELECTURE[k] = "repose sur la mémoire akashique, notion occulte reprise par Pathfinder"
# Géants : le géant du peuple reste une forme ; les géants « de feu, de givre, de nuage… » sont une transformation
# élémentaire (comme la forme de dragon) : un géant fait d'un élément, non un individu. Allié géant, qui fait venir
# un individu d'un peuple, est mis de côté avec les autres sorts de peuples.
FICHES["giant-form-i"].update(options=[O("Forme de géant", src_idx="giant-form-i", impact=(P, ["géant", "forme", "grand"], "la forme d'un géant"))] + [
    O(f"Forme de géant élémentaire — {n}", src_idx="giant-form-ii", fam="H", comb=c, why=f"l'élément {n.lower()}", impact=(P, ["géant", "forme", "élémentaire", w], f"un géant fait de {d}"))
    for n, c, w, d in [("Feu", "Feu", "feu", "feu"), ("Glace", "Glace", "glace", "glace"), ("Brume", "Brume", "nuage", "nuée"), ("Tempête", "Tempête", "tempête", "tempête"), ("Roche", "Roche", "roche", "roche")]])
for k in ("summon-giant-ally-i", "summon-giant-ally-ii", "summon-giant-ally-iii"):
    PF1_RELECTURE[k] = "fait venir un individu du peuple des géants : à reprendre avec les sorts peuple par peuple"
FICHES.pop("summon-giant-ally-i", None)
# Anciens lots D&D : céleste -> être de la face lumineuse du plan astral, fiélon -> être de sa face ténébreuse.
def _astr(ws): return [{"céleste": "lumineux", "fiélon": "ténébreux"}.get(w, w) for w in ws]
FICHES["detect-evil-and-good"]["notes"] = ["Êtres des deux faces du plan astral, élémentaires, fées, morts-vivants : des êtres qui relèvent d'un plan (Cible 9)."]
for k in ("protection-from-evil-and-good", "magic-circle", "planar-binding", "planar-ally"):
    v = FICHES[k].get("v24") if False else None
for k, key in (("protection-from-evil-and-good", "impact"), ("planar-ally", "impact")):
    for d in (FICHES[k], FICHES[k].get("v35") or {}, FICHES[k].get("vpf") or {}):
        if d.get(key) and d[key][1]: d[key] = (d[key][0], _astr(d[key][1]), d[key][2])
for k in ("magic-circle", "planar-binding"):
    for d in (FICHES[k], FICHES[k].get("v35") or {}, FICHES[k].get("vpf") or {}):
        if d.get("cible_note"): d["cible_note"] = _astr(d["cible_note"])
FICHES["divine-smite"]["impact_sats"] = [(5, ["ténébreux", "mort-vivant"])]
# Avec la règle de réciprocité : chaque sort lié à une face du plan astral reçoit sa forme réciproque.
FICHES["conjure-celestial"].update(fr="Invocation d'être astral", impact=(4, ["être"], "un être astral de puissance 4"),
    options=[O(f"Être {e}", impact=(4, ["être", e], f"un être de la face {ef} du plan astral, de puissance 4")) for e, ef in ASTR])
FICHES["conjure-celestial-2024"].update(fr="Invocation d'être astral (2024)", options=[
    O(f"Colonne {ef}", impact_sats=[(39, [e])]) for e, ef in ASTR])
FICHES["hellish-rebuke"].update(fr="Représailles astrales", options=[O(f"Représailles — {e}", impact_sats=[(P, [e])]) for e, ef in ASTR])

# ===== Essai de méthode (validé) : le glyphe dit le sort par ses mécaniques, l'annotation précise =====
# Protection contre le mal et le bien : le verbe Séparer dit la garde ; ceux dont on est gardé sont les êtres qui relèvent
# d'un plan (satellite de Cible 9 greffé sur l'Impact) et les aberrations, œuvres de magie.
FICHES["protection-from-evil-and-good"].update(impact=(P, [], "ni attaque franche, ni charme, ni peur, ni possession"),
    impact_sats=[(9, ["cible"]), (P, ["aberration"])])
# Image majeure : la Cosmétique annotée « sens trompé » compte les sens que l'illusion trompe (plein : tous).
FICHES["major-image"].update(impact=(P, ["image"], "une illusion qui trompe tous les sens"), cosm=(P, "sens trompé"))
# Esprit apaisé : on stabilise un être sans corps (Cible 7) ; toute agression rompt l'apaisement.
FICHES["calm-spirit"].update(verb=V("ordre"), cible=7, cond=[], impact=(P, ["paix"], "il ne peut plus rien faire de violent"), fin=["agression"])
# Coup repoussant : le verbe Repousser, et un Impact nu qui délivre sa force brute, au prochain coup.
FICHES["inheritors-smite"].update(verb=V("force", True), cible=3, cond=["coup"], impact=(P, [], "le coup frappe plus juste et repousse l'adversaire"))
# Glace bénite : mur ou javelots, deux options, chacune en forme lumineuse et ténébreuse.
FICHES["holy-ice"].update(impact=(P, ["glace"], "eau bénite gelée"), options=[
    O(f"Mur de glace {'bénite' if e == 'lumineux' else 'maudite'} — {e}", src_idx=k, aoe={"type": "line", "size": 90}, impact=(P, ["glace", e], f"un mur de glace d'eau chargée d'énergie {ef}"))
    for e, ef, k in (("lumineux", "lumineuse", "holy-ice"), ("ténébreux", "ténébreuse", "unholy-ice"))] + [
    O(f"Javelots de glace {'bénite' if e == 'lumineux' else 'maudite'} — {e}", src_idx=k, cible=3, impact=(5, ["glace", e], "1d6 + 2 par javelot (eau chargée d'énergie " + ef + ")"), impact_sats=[(9, ["nombre"])])
    for e, ef, k in (("lumineux", "lumineuse", "holy-ice"), ("ténébreux", "ténébreuse", "unholy-ice"))])

# ===== Relecture des glyphes, lot 1 : Abjuration (D&D 5e, 2024, 3.5) =====
FICHES["resistance"]["verb"] = V("intensite")                 # on amplifie la résistance, on ne la stabilise pas
FICHES["resistance"]["impact"] = (3, ["résistance"], "une résistance affermie un instant (1d4 ajouté à une sauvegarde)")
FICHES["aid"]["qty_cible"] = 3                                 # jusqu'à trois alliés
FICHES["pass-without-trace"]["qty_cible"] = P                  # le lanceur et tous ses compagnons proches
FICHES["beacon-of-hope"]["qty_cible"] = P                      # autant d'alliés que voulu
FICHES["magic-circle"]["cible_note"] = []                      # Cible 9 : tous les êtres qui relèvent d'un plan, sans liste
# Les aberrations relèvent elles aussi d'un plan : la Cible 9 suffit.
FICHES["protection-from-evil-and-good"]["impact_sats"] = [(9, ["cible"])]

# ===== Relecture des glyphes, lot 2 : Abjuration de Pathfinder 1 (1/3) =====
FICHES["abeyance"]["cible"] = 2
FICHES["ablative-sphere-garundi"].update(aoe={"type": "sphere", "size": 5}, impact=(P, ["abri"], "une sphère de cristal qui encaisse les coups à ta place"))
FICHES["allied-cloak"].update(cible_obj=["cape"], impact=(2, ["garde", "aide"], "une cape animée qui te garde et te prête main-forte"))
FICHES["animus-mine"].update(verb=V("force", True), cond=["esprit"], impact=(11, ["esprit", "chancellement"], "qui touche ton esprit en paie le prix (3d6), et chancelle"))
FICHES["anti-incorporeal-shell"].update(verb=V("force", True), aoe={"type": "sphere", "size": 10}, impact=(P, ["barrière"], "un dôme que les êtres sans corps ne peuvent franchir"), impact_sats=[(7, ["cible"])])
FICHES["arcana-theft"]["verb"] = V("flux")
FICHES["aura-of-inviolate-ownership"].update(cible=2, qty_cible=P)
FICHES["banishing-blade"].update(verb=V("force", True), cond=["coup"], impact=(P, [], "chaque coup de l'arme repousse l'adversaire"))
FICHES["bestow-grace"]["verb"] = INT
FICHES["blade-snare"].update(verb=REL, cond=["coup"], impact=(P, ["arme"], "l'arme qui te frappe reste prise"))
FICHES["blessing-of-liberty"]["cible"] = 1
FICHES["clay-skin"]["impact_sats"] = [(15, ["plafond"])]
FICHES["deflection"].update(verb=V("force", True), impact=(P, ["coup"], "les coups manqués reviennent sur leur auteur"))
# (lot 2, 2/3)
FICHES["free-spirit"]["cible"] = 1
FICHES["globe-of-tranquil-water"].update(aoe={"type": "sphere", "size": 20}, impact=(P, ["pluie", "brume"], "ni pluie, ni neige, ni brume n'entrent"))
FICHES["harvest-season"]["impact"] = (P, ["plante", "nourriture"], "une plante qui fleurit et fructifie d'un coup")
FICHES["homeward-bound"].update(verb=V("trame", True), cible=9)
FICHES["impenetrable-veil"]["verb"] = NVIS
FICHES["life-bubble"]["qty_cible"] = P
FICHES["magnetic-field"].update(verb=V("force"), aoe={"type": "sphere", "size": 30}, impact=(P, ["métal"], "le métal alentour attiré vers toi"))
FICHES["oath-of-peace"].update(impact=(5, ["paix", "garde", "résistance"], "mieux gardé et plus résistant, mais sans frapper (+5 à la CA et aux sauvegardes)"), fin=["agression"])
FICHES["rite-of-bodily-purity"]["cible"] = 1
FICHES["rite-of-centered-mind"]["cible"] = 1
FICHES["sacrificial-oath"]["impact"] = (P, ["sacrifice", "partage"], "tu prends ses blessures, longtemps")
# (lot 2, 3/3)
for k, why in {"word-of-resolve": "n'agit qu'avec les « auras de courage et de résolution » du paladin : pure mécanique de classe",
               "talisman-of-reprieve": "repose sur les « traits d'alignement » des plans, règle propre à la cosmologie de Pathfinder",
               "source-severance": "distingue magie profane et divine, distinction absente d'Inarama où la religion passe par l'Arcane",
               "numerological-resistance": "repose sur la « Voie des Nombres » de Golarion et sur des tirages de dés, comme les autres sorts de numérologie"}.items():
    FICHES.pop(k, None); PF1_RELECTURE[k] = why
FICHES["sphere-of-warding"].update(impact=(P, ["possession"], "les êtres sans corps arrêtés et chassés des corps volés"), impact_sats=[(7, ["cible"])])
FICHES["waterproof"].update(cible=1, cible_obj=["objet"])
FICHES["theft-ward"]["cible_obj"] = ["objet"]

# ===== Relecture des glyphes, lot 3 : Divination de D&D =====
FICHES["detect-evil-and-good"]["cible_note"] = []

# ===== Relecture des glyphes, lot 4 : Enchantement de D&D =====
# Le verbe d'un symbole suit l'effet qu'il déchaîne.
FICHES["symbol-of-sleep"]["verb"] = V("intensite", True)
FICHES["symbol-of-persuasion"]["verb"] = V("relation")
FICHES["symbol-of-stunning"]["verb"] = V("mouvement", True)
FICHES["symbol-of-insanity"]["verb"] = V("ordre", True)
FICHES["rage"]["impact"] = (2, ["fureur", "force", "endurance"], FICHES["rage"]["impact"][2])

# ===== Relecture des glyphes, lot 5 : Illusion de D&D =====
# La Cosmétique « sens trompé » compte les sens que l'illusion trompe ; l'Impact garde ce qu'on voit.
for k, n, imp in [("silent-image", 1, ["image"]), ("minor-image", 2, ["image"]), ("persistent-image", P, ["image", "scénario"]),
                  ("permanent-image", P, ["image"]), ("programmed-illusion", 2, ["image", "scénario"]), ("illusory-wall", 1, ["mur"]),
                  ("project-image", 2, ["double", "vue"]), ("disguise-self", 1, ["apparence"])]:
    old = FICHES[k].get("impact")
    FICHES[k]["impact"] = (P, imp, old[2] if old else "")
    FICHES[k]["cosm"] = (n, "sens trompé")
    for v in ("v35", "vpf", "v24"):
        if isinstance(FICHES[k].get(v), dict) and "cosm" in FICHES[k][v]: FICHES[k][v]["cosm"] = (n, "sens trompé")

# ===== Relecture des glyphes, lot 6 : Invocation de D&D =====
FICHES["conjure-animals"].update(cible=9, cible_note=["bête"])
FICHES["spirit-guardians"]["options"] = [O("Esprits gardiens — lumineux", impact=(14, ["lumière"], "3d8, la lumière des esprits de la face lumineuse")),
                                         O("Esprits gardiens — ténébreux", impact=(14, ["nécrose"], "3d8, la nécrose des esprits de la face ténébreuse"))]
FICHES["guardian-of-faith"]["impact_sats"] = [(60, ["plafond"])]

# ===== Relecture des glyphes, lot 7 : Nécromancie de D&D =====
FICHES["symbol-of-pain"]["verb"] = V("intensite", True)
FICHES["symbol-of-fear"]["verb"] = V("force", True)
FICHES["symbol-of-weakness"]["verb"] = V("intensite", True)
FICHES["symbol-of-death"]["verb"] = V("existence", True)
_p = FICHES["poison"].get("impact")
if _p: FICHES["poison"]["impact"] = (_p[0], ["poison", "endurance"], _p[2])

# ===== Relecture des glyphes, lot 8 : Transmutation de D&D =====
FICHES["control-water"]["impact"] = (P, ["inondation"], (FICHES["control-water"].get("impact") or (0, 0, ""))[2])
_s = FICHES["shrink-item"]["impact"]; FICHES["shrink-item"]["impact"] = (16, ["taille", "fractionné"], _s[2])
_t = FICHES["transformation"]["impact"]; FICHES["transformation"]["impact"] = (_t[0], ["force", "adresse", "endurance", "garde"], _t[2])

# ===== Relecture des glyphes, lot 9 : Évocation de D&D =====
FICHES["arcane-hand"]["impact"] = (18, [], "4d8 de force")
FICHES["sorcerous-burst"]["options"] = [dict(o, impact_sats=[(3, ["surcroît"])]) for o in FICHES["sorcerous-burst"]["options"]]

# ===== Relecture des glyphes, lot 10 : Divination de Pathfinder 1 =====
FICHES["create-treasure-map"].update(cible=1, cible_obj=["cadavre"], cond=[])
for _k, _w in [("heightened-awareness", ["perception", "mémoire"]), ("sensory-amplifier", ["perception", "vue"]),
               ("sarzari-shadow-memory", ["victime", "savoir"]), ("tap-inner-beauty", ["prestance"])]:
    _i = FICHES[_k]["impact"]; FICHES[_k]["impact"] = (_i[0], _w, _i[2])

# ===== Relecture des glyphes, lot 11 : Enchantement de Pathfinder 1 =====
for _k in ("charm-fey", "hold-fey"): FICHES[_k].update(cible=9, cible_note=["fée"], cond=[])
FICHES["covetous-urge"]["cond_sats"] = [(32, ["valeur"])]
FICHES["symbol-of-laughter"]["verb"] = V("ordre", True)
FICHES["symbol-of-distraction"]["verb"] = V("relation")
FICHES["symbol-of-strife"]["verb"] = V("relation", True)
FICHES["symbol-of-debauchery"]["verb"] = V("relation")
_i = FICHES["planeslayers-call"]["impact"]; FICHES["planeslayers-call"].update(impact=(_i[0], ["coup"], _i[2]), impact_sats=[(9, ["cible"])])
FICHES.pop("mad-sultans-melody", None)
PF1_RELECTURE["mad-sultans-melody"] = "ne touche que les vases, écartées, et imite les serviteurs d'un Dieu Extérieur de Golarion"

# ===== Relecture des glyphes, lot 12 : Illusion de Pathfinder 1 =====
_i = FICHES["haunting-mists"]["impact"]; FICHES["haunting-mists"]["impact"] = (_i[0], ["peur", "lucidité"], _i[2])
FICHES["phantasmal-revenge"].update(cible=1, cible_obj=["cadavre"], cond=[])
for _k, _n in [("vacuous-vessel", 2), ("alter-musical-instrument", 1), ("disguise-weapon", 1), ("adjustable-disguise", 1),
               ("shifted-steps", 1), ("illusory-hoard", P)]:
    FICHES[_k]["cosm"] = (_n, "sens trompé")

# ===== Relecture des glyphes, lot 13 : Invocation de Pathfinder 1 =====
_i = FICHES["blood-mist"]["impact"]; FICHES["blood-mist"]["impact"] = (_i[0], ["sang", "lucidité", "rage"], _i[2])
_i = FICHES["planar-inquiry"]["impact"]; FICHES["planar-inquiry"]["impact"] = (_i[0], ["savoir", "réponse"], _i[2])
FICHES["entice-fey-lesser"].update(cible_note=["fée"], cond=[])
FICHES["entice-fey-lesser"]["options"] = [dict(o, cond=[]) if isinstance(o, dict) and "cond" in o else o for o in FICHES["entice-fey-lesser"].get("options", [])]

# ===== Relecture des glyphes, lot 14 : Nécromancie de Pathfinder 1 =====
for _k, _w in [("blood-boil", ["sang", "endurance", "fatigue"]), ("phantom-blood", ["vie", "endurance"])]:
    _i = FICHES[_k]["impact"]; FICHES[_k]["impact"] = (_i[0], _w, _i[2])
_i = FICHES["calamitous-flailing"]["impact"]; FICHES["calamitous-flailing"]["impact"] = (4, _i[1], _i[2])

# ===== Relecture des glyphes, lot 15 : Évocation de Pathfinder 1 =====
# La force brute est un Impact nu (règle du lot 9) : le mot « force » ne s'écrit plus quand il dit des dégâts.
for _k in ("admonishing-ray", "battering-blast", "burst-of-force", "force-punch", "rend-body-i", "telekinetic-storm"):
    _i = FICHES[_k]["impact"]; FICHES[_k]["impact"] = (_i[0], [w for w in _i[1] if w != "force"], _i[2])
_i = FICHES["agonize"]["impact"]; FICHES["agonize"].update(cible=9, cond=[], impact=(_i[0], ["douleur", "obéissance"], _i[2]))
FICHES["pinecone-bomb"]["cible_obj"] = ["pigne"]
FICHES.pop("numerological-evocation", None)
PF1_RELECTURE["numerological-evocation"] = "repose sur la « Voie des Nombres » de Golarion, comme les autres sorts de numérologie"
FICHES["rend-body-i"]["options"] = [dict(o, impact=(o["impact"][0], [w for w in o["impact"][1] if w != "force"], o["impact"][2])) if isinstance(o, dict) and o.get("impact") else o for o in FICHES["rend-body-i"]["options"]]

# ===== Relecture des glyphes, lot 16 : Transmutation de Pathfinder 1 =====
_i = FICHES["crusaders-edge"]["impact"]; FICHES["crusaders-edge"].update(impact=(_i[0], ["arme", "hostile"], _i[2]), impact_sats=[(9, ["cible"])])
_i = FICHES["infuse-self"]["impact"]; FICHES["infuse-self"].update(impact=(_i[0], ["forme"], _i[2]), impact_sats=[(9, ["forme"])])
FICHES.pop("bone-flense", None)
PF1_RELECTURE["bone-flense"] = "n'agit qu'avec les armes des membres de la Mante rouge, une confrérie d'assassins de Golarion"
FICHES["sickening-entanglement"]["options"] = [dict(o, impact=(o["impact"][0], ["endurance" if w == "constitution" else w for w in o["impact"][1]], o["impact"][2])) if isinstance(o, dict) and o.get("impact") else o for o in FICHES["sickening-entanglement"]["options"]]
