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
# Technology Guide écarté. Les sorts non légaux en Pathfinder Society sont traités plus bas (« Pathfinder 1, suite »).
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

# ===== Décisions du 13 novembre : caractéristiques, peuples, classes, noms, illusions, grimoire =====
# 1. Table unique des caractéristiques : force, adresse, endurance, raison, lucidité, prestance.
_CARAC = {"charisme": "prestance", "constitution": "endurance", "dextérité": "adresse", "dexterite": "adresse",
          "intelligence": "raison", "sagesse": "lucidité"}
def _carac(x):
    if isinstance(x, list):
        return [(_CARAC[w.lower()].upper() if w.isupper() else _CARAC[w.lower()]) if isinstance(w, str) and w.lower() in _CARAC else _carac(w) for w in x]
    if isinstance(x, tuple): return tuple(_carac(w) for w in x)
    if isinstance(x, dict): return {k: _carac(v) for k, v in x.items()}
    return x
for _k in list(FICHES): FICHES[_k] = _carac(FICHES[_k])

# 3 et 4. Sorts rattachés à un peuple de Golarion ou à une classe : écartés.
for _k, _why in {"infuse-self": "les formes proposées sont des peuples nés d'outre-plan (aasimar, tieffelin, ifrit…)",
                 "elemental-mastery": "ne marche que si l'élément coule dans le sang du lanceur (ifrit, oréade…), peuples de Golarion",
                 "summon-totem-creature-shoanti": "sort des Shoantis, peuple de Golarion",
                 "fleshwarping-swarm-drow": "remodelage de chair des drows, peuple de Golarion",
                 "mark-of-spite": "sort des demi-drows, peuple de Golarion",
                 "arcane-disruption": "distingue magie profane et divine, distinction absente d'Inarama (comme Rupture de source)",
                 "huntmasters-spear": "s'appuie sur la liste d'ennemis jurés du rôdeur : mécanique de classe",
                 "blood-song": "ne transmet que des sorts de barde : mécanique de classe",
                 "ki-shout": "repose sur le ki du moine : mécanique de classe"}.items():
    FICHES.pop(_k, None); PF1_RELECTURE[_k] = _why

# 5. Noms sans trace de Golarion.
FICHES["light-of-iomedae"]["fr"] = "Lumière démasquante"
FICHES["leshy-swarm"]["fr"] = "Nuée d'esprits végétaux"

# 6. « Sens trompé » là où la source dit quels sens l'illusion trompe.
for _k, _n in [("mirage", 1), ("quintessence", 2), ("hallucinatory-decor", 3), ("echo", 1), ("open-and-shut", 1),
               ("decrepit-disguise", 1), ("illusion-of-calm", 1), ("horrific-doubles", 1), ("darting-duplicate", 1), ("hide-campsite", P)]:
    FICHES[_k]["cosm"] = (_n, "sens trompé")
FICHES["auditory-hallucination"]["options"] = [dict(o, cosm=(n, "sens trompé")) for o, n in zip(FICHES["auditory-hallucination"]["options"], [1, 2, P, P, P, P])]

# 7. Le grimoire n'était qu'un premier essai : ses sorts se génèrent depuis leurs données, comme les autres.
#    On garde les choix qui suivent les règles (verbe, combinaison quand un élément est en jeu, annotations utiles).
_G = {
 "spare-the-dying": dict(verb=V("ordre"), cible=2),
 "detect-magic": dict(verb=V("visibilite"), cible=1),
 "find-familiar": dict(verb=V("trame"), cible=7, comp=["ENCENS"]),
 "shield": dict(fam="H", comb="Acier", why="l'écran qui détourne le coup", cible=1, cond=["coup"]),
 "silent-image": dict(fam="H", comb="Plasma", why="la lumière qui trompe l'œil"),
 "thunderwave": dict(verb=V("force", True), cible=P),
 "enlarge-reduce": dict(verb=V("intensite"), cible=2, impact=(2, ["taille"], "taille doublée")),
 "gentle-repose": dict(verb=V("nature", True), cible=1, cible_obj=["cadavre"], comp=["SEL"]),
 "invisibility": dict(verb=V("visibilite", True), cible=2),
 "lesser-restoration": dict(verb=V("qualite"), cible=2),
 "levitate": dict(verb=V("mouvement"), cible=2),
 "mirror-image": dict(verb=V("identite", True), cible=1, impact=(3, ["image"], "trois doubles"), cosm=(1, "sens trompé")),
 "misty-step": dict(fam="H", comb="Brume", why="la brume argentée", cible=1),
 "scorching-ray": dict(verb=V("flux", True), cible=3, impact=(7, ["feu"], "2d6 par rayon"), qty=3),
 "animate-dead": dict(fam="H", comb="Sang", why="le sang rendu aux morts", cible=1, cible_obj=["os"]),
 "dispel-magic": dict(verb=V("relation", True)),
 "haste": dict(fam="R", art="chronomancie", verb=V("intensite"), cible=2, impact=(2, ["temps"], "le temps de la cible doublé")),
 "lightning-bolt": dict(fam="H", why="la foudre", cible=P),
 "meld-into-stone": dict(verb=V("identite"), cible=1, impact=(P, ["pierre"], "fondu dans la pierre")),
 "slow": dict(fam="R", art="chronomancie", verb=V("qualite", True), cible=3, impact=(2, ["temps", "fractionné"], "le temps des cibles réduit de moitié")),
 "banishment": dict(verb=V("trame", True), cible=9),
 "dimension-door": dict(fam="R", art="spatiomancie", verb=V("existence"), cible=2, qty_cible=2),
 "polymorph": dict(verb=V("nature"), cible=2, impact=(P, ["bête"], "changée en bête")),
 "conjure-elemental": dict(fam="H", comb="Air", why="l'élément appelé", cible=9, comp=["ENCENS"]),
 "contagion": dict(verb=V("qualite", True), cible=3),
 "telepathic-bond": dict(verb=V("relation"), cible=2, comp=["COQUILLES"]),
 "disintegrate": dict(verb=V("existence", True), cible=3, impact=(75, ["poussière"], "10d6 + 40 de force, réduite en poussière à 0")),
 "flesh-to-stone": dict(fam="H", comb="Roche", why="la chair changée en pierre", cible=3, impact=(P, ["pierre"], "pétrifiée")),
 "teleport": dict(fam="R", art="spatiomancie", verb=V("mouvement"), cible=2, qty_cible=9),
}
for _k, _d in _G.items():
    _f = FICHES[_k]; _f.pop("grimoire", None)
    for _x, _y in _d.items():
        if _x == "impact" or _x not in _f: _f[_x] = _y
    _f.setdefault("fam", "A")
FICHES["enlarge-reduce"]["alt"] = [dict(label="Rapetisser", verb=V("intensite", True), cible=3, impact=(2, ["taille", "fractionné"], "taille réduite de moitié"))]
FICHES["silent-image"]["alt"] = [dict(a, cosm=(1, "sens trompé"), impact=(P, ["image"], "")) if a.get("label") == "Forme arcane" else a for a in FICHES["silent-image"].get("alt", [])]
for _a in FICHES["gentle-repose"].get("alt", []):
    if _a.get("cible") == 4: _a.update(cible=1, cible_obj=["cadavre"])
FICHES["magic-missile"]["impact"] = (3, [], "1d4 + 1 de force par projectile")
# Symbole (5e) : un effet par forme, le verbe suit l'effet comme pour les symboles de la 3.5.
FICHES["symbol"] = dict(fr="Symbole", verb=V("visibilite"), cible=P, aoe={"type": "sphere", "size": 60}, cond=["déclencheur"], fin=["déclenchement"],
    comp=["MERCURE", "PHOSPHORE", "DIAMANT", "OPALE"], options=[
    O("Mort", verb=V("existence", True), impact=(55, ["nécrose"], "10d10")),
    O("Discorde", verb=V("relation", True), impact=(P, ["discorde"], "querelleuses, sans rien pouvoir dire de sensé")),
    O("Peur", verb=V("force", True), impact=(P, ["peur"], "effrayées, elles lâchent tout et fuient")),
    O("Désespoir", verb=V("intensite", True), impact=(P, ["désespoir"], "plus aucune envie de nuire")),
    O("Démence", verb=V("ordre", True), impact=(P, ["folie"], "folles pour une minute")),
    O("Douleur", verb=V("intensite", True), impact=(P, ["douleur"], "neutralisées par la douleur")),
    O("Sommeil", verb=V("intensite", True), impact=(P, ["sommeil"], "endormies dix minutes")),
    O("Étourdissement", verb=V("mouvement", True), impact=(P, ["étourdissement"], "étourdies"))])
FICHES["teleport"].update(cible=2, qty_cible=8, no_aoe=True, impact=(P, ["lieu", "passage"], "vers un lieu connu du même plan"))
FICHES["dimension-door"].update(cible=1, qty_cible=None, impact=(P, ["passage"], "une porte vers un lieu à portée"))
FICHES["dimension-door"].pop("qty_cible")
FICHES["symbol"]["dur"] = (P, None)

# ===== Refonte v2 : chaque sort relu en entier, tous ses cercles ensemble =====
# La face astrale d'un être visé se dit par un symbole en satellite de la Cible, pas par une annotation.
import unicodedata as _ud
def _nrm(w): return "".join(c for c in _ud.normalize("NFD", w) if _ud.category(c) != "Mn").upper()
def _faces(d):
    n = [w for w in (d.get("cible_note") or []) if _nrm(w) in ("LUMINEUX", "TENEBREUX")] if isinstance(d, dict) else []
    if n:
        d["cible_note"] = [w for w in d["cible_note"] if w not in n]
        d["cible_sym"] = [_nrm(w).lower() for w in n]
for _f in FICHES.values():
    _faces(_f)
    for _o in _f.get("options") or []: _faces(_o)
    for _a in _f.get("alt") or []: _faces(_a)
def RV(k, **kw):
    """relecture d'un sort : remplace les champs donnés ; opts={libellé: {champs}} retouche une option"""
    opts = kw.pop("opts", None); f = FICHES[k]
    for x, y in kw.items():
        if y is None: f.pop(x, None)
        else: f[x] = y
    if opts:
        f["options"] = [dict(o, **opts.get(o.get("label"), {})) for o in f["options"]]
def _dicts(f):
    out = [f]
    for x in f.get("options") or []: out.append(x)
    for x in f.get("alt") or []: out.append(x)
    for v in ("v24", "v35", "vpf"):
        if isinstance(f.get(v), dict):
            out.append(f[v])
            for x in f[v].get("options") or []: out.append(x)
            for x in f[v].get("alt") or []: out.append(x)
    return out
_REN = {"ESPRIT": "psyché", "PENSEE": "psyché"}
def MOVE(k, *words):
    """les mots qui disent la destination quittent l'Impact pour l'annotation de la Cible (esprit, pensée → psyché)"""
    W = {_nrm(w) for w in words}
    for d in _dicts(FICHES[k]):
        imp = d.get("impact")
        if imp and isinstance(imp[1], str): imp = d["impact"] = (imp[0], [imp[1]], *imp[2:])
        if not imp or not isinstance(imp[1], list): continue
        moved = [w for w in imp[1] if _nrm(w) in W]
        if not moved: continue
        d["impact"] = (imp[0], [w for w in imp[1] if _nrm(w) not in W], imp[2] if len(imp) > 2 else "")
        cn = list(d.get("cible_note") or (FICHES[k].get("cible_note") or [] if d is not FICHES[k] else []))
        for w in moved:
            w2 = _REN.get(_nrm(w), w)
            if _nrm(w2) not in {_nrm(x) for x in cn}: cn.append(w2)
        d["cible_note"] = cn
def DROP(k, *words):
    """mots retirés de l'Impact (dits ailleurs, en Cosmétique par exemple)"""
    W = {_nrm(w) for w in words}
    for d in _dicts(FICHES[k]):
        imp = d.get("impact")
        if imp and isinstance(imp[1], str): imp = (imp[0], [imp[1]], *imp[2:])
        if imp and isinstance(imp[1], list) and any(_nrm(w) in W for w in imp[1]):
            d["impact"] = (imp[0], [w for w in imp[1] if _nrm(w) not in W], imp[2] if len(imp) > 2 else "")
def SENS(k, *sens, manif=(), opt=None):
    """Cosmétique : les sens touchés (sens, intensité ou None) et ce qu'ils perçoivent"""
    d = FICHES[k] if opt is None else next(o for o in FICHES[k]["options"] if o["label"] == opt)
    d["sens"] = [s if isinstance(s, tuple) else (s, None) for s in sens]; d["manif"] = list(manif)

# ----- Refonte v2, lot A : Abjuration de D&D 5e -----
for _k, _w in [("resistance", ["résistance", "garde"]), ("mage-armor", ["garde"]), ("protection-from-evil-and-good", ["garde", "résistance"]),
               ("shield", ["garde", "projectile"]), ("shield-of-faith", ["garde", "foi"]), ("protection-from-poison", ["résistance"]),
               ("warding-bond", ["garde", "résistance"]), ("magic-circle", ["garde", "résistance"]), ("protection-from-energy", ["résistance"]),
               ("stoneskin", ["résistance", "coup", "garde"]), ("antilife-shell", ["vivant"]), ("dispel-evil-and-good", ["garde"]),
               ("holy-aura", ["garde", "résistance"]), ("mind-blank", ["esprit"])]:
    MOVE(_k, *_w)
RV("alarm", opts={"Alarme mentale": dict(impact=(P, ["alerte"], "un tintement dans l'esprit du lanceur")),
                  "Alarme sonore": dict(impact=(P, ["alerte"], "une clochette qui sonne dix secondes"), sens=[("ouïe", None)], manif=["clochette"])})
SENS("shield-of-faith", "vue", manif=["chatoiement"])
SENS("pass-without-trace", "vue", "ouïe", manif=["ombre", "silence"])
SENS("glyph-of-warding", "vue", manif=["glyphe"]); FICHES["glyph-of-warding"]["discret"] = 2
SENS("magic-circle", "vue", manif=["runes", "lueur"])
SENS("symbol", "vue", manif=["glyphe", "lueur"]); FICHES["symbol"]["discret"] = 4
SENS("holy-aura", "vue", manif=["lumière"]); DROP("holy-aura", "lumière")
SENS("antilife-shell", "vue", manif=["chatoiement"])
SENS("dispel-evil-and-good", "vue", manif=["chatoiement"])
SENS("globe-of-invulnerability", "vue", manif=["chatoiement"])
FICHES["prismatic-wall"].pop("cosm", None); SENS("prismatic-wall", "vue", manif=["couleurs", "lumière"])

# ----- Refonte v2, lot B : Divination de D&D 5e -----
# Pour Révéler, l'Impact dit le mode de la révélation (vision, lecture, présence…) ; ce qui est cherché va en Cible.
for _k, _w in [("guidance", ["aptitude"]), ("true-strike", ["coup"]), ("comprehend-languages", ["langue"]),
               ("detect-poison-and-disease", ["poison", "maladie"]), ("speak-with-animals", ["bête"]), ("detect-thoughts", ["pensée"]),
               ("find-traps", ["piège"]), ("locate-object", ["objet"]), ("see-invisibility", ["invisible", "éthéré"]),
               ("locate-creature", ["créature"]), ("commune-with-nature", ["terrain"]), ("telepathic-bond", ["pensée"]), ("foresight", ["garde"])]:
    MOVE(_k, *_w)
for _k, _w in [("detect-thoughts", ["lecture"]), ("see-invisibility", ["vision"]), ("detect-poison-and-disease", ["présence", "nature"])]:
    for _d in _dicts(FICHES[_k]):
        if _d.get("impact"): _d["impact"] = (_d["impact"][0], _w + [w for w in _d["impact"][1] if _nrm(w) not in {_nrm(x) for x in _w}], _d["impact"][2])
RV("detect-magic", cible=None)
RV("identify", cible_obj=["talisman"], impact=(P, ["savoir"], "ses propriétés et la manière de s'en servir"))
FICHES["identify"].get("vpf", {}).pop("impact", None)
RV("divination", cible=9, cible_note=["divinité"])

# ----- Refonte v2, lot C : Enchantement de D&D 5e -----
# Un enchantement qui prend l'esprit vise la psyché : la Cible le dit.
def PSY(*ks):
    for k in ks:
        for d in [FICHES[k]] + [x for x in _dicts(FICHES[k]) if x.get("cible_note")]:
            cn = list(d.get("cible_note") or [])
            if "psyché" not in cn: d["cible_note"] = cn + ["psyché"]
PSY("vicious-mockery", "animal-friendship", "charm-person", "command", "hideous-laughter", "sleep", "calm-emotions", "enthrall",
    "suggestion", "zone-of-truth", "compulsion", "confusion", "dominate-beast", "dominate-person", "geas", "irresistible-dance",
    "mass-suggestion", "dominate-monster", "feeblemind", "modify-memory")
for _k, _w in [("vicious-mockery", ["esprit"]), ("bane", ["coup", "résistance"]), ("bless", ["coup", "résistance"]),
               ("heroism", ["coup", "résistance", "aptitude"]), ("modify-memory", ["mémoire"]), ("feeblemind", ["esprit", "intellect", "prestance"])]:
    MOVE(_k, *_w)
for _d in _dicts(FICHES["geas"]):
    if _d.get("impact_sats"): _d["impact_sats"] = [(v, ["blessure"] if w == ["esprit"] else w) for v, w in _d["impact_sats"]]
for _d in _dicts(FICHES["feeblemind"]):
    if _d.get("impact_sats"): _d["impact_sats"] = [(v, ["raison"] if w == ["intellect"] else w) for v, w in _d["impact_sats"]]
    if _d.get("cible_note"): _d["cible_note"] = ["raison" if w == "intellect" else w for w in _d["cible_note"]]

# ----- Refonte v2, lot D : Illusion de D&D 5e -----
RV("minor-illusion", opts={o["label"]: dict(cosm=(1, "sens trompé")) for o in FICHES["minor-illusion"]["options"]})
for _k, _n in [("illusory-script", 1), ("blur", 1), ("major-image", 4), ("hallucinatory-terrain", 3), ("seeming", 1), ("mirage-arcane", 4)]:
    FICHES[_k]["cosm"] = (_n, "sens trompé")
DROP("mirage-arcane", "toucher")
SENS("color-spray", "vue", manif=["couleurs", "éclat"])
FICHES["hypnotic-pattern"].pop("cosm", None); SENS("hypnotic-pattern", "vue", manif=["couleurs", "motif"])
SENS("magic-mouth", "vue", "ouïe", manif=["bouche", "voix"])
SENS("silence", "ouïe", manif=["silence"])
for _k in ("invisibility", "greater-invisibility", "mislead"): FICHES[_k]["discret"] = True
PSY("fear", "hypnotic-pattern", "phantasmal-killer", "dream", "weird")
for _k in ("phantasmal-killer", "dream", "weird"): MOVE(_k, "esprit")
for _d in _dicts(FICHES["weird"]):
    if _d.get("impact_sats"): _d["impact_sats"] = [(v, ["blessure"] if w == ["esprit"] else w) for v, w in _d["impact_sats"]]

# ----- Refonte v2, lot E : Invocation de D&D 5e -----
# Les êtres invoqués vont en Cible ; l'Impact garde leur puissance, nue.
for _k, _w in [("conjure-animals", "bête"), ("conjure-minor-elementals", "élémentaire"), ("conjure-woodland-beings", "fée"),
               ("conjure-elemental", "élémentaire"), ("conjure-fey", "fée"), ("planar-ally", "élémentaire")]:
    MOVE(_k, _w)
for _k in ("conjure-celestial", "planar-ally"):
    for _d in _dicts(FICHES[_k]):
        imp = _d.get("impact")
        if imp and isinstance(imp[1], list) and any(_nrm(w) in ("ETRE",) for w in imp[1]):
            _d["impact"] = (imp[0], [w for w in imp[1] if _nrm(w) != "ETRE"], imp[2])
RV("conjure-celestial", opts={"Être lumineux": dict(cible_sym=["lumineux"], impact_sats=[]), "Être ténébreux": dict(cible_sym=["tenebreux"], impact_sats=[])})
for _d in _dicts(FICHES["conjure-celestial"]):
    if _d.get("impact") and isinstance(_d["impact"][1], list): _d["impact"] = (_d["impact"][0], [w for w in _d["impact"][1] if _nrm(w) not in ("LUMINEUX", "TENEBREUX")], _d["impact"][2])
MOVE("find-familiar", "familier"); MOVE("find-steed", "monture")
DROP("produce-flame", "lumière"); SENS("produce-flame", "vue", manif=["flamme", "lumière"])
SENS("mage-hand", "vue", manif=["main"])
SENS("entangle", "vue", manif=["lianes"])
DROP("fog-cloud", "brouillard"); SENS("fog-cloud", "vue", manif=["brouillard"])
SENS("grease", "vue", "toucher", manif=["graisse"])
SENS("flaming-sphere", "vue", manif=["flamme", "lumière"])
SENS("misty-step", "vue", manif=["brume"])
SENS("web", "vue", "toucher", manif=["toile"])
SENS("call-lightning", "vue", "ouïe", manif=["nuée", "éclair", "tonnerre"])
SENS("sleet-storm", "vue", "toucher", manif=["grésil", "pluie"])
SENS("spirit-guardians", "vue", manif=["esprits"])
SENS("stinking-cloud", "vue", "odorat", manif=["gaz", "puanteur"])
SENS("black-tentacles", "vue", manif=["tentacules"])
SENS("faithful-hound", "ouïe", manif=["aboiement"])
SENS("guardian-of-faith", "vue", manif=["gardien", "lueur"])
SENS("cloudkill", "vue", manif=["brume"])
SENS("insect-plague", "vue", "ouïe", manif=["criquets"])
SENS("teleportation-circle", "vue", manif=["cercle", "sigles"])
SENS("heroes-feast", "vue", "goût", "odorat", manif=["festin"])
SENS("wall-of-thorns", "vue", manif=["broussailles"])
SENS("magnificent-mansion", "vue", manif=["porte"])
SENS("demiplane", "vue", manif=["porte", "ombre"])
SENS("incendiary-cloud", "vue", manif=["fumée", "braises"])
SENS("gate", "vue", manif=["portail"])
SENS("storm-of-vengeance", "vue", "ouïe", manif=["orage", "éclairs", "tonnerre"])
FICHES["planar-ally"]["cible_sym"] = ["lumineux", "tenebreux"]
_i = FICHES["planar-ally"]["impact"]; FICHES["planar-ally"]["impact"] = (_i[0], [w for w in _i[1] if _nrm(w) not in ("LUMINEUX", "TENEBREUX")], _i[2])

# ----- Refonte v2, lot F : Nécromancie de D&D 5e -----
SENS("chill-touch", "vue", manif=["main", "spectre"])
SENS("ray-of-enfeeblement", "vue", manif=["rayon", "ténèbres"])
SENS("vampiric-touch", "vue", manif=["ombre"])
SENS("eyebite", "vue", manif=["regard", "ténèbres"]); PSY("eyebite")
MOVE("animate-dead", "mort-vivant"); MOVE("bestow-curse", "aptitude"); MOVE("speak-with-dead", "mort")
RV("create-undead", cible=1, cible_obj=["cadavre"]); MOVE("create-undead", "goule")

# ----- Refonte v2, lot G : Transmutation de D&D 5e -----
def OSENS(k, table):
    """Cosmétique par option : {libellé: (sens…, [manifestations])}"""
    for o in FICHES[k]["options"]:
        if o["label"] in table:
            *ss, m = table[o["label"]]; o["sens"] = [(s_, None) for s_ in ss]; o["manif"] = m
OSENS("druidcraft", {"Présage du temps": ("vue", ["signe"]), "Floraison": ("vue", "odorat", ["fleur"]),
                     "Effet sensoriel": ("vue", "ouïe", "odorat", "toucher", ["feuilles", "souffle", "odeur"]), "Flamme": ("vue", ["flamme"])})
OSENS("prestidigitation", {"Effet sensoriel": ("vue", "ouïe", "odorat", "toucher", ["étincelles", "souffle", "note", "odeur"]),
                           "Flamme": ("vue", ["flamme"]), "Saveur et température": ("goût", "toucher", ["saveur", "chaleur"]),
                           "Marque": ("vue", ["marque"])})
for o in FICHES["prestidigitation"]["options"]:
    if o["label"] == "Babiole": o["cosm"] = (1, "sens trompé")
OSENS("thaumaturgy", {"Voix tonnante": ("ouïe", ["voix"]), "Flammes": ("vue", ["flamme"]), "Tremblements": ("vue", "toucher", ["tremblement"]),
                      "Son": ("ouïe", ["son"]), "Porte": ("vue", "ouïe", ["porte", "claquement"]), "Regard": ("vue", ["regard"])})
for o in FICHES["thaumaturgy"]["options"]: o["impact"] = None
SENS("message", "ouïe", manif=["murmure"])
for _k, _w in [("shillelagh", "arme"), ("magic-weapon", "arme"), ("alter-self", "arme")]: DROP(_k, _w)
MOVE("barkskin", "garde"); SENS("barkskin", "vue", "toucher", manif=["écorce"])
MOVE("darkvision", "obscurité"); MOVE("gaseous-form", "résistance"); SENS("gaseous-form", "vue", manif=["brume"])
MOVE("speak-with-plants", "plante")
for o in FICHES["enhance-ability"]["options"]:
    w = {"Endurance de l'ours": "endurance", "Force du taureau": "force", "Grâce du félin": "adresse", "Splendeur de l'aigle": "prestance",
         "Ruse du renard": "raison", "Sagesse du hibou": "lucidité"}[o["label"]]
    i = o["impact"]; o["impact"] = (i[0], [x for x in i[1] if _nrm(x) not in ("ENDURANCE", "FORCE", "GRACE", "SPLENDEUR", "RUSE", "LUCIDITE")], i[2])
    o["cible_note"] = [w]
for o in FICHES["enhance-ability"]["v24"]["options"]:
    i = o.get("impact")
    if i: o["cible_note"] = [x for x in i[1] if _nrm(x) != "APTITUDE"]; o["impact"] = (i[0], [], i[2])
FICHES["control-water"]["impact_add"] = []
SENS("heat-metal", "vue", manif=["rougeoiement"])
SENS("knock", "ouïe", manif=["fracas"])
SENS("disintegrate", "vue", manif=["rayon"])
DROP("wind-walk", "nuage"); SENS("wind-walk", "vue", manif=["nuée"])
FICHES["sequester"]["discret"] = True

# ----- Refonte v2, lot H : Évocation de D&D 5e -----
def SENSL(table):
    """Cosmétique en série : {sort: (sens…, [manifestations])}"""
    for k, v in table.items():
        *ss, m = v; FICHES[k].pop("cosm", None) if FICHES[k].get("cosm") and "sens" not in str(FICHES[k]["cosm"][1]).lower() else None
        SENS(k, *ss, manif=m)
SENSL({"dancing-lights": ("vue", ["lueurs"]), "light": ("vue", ["lumière"]), "eldritch-blast": ("vue", "ouïe", ["rayon", "crépitement"]),
       "fire-bolt": ("vue", ["flamme"]), "ray-of-frost": ("vue", ["rayon"]), "sacred-flame": ("vue", ["flamme", "lumière"]),
       "shocking-grasp": ("vue", ["éclair"]), "burning-hands": ("vue", ["flammes"]), "faerie-fire": ("vue", ["lueur", "couleurs"]),
       "guiding-bolt": ("vue", ["éclair", "lueur"]), "magic-missile": ("vue", ["traits", "lueur"]), "thunderwave": ("ouïe", ["tonnerre"]),
       "acid-arrow": ("vue", ["flèche"]), "branding-smite": ("vue", ["lumière"]), "continual-flame": ("vue", ["flamme"]),
       "darkness": ("vue", ["ténèbres"]), "flame-blade": ("vue", ["lame", "flamme"]), "gust-of-wind": ("ouïe", "toucher", ["vent"]),
       "moonbeam": ("vue", ["rayon", "lune"]), "shatter": ("ouïe", ["fracas"]), "spiritual-weapon": ("vue", ["arme", "spectre"]),
       "daylight": ("vue", ["lumière"]), "fireball": ("vue", "ouïe", ["éclat", "grondement"]), "lightning-bolt": ("vue", "ouïe", ["éclair", "tonnerre"]),
       "tiny-hut": ("vue", ["dôme"]), "wind-wall": ("ouïe", "toucher", ["vent"]), "fire-shield": ("vue", ["flammes", "lumière"]),
       "ice-storm": ("vue", "ouïe", ["grêle"]), "resilient-sphere": ("vue", ["chatoiement"]), "wall-of-fire": ("vue", ["flammes"]),
       "arcane-hand": ("vue", ["main", "chatoiement"]), "cone-of-cold": ("toucher", ["souffle", "froid"]), "flame-strike": ("vue", "ouïe", ["colonne", "flammes"]),
       "blade-barrier": ("vue", "ouïe", ["lames"]), "chain-lightning": ("vue", "ouïe", ["éclairs"]), "freezing-sphere": ("vue", ["globe"]),
       "sunbeam": ("vue", ["rayon", "lumière"]), "arcane-sword": ("vue", ["épée"]), "delayed-blast-fireball": ("vue", ["perle", "lueur"]),
       "divine-word": ("ouïe", ["mot"]), "fire-storm": ("vue", "ouïe", ["flammes", "grondement"]), "prismatic-spray": ("vue", ["rayons", "couleurs"]),
       "earthquake": ("ouïe", "toucher", ["grondement", "secousse"]), "sunburst": ("vue", ["lumière"]), "meteor-swarm": ("vue", "ouïe", ["météores", "flammes"])})
MOVE("divine-favor", "coup"); MOVE("wind-wall", "projectile", "trait")

# ----- Refonte v2, lot I : sorts propres aux règles de 2024 -----
for _k in ("ice-knife", "mind-spike", "true-strike-2024"): FICHES[_k]["sans_parole"] = True
DROP("conjure-animals-2024", "meute", "esprit"); SENS("conjure-animals-2024", "vue", manif=["meute", "esprits"])
SENS("conjure-minor-elementals-2024", "vue", manif=["esprits", "tourbillon"])
RV("conjure-woodland-beings-2024", impact=(23, [], "5d8 dans l'esprit"), cible_note=["psyché"]); SENS("conjure-woodland-beings-2024", "vue", manif=["esprits"])
MOVE("conjure-fey-2024", "esprit"); SENS("conjure-fey-2024", "vue", manif=["esprit"])
SENS("conjure-celestial-2024", "vue", manif=["colonne", "lumière"])
SENS("conjure-elemental-2024", "vue", manif=["tourbillon"])
MOVE("resistance-2024", "garde"); DROP("true-strike-2024", "arme"); MOVE("aura-of-life", "résistance")
PSY("charm-monster")
SENS("dissonant-whispers", "ouïe", manif=["murmure"])
OSENS("elementalism", {"Appel de l'air": ("ouïe", "toucher", ["brise"]), "Appel de la terre": ("vue", ["poussière"]),
                       "Appel du feu": ("vue", "odorat", ["braise", "fumée"]), "Appel de l'eau": ("vue", "toucher", ["bruine"])})
SENS("ensnaring-strike", "vue", manif=["lianes"]); SENS("ice-knife", "vue", manif=["éclat"])
MOVE("phantasmal-force", "esprit")
SENS("ray-of-sickness", "vue", manif=["rayon"]); SENS("searing-smite", "vue", manif=["flammes"])
RV("sorcerous-burst", opts={"Esprit": dict(impact=(5, [], "1d8 dans l'esprit"), cible_note=["psyché"])}); SENS("sorcerous-burst", "vue", manif=["éclat"])
SENS("starry-wisp", "vue", manif=["lumière"])
DROP("summon-dragon", "esprit"); MOVE("summon-dragon", "dragon"); SENS("summon-dragon", "vue", manif=["dragon", "esprit"])
SENS("tsunami", "vue", "ouïe", manif=["vague"]); SENS("vitriolic-sphere", "vue", manif=["sphère"])

# ----- Refonte v2, lot J : Abjuration et Divination de D&D 3.5 -----
for _k, _w in [("entropic-shield", ["garde", "trait"]), ("protection-from-arrows", ["garde", "trait"]), ("resist-energy", ["résistance"]),
               ("shield-other", ["garde", "résistance"]), ("antiplant-shell", ["plante"]), ("repel-vermin", ["vermine"]),
               ("spell-resistance", ["résistance", "magie"]), ("protection-from-spells", ["résistance"]), ("stone-tell", ["pierre"]),
               ("detect-animals-or-plants", ["bête", "plante"]), ("detect-secret-doors", ["passage", "secret"]), ("detect-snares-and-pits", ["piège"])]:
    MOVE(_k, *_w)
DROP("explosive-runes", "force")
for _k, _w in [("detect-secret-doors", ["présence"]), ("detect-snares-and-pits", ["présence"])]:
    for _d in _dicts(FICHES[_k]):
        if _d.get("impact"): _d["impact"] = (_d["impact"][0], _w + list(_d["impact"][1]), _d["impact"][2])
RV("analyze-dweomer", cible_obj=["talisman"], impact=(P, ["savoir"], "les sorts et les propriétés magiques"))
SENSL({"entropic-shield": ("vue", ["couleurs", "lueur"]), "explosive-runes": ("vue", ["runes"]), "dimensional-anchor": ("vue", ["rayon"]),
       "dimensional-lock": ("vue", ["barrière", "émeraude"]), "arcane-sight": ("vue", ["regard", "lueur"]), "prying-eyes": ("vue", ["yeux"]),
       "prying-eyes-greater": ("vue", ["yeux"])})

# ----- Refonte v2, lot K : Enchantement, Illusion, Invocation de D&D 3.5 -----
def FACE(k):
    """un être invoqué d'une face du plan astral : « être » quitte l'Impact, la face devient un symbole sur la Cible"""
    for d in _dicts(FICHES[k]):
        imp = d.get("impact")
        if not imp or not isinstance(imp[1], list): continue
        f_ = [w for w in imp[1] if _nrm(w) in ("LUMINEUX", "TENEBREUX")]
        d["impact"] = (imp[0], [w for w in imp[1] if _nrm(w) not in ("LUMINEUX", "TENEBREUX", "ETRE")], imp[2] if len(imp) > 2 else "")
        if f_: d["cible_sym"] = [_nrm(w).lower() for w in f_]
PSY("daze", "daze-monster", "lullaby", "calm-animals", "charm-animal", "confusion-lesser", "hypnotism", "animal-trance", "crushing-despair",
    "geas-lesser", "mind-fog", "song-of-discord", "insanity", "demand", "symbol-of-persuasion", "symbol-of-insanity", "symbol-of-sleep",
    "touch-of-idiocy", "rainbow-pattern", "scintillating-pattern", "nightmare")
for _k, _w in [("touch-of-idiocy", ["intellect", "lucidité", "prestance"]), ("good-hope", ["coup", "résistance", "aptitude", "blessure"]),
               ("prayer", ["coup", "résistance", "aptitude", "blessure"]), ("crushing-despair", ["coup", "résistance", "aptitude", "blessure"]),
               ("heroism-greater", ["coup", "résistance", "aptitude"]), ("rage", ["force", "endurance"]), ("mind-fog", ["lucidité", "volonté"]),
               ("nightmare", ["esprit"]), ("mount", ["monture", "cheval"]), ("creeping-doom", ["nuée", "mille-pattes", "millepattes"]),
               ("elemental-swarm", ["élémentaire"]), ("shambler", ["tertre"]), ("glitterdust", ["invisible"])]:
    MOVE(_k, *_w)
for _d in _dicts(FICHES["touch-of-idiocy"]):
    if _d.get("cible_note"): _d["cible_note"] = ["raison" if w == "intellect" else w for w in _d["cible_note"]]
for o in FICHES["summon-swarm"]["options"]:
    i = o.get("impact")
    if i: o["cible_note"] = list(i[1]); o["impact"] = (i[0], [], i[2])
DROP("mind-fog", "brume"); SENS("mind-fog", "vue", manif=["brume"])
FICHES["ventriloquism"]["cosm"] = (1, "sens trompé"); FICHES["displacement"]["cosm"] = (1, "sens trompé")
for _k in ("persistent-image", "permanent-image"): FICHES[_k]["cosm"] = (4, "sens trompé")
for _k in ("rainbow-pattern", "scintillating-pattern"): FICHES[_k].pop("cosm", None); SENS(_k, "vue", manif=["motif", "couleurs"])
FACE("summon-monster-i"); DROP("summon-natures-ally-i", "bête"); DROP("summon-instrument", "instrument")
SENS("glitterdust", "vue", manif=["poussière", "or"]); SENS("sepia-snake-sigil", "vue", manif=["symbole", "serpent"])
for _k in ("solid-fog", "acid-fog"): DROP(_k, "brouillard"); SENS(_k, "vue", manif=["brouillard"])

# ----- Refonte v2, lot L : Nécromancie et Évocation de D&D 3.5 ; les symboles -----
PSY("cause-fear", "doom")
for _k, _w in [("doom", ["coup", "résistance", "aptitude"]), ("poison", ["endurance"]), ("symbol-of-pain", ["coup", "aptitude"]),
               ("symbol-of-weakness", ["force"]), ("consecrate", ["mort-vivant", "mortvivant"]), ("invisibility-purge", ["invisible"]),
               ("divine-power", ["force", "coup"])]:
    MOVE(_k, *_w)
DROP("helping-hand", "main"); DROP("holy-sword", "arme")
for _k in [k for k in FICHES if k.startswith("symbol-of") and not FICHES[k].get("sens")]: SENS(_k, "vue", manif=["glyphe", "lueur"])
SENSL({"disrupt-undead": ("vue", ["rayon"]), "spectral-hand": ("vue", ["main", "lueur"]), "enervation": ("vue", ["rayon", "ténèbres"]),
       "wail-of-the-banshee": ("ouïe", ["cri"]), "flare": ("vue", ["éclat"]), "sound-burst": ("ouïe", ["fracas"]), "helping-hand": ("vue", ["main"]),
       "searing-light": ("vue", ["rayon", "lumière"]), "shout": ("ouïe", ["cri"]), "shout-greater": ("ouïe", ["cri"]), "polar-ray": ("vue", ["rayon"]),
       "whirlwind": ("vue", "ouïe", ["tornade"]), "telekinetic-sphere": ("vue", ["chatoiement"])})

# ----- Refonte v2, lot M : Transmutation de D&D 3.5 -----
DROP("curse-water", "eau"); DROP("bless-weapon", "arme"); DROP("align-weapon", "arme"); DROP("magic-stone", "projectile")
DROP("spike-stones", "pierre")
for _k, _w in [("magic-fang", ["arme", "naturelle", "toutes"]), ("magic-vestment", ["garde"]), ("quench", ["feu"]),
               ("animal-growth", ["force"]), ("righteous-might", ["force"]), ("transformation", ["force", "adresse", "endurance", "garde"]),
               ("iron-body", ["garde"])]:
    MOVE(_k, *_w)
OSENS("pyrotechnics", {"Feux d'artifice": ("vue", "ouïe", ["étincelles", "éclat"]), "Fumée": ("vue", "odorat", ["fumée"])})
for o in FICHES["pyrotechnics"]["options"]:
    if o["label"] == "Fumée" and o.get("impact"): o["impact"] = (o["impact"][0], [w for w in o["impact"][1] if w != "fumée"], o["impact"][2])
SENS("whispering-wind", "ouïe", manif=["murmure"])
for o in FICHES["pyrotechnics"]["vpf"]["options"]:
    if o["label"] == "Fumée": o["impact"] = (o["impact"][0], [w for w in o["impact"][1] if w != "fumée"], o["impact"][2])
SENS("flame-arrow", "vue", manif=["flammes"])
FICHES["quench"]["impact_sats"] = [(18, ["élémentaire"])]
FICHES["rusting-grasp"]["impact_sats"] = [(11, ["créature"])]
DROP("secret-page", "écrit", "déguisement"); FICHES["secret-page"]["cosm"] = (1, "sens trompé")
DROP("arcane-mark", "rune"); SENS("arcane-mark", "vue", manif=["rune"])
DROP("liveoak", "arbre")
for o in FICHES["alarm"]["vpf"]["options"]:
    if o.get("impact"): o["impact"] = (o["impact"][0], [w for w in o["impact"][1] if w not in ("pensée", "son")], o["impact"][2])

# ----- Refonte v2, lot N : Abjuration de Pathfinder 1 -----
for _k, _w in [("allied-cloak", ["garde"]), ("clay-skin", ["garde", "coup"]), ("cloak-of-winds", ["garde"]), ("death-from-below", ["garde"]),
               ("gird-ally", ["garde"]), ("hedging-weapons", ["garde"]), ("mental-barrier-i", ["garde"]), ("nereids-grace", ["garde"]),
               ("oath-of-peace", ["garde", "résistance"]), ("protection-from-natural-attacks", ["garde"]), ("sanctify-armor", ["garde"]),
               ("shock-shield", ["garde"]), ("stunning-barrier", ["garde"]), ("tactical-formation", ["garde"]), ("veil-of-heaven", ["garde"]),
               ("veil-of-positive-energy", ["garde"]), ("ward-the-faithful", ["garde"]), ("wave-shield", ["garde"]), ("wreath-of-blades", ["garde"]),
               ("firewalkers-meditation", ["résistance"]), ("guarding-knowledge", ["résistance"]), ("hex-ward", ["résistance"]),
               ("bestow-grace", ["résistance"]), ("firebelly", ["résistance"]), ("rite-of-centered-mind", ["esprit", "résistance"]),
               ("thought-shield-i", ["esprit", "résistance"]), ("animus-mine", ["esprit"]), ("dream-shield", ["esprit"]),
               ("enshroud-thoughts", ["pensée"]), ("intellect-fortress-i", ["esprit"]), ("tower-of-iron-will-i", ["esprit"]),
               ("node-of-blasting", ["esprit"]), ("soul-vault", ["âme"]), ("dragon-turtle-shell", ["carapace"])]:
    MOVE(_k, *_w)
PSY("animus-mine", "dream-shield", "enshroud-thoughts", "intellect-fortress-i", "rite-of-centered-mind", "thought-shield-i",
    "tower-of-iron-will-i", "absolution", "hymn-of-peace", "miserable-pity", "node-of-blasting", "fools-forbiddance", "recentering-drone")
for _k, _w in [("absorb-rune-i", ["rune"]), ("book-ward", ["livre"]), ("caustic-safeguard", ["objet"]), ("sanctify-armor", ["armure"]),
               ("vestment-of-the-champion", ["armure"]), ("ward-shield", ["bouclier"]), ("harvest-season", ["plante"]),
               ("crimson-confession", ["marque", "rouge"]), ("peace-bond", ["rune"]), ("rune-of-warding", ["rune"]), ("woodland-rune", ["rune"])]:
    DROP(_k, *_w)
for _k in ("anti-incorporeal-shell", "sphere-of-warding"):      # « 7 cible » inventé : l'être visé est une condition
    for d in _dicts(FICHES[_k]): d.pop("impact_sats", None)
    FICHES[_k]["cond"] = list(FICHES[_k].get("cond") or []) + ["intangible"]
SENSL({"crimson-confession": ("vue", ["marque"]), "peace-bond": ("vue", ["rune", "lueur"]), "rune-of-warding": ("vue", ["rune"]),
       "woodland-rune": ("vue", ["rune"]), "medusas-bane": ("vue", ["miroir"]), "recentering-drone": ("ouïe", ["bourdon"]),
       "hedging-weapons": ("vue", ["arme"]), "wall-of-silver": ("vue", "ouïe", ["argent", "vibration"]),
       "wall-of-suppression": ("vue", ["étincelles"]), "undeath-ward": ("vue", ["argent"]), "sphere-of-warding": ("vue", ["lueur"]),
       "firebelly": ("toucher", ["chaleur"]), "wave-shield": ("vue", ["eau"]), "globe-of-tranquil-water": ("vue", ["eau"]),
       "wreath-of-blades": ("vue", ["dague"]), "cloak-of-winds": ("ouïe", ["hurlement"]), "stunning-barrier": ("vue", ["chatoiement"]),
       "veil-of-positive-energy": ("vue", ["lueur"])})
DROP("wreath-of-blades", "dague")
for _k in ("devil-snare", "diminished-detection", "impenetrable-veil", "obscure-poison", "shield-speech", "enshroud-thoughts",
           "sunder-breaker", "seers-bane", "blade-snare"):
    FICHES[_k]["discret"] = True

# ----- Refonte v2, lot O : Divination de Pathfinder 1 -----
for _k, _w in [("mind-thrust-i", ["esprit"]), ("mindlink", ["pensée"]), ("anticipate-thoughts", ["pensée"]), ("psychic-reading", ["pensée"]),
               ("heightened-awareness", ["mémoire"]), ("hypercognition", ["mémoire"]), ("share-memory", ["mémoire"]), ("seek-thoughts", ["pensée"]),
               ("mind-probe", ["mémoire"]), ("thoughtsense", ["pensée"]), ("dream-scan", ["pensée"]), ("synapse-overload", ["esprit"]),
               ("telepathy", ["pensée"]), ("truespeak", ["esprit"]), ("mindshock", ["esprit"]), ("tap-inner-beauty", ["prestance"]),
               ("perfect-placement", ["garde"]), ("battlemind-link", ["garde"]), ("soulseeker", ["âme"]), ("sense-vitals", ["vital"])]:
    MOVE(_k, *_w)
PSY("discern-next-of-kin", "detect-anxieties", "detect-desires", "mental-block", "reveal-emotions", "focused-scrutiny", "pack-empathy",
    "sense-fear", "build-trust", "domination-link")
for _k, _w in [("blood-biography", ["sang"]), ("kreightons-perusal", ["livre"]), ("rune-trace", ["rune"]), ("questing-stone", ["pierre"]),
               ("named-bullet", ["projectile"]), ("gilded-whispers", ["pièce"]), ("riversight", ["vue"])]:
    DROP(_k, *_w)
SENSL({"enchantment-sight": ("vue", ["iris"]), "commune-with-birds": ("ouïe", ["chant"]), "medusas-bane": ("vue", ["miroir"]),
       "eagle-eye": ("vue", ["capteur"]), "mark-of-obvious-ethics": ("vue", ["marque"]), "tap-inner-beauty": ("vue", "ouïe", ["regard", "voix"])})
DROP("mark-of-obvious-ethics", "marque")
for _k in ("mask-from-divination", "secret-speech", "seed-spies", "insect-spies", "gilded-whispers"):
    FICHES[_k]["discret"] = True

# ----- Refonte v2, lot P : Enchantement de Pathfinder 1 -----
# tout enchantement touche l'être en sa psyché : la Cible le dit
_ENCH_PF1 = ['abadars-truthtelling', 'blessing-of-the-watch', 'egorian-diplomacy', 'tieldlaras-feint', 'unwitting-ally', 'adoration', 'alluring-light', 'animal-purpose-training', 'aphasia', 'beguiling-gift', 'bungle', 'call-animal', 'challenge-evil', 'charm-fey', 'compel-hostility', 'compel-tongue', 'compulsive-liar', 'crime-of-opportunity', 'deja-vu', 'delusional-pride', 'demand-offering', 'fairness', 'forbid-action', 'fumbletongue', 'haunting-reminder', 'haze-of-dreams', 'ill-omen', 'implant-urge', 'intensify-psyche', 'keep-watch', 'knights-calling', 'litany-of-sloth', 'lock-gaze', 'make-lost', 'memorize-page', 'memory-lapse', 'moment-of-greatness', 'murderous-command', 'opportunistic-loyalty', 'rally-point', 'reveal-secrets', 'stalwart-resolve', 'swallow-your-fear', 'tactical-acumen', 'telempathic-projection', 'unbreakable-heart', 'unnatural-lust', 'unprepared-combatant', 'wartrain-mount', 'wrath', 'alpha-instinct', 'anonymous-interaction', 'aura-of-distraction', 'aura-of-the-unremarkable', 'aversion', 'babble', 'bestow-insight', 'bestow-weapon-proficiency', 'bleed-for-your-master', 'blessing-of-luck-and-resolve', 'blood-rage', 'burdened-thoughts', 'cacophonous-call', 'castigate', 'charitable-impulse', 'cognitive-block', 'compassionate-ally', 'confess', 'contagious-zeal', 'covetous-urge', 'curse-of-keeping', 'deflect-blame', 'delay-pain', 'emotive-block', 'false-belief', 'heckle', 'hidden-presence', 'hold-fey', 'hoodwink', 'id-insinuation-i', 'inflict-pain', 'investigative-mind', 'jealous-rage', 'litany-of-eloquence', 'mantle-of-calm', 'miasmal-dread', 'mindlocked-messenger', 'oppressive-boredom', 'passing-fancy', 'peacemakers-parley', 'psychic-leech', 'psychonaut-manifestation', 'puzzle-box', 'qualm', 'reckless-infatuation', 'reinvigorating-wind', 'righteous-vigor', 'seducers-eyes', 'sensory-overload', 'shamefully-overdressed', 'tactical-miscalculation', 'thought-worm-i', 'touch-of-mercy', 'unadulterated-loathing', 'vexing-miscalculation', 'animal-ambassador', 'apparent-treachery', 'battle-trance', 'bereave', 'bite-the-hand', 'champions-bout', 'companion-mind-link', 'control-summoned-creature', 'curse-of-disgust', 'daze-mass', 'demanding-message', 'ego-whip-i', 'false-alibi', 'fleeting-memory', 'gullibility', 'hollow-heroism', 'implanted-projection', 'inveigle-person', 'lovers-vengeance', 'malicious-spite', 'martial-marionette', 'mind-maze', 'mind-swap', 'nixies-lure', 'out-of-sight', 'overlook', 'overwhelming-grief', 'pillow-talk', 'seeds-of-influence', 'sequester-thoughts', 'sleepwalking-suggestion', 'smug-narcissism', 'stage-fright', 'symbol-of-laughter', 'synaptic-pulse', 'synaptic-scramble', 'terrible-remorse', 'they-know', 'triggered-suggestion', 'untold-wonder', 'utter-contempt', 'antithetical-constraint', 'cowards-lament', 'crime-wave', 'curse-of-the-outcast', 'debilitating-portent', 'debilitating-speech', 'envious-urge', 'forced-repentance', 'forgetful-slumber', 'foster-hatred', 'life-of-crime', 'litany-of-madness', 'lost-passage', 'mindwipe', 'moonstruck', 'shadow-of-doubt', 'sleepwalk', 'stay-the-hand', 'symbol-of-distraction', 'apathy', 'befuddled-combatant', 'burst-of-glory', 'compelling-rant', 'contagious-suggestion', 'dahaks-release', 'denounce', 'die-for-your-master', 'foe-to-friend', 'grand-destiny', 'hymn-of-mercy', 'pessimism', 'planeslayers-call', 'pox-of-rumors', 'seek-shelter', 'serenity', 'touch-of-slumber', 'cloak-of-dreams', 'lost-legacy', 'overwhelming-presence', 'phobia', 'pied-piping', 'primal-regression', 'psychic-surgery', 'repress-memory', 'symbol-of-strife', 'unconscious-agenda', 'vengeful-outrage', 'waves-of-ecstasy', 'euphoric-tranquility', 'symbol-of-debauchery', 'divide-mind', 'heroic-invocation', 'mind-swap-major']
for _k in _ENCH_PF1:
    MOVE(_k, "esprit", "pensée", "mémoire", "volonté", "ego")
PSY(*_ENCH_PF1)
for _d in _dicts(FICHES["confess"]):
    if _d.get("impact_sats"): _d["impact_sats"] = [(v, ["psyché" if _nrm(w) == "ESPRIT" else w for w in ws]) for v, ws in _d["impact_sats"]]
SENSL({"nixies-lure": ("ouïe", ["chant"]), "pied-piping": ("ouïe", ["musique"]), "alluring-light": ("vue", ["lumière"]),
       "cacophonous-call": ("ouïe", ["vacarme"]), "miasmal-dread": ("vue", "odorat", ["brume"]), "seducers-eyes": ("vue", ["regard"]),
       "babble": ("ouïe", ["babil"]), "litany-of-eloquence": ("ouïe", ["parole"]), "burst-of-glory": ("vue", ["éclat"])})
for _k, _w in [("nixies-lure", ["chant"]), ("pied-piping", ["chant"]), ("alluring-light", ["lumière"]), ("cacophonous-call", ["son"]),
               ("miasmal-dread", ["brume"])]:
    DROP(_k, *_w)
for _k in ("overlook", "out-of-sight", "hidden-presence", "aura-of-the-unremarkable", "anonymous-interaction", "sequester-thoughts"):
    FICHES[_k]["discret"] = True
for _d in _dicts(FICHES["ego-whip-i"]):
    if _d.get("cible_note"): _d["cible_note"] = ["prestance" if _nrm(w) == "EGO" else w for w in _d["cible_note"]]

# ----- Refonte v2, lot Q : Illusion de Pathfinder 1 -----
for _k, _w in [("mad-hallucination", ["esprit"]), ("dream-dalliance", ["psyché"]), ("thought-echo", ["pensée"]), ("jitterbugs", ["adresse"]),
               ("haunting-mists", ["lucidité"]), ("phantasmal-asphyxiation", ["souffle"]), ("oneiric-horror", ["force"])]:
    MOVE(_k, *_w)
PSY("mirror-mantis", "oneiric-horror", "mad-hallucination", "phantasmal-affliction", "phantasmal-asphyxiation", "phantasmal-reminder",
    "phantasmal-putrefaction", "phantasmal-web", "dream-dalliance", "night-terrors", "vision-of-lamashtu", "dreadscape", "haunting-mists",
    "paranoia", "negative-reaction", "jitterbugs", "absurdity", "synesthesia", "thought-echo", "minor-dream", "dream-council",
    "auditory-hallucination", "mantle-of-doubt", "impossible-angles", "isolate", "deceitful-veneer", "dream-reality", "placebo-effect")
for _k, _w in [("dazzling-blade", ["arme", "éclat"]), ("disguise-weapon", ["arme"]), ("hidden-blades", ["arme"]), ("quieting-weapons", ["arme"]),
               ("open-and-shut", ["porte"]), ("undetectable-trap", ["piège"]), ("obscured-script", ["écrit"]), ("geomessage", ["surface"]),
               ("stolen-light", ["gemme"]), ("instant-fake", ["objet"]), ("umbral-weapon", ["arme"]), ("wandering-star-motes", ["lumière"]),
               ("trail-of-the-rose", ["parfum"]), ("incessant-buzzing", ["guêpe"])]:
    DROP(_k, *_w)
SENSL({"dazzling-blade": ("vue", ["éclat"]), "incessant-buzzing": ("ouïe", ["bourdonnement"]), "clarion-call": ("ouïe", ["voix"]),
       "wandering-star-motes": ("vue", ["lueurs"]), "trail-of-the-rose": ("odorat", ["parfum"]), "wall-of-nausea": ("vue", ["mur"])})
FICHES["planetarium"]["cosm"] = (1, "sens trompé")
for _k in ("blend", "blurred-movement", "chameleon-stride", "hidden-blades", "hide-campsite", "invisibility-bubble", "muffle-sound",
           "selective-invisibility", "sunstalker", "shadowfade", "mask-dweomer", "undetectable-trap", "quieting-weapons", "respectful-quiet",
           "silent-table", "lose-the-trail", "village-veil", "deceptive-redundancy", "sympathetic-aura", "aura-alteration", "peerless-integrity",
           "false-future", "secret-sign", "illusory-hoard", "decrepit-disguise", "disguise-weapon", "ghostly-disguise", "adjustable-disguise",
           "hide-bruises", "quintessence", "shroud-of-innocuity", "open-and-shut", "implant-false-reading", "obscured-script", "geomessage"):
    FICHES[_k]["discret"] = True
for _d in _dicts(FICHES["dazzling-blade"]):
    if _d.get("impact") and not _d["impact"][1]: _d["impact"] = (_d["impact"][0], ["éblouissement"], _d["impact"][2])

# ----- Refonte v2, lot R : Invocation de Pathfinder 1 -----
def ETRE(k, *words):
    """l'être invoqué ou le lieu de destination passe sur la Cible, tel quel (un « esprit » invoqué n'est pas la psyché)"""
    _s = dict(_REN); _REN.clear()
    try: MOVE(k, *words)
    finally: _REN.update(_s)
for _k, _w in [("aquatic-cavalry", ["monture"]), ("calistrias-guardian-wasps", ["guêpe"]), ("cape-of-wasps", ["guêpe"]),
               ("draconic-ally", ["dragon", "serviteur"]), ("eagle-aerie", ["aigle", "monture"]), ("mad-monkeys", ["singe"]),
               ("leshy-swarm", ["esprit"]), ("bow-spirit", ["esprit"]), ("call-spirit", ["esprit"]), ("summon-ancestral-guardian", ["ancêtre", "esprit"]),
               ("bind-sage", ["savant"]), ("fleshworm-infestation", ["ver"]), ("frost-mammoth", ["mammouth"]), ("ghost-wolf", ["monture"]),
               ("flame-steed", ["monture"]), ("murderous-crow", ["corbeau"]), ("pernicious-pranksters", ["fée"]), ("phantom-driver", ["cocher"]),
               ("pocketful-of-vipers", ["vipère"]), ("rain-of-frogs", ["grenouille"]), ("release-the-hounds", ["loup"]),
               ("spectral-scout", ["bête"]), ("summon-elder-worm", ["ver"]), ("summon-flight-of-eagles", ["aigle", "monture"]),
               ("summon-froghemoth", ["batracien"]), ("summon-infernal-host", ["légion"]), ("summon-minor-ally", ["bête", "être"]),
               ("summon-stampede", ["aurochs"]), ("swarm-of-fangs", ["croc"]), ("vomit-swarm", ["araignée"]), ("whip-of-spiders", ["araignée", "millepattes", "fourmi"]),
               ("wicker-horse", ["monture"]), ("wooden-phalanx", ["golem"]), ("unseen-crew", ["équipage"]), ("phantom-chariot", ["cheval"]),
               ("ancestral-gift", ["ancêtre"]), ("masters-escape", ["invoqué"]), ("instant-restoration", ["invoqué"]),
               ("jannis-jaunt", ["plan"]), ("create-demiplane-lesser", ["plan"]), ("maddening-oubliette", ["plan"]), ("getaway", ["lieu"]),
               ("hostile-juxtaposition", ["lieu"]), ("dimensional-bounce", ["lieu"]), ("bilocation", ["lieu"]), ("surface-excursion", ["surface"]),
               ("soul-transfer", ["âme", "réceptacle"]), ("blood-mist", ["lucidité"]), ("resurgent-transformation", ["souffle"]),
               ("expel-blood", ["sang"]), ("seamantle", ["garde"]), ("murderous-crow", ["garde"]), ("calistrias-guardian-wasps", ["garde"])]:
    ETRE(_k, *_w)
for _k, _w in [("entice-fey-lesser", ["fée"]), ("curative-distillation", ["remède"]), ("returning-weapon", ["arme"]), ("restful-cloak", ["cape"]),
               ("secluded-grimoire", ["livre"]), ("light-of-iomedae", ["lumière"]), ("chains-of-light", ["lumière"]), ("dust-of-twilight", ["lumière"]),
               ("flame-steed", ["fumée"]), ("ghost-wolf", ["fumée"]), ("ash-storm", ["vue"]), ("sand-whirlwind", ["vue"]), ("path-of-glory", ["lueur"]),
               ("songbird", ["musique"]), ("solid-note", ["musique"])]:
    DROP(_k, *_w)
SENSL({"light-of-iomedae": ("vue", ["lumière"]), "chains-of-light": ("vue", ["lumière"]), "dust-of-twilight": ("vue", ["poussière", "lueur"]),
       "flame-steed": ("vue", "odorat", ["flammes", "fumée"]), "ghost-wolf": ("vue", ["fumée"]), "ash-storm": ("vue", ["cendre"]),
       "path-of-glory": ("vue", ["lueur"]), "songbird": ("ouïe", ["chant"]), "solid-note": ("ouïe", ["note"]),
       "music-of-the-spheres": ("ouïe", ["musique"]), "hallucinogenic-smoke": ("vue", "odorat", ["fumée"]),
       "nauseating-trail": ("odorat", ["puanteur"]), "wall-of-clockwork": ("vue", "ouïe", ["engrenages", "cliquetis"])})
for _k in ("sylvan-hideaway", "secluded-grimoire", "unseen-crew"):
    FICHES[_k]["discret"] = True
ETRE("leshy-swarm", "plante"); ETRE("jannis-jaunt", "élémentaire"); ETRE("summon-minor-ally", "petit")

# ----- Refonte v2, lot S : Nécromancie de Pathfinder 1 -----
for _k in ("psychic-crush-i", "sessile-spirit", "haunting-choir", "purge-spirit"): MOVE(_k, "esprit")
for _k, _w in [("bleed", ["sang"]), ("blood-boil", ["sang", "endurance"]), ("bloodbath", ["sang"]), ("fungal-infestation", ["sang"]),
               ("touch-of-bloodletting", ["sang"]), ("symbol-of-exsanguination", ["sang"]), ("vampiric-hunger", ["sang"]),
               ("suffocation", ["souffle"]), ("undines-curse", ["souffle"]), ("death-clutch", ["cœur"]), ("stricken-heart", ["cœur"]),
               ("boneshatter", ["os"]), ("boneshaker", ["os"]), ("wither-limb", ["membre"]), ("phantom-limb", ["membre", "esprit"]),
               ("decollate", ["tête"]), ("lipstitch", ["lèvre"]), ("depilate", ["poil"]), ("skinsend", ["peau"]), ("sweat-poison", ["peau"]),
               ("parasitic-soul", ["âme", "corps"]), ("possession", ["âme", "corps"]), ("soulswitch", ["âme"]), ("speak-with-soul", ["âme"]),
               ("death-knell-aura", ["âme"]), ("scourge-of-the-horsemen", ["âme"]), ("object-possession-lesser", ["âme"]),
               ("siphon-might", ["force"]), ("deadly-juggernaut", ["force"]), ("phantom-blood", ["endurance"]), ("khains-army", ["goule"]),
               ("skeleton-crew", ["squelette", "équipage"]), ("crafters-nightmare", ["esprit"]), ("entrap-spirit", ["esprit"]),
               ("speak-with-haunt", ["hantise"]), ("sands-of-time", ["âge"]), ("bone-fists", ["garde"]), ("defending-bone", ["garde"]),
               ("divine-transfer", ["garde"])]:
    ETRE(_k, *_w)
for _k, _w in [("bloody-arrows", ["trait"]), ("venomous-bolt", ["trait"]), ("reapers-coterie", ["arme"]), ("brow-gasher", ["arme"]),
               ("curse-item", ["objet"]), ("cursed-treasure", ["objet"]), ("decompose-corpse", ["cadavre"]), ("dress-corpse", ["cadavre"]),
               ("grasping-corpse", ["cadavre"]), ("grave-words", ["cadavre"]), ("natures-ravages", ["cadavre"]), ("restore-corpse", ["cadavre"]),
               ("sculpt-corpse", ["cadavre"]), ("deathwine", ["potion"]), ("skin-tag", ["nourriture"]), ("retributive-reparations", ["objet"]),
               ("object-possession-lesser", ["objet"]), ("corpse-lanterns", ["lumière"]), ("haunting-choir", ["chant"]), ("howling-agony", ["cri"]),
               ("barrow-haze", ["brume"])]:
    DROP(_k, *_w)
SENSL({"corpse-lanterns": ("vue", ["lueurs"]), "haunting-choir": ("ouïe", ["chant"]), "howling-agony": ("ouïe", ["cri"]),
       "banshee-blast": ("ouïe", ["cri"]), "barrow-haze": ("vue", ["brume"]), "virulent-miasma": ("vue", "odorat", ["brume", "miasme"]),
       "plague-storm": ("vue", "odorat", ["nuage"]), "wall-of-bone": ("vue", ["os"]), "flesh-wall": ("vue", "odorat", ["chair"])})
PSY("psychic-crush-i", "sessile-spirit", "haunting-choir", "aura-of-doom", "feast-on-fear", "garrulous-grin", "unsettling-presence",
    "persuasive-goad", "litany-of-admonition", "hydrophobia", "black-mark", "interrogation", "grim-stalker", "sadomasochism", "howling-agony")
FICHES["catatonia"]["discret"] = True

# ----- Refonte v2, lot T : Transmutation de Pathfinder 1 -----
# relecture systématique : l'objet déjà nommé sur la Cible quitte l'Impact ; les parts de l'être transformées passent sur la Cible
_TRA_PF1 = ['aboleths-lung', 'absorbing-inhalation', 'absorbing-touch', 'abstemiousness', 'accelerate-poison', 'acid-maw', 'acute-senses', 'adhesive-blood', 'adjustable-polymorph', 'adroit-retrieval', 'age-resistance-lesser', 'air-breathing', 'air-step', 'alchemical-allocation', 'alchemical-tinkering', 'aldori-alacrity', 'allfood', 'alter-river', 'alter-winds', 'amplify-elixir', 'anchored-step', 'angelic-aspect-lesser', 'animal-aspect', 'ant-haul', 'anthropomorphic-animal', 'ape-walk', 'arboreal-hammer', 'arodens-magic-army', 'arodens-spellsword', 'artificers-curse', 'aspect-of-the-bear', 'aspect-of-the-falcon', 'aspect-of-the-nightingale', 'aspect-of-the-stag', 'aspect-of-the-wolf', 'assume-appearance', 'atavism', 'badgers-ferocity', 'baphomets-blessing', 'beast-shape-i', 'billowing-skirt', 'binding-earth', 'blade-lash', 'blade-of-light', 'bladed-dash', 'blast-barrier', 'blessing-of-fervor', 'blessing-of-the-mole', 'blessing-of-the-salamander', 'blood-armor', 'blood-sentinel', 'bloodhound', 'body-capacitance', 'boiling-blood', 'bombers-eye', 'bowstaff', 'brand', 'break', 'bristle', 'brittle-portal', 'buoyancy', 'burning-disarm', 'burrow', 'burst-of-adrenaline', 'burst-of-insight', 'burst-of-speed', 'calcific-touch', 'call-weapon', 'carry-companion', 'carve-passage', 'caustic-blood', 'cauterizing-weapon', 'certain-grip', 'channel-vigor', 'charge-object', 'cheetahs-sprint', 'claim-identity', 'clear-grove', 'cloud-shape', 'codespeak', 'concealed-breath', 'condensed-ether', 'control-construct', 'conversing-wind', 'countless-eyes', 'crafters-fortune', 'create-holds', 'crimson-breath', 'crusaders-edge', 'cup-of-dust', 'curse-of-burning-sleep', 'dance-of-a-hundred-cuts', 'dancing-lantern', 'deft-digits', 'delectable-flesh', 'detoxify', 'dimensional-blade', 'diminish-resistance', 'disable-construct', 'disfiguring-touch', 'dissolution', 'divine-arrow', 'divine-pursuit', 'divine-vessel', 'dongun-shapers-touch', 'dragonvoice', 'drain-poison', 'dust-form', 'earth-tremor', 'echolocation', 'effortless-armor', 'eldritch-conduit', 'elemental-body-i', 'elude-time', 'emblazon-crest', 'emblem-of-greed', 'empower-holy-water', 'enemy-hammer', 'energy-hack', 'enhance-water', 'enlightened-step', 'enter-image', 'entomb', 'erode-defenses', 'eroding-ray', 'eruptive-pustules', 'ether-step', 'ethereal-fists', 'excruciating-deformation', 'expeditious-excavation', 'extreme-flexibility', 'eyes-of-the-void', 'fabricate-disguise', 'face-of-the-devourer', 'fair-is-foul', 'false-age', 'false-face', 'fear-the-sun', 'feast-of-ashes', 'feather-step', 'fey-form-i', 'form-of-the-dragon-i', 'giant-form-i', 'monstrous-physique-i', 'plant-shape-i', 'magical-beast-shape', 'fickle-winds', 'fiery-body', 'film-of-filth', 'fins-to-feet', 'fire-trail', 'firebrand', 'firefall', 'flames-of-the-faithful', 'fleeting-defect', 'fleshcurdle', 'flexile-curse', 'fluid-form', 'forced-quiet', 'fractions-of-heal-and-harm', 'frightful-aspect', 'frostbite', 'full-pouch', 'funereal-weapon', 'fungal-blisters', 'fury-of-the-sun', 'geniekind', 'ghost-brand', 'ghostbane-dirge', 'glide', 'golden-guise', 'gorums-armor', 'grappling-scarf', 'gravity-bow', 'gravity-sphere', 'gravity-well', 'green-caress', 'greensight', 'groundswell', 'hags-seasoning', 'hairline-fractures', 'hammer-of-mending', 'handy-grapnel', 'harmless-form', 'heart-of-the-mammoth', 'heart-of-the-metal', 'heavy-water', 'heightened-reflexes', 'hellmouth-lash', 'hidden-knowledge', 'hidden-speech', 'hidden-spring', 'hide-weapon', 'hobble', 'hollow-blades', 'holy-ice', 'holy-ice-weapon', 'hostile-levitation', 'hungry-earth', 'ice-armor', 'ice-body', 'inheritors-smite', 'innocence', 'innocuous-shape', 'instrument-of-agony', 'invigorating-poison', 'iron-spine', 'ironbeard', 'ironbloom-sprouts', 'irregular-size', 'jury-rig', 'keen-senses', 'kinetic-reverberation', 'lead-blades', 'liberating-command', 'life-channel', 'lighten-object', 'lightning-conductor', 'lily-pad-stride', 'linebreaker', 'liquefy', 'litany-of-defense', 'litany-of-vengeance', 'lockjaw', 'long-arm', 'longshot', 'magnifying-chime', 'malfunction', 'mantle-of-the-magic-warriors', 'marching-chant', 'marids-mastery', 'mark-of-blood', 'mark-of-buoyancy', 'martyrs-bargain', 'masters-mutation', 'masterwork-transformation', 'merge-with-familiar', 'miasmatic-form', 'mighty-strength', 'mirror-hideaway', 'mirror-polish', 'mirror-strike', 'mirror-transport', 'monkey-fish', 'monstrous-extremities', 'natural-rhythm', 'natures-exile', 'negate-aroma', 'oasis', 'obsidian-flow', 'overstimulate', 'parchment-swarm', 'particulate-form', 'peasant-armaments', 'perceive-cues', 'persistent-vigor', 'phantom-hunt', 'phasic-challenge', 'planar-adaptation', 'plant-voice', 'poisoned-egg', 'polar-midnight', 'polymorph-familiar', 'polypurpose-panacea', 'pouncing-fury', 'pup-shape', 'putrefy-food-and-drink', 'quick-change', 'raging-rubble', 'rags-to-riches', 'rapid-repair', 'ravens-flight', 'reboot', 'redcaps-touch', 'refine-improvised-weapon', 'reinforce-armaments', 'remarkable-legerdemain', 'reprobation', 'resilient-reservoir', 'resinous-skin', 'resist-starvation', 'resize-item', 'resonating-word', 'resounding-clang', 'revenant-armor', 'ride-the-waves', 'rigor-mortis', 'rivals-weald', 'ropeweave', 'rotgut', 'rovagugs-fury', 'rubberskin', 'rune-of-durability', 'rune-of-ruin', 'sabotage-construct', 'saddle-surge', 'salvage', 'sanctify-weapons', 'savage-maw', 'sawtooth-terrain', 'scamper', 'scent-trail', 'scorching-ash-form', 'scriveners-chant', 'sculpt-simulacrum', 'sculpted-cape', 'sea-of-dust', 'sea-steed', 'sebaceous-twin', 'seismic-fissure', 'serrens-armor-lock', 'serrens-swift-girding', 'shadow-body', 'shadowy-haven', 'shapechangers-gift', 'shield-of-shards', 'shifting-sand', 'sickening-entanglement', 'sickening-strikes', 'siege-of-trees', 'silk-to-steel', 'sky-steed', 'sky-swim', 'snake-staff', 'snapdragon-fireworks', 'snow-shape-ulfen', 'solidify-earth', 'sonic-form', 'spit-venom', 'splinter-spell-resistance', 'squeeze', 'staggering-fall', 'steady-saddle', 'steal-breath', 'stench-of-prey', 'stoke-the-inner-fire', 'stone-fist', 'stone-throwing', 'strangling-hair', 'strong-jaw', 'sturdy-tree-fort', 'submerge-ship', 'substitute-trail', 'sun-metal', 'suns-disdain', 'sundering-shards', 'surefoot-boots', 'swallow-poison', 'swarm-skin', 'sword-to-snake', 'symbol-of-slowing', 'tail-current', 'tail-strike', 'tailwind', 'tar-ball', 'tar-pool', 'tattoo-potion', 'telekinetic-assembly', 'telekinetic-maneuver', 'telekinetic-volley', 'temporal-divergence', 'temporary-graft', 'thorn-body', 'threefold-aspect', 'threefold-face', 'time-shudder', 'tireless-pursuit', 'touch-injection', 'touch-of-gracelessness', 'touch-of-the-sea', 'toxic-blood', 'transfer-tattoo', 'transfiguring-touch', 'transmute-blood-to-acid', 'transmute-golem', 'transmute-potion-to-poison', 'treasure-stitching', 'tripvine', 'twin-form', 'twisted-innards', 'twisted-space', 'undead-anatomy-i', 'underbrush-decoy', 'unerring-weapon', 'urban-grace', 'vengeful-stinger', 'venomous-bite', 'vermin-shape-i', 'versatile-weapon', 'vex-giant', 'vigor', 'violent-accident', 'vocal-alteration', 'waft', 'wandering-trail', 'wandering-weather', 'wave-form', 'weapon-of-awe', 'weapons-against-evil', 'weaponwand', 'wilderness-soldiers', 'wind-blades', 'windy-escape', 'wing-thorns', 'winged-sword', 'wizened-appearance', 'wooden-wing-shield', 'world-wave', 'wrathful-weapon', 'zephyrs-fleetness', 'zone-of-foul-flames']
_CORPS = ["souffle", "sang", "peau", "visage", "œil", "os", "membre", "corps", "chair", "jambe", "barbe", "voix", "bras", "cheveux",
          "queue", "articulation", "vital", "gueule", "poing", "force", "adresse", "endurance", "raison", "lucidité", "prestance", "garde"]
for _k in _TRA_PF1:
    _obj = [w for d in _dicts(FICHES[_k]) for w in (d.get("cible_obj") or [])]
    if _obj: DROP(_k, *_obj)
    ETRE(_k, *_CORPS)
    MOVE(_k, "esprit", "mémoire")
for _k, _w in [("magnifying-chime", ["son"]), ("resounding-clang", ["vibration"]), ("marching-chant", ["chant"]), ("snapdragon-fireworks", ["dragon"]),
               ("underbrush-decoy", ["bruissement"]), ("film-of-filth", ["puanteur"])]:
    DROP(_k, *_w)
SENSL({"magnifying-chime": ("ouïe", ["carillon"]), "resounding-clang": ("ouïe", ["fracas"]), "marching-chant": ("ouïe", ["chant"]),
       "snapdragon-fireworks": ("vue", "ouïe", ["étincelles", "dragon"]), "underbrush-decoy": ("ouïe", ["bruissement"]),
       "film-of-filth": ("odorat", ["puanteur"]), "fear-the-sun": ("vue", ["lumière"]), "emblazon-crest": ("vue", ["blason"]),
       "dancing-lantern": ("vue", ["lueur"]), "blade-of-light": ("vue", ["lumière"]), "eyes-of-the-void": ("vue", ["ténèbres"])})
PSY("burst-of-insight", "overstimulate", "frightful-aspect", "instrument-of-agony", "weapon-of-awe")
for _k in ("concealed-breath", "negate-aroma", "hidden-speech", "codespeak", "remarkable-legerdemain", "hide-weapon", "substitute-trail",
           "false-face", "fabricate-disguise", "false-age", "innocuous-shape", "claim-identity", "assume-appearance", "mirror-hideaway"):
    FICHES[_k]["discret"] = True

# ----- Refonte v2, lot U : Évocation de Pathfinder 1 -----
_EVO_PF1 = ['admonishing-ray', 'aggressive-thundercloud', 'agonize', 'air-geyser', 'apsus-shining-scales', 'archons-aura', 'archons-trumpet', 'augmenting-wall', 'ball-lightning', 'battering-blast', 'beacon-of-guilt', 'betraying-sting', 'biting-words', 'blast-of-wind', 'blazing-rainbow', 'blinding-ray', 'blistering-invective', 'blood-crow-strike', 'burn-corruption', 'burning-arc-keleshite', 'burning-entanglement', 'burning-gaze', 'burst-bonds', 'burst-of-force', 'burst-of-radiance', 'call-the-void', 'campfire-wall', 'chain-of-perdition', 'chains-of-fire', 'channel-the-gift', 'chord-of-shards', 'cleansing-fire', 'cold-ice-strike', 'contagious-flame', 'contingent-scroll', 'controlled-fireball', 'cosmic-ray', 'creeping-ice', 'damnation', 'dancing-darkness', 'daybreak-arrow', 'deadeyes-arrow', 'deadmans-contingency', 'deafening-song-bolt', 'decapitate', 'defensive-shock', 'detonate', 'discordant-blast', 'discovery-torch', 'distracting-cacophony', 'distressing-tone', 'dousing-rain', 'draconic-reservoir', 'dread-bolt', 'ear-piercing-scream', 'elemental-aura', 'elemental-touch', 'emergency-force-sphere', 'etheric-shards', 'explode-head', 'extreme-buoyancy', 'fiery-runes', 'final-sacrifice', 'fire-breath', 'fire-snake', 'fires-friend', 'firestream', 'flashfire', 'flickering-lights', 'flurry-of-snowballs', 'force-hook-charge', 'force-punch', 'force-sword', 'forceful-strike', 'frigid-touch', 'frost-fall', 'furious-fire-barrage', 'gentle-breeze', 'gozrehs-trident', 'gusting-sphere', 'heatstroke', 'holy-whisper', 'horn-of-pursuit', 'hungry-darkness', 'hydraulic-push', 'hydraulic-torrent', 'ice-slick', 'icy-prison', 'incorporeal-chains', 'jolting-portent', 'last-azlantis-defending-sword', 'lead-anchor', 'leashed-shackles', 'light-lance', 'light-prison', 'lightning-arc', 'lightning-lash', 'litany-of-order', 'litany-of-righteousness', 'litany-of-thunder', 'mages-decree', 'martial-telekinesis', 'molten-orb', 'moonrise-arrow', 'morning-sun', 'motes-of-dusk-and-dawn', 'mydriatic-spontaneity', 'neutral-buoyancy', 'night-of-blades', 'pain-strike', 'pale-flame', 'path-of-the-winds', 'piercing-shriek', 'pilfering-hand', 'pinecone-bomb', 'poison-breath', 'protective-penumbra', 'pyrotechnic-eruption', 'rebuke', 'reflexive-barrier', 'rend-body-i', 'resounding-blow', 'revealing-light', 'ricochet-shot', 'ride-the-lightning', 'river-of-wind', 'rope-tornado', 'runic-overload', 'sacred-nimbus', 'sacred-space', 'sanctify-corpse', 'scouring-winds', 'screaming-flames', 'sheet-lightning', 'shield-of-darkness', 'shield-of-the-dawnflower', 'shifting-shadows', 'shining-cord', 'shroud-of-darkness', 'siege-scatter', 'sign-of-wrath', 'silverlight', 'sirocco', 'snowball', 'sonic-scream', 'sonic-thrust', 'spark', 'spellcasting-contract-lesser', 'spiritual-ally', 'spiritual-squire', 'spontaneous-immolation', 'spotlight', 'steam-ray-fusillade', 'stormbolts', 'suppressing-stone', 'symbol-of-storms', 'tamers-lash', 'telekinetic-charge', 'telekinetic-projectile', 'telekinetic-storm', 'telekinetic-strikes', 'thundering-drums', 'thunderstomp', 'touch-of-combustion', 'tracking-mark', 'transfer-familiar', 'trial-by-fire', 'trial-of-fire-and-acid', 'twilight-knife', 'unbearable-brightness', 'unflappable-mien', 'unwelcome-halo', 'vengeful-comets', 'vitriolic-mist', 'volcanic-storm', 'vortex', 'wake-of-light', 'wall-of-sound', 'wall-of-split-illumination', 'winds-of-vengeance', 'wrathful-mantle']
_VUE = {"LUMIERE": "lumière", "SOLEIL": "lumière", "HALO": "halo", "AUBE": "lueur", "ETINCELLE": "étincelles", "FUMEE": "fumée",
        "TENEBRES": "ténèbres", "OMBRE": "ombre", "ARC": "arc-en-ciel"}
_OUIE = {"SON": "son", "CRI": "cri", "CHANT": "chant", "MUSIQUE": "musique", "BRUIT": "vacarme", "MURMURE": "murmure", "TROMPETTE": "trompette"}
for _k in _EVO_PF1:
    _obj = [w for d in _dicts(FICHES[_k]) for w in (d.get("cible_obj") or [])]
    if _obj: DROP(_k, *_obj)
    ETRE(_k, "tête", "membre", "garde")
    _imp = FICHES[_k].get("impact"); _ws = [_nrm(w) for w in (_imp[1] if _imp and isinstance(_imp[1], list) else [])]
    _s, _m = [], []
    if any(w in _VUE for w in _ws): _s.append("vue"); _m += [_VUE[w] for w in _ws if w in _VUE]
    if any(w in _OUIE for w in _ws): _s.append("ouïe"); _m += [_OUIE[w] for w in _ws if w in _OUIE]
    if _s and not FICHES[_k].get("sens"): SENS(_k, *_s, manif=list(dict.fromkeys(_m)))
SENSL({"archons-trumpet": ("ouïe", ["trompette"]), "fire-snake": ("vue", ["serpent"]), "screaming-flames": ("vue", "ouïe", ["flammes", "cri"]),
       "thundering-drums": ("ouïe", ["tambours"]), "deafening-song-bolt": ("ouïe", ["chant"]), "flashfire": ("vue", ["fumée", "flammes"])})
DROP("flashfire", "fumée"); DROP("burning-entanglement", "fumée"); SENS("burning-entanglement", "vue", manif=["fumée"])
PSY("agonize", "blistering-invective", "holy-whisper", "rebuke", "dread-bolt", "suppressing-stone", "mydriatic-spontaneity")
MOVE("suppressing-stone", "esprit")
# Vraie parole : comprendre et parler toute langue, ce n'est pas toucher la psyché (sinon elle se confond avec Télépathie)
for _d in _dicts(FICHES["truespeak"]):
    _d.pop("cible_note", None)
    if _d.get("impact"): _d["impact"] = (_d["impact"][0], ["parole", "langue"], _d["impact"][2])

# ----- Décisions du 13 novembre (soir) -----
# 1. Rayonnement et nécrose s'écrivent par les symboles des faces (moteur). La lumière qui ne frappe pas reste lumière vue :
DROP("produce-flame", "lumière")
FICHES["true-strike-2024"]["rayonnement"] = True
# 2. Contresort, dissipation : Cible vide, la trame, annotée « sort » (ou « magie » quand c'est toute magie)
for _k, _n in [("counterspell", "sort"), ("dispel-magic", "sort"), ("dispel-magic-greater", "sort"), ("symbol-of-dispelling", "sort"),
               ("antimagic-field", "magie"), ("mages-disjunction", "magie")]:
    for _d in _dicts(FICHES[_k]):
        if _d is FICHES[_k] or "cible" in _d: _d["cible"] = "trame"
    FICHES[_k]["cible_note"] = [_n]
    DROP(_k, _n)
    FICHES[_k]["notes"] = [n for n in (FICHES[_k].get("notes") or []) if not n.startswith("Cible vide")]
# 3. Les êtres créés vont en Cible (7 : un être sans corps propre, fait de force ou de fantasme)
RV("unseen-servant", cible=7, cible_note=["serviteur"]); DROP("unseen-servant", "serviteur")
RV("phantom-steed", cible=7, cible_note=["monture"]); DROP("phantom-steed", "monture")
RV("faithful-hound", cible=7, cible_note=["molosse"])
for _d in _dicts(FICHES["produce-flame"]):
    if _d.get("impact_add"): _d["impact_add"] = [w for w in _d["impact_add"] if _nrm(w) != "LUMIERE"]

# ----- Décisions du 13 novembre (nuit) : les satellites -----
def RESAT(k, old, new):
    """remplace (ou retire si new vaut None) les satellites d'Impact annotés old ; new peut être une fonction (v, mots) → satellite"""
    O_ = [_nrm(w) for w in old]
    for d in _dicts(FICHES[k]):
        if not d.get("impact_sats"): continue
        out = []
        for st in d["impact_sats"]:
            if [_nrm(w) for w in (st[1] or [])] == O_:
                if new is None: continue
                st = new(*st[:2]) if callable(new) else (st[0], list(new))
            out.append(st)
        d["impact_sats"] = out
def CN(k, *ws):
    """ajoute des précisions à la Cible (sur la fiche et ses versions qui la redisent)"""
    for d in [FICHES[k]] + [x for x in _dicts(FICHES[k]) if x.get("cible_note")]:
        cn = list(d.get("cible_note") or [])
        d["cible_note"] = cn + [w for w in ws if _nrm(w) not in {_nrm(x) for x in cn}]
_CAR = {"FORCE": "force", "DEXTERITE": "adresse", "CONSTITUTION": "endurance", "INTELLIGENCE": "raison", "INTELLECT": "raison",
        "SAGESSE": "lucidité", "CHARISME": "prestance"}

# Famille A — deuxième grandeur : valeur + unité, gardée ; ce qui a un meilleur cercle y va
RESAT("tree-stride", ["mètres"], None); FICHES["tree-stride"]["loc"] = (150, "METRES", "150 m, d'arbre en arbre")
RESAT("antipathy-sympathy", ["mètres"], None); FICHES["antipathy-sympathy"].update(no_aoe=False, aoe={"type": "sphere", "size": 120})
for o in FICHES["dragons-breath"]["options"]: o.pop("impact_sats", None)
FICHES["dragons-breath"]["aoe"] = {"type": "cone", "size": 15}
RESAT("create-food-and-water", ["litres", "eau"], None); FICHES["create-food-and-water"].update(qty=112, qty_note=["litres", "eau"])
for _k in ("sending", "magic-mouth", "animal-messenger", "demand"):
    if any([_nrm(w) for w in (st[1] or [])] == ["MOTS"] for d in _dicts(FICHES[_k]) for st in (d.get("impact_sats") or [])):
        RESAT(_k, ["mots"], None); FICHES[_k].update(qty=25, qty_note=["mots"])
RESAT("tiny-hut", ["occupants"], None); FICHES["tiny-hut"].update(qty_cible=9); CN("tiny-hut", "occupants")
RESAT("modify-memory", ["minutes"], None); FICHES["modify-memory"]["sats"] = {"LOCALISATION": [(5, ["minutes", "passé"])]}   # la portée garde sa valeur ; le passé atteint en satellite
RESAT("divination", ["jours"], None); FICHES["divination"]["loc"] = (7, ["JOURS", "AVENIR"], "7 jours dans l'avenir")
RESAT("augury", ["minutes", "avenir"], None); FICHES["augury"]["loc"] = (30, ["MINUTES", "AVENIR"], "30 minutes dans l'avenir")

# Famille B — ce qui a sa place ailleurs
RESAT("finger-of-death", ["zombi"], ["mort-vivant"])
RESAT("cone-of-cold", ["statue"], None); SENS("cone-of-cold", "vue", manif=["statue", "givre"])
for _k in ("branding-smite", "starry-wisp"):
    RESAT(_k, ["révélation"], None); RESAT(_k, ["révélation", "marque"], ["marque"])
SENS("branding-smite", "vue", manif=["lueur"]); SENS("starry-wisp", "vue", manif=["lueur"])
RESAT("freezing-sphere", ["gel", "eau"], None); CN("freezing-sphere", "eau")
RESAT("ice-knife", ["froid"], lambda v, w: (v, [])); FICHES["ice-knife"]["impact_add"] = list(FICHES["ice-knife"].get("impact_add") or [])
for _d in _dicts(FICHES["ice-knife"]):
    if _d.get("impact_sats"): _d["impact_sats"] = [st for st in _d["impact_sats"] if st[1]] + [(st[0], []) for st in _d["impact_sats"] if not st[1]]
_EU = {"FROID": ["air", "terre", "eau", "eau"], "FEU": ["feu"]}
for _d in _dicts(FICHES["fire-shield"]):
    _new = []
    for st in _d.get("impact_sats") or []:
        _n = [_nrm(x) for x in st[1]]
        if _n[:1] == ["RESISTANCE"] and len(_n) == 2: _new += [(st[0], ["résistance"])] + [(("sym", u), []) for u in _EU[_n[1]]]
        else: _new.append(st)
    if _d.get("impact_sats"): _d["impact_sats"] = _new
RESAT("cloudkill", ["constitution"], lambda v, w: (v, ["affaiblissement"])); FICHES["cloudkill"]["v35"]["cible_note"] = ["endurance"]
RESAT("feeblemind", ["intellect"], None); CN("feeblemind", "raison")
# Contact avec les plans : c'est le lanceur qui risque sa raison, pas l'être contacté — la perte reste un effet secondaire
RESAT("contact-other-plane", ["intellect", "charisme"], lambda v, w: (v, ["raison", "prestance"]))
RESAT("contact-other-plane", ["esprit", "folie"], lambda v, w: (v, ["folie"]))
for _k in ("power-word-kill", "weird", "geas"):
    RESAT(_k, ["esprit"], lambda v, w: (v, [])); CN(_k, "psyché")

# Famille C — le satellite porte sa propre Condition
for _k in ("planeslayers-call", "crusaders-edge"): RESAT(_k, ["cible"], lambda v, w: (P, ["si:plan"]))
RESAT("protection-from-evil-and-good", ["cible"], lambda v, w: (P, ["si:plan"]))
for _k in ("anti-incorporeal-shell", "sphere-of-warding"): RESAT(_k, ["cible"], None)
RESAT("searing-light", ["mort-vivant"], lambda v, w: (v, ["si:mort-vivant"]))
RESAT("divine-smite", ["fiélon", "mort-vivant"], lambda v, w: (v, ["si:ténébreux", "si:mort-vivant"]))
RESAT("forbiddance", ["hostile"], lambda v, w: (v, ["si:hostile"]))
RESAT("protection-from-evil-and-good", ["invoqué"], lambda v, w: (v, ["renvoi", "si:invoqué"]))
RESAT("magic-circle", ["invoqué", "barrière"], lambda v, w: (v, ["barrière", "si:invoqué"]))
RESAT("quench", ["élémentaire"], lambda v, w: (v, ["si:élémentaire"]))
RESAT("rusting-grasp", ["créature"], lambda v, w: (v, ["si:fer"]))
RESAT("confess", ["esprit"], lambda v, w: (v, ["si:mensonge"])); RESAT("confess", ["psyché"], lambda v, w: (v, ["si:mensonge"]))
RESAT("aura-of-life", ["vie", "mourant"], lambda v, w: (v, ["vie", "si:mourant"]))
for _o in FICHES["hallow"].get("options") or []:
    if _o.get("impact_sats"):
        _o["impact_sats"] = [(v, [w if _nrm(w) not in ("MORTVIVANT", "MORT-VIVANT") and w != "mort-vivant" else "si:mort-vivant" for w in ws]) for v, ws in _o["impact_sats"]]

# Famille D — les règles de jeu
for _o in FICHES["sorcerous-burst"]["options"]: _o.pop("impact_sats", None)
RESAT("harm", ["maximum"], lambda v, w: (1, ["plancher"]))
for _o in FICHES["chromatic-orb"]["options"]: _o["impact_sats"] = [st for st in (_o.get("impact_sats") or []) if [_nrm(x) for x in st[1]] != ["REBOND"]]
FICHES["chromatic-orb"]["qty_cible"] = 2; CN("chromatic-orb", "rebond")
RESAT("regenerate", ["vie", "tour"], None); FICHES["regenerate"]["sats"] = {"DUREE": [(1, ["vie", "tour"])]}
RESAT("geas", ["blessure", "jour"], None); FICHES["geas"]["sats"] = {"DUREE": [(11, ["blessure", "jour"])]}
RESAT("geas-lesser", ["aptitude", "jour"], None); FICHES["geas-lesser"]["sats"] = {"DUREE": [(2, ["aptitude", "jour"])]}
RESAT("cloudkill", ["seuil", "vie"], None)
FICHES["cloudkill"]["v35"]["cond"] = list(FICHES["cloudkill"]["v35"].get("cond") or []) + ["seuil"]; FICHES["cloudkill"]["v35"]["cond_sats"] = [(27, ["vie"])]
for _o in FICHES["entice-fey-lesser"]["options"]:
    _ss = [st for st in (_o.get("impact_sats") or []) if [_nrm(x) for x in st[1]] == ["VIE", "PLAFOND"]]
    if _ss: _o["impact_sats"] = []; _o["cond"] = ["seuil"]; _o["cond_sats"] = [(_ss[0][0], ["vie"])]
RESAT("transformation", ["sort", "interdit"], lambda v, w: (v, ["incantation"]))
for _o in FICHES["hex"]["options"]:
    _w = [x for x in _o["impact_sats"][0][1] if _nrm(x) != "MALADRESSE"][0]
    _o["impact_sats"] = [(P, ["maladresse"])]; _o["cible_note"] = [_CAR.get(_nrm(_w), _w)]
RESAT("holy-aura", ["force", "faiblesse"], lambda v, w: (v, ["affaiblissement"]))
for _o in _dicts(FICHES["holy-aura"]):
    if any(_nrm(x) == "AFFAIBLISSEMENT" for st in (_o.get("impact_sats") or []) for x in st[1]): _o["cible_note"] = ["force"]
RESAT("contact-other-plane", ["intellect", "prestance"], lambda v, w: (v, ["raison", "prestance"]))
RESAT("cloudkill", ["endurance"], lambda v, w: (v, ["affaiblissement"]))
for _v in ("v35", "vpf"):
    if isinstance(FICHES["cloudkill"].get(_v), dict):
        FICHES["cloudkill"][_v]["cible_note"] = ["endurance"]
        FICHES["cloudkill"][_v]["cond"] = ["seuil"]; FICHES["cloudkill"][_v]["cond_sats"] = [(27, ["vie"])]

# ----- Passe fine Pathfinder 1, lot V : Abjuration (relue sort par sort contre le texte entier) -----
def IMPW(k, words, value=None, why=None):
    """réécrit les mots (et au besoin la valeur) de l'Impact, sur la fiche et toutes ses formes"""
    for d in _dicts(FICHES[k]):
        imp = d.get("impact")
        if not imp: continue
        d["impact"] = (imp[0] if value is None else value, list(words), (imp[2] if len(imp) > 2 else "") if why is None else why)
def SI(k, *conds, value=P):
    """un satellite d'Impact qui ne vaut que pour ce qui remplit sa Condition"""
    for d in _dicts(FICHES[k]):
        if d is FICHES[k] or d.get("impact"):
            d["impact_sats"] = [st for st in (d.get("impact_sats") or []) if not any(str(w).startswith("si:") for w in st[1])] + [(value, ["si:" + c for c in conds])]
def NOCOND(k, *ws):
    W = {_nrm(w) for w in ws}
    for d in _dicts(FICHES[k]):
        if d.get("cond"): d["cond"] = [c for c in d["cond"] if _nrm(c) not in W]
SENSL({"ablative-sphere-garundi": ("vue", ["globe", "cristal"]), "deflection": ("vue", ["tourbillon"]), "primal-scream": ("ouïe", ["cri"]),
       "punishing-armor": ("vue", ["chatoiement"]), "spell-scourge": ("vue", "ouïe", ["fouet", "claquement"]), "soul-vault": ("vue", ["voûte"])})
CN("antitoxin-touch", "peau"); CN("life-bubble", "souffle")
IMPW("banishing-blade", ["recul"])
FICHES["bestow-grace"]["cible_sym"] = ["lumineux"]
IMPW("crimson-confession", ["marque"]); SENS("crimson-confession", "vue", manif=["rougeur", "marque"])
IMPW("death-from-below", []); SI("death-from-below", "grand")
IMPW("escaping-ward", ["esquive"]); SI("escaping-ward", "grand")
SI("devil-snare", "plan")
ETRE("draconic-suppression", "souffle")
IMPW("enshroud-thoughts", ["dissimulation"]); CN("enshroud-thoughts", "mémoire")
ETRE("gird-ally", "invoqué")
for _k in ("anti-incorporeal-shell", "sphere-of-warding"):
    NOCOND(_k, "intangible"); SI(_k, "intangible")
for _d in _dicts(FICHES["lament-of-summers-last-breath"]):
    if _d.get("impact_sats"): _d["impact_sats"] = [(("sym", "feu"), [])]
SI("lament-of-summers-last-breath", "glace", value=5)
FICHES["magnetic-field"]["cible"] = P; ETRE("magnetic-field", "métal")
DROP("marks-of-forbiddance", "marque"); SENS("marks-of-forbiddance", "vue", manif=["sceau"])
IMPW("node-of-blasting", ["chancellement"], value=21, why="6d6 en moyenne à qui le touche")
CN("rune-of-warding", "porte"); IMPW("rune-of-warding", ["explosion"])
ETRE("shield-of-fortification", "vital")
IMPW("undeath-ward", ["barrière"]); SI("undeath-ward", "mort-vivant")
IMPW("unholy-ward", ["lumineux"], value=10, why="10 points de dégâts sacrés retenus"); CN("unholy-ward", "résistance")
IMPW("veil-of-positive-energy", ["vie"]); SI("veil-of-positive-energy", "mort-vivant")
NOCOND("wall-of-silver", "hostile"); IMPW("wall-of-silver", ["mur"]); SI("wall-of-silver", "hostile")
ETRE("winter-feathers", "plume")
IMPW("wreath-of-blades", ["lame"])
for _o in FICHES["ward-of-the-season"]["options"]:     # la saison choisie est la nature de l'effet, pas une Condition de lancement
    _s = _o.pop("cond")[0]; _o["impact"] = (P, ["saison", _s], "la force d'une saison")
IMPW("lament-of-summers-last-breath", ["chaleur", "feu"])     # le manteau protège du froid et brûle les êtres de glace : c'est du feu
for _d in _dicts(FICHES["lament-of-summers-last-breath"]):
    _d["impact_sats"] = [st for st in (_d.get("impact_sats") or []) if not isinstance(st[0], tuple)]

# ----- Passe fine Pathfinder 1, lot W : Divination -----
SENSL({"carrion-compass": ("vue", ["organe"]), "rumormonger": ("vue", ["lueur"]), "whispering-lore": ("ouïe", ["murmure"]),
       "sense-vitals": ("vue", ["yeux", "rouge"]), "aerial-tracks": ("vue", ["lueurs", "ondes"]), "aura-sight": ("vue", ["yeux", "lueur"]),
       "track-ship": ("vue", ["icône"]), "pierce-disguise": ("vue", ["silhouette"]), "reveal-emotions": ("vue", ["couleurs"]),
       "sand-table": ("vue", ["maquette"]), "questing-stone": ("vue", ["pierre"]), "see-alignment": ("vue", ["lueur"]),
       "follow-aura": ("odorat", ["piste"]), "insect-spies": ("vue", ["scarabées"])})
DROP("see-alignment", "lueur")
IMPW("psychic-reading", ["lecture"]); IMPW("seek-thoughts", ["lecture"])
ETRE("ancestral-communion", "ancêtre"); ETRE("ancestral-memory", "ancêtre")
MOVE("anticipate-thoughts", "garde")
ETRE("insect-spies", "insecte"); ETRE("seed-spies", "graine")
IMPW("synapse-overload", ["foudre", "chancellement"])
CN("speak-with-waves", "eau")

# ----- Passe fine Pathfinder 1, lot X : Enchantement -----
SENSL({"abadars-truthtelling": ("vue", ["aura"]), "aura-of-distraction": ("ouïe", ["bourdonnement"]), "reinvigorating-wind": ("toucher", ["souffle"]),
       "debilitating-portent": ("vue", ["lueur", "vert"]), "moonstruck": ("vue", ["griffes", "crocs"]), "cloak-of-dreams": ("odorat", ["parfum"]),
       "compelling-rant": ("ouïe", ["discours"]), "debilitating-speech": ("ouïe", ["discours"]), "denounce": ("ouïe", ["voix"]),
       "forced-repentance": ("ouïe", ["aveux"]), "waves-of-ecstasy": ("toucher", ["frisson"])})
MOVE("tactical-acumen", "garde"); ETRE("blood-rage", "force")
for _d in _dicts(FICHES["thought-worm-i"]):
    if _d.get("cible_note"): _d["cible_note"] = ["lucidité" if _nrm(w) == "VOLONTE" else w for w in _d["cible_note"]]
IMPW("thought-worm-i", ["faiblesse"]); IMPW("id-insinuation-i", ["confusion"])
ETRE("martial-marionette", "membres"); ETRE("animal-ambassador", "raison")
CN("psychic-surgery", "raison", "lucidité", "prestance")

# ----- Passe fine Pathfinder 1, lot Y : Illusion -----
def TROMPE(k, n):
    """illusion : le Cosmétique compte les sens trompés"""
    for d in [FICHES[k]] + [x for x in _dicts(FICHES[k]) if "cosm" in x]:
        d["cosm"] = (n, "sens trompé")
for _k, _n in [("haunted-fey-aspect", 2), ("incessant-buzzing", 2), ("illusory-maze", 1), ("display-aversion", 2), ("hide-bruises", 1),
               ("raiment-of-command", 1), ("body-double", 3), ("appearance-of-life", 1), ("mirror-mantis", 1), ("blend", 1),
               ("chameleon-stride", 1), ("blurred-movement", 1), ("twilight-haze", 1), ("trail-of-the-rose", 2), ("dreadscape", 2),
               ("fearsome-duplicate", 2), ("illusion-of-treachery", 1), ("illusory-poison", 1), ("impossible-angles", 1),
               ("shroud-of-innocuity", 1), ("vision-of-hell", 1), ("dirge-of-the-victorious-knights", 2), ("fable-tapestry", 2),
               ("psychic-image", 3), ("phantasmal-revenge", 2), ("illusion-of-calm", 1), ("ghostly-disguise", 1), ("instant-fake", 1),
               ("familiar-figment", 1), ("familiar-double", 2), ("darting-duplicate", 1), ("horrific-doubles", 1), ("shadow-jaunt", 1)]:
    FICHES[_k].pop("sens", None); TROMPE(_k, _n)
DROP("illusory-maze", "verre"); DROP("trail-of-the-rose", "sillage")
IMPW("appearance-of-life", ["apparence", "vie"]); FICHES["appearance-of-life"]["cond"] = ["mort-vivant"]
SENSL({"cackling-skull": ("ouïe", ["ricanement"]), "loathsome-veil": ("vue", ["couleurs"]), "wall-of-nausea": ("vue", ["mur", "distorsion"])})
IMPW("phantasmal-asphyxiation", ["étouffement"])
IMPW("lunar-veil", ["obscurité"]); IMPW("cloak-of-shadows", ["ombre", "protection"])

# ----- Passe fine Pathfinder 1, lot Z : Invocation -----
# les êtres appelés d'ailleurs : Cible 9 ; les êtres faits de force, d'ombre ou de fantasme : Cible 7
for _k in ("aquatic-cavalry", "eagle-aerie", "mad-monkeys", "release-the-hounds", "rain-of-frogs", "summon-elder-worm", "summon-flight-of-eagles",
           "summon-froghemoth", "summon-minor-ally", "summon-stampede", "calistrias-guardian-wasps", "cape-of-wasps", "summon-infernal-host",
           "leshy-swarm", "murderous-crow", "vomit-swarm"):
    for _d in _dicts(FICHES[_k]):
        if _d is FICHES[_k] or "cible" in _d: _d["cible"] = 9
for _k in ("flame-steed", "ghost-wolf", "phantom-chariot", "phantom-driver", "draconic-ally", "spectral-scout", "summon-ancestral-guardian",
           "bow-spirit", "call-spirit", "pernicious-pranksters", "swarm-of-fangs", "unseen-crew"):
    for _d in _dicts(FICHES[_k]):
        if _d is FICHES[_k] or "cible" in _d: _d["cible"] = 7
SENSL({"ancestral-gift": ("vue", ["spectre"]), "blood-mist": ("vue", ["brume", "rouge"]), "bountiful-banquet": ("vue", "odorat", "goût", ["festin"]),
       "cloud-of-seasickness": ("vue", "odorat", ["vapeurs"]), "curse-of-dragonflies": ("vue", ["libellules"]), "euphoric-cloud": ("vue", "odorat", ["brume"]),
       "evaluators-lens": ("vue", ["lentille"]), "pillar-of-life": ("vue", ["lumière"]), "poisonous-cloud": ("vue", ["brume"]),
       "spectral-scout": ("vue", ["lueur"]), "spiral-ascent": ("vue", ["rayon"]), "storm-step": ("vue", "ouïe", ["éclair", "grésillement"]),
       "summon-ancestral-guardian": ("vue", ["spectres"]), "unleash-pandemonium": ("ouïe", ["hurlements"]), "light-of-iomedae": ("vue", ["lumière", "bleu"])})
DROP("euphoric-cloud", "brume"); DROP("evaluators-lens", "lentille"); DROP("poisonous-cloud", "brume")
IMPW("damnation-stride", ["téléportation"]); IMPW("phase-step", ["téléportation"]); IMPW("urban-step", ["téléportation"]); CN("urban-step", "porte")
ETRE("expel-blood", "élémentaire"); ETRE("fleshworm-infestation", "chair")
IMPW("holy-javelin", ["javelot"]); SI("holy-javelin", "hostile")
IMPW("healing-flames", ["vie"]); SI("healing-flames", "hostile")
IMPW("blaze-of-glory", ["vie"]); SI("blaze-of-glory", "hostile")
NOCOND("instant-restoration", "invoqué")
IMPW("life-shield", ["vie", "riposte"]); SI("life-shield", "mort-vivant")
IMPW("light-of-iomedae", ["révélation"]); SI("light-of-iomedae", "mort-vivant")
IMPW("pillar-of-life", ["vie"]); IMPW("waves-of-blood", ["sang", "recul", "nausée"])

# ----- Passe fine Pathfinder 1, lot AA : Nécromancie -----
for _d in _dicts(FICHES["black-mark"]):
    if _d.get("impact_sats"): _d["impact_sats"] = [st for st in _d["impact_sats"] if not isinstance(st[0], tuple)]
    if _d.get("impact_add"): _d["impact_add"] = [w for w in _d["impact_add"] if _nrm(w) != "EAU"]
IMPW("black-mark", ["peur", "malédiction"])
SENSL({"black-mark": ("vue", ["marque"]), "black-spot": ("vue", ["tache"]), "bone-fists": ("vue", ["os"]),
       "curse-of-unexpected-death": ("vue", ["flamme", "gris"]), "death-clutch": ("vue", ["cœur"]), "death-knell-aura": ("vue", ["aura", "gris"]),
       "decollate": ("vue", ["ligne", "rouge"]), "fungal-infestation": ("vue", ["champignons"]), "grave-words": ("ouïe", ["babil"]),
       "lash-of-the-astradaemon": ("vue", ["griffes", "lueur"]), "necrostasis": ("vue", ["volutes"]), "persuasive-goad": ("vue", ["regard"]),
       "red-hand-of-the-killer": ("vue", ["main", "rouge"]), "scarify": ("vue", ["cicatrices"]), "stricken-heart": ("vue", ["aura", "noir"]),
       "touch-of-blindness": ("vue", ["ténèbres"]), "vampiric-hunger": ("vue", ["crocs"]), "wall-of-blindness-deafness": ("vue", ["visages"]),
       "withdraw-affliction": ("vue", ["chair"]), "symbol-of-exsanguination": ("vue", ["glyphe", "sang"])})
IMPW("barrow-haze", ["obscurité"]); IMPW("bloodbath", ["saignement"]); ETRE("bone-fists", "os")
IMPW("decollate", ["détachement"]); IMPW("decompose-corpse", ["décomposition"])
ETRE("death-candle", "élémentaire")
IMPW("khains-army", ["animation"]); IMPW("skeleton-crew", ["animation"]); CN("skeleton-crew", "cadavre")
IMPW("phantom-limb", ["remplacement"])
IMPW("positive-pulse", ["vie"]); SI("positive-pulse", "mort-vivant")
IMPW("repair-undead", ["nécrose"]); IMPW("sands-of-time", ["vieillissement"])
IMPW("spawn-ward", ["résistance"]); CN("spawn-ward", "vie", "sang"); SI("spawn-ward", "mort-vivant")
IMPW("stricken-heart", ["nécrose", "chancellement"]); IMPW("symbol-of-exsanguination", ["saignement"])
IMPW("undines-curse", ["malédiction"]); IMPW("unliving-rage", ["rage"]); IMPW("undeath-inversion", ["vie", "nécrose", "inversion"])
IMPW("wither-limb", ["flétrissement"], value=7, why="2d6 en moyenne, perdus jusqu'à la guérison du membre")

# ----- Passe fine Pathfinder 1, lot AB : Transmutation -----
SENSL({"alchemical-allocation": ("vue", ["aura"]), "aspect-of-the-falcon": ("vue", ["plumes", "yeux"]), "aspect-of-the-nightingale": ("ouïe", ["voix"]),
       "aspect-of-the-stag": ("vue", ["bois"]), "aspect-of-the-wolf": ("vue", ["crocs", "fourrure"]), "baphomets-blessing": ("vue", ["taureau"]),
       "brand": ("vue", ["marque"]), "countless-eyes": ("vue", ["yeux"]), "face-of-the-devourer": ("vue", ["visage"]),
       "fiery-body": ("vue", ["flammes"]), "fire-trail": ("vue", ["flammes"]), "firebrand": ("vue", ["rune", "flamme"]),
       "flames-of-the-faithful": ("vue", ["rune", "lueur"]), "funereal-weapon": ("vue", ["lueur", "argent"]), "fungal-blisters": ("vue", ["cloques"]),
       "golden-guise": ("vue", ["or"]), "gorums-armor": ("vue", ["pointes"]), "hide-weapon": ("ouïe", ["succion"]), "ironbeard": ("vue", ["barbe"]),
       "instrument-of-agony": ("vue", ["aura"]), "mantle-of-the-magic-warriors": ("vue", ["masques", "or"]), "parchment-swarm": ("vue", ["parchemins"]),
       "ravens-flight": ("vue", ["plumes"]), "resonating-word": ("ouïe", ["parole"]), "rune-of-durability": ("vue", ["rune"]),
       "savage-maw": ("vue", "ouïe", ["crocs", "rugissement"]), "scorching-ash-form": ("vue", ["cendre", "fumée"]), "serrens-armor-lock": ("vue", ["chaînes"]),
       "sky-steed": ("vue", ["ailes"]), "sun-metal": ("vue", ["flamme"]), "thorn-body": ("vue", ["épines"]), "vocal-alteration": ("ouïe", ["voix"]),
       "weapons-against-evil": ("vue", ["lueur"]), "swarm-skin": ("vue", ["nuée"]), "tail-strike": ("vue", ["queue"]), "vengeful-stinger": ("vue", ["dard"])})
CN("abstemiousness", "nourriture"); IMPW("abstemiousness", ["satiété"])
IMPW("acid-maw", ["croc", "acide"]); IMPW("aspect-of-the-nightingale", ["mélodie"]); ETRE("baphomets-blessing", "tête"); DROP("baphomets-blessing", "taureau")
IMPW("blade-of-light", ["soleil"]); SI("blade-of-light", "mort-vivant"); IMPW("blood-armor", ["durcissement"])
CN("burning-disarm", "métal"); IMPW("burning-disarm", ["feu", "lâcher"]); IMPW("caustic-blood", ["acide", "riposte"])
IMPW("concealed-breath", ["apnée"]); IMPW("curse-of-burning-sleep", ["sommeil", "feu"])
for _k in ("divine-arrow", "empower-holy-water"):
    IMPW(_k, ["lumière"]); FICHES[_k]["rayonnement"] = True; SI(_k, "mort-vivant")
IMPW("erode-defenses", ["érosion"]); IMPW("face-of-the-devourer", ["difformité"]); IMPW("fiery-body", ["feu"]); IMPW("fire-trail", ["feu", "trace"])
IMPW("flames-of-the-faithful", ["feu"]); IMPW("funereal-weapon", ["faille"]); SI("funereal-weapon", "mort-vivant")
ETRE("hellmouth-lash", "langue"); IMPW("heart-of-the-mammoth", ["vigueur"]); IMPW("hidden-knowledge", ["oubli"]); IMPW("inheritors-smite", ["coup"])
IMPW("magnifying-chime", ["tonnerre"]); IMPW("mirror-transport", ["téléportation"]); IMPW("obsidian-flow", ["sol", "verre", "feu"])
IMPW("resonating-word", ["tonnerre", "étourdissement"]); CN("resounding-clang", "métal"); IMPW("resounding-clang", ["vibration"])
IMPW("rune-of-durability", ["solidité"]); IMPW("savage-maw", ["croc"]); IMPW("snapdragon-fireworks", ["feu"])
IMPW("steal-breath", ["mutisme"]); IMPW("stoke-the-inner-fire", ["feu", "arme"]); IMPW("sun-metal", ["feu"])
IMPW("tar-ball", ["goudron", "feu"]); IMPW("tar-pool", ["goudron", "sol", "feu"]); IMPW("transmute-blood-to-acid", ["acide", "chancellement"])
IMPW("vocal-alteration", ["changement"]); IMPW("weapons-against-evil", ["arme"]); SI("weapons-against-evil", "hostile")

# ----- Passe fine Pathfinder 1, lot AC : Évocation -----
SENSL({"apsus-shining-scales": ("vue", ["écailles", "argent"]), "battering-blast": ("vue", ["boule", "pointes"]),
       "betraying-sting": ("vue", "ouïe", ["éclair", "bourdonnement"]), "blood-crow-strike": ("vue", ["corbeaux"]),
       "burn-corruption": ("vue", ["flammes", "violet"]), "campfire-wall": ("vue", "ouïe", ["flammes", "crépitement"]),
       "cleansing-fire": ("vue", ["cercle", "flammes"]), "fires-friend": ("vue", ["flammes"]), "frigid-touch": ("vue", ["lueur", "bleu"]),
       "heatstroke": ("vue", ["rayon", "rouge"]), "jolting-portent": ("vue", ["aura", "rouge"]), "pale-flame": ("vue", ["flamme"]),
       "sacred-nimbus": ("vue", ["nimbe", "or"]), "sign-of-wrath": ("vue", ["symbole"]), "twilight-knife": ("vue", ["couteau"]),
       "vengeful-comets": ("vue", ["comètes"]), "vitriolic-mist": ("vue", ["brume"]), "piercing-shriek": ("vue", ["cri"]),
       "spiritual-ally": ("vue", ["silhouette"]), "spiritual-squire": ("vue", ["silhouette"])})
IMPW("burn-corruption", ["purification"])
for _k in ("burning-arc-keleshite", "chains-of-fire", "contagious-flame", "ricochet-shot"):
    DROP(_k, "rebond"); CN(_k, "rebond")
IMPW("decapitate", ["décapitation"]); IMPW("heatstroke", ["feu", "fatigue"])
IMPW("holy-whisper", ["parole"]); SI("holy-whisper", "hostile")
IMPW("incorporeal-chains", ["chaîne"]); SI("incorporeal-chains", "intangible")
IMPW("litany-of-righteousness", ["faiblesse"]); IMPW("pale-flame", ["flamme"]); IMPW("rebuke", ["colère"])
NOCOND("sacred-nimbus", "hostile"); IMPW("sacred-nimbus", ["riposte"]); SI("sacred-nimbus", "hostile")
IMPW("screaming-flames", ["peur"]); DROP("sign-of-wrath", "symbole")
for _k, _n in (("spiritual-ally", "allié"), ("spiritual-squire", "écuyer")):
    FICHES[_k]["cible"] = 7; CN(_k, _n); IMPW(_k, ["force"])
IMPW("suppressing-stone", ["protection"])
for _k in ("discordant-blast", "ear-piercing-scream", "tamers-lash", "sonic-scream", "wall-of-sound"): DROP(_k, "son")
for _k in ("piercing-shriek", "sonic-thrust", "distressing-tone"):
    for _d in _dicts(FICHES[_k]):
        if _d.get("impact") and isinstance(_d["impact"][1], list):
            _d["impact"] = (_d["impact"][0], ["tonnerre" if _nrm(w) == "SON" else w for w in _d["impact"][1]], _d["impact"][2] if len(_d["impact"]) > 2 else "")
IMPW("healing-flames", ["vie", "feu"]); IMPW("blaze-of-glory", ["vie", "lumière"]); FICHES["blaze-of-glory"]["rayonnement"] = True
def _REFACE(k):
    """les formes lumineuse et ténébreuse gardent leur face après une réécriture de l'Impact"""
    for _d in _dicts(FICHES[k]):
        lab = _nrm(_d.get("label", ""))
        f_ = "lumineux" if "LUMINEU" in lab else "ténébreux" if "TENEBREU" in lab else None
        if f_ and _d.get("impact"): _d["impact"] = (_d["impact"][0], list(_d["impact"][1]) + [f_], _d["impact"][2] if len(_d["impact"]) > 2 else "")
for _k in ("cloak-of-shadows", "lunar-veil"): _REFACE(_k)

# ----- Décisions du 14 novembre -----
# Les êtres créés, même pourvus d'un corps, sont faits d'une matière tirée de la trame : Cible 7
for _k, _w in [("simulacrum", "double"), ("frost-mammoth", "mammouth"), ("wooden-phalanx", "golem"), ("wicker-horse", "monture"),
               ("twine-double", "double"), ("snake-staff", "serpent")]:
    for _d in _dicts(FICHES[_k]):
        if _d is FICHES[_k] or "cible" in _d: _d["cible"] = 7
    ETRE(_k, _w); CN(_k, _w)
# (aveuglement et surdité passent d'office en Cosmétique « sens éteint » : moteur)

# ===== Règles du 14 novembre (audit par lecture inversée) =====
def UNCN(k, *ws):
    """retire des précisions de la Cible (sur la fiche, ses options et ses versions)"""
    W = {_nrm(w) for w in ws}
    for d in _dicts(FICHES[k]):
        if d.get("cible_note"): d["cible_note"] = [w for w in d["cible_note"] if _nrm(w) not in W]
def IADD(k, *ws):
    """ajoute des mots à l'Impact de chaque forme qui en porte un"""
    for d in _dicts(FICHES[k]):
        imp = d.get("impact")
        if imp and isinstance(imp[1], str): imp = (imp[0], [imp[1]], *imp[2:])
        if imp and isinstance(imp[1], list):
            d["impact"] = (imp[0], list(imp[1]) + [w for w in ws if _nrm(w) not in {_nrm(x) for x in imp[1]}], imp[2] if len(imp) > 2 else "")
def RESERVE(k):
    """règle 3 : une réserve de vie (« jusqu'à n points de vie de créatures ») n'est pas un Impact mais un seuil — Condition « seuil », satellite « vie »"""
    for d in _dicts(FICHES[k]):
        imp = d.get("impact")
        if not imp or imp[0] == P or not isinstance(imp[1], (list, type(None))): continue
        ws = [w for w in (imp[1] or []) if _nrm(w) != "VIE"]
        if imp[1] is not None and len(ws) == len(imp[1]): continue
        d["impact"] = (P, ws, imp[2] if len(imp) > 2 else "")
        c0 = d.get("cond") if d.get("cond") is not None else (FICHES[k].get("cond") or [])
        d["cond"] = [c for c in c0 if _nrm(c) != "SEUIL"] + ["seuil"]; d["cond_sats"] = [(imp[0], ["vie"])]
for _k in ("color-spray", "sleep", "hypnotic-pattern", "planar-binding", "circle-of-death", "planar-ally", "charm-monster", "calm-animals",
           "hypnotism", "animal-trance", "rainbow-pattern", "scintillating-pattern", "command-undead", "command-plants"):
    RESERVE(_k)
# règle 3 : « vie » dit un soin ; un dégât s'écrit nu (verbe Détruire) ou « blessure »
IMPW("hunters-mark", ["blessure"]); IMPW("mindwipe", ["effacement"]); IMPW("veil-of-positive-energy", []); IMPW("shambler", [])
for _k, _w in (("chill-touch", []), ("vampiric-touch", []), ("flame-strike", []), ("blight", ["dessèchement"])):
    for _v in ("v35", "vpf"):
        _d = FICHES[_k].get(_v)
        if isinstance(_d, dict) and _d.get("impact") and (_d["impact"][1] is None or "vie" in (_d["impact"][1] or [])):
            _d["impact"] = (_d["impact"][0], list(_w), _d["impact"][2] if len(_d["impact"]) > 2 else "")
for _o in FICHES["enhance-ability"].get("options") or []:
    if _o.get("impact") and _o["impact"][0] != P and (_o["impact"][1] is None or _o["impact"][1] == ["vie"]):
        _o["impact"] = (_o["impact"][0], ["vie", "temporaire"], _o["impact"][2])
# règle 2 : un sort qui guérit la cécité ou la surdité ne les inflige pas
for _k in ("heal", "mass-heal", "heal-mount"): FICHES[_k]["guerit"] = True
# règle 1 : un sort hybride n'a pas de verbe — son Impact plein nomme l'action
for _k, _w in [("color-spray", "éblouissement"), ("protection-from-poison", "neutralisation"), ("gaseous-form", "métamorphose"),
               ("stoneskin", "durcissement"), ("simulacrum", "création"), ("control-winds", "maîtrise"), ("transmute-rock-to-mud", "boue"),
               ("caustic-safeguard", "riposte"), ("flashfire", "embrasement"), ("sonic-scream", "onde"), ("frost-mammoth", "création"),
               ("fiery-body", "métamorphose"), ("flames-of-the-faithful", "embrasement"), ("magnifying-chime", "vibration"),
               ("snapdragon-fireworks", "explosion"), ("sun-metal", "embrasement"), ("pyrotechnics", "éblouissement")]:
    for _d in _dicts(FICHES[_k]):
        if _d.get("impact") and _d["impact"][0] == P and not [w for w in (_d["impact"][1] or []) if _nrm(w) not in ("AVEUGLEMENT", "CECITE", "SURDITE")]:
            _d["impact"] = (P, list(_d["impact"][1] or []) + [_w], _d["impact"][2] if len(_d["impact"]) > 2 else "")
for _o in FICHES["pyrotechnics"]["options"] + FICHES["pyrotechnics"]["vpf"]["options"]:
    if _o["label"] == "Fumée": _o["impact"] = (P, [w for w in _o["impact"][1] if _nrm(w) != "EBLOUISSEMENT"], _o["impact"][2])
# règle 5 : la Cible ne porte que l'être, l'objet, la part, la faculté ou le lieu visé
UNCN("comprehend-languages", "langue"); IMPW("comprehend-languages", ["langue", "compréhension"])
UNCN("shield", "projectile"); SI("shield", "projectile")
UNCN("shield-of-faith", "foi")
UNCN("darkvision", "obscurité"); IMPW("darkvision", ["vision", "obscurité", "mètres"])
UNCN("see-invisibility", "invisible", "éthéré"); IMPW("see-invisibility", ["vision", "invisible", "éthéré"])
for _k in ("good-hope", "prayer", "crushing-despair"):
    for _d in _dicts(FICHES[_k]):
        if _d.get("cible_note"): _d["cible_note"] = ["frappe" if _nrm(w) == "BLESSURE" else w for w in _d["cible_note"]]
for _k in ("chromatic-orb", "burning-arc-keleshite", "chains-of-fire", "contagious-flame", "ricochet-shot"):
    UNCN(_k, "rebond")
    for _d in _dicts(FICHES[_k]):
        if _d is FICHES[_k] or _d.get("impact"): _d["impact_add"] = list(_d.get("impact_add") or []) + ["rebond"]
# règle 6 : toujours un cercle Cible, sauf création à partir de rien
for _k, _c in [("detect-magic", P), ("augury", 1), ("arcane-eye", P), ("legend-lore", 4), ("globe-of-invulnerability", 1), ("prismatic-wall", P),
               ("prying-eyes", P), ("prying-eyes-greater", P), ("vision", 4)]:
    FICHES[_k]["cible"] = _c
# glyphes muets
FICHES["reincarnate"]["impact"] = (P, ["vie", "corps", "renaissance"], "revient à la vie dans un corps nouveau")
FICHES["time-stop"]["impact"] = (P, ["temps", "arrêt"], "le temps arrêté pour tous sauf le lanceur")
# petits défauts
RESAT("geas", [], lambda v, w: (v, ["blessure"])); RESAT("power-word-kill", [], lambda v, w: (v, ["blessure"]))
RESAT("ice-knife", [], lambda v, w: (v, ["explosion"]))
FICHES["continual-flame"].pop("cosm", None)
for _k, _w in (("chill-touch", []), ("vampiric-touch", []), ("flame-strike", []), ("blight", ["dessèchement"])):
    for _d in _dicts(FICHES[_k]):
        _i = _d.get("impact")
        if _i and _i[0] != P and (_i[1] is None or (isinstance(_i[1], list) and any(_nrm(w) == "VIE" for w in _i[1]))):
            _d["impact"] = (_i[0], list(_w), _i[2] if len(_i) > 2 else "")
for _k, _w in [("protection-from-poison", "neutralisation"), ("gaseous-form", "métamorphose"), ("simulacrum", "création"), ("control-winds", "maîtrise"),
               ("transmute-rock-to-mud", "boue"), ("caustic-safeguard", "riposte"), ("flashfire", "embrasement"), ("frost-mammoth", "création"),
               ("fiery-body", "métamorphose"), ("flames-of-the-faithful", "embrasement"), ("sun-metal", "embrasement"), ("stoneskin", "durcissement"),
               ("magnifying-chime", "vibration"), ("snapdragon-fireworks", "explosion"), ("sonic-scream", "onde"), ("color-spray", "éblouissement")]:
    FICHES[_k]["impact_add"] = [w for w in (FICHES[_k].get("impact_add") or []) if _nrm(w) != _nrm(_w)] + [_w]
    for _d in _dicts(FICHES[_k]):
        if _d.get("impact") and isinstance(_d["impact"][1], list): _d["impact"] = (_d["impact"][0], [w for w in _d["impact"][1] if _nrm(w) != _nrm(_w)], *_d["impact"][2:])
# options de version restées sans Impact
for _k, _imp in [("contagion", (P, ["maladie", "contagion"], "une maladie qui se transmet")), ("heal", (110, None, "10 par niveau, et les maux levés")),
                 ("resist-energy", (10, ["résistance", "énergie"], "10 retranché à chaque coup")), ("align-weapon", (P, ["arme", "orientation"], "les armes orientées"))]:
    for _v in ("v35", "vpf"):
        for _o in (FICHES[_k].get(_v) or {}).get("options") or []:
            if not _o.get("impact"): _o["impact"] = _imp
# Bouclier de feu : la résistance à l'énergie contraire est un second Impact (règle 4)
for _d in _dicts(FICHES["fire-shield"]):
    _ss = _d.get("impact_sats")
    if _ss and any(isinstance(st[0], tuple) for st in _ss):
        _el = "froid" if any(isinstance(st[0], tuple) and st[0][1] == "eau" for st in _ss) else "feu"
        _d["impact_sats"] = []; _d["impact_plus"] = [(P, ["résistance", _el], "")]
for _d in _dicts(FICHES["continual-flame"]) + _dicts(FICHES["minor-illusion"]):
    if _d.get("cosm") and "sens" not in str(_d["cosm"][1]).lower():
        if _d in _dicts(FICHES["minor-illusion"]): _d["cosm"] = (1, "sens trompé")
        else: _d.pop("cosm")
IMPW("transmute-rock-to-mud", ["boue", "métamorphose"])
# règle 8 : ce que la description dit, le glyphe l'inscrit
for _k in ("ash-storm", "sand-whirlwind"): FICHES[_k]["impact_add"] = list(FICHES[_k].get("impact_add") or []) + ["cécité"]
# règle 7 : une mesure porte son unité, un multiplicateur est dit « fois » ; « stature » dit la taille d'un être (« taille » reste le tranchant)
def _REW(k, a, b, extra=()):
    for d in _dicts(FICHES[k]):
        i = d.get("impact")
        if i and isinstance(i[1], list): d["impact"] = (i[0], [b if _nrm(w) == _nrm(a) else w for w in i[1]] + [x for x in extra if _nrm(x) not in {_nrm(w) for w in i[1]}], *i[2:])
        if d.get("impact_sats"): d["impact_sats"] = [(st[0], [b if _nrm(w) == _nrm(a) else w for w in (st[1] or [])]) for st in d["impact_sats"]]
_REW("jump", "saut", "saut", ["fois"]); _REW("longstrider", "pas", "pas", ["mètres"]); _REW("haste", "temps", "temps", ["fois"])
_REW("skim", "lecture", "lecture", ["fois"]); _REW("ant-haul", "charge", "port", ["fois"])
_REW("enlarge-reduce", "taille", "stature", ["fois"]); _REW("animal-growth", "taille", "stature"); _REW("righteous-might", "taille", "stature")
def ADD(k, *ws):
    """règle 8 : un effet que la description annonce s'inscrit à l'Impact (sur toutes les formes du sort)"""
    cur = list(FICHES[k].get("impact_add") or [])
    FICHES[k]["impact_add"] = cur + [w for w in ws if _nrm(w) not in {_nrm(x) for x in cur}]
for _k, _w in [("brow-gasher", ["cécité"]), ("scouring-winds", ["cécité"]), ("wall-of-sound", ["surdité"]), ("garrulous-grin", ["peur"]),
               ("devil-snare", ["ancrage"]), ("magic-circle", ["charme", "peur", "possession"]), ("beacon-of-hope", ["courage"]),
               ("dissonant-whispers", ["peur"]), ("rally-point", ["courage"]), ("free-spirit", ["courage"]), ("sequester", ["sommeil"]),
               ("lullaby", ["sommeil"]), ("freedom", ["paralysie", "sommeil"]), ("reinvigorating-wind", ["réveil"]),
               ("freedom-of-movement", ["paralysie"]), ("overwhelming-grief", ["paralysie"]), ("mantle-of-doubt", ["paralysie"]),
               ("hibernate", ["paralysie"]), ("delusional-pride", ["charme"]), ("battle-trance", ["charme"]), ("sleet-storm", ["extinction"]),
               ("gust-of-wind", ["extinction"]), ("heroes-feast", ["guérison"]), ("nauseating-dart", ["poison"]), ("make-lost", ["oubli"]),
               ("dream-reality", ["oubli"]), ("mindshock", ["douleur"]), ("spike-stones", ["lenteur"]), ("frost-fall", ["lenteur"]),
               ("sickening-entanglement", ["entrave"]), ("winds-of-vengeance", ["renvoi"]), ("communication-placeholder", [])]:
    if _k in FICHES: ADD(_k, *_w)
IMPW("protection-from-evil-and-good", ["protection", "charme", "peur", "possession"])
IMPW("rite-of-centered-mind", ["émotion", "peur"]); CN("mental-block", "mémoire"); SI("magic-stone", "mort-vivant")
_REW("twilight-haze", "vue", "obscurité")
IMPW("speak-with-animals", ["parole"]); IMPW("speak-with-plants", ["parole"])
ADD("jump", "fois"); ADD("longstrider", "mètres")
for _k in ("animal-growth", "righteous-might"):
    for _d in _dicts(FICHES[_k]):
        _i = _d.get("impact")
        if _i and isinstance(_i[1], list) and any(_nrm(w) == "STATURE" for w in _i[1]):
            _d["impact"] = (_i[0], [w for w in _i[1] if _nrm(w) != "STATURE"], *_i[2:])
            _d["impact_sats"] = list(_d.get("impact_sats") or []) + [(2, ["stature", "fois"])]
IMPW("disrupt-undead", ["lumière"]); RESERVE("undeath-to-death")
for _d in _dicts(FICHES["enervation"]):
    _i = _d.get("impact")
    if _i and isinstance(_i[1], list): _d["impact"] = (_i[0], ["affaiblissement" if _nrm(w) == "VIE" else w for w in _i[1]], *_i[2:])
IMPW("baphomets-blessing", ["taureau"])
FICHES["misty-step"]["impact"] = (P, ["téléportation"], "disparaît et reparaît plus loin")
IMPW("wave-shield", ["eau"]); FICHES["wave-shield"]["impact_plus"] = [(P, ["résistance", "feu"], "")]
ADD("holy-javelin", "lumineux"); IMPW("ghost-brand", ["tangibilité", "intangible"])

# ===== Pathfinder 1, suite : les sorts hors « Pathfinder Society » (import du 14 novembre) =====
# Le fichier d'origine ne gardait que les sorts légaux en jeu organisé ; les autres sont triés ici, école par école,
# avec les mêmes règles : pas de vocabulaire de jeu, Golarion et mécaniques de classe écartés, les dix règles de l'audit.
IL = lambda fr, verb, cible, words, v=None, why="", **kw: EP(fr, verb, cible, words, v, why, **{"alt": ILLH(), **kw})
_ART = "artefact animé"

# ----- Suite, lot 1 : Abjuration, Divination, Enchantement, Illusion -----
PF1_RELECTURE.update({
 "curse-of-magic-negation": "inflige un « fléau magique » (spellblight), sous-système de règles propre à Pathfinder",
 "detect-demon": "ne décèle que les démons des Abysses, propres à la cosmologie de Golarion",
 "glimpse-of-the-akashic": "repose sur la mémoire akashique, notion occulte reprise par Pathfinder",
 "harrowing": "repose sur le jeu de cartes du Harrow, propre à Golarion",
 "influence-wild-magic": "repose sur la « magie primitive », sous-système de règles propre à Pathfinder",
 "spellscar": "repose sur la « magie primitive », sous-système de règles propre à Pathfinder, et sur les Terres de Mana de Golarion",
 "shared-training": "prête des « dons d'équipe » : pure mécanique de jeu",
 "tactical-insight": "agit sur une armée du sous-système de batailles : pure mécanique de jeu",
 "bless-army": "agit sur une armée du sous-système de batailles : pure mécanique de jeu",
 "unravel-destiny": "repose sur les « points d'héroïsme » : pure mécanique de jeu",
 "severed-fate": "repose sur les « points d'héroïsme » : pure mécanique de jeu",
 "spherescry": "n'agit qu'à travers une sphère d'annihilation, artefact d'un autre jeu, absent d'Inarama",
 "business-booms": "repose sur les règles de gestion d'un commerce entre deux aventures : pure mécanique de jeu",
 "prosperous-room": "repose sur les règles de gestion d'un commerce entre deux aventures : pure mécanique de jeu",
 "create-mindscape": "repose sur les « mondes intérieurs » (mindscapes), sous-système de règles propre à Pathfinder",
 "create-mindscape-greater": "repose sur les « mondes intérieurs » (mindscapes), sous-système de règles propre à Pathfinder",
 "instigate-psychic-duel": "ouvre un « duel psychique », sous-système de règles propre à Pathfinder",
 "yellow-sign": "livre ses victimes à Hastur, entité étrangère à Inarama",
})
PF1_MEME.update({"detect-fiendish-presence": "detect-evil-and-good", "protection-from-outsiders": "protection-from-evil-and-good"})

SUITE1 = {
# -- Abjuration
"absorbing-barrier": EP("Barrière absorbante", SEP, P, [], 20, "20 retranché à chaque coup porté à distance", impact_sats=[(200, ["plafond"]), (12, ["hauteur", "mètres"])], cible_note=["garde", "trait"]),
"anti-summoning-shield": EP("Bouclier contre l'invocation", SEP, "trame", ["invocation", "échec"], why="les invocations tentées dans la zone échouent le plus souvent", cible_note=["sort"]),
"armor-of-darkness": EP("Armure de ténèbres", INT, 2, ["armure", "ombre"], 3, "3 ajouté à la défense", cible_note=["garde"],
    impact_plus=[(18, ["vision", "obscurité", "mètres"], "voit dans le noir à 18 m")], impact_sats=[(2, ["si:lumineux"])],
    sens=[("vue", None)], manif=["ombre", "voile"]),
"blood-transcription": EP("Transcription du sang", V("flux"), 4, ["sort", "savoir"], why="un sort du mort appris en buvant son sang", cible_obj=["cadavre", "sang"]),
"bloodstone-mirror": EP("Miroir de sanguine", V("force", True), 1, ["emprise", "renvoi"], why="l'emprise qui me vise renvoyée sur un être proche", cible_note=["psyché", "volonté"], cond=["emprise"], impact_sats=[(9, ["mètres"])]),
"dust-ward": EP("Garde de poussière", NE, 4, ["poussière"], why="l'objet tombe en poussière aux mains d'un autre", cible_obj=["objet"], cond=["porteur", "étranger"]),
"echeans-excellent-enclosure": EP("Enclos sans magie", SEP, "trame", ["suspension"], why="toute magie suspendue", cible_note=["magie"],
    impact_plus=[(P, ["barrière", "force", "sphère"], "une sphère de force infranchissable autour du champ")]),
"hide-from-undead-greater": EP("Invisibilité tenace pour les morts-vivants", NVIS, 2, ["dissimulation", "ténacité"], why="ni vue, ni ouïe, ni odorat, même après un geste hostile", cond=["MORTVIVANT"]),
"incendiary-runes": EP("Runes incendiaires", NE, 1, ["feu"], 4, "1d6 en moyenne", cible_obj=["écrit"], cond=["lecture"], impact_add=["embrasement"], sens=[("vue", None)], manif=["runes"]),
"righteous-blood": EP("Sang du juste", V("flux", True), 2, ["lumineux"], 4, "1d6 en moyenne à qui le blesse", cible_note=["sang"], cond=["coup", "ténébreux"],
    options=[O("Sang du juste"), O("Porteur voué à la face lumineuse", impact=(7, ["lumineux"], "2d6 en moyenne à qui le blesse"))]),
"righteous-condemnation": EP("Juste réprobation", NINT, 3, ["réprobation"], 4, "4 retranché à ses facultés d'esprit", cible_note=["raison", "lucidité", "prestance"], cond=["sort", "hostile"]),
"shield-the-banner": EP("Garde de l'étendard", SEP, 4, ["détournement", "solidité"], why="qui veut toucher l'étendard s'en détourne ; l'étoffe durcie", cible_obj=["étendard"], cond=["ATTAQUE"]),
"spellsteal": EP("Vol de sort", V("flux"), 3, ["sort", "perte", "savoir"], why="un sort arraché à la cible, que je peux lancer aussitôt"),
"status-greater": EP("Rapport supérieur", REL, 2, ["lien", "état", "direction", "sort"], why="position et état des compagnons ; mes sorts de contact passent par le lien"),
"sympathetic-wounds": EP("Blessures sympathiques", REL, 3, ["partage", "blessure"], why="la moitié de mes blessures passe à la cible", cible_note=["corps"]),
"telepathic-censure": EP("Censure télépathique", SEP, 3, ["télépathie"], why="ni émettre ni recevoir de pensées", cible_note=["psyché"]),
"teleport-trap": EP("Piège à téléportation", V("force"), P, ["téléportation", "piège"], why="toute téléportation vers la zone ou hors d'elle aboutit au point choisi"),
# -- Divination
"ears-of-the-city": EP("Oreilles de la cité", VIS, 2, ["rumeur", "passé"], why="scènes et propos passés de la ville", impact_add=["cécité", "surdité"], cible_note=["psyché"]),
"forests-sense": EP("Sens de la forêt", VIS, 4, ["position", "ouïe", "odorat", "toucher"], why="la cible située, et perçue à travers les plantes qui l'entourent", cond=["plante"]),
"fortunes-path": EP("Chemin de fortune", VIS, 1, ["présage", "vision"], why="un événement à venir vu dans un miroir, parfois faux", loc=(7, ["JOURS", "AVENIR"], "7 jours dans l'avenir"), cible_obj=["miroir"]),
"harvest-knowledge": EP("Moisson de savoir", V("flux"), 3, ["savoir", "réponse"], why="son savoir et ses souvenirs fouillés, une réponse par minute", cible_note=["psyché", "mémoire"]),
"insect-scouts": EP("Insectes éclaireurs", V("trame"), 9, ["exploration", "rapport"], why="des insectes fouillent un lieu puis reviennent dire ce qu'ils ont vu", cible_note=["insecte"]),
"prediction-of-failure": EP("Prédiction de l'échec", NQ, 3, ["échec", "effroi", "nausée"], why="tous ses échecs à venir ressentis d'un coup", cible_note=["psyché", "corps"]),
"probe-history": EP("Sonde d'une histoire possible", VIS, 3, ["savoir", "possible"], why="ce que j'aurais su d'elle dans une réalité voisine", cible_note=["mémoire"]),
"prognostication": EP("Pronostic", VIS, 9, ["réponse", "énigme"], why="une réponse véridique mais obscure", cible_note=["divinité"], loc=(1, ["AN", "AVENIR"], "un an et un jour dans l'avenir")),
"true-prognostication": EP("Pronostic véritable", VIS, 9, ["réponse", "énigme"], why="une réponse véridique mais très obscure", cible_note=["divinité"], loc=(100, ["ANS", "AVENIR"], "cent ans dans l'avenir")),
"reveal-true-shape": EP("Révélation de la forme véritable", VIS, 3, ["forme", "vérité"], why="sa vraie forme montrée à tous par-dessus le déguisement ou la métamorphose", sens=[("vue", None)], manif=["forme"]),
"sense-madness": EP("Perception de la folie", VIS, 4, ["folie", "emprise"], why="décèle la folie, la dépendance ou l'emprise", cible_note=["psyché"]),
"skyshroud": EP("Voûte céleste", VIS, P, ["ciel", "image"], why="le ciel du dehors montré sous la voûte, et tenu pour le vrai ciel", sens=[("vue", None)], manif=["ciel"]),
"unspoken-name": EP("Nom imprononcé", VIS, 4, ["nom", "apparence", "position"], why="qui me désigne par le mot choisi m'est révélé", cond=["mot"], loc=(1600, "METRES", "1,6 km alentour")),
# -- Enchantement
"agonizing-rebuke": EP("Réprimande douloureuse", V("force", True), 3, ["douleur"], 7, "2d6 en moyenne chaque fois qu'elle s'en prend à moi", cible_note=["psyché"], cond=["VIVANT", "agression"]),
"amnesia": EP("Amnésie", NREL, 3, ["oubli", "passé", "aptitude"], why="son passé, son nom et ses talents oubliés", cible_note=["mémoire", "psyché"], cond=["VIVANT"]),
"apparent-master": EP("Maître apparent", REL, 3, ["maître", "contrôle"], why="l'artefact animé me prend pour son maître", cond=["ARTEFACT"], fin=["blessure"]),
"bolts-of-bedevilment": EP("Traits d'égarement", NORD, 3, ["rayon", "hébétude"], why="un rayon par instant, qui laisse hébété", cible_note=["psyché"], cond=["VIVANT"], sens=[("vue", None)], manif=["rayon"]),
"constricting-coils": EP("Anneaux constricteurs", V("mouvement", True), 3, ["PARALYSIE"], why="paralysée", cond=["VIVANT"],
    impact_plus=[(10, ["écrasement", "anneaux"], "1d6 + 6 en moyenne à chaque instant, comme serrée par un grand serpent")]),
"cowards-cowl": EP("Capuchon du couard", INT, 2, ["prudence"], 1, "1 ajouté à la défense tant qu'elle se tient à distance de l'ennemi", cible_note=["garde", "résistance", "psyché"], cond=["distance"]),
"damnation-of-memory": EP("Damnation de la mémoire", NREL, P, ["oubli", "être", "gemme"], why="un être, un fait ou un sujet effacé des mémoires, le souvenir enfermé dans une gemme", cible_note=["mémoire", "psyché"], cond=["VIVANT"]),
"death-pact": EP("Pacte de mort", REL, 3, ["domination"], why="dominée, ses sens partagés", cible_note=["psyché"],
    impact_plus=[(49, ["signal", "déflagration"], "11d8 en moyenne quand je le décide, la mort si elle y succombe")]),
"debilitating-pain": EP("Douleur débilitante", NORD, 3, ["douleur", "étourdissement"], why="étourdie par la douleur", cible_note=["psyché"],
    options=[O("Douleur débilitante"), O("Douleur débilitante de groupe", src_idx="debilitating-pain-mass", qty_cible=3)]),
"demon-dream": EP("Cauchemar ténébreux", NQ, 3, ["cauchemar", "folie"], 3, "1d6 en moyenne retiré à la lucidité, le repos ruiné", cible_note=["psyché", "lucidité"], cond=["sommeil"], impact_add=["ténébreux"], loc=("plein", None, "illimitée")),
"draconic-malice": EP("Malveillance draconique", NINT, P, ["peur", "immunité"], why="nul n'est plus à l'abri de la peur que j'inspire", cible_note=["psyché"], cond=["VIVANT"], aoe={"type": "sphere", "size": 10}),
"enticing-adulation": EP("Adulation", REL, 3, ["adoration", "protection"], why="elle me choie et me défend", cible_note=["psyché"],
    impact_plus=[(2, ["fureur", "force", "endurance"], "2 ajouté à sa force et à son endurance quand on me blesse")]),
"fiendish-wrath": EP("Courroux féroce", INT, 2, ["frénésie", "déchirure"], 2, "2 ajouté à la force et à l'endurance ; deux coups de griffe déchirent", cible_note=["force", "endurance"], cond=["VIVANT"]),
"heretics-tongue": EP("Langue de l'hérétique", NREL, 3, ["sort", "interdit", "blasphème"], why="l'esprit empli de blasphèmes, elle ne peut plus lancer de sorts", cible_note=["psyché"], cond=["VIVANT"],
    impact_plus=[(P, ["cri", "paralysie", "effroi"], "elle peut s'en délivrer en hurlant ses blasphèmes : paralysée la moitié du temps restant, ses alliés effrayés")]),
"hermean-potential": EP("Potentiel accompli", INT, 2, ["clarté", "réussite"], why="sa prochaine épreuve tentée avec la meilleure chance", cible_note=["psyché"]),
"matchmaker": EP("Entremetteur", REL, 4, ["amour", "attirance"], why="deux êtres épris l'un de l'autre", cible_note=["psyché"], cond=["VIVANT"], qty_cible=2),
"mortal-terror": EP("Terreur mortelle", V("force", True), 3, ["peur", "croissance", "paralysie"], why="une peur qui grandit à chaque blessure, jusqu'à la figer", cible_note=["psyché"]),
"sacrifice": EP("Sacrifice", REL, 9, ["marché", "contrainte"], why="un sacrifice qui aide à appeler, lier ou payer l'être convoqué", cond=["sacrifice"]),
"sow-thought": EP("Pensée semée", REL, 3, ["idée", "sienne"], why="une idée qu'elle croit sienne", cible_note=["psyché"]),
"touch-of-madness": EP("Contact de folie", NORD, 3, ["hébétude", "folie"], why="hébétée au toucher", cible_note=["psyché"]),
"unshakeable-zeal": EP("Zèle inébranlable", INT, 2, ["zèle", "revanche"], 4, "4 ajouté à la tentative qui suit un échec ; une peur ou un désespoir écarté", cible_note=["psyché"]),
# -- Illusion
"assumed-likeness": IL("Semblance prêtée", NVIS, 1, ["apparence", "souvenir", "émotion"], why="chacun me voit sous les traits de qui lui inspire l'émotion choisie", cosm=(1, "sens trompé")),
"blend-with-surroundings": IL("Fondu dans le décor", NVIS, 2, ["décor", "immobilité"], why="l'air d'une statue, d'un meuble, d'un arbre tant qu'elle ne bouge pas", cosm=(1, "sens trompé"), fin=["mouvement"]),
"charnel-house": IL("Charnier", EXI, P, ["sang", "nausée", "glissade", "quasi-réel"], why="un carnage à demi réel : la nausée, et un sol où l'on glisse", cond=["sacrifice"], cosm=(2, "sens trompé")),
"cloak-of-secrets": IL("Manteau de secrets", NVIS, P, ["conversation", "leurre"], why="au dehors on entend et on lit sur les lèvres une tout autre conversation", cosm=(2, "sens trompé")),
"fools-gold-vc": IL("Or des dupes", NVIS, 4, ["or", "valeur"], why="le cuivre ou l'argent prend l'aspect de l'or", cible_obj=["métal"], cosm=(1, "sens trompé")),
"fools-teleport": IL("Fausse téléportation", NVIS, 1, ["invisibilité", "téléportation", "leurre"], why="invisible, sous l'apparence et le bruit d'un départ par téléportation", cosm=(2, "sens trompé")),
"illusory-crowd": IL("Foule illusoire", EXI, P, ["foule", "image", "gêne"], why="une foule qui va, vient, parle et encombre", cosm=(2, "sens trompé")),
"inhibiting-patterns": IL("Motifs inhibiteurs", V("mouvement", True), P, ["colonne", "couleur", "arrêt"], why="des colonnes de couleurs qu'on ne franchit pas", impact_add=["éblouissement"], sens=[("vue", None)], manif=["colonnes", "couleurs"]),
"oath-of-anonymity": IL("Serment d'anonymat", NVIS, 1, ["identité", "voix", "allure"], why="ma voix, mon allure, mon équipement et mes bêtes rendus méconnaissables", cosm=(2, "sens trompé"), fin=["visage"]),
"scintillating-wall": IL("Mur scintillant", REL, P, ["fascination", "mur"], why="qui traverse le mur reste fasciné", impact_add=["éblouissement", "cécité"], sens=[("vue", None)], manif=["mur", "couleurs"]),
"semblance-of-flesh": IL("Semblant de chair", NVIS, 2, ["chair", "apparence"], why="l'artefact animé prend l'aspect d'un être de chair", cond=["ARTEFACT"], cosm=(1, "sens trompé")),
"shadow-dragon-aspect": IL("Aspect du dragon d'ombre", V("nature"), 1, ["dragon", "griffe", "quasi-réel"], 10, "des griffes d'ombre, 1d6 + 7 en moyenne",
    impact_plus=[(11, ["croc", "gueule"], "une gueule d'ombre, 1d8 + 7 en moyenne"), (9, ["vol", "mètres", "aile"], "des ailes d'ombre : vol à 9 m par instant")], sens=[("vue", None)], manif=["dragon", "ombre"]),
"shadow-enchantment": IL("Enchantement d'ombre", REL, 3, ["ombre", "enchantement", "quasi-réel"], why="un enchantement imité, à demi réel", cible_note=["psyché"], impact_sats=[(2, ["niveau"])],
    options=[O("Enchantement d'ombre"), O("Enchantement d'ombre supérieur", src_idx="shadow-enchantment-greater", impact_sats=[(5, ["niveau"])])]),
"silt-sphere": IL("Sphère de vase", NVIS, P, ["vase", "nuage", "dissimulation"], why="un nuage de vase illusoire qui cache ceux qu'il enveloppe et me suit", cosm=(1, "sens trompé"), fin=["agression"]),
}
FICHES.update(SUITE1)

# ----- Suite, lot 2 : Nécromancie -----
PF1_RELECTURE.update({
 "bleed-glory": "agit sur le « pouvoir mythique », sous-système de règles propre à Pathfinder",
 "mythic-severance": "agit sur le « pouvoir mythique », sous-système de règles propre à Pathfinder",
 "steal-power": "agit sur le « pouvoir mythique », sous-système de règles propre à Pathfinder",
 "eldritch-fever": "inflige un « fléau magique » (spellblight), sous-système de règles propre à Pathfinder",
 "steal-voice": "inflige un « fléau magique » (spellblight), sous-système de règles propre à Pathfinder",
 "malediction-hero-points": "repose sur les « points d'héroïsme » : pure mécanique de jeu",
 "curse-terrain-lesser": "repose sur les « domaines périlleux », sous-système de règles propre à Pathfinder",
 "curse-terrain": "repose sur les « domaines périlleux », sous-système de règles propre à Pathfinder",
 "curse-terrain-greater": "repose sur les « domaines périlleux », sous-système de règles propre à Pathfinder",
 "curse-terrain-supreme": "repose sur les « domaines périlleux », sous-système de règles propre à Pathfinder",
 "pesh-addiction": "n'ordonne que l'usage du pesh, drogue propre à Golarion",
 "pesh-addiction-lesser": "n'ordonne que l'usage du pesh, drogue propre à Golarion",
 "judgement-undone": "défait le jugement de Pharasma sur une âme : propre à la cosmologie de Golarion",
 "what-grows-within": "invoque Xhamen-Dor, entité étrangère à Inarama",
 "infuse-effigy": "repose sur les effigies rituelles des Terres des rois linnorms, propres à Golarion",
 "project-weakness": "ne se lance que par un vampire et transmet ses faiblesses (ail, miroirs, soleil), qui ne sont pas établies dans Inarama",
})
PF1_MEME.update({"create-variant-mummy": "create-undead"})

SUITE2 = {
"aura-of-cannibalism": EP("Aura de cannibalisme", V("flux"), P, ["blessure"], 2, "1d4 en moyenne à chaque instant, à mes semblables", cond=["semblable"],
    impact_sats=[(15, ["vie", "temporaire"]), (2, ["vigueur"])]),
"black-sword-of-war": EP("Épée noire de la guerre", INT, 1, ["saignement"], 2, "chaque blessure saigne de 2 par instant", cible_obj=["arme"], sens=[("vue", None)], manif=["noir"]),
"bleeding-strike": EP("Frappe saignante", INT, 1, ["saignement", "ténacité"], 1, "1 de saignement, difficile à arrêter", cible_obj=["arme"], cond=["coup", "VIVANT"]),
"blood-of-the-martyr": EP("Sang du martyr", V("flux", True), 4, ["saignement"], 3, "1d6 en moyenne par instant", cible_note=["sang"], cond=["VIVANT"],
    impact_plus=[(7, ["vie", "boire"], "qui boit ce sang guérit du double de ce qu'elle perd")]),
"blood-tentacles": EP("Tentacules de sang", EXI, 1, ["tentacule"], 7, "2d6 en moyenne par tentacule", cible_note=["sang"], qty=9,
    impact_sats=[(7, ["vie", "temporaire"])], sens=[("vue", None)], manif=["tentacules", "sang"]),
"blood-ties": EP("Liens du sang", REL, 3, ["partage", "blessure"], why="ce que subit l'otage, son parent le subit aussi, où qu'il soit", cible_note=["sang"], cond=["VIVANT", "otage", "parenté"], qty_cible=2),
"bloody-tears-and-jagged-smile": EP("Larmes de sang et sourire acéré", TR, 1, ["effroi"], 4, "4 ajouté à la peur que j'inspire", cible_note=["œil", "croc"],
    impact_plus=[(2, ["croc", "morsure"], "1d4 en moyenne"), (P, ["agonie", "vision"], "je vois qui est mourant, blessé, mort ou mort-vivant")], sens=[("vue", None)], manif=["larmes", "sang"]),
"canopic-conversion": EP("Conversion canope", NE, 3, ["éviscération"], 59, "17d6 en moyenne", cond=["humanoïde", "VIVANT"],
    impact_plus=[(P, ["momie", "canope", "emprise"], "tuée, elle se relève en momie ; ses organes scellés dans quatre vases donnent prise sur elle")]),
"create-soul-gem": EP("Création d'une gemme d'âme", V("mouvement", True), 3, ["mort", "gemme"], why="la vie qui s'éteint tirée dans une gemme", cible_note=["âme"], cond=["mourant"]),
"deathless": EP("Sans-mort", V("nature", True), 2, ["mort", "refus"], why="aucune blessure ne peut la tuer", cible_note=["âme", "corps"], cond=["VIVANT"]),
"drain-construct": EP("Artefact vidé", NINT, 3, ["lenteur", "faiblesse"], 4, "4 retiré à sa force, son pas réduit de moitié, ses défenses innées éteintes", cible_note=["force"], cond=["ARTEFACT"]),
"earsend": EP("Oreille envoyée", ID, 1, ["possession", "ouïe", "vol"], why="mon oreille détachée vole et entend pour moi", cible_note=["oreille"]),
"enemys-heart": EP("Cœur de l'ennemi", V("flux"), 3, ["dévoration", "mort"], why="son cœur arraché et mangé, sa force prise", cible_note=["cœur"], cond=["VIVANT", "inerte"],
    impact_sats=[(8, ["vie", "temporaire"]), (2, ["force"])]),
"ghoul-hunger": EP("Faim de goule", NQ, 3, ["faim", "chair", "dévoration"], why="se jette sur un corps inerte ou mort et le dévore", cible_note=["psyché"], cond=["humanoïde"]),
"hasten-judgement": EP("Jugement hâté", NQ, 3, ["mort", "rappel", "entrave"], why="morte sous le sort, elle ne peut guère être rappelée à la vie", cible_note=["âme"],
    options=[O("Sur un vivant"), O("Sur un mort-vivant", cond=["MORTVIVANT"], impact=(P, ["affaiblissement", "réserve"], "sa force d'animation affaiblie : plus de vie d'emprunt, sa résistance au renvoi réduite de moitié"))]),
"healing-leak": EP("Fuite des soins", NINT, 3, ["soin", "fractionné"], 2, "les soins qu'elle reçoit ou donne réduits de moitié"),
"horrifying-visage": EP("Vision d'horreur", V("force", True), P, ["phobie", "objet"], why="la peur panique d'une chose désignée", cible_note=["psyché"]),
"hunger-for-flesh": EP("Faim de chair", NQ, 3, ["faim", "chair", "semblable", "chancellement"], why="chancelante de faim, poussée à mordre ses semblables", cible_note=["corps"],
    impact_plus=[(4, ["croc", "morsure"], "1d6 en moyenne")],
    options=[O("Faim de chair"), O("Faim de chair de groupe", src_idx="hunger-for-flesh-mass", qty_cible=P)]),
"impede-speech": EP("Élocution entravée", NINT, 3, ["élocution", "sort", "échec"], why="peine à parler ; un sort prononcé sur deux échoue", cible_note=["voix"]),
"infuse-decay": EP("Infusion de pourriture", REL, 2, ["sort", "transfert", "contact"], why="des sorts de contact confiés à un mort-vivant", cond=["MORTVIVANT"]),
"limp-lash": EP("Fouet d'atonie", NINT, 3, ["fouet", "paralysie"], 3, "1d6 en moyenne retiré à chaque instant, jusqu'à la paralysie du corps", cible_note=["force", "adresse", "endurance"],
    sens=[("vue", None)], manif=["fouet", "ténèbres"]),
"litany-of-the-red-crusader": EP("Litanie de la croisée rouge", NQ, 3, ["saignement", "cumul"], 1, "1 de saignement de plus à chaque coup tranchant ou perforant", cible_note=["sang"], cond=["coup"]),
"malediction": EP("Malédiction de damnation", NQ, 3, ["damnation", "mort"], why="si elle meurt dans la minute, son âme est damnée", cible_note=["âme"], impact_add=["ténébreux"]),
"night-blindness": EP("Cécité nocturne", NINT, 3, ["vision", "pénombre"], why="voit comme si la lumière était d'un degré plus faible, et plus du tout dans le noir", cible_note=["œil"], cond=["VIVANT"], impact_sats=[(4, ["résistance", "éclat"])]),
"plundered-power": EP("Pouvoir pillé", V("flux"), 3, ["pouvoir", "inné", "sanguine"], why="le pouvoir magique inné de l'être sacrifié enfermé dans une pierre de sang", cond=["sacrifice"]),
"recorporeal-incarnation": EP("Incarnation d'emprunt", ID, 2, ["corps", "apparence", "aptitude"], why="un vivant revêt le corps d'un mort, son apparence et ses facultés", cible_note=["corps"], cond=["VIVANT", "cadavre"]),
"sacramental-seal": EP("Sceau sacramentel", V("mouvement", True), 3, ["prison", "objet", "symbole"], why="enfermée dans un objet consacré tant que je le garde", cond=["détention"]),
"sentry-skull": EP("Crâne sentinelle", VIS, 4, ["guet", "vue", "ouïe"], why="une tête tranchée rend ses sens, que je peux emprunter", cible_obj=["crâne"], impact_add=["cécité", "surdité"],
    impact_plus=[(18, ["vision", "obscurité", "mètres"], "voit dans le noir à 18 m")]),
"shared-suffering": EP("Souffrance partagée", NE, 3, ["nécrose", "partage"], 7, "2d6 en moyenne, que je m'inflige d'abord", cond=["VIVANT", "sacrifice"]),
"sotto-voce": EP("Sotto voce", V("force", True), 3, ["peur", "murmure"], why="effrayée un instant par un murmure", cible_note=["psyché"], cond=["humanoïde", "seuil"], cond_sats=[(18, ["vie"])]),
"soulreaver": EP("Faucheur d'âmes", NE, P, ["mort"], 52, "15d6 en moyenne", cond=["VIVANT"], cible_note=["âme"]),
"spectral-saluqi": EP("Lévrier spectral", EXI, 7, ["traque", "éthéré", "télépathie"], why="un grand chien mort-vivant qui me parle par la pensée et mord jusqu'aux êtres de l'éther", cible_note=["molosse", "mort-vivant"]),
"suffocation-instant": EP("Étouffement foudroyant", NE, 3, ["mort", "étouffement"], why="morte étouffée sur-le-champ", cible_note=["souffle"], cond=["VIVANT"]),
"suffocation-slow": EP("Étouffement lent", NREL, 3, ["apnée"], why="ne peut plus respirer", cible_note=["souffle"], cond=["VIVANT"], fin=["choc"]),
"tomb-legion": EP("Légion des tombes", EXI, 7, ["momie", "service"], why="des momies puissantes à mon service", cible_note=["mort-vivant"], qty=4),
"umbral-infusion": EP("Infusion d'ombre", INT, 2, ["ombre", "puissance", "fureur"], 2, "2 ajouté à tout ce qu'il fait, 4 à sa défense ; il échappe une fois sur deux à qui le commande", cond=["MORTVIVANT"],
    options=[O("Infusion d'ombre"), O("Infusion d'ombre de groupe", src_idx="umbral-infusion-mass", qty_cible=P)]),
"unlock-flesh": EP("Chair déverrouillée", NORD, 3, ["chancellement"], why="la chair qui glisse sur les os la laisse chancelante", cible_note=["chair"],
    options=[O("Sur un vivant", cond=["VIVANT"]), O("Sur un mort-vivant de chair", cond=["MORTVIVANT"], verb=NE, impact=(17, ["lambeaux"], "5d6 en moyenne : sa chair tombe par lambeaux"))]),
"urgathoas-beacon": EP("Fanal des affamés", V("force"), P, ["mort-vivant", "attirance", "proie"], why="qui traverse la zone attire les morts-vivants, qui veulent le dévorer"),
"virulence": EP("Virulence", NQ, P, ["maladie", "accès"], why="toute maladie contractée frappe aussitôt", cond=["VIVANT"], cible_note=["corps"], aoe={"type": "sphere", "size": 40}),
"wracking-ray": EP("Rayon de torsion", NINT, 3, ["spasme", "nécrose"], 7, "3d4 en moyenne retiré à l'adresse et à la force", cible_note=["adresse", "force"], sens=[("vue", None)], manif=["rayon", "verdâtre"]),
}
FICHES.update(SUITE2)

# ----- Suite, lot 3 : Invocation -----
_FIEL = "ne convoque que des fiélons nommés des Abysses ou des Enfers, propres à la cosmologie de Golarion"
PF1_RELECTURE.update({
 "dream-travel": "mène dans une « Dimension des Rêves », absente de la cosmologie d'Inarama",
 "dream-voyage": "mène dans une « Dimension des Rêves », absente de la cosmologie d'Inarama",
 "genius-avaricious": "est un rite de sacrifice à l'archidiable Mammon, propre à la cosmologie de Golarion",
 "open-the-dead-roads": "ouvre les Routes des Morts, réseau propre à la cosmologie de Golarion",
 "spawn-calling": "appelle les Rejetons de Rovagug, propres au monde de Golarion",
 "summon-accuser": _FIEL, "summon-barghest-i": _FIEL, "summon-barghest-ii": _FIEL, "summon-greater-demon": _FIEL, "summon-lesser-demon": _FIEL,
 "vermicious-assumption": _FIEL,
 "summon-laborers": "convoque des « pétitionnaires » et repose sur les règles de gestion entre deux aventures : cosmologie de Golarion et mécanique de jeu",
 "sustaining-legend": "agit sur le « pouvoir mythique », sous-système de règles propre à Pathfinder",
 "teleport-structure": "repose sur les règles de gestion d'une cité : pure mécanique de jeu",
})

SUITE3 = {
"alleviate-addiction": EP("Répit de la dépendance", V("qualite"), 2, ["dépendance", "répit"], why="la dépendance sans effet le temps du sort, le corps peut s'en remettre"),
"alter-summoned-monster": EP("Échange de l'être convoqué", TR, 9, ["échange"], why="un être convoqué remplacé par un autre de même rang ou moindre", cible_note=["invoqué"]),
"arid-refuge": EP("Refuge au sec", EXI, P, ["abri", "pierre", "étanche"], why="une bâtisse de pierre qui garde son air, même au fond de l'eau", aoe={"type": "cube", "size": 20}),
"beanstalk": EP("Haricot géant", EXI, P, ["tige", "escalade", "mètres"], 105, "une tige de 105 m que l'on gravit comme une corde à nœuds", comp=["graine"], no_aoe=True),
"blade-tutors-spirit": EP("Esprit du maître d'armes", INT, 1, ["esprit", "guidage"], 1, "1 rendu aux coups portés en se gardant ou en s'emportant", cible_note=["frappe"]),
"create-drug": EP("Création de drogue", EXI, 1, ["éphémère"], why="une dose de drogue, à prendre dans la minute", cible_obj=["drogue"]),
"drench": EP("Averse", EXI, 4, ["averse", "extinction"], why="une ondée qui trempe la cible et éteint les petites flammes"),
"drunkards-breath": EP("Haleine d'ivrogne", NQ, P, ["nausée", "ivresse", "poison"], why="une haleine presque invisible qui donne la nausée d'un lendemain d'ivresse", cond=["souffle"], aoe={"type": "cone", "size": 30}),
"elemental-bombardment": EP("Bombardement élémentaire", V("trame"), 9, ["projection", "choc"], why="des élémentaires jetés de haut sur l'ennemi, qui combattent ensuite", cible_note=["élémentaire"], impact_sats=[(18, ["hauteur", "mètres"])],
    options=[O("Huit élémentaires moyens", impact=(21, ["projection", "choc"], "6d6 en moyenne chacun"), qty=8), O("Quatre grands élémentaires", impact=(28, ["projection", "choc"], "8d6 en moyenne chacun"), qty=4),
             O("Deux très grands élémentaires", impact=(42, ["projection", "choc"], "12d6 en moyenne chacun"), qty=2), O("Un élémentaire majeur", impact=(42, ["projection", "choc"], "12d6 en moyenne"), qty=1)]),
"false-resurrection": EP("Fausse résurrection", V("trame"), 9, ["résurrection", "leurre", "possession"], why="le corps revit, mais c'est un être de la face ténébreuse qui l'habite", cible_sym=["tenebreux"], cond=["cadavre"],
    options=[O("Fausse résurrection"), O("Fausse résurrection suprême", src_idx="false-resurrection-greater", impact=(P, ["résurrection", "leurre", "possession", "corps"], "même sans dépouille, et sans terme"))]),
"genesis": EP("Genèse", EXI, P, ["création", "croissance"], why="un demi-plan qui s'étend de jour en jour, façonné à ma guise", cible_note=["plan"], aoe={"type": "sphere", "size": 180}),
"instant-clot": EP("Caillot instantané", ORD, 2, ["saignement", "arrêt"], why="tout saignement cesse ; ses plaies ne versent plus de sang", cible_note=["sang"], cond=["VIVANT"]),
"lead-plating": EP("Gaine de plomb", EXI, 4, ["plomb", "gaine", "divination"], why="une fine gaine de plomb qui arrête les sorts de divination"),
"maze-of-madness-and-suffering": EP("Labyrinthe de folie et de souffrance", V("trame", True), 3, ["labyrinthe", "folie", "souffrance"], why="bannie dans un labyrinthe dont chaque quartier la tourmente", fam="A", cible_note=["psyché"],
    impact_plus=[(11, ["forêt", "effroi", "lacération"], "la forêt hantée : effroi, et 3d6 en moyenne"), (14, ["feu", "paralysie", "supplice"], "le paysage infernal : paralysie de peur, puis 4d6 en moyenne, mortel"),
                 (P, ["oasis", "fascination", "léthargie"], "l'oasis : fascination, jusqu'à renoncer à sortir")]),
"mud-buddy": EP("Compagnon de boue", EXI, 7, ["boue", "nage", "croc-en-jambe"], why="un petit serviteur de boue, qui nage et peut faire tomber", cible_note=["serviteur"]),
"penumbral-disguise": EP("Déguisement de pénombre", NVIS, 2, ["déguisement", "discrétion", "pénombre"], 5, "5 ajouté au déguisement et à la discrétion hors du plein jour ; ses traits indiscernables dans la pénombre", sens=[("vue", None)], manif=["ombre"]),
"purify-body": EP("Purification du corps", HE, 2, ["vie"], 20, "3d8 + 7 en moyenne", cond=["VIVANT"], guerit=True,
    impact_plus=[(P, ["douleur", "faiblesse", "cécité", "surdité", "nausée", "paralysie"], "ôte la douleur, les atteintes du corps, la cécité, la surdité, la nausée et la paralysie")],
    impact_sats=[(P, ["excédent", "temporaire"])]),
"reincarnate-spy": EP("Réincarnation en sosie", TR, 7, ["vie", "corps", "renaissance", "ressemblance"], why="revient à la vie dans un corps neuf, façonné à la ressemblance d'un autre", cond=["mort"]),
"rift-of-ruin": EP("Faille de ruine", EXI, P, ["faille", "chute"], 21, "6d6 en moyenne pour la chute", impact_add=["ténébreux"], impact_sats=[(18, ["profondeur", "mètres"])],
    impact_plus=[(21, ["lame", "tourment"], "6d6 en moyenne à chaque instant passé dans la faille"),
                 (P, ["fermeture", "invocation", "ténébreux"], "je peux refermer la faille pour en faire sortir des êtres de la face ténébreuse")]),
"soothing-word": EP("Parole apaisante", V("qualite"), 2, ["apaisement", "degré"], why="nausée, étourdissement, épuisement, effroi et paralysie ramenés chacun au degré moindre"),
"summon-elemental-steed": EP("Convocation d'un char élémentaire", V("trame"), 9, ["char", "transport"], why="un élémentaire majeur lié en forme de char", cible_note=["élémentaire"], impact_sats=[(9, ["passager"])]),
"summon-genie-lesser": EP("Convocation de génie", V("trame"), 9, [], 1, "un génie mineur", cible_note=["génie"],
    options=[O("Convocation de génie mineure"), O("Convocation de génie", src_idx="summon-genie", impact=(2, [], "un génie des vents, ou deux génies mineurs")),
             O("Convocation de génie supérieure", src_idx="summon-genie-greater", impact=(3, [], "un génie de la terre, deux génies des vents ou trois génies mineurs"))]),
"sundered-serpent-coil": EP("Serpent décapité", EXI, 3, ["serpent", "étreinte"], 8, "1d6 + 4 en moyenne à chaque instant", sens=[("vue", None)], manif=["serpent"]),
"teratoid-caress": EP("Caresse tératogène", NQ, 3, ["difformité"], 2, "2 retiré à l'adresse ou à la prestance", cible_note=["adresse", "prestance", "corps"], cond=["VIVANT"], impact_add=["ténébreux"]),
"treacherous-teleport": EP("Téléportation traîtresse", V("mouvement"), 2, ["lieu", "passage", "traîtrise"], why="ceux que je choisis arrivent ailleurs, ou mal"),
"true-creation": EP("Création véritable", EXI, 1, ["matière", "réel", "permanent"], why="un objet bien réel et durable, de toute matière", cible_obj=["OBJET"]),
"unseen-engineers": EP("Ingénieurs invisibles", EXI, 7, ["piège", "construction"], why="une équipe invisible qui monte un piège en quelques instants", cible_note=["serviteur"]),
"vomit-twin": EP("Jumeau régurgité", V("identite", True), 1, ["double", "échange", "visqueux"], why="un double visqueux avec lequel j'échange ma place"),
"web-bolt": EP("Trait de toile", EXI, 3, ["toile", "entrave", "projectile"], why="une boule de toile qui englue une seule créature"),
"web-cloud": EP("Nuage de toile", EXI, P, ["toile", "entrave", "nuage", "dérive"], why="un nuage de fils collants qui roule au sol et englue ceux qu'il traverse"),
}
FICHES.update(SUITE3)

# ----- Suite, lot 4 : Évocation -----
_CTH = "ne joint que des entités du mythe de Cthulhu dont le jeu dresse la liste, étrangères à Inarama"
PF1_RELECTURE.update({
 "heroic-fortune": "repose sur les « points d'héroïsme » : pure mécanique de jeu",
 "heroic-fortune-mass": "repose sur les « points d'héroïsme » : pure mécanique de jeu",
 "imbue-army-special-ability": "agit sur une armée du sous-système de batailles : pure mécanique de jeu",
 "violent-misfire": "met en jeu les armes à feu, absentes d'Inarama",
 "violent-misfire-greater": "met en jeu les armes à feu, absentes d'Inarama",
 "contact-entity-i": _CTH, "contact-entity-ii": _CTH, "contact-entity-iii": _CTH, "contact-entity-iv": _CTH,
})
EV = lambda fr, cible, words, v=None, why="", **kw: EP(fr, NE, cible, words, v, why, **kw)

SUITE4 = {
"bit-of-luck": EP("Brin de chance", INT, 1, ["chance", "réserve"], 4, "1d8 en moyenne ajouté à une tentative, deux fois", cible_note=["aptitude"], impact_sats=[(2, ["usage"])]),
"blacklight": EP("Lumière noire", NVIS, P, ["ténèbres", "impénétrable"], why="une obscurité que nul regard ne perce, sauf le mien", sens=[("vue", None)], manif=["ténèbres"], aoe={"type": "sphere", "size": 20}),
"bolt-of-glory": EV("Trait de gloire", 3, ["lumineux"], 17, "5d6 en moyenne aux êtres du monde et des éléments", fam="A",
    impact_sats=[(38, ["si:ténébreux"]), (38, ["si:mort-vivant"])], sens=[("vue", None)], manif=["rayon", "lumière"]),
"breeze": EP("Brise", INT, 2, ["brise", "fraîcheur"], 2, "2 ajouté à la résistance contre la chaleur, les souffles et les vapeurs", cible_note=["résistance"]),
"burst-with-light": EV("Éclatement de lumière", 3, ["lumineux"], 7, "2d6 en moyenne, la lumière jaillit de ses plaies", fam="A", impact_sats=[(9, ["si:mort-vivant"])], impact_add=["cécité"],
    impact_plus=[(9, ["clarté", "mètres"], "elle éclaire vivement à 9 m et rehausse la lumière au-delà")], sens=[("vue", None)], manif=["lumière", "éclat"]),
"crown-of-glory": EP("Couronne de gloire", INT, 1, [], 4, "4 ajouté à la prestance", cible_note=["prestance"], comp=["opale"],
    impact_plus=[(P, ["attention", "fascination", "suggestion"], "les êtres de moindre puissance s'arrêtent, m'écoutent, me comprennent, et suivent trois suggestions")],
    sens=[("vue", None)], manif=["couronne", "lumière"]),
"curse-of-night": EP("Malédiction de la nuit", NINT, P, ["lumière", "nuit", "malédiction"], why="un lieu voué à la pénombre : le jour n'y est qu'un clair de lune, les plantes s'y étiolent", loc=(1600, "METRES", "1,6 km alentour"),
    sens=[("vue", None)], manif=["pénombre"]),
"dark-light": EP("Lumière aveuglante", NINT, P, ["lumière"], why="une lumière qui aveugle", impact_add=["cécité", "éblouissement"], cond=["VIVANT"], sens=[("vue", None)], manif=["lumière"]),
"diamond-spray": EV("Gerbe de diamant", P, ["tranchant", "diamant"], 17, "5d6 en moyenne", aoe={"type": "cone", "size": 20}, sens=[("vue", None)], manif=["éclats", "scintillement"]),
"elemental-assessor": EV("Jauge élémentaire", 3, ["acide"], 7, "2d6 en moyenne", fam="A",
    impact_plus=[(7, ["froid"], "2d6 en moyenne"), (7, ["foudre"], "2d6 en moyenne"), (7, ["feu"], "2d6 en moyenne"), (14, ["persistance"], "l'énergie qui l'a le plus blessée persiste, 4d6 en moyenne à chaque instant")],
    sens=[("vue", None)], manif=["rayon", "couleurs"]),
"fire-sneeze": EV("Éternuement de feu", P, ["feu", "éternuement"], 7, "2d6 en moyenne à chaque éternuement", impact_add=["chute"], aoe={"type": "cone", "size": 10}, sens=[("vue", None)], manif=["flamme"]),
"frosthammer": EV("Marteau de givre", 3, ["froid", "marteau"], 9, "2d8 en moyenne, moitié choc, moitié froid", impact_add=["chute"], sens=[("vue", None)], manif=["marteau", "glace"]),
"ghost-whip": EP("Fouet fantôme", EXI, 1, ["fouet", "spectral", "intangible"], why="un fouet d'ectoplasme qui traverse les obstacles et saisit les êtres sans corps", cible_obj=["arme"], impact_sats=[(5, ["longueur", "mètres"])], sens=[("vue", None)], manif=["fouet", "blanc"]),
"hellfire-ray": EV("Rayon de feu ténébreux", 3, ["feu"], 19, "la moitié de 11d6, en feu", fam="A",
    impact_plus=[(19, ["ténébreux", "damnation"], "l'autre moitié, de la face ténébreuse, que rien n'atténue ; qui en meurt est difficile à rappeler")], sens=[("vue", None)], manif=["rayon", "flamme"]),
"hurricane-blast": EP("Rafale d'ouragan", V("force", True), P, ["vent", "renversement", "recul"], why="un vent de tempête qui roule les petits, renverse et arrête les autres, et souffle les flammes", sens=[("ouïe", None), ("toucher", None)], manif=["vent"]),
"penumbra": EP("Pénombre", SEP, 2, ["ombre", "éblouissement"], why="une ombre légère qui épargne les maux du plein jour", cible_note=["œil"]),
"scoop": EP("Écope", EXI, 1, ["récipient", "force"], why="un petit vase de force qui puise, porte et verse un demi-litre", cible_obj=["récipient"]),
"torrent-of-elemental-rage": EV("Torrent de rage élémentaire", P, ["feu"], 7, "2d6 en moyenne", fam="A",
    impact_plus=[(7, ["froid"], "2d6 en moyenne"), (7, ["tonnerre"], "2d6 en moyenne"), (7, ["tranchant", "éclat"], "2d6 en moyenne")],
    aoe={"type": "line", "size": 30}, sens=[("vue", None), ("ouïe", None)], manif=["tourbillon", "hurlement"]),
"veil-of-ash": EV("Voile de cendre", 3, ["feu", "cendre"], 4, "1d6 en moyenne à chaque instant", impact_add=["cécité"], cible_note=["visage"], sens=[("vue", None)], manif=["cendre"]),
"wall-of-light": EP("Mur de lumière", EXI, P, ["mur", "lumière"], why="un rideau de lumière blanche qui arrête le regard et aveugle", impact_add=["cécité"], rayonnement=True,
    impact_sats=[(2, ["si:ténébreux"])], sens=[("vue", None)], manif=["mur", "lumière"]),
"water-shield": EP("Bouclier d'eau", SEP, 1, ["acide", "riposte"], 5, "1d6 + 2 en moyenne à qui me frappe au corps à corps", cible_note=["garde"], fam="A",
    impact_plus=[(P, ["feu", "moitié"], "le feu ne me blesse qu'à moitié"), (P, ["acide", "moitié"], "l'acide ne me blesse qu'à moitié")], sens=[("vue", None)], manif=["trombe"]),
}
FICHES.update(SUITE4)

# ----- Suite, lot 5 : Transmutation -----
_PEU = "propre à un peuple : à reprendre avec les sorts peuple par peuple"
_NAT = "ne sert qu'aux créatures dotées d'un pouvoir naturel précis : à reprendre avec les sorts peuple par peuple"
_MYT = "agit sur le « pouvoir mythique », sous-système de règles propre à Pathfinder"
_NAG = "donne la forme d'un naga, créature qui n'est pas établie dans Inarama"
PF1_RELECTURE.update({
 "ancestral-regression": _PEU, "ignoble-form": _PEU, "half-blood-extraction": _PEU, "gift-of-the-deep": _PEU, "chameleon-scales": _PEU, "thanatotic-fury": _PEU,
 "fey-blight": "ne se lance que par une fée et transmet le fléau de sa lignée : " + _PEU,
 "amplify-stench": _NAT, "transfer-regeneration": _NAT,
 "lend-path": _MYT, "restore-mythic-power": _MYT, "share-glory": _MYT, "terraform": _MYT,
 "naga-shape-i": _NAG, "naga-shape-ii": _NAG, "naga-shape-iii": _NAG,
 "arcane-cannon": "fait paraître un canon : met en jeu les armes à feu, absentes d'Inarama",
 "borrow-corruption": "repose sur la « corruption », sous-système de règles propre à Pathfinder",
 "renovation": "repose sur les règles de construction entre deux aventures : pure mécanique de jeu",
 "ceremony": "repose sur la divinité du prêtre et ses domaines : mécanique de classe",
 "invoke-deity": "repose sur les domaines divins du prêtre : mécanique de classe",
 "form-of-the-alien-dragon-iii": "classe de dragons propre à Pathfinder (le dragon reste, sans ces titres)",
})

SUITE5 = {
"abyssal-vermin": EP("Vermine ténébreuse", INT, 2, ["résistance", "châtiment"], why="une vermine endurcie contre les coups, le froid, le feu et les sorts, qui châtie les êtres lumineux", cible_note=["vermine"], impact_add=["ténébreux"]),
"arcane-reinforcement": EP("Renfort arcanique", INT, 1, ["artisanat", "savoir"], why="mon savoir magique guide ma main d'artisan tant que je psalmodie", cible_note=["aptitude"]),
"ashen-path": EP("Chemin de cendre", SEP, 2, ["cendre", "fumée", "poussière"], 4, "respire sans mal l'air souillé ; 4 ajouté contre la magie qui en use", cible_note=["souffle"], cond=["VIVANT"],
    impact_plus=[(18, ["vision", "fumée", "mètres"], "voit à 18 m à travers cendre, fumée et brume")]),
"assume-appearance-greater": EP("Apparence empruntée supérieure", ID, 1, ["apparence", "portrait", "voix"], why="prendre l'allure et la voix d'un être d'après son seul portrait"),
"awaken-construct": EP("Éveil de l'artefact", INT, 2, ["éveil", "conscience", "liberté"], why="un artefact animé reçoit une conscience et sa liberté", cible_note=["psyché", "raison"], cond=["ARTEFACT"]),
"barghest-feast": EP("Festin du dévoreur", V("flux"), 2, ["dévoration", "cadavre", "puissance"], 5, "jusqu'à 5 ajouté à tout ce qu'elle entreprend, à mesure qu'elle dévore un humanoïde mort"),
"batrachian-surge": EP("Élan batracien", TR, 1, ["batracien"], why="un trait d'amphibien, pour un instant", options=[
    O("Branchies", impact=(P, ["batracien", "branchies", "eau"], "respirer sous l'eau"), cible_note=["souffle"]),
    O("Saut", impact=(P, ["batracien", "saut", "élan"], "des jambes longues et puissantes"), cible_note=["jambe"]),
    O("Nage", impact=(9, ["batracien", "nage", "mètres"], "une queue de têtard : nage à 9 m par instant"), cible_note=["queue"]),
    O("Langue", impact=(P, ["batracien", "allonge", "contact"], "une langue longue comme le corps, pour toucher plus loin"), cible_note=["langue"])]),
"blightburn-weapon": EP("Arme de cristal ardent", TR, 1, ["feu", "cristal"], 7, "2d6 en moyenne à chaque instant de contact", cible_obj=["arme"], impact_add=["maladie", "émanation"], sens=[("vue", None)], manif=["cristal", "lueur"]),
"blood-blaze": EP("Sang ardent", TR, 2, ["feu", "sang", "gerbe"], 4, "1d6 en moyenne : le sang versé alentour s'enflamme et jaillit", cible_note=["sang"], cond=["blessure"]),
"blood-money": EP("Prix du sang", TR, 1, ["composante", "sang"], why="mon sang devient la composante du sort qui suit", cible_note=["sang"], impact_sats=[(4, ["blessure"])]),
"blood-scent": EP("Flair du sang", INT, 2, ["odorat", "sang", "flair"], why="sent et situe les êtres blessés", qty_cible=2),
"blot": EP("Pâté", NE, P, ["effacement", "bavure"], why="tout écrit et tout signe alentour réduit à des taches illisibles", cible_obj=["écrit"]),
"borrowed-time": EP("Temps emprunté", INT, 1, ["temps", "futur", "contrecoup"], why="un instant d'action pris sur l'avenir, payé de ma santé puis d'un chancellement", impact_sats=[(1, ["endurance"])]),
"bouncy-body": EP("Corps élastique", TR, 2, ["souplesse", "rebond"], 2, "2 ajouté pour se dégager ; les chutes amorties de 6 m", cible_note=["chair"]),
"break-greater": EP("Brisure supérieure", TR, P, ["fêlure", "destruction"], why="tous les objets de taille humaine alentour abîmés, ou détruits s'ils l'étaient déjà", cible_obj=["objet"], aoe={"type": "sphere", "size": 30}),
"brightest-night": EP("Nuit claire", VIS, 2, ["vision", "pénombre"], why="voit dans la pénombre, quatre fois plus loin s'il y voyait déjà", cible_note=["œil"], qty_cible=P),
"celestial-companion": EP("Compagnon béni", SEP, 2, ["résistance", "sort"], 7, "7 de résistance aux sorts des êtres hostiles, sa peau gardée de leurs coups", cond=["compagnon", "hostile"], impact_add=["lumineux"], sens=[("vue", None)], manif=["aura", "dorure"]),
"chastise": EP("Remontrance", INT, 1, ["menace", "autorité"], 5, "5 ajouté pour convaincre qu'on s'attirera les foudres de ses supérieurs ou de la loi", cible_note=["prestance"]),
"claim-identity-greater": EP("Visage volé supérieur", ID, 3, ["masque", "identité", "sosie"], why="la cible changée en masque de porcelaine : qui le porte devient son sosie", cible_note=["visage"], cond=["humanoïde"]),
"contact-high": EP("Ivresse partagée", REL, 4, ["drogue", "partage"], why="ceux que je touche ressentent la drogue qui m'habite, sans ses séquelles", cond=["VIVANT"]),
"control-vermin": EP("Maîtrise de la vermine", REL, 3, ["dressage", "contrôle"], why="la vermine se laisse mener comme une bête dressée", cible_note=["vermine"]),
"curse-of-fell-seasons": EP("Malédiction des saisons funestes", TR, P, ["climat", "saison", "malédiction"], why="le temps d'une région bouleversé : froid, canicule ou tempêtes", loc=(3200, "METRES", "3,2 km alentour")),
"cyclic-reincarnation": EP("Réincarnation cyclique", TR, 7, ["vie", "corps", "renaissance", "parenté"], why="revient à la vie dans un corps neuf de son propre peuple, qui ressemble à l'ancien", cond=["mort"]),
"daggermarks-exchange": EP("Échange de poison", TR, 1, ["échange", "régurgitation"], why="un poison avalé sans mal, un autre rendu à sa place", cible_obj=["poison"]),
"deivons-parry": EP("Parade éclair", SEP, 1, ["parade"], why="un coup détourné de mon arme", cible_note=["garde"], cond=["coup"]),
"earth-glide": EP("Glissement de terre", V("mouvement"), 2, ["terre", "traversée"], why="traverse la pierre et la terre comme un poisson l'eau, sans laisser de trace"),
"endothermic-touch": EP("Contact endothermique", NINT, 3, ["métabolisme", "lenteur", "chancellement"], why="le corps ralenti : chancelante, moitié moins vive, mais deux fois plus de souffle", cible_note=["corps"], cond=["VIVANT"]),
"energy-siege-shot": EP("Tir de siège énergétique", TR, 1, ["projectile", "énergie"], why="les projectiles de l'engin changés en énergie pure, au choix", cible_obj=["engin"],
    fam="A", options=[
    O("Acide", impact=(P, ["projectile", "acide", "éclaboussure"], "l'acide éclabousse à 4,5 m pour moitié")),
    O("Froid", impact=(7, ["projectile", "froid", "verglas", "entrave"], "un verglas de 6 m qui entrave et glace, 2d6 en moyenne à chaque instant")),
    O("Foudre", impact=(P, ["projectile", "foudre", "chancellement"], "ceux qu'il touche, à 4,5 m, chancellent")),
    O("Feu", impact=(P, ["projectile", "feu", "embrasement"], "êtres et bois s'embrasent à 4,5 m")),
    O("Son", impact=(P, ["projectile", "tonnerre"], "assourdit à 6 m"), impact_add=["surdité"]),
    O("Force", impact=(P, ["projectile", "force"], "de la force pure")),
    O("Tir de siège énergétique supérieur", src_idx="energy-siege-shot-greater", impact=(P, ["projectile", "énergie", "colossal"], "sur un engin de toute taille, avec les mêmes énergies"))]),
"enlarge-tail": EP("Queue allongée", INT, 1, ["coup"], 2, "1 de justesse et 2 de force aux coups de queue", cible_note=["queue"],
    impact_plus=[(2, ["allonge", "mètres"], "1,5 m d'allonge de plus, arrondi à 2")]),
"flaming-aura": EP("Aura de flammes", TR, 1, ["nature", "feu"], why="le feu devient ma nature", fam="A",
    impact_plus=[(5, ["aura", "feu"], "si j'en suis déjà : une aura de 3 m, 1d8 en moyenne")]),
"frosty-aura": EP("Aura de givre", TR, 1, ["nature", "froid"], why="le froid devient ma nature", fam="A",
    impact_plus=[(5, ["aura", "froid"], "si j'en suis déjà : une aura de 3 m, 1d8 en moyenne")]),
"fleshy-facade": EP("Façade de chair", TR, 2, ["chair", "teint", "vivant"], why="un mort-vivant reprend chair et couleur, et passe pour vivant", cond=["MORTVIVANT"], discret=True),
"fools-gold-aa": EP("Or du dupeur", NQ, 4, ["vulnérabilité", "sort"], 2, "qui garde la pièce résiste moins (2) à ma magie, qui dure deux fois plus sur lui", cible_obj=["pièce"], cond=["porteur"]),
"forced-mutation": EP("Mutation forcée", NQ, 3, ["difformité", "mutation"], 4, "4 retiré à l'endurance et à la prestance, et une infirmité au choix", cible_note=["corps", "endurance", "prestance"], cond=["VIVANT"]),
"grasping-vine": EP("Liane préhensile", TR, 1, ["liane", "préhension", "contact"], why="une liane qui saisit, porte, crochète et transmet mes sorts de contact", impact_sats=[(6, ["mètres"])]),
"hardening": EP("Durcissement", INT, 4, ["solidité", "permanent"], 5, "5 ajouté à la dureté de la matière", cible_obj=["matière"]),
"imbue-with-addiction": EP("Dépendance instillée", NQ, 3, ["dépendance", "drogue"], why="dépendante sur-le-champ de la drogue employée", cond=["VIVANT"], comp=["drogue"]),
"imbue-with-flight": EP("Objet volant", V("mouvement"), 4, ["vol", "mètres"], 12, "vole à 12 m par instant, à ma guise", cible_obj=["objet"]),
"impart-mind": EP("Esprit prêté", INT, 4, ["conscience", "esprit", "part"], why="un objet magique reçoit une part de mon esprit et s'éveille", cible_obj=["objet"]),
"improve-trap": EP("Piège amélioré", INT, 4, ["amélioration"], why="un piège mieux caché, plus dur à désarmer, ou plus sûr", cible_obj=["piège"]),
"ironskin": EP("Peau de fer", INT, 1, ["fer", "parade"], 4, "4 ajouté à la défense de la peau ; rompre le sort réduit un coup décisif à un coup ordinaire", cible_note=["peau", "garde"], sens=[("vue", None)], manif=["fer"]),
"jatembes-ire": EP("Ire du vieux mage", TR, P, ["liane", "étreinte", "ruine"], 27, "4d6 + 13 en moyenne : les herbes deviennent des lianes colossales qui broient bâtisses et êtres hostiles", cond=["plante"], sens=[("vue", None)], manif=["lianes"]),
"jolt": EP("Décharge", NE, 3, ["foudre"], 2, "1d3 en moyenne", sens=[("vue", None)], manif=["étincelle"]),
"kalistocrats-nightmare": EP("Cauchemar du marchand", NQ, 3, ["monnaie", "cuivre", "malédiction"], why="toute pièce qu'elle touche se change en cuivre"),
"keyhole": EP("Trou de serrure", TR, 4, ["serrure", "regard"], why="une serrure paraît, ou double de taille : on voit au travers, on peut crocheter", cible_obj=["porte"]),
"legendary-proportions": EP("Proportions légendaires", INT, 2, ["géant"], 6, "6 ajouté à la force et à la défense de la peau, 4 à l'endurance ; les coups ordinaires l'entament à peine", cible_note=["force", "endurance", "peau"],
    impact_sats=[(2, ["stature", "fois"])]),
"lightfingers": EP("Doigts légers", V("force"), 3, ["chute", "objet", "larcin"], why="une poussée subtile lui fait lâcher un petit objet sans qu'elle le sente", discret=True),
"mages-crawl-space": EP("Niche du mage", ID, 1, ["pierre", "refuge", "poche"], why="fondu dans la roche, dans une poche d'air à ma taille"),
"magic-boulder": EP("Rocher magique", INT, 1, ["rocher"], 1, "des rochers plus lourds et plus sûrs à lancer", cible_obj=["pierre"], impact_sats=[(3, ["nombre"])]),
"magic-siege-engine": EP("Engin de siège magique", INT, 1, [], 1, "+1", cible_obj=["engin"],
    options=[O("Engin de siège magique"), O("Engin de siège magique supérieur", src_idx="magic-siege-engine-greater", impact=(1, [], "+1 par quatre niveaux"))]),
"mark-of-the-reptile-god": EP("Marque du dieu reptile", NQ, 3, ["marque", "écaille"], 4, "1d6 en moyenne ; la peau devient écailleuse autour de la marque", fam="A", impact_add=["acide"], cible_note=["peau"],
    impact_sats=[(2, ["vulnérabilité"])], sens=[("vue", None)], manif=["empreinte", "lueur"],
    impact_plus=[(2, ["prestance", "jour", "lézard"], "1d4 en moyenne retiré à la prestance chaque jour ; à zéro, elle devient un petit lézard")]),
"metabolic-molting": EP("Mue métabolique", HE, 2, ["mue", "stase", "régénération"], why="sept jours dans une coque de gemme : tout se répare, jusqu'aux membres perdus", cible_note=["corps"], comp=["gemme"],
    impact_plus=[(P, ["vie", "retour"], "avec une gemme de grand prix : ramène un mort de moins d'une heure")]),
"pattern-recognition": EP("Reconnaissance des motifs", VIS, 1, ["motif", "anomalie", "piste"], 2, "2 ajouté pour fouiller et pister", cible_note=["œil"]),
"pesh-vigor": EP("Vigueur fébrile", INT, 2, ["vigueur", "surcroît", "fatigue"], 2, "2 ajouté à la force ; 2 de plus à volonté, au prix de la douleur", cible_note=["force"], cond=["VIVANT"], impact_sats=[(4, ["douleur"])]),
"prehensile-pilfer": EP("Queue chapardeuse", INT, 2, ["larcin", "ruse"], why="la queue agit d'elle-même : elle vole ou joue un mauvais tour", cible_note=["queue"]),
"qlippoth-appearance": EP("Le visage sous le visage", TR, 1, ["effroi", "étrangeté"], 4, "4 ajouté à la peur que j'inspire, 4 retiré à l'amabilité", cible_note=["visage", "corps"],
    impact_plus=[(P, ["visage", "horreur", "paralysie", "nausée", "douleur"], "je peux dévoiler l'autre visage : un être vivant en perd de sa lucidité, se fige, est pris de nausée ou souffre")]),
"quick-throwing": EP("Lancer vif", INT, 2, ["lancer", "rapidité"], why="tire et lance ses armes de jet sans perdre un instant", qty_cible=P),
"repugnant-taste": EP("Goût répugnant", TR, 2, ["goût", "nausée"], why="une sueur infecte : qui la mord ou l'avale est pris de nausée", cible_note=["peau"], cond=["morsure"]),
"root": EP("Enracinement", ORD, 2, ["ancrage", "équilibre"], 2, "2 ajouté pour n'être ni déplacé ni renversé"),
"scale-spikes": EP("Écailles hérissées", TR, 2, ["pointe", "écaille"], 1, "des pointes d'armure +1", cible_note=["peau"], cond=["VIVANT"],
    options=[O("Écailles hérissées"), O("Écailles hérissées supérieures", src_idx="scale-spikes-greater", impact=(1, ["pointe", "écaille"], "+1 par quatre niveaux"))]),
"scribes-binding": EP("Reliure du scribe", V("mouvement", True), 3, ["livre", "stase", "savoir"], why="liée dans un livre qui la garde hors du temps et se remplit de sa vie et de son savoir", comp=["livre"]),
"shield-of-wings": EP("Bouclier d'ailes", TR, 1, ["vol", "mètres", "aile"], 15, "cinq ailes ardentes : vol à 15 m par instant", fam="A",
    impact_plus=[(30, ["résistance", "feu"], "une aile se consume pour retrancher 30 au feu reçu")], sens=[("vue", None)], manif=["ailes", "flamme"]),
"slough": EP("Dépouillement", NQ, 3, ["écorchement"], 2, "1d4 en moyenne retiré à l'endurance à chaque instant, jusqu'à ce que la peau tombe", cible_note=["peau", "endurance"], cond=["VIVANT"]),
"spirit-share": EP("Partage de breuvage", V("mouvement"), 2, ["breuvage", "contact"], why="un breuvage que je porte passe dans l'allié que je touche"),
"steal-book": EP("Vol de livre", V("mouvement"), 4, ["copie", "effacement"], why="le texte passe dans un livre vierge et s'efface de l'original", cible_obj=["livre"], discret=True),
"steal-size": EP("Vol de stature", V("flux"), 3, ["transfert"], why="elle rapetisse d'un cran, je grandis d'autant", cond=["humanoïde"], impact_sats=[(2, ["stature", "fois"])]),
"steal-years": EP("Vol d'années", V("flux"), 3, ["jeunesse", "ans"], 5, "2d4 ans en moyenne : elle vieillit, je rajeunis", cible_note=["âge"],
    options=[O("Vol d'années"), O("Vol d'années supérieur", src_idx="steal-years-greater", impact=(14, ["jeunesse", "ans"], "4d6 ans en moyenne"))]),
"strip-scales": EP("Écailles arrachées", NINT, 3, ["écaille"], 2, "2 retiré à la défense naturelle de sa peau", cible_note=["peau", "garde"], cond=["VIVANT"]),
"strong-wings": EP("Ailes puissantes", INT, 2, ["vol", "mètres", "aile"], 3, "3 m de vol de plus par instant, et plus d'aisance"),
"suspend-drowning": EP("Noyade suspendue", ORD, 2, ["noyade", "répit"], why="cesse de se noyer et respire un instant", cible_note=["souffle"]),
"tears-to-wine": EP("Des larmes au vin", TR, 4, ["vin", "clarté"], 2, "tout liquide devient vin ou hydromel ; qui en boit gagne 2 en raison et en lucidité", cible_obj=["eau"]),
"thorn-snare": EP("Collet d'épines", TR, 1, ["entrave", "collet", "épine"], 1, "1 par instant, 1d6 à qui se débat", cible_obj=["corde"], cond=["passage"]),
"thunderous-footfalls": EP("Pas de tonnerre", TR, 2, ["séisme", "renversement", "lenteur"], why="ses pas ébranlent le sol et renversent les plus petits ; elle va moitié moins vite"),
"titanic-anchoring": EP("Ancrage titanesque", ORD, 1, ["ancrage", "immobilité"], why="rien de ma taille ne peut me pousser, me tirer, me saisir ni me renverser"),
"transmute-wine-to-blood": EP("Du vin au sang", TR, 4, ["sang"], why="une bouteille de vin fin devient un demi-litre de sang de bête", cible_obj=["vin"]),
"transplant-visage": EP("Greffe de visage", ID, 1, ["greffe", "apparence", "permanent"], why="le visage d'un mort fondu au mien, sans trace de magie", cible_note=["visage"], cond=["cadavre"]),
"unhallowed-blows": EP("Coups impies", INT, 2, [], 1, "+1 à ses coups naturels", cible_note=["frappe"], cond=["MORTVIVANT"],
    options=[O("Coups impies"), O("Coups impies supérieurs", src_idx="unhallowed-blows-greater", impact=(1, [], "+1 par quatre niveaux"))]),
"venomous-promise": EP("Promesse venimeuse", REL, 3, ["secret", "serment", "poison"], why="si elle révèle ce que je lui confie, le poison la frappe", cond=["secret"], comp=["poison"]),
"vile-dog-transformation": EP("Métamorphose du chien vil", TR, 2, ["monstre"], why="un chien changé en molosse monstrueux", cible_note=["molosse"], fam="A",
    impact_plus=[(4, ["croc", "acide"], "1d6 en moyenne d'acide à chaque morsure"), (5, ["souffle", "acide"], "un souffle d'acide en cône de 3 m, 2d4 en moyenne")]),
"visualization-of-the-body": EP("Visualisation du corps", INT, 1, ["visualisation"], 5, "5 ajouté à ce qui relève de la faculté choisie ; le reste du sort peut se dépenser d'un coup", cible_note=["force", "adresse", "endurance"]),
"visualization-of-the-mind": EP("Visualisation de l'esprit", INT, 1, ["visualisation"], 5, "5 ajouté à ce qui relève de la faculté choisie ; le reste du sort peut se dépenser d'un coup", cible_note=["raison", "lucidité", "prestance"]),
}
FICHES.update(SUITE5)

# ----- Suite : les composantes de prix (focalisateur ou matière) s'inscrivent dans le cercle Composante -----
for _k, _c in {"bloodstone-mirror": ["sanguine"], "echeans-excellent-enclosure": ["verre"], "sympathetic-wounds": ["ambre"], "teleport-trap": ["aimant"],
    "fortunes-path": ["encens", "miroir"], "prognostication": ["encens"], "true-prognostication": ["encens"], "reveal-true-shape": ["herbes"],
    "damnation-of-memory": ["gemme"], "canopic-conversion": ["canopes"], "create-soul-gem": ["lentille"], "infuse-decay": ["outils"],
    "plundered-power": ["rubis"], "recorporeal-incarnation": ["gemme"], "sacramental-seal": ["objet"], "sentry-skull": ["onyx"],
    "shared-suffering": ["dague"], "spectral-saluqi": ["statuette"], "false-resurrection": ["diamant"], "maze-of-madness-and-suffering": ["boîte"],
    "reincarnate-spy": ["huile"], "summon-genie-lesser": ["lampe"], "curse-of-night": ["jais"], "awaken-construct": ["herbes", "huile"],
    "break-greater": ["diapason"], "claim-identity-greater": ["aiguille"], "curse-of-fell-seasons": ["sculpture"], "cyclic-reincarnation": ["huile"],
    "fools-gold-aa": ["or"], "impart-mind": ["diamant"], "legendary-proportions": ["os", "ambre"], "pesh-vigor": ["drogue"],
    "visualization-of-the-body": ["encens"], "visualization-of-the-mind": ["encens"]}.items():
    FICHES[_k]["comp"] = _c
# une composante matérielle se consume ; un focalisateur accompagne le sort
for _k in ("bloodstone-mirror", "echeans-excellent-enclosure", "sympathetic-wounds", "teleport-trap", "fortunes-path", "prognostication", "true-prognostication",
           "reveal-true-shape", "plundered-power", "sentry-skull", "false-resurrection", "maze-of-madness-and-suffering", "reincarnate-spy", "awaken-construct",
           "break-greater", "claim-identity-greater", "cyclic-reincarnation", "impart-mind", "legendary-proportions", "pesh-vigor",
           "visualization-of-the-body", "visualization-of-the-mind", "beanstalk", "imbue-with-addiction", "venomous-promise"):
    FICHES[_k]["consumed"] = True

# ===== Tri du 14 novembre : canon strict, puissance, intérêt (décisions de Baptiste) =====
_T_PEU = "propre à un peuple ou à une sorte de créature : à reprendre avec les sorts peuple par peuple"
_T_REG = "repose sur les « malédictions régionales », sous-système de règles propre à Pathfinder"
_T_DRO = "tri du 14 novembre : les drogues n'entrent pas dans la bibliothèque"
_T_SIE = "tri du 14 novembre : les engins de siège n'entrent pas dans la bibliothèque"
_TRI = {
 "probe-history": "puise dans une réalité parallèle, absente de la cosmologie d'Inarama",
 "vomit-twin": "le double est une vase, absente d'Inarama",
 "blightburn-weapon": "repose sur une substance propre à Golarion",
 "pesh-vigor": "repose sur le pesh, drogue propre à Golarion",
 "hasten-judgement": "suppose un jugement des âmes après la mort, propre à la cosmologie de Golarion",
 "malediction": "envoie l'âme aux Enfers, propres à la cosmologie de Golarion",
 "mark-of-the-reptile-god": "suppose un dieu et un peuple reptiliens, non établis dans Inarama",
 "transmute-wine-to-blood": "ne sert qu'aux buveurs de sang, non établis dans Inarama",
 "curse-of-night": _T_REG, "curse-of-fell-seasons": _T_REG,
 "sense-madness": "repose sur les règles de folie et de santé mentale, sous-système propre à Pathfinder",
 "maze-of-madness-and-suffering": "repose en partie sur les règles de folie, sous-système propre à Pathfinder",
 "tomb-legion": "fait surgir des momies, non établies ; sans elles, double la création de morts-vivants",
 "canopic-conversion": "repose sur la momie et ses vases canopes, non établis dans Inarama",
 "sacramental-seal": "suppose les symboles d'un culte, non établis dans Inarama",
 "rift-of-ruin": "ouvre une faille vers les Abysses et en tire leurs habitants : cosmologie de Golarion",
 "hellfire-ray": "feu des Enfers et damnation de l'âme : cosmologie de Golarion",
 "ghoul-hunger": "tri du 14 novembre : lié à la goule, créature non établie",
 "barghest-feast": "tri du 14 novembre : lié au barghest, créature non établie",
 "enlarge-tail": _T_PEU, "prehensile-pilfer": _T_PEU, "scale-spikes": _T_PEU, "scale-spikes-greater": _T_PEU, "strip-scales": _T_PEU, "strong-wings": _T_PEU,
 "batrachian-surge": _T_PEU, "endothermic-touch": _T_PEU, "magic-boulder": _T_PEU,
 "deivons-parry": "copie un pouvoir de classe : pure mécanique de jeu",
 "blade-tutors-spirit": "compense des malus de manœuvres : pure mécanique de jeu",
 "hermean-potential": "fait lancer deux fois le dé : pure mécanique de jeu",
 "bit-of-luck": "réserve de points à ajouter aux jets : pure mécanique de jeu",
 "cowards-cowl": "repose sur les actions préparées et les attaques d'opportunité : pure mécanique de jeu",
 "arcane-reinforcement": "ajoute une compétence à une autre : pure mécanique de jeu",
 "quick-throwing": "remplace un don : pure mécanique de jeu",
 "righteous-condemnation": "tout l'effet tient à l'alignement en trois composantes, sans équivalent dans Inarama",
 "chastise": "simple bonus à trois compétences : pure mécanique de jeu",
 "blood-money": "puissance : crée sans frais des composantes coûteuses",
 "amnesia": "puissance : efface pour de bon tous les talents acquis, dès le niveau 3",
 "sympathetic-wounds": "puissance : reporte la moitié des blessures du lanceur sur autrui pendant des heures, dès le niveau 2",
 "constricting-coils": "puissance : Immobilisation de monstre avec des blessures en plus, au même niveau",
 "suffocation-instant": "double Mise à mort, et lié au pesh de Golarion",
 "suffocation-slow": "double Suffocation, et lié au pesh de Golarion",
 "create-drug": _T_DRO, "alleviate-addiction": _T_DRO, "contact-high": _T_DRO, "imbue-with-addiction": _T_DRO,
 "magic-siege-engine": _T_SIE, "magic-siege-engine-greater": _T_SIE, "energy-siege-shot": _T_SIE, "energy-siege-shot-greater": _T_SIE,
}
for _k in _TRI: FICHES.pop(_k, None)
PF1_RELECTURE.update(_TRI)

# Les deux faces du plan astral ne vont jamais l'une sans l'autre : chaque sort du lot lié à une face reçoit sa forme réciproque.
def _F(k, **kw): FICHES[k].update(kw)
_F("armor-of-darkness", fr="Armure astrale", options=[
    O("Forme ténébreuse"),
    O("Forme lumineuse", impact=(3, ["armure", "clarté"], "3 ajouté à la défense"), impact_sats=[(2, ["si:ténébreux"])], manif=["clarté", "voile"])])
_F("righteous-blood", options=[
    O("Forme lumineuse"), O("Forme lumineuse — porteur voué à sa face", impact=(7, ["lumineux"], "2d6 en moyenne à qui le blesse")),
    O("Forme ténébreuse", impact=(4, ["ténébreux"], "1d6 en moyenne à qui le blesse"), cond=["coup", "lumineux"]),
    O("Forme ténébreuse — porteur voué à sa face", impact=(7, ["ténébreux"], "2d6 en moyenne à qui le blesse"), cond=["coup", "lumineux"])])
_F("bolt-of-glory", options=[
    O("Forme lumineuse"),
    O("Forme ténébreuse", impact=(17, ["ténébreux"], "5d6 en moyenne aux êtres du monde et des éléments"), impact_sats=[(38, ["si:lumineux"])], manif=["rayon", "ténèbres"])])
_F("celestial-companion", fr="Compagnon gardé", options=[O("Forme lumineuse"), O("Forme ténébreuse", impact_add=["ténébreux"], manif=["aura", "ombre"])])
_F("abyssal-vermin", fr="Vermine astrale", options=[O("Forme ténébreuse"),
    O("Forme lumineuse", impact_add=["lumineux"], impact=(P, ["résistance", "châtiment"], "une vermine endurcie contre les coups, le froid, le feu et les sorts, qui châtie les êtres ténébreux"))])
_F("demon-dream", fr="Cauchemar astral", options=[O("Forme ténébreuse"), O("Forme lumineuse", impact_add=["lumineux"])])
_F("false-resurrection", options=[
    O("Forme ténébreuse"), O("Forme ténébreuse suprême", src_idx="false-resurrection-greater", impact=(P, ["résurrection", "leurre", "possession", "corps"], "même sans dépouille, et sans terme")),
    O("Forme lumineuse", cible_sym=["lumineux"], impact=(P, ["résurrection", "leurre", "possession"], "le corps revit, mais c'est un être de la face lumineuse qui l'habite")),
    O("Forme lumineuse suprême", src_idx="false-resurrection-greater", cible_sym=["lumineux"], impact=(P, ["résurrection", "leurre", "possession", "corps"], "même sans dépouille, et sans terme"))])
_F("wall-of-light", fr="Mur astral", options=[
    O("Forme lumineuse"),
    O("Forme ténébreuse", impact=(P, ["mur", "ténèbres"], "un rideau de ténèbres qui arrête le regard et aveugle"), impact_add=["cécité", "ténébreux"], rayonnement=False,
      impact_sats=[(2, ["si:lumineux"])], manif=["mur", "ténèbres"])])
_F("shadow-enchantment", options=[
    O("Enchantement d'ombre — lumineux", impact=(P, ["ombre", "enchantement", "quasi-réel", "lumineux"], "un enchantement imité, à demi réel")),
    O("Enchantement d'ombre — ténébreux", impact=(P, ["ombre", "enchantement", "quasi-réel", "ténébreux"], "un enchantement imité, à demi réel")),
    O("Enchantement d'ombre supérieur — lumineux", src_idx="shadow-enchantment-greater", impact=(P, ["ombre", "enchantement", "quasi-réel", "lumineux"], "un enchantement imité, à demi réel"), impact_sats=[(5, ["niveau"])]),
    O("Enchantement d'ombre supérieur — ténébreux", src_idx="shadow-enchantment-greater", impact=(P, ["ombre", "enchantement", "quasi-réel", "ténébreux"], "un enchantement imité, à demi réel"), impact_sats=[(5, ["niveau"])])])
_F("shadow-dragon-aspect", options=[
    O("Forme lumineuse", impact=(10, ["dragon", "griffe", "quasi-réel", "lumineux"], "des griffes d'ombre, 1d6 + 7 en moyenne")),
    O("Forme ténébreuse", impact=(10, ["dragon", "griffe", "quasi-réel", "ténébreux"], "des griffes d'ombre, 1d6 + 7 en moyenne"))])
_F("teratoid-caress", options=[O("Forme ténébreuse"), O("Forme lumineuse", impact_add=["lumineux"])])

# ===================== Pathfinder 2 (édition d'origine et version remaniée) =====================
# Tri validé le 14 novembre : canon strict, sorts sans dieu gardés en Arcane, niveau = rang sauf écart signalé (« niveau »),
# rang 10 sans équivalent = niveau 10. « vr » : la version remaniée du même sort donne une forme de plus si son glyphe diffère.
P2 = lambda fr, verb, cible, words, v=None, why="", **kw: {**dict(src="pf2", fr=fr, verb=verb, cible=cible, impact=(P if v is None else v, list(words), why)), **kw}
PF2_ECARTE = {}        # sorts de Pathfinder 2 écartés, avec leur motif

# ----- Pathfinder 2, lot 1 : Abjuration -----
PF2_ECARTE.update({
 "protect-companion": "n'agit que sur l'eidolon ou le serviteur : mécanique de classe", "wash-your-luck": "n'efface que des effets de « fortune » : mécanique de jeu",
 "brand-the-impenitent": "marque visible des seuls fidèles d'un culte", "spiritual-attunement": "s'accorde à un plan de la « Sphère extérieure » et à son alignement",
 "tomorrows-dawn": "vise une lignée de fiélons propre à Golarion"})
_ELEM6 = [("Feu", "feu"), ("Air", "air"), ("Terre", "terre"), ("Eau", "eau"), ("Métal", "acier"), ("Bois", "bois")]
PF2_ABJ = {
"breadcrumbs": P2("Traînée de repères", VIS, 2, ["traînée", "passage"], why="une traînée brillante marque partout où elle est passée", sens=[("vue", None)], manif=["traînée", "scintillement"]),
"forbidding-ward": P2("Garde contre l'ennemi", SEP, 2, ["ennemi", "désigné"], 1, "1 ajouté à sa défense et à sa résistance contre un ennemi précis", cible_note=["garde", "résistance"], vr={}),
"shattering-gem": P2("Gemme brisante", SEP, 2, ["gemme", "absorption"], 5, "une gemme flottante encaisse 5 points, une fois sur deux", cible_note=["garde"],
    impact_plus=[(4, ["éclat", "tranchant"], "brisée, elle blesse de 1d8 en moyenne celui qui l'a brisée")], sens=[("vue", None)], manif=["gemme"]),
"tether": P2("Attache", V("mouvement", True), 3, ["lien", "entrave"], why="liée à moi : ralentie, elle ne peut s'éloigner", impact_sats=[(9, ["mètres"])], sens=[("vue", None)], manif=["chaînes"]),
"thermal-stasis": P2("Stase thermique", SEP, 2, ["feu"], 2, "2 retranché au feu reçu", fam="A", cible_note=["résistance"], impact_plus=[(2, ["froid"], "2 retranché au froid reçu")]),
"erase-trail": P2("Piste effacée", NVIS, P, ["trace", "effacement"], 4, "les traces d'un être précis presque introuvables (4)", discret=True),
"extract-poison": P2("Extraction de poison", V("flux"), 4, ["retrait", "arme", "enduit"], 4, "le poison retiré d'un objet passe sur mon arme : 1d6 en moyenne par degré du poison", fam="A", cible_obj=["poison"]),
"lock-item": P2("Objet soudé", V("mouvement", True), 3, ["objet", "soudure"], why="ce qu'elle tient reste collé à sa main", cible_note=["membre"], dur=(24, "SECONDES")),
"magnetic-repulsion": P2("Répulsion magnétique", V("force", True), 1, ["acier", "répulsion"], 1, "1 retranché aux coups portés avec du métal ; qui porte du métal peine à m'approcher", cible_note=["garde"]),
"elemental-absorption": P2("Absorption élémentaire", V("flux"), 1, ["absorption"], 5, "5 retranché à ce que l'élément choisi m'inflige", cible_note=["résistance"],
    impact_plus=[(30, ["décharge"], "je rends d'un coup ce que j'ai absorbé, 30 au plus"), (18, ["portée", "mètres"], "à un ennemi à 18 m")],
    options=[O(n, impact=(5, ["absorption", w], f"5 retranché à ce que {'le ' if n not in ('Air', 'Eau') else 'l’'}{n.lower()} m'inflige")) for n, w in _ELEM6]),
"safe-passage": P2("Passage sûr", SEP, P, ["danger", "terrain"], 5, "5 retranché aux dangers du lieu, 2 ajouté à la défense contre eux ; rien ne s'effondre", cible_note=["garde", "résistance"], vr={}),
"sanctified-ground": P2("Sol consacré", SEP, P, ["consécration"], 1, "1 ajouté à tout ce qu'on fait contre la sorte d'êtres choisie", comp=["eau", "bénite"], consumed=True, options=[
    O("Contre les aberrations", cond=["aberration"]), O("Contre les dragons", cond=["dragon"]), O("Contre les morts-vivants", cond=["MORTVIVANT"]),
    O("Contre les êtres de la face lumineuse", cond=["lumineux"]), O("Contre les êtres de la face ténébreuse", cond=["ténébreux"])]),
"vector-screen": P2("Écran aux projectiles", SEP, P, ["projectile", "capture"], why="un écran de force happe flèches, carreaux et pierres de fronde", cible_note=["trait"]),
"warding-aggression": P2("Garde agressive", SEP, 1, ["ennemi", "frappé"], 2, "2 ajouté à ma défense contre l'ennemi que je frappe, tant que je le frappe", cible_note=["garde"], cond=["coup"]),
"whirling-scarves": P2("Écharpes tourbillonnantes", NVIS, 1, ["écharpes", "force", "accroc"], why="un tourbillon d'écharpes me dérobe aux coups et accroche les armes", sens=[("vue", None)], manif=["écharpes", "couleurs"]),
"chromatic-armor": P2("Armure chromatique", SEP, 2, ["couleur", "résistance"], 5, "5 retranché à l'énergie de chacune des deux couleurs tirées", cible_note=["garde", "résistance"], qty=2, qty_note=["couleur"],
    impact_add=["éblouissement"], sens=[("vue", None)], manif=["armure", "lumière", "couleurs"],
    options=[O("Armure chromatique"), O("Armure prismatique", src_idx="prismatic-armor", qty=7, impact=(5, ["couleur", "résistance", "toutes"], "5 retranché aux sept énergies à la fois"), impact_add=["cécité"])]),
"rebounding-barrier": P2("Barrière à rebond", V("force", True), 1, ["barrière"], 10, "10 retranché au coup reçu", cible_note=["garde"], cond=["coup"], impact_sats=[(5, ["renvoi"])]),
"reflective-scales": P2("Écailles réfléchissantes", V("flux"), 1, ["écaille", "absorption"], 5, "5 retranché à l'énergie choisie", cible_note=["résistance"],
    impact_plus=[(35, ["éclat", "décharge"], "les écailles éclatent à 6 m : 1d6 par 10 points absorbés, 10d6 au plus")], sens=[("vue", None)], manif=["écailles", "lueur"],
    options=[O(n, impact=(5, ["écaille", "absorption", w], f"5 retranché : {n.lower()}")) for n, w in (("Acide", "acide"), ("Froid", "froid"), ("Feu", "feu"), ("Foudre", "foudre"), ("Poison", "poison"))]),
"soft-landing": P2("Atterrissage en douceur", ORD, P, ["chute", "douceur"], why="tout ce qui tombe dans la zone s'y pose sans mal, de n'importe quelle hauteur"),
"bandits-doom": P2("Perte du voleur", SEP, 4, ["psyché", "condamnation"], 36, "8d8 en moyenne à l'esprit de qui s'empare de l'objet, et la mort plus proche", cible_obj=["objet"], cond=["larcin"], dur=("plein", None)),
"blessing-of-defiance": P2("Bénédiction de défi", INT, 2, ["défi"], 4, "4 ajouté un instant contre un type de danger", cible_note=["résistance"], options=[
    O("Le corps", impact_plus=[(15, ["poison"], "15 retranché au poison")]),
    O("L'esquive", impact_plus=[(5, ["vitesse", "mètres"], "4,5 m de plus par instant, arrondi à 5")]),
    O("L'esprit", impact_plus=[(15, ["psyché", "garde"], "15 retranché aux atteintes de l'esprit")]),
    O("Tout le groupe", qty_cible=P)]),
"chromatic-wall": P2("Mur chromatique", EXI, P, ["mur", "couleur"], why="un mur opaque d'une seule couleur, tirée au hasard", fam="A", sens=[("vue", None)], manif=["mur", "lumière"],
    forme=[("FORME", 2, [], "plan : un mur droit et vertical", [(90, 1)]), ("AMPLEUR", 162, ["SURFACE", "METRES"], "162 m² : 18 m sur 9")], options=[
    O("Rouge", impact=(20, ["mur", "feu"], "détruit flèches et carreaux ; 20 de feu à qui le traverse")),
    O("Orange", impact=(25, ["mur", "acide"], "détruit les armes de jet ; 25 d'acide à qui le traverse")),
    O("Jaune", impact=(30, ["mur", "foudre"], "arrête les énergies ; 30 de foudre à qui le traverse")),
    O("Vert", impact=(10, ["mur", "poison", "faiblesse"], "arrête poisons, gaz et souffles ; 10 de poison et la faiblesse à qui le traverse"))]),
"spiritual-guardian": P2("Gardien spirituel", EXI, 7, ["force", "frappe"], 12, "un gardien de force frappe (2d8 + 3 en moyenne) ou garde", cible_note=["serviteur"], vr={},
    impact_plus=[(10, ["garde", "allié"], "il prend sur lui les 10 premiers points de chaque coup porté à l'allié gardé, 50 en tout")], sens=[("vue", None)], manif=["gardien", "translucide"]),
"temporary-glyph": P2("Glyphe éphémère", ORD, P, ["piège", "sort", "éphémère"], why="un sort hostile enfermé dans un glyphe, pour une minute", cond=["PASSAGE"], impact_sats=[(None, ["sort"])], sens=[("vue", None)], manif=["glyphe"]),
"scintillating-safeguard": P2("Sauvegarde scintillante", SEP, 2, ["barrière", "étincelles"], 10, "10 retranché à l'effet qui allait les frapper", cible_note=["résistance"], cond=["danger"], qty_cible=5, sans_parole=True, vr={},
    sens=[("vue", None)], manif=["étincelles"]),
"spellwrack": P2("Sorts en perdition", NQ, 3, ["malédiction", "déperdition"], 13, "2d12 en moyenne chaque fois qu'un sort durable la touche ; ses sorts s'écourtent", cond=["sort"], vr={}),
"temporal-ward": P2("Garde temporelle", V("mouvement"), 4, ["temps", "recul", "piège"], why="qui veut ouvrir est renvoyé un instant en arrière, à sa place d'avant", cible_obj=["porte"], cond=["INTRUS"]),
"energy-aegis": P2("Égide contre les énergies", SEP, 2, ["énergie", "toutes"], 5, "5 retranché à l'acide, au froid, à la foudre, au feu, à la force, au son et aux deux énergies astrales", cible_note=["résistance"], vr={}),
"return-to-essence": P2("Retour à l'essence", SEP, "trame", ["sceau", "reprise", "énergie"], why="le sort qui scelle une porte ou un coffre défait, son énergie rendue au lanceur", cible_note=["sort"]),
"unfettered-pack": P2("Meute sans entraves", SEP, 2, ["terrain", "entrave", "liberté"], why="le groupe ignore broussailles, gravats, vents et terrain difficile", qty_cible=10, vr={}),
"prismatic-shield": P2("Bouclier prismatique", SEP, 1, ["éclat", "prisme", "riposte"], why="des éclats de lumière arrêtent les traits, frappent l'assaillant d'un effet prismatique et font échouer les sorts", cible_note=["garde"],
    sans_parole=False, sens=[("vue", None)], manif=["éclats", "couleurs"]),
"indestructibility": P2("Indestructibilité", V("nature", True), 1, ["invulnérabilité"], why="rien ne peut m'atteindre si je ne le veux pas", vr={}),
"nullify": P2("Annulation", DISP, "trame", ["annulation"], why="le sort qui me vise est détruit à coup sûr", cible_note=["sort"], niveau=9, impact_sats=[(4, ["blessure", "niveau"])]),
"ravenous-portal": P2("Porte vorace", TR, 4, ["mimique", "garde", "morsure"], why="la porte qu'on force devient une mimique qui attaque", cible_obj=["porte"], cond=["INTRUS"]),
"astral-labyrinth": P2("Labyrinthe astral", SEP, P, ["dédale", "téléportation", "psyché", "détournement"], why="la magie de l'esprit s'y défait ; qui s'y téléporte est étourdi et dévié vers le point choisi", impact_add=["étourdissement"], options=[
    O("Forme lumineuse", impact=(P, ["dédale", "téléportation", "psyché", "détournement", "lumineux"], "tissé de l'énergie de la face lumineuse")),
    O("Forme ténébreuse", impact=(P, ["dédale", "téléportation", "psyché", "détournement", "ténébreux"], "tissé de l'énergie de la face ténébreuse"))]),
}
FICHES.update(PF2_ABJ)

# ----- Pathfinder 2, lot 2 : Invocation -----
PF2_ECARTE.update({
 "summon-anarch": "défini par l'alignement chaotique", "summon-axiom": "défini par l'alignement loyal", "summon-lesser-servitor": "habitant de la « Sphère extérieure »",
 "summon-ancient-fleshforged": "créature de l'histoire de Golarion", "summon-irii": "entité propre à Pathfinder", "frosts-touch": "lié à un objet unique d'une campagne",
 "summon-kaiju": "le kaiju n'existe pas dans Inarama", "summon-deific-herald": "n'existe que par une divinité", "sign-of-conviction": "n'existe que par le symbole d'une divinité"})
TP2 = V("mouvement"); INV = V("trame")
_MUR = lambda l, h: [("FORME", 2, [], "plan : un mur droit et vertical", [(90, 1)]), ("AMPLEUR", l * h, ["SURFACE", "METRES"], f"{l * h} m² : {l} m sur {h}")]
_CONV = lambda fr, quoi, v, why: P2(fr, INV, 9, [], v[0], why, cible_note=[quoi], vr={}, **({"impact": (v[0], ["fractionné"], why)} if len(v) > 1 else {}))
PF2_INV = {
"tanglefoot": P2("Liane poisseuse", V("mouvement", True), 3, ["liane", "entrave", "mètres"], 3, "ralentie de 3 m par instant, parfois clouée sur place", vr={"src_idx": "tangle-vine"}, sens=[("vue", None)], manif=["liane"]),
"distortion-lens": P2("Lentille de distorsion", TR, P, ["lentille", "portée", "mètres"], 3, "les tirs alliés qui la traversent portent 3 m plus loin, les tirs ennemis 3 m moins loin"),
"ghostly-shift": P2("Déphasage spectral", SEP, 2, ["déphasage"], 2, "le corps à demi déphasé : 2 retranché à tout ce qui le blesse, hormis la force", cible_note=["corps", "résistance"]),
"tesseract-tunnel": P2("Tunnel du tesseract", TP2, 1, ["tunnel", "espace", "passage"], why="deux portails aux deux bouts de ma course : qui entre dans l'un sort par l'autre"),
"warp-step": P2("Pas plié", INT, 1, ["foulée", "vitesse", "mètres"], 2, "le sol se plie sous mes pas : 1,5 m de plus par instant, arrondi à 2, et deux déplacements d'un coup"),
"animal-allies": P2("Alliés animaux", INV, P, ["harcèlement"], 8, "3d4 en moyenne à tous ceux qui m'entourent", cible_note=["bête"]),
"mud-pit": P2("Fosse de boue", EXI, P, ["boue", "enlisement"], why="une boue épaisse couvre le sol et freine la marche", vr={}),
"pet-cache": P2("Cache du compagnon", TP2, 2, ["poche", "abri", "plan"], why="mon compagnon abrité dans une poche hors du monde, avec de quoi vivre", cond=["compagnon"], vr={}),
"protector-tree": P2("Arbre protecteur", EXI, 2, ["arbre", "interposition"], 10, "un arbre surgit et prend sur lui les coups portés à l'allié voisin, 10 points en tout", cible_note=["garde"], vr={}, sens=[("vue", None)], manif=["arbre"]),
"temporary-tool": P2("Outil éphémère", EXI, 1, ["éphémère", "usage"], why="un outil simple, pour un seul usage ou une minute", cible_obj=["outil"]),
"thoughtful-gift": P2("Présent attentionné", TP2, 2, ["objet", "don", "téléportation"], why="un petit objet passe de ma main à la sienne", vr={}),
"verdant-sprout": P2("Pousse verdoyante", EXI, P, ["plante", "abri", "fruit"], why="en dix minutes, une plante robuste qui abrite et nourrit un être pour un jour", comp=["graine"], consumed=True, vr={}),
"ash-cloud": P2("Nuage de cendre", EXI, P, ["cendre", "fumée"], 5, "2d4 en moyenne à chaque instant ; la fumée gêne le vol et éteint l'odorat", impact_add=["éblouissement"], sens=[("vue", None), ("odorat", None)], manif=["cendre", "fumée"]),
"carrion-mire": P2("Bourbier de charogne", EXI, P, ["cadavre", "membres", "chute"], why="des membres de cadavres agrippent et font tomber",
    impact_plus=[(P, ["soin", "empêchement"], "les soins d'énergie de vie y sont défaits")], sens=[("vue", None)], manif=["membres", "cadavres"]),
"persistent-servant": P2("Serviteur persistant", EXI, 7, ["corvée", "répétition"], why="un serviteur invisible répète une corvée un jour durant", cible_note=["serviteur"]),
"sonata-span": P2("Pont de sonate", EXI, P, ["pont", "mélodie"], why="les notes d'un air deviennent un pont translucide, même au-dessus du vide", cond=["musique"], sens=[("vue", None), ("ouïe", None)], manif=["pont", "notes"]),
"bottomless-stomach": P2("Estomac sans fond", EXI, 2, ["poche", "rangement", "plan"], why="un espace de rangement hors du monde, qui s'ouvre par la bouche", cible_note=["gueule"]),
"magical-fetters": P2("Fers magiques", V("mouvement", True), 3, ["menottes", "maladresse", "mètres"], 3, "gauche, et ralentie de 3 m par instant", cible_note=["membres"], dur=(1, "MINUTES"), sens=[("vue", None)], manif=["menottes", "spectre"]),
"sea-of-thought": P2("Mer de pensée", EXI, P, ["pensée", "bourbier", "mètres"], 3, "une nappe de pensée figée : on y perd 3 m par instant, parfois l'équilibre", cible_note=["psyché"]),
"soothing-blossoms": P2("Fleurs apaisantes", EXI, P, ["fleur", "apaisement", "remède"], why="des fleurs aident à vaincre poisons et maladies et à faire cesser les maux qui durent", sens=[("vue", None), ("odorat", None)], manif=["fleurs"]),
"temporal-twin": P2("Jumeau temporel", V("identite", True), 2, ["double", "passé", "répétition"], why="un double tiré de l'instant d'avant refait le dernier geste de l'allié"),
"wall-of-water": P2("Mur d'eau", EXI, P, ["mur", "eau", "extinction"], why="une vague dressée en mur : elle éteint les feux et arrête les projectiles", fam="A", forme=_MUR(18, 3), sens=[("vue", None)], manif=["mur", "vague"]),
"coral-eruption": P2("Éruption de corail", EXI, P, ["corail", "lacération"], 21, "6d6 en moyenne", impact_plus=[(3, ["terrain", "lacération"], "3 à chaque pas fait ensuite dans le récif")], sens=[("vue", None)], manif=["corail"]),
"magic-mailbox": P2("Boîte aux lettres magique", TP2, 4, ["échange", "contenu"], why="ce qu'on laisse dix minutes dans l'un des deux contenants passe dans l'autre", cible_obj=["contenant"], qty_cible=2),
"murderous-vine": P2("Liane meurtrière", EXI, 3, ["liane", "étreinte", "épine"], 20, "3d6 + 2d8 en moyenne : saisie et broyée contre une paroi",
    impact_plus=[(7, ["écrasement"], "2d6 en moyenne à chaque instant tant qu'elle la tient")], sens=[("vue", None)], manif=["liane", "épines"]),
"petal-storm": P2("Tempête de pétales", EXI, P, ["pétale", "tranchant"], 11, "2d10 en moyenne à qui entre dans le nuage ou y reste", sens=[("vue", None)], manif=["pétales"]),
"wall-of-mirrors": P2("Mur de miroirs", EXI, P, ["mur", "miroir", "dissimulation"], why="un mur de verre réfléchissant cache chaque côté à l'autre", forme=_MUR(15, 6),
    impact_plus=[(10, ["psyché", "reflet"], "4d4 en moyenne à l'esprit de qui frappe le mur")], sens=[("vue", None)], manif=["mur", "miroirs"]),
"blink-charge": P2("Charge clignotante", TP2, 3, ["téléportation", "frappe", "élan"], 9, "je parais contre elle et frappe : 2d8 en moyenne de force en plus du coup"),
"flammable-fumes": P2("Vapeurs inflammables", EXI, P, ["gaz", "invisible"], 7, "2d6 en moyenne de poison à chaque instant", impact_add=["poison"], fam="A",
    impact_plus=[(35, ["feu", "détonation"], "10d6 en moyenne si une flamme y est portée")], sens=[("odorat", None)], manif=["âcreté"]),
"impaling-spike": P2("Pieu empaleur", EXI, 3, ["pieu", "fer", "empalement"], 28, "8d6 en moyenne ; empalée, elle reste clouée", impact_add=["entrave"], vr={}),
"pillars-of-sand": P2("Piliers de sable", EXI, P, ["pilier", "sable", "mètres"], 9, "des piliers de sable durci, 9 m de haut en tout"),
"return-beacon": P2("Balise de retour", TP2, 1, ["balise", "retour", "plan"], why="une balise invisible où revenir, même d'un autre plan"),
"collective-transposition": P2("Transposition collective", TP2, 4, ["téléportation", "replacement"], why="deux êtres déplacés où je veux dans la zone", qty_cible=2, vr={}),
"elemental-confluence": P2("Confluence élémentaire", INV, 9, ["confluence", "tempête"], why="quatre élémentaires fondus en une tempête ; deux agissent à chaque instant", cible_note=["élémentaire"], fam="A", options=[
    O("Air", impact=(10, ["confluence", "foudre"], "4d4 en moyenne de foudre à 6 m autour")),
    O("Terre", impact=(10, ["confluence", "terre", "rempart"], "la confluence durcit : 10 retranché aux coups")),
    O("Feu", impact=(4, ["confluence", "feu"], "1d6 en moyenne de feu persistant à ceux qui s'y trouvent")),
    O("Métal", impact=(7, ["confluence", "acier", "éclat"], "2d6 en moyenne d'éclats tranchants à ceux qui s'y trouvent")),
    O("Eau", impact=(14, ["confluence", "eau", "jet"], "4d6 en moyenne : un jet d'eau jusqu'à 18 m")),
    O("Bois", impact=(P, ["confluence", "bois", "racines"], "des racines encombrent le sol"))]),
"tangling-creepers": P2("Lianes enchevêtrantes", EXI, P, ["liane", "lenteur", "mètres"], 3, "des lianes partout : 3 m de moins par instant",
    impact_plus=[(P, ["fouet", "traction", "entrave"], "une liane peut happer un être à 4,5 m et le clouer")], vr={}, sens=[("vue", None)], manif=["lianes"]),
"unexpected-transposition": P2("Transposition imprévue", TP2, 4, ["échange", "place"], why="j'échange ma place avec un autre, qui prend le coup", cond=["coup"]),
"duplicate-foe": P2("Double de l'ennemi", V("identite", True), 3, ["double", "service"], why="un double de l'ennemi combat pour moi, sans ses pouvoirs", impact_sats=[(70, ["réserve"])], vr={}),
"maze-of-locked-doors": P2("Dédale de portes closes", V("trame", True), 3, ["couloir", "portes", "serrure"], why="bannie dans un couloir hors du monde, barré de portes verrouillées", impact_sats=[(9, ["intervalle", "mètres"])]),
"momentary-recovery": P2("Répit d'un instant", TP2, 1, ["téléportation", "répit", "instant"], why="je disparais, j'agis le temps d'un souffle hors du monde, et reparais ailleurs"),
"clone-companion": P2("Clone du compagnon", V("identite", True), 2, ["double", "mimétisme"], why="un double de mon compagnon, qui refait chacun de ses gestes", cond=["compagnon"]),
"summon-archmage": P2("Convocation d'un archimage", INV, 9, ["force"], 10, "à sa venue : 3d4 + 3 en moyenne à cinq ennemis", cible_note=["esprit"], qty=5,
    impact_plus=[(P, ["sort", "prolongation"], "les sorts bénéfiques ne s'écoulent plus près de lui"), (2, ["stupeur", "dissipation"], "à son départ : les ennemis stupéfiés, un de leurs sorts défait")]),
"summon-draconic-legion": P2("Convocation d'une légion draconique", INV, 9, ["souffle", "énergie"], 45, "à sa venue : deux souffles, 10d8 en moyenne chacun", cible_note=["dragon"], qty=2,
    impact_plus=[(40, ["griffe", "tourbillon"], "à son départ : 9d8 en moyenne à tous les ennemis proches")], sens=[("vue", None), ("ouïe", None)], manif=["dragons"]),
"upheaval": P2("Bouleversement", TR, P, ["séisme", "effondrement"], 38, "11d6 en moyenne sous ce qui s'effondre ; le sol devient chaos",
    impact_plus=[(18, ["pilier", "roche", "mètres"], "des piliers de roche jaillissent à 18 m de haut")]),
"remake": P2("Recréation", EXI, 1, ["recréation", "vestige"], why="un objet détruit recréé à l'identique à partir d'un de ses restes", cible_obj=["OBJET"], comp=["vestige"], consumed=True, niveau=9, vr={}),
"summon-construct": _CONV("Convocation d'artefact animé", "golem", (2, "f"), "puissance ½"),
"summon-fey": _CONV("Convocation de fée", "fée", (2, "f"), "puissance ½"),
"summon-plant-or-fungus": _CONV("Convocation de plante", "plante", (2, "f"), "puissance ½"),
"summon-elemental": _CONV("Convocation d'élémentaire", "élémentaire", (1,), "puissance 1"),
"summon-entity": _CONV("Convocation d'aberration", "aberration", (5,), "puissance 5"),
"summon-giant": _CONV("Convocation de géant", "géant", (5,), "puissance 5"),
}
FICHES.update(PF2_INV)

# ----- Pathfinder 2, lot 3 : Divination (première partie : tours de magie et rangs 1 à 3) -----
PF2_ECARTE.update({
 "focusing-hum": "ne modifie qu'un test de règles", "prophets-luck": "parie sur l'issue d'un jet : mécanique de jeu", "timely-tutor": "eidolon et mémoire akashique",
 "lucky-number": "ajuste les jets de dé à venir : pure mécanique de jeu", "bee-mans-summons": "pouvoir d'une figure propre à une campagne",
 "perseiss-precautions": "fait lancer deux fois le dé d'initiative : pure mécanique de jeu"})
PF2_DIV = {
"approximate": P2("Estimation", VIS, P, ["nombre", "estimation"], why="le nombre approché des objets d'une sorte, d'un coup d'œil"),
"read-aura": P2("Lecture de l'aura", VIS, 4, ["magie", "école"], why="dit si l'objet est magique, et de quelle école", cible_obj=["objet"], vr={}),
"read-the-air": P2("Lecture de l'assemblée", VIS, 1, ["usages", "assemblée", "impression"], 1, "les usages et les non-dits du lieu saisis ; 1 ajouté pour y faire bonne impression", cible_note=["psyché"]),
"foresee-the-path": P2("Chemin entrevu", VIS, 3, ["mouvement", "avenir", "ouverture"], why="son prochain mouvement deviné : un allié peut la frapper au passage"),
"glimpse-weakness": P2("Faille entrevue", VIS, 3, ["faille", "précision"], 2, "2 ajouté au premier coup qu'un allié lui porte", cible_note=["garde"]),
"join-pasts": P2("Passés joints", REL, 2, ["communion", "souvenir", "savoir"], why="deux esprits partagent pensées et vécu, sans mots, et s'entraident à se souvenir", cible_note=["psyché", "mémoire"], qty_cible=2),
"omnidirectional-scan": P2("Balayage en tous sens", VIS, P, ["angles", "fouille", "appui"], why="le lieu vu sous tous les angles ; un allié guidé contre un ennemi"),
"imprint-message": P2("Message imprimé", ORD, 4, ["message", "empreinte", "émotion"], why="un court message ou une émotion imprimés dans un objet, pour qui le sondera", cible_obj=["objet"], vr={}, discret=True),
"message-rune": P2("Rune à message", ORD, 4, ["rune", "message", "voix"], why="une rune garde un message de cinq minutes pour qui la touche", cible_obj=["surface"], cond=["contact"], impact_sats=[(5, ["minutes"])],
    sens=[("vue", None)], manif=["rune"]),
"nudge-the-odds": P2("Coup de pouce au hasard", INT, 1, ["chance", "jeu"], 1, "1 ajouté aux jeux de hasard ; un trait du visage devient doré", sens=[("vue", None)], manif=["doré"]),
"pocket-library": P2("Bibliothèque de poche", EXI, 1, ["savoir", "livre", "plan"], 1, "un livre sur le sujet choisi vient en main d'une bibliothèque hors du monde : 1 ajouté au souvenir", vr={}),
"seashell-of-stolen-sound": P2("Coquillage au son volé", V("flux"), 4, ["son", "coquillage", "restitution"], why="une minute de sons gardée dans un coquillage, à rejouer une fois", comp=["coquillage"], impact_sats=[(1, ["minutes"])]),
"share-lore": P2("Savoir partagé", REL, 2, ["savoir", "prêt"], why="un de mes savoirs prêté à ceux que je touche", cible_note=["mémoire"], qty_cible=3),
"synchronize": P2("Synchronisation", ORD, 2, ["sceau", "heure", "signal"], why="un sceau sur chacun, qui luit trois fois à l'heure dite, à la seconde près", qty_cible=5, sens=[("vue", None)], manif=["sceau", "lueur"]),
"time-sense": P2("Sens du temps", VIS, 1, ["heure", "date", "exactitude"], why="l'heure exacte, ou la date et les échéances du ciel"),
"empathic-link": P2("Lien empathique", REL, 2, ["émotion", "lien"], why="chacun ressent les émotions de l'autre", cible_note=["psyché"], impact_sats=[(2, ["kilomètres"])]),
"impeccable-flow": P2("Flux impeccable", INT, 1, ["ordre", "harmonie", "revers"], 1, "accordé à l'ordre du monde : 1 ajouté à tout ; un échec grave le retourne en 1 retranché", cible_note=["aptitude"]),
"spirit-sense": P2("Sens des esprits", VIS, P, ["hantise", "présence"], 1, "sent les esprits et les hantises ; 1 ajouté pour les comprendre et s'en garder", cible_note=["esprit"], vr={}),
"animal-vision": P2("Vision animale", VIS, 4, ["sens", "partage"], why="voir, entendre et sentir par une bête, au lieu de ses propres sens", cible_note=["bête"], vr={}),
"behold-the-weave": P2("Contemplation de la trame", V("ordre"), 3, ["avenir", "geste", "verrou"], why="elle doit annoncer un geste de son prochain tour, et s'y tenir", cible_note=["psyché"]),
"familiars-face": P2("Visage du familier", VIS, 2, ["sens", "voix", "capteur"], why="voir, sentir et parler par son compagnon, de loin", cond=["compagnon"], vr={}),
"impending-doom": P2("Fin imminente", V("force", True), 3, ["présage", "mort", "effroi"], 21, "une vision de sa mort qui grandit trois instants, puis 6d6 en moyenne", cible_note=["psyché"], cond=["VIVANT"]),
"organsight": P2("Vision des organes", VIS, 3, ["organe", "faille"], 14, "la cible vue comme écorchée : 4d6 en moyenne au prochain coup tranchant ou perforant", cible_note=["corps"]),
}
FICHES.update(PF2_DIV)

# ----- Pathfinder 2, lot 4 : Divination (seconde partie : rangs 3 à 10) -----
# prying-eye (« scouting-eye » remanié) : même sort que l'Œil magique déjà publié, renvoyé à la comparaison glyphe à glyphe.
PF2_DIV2 = {
"show-the-way": P2("Voie montrée", VIS, P, ["route", "terrain", "voyage"], why="le meilleur chemin pressenti : le terrain difficile ne coûte plus qu'un quart de l'allure, au lieu de la moitié"),
"web-of-eyes": P2("Toile de regards", REL, 2, ["vue", "partage", "capteur"], why="un capteur invisible sur chacun : l'un d'eux, tour à tour, montre aux autres ce qu'il voit", qty_cible=5, discret=True),
"detect-creator": P2("Détection du créateur", VIS, 4, ["créateur", "direction"], why="des restes d'un mort-vivant détruit, la direction de celui qui l'a relevé ; le plomb et l'eau courante l'arrêtent", cible_obj=["cadavre"],
    cond=["MORTVIVANT"], impact_sats=[(30, ["présence", "mètres"])]),
"enhance-senses": P2("Sens aiguisés", INT, 2, ["sens", "pénombre", "doublement"], why="voit dans la pénombre, ou dans le noir s'il y voyait déjà ; ses sens diffus portent deux fois plus loin"),
"entangle-fate": P2("Destins emmêlés", NORD, 3, ["destin", "avenir", "stupeur"], 1, "leurs avenirs se brouillent : pris au dépourvu ; si plusieurs cèdent, stupéfiés de 1 en plus", cible_note=["psyché"], qty_cible=4),
"forgotten-lines": P2("Lignes oubliées", VIS, 4, ["rature", "restitution"], why="une information ôtée d'un texte, ou tirée d'un texte détruit dont il reste un fragment", cible_obj=["écrit"]),
"ghostly-tragedy": P2("Tragédie spectrale", VIS, P, ["esprit", "passé", "violence"], why="les esprits du lieu rejouent les dix dernières minutes d'un drame récent ; je tiens le rôle de la victime",
    impact_plus=[(7, ["ténébreux", "contrecoup"], "2d6 en moyenne pour moi quand la scène s'achève")], vr={}, sens=[("vue", None)], manif=["spectres"]),
"winning-streak": P2("Série gagnante", INT, 2, ["hâte", "chance", "contagion"], why="un geste de plus par instant ; chaque coup décisif du groupe prolonge le sort d'un instant et gagne celui qui l'a porté",
    impact_sats=[(6, ["mètres"])]),
"inevitable-disaster": P2("Désastre inévitable", NORD, 3, ["accident", "fatalité"], 55, "un accident la frappe de 55, où qu'elle soit, même sur un autre plan", impact_sats=[(4, ["délai", "instants"])]),
"mirecloak": P2("Manteau de fange", SEP, 2, ["suaire", "pénombre", "discrétion"], 1, "dans la pénombre ou le noir : 1 ajouté à la défense, 2 à la discrétion", cible_note=["garde"], qty_cible=4,
    impact_plus=[(9, ["psyché", "savoir", "arrachement"], "2d8 en moyenne à qui frappe de près : une information lui est arrachée, puis le suaire tombe")], sens=[("vue", None)], manif=["suaire", "vert"]),
"cast-into-time": P2("Jeté dans le temps", DISP, P, ["temps", "chute", "savoir"], 41, "5d8 + 5d6 en moyenne, à l'esprit et au corps ; elles disparaissent dans le temps jusqu'à la fin de l'instant"),
"catch-your-name": P2("Nom saisi au vol", VIS, 4, ["nom", "lieu", "exactitude"], why="un nom et le lieu exact de celui qui vient de prononcer le mien", cond=["nom"]),
"halcyon-infusion": P2("Infusion de magie", REL, 2, ["sort", "prêt", "usage"], 1, "un de mes sorts d'interaction 2 prêté pour un jour, à lancer une fois ; d'interaction 3 ou 4 si l'allié est aguerri", cible_note=["aptitude"]),
"heinous-future": P2("Avenir odieux", NORD, 3, ["présage", "lenteur", "stupeur"], 1, "un avenir affreux vu dans un miroir fêlé : ralentie et stupéfiée de 1 jusqu'à son prochain repos de 8 heures", cible_note=["psyché"],
    comp=["miroir"], dur=(8, "HEURES"), fin=["repos"]),
"suspended-retribution": P2("Châtiment suspendu", NORD, 3, ["présage", "interdit", "épée"], 70, "un présage au-dessus d'elle : il s'abat de 70 si elle fait le geste interdit ; 3 gestes de conjuration l'écartent",
    cible_note=["psyché"], sens=[("vue", None)], manif=["épée", "présage"]),
"time-beacon": P2("Balise temporelle", ORD, 1, ["temps", "balise", "retour"], why="à la fin de l'instant, je peux revenir au moment de la balise et défaire tout ce qui s'est passé depuis"),
"true-target": P2("Cible véritable", VIS, 2, ["avenir", "précision", "désigné"], why="le premier coup de chacun contre l'ennemi désigné : le meilleur de deux essais, sans gêne ni dissimulation", qty_cible=4, vr={}),
"prying-survey": P2("Ronde indiscrète", VIS, P, ["œil", "capteur", "fouille"], why="huit yeux invisibles fouillent les alentours et me rapportent ce qu'ils trouvent", qty=8, discret=True),
"unrelenting-observation": P2("Observation implacable", VIS, 5, ["suivi", "image", "obstacle"], why="mes alliés voient son image à travers tout, hormis le plomb et l'eau courante, à toute distance",
    impact_sats=[(5, ["alliés"])], dur=(1, "HEURES"), vr={}),
"proliferating-eyes": P2("Yeux proliférants", VIS, 4, ["œil", "capteur", "contagion"], 31, "un œil invisible posé sur elle, qui bourgeonne sur ceux qu'elle touche : jusqu'à 31 yeux, par lesquels je vois", discret=True),
"fated-confrontation": P2("Affrontement fatidique", REL, 3, ["destin", "duel", "isolement"], why="un allié paraît près de son ennemi ; un instant durant, rien d'extérieur ne les atteint ; chacun plie le sort une fois par instant",
    qty_cible=2, impact_sats=[(9, ["mètres"])]),
}
FICHES.update(PF2_DIV2)

# ----- Pathfinder 2, lot 5 : Enchantement -----
PF2_ECARTE.update({"anathematic-reprisal": "n'existe que par l'interdit d'une divinité", "divinity-leech": "n'agit que sur le lien d'un prêtre à sa divinité",
 "fateful-condemnation": "suppose des vies antérieures"})
PEUR = V("force", True); ATT = V("force")
_PSY = dict(cible_note=["psyché"])
PF2_ENC = {
"contagious-idea": P2("Idée contagieuse", REL, 4, ["pensée", "contagion"], why="une pensée posée dans un esprit, puis dans un second", qty_cible=2, **_PSY, options=[
    O("Pensée plaisante", impact=(5, ["pensée", "contagion", "apaisement"], "apaisée : 5 points de vie d'emprunt pour une minute")),
    O("Pensée terrifiante", verb=PEUR, impact=(1, ["pensée", "contagion", "effroi"], "effrayée de 1"))]),
"forbidden-thought": P2("Pensée interdite", NORD, 3, ["verrou", "interdit"], 4, "1d6 en moyenne si elle tente le geste interdit à son prochain instant", **_PSY),
"infectious-enthusiasm": P2("Enthousiasme contagieux", INT, 1, ["entrain", "partage"], 1, "1 ajouté à mes coups, à ma volonté ou à mon ascendant ; un allié qui m'a vu peut prendre le même élan", impact_sats=[(9, ["mètres"])]),
"invoke-true-name": P2("Invocation du vrai nom", NINT, 3, ["nom", "faille"], 2, "jusqu'à la fin de l'instant : prise au dépourvu par mes sorts, 2 retranché à ce qu'elle leur oppose", cible_note=["résistance"], cond=["nom"]),
"tame": P2("Apprivoisement", REL, 4, ["douceur", "confiance"], 1, "son humeur envers moi s'améliore de 1 cran", cible_note=["bête"], cond=["domestique"]),
"agitate": P2("Fébrilité", NORD, 3, ["agitation", "mouvement"], 9, "2d8 en moyenne à chaque instant où elle ne se déplace pas", dur=(12, "SECONDES"), **_PSY),
"befuddle": P2("Embrouillement", NORD, 3, ["maladresse", "stupeur"], 2, "gauche et stupéfiée de 2", **_PSY),
"cycle-of-retribution": P2("Cycle des représailles", NORD, 3, ["violence", "remords"], 2, "1d4 en moyenne à son premier geste hostile de chaque instant", **_PSY),
"d-j-vu": P2("Déjà-vu", ORD, 3, ["boucle", "répétition"], why="ce qu'elle fait à son prochain instant, elle doit le refaire au suivant", vr={}, **_PSY),
"draw-ire": P2("Colère attirée", ATT, 3, ["colère", "provocation"], 6, "1d10 en moyenne ; 1 retranché à ses coups contre tout autre que moi", **_PSY),
"fated-healing": P2("Guérison des adversaires", HE, 4, ["vie", "trêve"], 2, "1d4 en moyenne à la fin de chacun de leurs instants, tant qu'aucun ne s'en prend à l'autre", qty_cible=2, guerit=True, fin=["agression"]),
"forced-mercy": P2("Clémence forcée", NINT, 3, ["retenue", "clémence"], why="ses coups évitent les points vitaux : ils assomment sans tuer et ne laissent aucun mal durable", cible_note=["frappe"], dur=(12, "SECONDES")),
"schadenfreude": P2("Joie mauvaise", NORD, 3, ["moquerie", "stupeur"], 1, "distrait par mon échec cuisant : stupéfié de 1 un instant", cond=["échec"], vr={}, **_PSY),
"soothe": P2("Baume de l'esprit", HE, 2, ["vie"], 10, "1d10 + 4 en moyenne", guerit=True, vr={}, impact_plus=[(2, ["psyché", "résistance"], "2 ajouté contre ce qui vise l'esprit")]),
"synchronize-steps": P2("Pas accordés", REL, 2, ["pas", "unisson"], why="quand l'un se déplace, l'autre peut le suivre aussitôt", qty_cible=2),
"charitable-urge": P2("Élan charitable", ORD, 3, ["don", "charité", "contrainte"], why="à son prochain instant, elle doit d'abord donner un de ses biens au plus proche", vr={}, **_PSY),
"mind-games": P2("Joute d'esprits", NORD, 3, ["joute", "étourdissement"], why="étourdie tant que je tiens la joute ; si elle l'emporte nettement, c'est moi qui le suis", comp=["pion"], **_PSY),
"thundering-dominance": P2("Domination tonitruante", INT, 2, ["rugissement", "intimidation"], 1, "1 ajouté pour intimider", cond=["compagnon"], fam="A",
    impact_plus=[(18, ["son", "effroi"], "un rugissement, une fois : 4d8 en moyenne à 3 m autour, et l'effroi")], sens=[("ouïe", None)], manif=["rugissement"]),
"warriors-regret": P2("Regret du guerrier", NORD, 3, ["malédiction", "remords", "violence"], 4, "1d8 en moyenne par être blessé dans l'instant, 4d8 au plus, tant qu'elle ne cesse pas", **_PSY),
"agonizing-despair": P2("Désespoir déchirant", PEUR, 3, ["effroi", "désespoir"], 14, "4d6 en moyenne ; effrayée de 2", impact_sats=[(2, ["effroi"])], **_PSY),
"crisis-of-faith": P2("Crise de foi", NORD, 3, ["doute", "foi"], 21, "6d6 en moyenne", vr={}, **_PSY,
    impact_plus=[(27, ["foi", "stupeur"], "6d8 en moyenne à qui tire ses sorts d'une foi, stupéfié de 1")]),
"dream-message": P2("Message en rêve", REL, 2, ["rêve", "message"], why="un message d'une minute, reçu dans son sommeil", impact_sats=[(1, ["minutes"])], vr={}),
"mind-of-menace": P2("Esprit menaçant", SEP, 1, ["riposte", "effroi"], 2, "qui s'en prend à mon esprit est effrayé de 2, et j'ajoute 2 à ma défense contre lui", cible_note=["psyché", "résistance"]),
"roaring-applause": P2("Tonnerre d'applaudissements", ORD, 3, ["ovation", "lenteur"], 1, "elle m'applaudit sans pouvoir s'arrêter : ralentie de 1, incapable de riposter", **_PSY),
"shift-blame": P2("Faute reportée", TR, 3, ["souvenir", "coupable"], why="elle se souvient d'un autre que le vrai auteur du coup ou du geste", cible_note=["mémoire"], cond=["coup"]),
"sudden-recollection": P2("Souvenir soudain", NVIS, 4, ["savoir", "déclencheur"], why="un savoir enfoui dans son esprit, ou oublié, jusqu'au signal fixé", cible_note=["mémoire"]),
"aromatic-lure": P2("Leurre odorant", ATT, 3, ["odeur", "attirance", "stupeur"], 2, "stupéfiée de 2, elle va droit au lieu choisi, un instant durant", dur=(6, "SECONDES"), **_PSY),
"clownish-curse": P2("Malédiction du pitre", NORD, 3, ["malédiction", "pitrerie", "bruit"], why="mains et pieds gourds, bruits ridicules à chaque pas : le pire de deux essais à l'adresse, à la discrétion, au larcin",
    cible_note=["corps"], dur=(1, "HEURES")),
"compel-true-name": P2("Contrainte du vrai nom", ORD, 3, ["nom", "obéissance"], why="appelée par son vrai nom, elle obéit à un ordre qui ne la détruit pas", cond=["nom"], dur=(10, "MINUTES"), **_PSY),
"daydreamers-curse": P2("Malédiction du rêveur", NORD, 3, ["malédiction", "distraction"], why="distraite : le pire de deux essais pour soigner, observer, lire la nature, survivre", dur=(P, None), **_PSY),
"deathless-march": P2("Marche des sans-repos", PEUR, P, ["chant", "effroi"], 2, "les vivants effrayés de 2", **_PSY,
    impact_plus=[(P, ["relevé", "hâte", "marche"], "les morts-vivants font un déplacement de plus par instant, une minute durant")], sens=[("ouïe", None)], manif=["chant"]),
"dull-ambition": P2("Ambition émoussée", NORD, 3, ["malédiction", "élan", "échec"], why="un jour durant : toujours en retard à l'action, et ses entreprises de longue haleine tournent court", dur=(1, "JOURS"), vr={}, **_PSY),
"favorable-review": P2("Critique favorable", ORD, 3, ["éloge", "silence"], why="une semaine durant, elle ne peut dire de mal du sujet nommé : ses critiques tournent en éloges", dur=(7, "JOURS"), **_PSY),
"girzanjes-march": P2("Marche guerrière", INT, P, ["chant", "vaillance"], 1, "1 ajouté aux coups, à la vigueur et à la volonté de ceux qui m'entendent", cible_note=["aptitude"], sens=[("ouïe", None)], manif=["chant"]),
"implement-of-destruction": P2("Instrument de destruction", PEUR, 3, ["arme", "hantise"], 7, "2d6 en moyenne à l'esprit, à chaque instant, dès que l'arme désignée la touche", **_PSY),
"infectious-melody": P2("Mélodie entêtante", ORD, P, ["mélodie", "chant", "parole"], why="les ennemis ne peuvent plus s'exprimer qu'en chantant l'air", impact_sats=[(3, ["instants"])], dur=(18, "SECONDES"), **_PSY,
    sens=[("ouïe", None)], manif=["mélodie"]),
"outcasts-curse": P2("Malédiction du paria", NREL, 3, ["malédiction", "rejet"], 1, "sa présence rebute : chacun l'accueille 1 cran plus mal ; le pire de deux essais pour convaincre, tromper, intimider", dur=(P, None), vr={}, **_PSY),
"sages-curse": P2("Malédiction du sage", NORD, 3, ["malédiction", "savoir", "doute"], why="l'esprit encombré de détails : le pire de deux essais pour tout savoir", cible_note=["mémoire"], dur=(P, None)),
"dreaming-potential": P2("Potentiel rêvé", INT, 2, ["rêve", "apprentissage"], why="un rêve lucide d'une nuit vaut une journée passée à se former", cible_note=["aptitude"], cond=["sommeil"], vr={}),
"glimmer-of-charm": P2("Lueur de charme", REL, P, ["charme", "amitié"], 2, "l'humeur de ceux qui m'approchent s'améliore de 2 crans ; ils ne peuvent plus s'en prendre à moi", fin=["agression"], **_PSY,
    sens=[("vue", None)], manif=["scintillement"]),
"subconscious-suggestion": P2("Suggestion enfouie", ORD, 3, ["suggestion", "déclencheur"], why="une suggestion dort dans son esprit jusqu'au signal fixé ; elle la suit alors", impact_sats=[(1, ["minutes"])], dur=(1, "JOURS"), vr={}, **_PSY),
"blinding-fury": P2("Fureur aveuglante", NVIS, 3, ["colère", "aveuglement", "riposte"], why="qui m'a frappé cesse de me voir jusqu'à la fin de son instant, et de nouveau chaque fois qu'il me blesse", cond=["coup"], dur=(1, "MINUTES"), vr={}),
"zealous-conviction": P2("Conviction zélée", ORD, 2, ["zèle", "obéissance"], 2, "2 ajouté contre ce qui vise l'esprit ; ils font ce que je leur dis", qty_cible=10, impact_sats=[(12, ["vie", "temporaire"])], vr={}, **_PSY),
"entrancing-eyes": P2("Regard envoûtant", ATT, P, ["regard", "fascination", "stupeur"], why="qui finit son instant près de moi est stupéfié et fasciné jusqu'à la fin du suivant", **_PSY, sens=[("vue", None)], manif=["lueur", "yeux"]),
"inexhaustible-cynicism": P2("Cynisme inépuisable", NREL, 3, ["doute", "défiance"], 21, "6d6 en moyenne à la fin de chaque instant passé sans chercher à percer l'illusion qu'elle croit voir partout", qty_cible=5, dur=(1, "MINUTES"), **_PSY),
"warp-mind": P2("Esprit distordu", NORD, 3, ["confusion", "immédiat"], why="confuse une minute ; l'effet est immédiat et ne se dissipe pas", dur=(1, "MINUTES"), vr={}, **_PSY),
"burning-blossoms": P2("Floraison ardente", EXI, P, ["arbre", "pétale", "feu"], 21, "6d6 en moyenne sous les branches", fam="A",
    impact_plus=[(P, ["fascination", "attirance"], "qui voit l'arbre est fasciné et marche vers lui")], impact_sats=[(30, ["élévation", "mètres"]), (9, ["branche", "mètres"])],
    sens=[("vue", None)], manif=["arbre", "fleurs"]),
"canticle-of-everlasting-grief": P2("Cantique du deuil éternel", PEUR, 3, ["deuil", "effroi", "mélodie"], 35, "10d6 en moyenne ; effrayée de 3, sourde à tout appui pendant une semaine", impact_sats=[(3, ["effroi"])],
    dur=(7, "JOURS"), vr={}, **_PSY),
"divine-inspiration": P2("Inspiration", INT, 2, ["sort", "regain"], 7, "rend un sort déjà lancé, d'interaction 7 au plus", cible_note=["aptitude"], vr={}),
"crusade": P2("Croisade", ORD, 4, ["cause", "dévouement"], why="voués à la cause que je proclame — jusqu'à la mort pour les moins aguerris", qty_cible=4, **_PSY),
"natures-enmity": P2("Inimitié de la nature", NREL, 3, ["nature", "bête", "plante"], 11, "2d10 en moyenne quand les bêtes l'assaillent ; la nature se ferme à elle", qty_cible=5, impact_sats=[(3, ["lenteur", "mètres"])], vr={}),
"unfathomable-song": P2("Chant insondable", NORD, 3, ["chant", "égarement", "hasard"], why="à chaque instant, le chant frappe au hasard : effroi, confusion, stupeur ou cécité", qty_cible=5, vr={}, **_PSY, sens=[("ouïe", None)], manif=["chant"]),
"fabricated-truth": P2("Vérité fabriquée", EXI, 4, ["croyance", "certitude"], why="une affirmation tenue pour vraie pendant une semaine", qty_cible=5, dur=(7, "JOURS"), vr={}, **_PSY),
}
FICHES.update(PF2_ENC)

# ----- Pathfinder 2, lot 6 : Illusion -----
# Les sorts d'« ombre » de Pathfinder sont tissés d'énergie astrale : chacun a sa forme ténébreuse et sa forme lumineuse.
def _FACES(words, v=None, why=""):
    v = P if v is None else v
    return [O("Forme ténébreuse", impact=(v, list(words) + ["ténébreux"], why + " ; tissé de la face ténébreuse")),
            O("Forme lumineuse", impact=(v, list(words) + ["lumineux"], why + " ; tissé de la face lumineuse"))]
P2F = lambda fr, verb, cible, words, v=None, why="", **kw: P2(fr, verb, cible, words, v, why, options=_FACES(words, v, why), **kw)
PF2_ILL = {
"bullhorn": P2("Porte-voix", INT, 1, ["voix", "portée", "mètres"], 150, "ma voix s'entend clairement à 150 m, par-dessus tout autre bruit", vr={}),
"hologram-cage": P2("Cage chatoyante", NVIS, P, ["cube", "lumière", "écran"], why="un cube de motifs lumineux : nul ne voit au travers, ni dans un sens ni dans l'autre", impact_sats=[(3, ["éclat", "mètres"])],
    sens=[("vue", None)], manif=["cube", "motifs"]),
"exchange-image": P2("Échange de visages", NVIS, 4, ["apparence", "échange"], why="je prends son apparence, et elle la mienne", cond=["humanoïde"], dur=(1, "HEURES")),
"item-facade": P2("Façade d'objet", NVIS, 4, ["apparence", "état"], why="l'objet paraît neuf, ou au contraire délabré, à l'œil comme au toucher", cible_obj=["objet"], vr={}),
"lose-the-path": P2("Chemin perdu", NVIS, 3, ["terrain", "égarement"], why="le terrain lui semble autre : toute sa course en devient pénible", cond=["mouvement"], **_PSY),
"phantom-pain": P2("Douleur fantôme", EXI, 3, ["douleur", "fantasme"], 5, "2d4 en moyenne", vr={}, **_PSY,
    impact_plus=[(2, ["persistance", "nausée"], "1d4 en moyenne à chaque instant, tant que dure la nausée")]),
"thicket-of-knives": P2("Fourré de lames", EXI, 1, ["bras", "double", "feinte"], 2, "des copies fantômes de mon bras armé : 2 ajouté pour tromper et feinter", sens=[("vue", None)], manif=["bras", "lames"]),
"befitting-attire": P2("Tenue de circonstance", NVIS, 2, ["habit", "occasion"], why="leurs habits et leur équipement paraissent ceux qui conviennent à l'occasion", qty_cible=5),
"empty-pack": P2("Sac vide", NVIS, 4, ["contenu", "invisible"], why="tout ce que contient le sac devient invisible ; le sac reste visible", cible_obj=["contenant"]),
"illusory-creature": P2("Créature illusoire", EXI, P, ["créature", "fantasme", "toucher"], why="l'image d'une créature, avec ses bruits et son odeur, crédible au toucher ; ses coups ne blessent que l'esprit", vr={},
    sens=[("vue", None), ("ouïe", None), ("odorat", None)], manif=["créature"]),
"phantasmal-treasure": P2("Trésor fantasmatique", ATT, 3, ["trésor", "fascination"], why="elle seule voit ce qu'elle a de plus précieux au monde, et en reste fascinée", cond=["VIVANT"], dur=(1, "MINUTES"), vr={}, **_PSY),
"phantom-crowd": P2("Foule fantôme", EXI, P, ["foule", "approbation"], why="une foule serrée m'approuve bruyamment ; elle gêne le passage de qui y croit", sens=[("vue", None), ("ouïe", None)], manif=["foule"]),
"umbral-extraction": P2F("Extraction astrale", V("flux"), 3, ["sort", "larcin"], 2, "un sort préparé arraché à son reflet astral : 1d4 en moyenne par cran du sort volé, que je pourrai lancer"),
"distracting-chatter": P2("Brouhaha", EXI, 3, ["voix", "cacophonie"], 2, "prise au dépourvu ; 2 retranché à son ouïe ; une fois sur cinq, sa parole et ses sorts parlés se perdent", dur=(18, "SECONDES"), **_PSY),
"oneiric-mire": P2("Bourbier onirique", EXI, P, ["bourbier", "rêve", "mètres"], 3, "le sol semble une fondrière : 3 m de moins par instant, parfois cloué sur place", **_PSY),
"phantom-prison": P2("Prison fantôme", EXI, 3, ["mur", "prison", "fantasme"], why="des murs qu'elle seule voit et sent l'enferment ; elle ne voit plus rien au-dehors", **_PSY),
"shadow-projectile": P2F("Projectile astral", EXI, 3, ["projectile", "double"], 14, "3d8 en moyenne : un double illusoire du tir d'un allié, qui la prend au dépourvu", cond=["tir"], **_PSY),
"false-nature": P2("Fausse nature", NVIS, 4, ["nature", "affirmation"], why="l'objet passe pour ce que je déclare qu'il est", cible_obj=["objet"]),
"invisibility-curtain": P2("Rideau d'invisibilité", NVIS, P, ["rideau", "côté"], why="ceux d'un côté du mur sont invisibles pour ceux de l'autre", forme=_MUR(18, 3), discret=True),
"mirrors-misfortune": P2("Miroir de malchance", EXI, 1, ["double", "miroir", "malchance"], 2, "qui frappe mon double le brise : le pire de deux essais à ses 2 prochains coups", sens=[("vue", None)], manif=["double"]),
"ocular-overload": P2("Surcharge oculaire", NVIS, 3, ["éclair", "aveuglement"], why="au moment où il m'attaque, des éclats de couleur l'aveuglent jusqu'à la fin de l'instant", cond=["agression"]),
"replicate": P2("Réplique", EXI, 2, ["double", "service"], why="un double illusoire de l'allié, qui marche, parle et fait des gestes simples à mon ordre", sens=[("vue", None)], manif=["double"]),
"umbral-graft": P2F("Greffe astrale", V("flux"), 3, ["sort", "larcin", "greffe"], why="un sort qui agit sur l'ennemi lui est arraché : je le prends pour moi, ou le garde pour l'offrir"),
"chameleon-coat": P2("Manteau caméléon", NVIS, 2, ["couleur", "affût"], 3, "habits et équipement prennent les couleurs du lieu : 3 ajouté pour se cacher", qty_cible=8, vr={}),
"cloak-of-colors": P2("Cape de couleurs", EXI, 2, ["couleur", "éblouissement", "aveuglement"], why="éblouit ceux qui la côtoient ; qui la frappe de près est aveuglé un instant", vr={}, sens=[("vue", None)], manif=["couleurs"]),
"drop-dead": P2("Tomber raide", NVIS, 2, ["cadavre", "invisible"], why="elle semble tomber morte : un faux cadavre reste là, et elle devient invisible", cond=["blessure"], vr={}),
"hallucination": P2("Hallucination tenace", EXI, 3, ["fantasme", "perception"], why="elle perçoit une chose pour une autre, cesse de percevoir ce qui est là, ou perçoit ce qui n'y est pas", vr={}, **_PSY),
"mirror-malefactors": P2("Miroirs malfaisants", EXI, 3, ["miroir", "reflet"], 32, "7d8 en moyenne à chaque instant où je soutiens le sort ; effrayée de 1 tant que les miroirs l'entourent", impact_sats=[(1, ["effroi"])],
    sens=[("vue", None)], manif=["miroirs"], **_PSY),
"portrait-of-the-artist": P2("Portrait de l'artiste", NVIS, 1, ["apparence", "artiste", "talent"], why="je prends les traits d'un artiste connu, et mes œuvres ou mon jeu semblent valoir les siens"),
"shadow-siphon": P2F("Siphon astral", NINT, 4, ["illusion", "fractionné"], 2, "le sort visé devient à demi illusoire : ses dégâts réduits de moitié", cible_note=["sort"], cond=["sort"]),
"strange-geometry": P2("Géométrie étrange", NORD, P, ["espace", "torsion", "téléportation"], why="l'espace s'y tord : tout y devient terrain pénible, et qui sort d'une zone ressort par une autre, au hasard", vr={}),
"blanket-of-stars": P2("Manteau d'étoiles", NVIS, 1, ["nuit", "étoile", "discrétion"], 2, "2 ajouté à la discrétion ; sous un ciel étoilé, invisible immobile, estompé en mouvement", vr={},
    impact_plus=[(P, ["éblouissement", "vertige"], "qui scrute les étoiles du manteau est ébloui")], sens=[("vue", None)], manif=["manteau", "étoiles"]),
"chromatic-image": P2("Image chromatique", EXI, 1, ["double", "couleur"], 10, "trois doubles colorés ; qui en détruit un prend 5 d'un élément et 5 à l'esprit", qty=3, fam="A", sens=[("vue", None)], manif=["doubles", "couleurs"]),
"phantasmal-calamity": P2("Calamité fantasmatique", EXI, P, ["cataclysme", "fantasme"], 38, "11d6 en moyenne ; au pire, se croit piégée, étourdie une minute", vr={}, **_PSY),
"vibrant-pattern": P2("Motif vibrant", EXI, P, ["motif", "lumière", "aveuglement"], why="éblouit ceux qui s'y trouvent, aveugle ceux qui cèdent", vr={}, sens=[("vue", None)], manif=["motif", "lumières"]),
"mask-of-terror": P2("Masque de terreur", EXI, 2, ["masque", "effroi"], 2, "chacun la voit sous les traits de ce qu'il redoute : qui veut s'en prendre à elle est d'abord effrayé de 2", vr={}),
"shadow-raid": P2F("Raid astral", EXI, P, ["silhouette", "assaut"], 27, "6d8 en moyenne à l'apparition",
    impact_plus=[(14, ["persistance", "dissimulation"], "3d8 en moyenne à chaque instant ; tous y sont estompés")], sens=[("vue", None)], manif=["silhouettes"]),
"visions-of-danger": P2("Visions de danger", EXI, P, ["nuée", "monstre", "fantasme"], 36, "8d8 en moyenne à chaque instant passé dans la zone", vr={}, **_PSY),
"disappearance": P2("Disparition", NVIS, 2, ["sens", "indétectable"], why="échappe à tous les sens, pas seulement à la vue", vr={}),
"undermine-reality": P2("Réalité sapée", NE, 3, ["substance", "fractionné"], 2, "à demi réelle : ses coups réduits de moitié, ses réussites bornées, ses sorts mieux repoussés", dur=(1, "MINUTES")),
"unspeakable-shadow": P2("Ombre indicible", TR, 3, ["ombre", "monstre", "effroi"], 3, "son ombre devient un monstre qui veut la dévorer : effrayée de 3, elle doit la frapper ou la fuir ; au pire, elle en meurt",
    dur=(1, "MINUTES"), **_PSY),
"shadow-army": P2F("Armée astrale", EXI, P, ["double", "armée", "assaut"], 33, "3d10 + 3d10 en moyenne, à l'esprit et au corps, à chaque instant ; je me fonds parmi mes doubles",
    impact_plus=[(2, ["entrave", "choix"], "maladresse, faiblesse ou lenteur de 2, à mon choix")], sens=[("vue", None)], manif=["doubles"]),
}
FICHES.update(PF2_ILL)

# ----- Pathfinder 2, lot 7 : Évocation -----
PF2_ECARTE.update({"blightburn-blast": "substance propre à Golarion"})
# Sorts fondus dans la page d'un autre : la face opposée du même sort, ou le même mur vu de l'autre face.
PF2_FONDU = {"moonlight-ray": "chilling-darkness", "wall-of-shadow": "wall-of-radiance"}
E2 = lambda fr, cible, words, v=None, why="", **kw: P2(fr, NF, cible, words, v, why, **kw)
PF2_EVO = {
"astral-rain": E2("Pluie de lames mentales", P, ["lame", "pluie"], 5, "2d4 en moyenne à qui s'y trouve ou y entre avant mon prochain instant"),
"dancing-blade": E2("Lame dansante", 3, ["arme", "danse"], 7, "2d6 en moyenne : une arme animée harcèle la cible et la suit"),
"divine-lance": P2F("Lance astrale", NF, 3, ["trait"], 2, "1d4 en moyenne", vr={}),
"electric-arc": E2("Arc électrique", 3, ["arc", "rebond"], 2, "1d4 en moyenne à chacune", qty_cible=2, comb="Foudre", vr={}),
"entropic-wheel": P2("Roue d'entropie", INT, 1, ["chaleur", "roue", "inversion"], 1, "une roue amasse la chaleur : mes sorts de feu glacent en plus, mes sorts de froid brûlent en plus, de 1 par grain amassé", fam="A"),
"gale-blast": E2("Rafale", P, ["vent", "poussée"], why="ceux qui m'entourent sont frappés et repoussés d'un pas", comb="Air", vr={}),
"haunting-hymn": E2("Hymne lancinant", P, ["hymne", "surdité"], why="un hymne discordant que seuls entendent ceux de la zone : il blesse, et peut assourdir", impact_sats=[(1, ["minutes"])], comb="Orage", vr={}),
"imaginary-weapon": E2("Arme imaginaire", 3, ["arme", "force"], 5, "1d8 en moyenne ; au mieux, l'arme éclate et repousse de 3 m", impact_sats=[(3, ["poussée", "mètres"])]),
"phase-bolt": E2("Trait déphasé", 3, ["trait", "déphasage"], 2, "1d4 en moyenne ; bouclier et abri la protègent de 2 de moins"),
"puff-of-poison": E2("Bouffée de poison", 3, ["haleine", "persistance"], 2, "un souffle toxique au visage, puis 2 à chaque instant", comb="Ammoniac", vr={}),
"redistribute-potential": E2("Chaleur redistribuée", P, ["chaleur", "transfert", "froid", "feu"], 10, "4d4 en moyenne : le froid d'un côté, le feu de l'autre", fam="A"),
"scatter-scree": E2("Éboulis", P, ["pierre", "encombrement"], 2, "1d4 en moyenne ; le sol encombré une minute", comb="Roche", vr={}),
"shatter-mind": E2("Esprits fracassés", P, ["assaut"], 5, "2d4 en moyenne", **_PSY),
"spout": E2("Jaillissement", P, ["eau", "jet"], 2, "1d4 en moyenne", comb="Eau", vr={}),
"telekinetic-rend": E2("Déchirure télékinétique", P, ["torsion"], 4, "1d6 en moyenne, en choc ou en taille"),
"acidic-burst": E2("Explosion acide", P, ["coque", "éclatement"], 7, "2d6 en moyenne"),
"airburst": E2("Souffle d'air", P, ["vent", "poussée", "mètres"], 2, "tout est repoussé de 1,5 m, arrondi à 2 ; les ripostes gênées", comb="Air"),
"briny-bolt": E2("Trait de saumure", 3, ["eau", "sel", "aveuglement"], 7, "2d6 en moyenne ; le sel aveugle un instant", comb="Eau"),
"buffeting-winds": E2("Vents cinglants", P, ["vent", "assommer"], 5, "2d4 en moyenne : assomme les vivants sans les tuer, blesse et repousse les morts-vivants", comb="Air"),
"chilling-spray": E2("Gerbe glacée", P, ["givre", "lenteur", "mètres"], 5, "2d4 en moyenne ; ralentis de 1,5 m", vr={}),
"concordant-choir": E2("Chœur concordant", 3, ["son", "consonance"], 2, "1d4 en moyenne", vr={}),
"echoing-weapon": P2("Arme à échos", INT, 4, ["son", "écho", "décharge"], 4, "à la fin de l'instant, l'arme rend en son les coups portés : 1 par coup, 4 au plus", cible_obj=["arme"], fam="A"),
"forge": E2("Forge", 3, ["métal", "chauffe"], 11, "3d6 en moyenne ; le métal chauffé s'amollit d'autant"),
"friendfetch": P2("Rappel des amis", ATT, 2, ["fil", "traction"], why="des fils de force tirent deux alliés jusqu'à moi", qty_cible=2),
"gravitational-pull": P2("Attraction", ATT, 3, ["pesanteur", "traction", "mètres"], 3, "tirée de 3 m vers moi, parfois renversée"),
"gritty-wheeze": E2("Souffle de sable", P, ["sable", "dessèchement"], 5, "2d4 en moyenne ; pire pour les êtres d'eau et les plantes", comb="Sable"),
"horizon-thunder-sphere": E2("Sphère du tonnerre lointain", 3, ["sphère", "éblouissement"], 11, "3d6 en moyenne"),
"kinetic-ram": E2("Bélier cinétique", 3, ["poussée", "mètres"], 3, "repoussée de 3 m"),
"noxious-vapors": E2("Vapeurs nocives", P, ["fumée", "dissimulation"], 4, "1d6 en moyenne ; la fumée cache ceux qui s'y trouvent", vr={}),
"penumbral-shroud": P2("Voile de pénombre", NINT, 4, ["lumière", "pénombre"], 1, "elle perçoit la lumière un cran plus bas ; 1 ajouté contre les effets de lumière"),
"personal-rain-cloud": P2("Nuage de pluie personnel", EXI, 4, ["nuage", "pluie"], 2, "un petit nuage la suit et l'arrose : 2 retranché au feu reçu, les flammes s'éteignent", comb="Eau"),
"pummeling-rubble": E2("Grêle de gravats", P, ["pierre", "poussée"], 5, "2d4 en moyenne ; repoussés d'un pas", comb="Roche", vr={}),
"purifying-icicle": E2("Stalactite purificatrice", 3, ["glace", "perforation"], 11, "2d6 + 1d6 en moyenne", comb="Glace", impact_plus=[(2, ["lumineux"], "1d4 en moyenne de plus à un mort-vivant")]),
"scouring-sand": P2("Sable décapant", NE, P, ["sable", "végétation", "éblouissement"], why="le sable arrache les broussailles, défait les entraves végétales et brouille la vue", comb="Sable"),
"shockwave": E2("Onde de choc", P, ["terre", "secousse", "chute"], why="le sol tremble : ceux qui s'y tiennent trébuchent ou tombent", comb="Terre"),
"animated-assault": E2("Assaut animé", P, ["objet", "projection"], 11, "2d10 en moyenne", impact_plus=[(6, ["persistance"], "1d10 en moyenne à chaque instant où je soutiens le sort")], vr={}),
"breath-of-drought": P2("Souffle de sécheresse", NQ, P, ["chaleur", "aridité", "nausée"], why="une touffeur aride donne la nausée ; pire pour les êtres d'eau et les plantes", fam="A"),
"dancing-shield": P2("Bouclier dansant", SEP, 2, ["bouclier", "orbite"], why="un bouclier lévite autour de l'allié et pare pour lui", cible_note=["garde"]),
"elemental-zone": P2("Zone élémentaire", INT, P, ["élément", "zone"], 2, "les sorts de l'élément choisi y frappent de 2 de plus", fam="A",
    options=[O(n, impact=(2, ["zone", w], f"les sorts de cet élément y frappent de 2 de plus")) for n, w in _ELEM6]),
"flame-wisp": P2("Flammèches", EXI, 1, ["flammèche", "riposte"], 2, "trois flammèches autour de ma tête : à chacun de mes coups, l'une part et brûle de 1d4 en moyenne", qty=3),
"ignite-fireworks": E2("Feu d'artifice", P, ["étincelle", "fracas", "éblouissement"], 10, "1d8 de feu + 1d8 de son en moyenne"),
"magnetic-attraction": P2("Attraction magnétique", ATT, 4, ["métal", "aimant"], why="jusqu'à dix petits objets de métal volent jusqu'à moi", cible_obj=["objet"], qty_cible=10, comb="Magnétisme"),
"radiant-field": P2("Champ radieux", EXI, P, ["lumière", "aveuglement"], why="une vive lumière : aveugle ceux qui la craignent, étouffe les ténèbres magiques"),
"rime-slick": E2("Verglas", P, ["glace", "glissade"], 5, "2d4 en moyenne ; le sol verglacé"),
"sea-surge": E2("Lame de fond", P, ["vague", "renversement"], 11, "une vague renverse et emporte ; 3d6 en moyenne pour qui est emporté", comb="Eau", impact_sats=[(18, ["course", "mètres"])]),
"sudden-bolt": E2("Éclair soudain", 3, ["éclair"], 26, "4d12 en moyenne", niveau=3),
"blazing-dive": E2("Plongeon ardent", P, ["comète", "chute"], 19, "3d4 + 3d6 en moyenne à 3 m autour du point de chute", comb="Feu", impact_sats=[(18, ["bond", "mètres"])]),
"bracing-tendrils": P2("Vrilles d'ancrage", V("mouvement", True), 1, ["vrille", "ancrage", "riposte"], why="des vrilles de force m'ancrent au sol : on ne me déplace plus contre mon gré, et qui échoue est repoussé d'un pas",
    sens=[("vue", None)], manif=["vrilles"]),
"chilling-darkness": E2("Rayon astral glacé", 3, ["rayon"], 18, "5d6 en moyenne de froid", options=[
    O("Forme ténébreuse", impact=(18, ["rayon", "ténébreux"], "5d6 en moyenne de froid ; autant de plus aux êtres de lumière ; défait la lumière magique")),
    O("Forme lumineuse", src_idx="moonlight-ray", impact=(18, ["rayon", "lumineux"], "5d6 en moyenne de froid ; autant de plus aux fiélons et aux morts-vivants ; défait les ténèbres magiques"))]),
"crashing-wave": E2("Vague déferlante", P, ["vague"], 21, "6d6 en moyenne ; éteint les feux", comb="Eau", vr={}),
"cyclone-rondo": E2("Rondo du cyclone", P, ["tourbillon", "mélodie", "renversement"], 14, "renverse à son apparition ; 4d6 en moyenne à ceux qu'il traverse quand je le déplace", comb="Air", cond=["musique"]),
"elemental-annihilation-wave": E2("Vague d'anéantissement élémentaire", P, ["élément", "couleur", "poussée"], 14, "1d6 de feu + 3d6 en moyenne ; repousse", comb="Énergie pure"),
"gasping-marsh": E2("Miasme des marais", P, ["gaz", "invisible"], 14, "4d6 en moyenne ; la nappe se déplace quand je la soutiens"),
"glass-sand": E2("Sable de verre", P, ["verre", "éclat"], 14, "4d6 en moyenne, puis 1 à chaque instant", comb="Verre", comp=["sable"]),
"magnetic-acceleration": E2("Accélération magnétique", 3, ["métal", "projectile"], 21, "3d6 + 3d6 en moyenne : un clou ou une pièce lancés à toute vitesse", comb="Magnétisme"),
"pillar-of-water": P2("Pilier d'eau", EXI, P, ["eau", "colonne", "nage"], why="un cylindre d'eau douce immobile, où l'on nage", comb="Eau", vr={}, impact_sats=[(18, ["élévation", "mètres"]), (5, ["rayon", "mètres"])]),
"unseasonable-squall": E2("Bourrasque hors saison", P, ["vent", "dispersion", "renversement"], 7, "renverse ; au pire, projette à 9 m et meurtrit de 2d6 en moyenne", comb="Air", impact_sats=[(9, ["mètres"])]),
"wall-of-radiance": P2("Rideau astral", EXI, P, ["mur"], why="un mur mince, droit et vertical, tissé d'énergie astrale", forme=_MUR(18, 3), fam="A", sens=[("vue", None)], manif=["mur"], options=[
    O("Forme lumineuse", impact=(7, ["mur", "éblouissement", "lumineux"], "éblouit ceux qui le longent ; 2d6 en moyenne à qui le traverse")),
    O("Forme ténébreuse", src_idx="wall-of-shadow", impact=(P, ["mur", "obscurité", "ténébreux"], "la lumière ne passe pas ; sans voir dans le noir, on ne voit rien au travers"))]),
"wall-of-virtue": P2("Mur de vertu", EXI, P, ["mur", "lumineux"], 9, "1d8 + 1d8 en moyenne à qui le traverse ou s'y tient ; défait les ténèbres magiques", forme=_MUR(18, 3), sens=[("vue", None)], manif=["mur", "lumière"]),
"chromatic-ray": E2("Rayon chromatique", 3, ["rayon", "couleur", "hasard"], 30, "la couleur du rayon vient au hasard", fam="A", options=[
    O("Rouge", impact=(30, ["rayon", "hasard", "feu"], "30 de feu")), O("Orange", impact=(40, ["rayon", "hasard", "acide"], "40 d'acide")),
    O("Jaune", impact=(50, ["rayon", "hasard", "foudre"], "50 de foudre")), O("Vert", impact=(25, ["rayon", "hasard", "poison", "faiblesse"], "25 de poison, et la faiblesse une minute"))]),
"draw-the-lightning": E2("Foudre attirée", 3, ["éclair", "arme", "charge"], 20, "3d12 en moyenne", impact_plus=[(7, ["arme", "charge"], "1d12 en moyenne ajouté à mon premier coup de chaque instant")]),
"holy-cascade": E2("Cascade astrale", P, ["eau", "fiole"], 11, "3d6 en moyenne", comb="Eau", comp=["fiole", "eau"], consumed=True, vr={}, options=[
    O("Forme lumineuse", impact_plus=[(21, ["lumineux"], "6d6 en moyenne de plus aux morts-vivants et aux fiélons")]),
    O("Forme ténébreuse", impact_plus=[(21, ["ténébreux"], "6d6 en moyenne de plus aux êtres de lumière")])]),
"lifes-flowing-river": P2("Fleuve de la vie", EXI, P, ["fleuve", "lueur", "entrave"], 7, "un ruban de lumière : terrain pénible, renverse ; 2d6 en moyenne à l'esprit des morts-vivants", impact_sats=[(3, ["éclat", "mètres"])],
    sens=[("vue", None)], manif=["fleuve", "lueur"]),
"painful-vibrations": E2("Vibrations douloureuses", 3, ["os", "nausée", "surdité"], 28, "8d6 en moyenne", cond=["VIVANT"]),
"radiant-beam": E2("Rayon radieux", P, ["rayon", "lumineux", "éblouissement"], 28, "5d10 en moyenne ; éblouit ; défait les ténèbres magiques"),
"weapon-storm": E2("Tempête d'armes", P, ["arme", "multiplication"], 4, "mon arme se multiplie et frappe tous ceux de la zone, de 4 fois son dé", vr={}),
"acid-storm": E2("Tempête acide", P, ["pluie"], 14, "3d8 en moyenne à chaque instant"),
"blazing-fissure": E2("Fissure ardente", P, ["magma", "fissure", "chute"], 35, "4d6 + 6d6 en moyenne ; renverse", comb="Lave"),
"flowing-strike": P2("Frappe coulante", TP2, 1, ["vague", "course", "frappe"], 11, "une vague me porte sans que je prête le flanc ; mon coup est suivi de 2d10 en moyenne", comb="Eau", impact_sats=[(15, ["course", "mètres"])]),
"repelling-pulse": E2("Onde répulsive", P, ["force", "poussée"], 39, "7d10 en moyenne ; projetés au loin"),
"scouring-pulse": E2("Onde purificatrice", P, ["lumineux", "purification"], 27, "6d8 en moyenne aux morts-vivants", cond=["MORTVIVANT"], impact_plus=[(5, ["persistance", "lueur"], "1d8 en moyenne à chaque instant ; ceux qui brûlent ainsi luisent")]),
"shadow-blast": P2F("Déflagration astrale", NF, P, ["déflagration", "choix"], 23, "5d8 en moyenne, de la nature choisie, en cône, en éclat ou en ligne", vr={}),
"stormburst": E2("Éclat d'orage", P, ["éclair", "vent"], 21, "6d6 en moyenne"),
"flame-vortex": E2("Vortex de flammes", P, ["tourbillon", "feu", "vent"], 19, "3d4 + 3d6 en moyenne ; gêne le vol", comb="Feu", impact_sats=[(6, ["course", "mètres"])]),
"poltergeists-fury": E2("Fureur du poltergeist", P, ["objet", "orbite", "tempête"], 15, "6d4 en moyenne ; la tempête me suit et peut grandir", impact_sats=[(30, ["rayon", "mètres"])]),
"zero-gravity": P2("Apesanteur", NINT, P, ["pesanteur", "flottement"], why="plus de pesanteur : on flotte sur place, et l'on ne bouge qu'en prenant appui"),
"control-sand": E2("Maîtrise du sable", P, ["sable", "tourbillon", "éblouissement"], why="une tempête de sable autour de moi, qui éblouit", comb="Sable", options=[
    O("Bouclier de sable", impact=(21, ["sable", "tourbillon", "bouclier"], "un bouclier de sable qui encaisse 21 points")),
    O("Jet de sable", impact=(28, ["sable", "tourbillon", "jet"], "8d6 en moyenne à un être proche")),
    O("Tempête de sable", impact=(15, ["sable", "tourbillon", "tempête"], "6d4 en moyenne à tous ceux qu'elle englobe"))]),
"deitys-strike": E2("Frappe de l'arme céleste", 3, ["arme", "force"], 46, "7d12 en moyenne", impact_plus=[(18, ["onde", "ligne"], "5d6 en moyenne le long d'une onde de 9 m")]),
"frigid-flurry": E2("Rafale glaciale", P, ["éclat", "glace", "envol"], 63, "9d6 + 9d6 en moyenne aux ennemis ; le vent m'emporte au bout de la zone"),
"moonburst": E2("Éclat de lune", P, ["lune", "argent"], 44, "8d10 en moyenne", impact_plus=[(44, ["lumineux"], "8d10 en moyenne de plus aux morts-vivants")]),
"telekinetic-bombardment": E2("Bombardement télékinétique", P, ["projectile", "décombres"], 49, "14d6 en moyenne ; la zone encombrée"),
"volcanic-eruption": E2("Éruption volcanique", P, ["lave", "colonne", "gangue"], 49, "14d6 en moyenne ; la lave refroidie englue", comb="Lave", vr={}, impact_sats=[(3, ["lenteur", "mètres"])]),
"boil-blood": E2("Sang bouillant", 3, ["sang", "ébullition"], 55, "10d10 en moyenne", cond=["sang"]),
"deluge": E2("Déluge", P, ["trombe", "chute", "poussée", "mètres"], 15, "ceux qui volent chutent de 15 m ; ceux au sol sont emportés à 15 m du centre", comb="Eau"),
"falling-sky": E2("Ciel qui tombe", P, ["pression", "chute", "écrasement"], 60, "une pression écrase tout vers le bas : jusqu'à 60 pour qui volait"),
"punishing-winds": E2("Vents punitifs", P, ["cyclone", "rabat", "mètres"], 12, "ceux qui volent descendent de 12 m ; nul ne sort aisément du cyclone", comb="Air", vr={}),
"weapon-of-judgment": E2("Arme du jugement", 3, ["arme", "force", "jugement"], 17, "3d10 en moyenne à chaque frappe", vr={}, sens=[("vue", None)], manif=["arme"], options=[
    O("Guerre", impact=(17, ["arme", "force", "jugement", "guerre"], "3d10 en moyenne chaque instant où elle ne s'en prend pas à l'être désigné")),
    O("Paix", impact=(17, ["arme", "force", "jugement", "paix"], "3d10 en moyenne chaque fois qu'elle s'en prend à moi ou à mes alliés"))]),
"cataclysm": E2("Cataclysme", P, ["fléau", "fin"], 116, "sept fléaux à la fois, 3d10 en moyenne chacun : acide, séisme, froid, foudre, ouragan, raz-de-marée, brasier", comb="Énergie pure", vr={}),
}
FICHES.update(PF2_EVO)

# ----- Pathfinder 2, lot 8 : Nécromancie -----
PF2_ECARTE.update({"abyssal-plague": "nourrit les Abysses : écartée par décision", "ghoulish-cravings": "fièvre des goules, créature non admise", "leng-sting": "araignées de Leng, mythe étranger à Inarama",
 "linnorm-sting": "linnorm, dragon propre à Golarion", "spiritual-anamnesis": "suppose des vies antérieures", "summon-fluxwraith": "créature propre à une campagne",
 "summon-healing-servitor": "serviteur propre au monde de Golarion", "summoners-precaution": "n'agit que sur le lien avec l'eidolon"})
N2 = lambda fr, cible, words, v=None, why="", **kw: P2(fr, NE, cible, words, v, why, **kw)
_VIV = dict(cond=["VIVANT"])
FICHES.pop("moonburst"); PF2_FONDU["moonburst"] = "eclipse-burst"      # l'Éclat de lune est la forme lumineuse de l'Éclat d'éclipse
PF2_NEC = {
"goblin-pox": N2("Vérole urticante", 3, ["maladie", "éruption"], 1, "une éruption qui démange : nausée de 1, puis lenteur", vr={}),
"grim-tendrils": N2("Vrilles sinistres", P, ["vrille", "ténébreux"], 5, "2d4 en moyenne aux vivants, puis 1 à chaque instant", vr={}),
"necromancers-generosity": P2("Largesse du nécromancien", HE, 2, ["regain", "ténébreux"], 9, "1d8 + 4 en moyenne rendus à mon serviteur mort-vivant ; 2 ajouté contre l'énergie de vie", cond=["MORTVIVANT"], guerit=True),
"spider-sting": N2("Dard de l'araignée", 3, ["dard", "venin"], 2, "1d4 en moyenne, puis le venin de l'araignée", vr={}),
"spirit-link": P2("Lien spirituel", REL, 2, ["douleur", "transfert"], 2, "à chaque instant, il regagne 2 points que je perds", vr={}),
"blood-vendetta": N2("Vendetta de sang", 3, ["malédiction", "saignement"], 7, "2d6 en moyenne à chaque instant ; tant qu'elle saigne, 1 de plus à chaque coup de pointe ou de taille", cond=["blessure"], vr={}),
"feral-shades": N2("Meute d'ombres", P, ["brume", "meute", "ténébreux"], 10, "2d4 + 2d4 en moyenne ; plus féroce sur qui est à terre ou saigne"),
"fungal-hyphae": P2("Hyphes fongiques", VIS, 1, ["racine", "réseau", "vibration"], why="relié aux racines des plantes : je sens tout ce qui les touche, tant que je ne bouge pas", impact_sats=[(9, ["mètres"])]),
"grave-impressions": P2("Impressions de la tombe", VIS, 4, ["sens", "capteur"], why="voir et entendre par les yeux et les oreilles d'un cadavre, tant qu'on ne le déplace pas", cible_obj=["cadavre"], impact_sats=[(150, ["mètres"])]),
"imp-sting": N2("Dard du diablotin", 3, ["dard", "venin", "engourdissement"], 6, "1d4 + 1d6 en moyenne ; le venin engourdit"),
"inner-radiance-torrent": E2("Torrent de rayonnement intérieur", P, ["trait", "aveuglement"], 10, "4d4 en moyenne le long d'une ligne", impact_sats=[(18, ["ligne", "mètres"])]),
"mimic-undead": P2("Semblant de mort-vivant", NVIS, 1, ["mort", "pâleur", "leurre"], 4, "froid, livide, le cœur imperceptible : on me prend pour un mort-vivant ; 4 ajouté pour en jouer le rôle"),
"osseous-cage": P2("Cage d'os", V("mouvement", True), 3, ["os", "cage"], why="une prison d'os enferme ceux d'un petit espace ; il faut s'en extraire ou la briser", impact_sats=[(10, ["réserve"])], sens=[("vue", None)], manif=["os"]),
"reapers-lantern": P2("Lanterne du faucheur", NINT, P, ["lanterne", "soin", "fractionné"], 2, "près d'elle, les vivants ne reçoivent que la moitié des soins ; les morts-vivants sont affaiblis de 1", vr={}, sens=[("vue", None)], manif=["lanterne"]),
"slough-skin": P2("Mue continue", V("qualite"), 1, ["peau", "mue"], 2, "ma peau se renouvelle sans cesse : ce qui la ronge part plus vite ; 2 ajouté contre les poisons de contact"),
"sudden-blight": N2("Flétrissure soudaine", P, ["pourriture", "ténébreux"], 11, "2d10 en moyenne aux vivants ; les petites plantes pourrissent", vr={}),
"worms-repast": N2("Festin des vers", 3, ["ver", "chair"], 14, "4d6 en moyenne ; la douleur la laisse sans défense", impact_plus=[(4, ["persistance"], "1d6 en moyenne à chaque instant")]),
"bonewall-bulwark": P2("Rempart d'ossements", EXI, P, ["os", "rempart", "abri"], 17, "un mur d'os de 3 m sur 3, qui abrite ; ses membres frappent un voisin de 3d10 en moyenne à chaque instant", impact_sats=[(30, ["réserve"])],
    sens=[("vue", None)], manif=["ossements"]),
"claim-curse": P2("Malédiction endossée", V("flux"), 2, ["malédiction", "transfert"], why="sa malédiction passe sur moi, puis lui revient", impact_sats=[(5, ["minutes"])]),
"envenom-companion": P2("Compagnon venimeux", INT, 2, ["venin", "morsure"], 5, "1d8 en moyenne de poison à sa première morsure ou griffure de chaque instant", cond=["compagnon"]),
"life-connection": P2("Lien de vie", REL, 2, ["sauvegarde", "transfert"], why="je sens ses blessures à 1,6 km, arrondi à 2 ; une fois, je prends sur moi tout un coup qui lui était destiné", impact_sats=[(2, ["kilomètres"])], **_VIV),
"martyrs-intervention": P2("Intervention du martyr", SEP, 2, ["sacrifice", "transfert"], 1, "au lieu de tomber, il lui reste 1 point ; je prends le reste du coup, et nous en gardons tous deux la blessure", **_VIV),
"moths-supper": P2("Souper des phalènes", HE, 1, ["vie", "phalène", "sang"], 5, "2d4 en moyenne toutes les dix minutes ; 4d4 de plus au premier pansement ; je sens le sang frais et la chair pourrie", guerit=True,
    impact_sats=[(9, ["flair", "mètres"])], sens=[("vue", None)], manif=["phalènes"]),
"positive-attunement": P2("Accord à l'énergie de vie", HE, 4, ["vie", "accord"], 5, "1d8 en moyenne aussitôt, puis à chaque instant", guerit=True, impact_plus=[(5, ["lumineux"], "un mort-vivant en est blessé d'autant")]),
"rouse-skeletons": N2("Squelettes réveillés", P, ["squelette", "griffe"], 7, "2d6 en moyenne ; le sol encombré", vr={}, impact_sats=[(6, ["course", "mètres"])], sens=[("vue", None)], manif=["squelettes"]),
"shadow-spy": P2F("Espion astral", EXI, P, ["oiseau", "capteur", "mémoire"], why="un oiseau à demi réel va observer un lieu un jour durant ; revenu, il me livre tout ce qu'il a vu", comp=["sang", "terre"]),
"bloodspray-curse": N2("Malédiction du sang jaillissant", 3, ["malédiction", "hémorragie"], 7, "toute plaie de 10 ou plus saigne de 2d6 en moyenne en plus, puis d'autant à chaque instant", impact_sats=[(10, ["seuil"])], dur=(1, "MINUTES")),
"call-the-blood": N2("Appel du sang", 3, ["sang", "flot", "ténébreux"], 20, "8d4 en moyenne ; son sang coule jusqu'à ma bouche", **_VIV,
    impact_plus=[(P, ["nausée", "hâte"], "vivant, j'en ai la nausée ; mort-vivant, j'y gagne force d'emprunt ou vitesse")]),
"chroma-leach": N2("Sangsue de couleurs", 3, ["couleur", "faiblesse", "langueur"], 2, "affaiblie de 2 une minute, vidée de 1, prise de langueur", vr={}, **_VIV),
"cloak-of-light": P2("Manteau de lumière", HE, 1, ["vie", "halo"], 5, "2d4 en moyenne rendus aux vivants qui me côtoient", guerit=True, impact_plus=[(10, ["lumineux"], "4d4 en moyenne aux morts-vivants qui me côtoient")],
    impact_sats=[(9, ["éclat", "mètres"])], sens=[("vue", None)], manif=["halo"]),
"internal-insurrection": N2("Insurrection interne", 3, ["maladie", "révolte", "organe"], why="une maladie : des parties de son corps se rebellent contre le tout, jusqu'à la mort", cible_note=["corps"]),
"lifes-fresh-bloom": P2("Floraison de la vie", HE, P, ["vie", "floraison", "mètres"], 4, "1d6 en moyenne à chaque instant aux vivants, et 1,5 m de plus par instant", guerit=True, sens=[("vue", None)], manif=["fleurs"]),
"necrotic-radiation": N2("Rayonnement nécrotique", 4, ["imprégnation", "ténébreux"], 7, "2d6 en moyenne à qui finit son instant en portant l'objet, ou dans le lieu imprégné", cible_obj=["objet"]),
"pernicious-poltergeist": N2("Poltergeist pernicieux", P, ["esprit", "hantise", "ténébreux"], 22, "4d10 en moyenne à un être de la zone ; ou bien il effraie, ou il jette les objets"),
"sanguine-mist": N2("Brume sanguine", P, ["brume", "sang", "ténébreux"], 21, "6d6 en moyenne aux vivants", impact_plus=[(7, ["persistance", "drain"], "2d6 en moyenne à chaque instant ; j'en tire une vie d'emprunt")]),
"seal-fate": N2("Sort scellé", 3, ["malédiction", "mort", "désigné"], 2, "la forme de mort choisie la blesse de 2 de plus, et la tue si elle la terrasse", dur=(1, "MINUTES"), vr={}, **_VIV),
"soothing-spring": P2("Source apaisante", HE, P, ["vie", "source", "bain"], 45, "10d8 en moyenne à qui s'y baigne une heure ; la fatigue s'efface", guerit=True, sens=[("vue", None)], manif=["bassin", "vapeur"]),
"swarming-wasp-stings": N2("Nuée de dards", P, ["dard", "venin"], 4, "1d6 en moyenne, puis le venin"),
"vampiric-maiden": N2("Vierge de fer vampirique", 3, ["cercueil", "pointe", "ténébreux"], 20, "4d4 + 4d4 en moyenne ; enfermée un instant ; j'en tire une vie d'emprunt", impact_sats=[(10, ["vie", "temporaire"])], vr={},
    sens=[("vue", None)], manif=["cercueil", "spectre"]),
"vital-beacon": P2("Phare vital", HE, 1, ["vie", "phare"], 22, "4d10 en moyenne au premier qui me touche, puis de moins en moins, 4 fois en tout", guerit=True, vr={}),
"blister": N2("Cloque", 3, ["cloque", "éclatement"], 25, "7d6 en moyenne par cloque crevée, à elle et à ceux d'un cône de 4,5 m", impact_sats=[(2, ["cloques"])], vr={}),
"blood-feast": N2("Festin de sang", 3, ["gueule", "sang"], 42, "12d6 en moyenne ; je gagne en vie d'emprunt la moitié de ce qu'elle perd", impact_sats=[(21, ["vie", "temporaire"])]),
"ectoplasmic-expulsion": P2("Expulsion ectoplasmique", DISP, 2, ["emprise", "possession", "ectoplasme"], 2, "défait une emprise sur son esprit ; sinon, 2 ajouté pour s'en libérer, une heure durant", cible_note=["psyché"]),
"healing-well": P2("Puits de guérison", HE, P, ["vie", "puits"], 18, "4d8 en moyenne à qui y puise, 5 fois en tout", guerit=True, impact_sats=[(5, ["usage"])], sens=[("vue", None)], manif=["disque", "lueur"]),
"invoke-spirits": N2("Appel des esprits", P, ["spectre", "effroi", "ténébreux"], 10, "2d4 + 2d4 en moyenne aux vivants ; au pire, l'effroi et la fuite", vr={}, sens=[("vue", None)], manif=["spectres"]),
"mariners-curse": N2("Malédiction du marin", 3, ["malédiction", "mer", "nausée"], 1, "nausée de 1 qui ne passe pas ; en mer, loin des côtes, ralentie de 1", dur=(P, None), vr={}),
"ravening-maw": N2("Gueule vorace", 3, ["faim", "dévoration"], 13, "5d4 en moyenne ; prise d'une faim cannibale, elle peut dévorer un mourant ou un mort pour se refaire", **_VIV, **_PSY),
"rip-the-spirit": N2("Esprit arraché", 3, ["âme", "arrachement", "ténébreux"], 18, "5d6 en moyenne ; vidée de 1", **_VIV),
"wall-of-flesh": P2("Mur de chair", EXI, P, ["chair", "mur"], why="un mur de chair vivante, que l'on soigne ; il mord, saisit ou observe, selon le choix", forme=_MUR(9, 6), impact_sats=[(75, ["réserve"])], vr={},
    sens=[("vue", None)], manif=["chair"]),
"wyvern-sting": N2("Dard de la vouivre", 3, ["dard", "venin"], 8, "3d4 en moyenne, puis le venin de la vouivre"),
"awaken-entropy": N2("Éveil de l'entropie", P, ["temps", "usure", "délabrement"], 28, "8d6 en moyenne à qui y entre ou y commence son instant ; la zone s'aggrave quand je la soutiens"),
"field-of-life": P2("Champ de vie", HE, P, ["vie", "champ"], 5, "1d8 en moyenne à chaque instant aux vivants", guerit=True, impact_plus=[(5, ["lumineux"], "1d8 en moyenne aux morts-vivants")], vr={}),
"gray-shadow": P2F("Ombre du mourant", INV, 9, ["ombre", "agonie", "service"], 5, "l'ombre d'un mourant me sert tant qu'il agonise ; sa main empoisonne de 1d8 en moyenne", cond=["mourant"]),
"necrotize": N2("Nécrose", 3, ["putréfaction", "ténébreux", "infirmité"], 42, "12d6 en moyenne, et une infirmité au hasard : os fragiles, jointures gauches, jambes lentes", dur=(1, "MINUTES"), **_VIV),
"purple-worm-sting": N2("Dard du ver pourpre", 3, ["dard", "venin"], 11, "3d6 en moyenne, puis le venin du ver pourpre"),
"spirit-blast": N2("Déflagration spirituelle", 3, ["âme", "force"], 56, "16d6 en moyenne : frappe l'esprit même, fût-il projeté ou logé dans un autre corps", vr={}),
"vampiric-exsanguination": N2("Exsanguination vampirique", P, ["sang", "drain", "ténébreux"], 42, "12d6 en moyenne aux vivants ; j'en tire une vie d'emprunt", impact_sats=[(21, ["vie", "temporaire"])], vr={}),
"eclipse-burst": N2("Éclat astral glacé", P, ["globe", "froid"], 44, "8d10 en moyenne de froid", options=[
    O("Forme ténébreuse", impact_plus=[(20, ["ténébreux"], "8d4 en moyenne de plus aux vivants ; défait la lumière magique")]),
    O("Forme lumineuse", src_idx="moonburst", impact_plus=[(44, ["lumineux"], "8d10 en moyenne de plus aux morts-vivants ; ce froid vaut l'argent")])]),
"tempest-of-shades": N2("Tempête d'esprits", P, ["tornade", "spectre", "effroi"], 3, "une tornade de visages hurlants : effrayés de 3, parfois mis en fuite", impact_sats=[(18, ["mètres"])], **_PSY, sens=[("vue", None), ("ouïe", None)], manif=["tornade", "visages"]),
"all-is-one-one-is-all": P2("Tous en un", V("identite"), 2, ["fusion", "partage", "échange"], why="fondus un instant puis rendus à eux-mêmes : leurs places échangées et leur vitalité répartie à mon gré", qty_cible=10, **_VIV),
"devour-life": N2("Vie dévorée", 3, ["dévoration", "ténébreux"], 60, "60 ; si elle tombe, elle meurt ; je guéris de la moitié", impact_sats=[(30, ["regain"])], **_VIV),
"divine-armageddon": N2("Armageddon", P, ["cataclysme", "ténébreux"], 70, "10d6 + 10d6 en moyenne : vivants et morts-vivants sont détruits ensemble"),
"moment-of-renewal": P2("Instant de renouveau", HE, 2, ["vie", "repos"], why="un jour entier de repos en un instant : ils guérissent d'autant, et les maux d'un jour s'effacent", qty_cible=6, guerit=True, vr={}),
"spirit-song": N2("Chant spirituel", P, ["chant", "âme", "force"], 63, "18d6 en moyenne", vr={}),
"spiritual-epidemic": N2("Épidémie spirituelle", 3, ["malédiction", "contagion"], 2, "affaiblie et stupéfiée de 2 une minute, puis de 1 pour toujours ; qui lui lance un sort de foi ou d'occulte s'expose au même mal", dur=(P, None), vr={}, **_PSY),
"voracious-gestalt": N2("Gestalt vorace", P, ["esprit", "dévoration", "ténébreux"], 49, "14d6 en moyenne aux vivants choisis", impact_plus=[(21, ["persistance", "croissance"], "6d6 en moyenne à chaque instant ; chaque âme prise le fait grandir")]),
"revival": P2("Renouveau", HE, 2, ["vie", "rappel"], 85, "10d8 + 40 en moyenne aux vivants ; les morts récents se relèvent le temps du sort, sur une vie d'emprunt", guerit=True, vr={}),
}
FICHES.update(PF2_NEC)

# ----- Pathfinder 2, lot 9 : Transmutation -----
PF2_ECARTE.update({"avatar": "n'existe que par une divinité", "daemon-form": "daémons d'Abaddon, propres à Golarion", "dinosaur-form": "les dinosaures n'existent pas dans Inarama",
 "nature-incarnate": "homme vert et kaiju n'existent pas dans Inarama", "ooze-form": "pas de vases dans Inarama", "summoners-visage": "n'agit que sur l'eidolon"})
PF2_FONDU.update({"demon-form": "angel-form", "devil-form": "angel-form"})       # une seule « Forme astrale », à deux faces
PF2_TRA = {
"gouging-claw": N2("Griffe lacérante", 3, ["griffe", "membre"], 4, "ma main devient griffe : 1d6 en moyenne, en taille ou en pointe", vr={}),
"healing-plaster": P2("Emplâtre de soin", TR, 4, ["boue", "emplâtre", "pansement"], why="une poignée de terre ou de boue devient un emplâtre qui tient lieu de trousse de soins", cible_obj=["objet"]),
"juvenile-companion": P2("Compagnon juvénile", TR, 2, ["petit", "jeunesse", "inoffensif"], 5, "mon compagnon redevient petit : minuscule, moitié moins rapide, d'allure inoffensive ; les coups le blessent de 5 de plus", cond=["compagnon"]),
"nettleskin": P2("Peau d'ortie", TR, 1, ["épine", "riposte"], 2, "qui me frappe de près se pique : 1d4 en moyenne", sens=[("vue", None)], manif=["épines"]),
"quick-sort": P2("Tri rapide", ORD, 4, ["tri", "pile"], why="de petits objets se rangent d'eux-mêmes en piles, par couleur, par forme ou dans l'ordre", cible_obj=["objet"], qty_cible=200),
"restyle": P2("Retouche", TR, 4, ["habit", "couleur", "motif"], why="la couleur, la texture et le motif d'un vêtement changés pour de bon", cible_obj=["objet"]),
"swampcall": P2("Appel du marais", TR, P, ["boue", "enlisement", "mètres"], 3, "le sol devient bourbier : terrain pénible ; ceux qui s'enfoncent perdent 3 m par instant"),
"verminous-lure": P2("Leurre à vermine", ATT, 4, ["musc", "vermine", "attirance"], why="un musc attire sur la cible les petites bêtes et les nuées"),
"clawsong": P2("Chant des griffes", INT, 2, ["griffe", "chant"], 4, "ses griffes frappent de 1d6 en moyenne, en taille ou en pointe ; un cran de plus si elles valaient déjà cela", cond=["griffe"]),
"dismantle": P2("Démontage", V("identite", True), 4, ["pièce", "démontage"], why="l'objet se défait en ses pièces, assez petites pour être cachées ; il se remonte à la fin du sort", cible_obj=["objet"], vr={}),
"enhance-victuals": P2("Mets rehaussés", V("qualite"), 4, ["festin", "vin", "poison"], why="l'eau devient vin, les vivres un festin ; les poisons qui s'y trouvaient sont défaits", cible_obj=["nourriture"]),
"iron-gut": P2("Estomac de fer", TR, 1, ["gorge", "estomac", "cache"], why="gorge et estomac élastiques, plus durs que le métal : j'y range un petit objet"),
"loose-times-arrow": P2("Flèche du temps", INT, 2, ["temps", "hâte", "pas"], why="un déplacement de plus dans l'instant", qty_cible=6),
"rapid-adaptation": P2("Adaptation rapide", TR, 2, ["milieu", "adaptation"], why="mon compagnon prend l'adaptation du milieu où il se trouve : nage, froid, chaleur, flair, escalade ou course", cond=["compagnon"]),
"consecrate-flesh": P2("Chair consacrée", TR, 1, ["chair", "riposte"], 4, "1d6 en moyenne à qui me touche ou me frappe de près", options=[
    O("Forme lumineuse", impact=(4, ["chair", "riposte", "lumineux"], "1d6 en moyenne à qui me touche ou me frappe de près ; mes coups 1 de plus, mes soins 1d4 de plus ; la face ténébreuse me blesse de 5 de plus")),
    O("Forme ténébreuse", impact=(4, ["chair", "riposte", "ténébreux"], "1d6 en moyenne à qui me touche ou me frappe de près ; mes coups 1 de plus, mes flétrissures 1d4 de plus ; la face lumineuse me blesse de 5 de plus"))]),
"curse-of-lost-time": N2("Malédiction du temps perdu", 4, ["malédiction", "vieillissement", "érosion"], 14, "4d6 en moyenne à un objet ou une créature d'artifice, qu'on ne peut plus réparer ; un vivant vieilli est gauche et faible",
    dur=(1, "HEURES"), vr={}),
"days-weight": N2("Poids du jour", 3, ["temps", "fatigue", "faiblesse"], 1, "le poids d'une journée entière : fatiguée et affaiblie de 1", **_VIV),
"dividing-trench": P2("Tranchée", TR, P, ["tranchée", "abri"], why="une tranchée dans la terre meuble, large et profonde de 1,5 m, longue de 4,5 m : elle abrite"),
"earthbind": P2("Entrave terrestre", V("mouvement", True), 3, ["pesanteur", "chute", "sol"], why="elle descend sans mal et ne peut plus quitter le sol d'un instant", cond=["envol"], impact_sats=[(36, ["chute", "mètres"])], vr={}),
"feet-to-fins": P2("Pieds palmés", TR, 2, ["nageoire", "nage"], why="ses pieds deviennent nageoires : il nage aussi vite qu'il marchait, mais ne fait plus que 1,5 m par instant à terre", vr={}),
"ghostly-weapon": P2("Arme spectrale", TR, 4, ["spectre", "intangible"], why="l'arme, translucide, frappe aussi bien les êtres sans corps", cible_obj=["arme"], vr={}),
"lashing-rope": P2("Corde cinglante", V("mouvement"), 4, ["fouet", "croc-en-jambe"], 7, "une corde s'anime autour de moi et cingle à distance : 2d6 en moyenne, et fait tomber", cible_obj=["corde"]),
"time-jump": P2("Saut dans le temps", TP2, 1, ["temps", "déplacement"], why="deux déplacements hors du temps : aux yeux de tous, je parais ailleurs d'un coup ; recommencer trop tôt stupéfie"),
"time-pocket": P2("Poche de temps", TP2, 4, ["temps", "avenir", "retour"], why="un objet envoyé un jour en avant : il reparaît entre les mains de son porteur", cible_obj=["objet"]),
"bestial-curse": P2("Malédiction bestiale", TR, 3, ["malédiction", "bête", "argent"], 1, "sous des traits de bête : gauche de 1, l'argent la blesse de 1 de plus, ses mains la trahissent une fois sur cinq",
    cond=["humanoïde", "VIVANT"], dur=(1, "HEURES"), vr={}),
"elemental-gift": P2("Don élémentaire", INT, 2, ["élément", "don"], why="la force d'un élément emplit l'allié", fam="A", options=[
    O("Air", impact=(9, ["don", "air", "vitesse", "mètres"], "9 m de plus par instant, et le vol")),
    O("Terre", impact=(2, ["don", "terre", "aplomb"], "2 ajouté pour rester debout ; le sol alentour gêne les autres")),
    O("Feu", impact=(4, ["don", "feu", "persistance"], "ses coups brûlent de 1d6 en moyenne à chaque instant")),
    O("Métal", impact=(2, ["don", "acier", "foudre"], "ses coups de métal frappent de 1d4 en moyenne de foudre en plus ; 1 ajouté contre qui porte du métal")),
    O("Eau", impact=(5, ["don", "eau", "nage"], "5 retranché au feu reçu ; il nage comme il marche")),
    O("Bois", impact=(4, ["don", "bois", "sève"], "une vie d'emprunt égale au cran du sort, renouvelée de moitié à chaque instant"))]),
"morass-of-ages": P2("Bourbier des âges", NINT, P, ["temps", "lenteur"], why="le temps s'étire autour de moi : terrain pénible, lenteur, parfois l'immobilité ; la zone peut grandir", impact_sats=[(18, ["rayon", "mètres"])]),
"tortoise-and-the-hare": P2("Le lièvre et la tortue", V("flux"), 3, ["allure", "transfert"], 1, "l'ennemi ralenti de 1 ; sa vitesse passe à un allié, hâté un instant", impact_sats=[(3, ["instants"])]),
"variable-gravity": P2("Pesanteur variable", INT, 1, ["pesanteur", "réglage"], 2, "légère : je saute deux fois plus loin et tombe sans mal ; lourde : 2 ajouté pour ne pas être déplacé, mais chargé"),
"aberrant-form": P2("Forme d'aberration", TR, 1, ["forme", "aberration"], why="une grande aberration de combat : pinces, tentacules ou gueule, selon la forme choisie"),
"blackfingerss-blades": P2("Lames venimeuses", INT, 4, ["venin", "scorpion"], why="des armes enduites de venin de scorpion géant, pour un coup chacune", cible_obj=["arme"], qty_cible=4),
"desperate-repair": P2("Réparation désespérée", V("nature", True), 4, ["soudure", "sursis"], 1, "le bouclier qui allait être détruit tient à 1 point", cible_obj=["bouclier"]),
"grisly-growths": N2("Excroissances macabres", 3, ["membre", "organe", "éruption"], 35, "10d6 en moyenne ; la nausée pour elle et pour qui la regarde", vr={}),
"mantle-of-the-frozen-heart": P2("Manteau du cœur gelé", TR, 1, ["glace", "manteau"], why="peau et armure deviennent glace bleue ; deux dons à la fois", comb="Glace", options=[
    O("Glace protectrice", impact=(10, ["glace", "manteau", "rempart"], "10 retranché au froid reçu")),
    O("Cœur de glace", impact=(7, ["glace", "manteau", "riposte"], "2d6 en moyenne à qui me touche ou me frappe de près")),
    O("Glissade", impact=(6, ["glace", "manteau", "vitesse", "mètres"], "6 m de plus par instant sur sol lisse ; la glace ne me gêne plus")),
    O("Griffes de glace", impact=(11, ["glace", "manteau", "griffe"], "1d6 + 2d6 en moyenne ; je grimpe comme je marche"))]),
"mantle-of-the-magma-heart": P2("Manteau du cœur de magma", TR, 1, ["lave", "manteau"], why="peau et habits deviennent lave ardente ; deux dons à la fois", comb="Lave", options=[
    O("Éruption", impact=(2, ["lave", "manteau", "croissance"], "je grandis d'une taille : gauche, mais j'atteins plus loin et frappe de 2 de plus")),
    O("Poigne ardente", impact=(12, ["lave", "manteau", "poing"], "1d8 + 2d6 en moyenne, et la brûlure qui dure")),
    O("Cœur de feu", impact=(7, ["lave", "manteau", "riposte"], "2d6 en moyenne à qui me touche ou me frappe de près")),
    O("Flammes tièdes", impact=(5, ["lave", "manteau", "rempart"], "5 retranché au froid et au feu reçus"))]),
"moon-frenzy": P2("Frénésie lunaire", TR, 2, ["croc", "griffe", "sauvagerie"], 9, "crocs de 2d8 en moyenne, griffes de 2d6 ; l'argent les blesse de 5 de plus", qty_cible=5,
    impact_sats=[(5, ["vie", "temporaire"]), (3, ["vitesse", "mètres"])], vr={}),
"natures-reprisal": P2("Représailles de la nature", TR, P, ["plante", "fouet", "entrave"], 6, "pour mes ennemis : terrain pénible, et 6 de poison à chaque pas dans les fourrés", fam="A"),
"quicken-time": P2("Temps hâté", INT, P, ["temps", "hâte", "flou"], why="le temps s'y emballe : un déplacement ou un coup de plus par instant ; on y voit flou, du dehors comme du dedans"),
"rewinding-step": P2("Pas à rebours", TP2, 1, ["temps", "ancre", "retour"], why="une ancre dans le temps : d'un geste, je reviens à l'endroit où je l'ai posée", impact_sats=[(150, ["mètres"])]),
"stagnate-time": P2("Temps stagnant", NINT, P, ["temps", "lenteur"], why="le temps s'y épaissit : qui y commence son instant peut être ralenti"),
"angel-form": P2("Forme astrale", TR, 1, ["forme", "astral"], why="une forme de combat tissée d'énergie astrale", options=[
    O("Forme lumineuse", impact=(P, ["forme", "ange", "lumineux"], "un être de lumière, ailé, aux armes qui brûlent les fiélons")),
    O("Forme ténébreuse", src_idx="demon-form", impact=(P, ["forme", "fiélon", "ténébreux"], "un fiélon, démon ou diable, aux armes qui brûlent les êtres de lumière"))]),
"corrosive-body": P2("Corps corrosif", TR, 1, ["acide", "corps", "riposte"], 11, "immunisé à l'acide ; 3d6 en moyenne à qui me touche ou me frappe de près ; mes coups 1d4 de plus", impact_sats=[(11, ["vie", "temporaire"])]),
"cosmic-form": P2("Forme cosmique", TR, 1, ["forme", "astre"], why="un grand corps d'énergie cosmique, qui vole", fam="A", impact_sats=[(20, ["vie", "temporaire"])], options=[
    O("Lune", impact=(15, ["forme", "astre", "lune", "argent"], "2d4 + 10 en moyenne ; ses coups valent l'argent et stupéfient")),
    O("Soleil", impact=(17, ["forme", "astre", "soleil", "feu"], "2d6 + 10 en moyenne de feu, qui brûle encore ensuite ; éblouit"))]),
"one-with-the-land": P2("Uni à la terre", ID, 1, ["fusion", "terrain", "vengeance"], 33, "fondu dans le sol ou un grand arbre : abrité, je sens tout alentour et le terrain frappe pour moi de 5d12 en moyenne",
    impact_sats=[(60, ["frémissement", "mètres"]), (18, ["frappe", "mètres"])]),
"element-embodied": P2("Élément incarné", TR, 1, ["forme", "élémentaire", "colosse"], why="un élémentaire colossal", fam="A", impact_sats=[(30, ["vie", "temporaire"])], options=[
    O(n, impact=(P, ["forme", "élémentaire", "colosse", w], f"un élémentaire colossal de l'élément choisi")) for n, w in _ELEM6[:4]]),
"primal-herd": P2("Harde primordiale", TR, 2, ["forme", "mammouth", "harde"], why="six êtres deviennent une harde de mammouths", qty_cible=6, niveau=9),
}
FICHES.update(PF2_TRA)

# ----- Pathfinder 2 : reprises du 15 novembre (décisions de Baptiste) -----
def _R(k, **kw): FICHES[k].update(kw)
_R("goblin-pox", fr="Vérole gobeline")          # les gobelins existent dans Inarama
# Zones données seulement dans le texte de la source
_S = lambda n: {"type": "sphere", "size": n}
_R("gale-blast", aoe=_S(5)); _R("blazing-dive", aoe=_S(10)); _R("tempest-of-shades", aoe=_S(60))
_R("pillar-of-water", aoe={"type": "cylinder", "size": 15, "height": 60}, impact_sats=[])
_R("sea-surge", aoe={"type": "line", "size": 60}); _R("lifes-flowing-river", aoe={"type": "line", "size": 120}); _R("dividing-trench", aoe={"type": "line", "size": 15})
_R("redistribute-potential", aoe={"type": "cube", "size": 5}, qty=2)
_R("burning-blossoms", impact_sats=[])
# Sorts dont l'ampleur dépend du temps mis à les lancer : la forme de base et la forme maximale
_R("shadow-blast", aoe={"type": "cone", "size": 30})
_R("concordant-choir", options=[
    O("Forme de base", impact=(2, ["son", "consonance"], "1d4 en moyenne à un seul ennemi, d'un mot")),
    O("Forme maximale", cible=P, aoe=_S(30), impact=(5, ["son", "consonance"], "2d4 en moyenne à tous ceux qui m'entourent ; tout l'instant y passe"))])
_R("kinetic-ram", options=[
    O("Forme de base", loc=(5, "METRES", "4,5 m, arrondi à 5"), impact=(3, ["poussée", "mètres"], "une cible proche repoussée de 3 m, d'un geste")),
    O("Forme maximale", cible=P, aoe=_S(5), impact=(3, ["poussée", "mètres"], "tous ceux qui m'entourent repoussés de 3 m ; tout l'instant y passe"))])
_R("gravitational-pull", options=[
    O("Forme de base", impact=(3, ["pesanteur", "traction", "mètres"], "une cible tirée de 3 m vers moi, d'un geste")),
    O("Forme maximale", qty_cible=5, impact=(3, ["pesanteur", "traction", "mètres"], "cinq cibles tirées de 3 m vers moi ; tout l'instant y passe"))])
_R("elemental-annihilation-wave", options=[
    O("Forme de base", impact=(14, ["élément", "couleur", "poussée"], "1d6 de feu + 3d6 en moyenne ; repousse")),
    O("Forme maximale", aoe={"type": "cone", "size": 60}, impact=(14, ["élément", "couleur", "poussée"], "1d6 de feu + 3d6 en moyenne ; repousse ; deux instants de préparation"),
      impact_plus=[(P, ["vent", "persistance"], "les éléments s'attardent un instant dans le cône : un vent violent en interdit l'approche")])])
_R("rip-the-spirit", options=[
    O("Forme de base", impact=(18, ["âme", "arrachement", "ténébreux"], "5d6 en moyenne à un vivant, d'un geste ; vidé de 1")),
    O("Forme maximale", cible=P, aoe=_S(30), impact=(18, ["âme", "arrachement", "ténébreux"], "5d6 en moyenne à tous les vivants qui m'entourent ; vidés de 1 ; tout l'instant y passe"))])
_R("inner-radiance-torrent", impact_sats=[], options=[
    O("Forme de base", aoe={"type": "line", "size": 60}, impact=(10, ["trait", "aveuglement"], "4d4 en moyenne le long de la ligne")),
    O("Forme maximale", aoe={"type": "line", "size": 120}, impact=(20, ["trait", "aveuglement"], "8d4 en moyenne le long d'une ligne double ; deux instants de préparation"),
      impact_plus=[(1, ["éclat", "halo"], "je rayonne ensuite une minute : 1 à qui finit son instant contre moi")])])
# Formes de combat : la robustesse et l'attaque principale, lues dans la source
_R("aberrant-form", impact=(21, ["forme", "aberration"], "une grande aberration : sa meilleure attaque frappe de 2d12 + 8 en moyenne ; elle saisit"), impact_sats=[(13, ["vie", "temporaire"])])
_R("angel-form", options=[
    O("Forme lumineuse", impact=(27, ["forme", "ange", "lumineux"], "un être de lumière, ailé : 2d6 + 12 et 2d6 de feu et de lumière en moyenne ; la face ténébreuse le blesse de 10 de plus"), impact_sats=[(40, ["vie", "temporaire"])]),
    O("Forme ténébreuse", src_idx="demon-form", impact=(23, ["forme", "fiélon", "ténébreux"], "un fiélon, démon ou diable : 2d8 + 10 et 1d6 de ténèbres en moyenne ; la face lumineuse le blesse de 5 de plus"), impact_sats=[(30, ["vie", "temporaire"])])])
_R("primal-herd", impact=(37, ["forme", "mammouth", "harde"], "une harde de mammouths : défenses de 4d8 + 19 en moyenne ; ils piétinent"), impact_sats=[(20, ["vie", "temporaire"])])

# ----- Pathfinder 2, lot 10 : sorts propres à la version remaniée (Abjuration, Divination, Enchantement, Illusion, Nécromancie) -----
PF2_ECARTE.update({"recall-legacy": "accorde un don d'ascendance : pure mécanique de jeu"})
PR = lambda fr, verb, cible, words, v=None, why="", **kw: {**P2(fr, verb, cible, words, v, why, **kw), "src": "pf2r"}
_RES = dict(cible_note=["résistance"])
PF2_REM1 = {
"buoyant-bubbles": PR("Bulles flottantes", SEP, 2, ["bulle", "flottaison"], why="une écume la fait flotter : elle ne coule plus, et remonte en un instant si elle coulait"),
"burrow-ward": PR("Garde contre les fouisseurs", SEP, P, ["terre", "durcissement", "fouisseur"], why="la terre durcit autour de moi : on n'y creuse plus, et ce qui s'y trouvait en est chassé", fam="A"),
"cleanse-air": PR("Air purifié", V("qualite"), P, ["air", "poison", "pureté"], why="l'air de la zone redevient sain et le reste", fam="A"),
"cloud-dragons-cloak": PR("Manteau de brume", NVIS, 2, ["brume", "dérobade"], why="une brume la dérobe au coup qui la vise, puis aux tirs, un instant", cond=["coup"]),
"defended-by-spirits": PR("Défendu par les esprits", SEP, 2, ["esprit", "riposte"], 4, "chaque fois que l'ennemi désigné blesse l'allié, les esprits le frappent de 1d6 en moyenne", cible_note=["garde"]),
"eat-fire": PR("Avaleur de feu", SEP, 1, ["feu", "fumée"], 5, "5 retranché au feu reçu ; la fumée recrachée ensuite fait écran", fam="A", **_RES),
"entwined-roots": PR("Racines entrelacées", SEP, 2, ["bois", "racine", "rempart"], 5, "5 retranché aux chocs et aux pointes ; les racines attrapent les projectiles manqués", qty_cible=5, fam="A", **_RES, **_VIV),
"fireproof": PR("Ignifugation", SEP, 4, ["feu", "isolant"], 10, "10 retranché au feu ; l'objet ne conduit plus la chaleur et ne s'enflamme plus", cible_obj=["objet"], fam="A"),
"glass-shield": PR("Bouclier de verre", SEP, 1, ["verre", "bouclier"], 2, "arrête 2 points par coup ; brisé, ses éclats blessent de 1d4 en moyenne", cible_note=["garde"], fam="A"),
"interposing-earth": PR("Terre interposée", SEP, 1, ["terre", "muret", "abri"], why="un muret de terre surgit entre moi et le danger et m'abrite", cond=["coup"], fam="A"),
"phoenix-ward": PR("Garde du phénix", SEP, 1, ["feu", "phénix", "renaissance"], 10, "10 retranché au feu ; un feu mortel me laisse à 1 point, puis la garde me rend 4d8 en moyenne et s'éteint", fam="A", **_RES,
    impact_sats=[(18, ["regain"])], sens=[("vue", None)], manif=["ailes", "flammes"]),
"radiant-globe": PR("Globe radieux", SEP, P, ["dôme", "lumière", "projectile"], why="un dôme de lumière détruit flèches et carreaux qui le traversent, dans les deux sens", sens=[("vue", None)], manif=["dôme"]),
"rigid-form": PR("Forme rigide", V("nature", True), 1, ["bois", "rigidité", "métamorphose"], why="je peux défaire toute métamorphose hostile qui me vise", fam="A"),
"spirit-ward": PR("Garde contre les esprits", SEP, 2, ["esprit", "hantise"], 1, "1 ajouté contre les esprits et les hantises", **_RES),
"tempest-cloak": PR("Manteau de tempête", SEP, 2, ["vent", "manteau"], 2, "2 ajouté à sa défense contre les tirs ; les vents gênent l'approche", cible_note=["garde"], sens=[("ouïe", None)], manif=["vent"]),
"thief-of-fortune": PR("Voleur de fortune", V("flux"), 4, ["bienfait", "partage"], why="je m'approprie le bienfait d'un sort qui agit sur un autre, sans le lui ôter", cible_note=["sort"]),
"veil-of-spirits": PR("Voile d'esprits", EXI, P, ["brume", "esprit", "éblouissement"], why="un voile d'esprits éblouit ceux qui s'y tiennent et les livre aux coups portés à l'âme", sens=[("vue", None)], manif=["brume"]),
"elemental-sense": PR("Sens élémentaire", INT, 1, ["sens", "élément"], why="un sens prêté par un élément", fam="A", options=[
    O("Eau", impact=(P, ["sens", "eau", "écho"], "sous l'eau, l'ouïe vaut la vue")),
    O("Feu", impact=(9, ["sens", "feu", "chaleur", "mètres"], "je sens les corps chauds à 9 m")),
    O("Métal", impact=(9, ["sens", "acier", "aimant", "mètres"], "je sens qui porte du métal à 9 m, et je sais où est le nord")),
    O("Air", impact=(P, ["sens", "air", "invisible"], "je devine les formes invisibles")),
    O("Terre", impact=(P, ["sens", "terre", "vibration"], "je sens ce qui bouge sur le même sol"))]),
"engrave-memory": PR("Mémoire gravée", ORD, 4, ["souvenir", "pierre", "mot"], why="des souvenirs gardés dans une pierre, livrés à qui dit le mot ; la pierre s'effrite alors", cible_obj=["objet"], impact_sats=[(10, ["minutes"])]),
"heatvision": PR("Vision de la chaleur", VIS, 2, ["chaleur", "regard", "mètres"], 18, "voit la chaleur à 18 m, à travers fumée et ténèbres"),
"mental-map": PR("Carte mentale", VIS, 4, ["lieu", "souvenir"], 2, "le souvenir d'un lieu tiré de son esprit : 2 ajouté pour m'y orienter", cible_note=["mémoire"]),
"mimic-spell": PR("Sort imité", V("flux"), 4, ["imitation", "contre"], why="je contre le sort qu'on lance ; si j'y parviens, je le relance moi-même à l'instant suivant", cible_note=["sort"], cond=["sort"]),
"misty-memory": PR("Mémoire de l'eau", VIS, P, ["eau", "brume", "passé", "heures"], 24, "une brume monte de l'eau et rejoue ce qui s'est passé là, jusqu'à 24 heures plus tôt", sens=[("vue", None)], manif=["brume"]),
"primal-chorus": PR("Chœur sauvage", VIS, P, ["hurlement", "bête", "nombre"], 1, "les bêtes d'alentour répondent : j'en sais à peu près le nombre ; 1 ajouté à ma prochaine entrée en lice", sens=[("ouïe", None)], manif=["hurlement"]),
"root-reading": PR("Lecture des racines", VIS, P, ["racine", "présence"], 1, "les grandes créatures inaperçues me sont révélées ; 1 ajouté pour les trouver"),
"scrying-ripple": PR("Onde de scrutation", VIS, 4, ["courant", "capteur"], why="je vois et j'entends depuis une eau courante des alentours", cible_obj=["eau"], impact_sats=[(150, ["mètres"])]),
"the-parrots-whisper": PR("Murmure du perroquet", VIS, 3, ["perroquet", "faille", "bavardage"], why="un perroquet spectral me dit sa plus grande faiblesse, puis bavarde encore un instant"),
"tremor-signs": PR("Signes par le sol", REL, 2, ["vibration", "message"], why="une courte phrase portée par le sol jusqu'à elle, sans la voir ; elle peut répondre"),
"tremorsense": PR("Perception des vibrations", VIS, 1, ["vibration", "sol", "mètres"], 9, "je sens à 9 m ce qui bouge sur le même sol"),
"voice-on-the-breeze": PR("Voix sur la brise", REL, P, ["vent", "murmure", "message"], why="un murmure porté par le vent jusqu'à un lieu connu, très loin"),
"wisdom-of-the-wind": PR("Sagesse du vent", VIS, 1, ["vent", "conseil", "guide"], why="les esprits de l'air répondent à une question, d'un mot sage ou d'un vent qui guide"),
"albatross-curse": PR("Malédiction de l'albatros", NORD, 3, ["albatros", "malédiction"], 1, "un albatros spectral la suit : 1 ajouté aux coups contre elle ; si elle le tue, il pend à son cou et la maudit",
    sens=[("vue", None)], manif=["albatros"]),
"attacked-from-within": PR("Attaqué du dedans", PEUR, 3, ["âme", "angoisse", "effroi"], 54, "12d8 en moyenne ; effrayée", **_PSY),
"confusing-cry": PR("Cri déroutant", NORD, P, ["cri", "confusion"], why="ceux qui l'entendent frappent sans contrôle : confus une minute", **_PSY, sens=[("ouïe", None)], manif=["cri"]),
"cordyceps-command": PR("Ordre du cordyceps", ORD, 3, ["spore", "champignon", "emprise"], why="un champignon gagne son corps par degrés et finit par la mener : monter, dévorer, descendre ou attirer"),
"equal-footing": PR("À armes égales", V("mouvement", True), 3, ["lenteur", "maladresse", "mètres"], 5, "plus rapide que moi, elle devient gauche et perd 4,5 m, arrondi à 5"),
"flames-of-ego": PR("Flammes de l'orgueil", ATT, 3, ["flamme", "vanité", "fascination"], why="des flammes superbes la parent : fascinée par elle-même, elle ne s'en prend qu'à qui s'en prend à elle", dur=(1, "MINUTES"),
    impact_sats=[(6, ["éclat", "mètres"])], fam="A", **_PSY, sens=[("vue", None)], manif=["flammes"]),
"indolent-haze": PR("Brume d'indolence", NORD, P, ["pavot", "torpeur", "repos"], why="ils s'allongent, ne veulent plus se relever, puis s'endorment", **_PSY, sens=[("odorat", None)], manif=["pavot"]),
"loves-sacrifice": PR("Sacrifice d'amour", ATT, 4, ["amour", "sacrifice", "interposition"], why="elle se jette devant le coup qui me vise et le prend à ma place ; elle peut en mourir", cond=["coup"], **_PSY),
"luring-wail": PR("Plainte attirante", ATT, P, ["plainte", "fascination", "approche"], why="fascinés, ceux qui m'entendent marchent vers ma voix ; nommer quelqu'un l'y livre mieux", **_PSY, sens=[("ouïe", None)], manif=["plainte"]),
"overwhelming-memory": PR("Souvenir envahissant", NORD, 3, ["souvenir", "stupeur"], why="un souvenir la submerge un instant et la laisse stupéfiée", cible_note=["mémoire"], options=[
    O("Joyeux", impact=(P, ["souvenir", "stupeur", "rire"], "elle rit sans pouvoir riposter")),
    O("Amoureux", impact=(P, ["souvenir", "stupeur", "fascination"], "elle en reste fascinée")),
    O("Terrifiant", impact=(P, ["souvenir", "stupeur", "effroi"], "elle en est effrayée")),
    O("Tragique", impact=(P, ["souvenir", "stupeur", "larmes"], "les larmes l'éblouissent"))]),
"reed-whistle": PR("Sifflet de roseau", VIS, 1, ["brin", "sifflement", "signal"], 2, "d'un coup de sifflet, je désigne à mes alliés une créature que j'ai repérée ; 2 ajouté pour la retrouver"),
"falsify-heat": PR("Chaleur falsifiée", NVIS, 4, ["chaleur", "leurre"], 2, "sa chaleur apparente est fausse, au toucher même : 2 ajouté pour passer pour froid, ou pour chaud ; invisible aux sens de la chaleur"),
"manifestation-of-spirits": PR("Esprits manifestés", EXI, 3, ["esprit", "menace", "stupeur"], why="elle voit tous les esprits qui l'entourent, et les croit menaçants : stupéfiée une minute", dur=(1, "MINUTES"), **_PSY),
"wooden-double": PR("Double de bois", SEP, 1, ["bois", "double", "esquive"], 20, "je fais un pas ; une bûche à ma forme prend le coup à ma place : elle encaisse 20 points", cond=["coup"], fam="A"),
"cauterize-wounds": PR("Plaies cautérisées", HE, 2, ["feu", "cautère", "saignement"], 1, "pour 1 point de brûlure, une chance d'arrêter ce qui saigne ou ronge", qty_cible=5, guerit=True, fam="A"),
"coral-scourge": PR("Fléau de corail", NE, 3, ["corail", "raideur", "maladresse"], 1, "des coraux lui poussent aux jointures : gauche de 1, puis de pis en pis à chaque instant"),
"life-draining-roots": PR("Racines voraces", NE, P, ["bois", "racine", "épine"], 28, "8d6 en moyenne ; 1d4 de vie d'emprunt par vivant transpercé", fam="A", impact_sats=[(2, ["vie", "temporaire"])]),
"noxious-metals": PR("Métaux nocifs", NE, P, ["acier", "toxique"], 14, "4d6 en moyenne aux vivants ; pire pour les plantes et les êtres du bois", fam="A", impact_add=["poison"]),
"pain-of-ages": PR("Douleur des âges", NE, P, ["âme", "angoisse", "lieu"], 36, "8d8 en moyenne : la peine accumulée d'un lieu, lâchée sur mes ennemis"),
"shock-to-the-system": PR("Électrochoc", HE, 2, ["vie", "foudre", "réveil"], 36, "8d8 en moyenne ; un mort de l'instant d'avant revient ; hâté, il peut lancer la foudre à volonté", guerit=True, fam="A"),
"spiritual-renewal": PR("Renouveau spirituel", HE, 2, ["vie", "esprit"], 8, "8 points rendus à chaque instant, quatre instants durant", guerit=True, **_VIV),
"thermal-remedy": PR("Remède thermal", V("qualite"), 4, ["amer", "remède", "repas"], why="un repas ou une boisson pour dix, aux vertus tirées de ses amers", cible_obj=["nourriture"], options=[
    O("Fortifiant", impact=(5, ["amer", "remède", "vie", "temporaire"], "5 points de vie d'emprunt")),
    O("Rafraîchissant", impact=(2, ["amer", "remède", "feu"], "2 retranché au feu reçu")),
    O("Dépuratif", impact=(1, ["amer", "remède", "maladie"], "1 ajouté contre les maladies"))]),
}
FICHES.update(PF2_REM1)

# ----- Pathfinder 2, lot 11 : sorts propres à la version remaniée (Invocation, Évocation) -----
# summon-undead : renvoyé à la comparaison avec les convocations et l'animation des morts déjà publiées.
ER = lambda fr, cible, words, v=None, why="", **kw: PR(fr, NF, cible, words, v, why, **kw)
PF2_REM2 = {
"bramble-bush": ER("Buisson de ronces", P, ["ronce", "épine"], 2, "1d4 en moyenne, et autant à qui y entre avant mon prochain instant", comb="Plante"),
"rousing-splash": PR("Éclaboussure vivifiante", INT, 2, ["eau", "vigueur"], 2, "1d4 en moyenne de vie d'emprunt pour une minute ; une chance d'éteindre ce qui la brûle ou la ronge", comb="Eau"),
"timber": ER("Chute d'arbre", P, ["arbre", "chute"], 5, "2d4 en moyenne : un arbre mort tombe sur ceux qui sont devant moi, puis se décompose", comb="Bois"),
"flourishing-flora": ER("Flore foisonnante", P, ["plante", "pousse"], 5, "2d4 en moyenne, d'une nature qui dépend de la plante choisie", comb="Plante", aoe={"type": "sphere", "size": 5}),
"foraging-friends": PR("Amis glaneurs", INV, P, ["bête", "glanage", "vivres"], 4, "de petites bêtes rapportent en une heure de quoi nourrir 4 personnes un jour"),
"instant-potter": PR("Poterie instantanée", EXI, 4, ["terre", "poterie"], why="la terre des alentours façonnée en objets simples, pour une heure", cible_obj=["objet"], fam="A"),
"wall-of-shrubs": PR("Haie", EXI, P, ["haie", "abri"], why="une ligne de buissons du pays sort de terre : elle abrite un peu", comb="Plante", aoe={"type": "line", "size": 60}),
"avenging-wildwood": PR("Arbre vengeur", EXI, P, ["arbre", "branche", "frappe"], why="un arbre animé frappe mes ennemis de ses branches", comb="Bois", impact_sats=[(20, ["réserve"])]),
"blazing-armory": PR("Armurerie ardente", EXI, 2, ["arme", "flamme"], 4, "une arme de flammes dans sa main : elle frappe en feu, 1d6 en moyenne de plus"),
"helpful-wood-spirits": PR("Esprits du bois serviables", INV, P, ["esprit", "corvée"], why="de petits esprits du bois font une tâche simple à chaque instant ; rien ne les atteint", comb="Bois"),
"rubble-step": PR("Pas d'éboulis", TR, 2, ["gravats", "sillage"], why="chaque case qu'il quitte devient terrain pénible, deux instants durant", comb="Roche"),
"warping-pull": PR("Traction salvatrice", TP2, 2, ["téléportation", "sauvegarde"], 5, "je le tire de 3 m vers moi, hors du danger : 5 retranché à ce qui le frappait", cond=["coup"], impact_sats=[(3, ["mètres"])]),
"conjured-conveyance": PR("Véhicule conjuré", EXI, P, ["véhicule", "bois"], why="un véhicule ouvragé, tout de bois, que je mène par la magie, une heure durant", fam="A"),
"dive-and-breach": PR("Plongeon et jaillissement", TP2, 1, ["plongeon", "eau", "jaillissement"], 17, "je plonge dans le sol comme dans l'eau et ressors à 12 m : 3d10 en moyenne à ceux d'alentour", comb="Eau", impact_sats=[(12, ["mètres"])]),
"echo-jump": PR("Saut à écho", TP2, 1, ["téléportation", "écho", "force"], 18, "je me téléporte ; mon écho éclate où j'étais : 4d8 en moyenne à 3 m autour"),
"bridge-of-vines": PR("Pont de lianes", EXI, P, ["liane", "pont"], why="un pont de lianes large de 3 m, qui franchit obstacles et dénivelés", comb="Plante", aoe={"type": "line", "size": 60}, impact_sats=[(20, ["réserve"])]),
"sliding-blocks": PR("Blocs coulissants", EXI, P, ["pierre", "cube", "lévitation"], why="six cubes de pierre de 1,5 m, que je déplace d'un geste", comb="Roche", qty=6),
"boomerang-shot": ER("Tir en boomerang", 3, ["bois", "courbe", "contournement"], 39, "7d10 en moyenne ; il contourne abris et obstacles", comb="Bois"),
"corrosive-muck": ER("Fange corrosive", P, ["flaque", "enlisement"], 28, "8d6 en moyenne à chaque instant ; deux flaques où l'on s'englue", qty=2),
"fires-pathway": PR("Chemin du feu", TP2, 1, ["feu", "brasier", "passage"], why="j'entre dans un feu et ressors par un autre, à 8 km au plus", fam="A", impact_sats=[(8, ["kilomètres"])]),
"spiritual-transport": PR("Transport spirituel", TP2, 1, ["téléportation", "esprit"], why="les esprits me portent en un lieu que je vois ; mon compagnon suit"),
"arrow-salvo": ER("Salve de flèches", P, ["arc", "flèche"], 44, "8d10 en moyenne ; au pire, renverse", comb="Bois"),
"field-of-razors": PR("Champ de rasoirs", EXI, P, ["fil", "rasoir"], 5, "un enchevêtrement de fils tranchants : terrain pénible, 5 à chaque pas", comb="Acier", comp=["métal"]),
"personal-ocean": PR("Océan personnel", EXI, 1, ["eau", "bulle", "nage"], why="une bulle d'eau de mer m'entoure et me suit : j'y nage et y respire ; on m'y combat comme sous l'eau", comb="Eau"),
"wall-of-metal": PR("Mur de métal", EXI, P, ["mur", "acier"], why="une feuille de fer, de fer froid ou d'argent", comb="Acier", forme=_MUR(18, 9)),
"beheading-buzz-saw": ER("Scie décapitante", P, ["disque", "lame"], 28, "5d10 en moyenne", comb="Acier", impact_plus=[(14, ["persistance", "saignement"], "4d6 en moyenne à chaque instant")]),
"dancing-fountain": ER("Fontaine dansante", P, ["fontaine", "jet"], 35, "10d6 en moyenne, selon la figure commandée à chaque instant", comb="Eau"),
"devouring-void": PR("Vide dévorant", NE, P, ["déchirure", "ténébreux", "retenue"], 32, "7d8 en moyenne aux vivants à chaque instant ; qui veut sortir peut être retenu"),
"hungry-depths": PR("Abysse affamé", NE, P, ["gouffre", "eau", "croc"], 28, "4d8 + 4d4 en moyenne : une spirale d'eau noire, pleine d'yeux et de dents", fam="A"),
"pollen-pods": PR("Cosses à pollen", EXI, P, ["cosse", "pollen", "piège"], 36, "8d8 en moyenne à 4,5 m quand on l'approche ; éblouit, stupéfie", qty=4, dur=(12, "HEURES")),
"sudden-transposition": PR("Transposition brutale", TP2, 3, ["téléportation", "arrachement"], 55, "10d10 en moyenne ; je choisis où elle reparaît", qty_cible=2),
"summon-elemental-herald": PR("Convocation d'un héraut élémentaire", INV, 9, ["héraut", "désastre"], 45, "il vient sous la forme d'un désastre : 10d8 en moyenne", cible_note=["élémentaire"], fam="A"),
"illuminate": PR("Allumage", EXI, P, ["flamme", "lampe"], why="toutes les bougies, lampes et torches de la zone s'allument", fam="A"),
"live-wire": ER("Fil sous tension", 3, ["fil", "cuivre", "foudre"], 4, "1d4 de taille + 1d4 de foudre en moyenne", comb="Bronze"),
"needle-darts": ER("Aiguilles", 3, ["aiguille", "saignement"], 8, "3d4 en moyenne ; les aiguilles gardent les vertus de leur métal", comb="Acier", comp=["métal"]),
"slashing-gust": ER("Rafale tranchante", 3, ["vent", "taille"], 5, "2d4 en moyenne à chacune", comb="Air", qty_cible=2),
"conductive-weapon": PR("Arme conductrice", INT, 4, ["courant", "décharge"], 4, "1d6 en moyenne de foudre à chaque coup ; 1d12 sur qui porte du métal", cible_obj=["arme"], comb="Foudre"),
"dehydrate": PR("Déshydratation", NE, P, ["sécheresse", "persistance"], 4, "1d6 en moyenne à chaque instant ; affaiblit ; pire pour les êtres d'eau et les plantes", fam="A"),
"signal-skyrocket": ER("Fusée de signal", P, ["fusée", "signal", "fracas"], 6, "1d10 en moyenne ; une fusée rouge monte droit et éclate : vue et entendue de très loin", comp=["poudre"]),
"brine-dragon-bile": ER("Bile saumâtre", 3, ["sel", "plaie", "persistance"], 7, "2d6 en moyenne à chaque instant : le sel ronge la plaie fraîche", cond=["blessure"], comb="Eau"),
"exploding-earth": ER("Terre explosive", 3, ["terre", "éclat"], 14, "4d6 en moyenne, et 1d6 d'éclats alentour", comb="Roche"),
"propulsive-breeze": PR("Brise propulsive", TP2, 2, ["vent", "élan", "mètres"], 5, "à la fin de sa course ou de son saut, le vent le pousse 4,5 m plus loin, arrondi à 5", comb="Air", cond=["mouvement"]),
"splinter-volley": ER("Volée d'échardes", 3, ["écharde", "saignement"], 14, "4d6 en moyenne ; sur deux cibles en y mettant plus de temps", comb="Bois"),
"blastback": ER("Onde de chute", P, ["chute", "onde"], 15, "6d4 en moyenne ; je me pose sans mal et ceux d'alentour sont repoussés", cond=["chute"], comb="Air"),
"airlift": PR("Envol", TP2, P, ["vent", "transport", "mètres"], 18, "le vent m'emporte avec tout ce qui m'entoure à 18 m de là", comb="Air"),
"cinder-swarm": ER("Nuée de braises", 3, ["insecte", "braise"], 11, "3d6 en moyenne à elle et à ses voisins, à chaque instant, selon l'insecte choisi", comb="Feu"),
"grasp-of-the-deep": ER("Étreinte des profondeurs", 3, ["pression", "abysse", "suffocation"], 21, "6d6 en moyenne ; elle étouffe et s'égare", comb="Eau", **_PSY),
"rust-cloud": ER("Nuage de rouille", P, ["rouille", "dissimulation"], 28, "5d10 en moyenne à chaque instant ; le métal s'y corrode", comb="Acier"),
"ymeris-mark": ER("Marque ardente", 3, ["marque", "épuisement", "piste"], 18, "5d6 en moyenne ; fatiguée, et je sens où elle est", dur=(7, "JOURS")),
"zephyr-slip": PR("Dérobade du zéphyr", TP2, 1, ["vent", "esquive", "mètres"], 5, "une brise m'emporte à 4,5 m de mon agresseur, arrondi à 5", comb="Air", cond=["agression"]),
"elemental-breath": ER("Souffle élémentaire", P, ["souffle", "élément", "hasard"], 33, "6d10 en moyenne, d'un élément tiré au sort", comb="Énergie pure"),
"freezing-rain": ER("Pluie verglaçante", P, ["pluie", "grésil", "lenteur"], 14, "4d6 en moyenne quand la pluie tourne au grésil ; ralentit ; le sol détrempé gêne"),
"pressure-zone": PR("Zone de dépression", NINT, P, ["pression", "surdité", "maladresse"], why="l'air se raréfie : les vivants sont assourdis et gauches", fam="A", **_VIV),
"frost-pillar": PR("Pilier de givre", V("mouvement", True), 3, ["glace", "prison"], why="prise dans un pilier de glace, elle ne bouge presque plus", comb="Glace", impact_sats=[(60, ["réserve"])]),
"phantom-orchestra": ER("Orchestre fantôme", P, ["orchestre", "symphonie"], 28, "8d6 en moyenne, là où je dirige la symphonie", sens=[("ouïe", None), ("vue", None)], manif=["musiciens"]),
"heaving-earth": ER("Terre soulevée", 3, ["onde", "sol", "secousse"], 66, "12d10 en moyenne ; ceux qui sont sur le trajet de l'onde chancellent", comb="Terre"),
"vacuum": PR("Vide d'air", NE, P, ["souffle", "étouffement"], why="l'air est aspiré autour de moi : on y suffoque, étourdi", fam="A"),
"rainbow-fumarole": ER("Fumerolle irisée", P, ["flamme", "fumée", "hasard"], why="des flammes de toutes couleurs percent le sol : dégâts et vapeurs tirés au sort parmi huit", fam="A"),
"whirlpool": ER("Maelström", P, ["tourbillon", "aspiration"], 33, "6d10 en moyenne ; attire vers son centre de 3 m", comb="Eau", impact_sats=[(3, ["traction", "mètres"])]),
"magnetic-dominion": PR("Empire magnétique", V("mouvement"), P, ["aimant", "déplacement"], why="tout ce qui est de métal ou en porte, je le déplace à mon gré dans la zone", comb="Magnétisme"),
}
FICHES.update(PF2_REM2)

# ----- Pathfinder 2, lot 12 : sorts propres à la version remaniée (Transmutation) -----
# Restent pour la comparaison glyphe à glyphe : hidebound, whispers-of-the-void, lignify, eagles-cry (appariements automatiques rejetés).
PF2_REM3 = {
"deep-breath": PR("Grande inspiration", INT, 1, ["souffle", "apnée"], why="un souffle retenu dix minutes, que les coups ne font pas perdre ; parler le vide"),
"draw-moisture": PR("Eau soutirée", V("flux"), 4, ["eau", "séchage"], why="l'eau sort de l'objet et se rassemble en un globe dans ma main : il sèche", cible_obj=["objet"], fam="A"),
"take-root": PR("Enracinement", V("mouvement", True), 2, ["bois", "racine", "aplomb"], 1, "des racines l'ancrent : 1 ajouté pour n'être ni poussé, ni renversé, ni désarmé", fam="A"),
"camel-spit": PR("Crachat du chameau", NF, 3, ["crachat", "éblouissement"], 4, "1d6 en moyenne d'acide ; éblouit ; trois crachats en tout", impact_sats=[(3, ["usage"])]),
"fold-metal": PR("Métal plié", TR, 4, ["acier", "boule", "cachette"], why="l'objet de métal se replie en une boule lisse pas plus grosse qu'un œuf ; l'eau ou le feu la défont", cible_obj=["objet"], fam="A"),
"hippocampus-retreat": PR("Retraite de l'hippocampe", NF, 3, ["queue", "nage", "repli"], 7, "un coup de queue de 2d6 en moyenne, puis je nage 9 m plus loin", impact_sats=[(9, ["nage", "mètres"])]),
"leaden-steps": PR("Pas de plomb", V("mouvement", True), 3, ["acier", "pied", "charge"], 2, "ses pieds deviennent des blocs de métal : chargée, et la foudre la blesse de 2 de plus", fam="A"),
"shielded-arm": PR("Bras bouclier", SEP, 2, ["minerai", "bras", "parade"], 2, "des veines de minerai durcissent son bras : il pare comme un bouclier, 2 ajouté à sa défense", cible_note=["garde"]),
"threefold-limb": PR("Membre aux trois états", NF, 3, ["membre", "eau"], 7, "2d6 en moyenne", fam="A", options=[
    O("Glace", impact=(7, ["membre", "eau", "froid", "lenteur"], "2d6 en moyenne de froid ; ralentie de 3 m")),
    O("Eau", impact=(7, ["membre", "eau", "déplacement"], "2d6 en moyenne de choc ; je la replace à 3 m")),
    O("Vapeur", impact=(7, ["membre", "eau", "feu", "voile"], "2d6 en moyenne de feu ; la vapeur lui cache tout"))]),
"unbroken-panoply": PR("Panoplie intacte", V("nature", True), 4, ["arme", "sursis", "retenue"], why="l'arme brisée sert comme si elle était entière, une heure ; elle assomme sans tuer", cible_obj=["arme"]),
"weaken-earth": PR("Terre affaiblie", NINT, 4, ["pierre", "fragilité"], 5, "la pierre ou la terre visée perd 5 de dureté ; ce qui n'en a pas est blessé de 3 de plus", impact_sats=[(3, ["faille"])], fam="A"),
"weave-wood": PR("Bois tressé", TR, 4, ["bois", "fibre", "tressage"], 4, "le bois brut se défait en fibres qui se tressent en objets simples, jusqu'à 4", cible_obj=["objet"], fam="A"),
"wooden-fists": PR("Poings de bois", TR, 1, ["bois", "poing", "tronc"], 4, "mes bras deviennent troncs : mes poings frappent de 1d6 en moyenne, et plus loin", fam="A"),
"clad-in-metal": PR("Paré de métal", TR, 4, ["acier", "placage"], why="la surface d'un objet de métal devient pour une minute celle d'un métal précieux, avec ses vertus", cible_obj=["objet"], fam="A"),
"claws-of-the-otter": PR("Griffes de la loutre", TR, 1, ["griffe", "palmure", "froid"], 6, "des griffes de 1d4 + 1d6 de froid en moyenne ; 1 ajouté pour nager", fam="A"),
"frog-tongue": PR("Langue de grenouille", ATT, 3, ["langue", "colle"], 9, "2d8 en moyenne ; collée au bout de ma langue, elle ne peut s'éloigner"),
"pave-ground": PR("Sol aplani", TR, P, ["terre", "chemin"], why="la terre, les gravats et le sable s'aplanissent devant moi : le terrain pénible redevient aisé", fam="A"),
"antlion-trap": PR("Piège du fourmilion", TR, P, ["sable", "entonnoir", "glissement", "mètres"], 3, "le sol devient un entonnoir de sable meuble : on y glisse de 3 m vers le centre à chaque instant", comb="Sable"),
"croak-voice": PR("Voix coassante", NQ, 3, ["voix", "enrouement"], 11, "sa gorge enfle : parler et incanter lui font mal, 2d10 en moyenne à chaque fois", **_PSY),
"lotus-walk": PR("Marche du lotus", TP2, 1, ["lotus", "eau", "marche"], why="des fleurs d'eau s'ouvrent sous mes pas : je marche sur l'eau, et mon sillage de feuilles porte les autres", comb="Plante"),
"sand-form": PR("Forme de sable", TR, 2, ["sable", "corps"], 5, "5 retranché aux pointes et aux tranchants ; sans odeur, ne saigne pas, se fond dans le sable", comb="Sable"),
"glass-form": PR("Forme de verre", TR, 2, ["verre", "corps", "transparence"], 5, "estompé, sans odeur ; 5 retranché à l'acide, au froid, à la foudre et aux pointes ; 5 ajouté au son et aux chocs", comb="Verre"),
"grasping-earth": PR("Terre agrippante", V("mouvement", True), P, ["terre", "main", "ensevelissement"], 4, "des mains de roche saisissent et enterrent : 1d6 en moyenne à chaque instant", comb="Roche"),
"mercurial-stride": PR("Foulée de mercure", TP2, 1, ["mercure", "traversée"], 21, "je cours deux fois plus loin et traverse un être en gouttes de mercure : 6d6 en moyenne de poison, et la nausée", comb="Mercure"),
"snake-fangs": PR("Crocs du serpent", TR, 1, ["croc", "venin", "avalement"], 16, "des crocs de 1d8 + 2d10 de poison en moyenne ; je peux avaler une proie plus petite"),
"stifling-stillness": PR("Calme étouffant", NINT, P, ["air", "stagnation", "suffocation"], 11, "l'air se fige : terrain pénible ; qui y respire s'épuise et s'empoisonne, 3d6 en moyenne", fam="A"),
"flame-dancer": PR("Danseur de flammes", INT, 2, ["flamme", "danse"], 7, "ses poings et ses pieds frappent de 2d6 en moyenne de feu en plus ; il intimide en dansant"),
"mantle-of-the-melting-heart": PR("Manteau du cœur fondant", TR, 1, ["acier", "manteau"], why="peau et armure se couvrent de métal liquide ; deux dons à la fois", comb="Mercure", options=[
    O("Cœur de cuivre", impact=(10, ["acier", "manteau", "foudre"], "10 retranché à la foudre, que j'attire sur moi")),
    O("Chair d'or", impact=(2, ["acier", "manteau", "or"], "insensible aux poisons et aux maladies ; 2 ajouté contre ceux que je porte déjà")),
    O("Toucher réactif", impact=(7, ["acier", "manteau", "corrosion"], "2d6 en moyenne à tout métal qui me touche")),
    O("Poigne lestée", impact=(6, ["acier", "manteau", "câble"], "des poings au bout de câbles : 1d4 + 1d6 de poison en moyenne ; ils saisissent"))]),
"mantle-of-the-unwavering-heart": PR("Manteau du cœur inébranlable", TR, 1, ["bois", "manteau"], why="lianes et branches m'enveloppent ; deux dons à la fois", comb="Bois", options=[
    O("Vigueur toujours verte", impact=(3, ["bois", "manteau", "sève"], "3 points rendus à chaque instant ; 2 ajouté contre poisons et maladies")),
    O("Parfum entêtant", impact=(P, ["bois", "manteau", "parfum", "nausée"], "à 4,5 m autour, la nausée, et plus de flair")),
    O("Tronc dressé", impact=(9, ["bois", "manteau", "croissance"], "je grandis d'une taille : gauche, mais une branche qui saisit, 2d8 en moyenne")),
    O("Volonté inflexible", impact=(1, ["bois", "manteau", "psyché"], "rien ne me fascine ; 1 ajouté contre ce qui vise l'esprit"))]),
"vitrifying-blast": PR("Souffle vitrifiant", NF, P, ["verre", "éclat", "vitrification"], 28, "8d6 en moyenne ; ralentie, à demi changée en verre : le son et les chocs la blessent de 3 de plus", comb="Verre", impact_sats=[(3, ["faille"])]),
"chrysopoetic-curse": PR("Malédiction de l'or", TR, 3, ["malédiction", "or", "fardeau"], why="tout ce qu'elle touche devient or : armure et habits l'écrasent, puis ses armes ; au pire, sa chair même", dur=(1, "MINUTES")),
"restore-ground": PR("Sol rendu à la nature", NE, P, ["édifice", "nature", "retour"], why="le lieu redevient sauvage : objets et bâtiments de main d'homme s'effacent, la végétation reprend"),
"ferrous-form": PR("Forme de fer", TR, 1, ["acier", "corps", "invulnérable"], 10, "un corps de fer souple : 10 retranché aux coups ; ni poison, ni maladie, ni mort subite, ni soin", comb="Acier"),
}
FICHES.update(PF2_REM3)

# ----- Pathfinder 2 : reprises du 16 novembre -----
# Inarama n'a ni lune ni soleil (décision de Baptiste).
FICHES.pop("cosmic-form"); PF2_ECARTE["cosmic-form"] = "prend les pouvoirs de la lune ou du soleil, qui n'existent pas dans Inarama"
_R("moon-frenzy", fr="Frénésie sauvage")

# ----- Pathfinder 2, lot 13 : versions PF2 des sorts déjà publiés (comparaison automatique : niveau, portée, durée, zone, dégâts) -----
# Engendré par pf2work/gen96.py. Une forme « version » ne paraît que si son glyphe diffère de ceux de la page.
PF2_VERSIONS = {
 'acid-arrow': {'vp2': {}, 'vr': {'src_idx': 'acid-grip'}},
 'acid-splash': {'vp2': {}, 'vr': {'src_idx': 'caustic-blast'}},
 'admonishing-ray': {'vp2': {'impact': (7, ['assommer'], '2d6 en moyenne')}},
 'advanced-scurvy': {'vp2': {}},
 'air-bubble': {'vp2': {}, 'vr': {}},
 'air-walk': {'vp2': {}},
 'alarm': {'vp2': {}, 'vr': {}},
 'alter-self': {'vp2': {'src_idx': 'humanoid-form'}, 'vr': {'src_idx': 'humanoid-form'}},
 'animal-messenger': {'vp2': {}, 'vr': {}},
 'animate-dead': {'vp2': {}, 'vr': {'src_idx': 'summon-undead'}},
 'animate-rope': {'vp2': {}},
 'animus-mine': {'vp2': {'options': [{'label': 'Mine mentale'}], 'impact': (18, ['chancellement'], '4d8 en moyenne')}},
 'ant-haul': {'vp2': {'options': [{'label': 'Force de fourmi'}]}, 'vr': {'options': [{'label': 'Force de fourmi'}]}},
 'anticipate-peril': {'vp2': {}},
 'antimagic-field': {'vp2': {}},
 'aqueous-orb': {'vp2': {}, 'vr': {}},
 'arcane-eye': {'vp2': {'src_idx': 'prying-eye'}},
 'arcane-hand': {'vp2': {'src_idx': 'forceful-hand'}},
 'arcane-lock': {'vp2': {'src_idx': 'lock'}, 'vr': {'src_idx': 'lock'}},
 'arcane-mark': {'vp2': {'src_idx': 'sigil'}, 'vr': {'src_idx': 'sigil'}},
 'arcanists-magic-aura': {'vp2': {'src_idx': 'magic-aura'}, 'vr': {'src_idx': 'disguise-magic'}},
 'augury': {'vp2': {}, 'vr': {}},
 'aura-of-the-unremarkable': {'vp2': {}},
 'baleful-polymorph': {'vp2': {}},
 'bane': {'vp2': {}, 'vr': {}},
 'banishment': {'vp2': {}, 'vr': {}},
 'barkskin': {'vp2': {}},
 'beast-shape-i': {'vp2': {'options': [{'label': 'Forme bestiale I', 'impact': ('plein', ['bête', 'forme'], 'un animal petit ou moyen')}], 'src_idx': 'animal-form'}, 'vr': {'options': [{'label': 'Forme bestiale I', 'impact': ('plein', ['bête', 'forme'], 'un animal petit ou moyen')}], 'src_idx': 'animal-form'}},
 'bilocation': {'vp2': {}},
 'biting-words': {'vp2': {'impact': (7, ['parole'], '2d6 en moyenne')}},
 'black-tentacles': {'vp2': {}, 'vr': {'src_idx': 'slither'}},
 'blade-barrier': {'vp2': {}, 'vr': {'src_idx': 'blessed-boundary'}},
 'bless': {'vp2': {}, 'vr': {}},
 'blindness-deafness': {'vp2': {'src_idx': 'blindness'}, 'vr': {'src_idx': 'blindness'}},
 'blink': {'vp2': {}, 'vr': {'src_idx': 'flicker'}},
 'blistering-invective': {'vp2': {}, 'vr': {}},
 'blur': {'vp2': {}, 'vr': {}},
 'breath-of-life': {'vp2': {}, 'vr': {}},
 'burning-hands': {'vp2': {}},
 'call-lightning': {'vp2': {'src_idx': 'lightning-storm'}, 'vr': {'src_idx': 'lightning-storm'}},
 'calm-emotions': {'vp2': {}},
 'cave-fangs': {'vr': {}},
 'chain-lightning': {'vp2': {}, 'vr': {}},
 'charm-person': {'vp2': {'src_idx': 'charm'}, 'vr': {'src_idx': 'charm'}},
 'chill-touch': {'vp2': {}, 'vr': {'src_idx': 'void-warp'}},
 'clairvoyance': {'vp2': {}, 'vr': {}},
 'cloudkill': {'vp2': {}},
 'color-spray': {'vp2': {}},
 'command': {'vp2': {}, 'vr': {}},
 'command-undead': {'vp2': {'options': [{'label': 'Injonction aux morts-vivants', 'impact': ('plein', ['amitié'], 'un mort-vivant amical')}], 'src_idx': 'bind-undead'}, 'vr': {'options': [{'label': 'Injonction aux morts-vivants', 'impact': ('plein', ['amitié'], 'un mort-vivant amical')}], 'src_idx': 'bind-undead'}},
 'comprehend-languages': {'vp2': {'src_idx': 'comprehend-language'}},
 'cone-of-cold': {'vp2': {}, 'vr': {'src_idx': 'howling-blizzard'}},
 'confusion': {'vp2': {}, 'vr': {}},
 'contingency': {'vp2': {}, 'vr': {}},
 'continual-flame': {'vp2': {}, 'vr': {'src_idx': 'everlight'}},
 'control-water': {'vp2': {}, 'vr': {}},
 'countless-eyes': {'vp2': {}, 'vr': {}},
 'create-food-and-water': {'vp2': {'src_idx': 'create-food'}, 'vr': {'src_idx': 'create-food'}},
 'create-or-destroy-water': {'vp2': {'src_idx': 'create-water'}, 'vr': {'src_idx': 'create-water'}},
 'creation': {'vp2': {}, 'vr': {}},
 'crushing-despair': {'vp2': {}},
 'cup-of-dust': {'vp2': {}},
 'dancing-lights': {'vp2': {}},
 'darkness': {'vp2': {}, 'vr': {}},
 'darkvision': {'vp2': {}, 'vr': {}},
 'daze': {'vp2': {}, 'vr': {}},
 'death-knell': {'vp2': {}},
 'death-ward': {'vp2': {}},
 'demand': {'vp2': {'src_idx': 'telepathic-demand'}, 'vr': {'src_idx': 'telepathic-demand'}},
 'detect-evil-and-good': {'vp2': {'src_idx': 'detect-alignment'}},
 'detect-magic': {'vp2': {}, 'vr': {}},
 'detect-metal': {'vr': {}},
 'detect-poison-and-disease': {'vp2': {'src_idx': 'detect-poison'}, 'vr': {'src_idx': 'detect-poison'}},
 'detect-scrying': {'vp2': {}, 'vr': {}},
 'detect-thoughts': {'vp2': {'src_idx': 'mind-reading'}, 'vr': {'src_idx': 'mind-reading'}},
 'dimension-door': {'vp2': {}},
 'dimensional-anchor': {'vp2': {}, 'vr': {'src_idx': 'planar-tether'}},
 'dimensional-lock': {'vp2': {}, 'vr': {'src_idx': 'planar-seal'}},
 'discern-lies': {'vp2': {}},
 'discern-location': {'vp2': {}},
 'disguise-self': {'vp2': {'src_idx': 'illusory-disguise'}, 'vr': {'src_idx': 'illusory-disguise'}},
 'disintegrate': {'vp2': {}, 'vr': {}},
 'dispel-magic': {'vp2': {}, 'vr': {}},
 'disrupt-undead': {'vp2': {}, 'vr': {'src_idx': 'vitality-lash', 'impact': (7, ['lumière'], '2d6 en moyenne')}},
 'disrupting-weapon': {'vp2': {'src_idx': 'disrupting-weapons'}, 'vr': {'src_idx': 'infuse-vitality'}},
 'divination': {'vp2': {'src_idx': 'read-omens'}, 'vr': {'src_idx': 'read-omens'}},
 'divine-vessel': {'vp2': {}},
 'divine-word': {'vp2': {'src_idx': 'divine-decree'}, 'vr': {'src_idx': 'divine-decree'}},
 'dominate-person': {'vp2': {'src_idx': 'dominate'}, 'vr': {'src_idx': 'dominate'}},
 'dream-council': {'vp2': {}, 'vr': {}},
 'earthquake': {'vp2': {}, 'vr': {}},
 'elemental-body-i': {'vp2': {'options': [{'label': 'Corps élémentaire I', 'impact': ('plein', ['élémentaire', 'forme', 'petit'], 'un élémentaire petit')}], 'src_idx': 'elemental-form'}, 'vr': {'options': [{'label': 'Corps élémentaire I', 'impact': ('plein', ['élémentaire', 'forme', 'petit'], 'un élémentaire petit')}], 'src_idx': 'elemental-form'}},
 'endure-elements': {'vp2': {}},
 'enervation': {'vp2': {'options': [{'label': 'Énervation', 'impact': (11, ['affaiblissement'], '1d4 niveaux perdus pour un temps, soit 11 points de vie')}]}},
 'enhance-victuals': {'vr': {'src_idx': 'cleanse-cuisine'}},
 'enlarge-reduce': {'vp2': {'src_idx': 'enlarge'}, 'vr': {'src_idx': 'enlarge'}},
 'entangle': {'vp2': {}},
 'enthrall': {'vp2': {}, 'vr': {}},
 'etherealness': {'vp2': {'src_idx': 'ethereal-jaunt'}},
 'etheric-shards': {'vp2': {}},
 'expeditious-excavation': {'vp2': {}},
 'expeditious-retreat': {'vp2': {'src_idx': 'fleet-step'}, 'vr': {'src_idx': 'fleet-step'}},
 'faerie-fire': {'vp2': {}},
 'false-life': {'vp2': {}, 'vr': {'src_idx': 'false-vitality'}},
 'false-vision': {'vp2': {}, 'vr': {}},
 'fear': {'vp2': {}, 'vr': {}},
 'fear-the-sun': {'vp2': {}},
 'feast-of-ashes': {'vp2': {}},
 'feather-fall': {'vp2': {}},
 'feeblemind': {'vp2': {}},
 'fey-form-i': {'vp2': {'options': [{'label': 'Forme féerique I', 'impact': ('plein', ['fée', 'forme'], 'une fée petite ou moyenne')}], 'src_idx': 'fey-form'}},
 'fiery-body': {'vp2': {}, 'vr': {}},
 'final-sacrifice': {'vp2': {}, 'vr': {}},
 'find-the-path': {'vp2': {'src_idx': 'wanderers-guide'}, 'vr': {'src_idx': 'wanderers-guide'}},
 'finger-of-death': {'vp2': {'impact': (70, ['mort', 'ténébreux'], '70 ; si elle tombe, elle meurt')}, 'vr': {'src_idx': 'execute', 'impact': (70, ['mort', 'ténébreux'], '70 ; si elle tombe, elle meurt')}},
 'fire-seeds': {'vp2': {}, 'vr': {'src_idx': 'tree-of-seasons'}},
 'fire-shield': {'vp2': {}, 'vr': {}},
 'fireball': {'vp2': {}, 'vr': {}},
 'flame-strike': {'vp2': {}, 'vr': {'src_idx': 'divine-immolation'}},
 'flaming-sphere': {'vp2': {}, 'vr': {'src_idx': 'floating-flame'}},
 'flesh-to-stone': {'vp2': {}},
 'floating-disk': {'vp2': {}, 'vr': {'src_idx': 'carryall'}},
 'fly': {'vp2': {}, 'vr': {}},
 'fog-cloud': {'vp2': {'src_idx': 'obscuring-mist'}},
 'forcecage': {'vp2': {'src_idx': 'force-cage'}, 'vr': {'src_idx': 'lifewood-cage'}},
 'foresight': {'vp2': {}, 'vr': {}},
 'form-of-the-dragon-i': {'vp2': {'options': [{'label': 'Forme draconique I', 'impact': ('plein', ['dragon', 'forme'], 'un dragon moyen')}], 'src_idx': 'dragon-form'}, 'vr': {'options': [{'label': 'Forme draconique I', 'impact': ('plein', ['dragon', 'forme'], 'un dragon moyen')}], 'src_idx': 'dragon-form'}},
 'freedom-of-movement': {'vp2': {}},
 'frostbite': {'vr': {}},
 'fungal-infestation': {'vp2': {}, 'vr': {}},
 'gaseous-form': {'vp2': {}, 'vr': {'src_idx': 'vapor-form'}},
 'gate': {'vp2': {}, 'vr': {}},
 'gentle-breeze': {'vr': {}},
 'gentle-repose': {'vp2': {}},
 'geyser': {'vp2': {}},
 'glibness': {'vp2': {}},
 'glitterdust': {'vp2': {}},
 'globe-of-invulnerability': {'vp2': {}, 'vr': {'src_idx': 'dispelling-globe'}},
 'glyph-of-warding': {'vp2': {}},
 'gravity-well': {'vp2': {}, 'vr': {}},
 'grease': {'vp2': {}, 'vr': {}},
 'greater-restoration': {'vp2': {'src_idx': 'restoration'}},
 'guidance': {'vp2': {}, 'vr': {}},
 'guiding-star': {'vp2': {}},
 'gust-of-wind': {'vp2': {}, 'vr': {}},
 'hallucinatory-terrain': {'vp2': {}},
 'harm': {'vp2': {}, 'vr': {}},
 'haste': {'vp2': {}, 'vr': {}},
 'heal': {'vp2': {'impact': (13, ['vie'], '1d8 + 8 en moyenne'), 'guerit': True}, 'vr': {'impact': (13, ['vie'], '1d8 + 8 en moyenne'), 'guerit': True}},
 'heat-metal': {'vp2': {}},
 'heroism': {'vp2': {}, 'vr': {}},
 'hideous-laughter': {'vp2': {}},
 'hold-person': {'vp2': {'src_idx': 'paralyze'}, 'vr': {'src_idx': 'paralyze'}},
 'holy-aura': {'vp2': {'src_idx': 'divine-aura'}},
 'holy-smite': {'vp2': {'options': [{'label': "Châtiment sacré — contre l'hostile", 'cond': ['hostile'], 'impact': (14, ['aveuglement'], '3d8 en moyenne, puis aveuglée')}], 'src_idx': 'divine-wrath'}, 'vr': {'options': [{'label': "Châtiment sacré — contre l'hostile", 'cond': ['hostile'], 'impact': (14, ['aveuglement'], '3d8 en moyenne, puis aveuglée')}], 'src_idx': 'divine-wrath'}},
 'horrid-wilting': {'vp2': {'impact': (55, ['dessèchement'], '10d10 en moyenne')}},
 'hydraulic-push': {'vp2': {}, 'vr': {}},
 'hydraulic-torrent': {'vp2': {}, 'vr': {}},
 'hypercognition': {'vp2': {}, 'vr': {}},
 'hypnotic-pattern': {'vp2': {}},
 'ice-storm': {'vp2': {}, 'vr': {}},
 'ill-omen': {'vp2': {}, 'vr': {}},
 'implosion': {'vp2': {}, 'vr': {}},
 'instant-armor': {'vp2': {}},
 'invisibility': {'vp2': {}, 'vr': {}},
 'irresistible-dance': {'vp2': {'src_idx': 'uncontrollable-dance'}, 'vr': {'src_idx': 'uncontrollable-dance'}},
 'jump': {'vp2': {}, 'vr': {}},
 'kings-castle': {'vr': {}},
 'knock': {'vp2': {}, 'vr': {}},
 'know-direction': {'vp2': {}, 'vr': {'src_idx': 'know-the-way'}},
 'lesser-restoration': {'vp2': {'src_idx': 'remove-disease'}, 'vr': {'src_idx': 'sound-body'}},
 'levitate': {'vp2': {}, 'vr': {}},
 'liberating-command': {'vp2': {}},
 'life-bubble': {'vp2': {'src_idx': 'lashuntas-life-bubble'}},
 'life-pact': {'vp2': {}},
 'light': {'vp2': {}, 'vr': {}},
 'lightning-bolt': {'vp2': {'impact': (26, ['foudre', 'embrasement'], '4d12 en moyenne')}, 'vr': {'impact': (26, ['foudre', 'embrasement'], '4d12 en moyenne')}},
 'locate-object': {'vp2': {'src_idx': 'locate'}, 'vr': {'src_idx': 'locate'}},
 'longstrider': {'vp2': {}},
 'mad-monkeys': {'vp2': {}, 'vr': {}},
 'mage-armor': {'vp2': {}},
 'mage-hand': {'vp2': {}},
 'mages-disjunction': {'vp2': {'src_idx': 'disjunction'}, 'vr': {'src_idx': 'detonate-magic'}},
 'magic-circle': {'vp2': {'src_idx': 'circle-of-protection'}},
 'magic-fang': {'vp2': {'options': [{'label': 'Morsure magique', 'impact': (1, [], '+1 à une arme naturelle'), 'cible_note': ['arme', 'naturelle']}]}, 'vr': {'options': [{'label': 'Morsure magique', 'impact': (1, [], '+1 à une arme naturelle'), 'cible_note': ['arme', 'naturelle']}], 'src_idx': 'runic-body'}},
 'magic-missile': {'vp2': {}},
 'magic-mouth': {'vp2': {}, 'vr': {'src_idx': 'embedded-message'}},
 'magic-stone': {'vp2': {}},
 'magic-weapon': {'vp2': {}},
 'magnificent-mansion': {'vp2': {}},
 'major-image': {'vp2': {'src_idx': 'illusory-scene'}, 'vr': {'src_idx': 'illusory-scene'}},
 'massacre': {'vp2': {}, 'vr': {}},
 'maze': {'vp2': {}, 'vr': {'src_idx': 'quandary'}},
 'meld-into-stone': {'vp2': {}, 'vr': {'src_idx': 'one-with-stone'}},
 'mending': {'vp2': {}, 'vr': {}},
 'message': {'vp2': {}, 'vr': {}},
 'meteor-swarm': {'vp2': {}, 'vr': {'src_idx': 'falling-stars'}},
 'mind-blank': {'vp2': {}},
 'mind-probe': {'vp2': {}, 'vr': {}},
 'mindlink': {'vp2': {}, 'vr': {}},
 'minor-illusion': {'vp2': {'src_idx': 'ghost-sound'}, 'vr': {'src_idx': 'figment'}},
 'miracle': {'vp2': {}},
 'mirror-image': {'vp2': {}},
 'misdirection': {'vp2': {}},
 'mislead': {'vp2': {}, 'vr': {}},
 'modify-memory': {'vp2': {}},
 'monstrous-physique-i': {'vp2': {'options': [{'label': 'Physique monstrueux I', 'impact': ('plein', ['monstre', 'forme'], 'petit ou moyen')}], 'src_idx': 'monstrosity-form'}, 'vr': {'options': [{'label': 'Physique monstrueux I', 'impact': ('plein', ['monstre', 'forme'], 'petit ou moyen')}], 'src_idx': 'monstrosity-form'}},
 'negate-aroma': {'vp2': {}},
 'nightmare': {'vp2': {}, 'vr': {}},
 'nondetection': {'vp2': {}, 'vr': {'src_idx': 'veil-of-privacy'}},
 'object-reading': {'vp2': {}, 'vr': {}},
 'overwhelming-presence': {'vp2': {}, 'vr': {}},
 'paranoia': {'vp2': {}, 'vr': {}},
 'pass-without-trace': {'vp2': {}},
 'passwall': {'vp2': {}},
 'penumbral-disguise': {'vp2': {}},
 'phantasmal-killer': {'vp2': {}, 'vr': {'src_idx': 'vision-of-death'}},
 'phantom-steed': {'vp2': {}, 'vr': {'src_idx': 'marvelous-mount'}},
 'plane-shift': {'vp2': {}},
 'plant-shape-i': {'vp2': {'options': [{'label': 'Forme végétale I', 'impact': ('plein', ['plante', 'forme'], 'une plante petite ou moyenne')}], 'src_idx': 'plant-form'}, 'vr': {'options': [{'label': 'Forme végétale I', 'impact': ('plein', ['plante', 'forme'], 'une plante petite ou moyenne')}], 'src_idx': 'plant-form'}},
 'polar-ray': {'vp2': {}, 'vr': {'src_idx': 'arctic-rift'}},
 'possession': {'vp2': {'options': [{'label': 'Possession'}]}, 'vr': {'options': [{'label': 'Possession'}]}},
 'power-word-blind': {'vp2': {}},
 'power-word-kill': {'vp2': {}},
 'power-word-stun': {'vp2': {}},
 'prestidigitation': {'vp2': {}, 'vr': {}},
 'prismatic-spray': {'vp2': {}},
 'prismatic-wall': {'vp2': {}},
 'private-sanctum': {'vp2': {}, 'vr': {'src_idx': 'peaceful-bubble'}},
 'produce-flame': {'vp2': {}, 'vr': {'src_idx': 'ignition'}},
 'project-image': {'vp2': {}, 'vr': {}},
 'protection-from-evil-and-good': {'vp2': {'src_idx': 'protection'}, 'vr': {'src_idx': 'protection'}},
 'protection-from-poison': {'vp2': {'src_idx': 'neutralize-poison'}, 'vr': {'src_idx': 'cleanse-affliction'}},
 'purify-food-and-drink': {'vp2': {}},
 'putrefy-food-and-drink': {'vp2': {}},
 'pyrotechnics': {'vp2': {}},
 'quench': {'vp2': {}},
 'raise-dead': {'vp2': {}, 'vr': {}},
 'rally-point': {'vp2': {}},
 'ray-of-enfeeblement': {'vp2': {}, 'vr': {'src_idx': 'enfeeble'}},
 'ray-of-frost': {'vp2': {}},
 'regenerate': {'vp2': {'impact': (15, ['vie', 'repousse'], '15 points rendus à chaque instant ; les membres perdus repoussent'), 'guerit': True}, 'vr': {'impact': (15, ['vie', 'repousse'], '15 points rendus à chaque instant ; les membres perdus repoussent'), 'guerit': True}},
 'remove-curse': {'vp2': {}},
 'remove-fear': {'vp2': {}, 'vr': {'src_idx': 'clear-mind'}},
 'repulsion': {'vp2': {}, 'vr': {}},
 'resilient-sphere': {'vp2': {}, 'vr': {'src_idx': 'containment'}},
 'resist-energy': {'vp2': {}, 'vr': {}},
 'resplendent-mansion': {'vp2': {}, 'vr': {}},
 'retrocognition': {'vp2': {}, 'vr': {}},
 'revealing-light': {'vr': {}},
 'reverse-gravity': {'vp2': {}},
 'righteous-might': {'vp2': {}},
 'rope-trick': {'vp2': {}, 'vr': {'src_idx': 'liminal-doorway'}},
 'rusting-grasp': {'vp2': {}},
 'sacred-nimbus': {'vp2': {}},
 'sanctuary': {'vp2': {}, 'vr': {}},
 'scintillating-pattern': {'vp2': {}},
 'scorching-ray': {'vp2': {}},
 'scrying': {'vp2': {}, 'vr': {}},
 'sculpt-sound': {'vp2': {}},
 'searing-light': {'vp2': {}},
 'secret-chest': {'vp2': {}, 'vr': {'src_idx': 'imaginary-lockbox'}},
 'secret-page': {'vp2': {}},
 'secure-shelter': {'vp2': {'src_idx': 'cozy-cabin'}, 'vr': {'src_idx': 'cozy-cabin'}},
 'see-invisibility': {'vp2': {}, 'vr': {'src_idx': 'see-the-unseen'}},
 'sending': {'vp2': {}, 'vr': {}},
 'shadow-walk': {'vp2': {}, 'vr': {'src_idx': 'umbral-journey'}},
 'shapechange': {'vp2': {}},
 'shatter': {'vp2': {}, 'vr': {}},
 'shield': {'vp2': {}, 'vr': {}},
 'shield-other': {'vp2': {}},
 'shifting-sand': {'vp2': {}},
 'shillelagh': {'vp2': {}},
 'shocking-grasp': {'vp2': {}, 'vr': {'src_idx': 'thunderstrike'}},
 'shrink-item': {'vp2': {}, 'vr': {}},
 'silence': {'vp2': {}, 'vr': {}},
 'silent-image': {'vp2': {'src_idx': 'illusory-object'}, 'vr': {'src_idx': 'illusory-object'}},
 'sleep': {'vp2': {}, 'vr': {}},
 'slow': {'vp2': {}, 'vr': {}},
 'snowball': {'vp2': {'impact': (5, ['neige', 'froid'], '2d4 en moyenne')}},
 'solid-fog': {'vp2': {}},
 'soul-bind': {'vp2': {'src_idx': 'bind-soul'}, 'vr': {'src_idx': 'seize-soul'}},
 'sound-burst': {'vp2': {}},
 'speak-with-animals': {'vp2': {}, 'vr': {}},
 'speak-with-dead': {'vp2': {'src_idx': 'talking-corpse'}, 'vr': {'src_idx': 'talking-corpse'}},
 'speak-with-plants': {'vp2': {}, 'vr': {}},
 'spectral-hand': {'vp2': {}, 'vr': {'src_idx': 'ghostly-carrier'}},
 'spell-immunity': {'vp2': {'options': [{'label': 'Immunité contre les sorts', 'impact': (1, ['immunité', 'sort'], 'un sort désigné sans effet'), 'impact_sats': [(4, ['seuil', 'niveau'])]}]}},
 'spell-turning': {'vp2': {}, 'vr': {'src_idx': 'spell-riposte'}},
 'spider-climb': {'vp2': {}},
 'spike-stones': {'vp2': {}},
 'spiritual-weapon': {'vp2': {}, 'vr': {'src_idx': 'spiritual-armament'}},
 'stabilize': {'vp2': {}, 'vr': {}},
 'status': {'vp2': {}, 'vr': {}},
 'stinking-cloud': {'vp2': {}},
 'stone-shape': {'vp2': {'src_idx': 'shape-stone'}, 'vr': {'src_idx': 'shape-stone'}},
 'stone-tell': {'vp2': {}},
 'stone-to-flesh': {'vp2': {}},
 'stoneskin': {'vp2': {}},
 'storm-of-vengeance': {'vp2': {}, 'vr': {'src_idx': 'wrathful-storm'}},
 'suggestion': {'vp2': {}, 'vr': {}},
 'summon-dragon': {'vp2': {}, 'vr': {}},
 'summon-instrument': {'vp2': {}, 'vr': {}},
 'summon-monster-i': {'vp2': {'options': [{'label': 'Rang I — 1 être de puissance ½ — lumineux', 'impact': (2, ['fractionné'], 'puissance ½'), 'cible_sym': ['lumineux']}], 'src_idx': 'summon-celestial'}, 'vr': {'options': [{'label': 'Rang I — 1 être de puissance ½ — lumineux', 'impact': (2, ['fractionné'], 'puissance ½'), 'cible_sym': ['lumineux']}], 'src_idx': 'summon-celestial'}},
 'summon-natures-ally-i': {'vp2': {'options': [{'label': 'Rang I — 1 être de puissance ½', 'impact': (2, ['fractionné'], 'puissance ½')}], 'src_idx': 'summon-animal'}, 'vr': {'options': [{'label': 'Rang I — 1 être de puissance ½', 'impact': (2, ['fractionné'], 'puissance ½')}], 'src_idx': 'summon-animal'}},
 'summon-stampede': {'vr': {}},
 'sunburst': {'vp2': {}, 'vr': {}},
 'synaptic-pulse': {'vp2': {'options': [{'label': 'Pulsation synaptique'}]}, 'vr': {'options': [{'label': 'Pulsation synaptique'}]}},
 'synesthesia': {'vp2': {'options': [{'label': 'Synesthésie'}]}, 'vr': {'options': [{'label': 'Synesthésie'}]}},
 'telekinesis': {'vp2': {'src_idx': 'telekinetic-haul'}, 'vr': {'src_idx': 'telekinetic-haul'}},
 'telekinetic-maneuver': {'vp2': {}, 'vr': {}},
 'telekinetic-projectile': {'vp2': {}, 'vr': {}},
 'telepathic-bond': {'vp2': {}},
 'telepathy': {'vp2': {}, 'vr': {}},
 'teleport': {'vp2': {}, 'vr': {}},
 'threefold-aspect': {'vp2': {}, 'vr': {}},
 'time-stop': {'vp2': {}},
 'tongues': {'vp2': {}},
 'touch-of-idiocy': {'vp2': {}},
 'trade-items': {'vr': {}},
 'transmute-rock-to-mud': {'vp2': {'src_idx': 'transmute-rock-and-mud'}},
 'tree-shape': {'vp2': {}, 'vr': {'src_idx': 'one-with-plants'}},
 'tree-stride': {'vp2': {}},
 'true-seeing': {'vp2': {}},
 'true-strike': {'vp2': {}},
 'undetectable-alignment': {'vp2': {}},
 'unseen-servant': {'vp2': {}, 'vr': {'src_idx': 'phantasmal-minion'}},
 'vampiric-touch': {'vp2': {}},
 'ventriloquism': {'vp2': {}, 'vr': {}},
 'vermin-shape-i': {'vp2': {'options': [{'label': 'Forme de vermine I', 'impact': ('plein', ['vermine', 'forme'], 'petite ou moyenne')}], 'src_idx': 'insect-form'}, 'vr': {'options': [{'label': 'Forme de vermine I', 'impact': ('plein', ['vermine', 'forme'], 'petite ou moyenne')}], 'src_idx': 'insect-form'}},
 'vomit-swarm': {'vp2': {}, 'vr': {}},
 'wail-of-the-banshee': {'vp2': {}},
 'wall-of-fire': {'vp2': {}, 'vr': {}},
 'wall-of-force': {'vp2': {}, 'vr': {}},
 'wall-of-ice': {'vp2': {}, 'vr': {}},
 'wall-of-stone': {'vp2': {}, 'vr': {}},
 'wall-of-thorns': {'vp2': {}, 'vr': {}},
 'water-breathing': {'vp2': {}, 'vr': {}},
 'water-walk': {'vp2': {}, 'vr': {}},
 'waterproof': {'vr': {}},
 'web': {'vp2': {}, 'vr': {}},
 'weird': {'vp2': {'impact': (56, [], '16d6 en moyenne')}, 'vr': {'src_idx': 'phantasmagoria', 'impact': (56, [], '16d6 en moyenne')}},
 'whirlwind': {'vp2': {'impact': (28, ['choc', 'tourbillon'], '5d10 en moyenne')}},
 'wind-walk': {'vp2': {}, 'vr': {'src_idx': 'migration'}},
 'wind-wall': {'vp2': {'src_idx': 'wall-of-wind'}, 'vr': {'src_idx': 'wall-of-wind'}},
 'wish': {'vp2': {}, 'vr': {'src_idx': 'manifestation'}},
 'wood-shape': {'vp2': {'src_idx': 'shape-wood'}, 'vr': {'src_idx': 'shape-wood'}},
 'zone-of-truth': {'vp2': {}, 'vr': {'src_idx': 'ring-of-truth'}},
}
for _k, _v in PF2_VERSIONS.items(): FICHES[_k].update(_v)

# ----- Reprise du 17 novembre : ni lune ni soleil dans Inarama (décision de Baptiste) -----
# Les sorts « de lune » et « de soleil » deviennent des sorts d'énergie astrale, à deux formes : lumineuse (l'Étoile) et ténébreuse (l'Abysse).
def _AST(k, fr, words, why_l, why_t, v=P):
    f = FICHES[k]; subs = f.get("options") or [{"label": None}]
    ops = []
    for s in subs:
        w = list(words) + [x for x in (s.get("impact") or (0, []))[1] if x in ("éclat",)]
        for face, mot, why in (("Forme lumineuse", "lumineux", why_l), ("Forme ténébreuse", "ténébreux", why_t)):
            lab = face if (s["label"] is None or len(subs) == 1 or s is subs[0]) else f"{s['label'].replace('du soleil', 'astral').replace('de l' + chr(39) + 'aube', 'astral')} — {face.lower()}"
            ops.append({**{a: b for a, b in s.items() if a not in ("label", "impact")}, "label": lab, "impact": (v, w + [mot], why + (" ; plus ardent" if "éclat" in w else ""))})
    f.update(fr=fr, impact=(v, list(words), why_l), options=ops)
    for a in f.get("alt", []): a["why"] = "l'énergie astrale"
for _k, _fr in (("moonbeam", "Faisceau astral"), ("sunbeam", "Rayon astral"), ("sunburst", "Explosion astrale")):
    FICHES[_k].update(fr=_fr, options=[O("Forme lumineuse"), O("Forme ténébreuse", face="ténébreux")])
    for _a in FICHES[_k].get("alt", []): _a["why"] = "l'énergie astrale"
FICHES["lunar-veil"].update(fr="Voile astral")
_AST("moonstruck", "Frénésie astrale", ["fureur", "folie"], "l'éclat de l'Étoile la rend enragée et confuse", "l'ombre de l'Abysse la rend enragée et confuse")
_AST("sunstalker", "Traqueur astral", ["invisibilité"], "invisible tant qu'il reste en pleine lumière", "invisible tant qu'il reste en pleine obscurité")
_AST("cloak-of-shade", "Manteau d'ombre", ["abri", "chaleur"], "à l'abri des ardeurs de l'Étoile : chaleur et éblouissement", "à l'abri des rigueurs de l'Abysse : froid et ténèbres")
_AST("blinding-ray", "Rayon aveuglant", ["rayon", "cécité"], "des rayons d'éclat qui aveuglent", "des rayons d'ombre qui aveuglent")
_AST("moonrise-arrow", "Flèche astrale", ["argent", "trait"], "des traits de lueur d'argent, qui frappent comme l'argent", "des traits d'ombre d'argent, qui frappent comme l'argent")
_AST("morning-sun", "Sphère astrale", ["sphère", "jour"], "une sphère d'éclat, vive comme le plein jour", "une sphère d'ombre, noire comme la pleine nuit")
_AST("shield-of-the-dawnflower", "Bouclier astral", ["bouclier", "brûlure"], "un disque d'éclat qui brûle qui me frappe", "un disque d'ombre qui glace qui me frappe")
_AST("blade-of-light", "Lame astrale", ["arme", "charge"], "une arme chargée d'éclat, fléau des morts-vivants", "une arme chargée d'ombre, fléau des êtres de lumière")
_AST("fear-the-sun", "Crainte astrale", ["aveuglement"], "la lumière l'aveugle", "l'obscurité l'aveugle, même s'il y voyait")
_AST("fury-of-the-sun", "Fureur astrale", ["malédiction", "chaleur"], "un coup de chaleur intérieur", "un coup de froid intérieur")
_AST("sun-metal", "Métal astral", ["embrasement"], "une arme qui s'embrase d'un feu clair sans se consumer", "une arme qui s'embrase d'un feu noir sans se consumer")
_AST("suns-disdain", "Dédain astral", ["aveuglement", "faiblesse"], "la lumière l'aveugle et la blesse", "l'obscurité l'aveugle et la blesse")

# ----- Pathfinder 2, lot 14 : quatre sorts remaniés mal appariés, et trois formes base / maximale -----
PF2_REM4 = {
"hidebound": PR("Cuir épais", SEP, 2, ["cuir", "écaille"], 5, "sa peau se couvre de cuir ou d'écailles : 5 retranché aux coups jusqu'à son prochain instant", **_RES),
"whispers-of-the-void": PR("Murmures du vide", NE, P, ["murmure", "secret", "ténébreux"], 18, "4d8 en moyenne à chaque instant ; vidés de leur force"),
"lignify": PR("Lignification", TR, 3, ["bois", "pétrification", "lenteur"], why="sa chair devient bois peu à peu : ralentie de plus en plus, puis statue de bois", fam="A"),
"eagles-cry": PR("Cri de l'aigle", NF, P, ["cri", "effroi"], 18, "4d8 en moyenne ; effrayés, les plus atteints fuient"),
}
FICHES.update(PF2_REM4)
_R("spirit-ward", options=[
    O("Forme de base", impact=(1, ["esprit", "hantise"], "au toucher, d'un geste : 1 ajouté contre les esprits et les hantises")),
    O("Forme maximale", cible=P, aoe=_S(30), impact=(1, ["esprit", "hantise"], "moi et tous mes alliés alentour : 1 ajouté contre les esprits et les hantises ; tout l'instant y passe"))])
_R("elemental-breath", options=[
    O("Forme de base", impact=(33, ["souffle", "élément", "hasard"], "6d10 en moyenne, d'un élément tiré au sort")),
    O("Forme maximale", impact=(39, ["souffle", "élément", "choix"], "l'élément choisi, jusqu'à 7d10 en moyenne pour le feu ; tout l'instant y passe"))])
_R("splinter-volley", options=[
    O("Forme de base", impact=(14, ["écharde", "saignement"], "4d6 en moyenne à une cible")),
    O("Forme maximale", qty_cible=2, impact=(14, ["écharde", "saignement"], "4d6 en moyenne à chacune de deux cibles ; tout l'instant y passe"))])

# ----- Pathfinder 2 : corrections de la relecture inversée (18 novembre) -----
_R("charitable-urge", dur=(6, "SECONDES")); _R("earthbind", dur=(6, "SECONDES")); _R("equal-footing", dur=(6, "SECONDES")); _R("lignify", dur=(P, None))
_R("camel-spit", loc=(5, "METRES", "4,5 m, arrondi à 5"))
_R("misty-memory", aoe=_S(30)); _R("pollen-pods", aoe=_S(15))
_R("soothing-spring", aoe={"type": "cylinder", "size": 10, "height": 5})

# ----- Pathfinder 2, lot 15 : sorts focalisés gardés — magicien et sorcière -----
# Tri : pf2work/focal.py. Gardé si l'effet tient comme un sort ordinaire, sans la classe.
PF2_FOCAL_ECARTE = {}       # rempli lot par lot
PF2_FOCAL_ECARTE.update({"personal-runewell": "puits runique de Thassilon (Golarion)", "capital-dividend": "régime des prophéties de Kalistrade (Golarion)",
 "invisibility-cloak": "même effet que l'Invisibilité déjà publiée", "diviners-sight": "remplace un jet de dé : pure mécanique de jeu",
 "life-siphon": "ne fait que modifier le sort qu'on lance", "elemental-tempest": "ne fait que modifier le sort qu'on lance",
 "interdisciplinary-incantation": "reprend le sort d'un autre lanceur : mécanique de classe", "cackle": "ne fait que prolonger un autre sort", "patrons-puppet": "économie d'actions du familier"})
PF2_FOC1 = {
"all-encompassing-hunger": N2("Faim dévorante", 3, ["dévoration", "ténébreux"], 4, "1d6 en moyenne ; si elle en meurt, je gagne autant de vie d'emprunt", **_VIV),
"crescent-scepter": P2("Sceptre d'autorité", SEP, 1, ["insigne", "crainte"], why="l'objet que je brandis paraît l'insigne du pouvoir que chacun redoute : qui veut me frapper peut y renoncer, effrayé", cible_note=["garde"]),
"cutting-eye": P2("Œil envieux", SEP, 1, ["envie", "parade"], 2, "2 ajouté à ma défense ou à ma résistance contre ce qui me vise ; il ne me prend plus au dépourvu", cond=["coup"], cible_note=["garde"]),
"hearts-hook": P2("Crochet du cœur", ATT, 4, ["rencontre", "attirance"], why="deux êtres poussés l'un vers l'autre : chacun doit d'abord s'approcher de l'autre", qty_cible=2, **_PSY),
"precious-gleam": P2("Éclat précieux", INT, 4, ["acier", "argent", "affinage"], 4, "l'arme devient de fer froid, d'argent ou d'acier fin : 1d6 en moyenne de plus à son prochain coup", cible_obj=["arme"], fam="A"),
"vengeful-glare": P2("Regard vengeur", NF, 3, ["regard", "froid", "feu"], 2, "1d4 en moyenne, de froid ou de feu ; 1 de plus par instant si je l'avais déjà blessée", fam="A"),
"unexpected-windfall": P2("Aubaine imprévue", V("mouvement", True), 3, ["trésor", "fardeau"], why="une pluie de pièces et de pierres lourdes : elle ploie sous la charge"),
"friendly-push": P2("Poussée amicale", V("mouvement"), 2, ["poussée", "mètres"], 3, "je propulse un allié de 3 m en ligne droite, même vers le haut, à chaque instant"),
"rapid-retreat": P2("Retraite rapide", TP2, 1, ["téléportation", "esquive"], 6, "je me téléporte à 6 m, hors du danger, et ce qui me frappait me blesse moins", cond=["coup"]),
"force-bolt": E2("Trait de force", 3, ["trait", "infaillible"], 4, "1d4 + 1 en moyenne ; il touche toujours"),
"energy-absorption": P2("Absorption d'énergie", SEP, 1, ["énergie", "absorption"], 15, "15 retranché à l'acide, au froid, à la foudre ou au feu qui me frappe", cond=["coup"], fam="A", **_RES),
"earthworks": P2("Terrassement", TR, P, ["terre", "butte"], why="de petites buttes sortent du sol : terrain pénible, qu'on peut dégager", fam="A"),
"community-restoration": P2("Réconfort partagé", INT, 1, ["partage", "vigueur"], 2, "quand j'aide mes alliés par un sort : 2 points de vie d'emprunt par cran du sort, pour moi et à répartir entre eux", cond=["sort"]),
"shifting-form": P2("Forme changeante", TR, 1, ["forme", "choix"], why="un don au choix", options=[
    O("Vitesse", impact=(6, ["forme", "vitesse", "mètres"], "6 m de plus par instant")), O("Escalade ou nage", impact=(P, ["forme", "escalade", "nage"], "je grimpe ou nage à demi-allure")),
    O("Vision dans le noir", impact=(P, ["forme", "nuit", "regard"], "je vois dans le noir")), O("Griffes", impact=(5, ["forme", "griffe"], "des griffes de 1d8 en moyenne"))]),
"hand-of-the-apprentice": E2("Main de l'apprenti", 3, ["arme", "lancer", "retour"], why="l'arme que je tiens vole frapper au loin comme si je la maniais, puis me revient"),
"augment-summoning": P2("Convocation augmentée", INT, 2, ["invoqué", "renfort"], 1, "1 ajouté à tout ce que fait l'être que j'ai convoqué", cond=["convoqué"], vr={"src_idx": "fortify-summoning"}),
"call-of-the-grave": N2("Appel de la tombe", 3, ["rayon", "nausée"], 1, "nausée de 1 ; au mieux, nausée de 2 et lenteur", vr={"src_idx": "scramble-body"}, **_VIV),
"charming-words": P2("Mots charmeurs", REL, 3, ["murmure", "désarmement"], why="elle ne peut plus s'en prendre à moi, un instant", vr={"src_idx": "charming-push"}, **_PSY),
"dimensional-steps": P2("Pas dimensionnel", TP2, 1, ["téléportation", "mètres"], 6, "je me téléporte à 6 m, à vue"),
"dread-aura": P2("Aura d'effroi", PEUR, P, ["aura", "effroi"], 1, "mes ennemis alentour sont effrayés de 1, sans répit", vr={"src_idx": "spiral-of-horrors"}, **_PSY),
"physical-boost": P2("Regain physique", INT, 2, ["corps", "élan"], 2, "2 ajouté à son prochain effort du corps ou à sa prochaine esquive", **_VIV),
"protective-ward": P2("Garde protectrice", SEP, P, ["aura", "garde"], 1, "1 ajouté à la défense, pour moi et mes alliés ; l'aura grandit tant que je la soutiens", impact_sats=[(9, ["rayon", "mètres"])], vr={"src_idx": "protective-wards"}),
"vigilant-eye": P2("Œil vigilant", VIS, 1, ["œil", "capteur", "invisible"], why="un œil invisible posé à vue, par lequel je vois, une heure durant", discret=True, vr={"src_idx": "rune-of-observation"}),
"warped-terrain": P2("Terrain faussé", EXI, P, ["terrain", "fantasme"], why="des embûches illusoires couvrent le sol : terrain pénible pour qui y croit"),
"efficient-apport": P2("Rappel commode", TP2, 4, ["objet", "main"], why="un petit objet à vue se téléporte dans ma main", cible_obj=["objet"], vr={"src_idx": "reclined-apport"}),
"unravel-knowledge": P2("Savoir détricoté", NORD, 3, ["souvenir", "aptitude", "oubli"], 14, "un de ses savoir-faire s'embrume : 3d8 en moyenne chaque fois qu'elle s'en sert", cible_note=["mémoire"]),
"censure-falsehoods": P2("Mensonges châtiés", NQ, 3, ["mensonge", "crapaud", "nausée"], why="qui m'a menti crache crapauds et serpents à chaque mot : nausée, et la parole lui coûte"),
"blood-ward": P2("Garde du sang", SEP, 2, ["espèce", "désigné"], 1, "1 ajouté à sa défense et à sa résistance contre une sorte d'êtres désignée", cible_note=["garde", "résistance"]),
"curse-of-death": N2("Malédiction de mort", 3, ["malédiction", "cœur", "mort"], why="son cœur se serre d'effroi : le mal empire par degrés, jusqu'à la mort", dur=(1, "MINUTES")),
"deceivers-cloak": P2("Manteau du trompeur", NVIS, 1, ["apparence", "leurre"], why="je parais un autre être de même carrure"),
"elemental-betrayal": P2("Trahison élémentaire", NINT, 3, ["élément", "faille"], 2, "l'élément choisi la blesse de 2 de plus à chaque fois", fam="A", **_RES),
"life-boost": P2("Regain de vie", HE, 2, ["vie"], 2, "2 points rendus à chaque instant, quatre instants durant", guerit=True),
"malicious-shadow": P2("Ombre malveillante", TR, 3, ["ombre", "frappe"], why="son ombre prend une forme mortelle et la frappe à chaque instant, sans la quitter", sens=[("vue", None)], manif=["ombre"]),
"needle-of-vengeance": P2("Aiguille de vengeance", NORD, 3, ["aiguille", "interdit"], 2, "2 à l'esprit chaque fois qu'elle s'en prend à l'être que j'ai nommé", **_PSY),
"personal-blizzard": E2("Blizzard personnel", 3, ["blizzard", "persistance"], 4, "1d6 en moyenne de froid, puis autant à chaque instant ; la neige la suit et lui brouille la vue"),
"phase-familiar": P2("Familier déphasé", SEP, 2, ["brume", "déphasage"], 5, "mon compagnon devient brume un instant : 5 retranché au coup qui le frappe", cond=["compagnon", "coup"], **_RES),
"restorative-moment": P2("Instant réparateur", HE, 2, ["vie", "temps", "repos"], 1, "le bienfait d'un jour passé : ses maux durables reculent de 1, et elle lutte à nouveau contre ce qui l'afflige", guerit=True),
"veil-of-dreams": P2("Voile de rêves", NORD, 3, ["torpeur", "rêverie"], 1, "somnolente : 1 retranché à sa vigilance, à ses coups et à sa volonté", **_PSY),
"clinging-ice": E2("Glace tenace", 3, ["neige", "lenteur", "mètres"], 2, "1d4 en moyenne de froid ; ralentie de 1,5 m"),
"discern-secrets": P2("Secrets percés", VIS, 2, ["secret", "flair"], 1, "1 ajouté pour se souvenir, chercher ou percer une intention"),
"evil-eye": P2("Mauvais œil", PEUR, 3, ["œil", "effroi"], 1, "effrayée de 1, sans répit tant que je la vois", **_PSY),
"nudge-fate": P2("Coup de pouce au destin", INT, 2, ["destin", "ajustement"], 1, "une fois : 1 ajouté à l'essai qui allait manquer de peu"),
"shroud-of-night": P2("Linceul de nuit", NVIS, 4, ["nuit", "voile"], why="ses yeux sont voilés de ténèbres : tout lui paraît estompé, à moins de voir dans le noir"),
"stoke-the-heart": P2("Cœur attisé", INT, 2, ["ferveur", "frappe"], 2, "2 ajouté à ses coups"),
"wilding-word": P2("Parole sauvage", REL, 4, ["parenté", "retenue"], 2, "la bête ou la plante répugne à me nuire : 2 retranché à ses coups contre moi", cible_note=["bête"]),
"pact-broker": P2("Pacte de paix", REL, 3, ["pacte", "trêve"], 1, "j'offre la paix : si elle la rompt, 1 retranché à ses coups contre moi et les miens", **_PSY),
"return-the-favor": P2("Service rendu", INT, 2, ["dette", "vigueur"], 12, "à l'allié qui vient de m'aider : 12 points de vie d'emprunt pour une minute", cond=["aide"]),
"over-the-coals": P2("Sur les charbons", ORD, 3, ["dette", "exigence", "châtiment"], 27, "je réclame mon dû : payer, obéir ou céder ; si elle refuse, vidée, et 6d8 en moyenne à chaque instant", **_PSY),
"glacial-heart": E2("Cœur de glace", 3, ["gel", "lenteur", "statue"], 35, "10d6 en moyenne ; ralentie, et peu à peu changée en glace"),
"spirit-object": P2("Objet animé", V("mouvement"), 4, ["objet", "pattes", "course"], 8, "l'objet se dote de pattes et court 7,5 m, arrondi à 8 ; il peut frapper à l'arrivée", cible_obj=["objet"]),
"buzzing-bites": P2("Morsures bourdonnantes", NE, 3, ["insecte", "morsure", "nausée"], 2, "1d4 en moyenne à chaque instant où je soutiens le sort ; la nausée"),
"stumbling-curse": P2("Malédiction du faux pas", NORD, 3, ["malédiction", "trajectoire"], 2, "2 retranché à son agilité et à sa force ; ses déplacements dévient"),
}
for _k in "all-encompassing-hunger crescent-scepter cutting-eye hearts-hook precious-gleam vengeful-glare unexpected-windfall friendly-push rapid-retreat earthworks community-restoration unravel-knowledge censure-falsehoods".split():
    PF2_FOC1[_k]["src"] = "pf2r"
FICHES.update(PF2_FOC1)
FICHES["grasping-vine"].update(vr={})      # la Liane préhensile focalisée : version remaniée de la page déjà publiée

# ----- Pathfinder 2, lot 16 : sorts focalisés gardés — barde, druide, rôdeur, champion, moine, magus -----
PF2_FOCAL_ECARTE.update({"counter-performance": "remplace un jet de sauvegarde par un jet de représentation", "fortissimo-composition": "ne fait que renforcer une autre composition",
 "lingering-composition": "ne fait que prolonger une autre composition", "inspire-heroics": "ne fait que renforcer une autre composition", "silvers-refrain": "chant d'une faction de Golarion",
 "primal-summons": "ne fait que modifier la prochaine convocation", "wild-shape": "formes données par les dons de la classe", "untamed-form": "formes données par les dons de la classe",
 "wild-morph": "effets donnés par les dons de la classe", "untamed-shift": "effets donnés par les dons de la classe", "snare-hopping": "déplace un piège de rôdeur",
 "shields-of-the-spirit": "aura du champion", "litany-of-depravity": "n'existe que par l'alignement", "litany-of-righteousness": "n'existe que par l'alignement",
 "clinging-shadows-stance": "posture de moine", "wild-winds-stance": "posture de moine", "medusas-wrath": "méduse, créature non admise (décision de Baptiste)",
 "turbulent-tide": "frappe du magus", "cascade-countermeasure": "posture du magus", "dimensional-assault": "frappe du magus", "force-fang": "frappe du magus",
 "shielding-strike": "frappe du magus", "shooting-star": "frappe du magus", "spinning-staff": "frappe du magus", "thunderous-strike": "frappe du magus"})
PF2_FONDU.update({"touch-of-corruption": "lay-on-hands"})
_CHANT = dict(sens=[("ouïe", None)], manif=["chant"])
PF2_FOC2 = {
"fatal-aria": P2("Aria fatale", NE, 3, ["musique", "perfection", "mort"], 50, "une musique si parfaite qu'on en meurt ; les plus forts y perdent 50, ou restent hébétés", **_PSY, **_CHANT),
"hymn-of-healing": P2("Hymne de guérison", HE, 2, ["vie", "hymne"], 2, "2 points rendus à chaque instant, et 2 de vie d'emprunt", guerit=True, **_CHANT),
"loremasters-etude": P2("Étude du maître du savoir", INT, 2, ["savoir", "essai"], why="pour se souvenir : le meilleur de deux essais", cible_note=["mémoire"], cond=["souvenir"]),
"ode-to-ouroboros": P2("Ode à l'ouroboros", V("nature", True), 2, ["agonie", "sursis"], 1, "l'agonie s'arrête à 1 cran de la mort", cond=["mourant"], **_CHANT),
"soothing-ballad": P2("Ballade apaisante", HE, 2, ["vie", "ballade"], 32, "7d8 en moyenne à chacun", qty_cible=10, guerit=True, **_CHANT, options=[
    O("Guérir", impact=(32, ["vie", "ballade"], "7d8 en moyenne à chacun")),
    O("Rassurer", impact=(P, ["effroi", "délivrance", "ballade"], "défait les peurs")),
    O("Délier", impact=(P, ["paralysie", "délivrance", "ballade"], "défait les paralysies"))]),
"symphony-of-the-unfettered-heart": P2("Symphonie du cœur délié", DISP, 2, ["entrave", "délivrance"], why="défait ce qui la tient : prise, immobilité, paralysie, lenteur, étourdissement", **_CHANT),
"song-of-the-fallen": P2("Chant des tombés", V("existence"), 4, ["élégie", "mort", "sursaut"], 60, "quatre morts se relèvent et agissent comme vivants, sur 60 points de vie d'emprunt", qty_cible=4, cond=["mort"], **_CHANT, options=[
    O("Élégie", impact=(60, ["élégie", "mort", "sursaut"], "quatre morts se relèvent et agissent comme vivants, sur 60 points de vie d'emprunt")),
    O("Thrène", verb=NE, cond=["MORTVIVANT"], impact=(100, ["thrène", "repos", "lumineux"], "quatre morts-vivants rappelés au repos : 100, et ralentis une minute"))]),
"song-of-marching": P2("Chant de marche", INT, P, ["marche", "allure"], why="moi et mes alliés forçons l'allure une heure durant, sans fatigue", **_CHANT),
"song-of-strength": P2("Chant de force", INT, P, ["force", "aplomb"], 1, "1 ajouté aux tours de force et pour n'être ni désarmé, ni poussé, ni renversé", **_CHANT),
"allegro": P2("Allegro", INT, 2, ["tempo", "hâte"], why="un geste de plus dans l'instant : frapper ou se déplacer", **_CHANT),
"dirge-of-doom": P2("Chant funèbre", PEUR, P, ["glas", "effroi"], 1, "mes ennemis alentour sont effrayés de 1, sans répit", **_PSY, **_CHANT),
"house-of-imaginary-walls": P2("Maison aux murs imaginaires", EXI, P, ["mur", "mime", "fantasme"], why="un mur mimé de 3 m sur 3, solide pour qui y croit, même sans corps", forme=_MUR(3, 3)),
"inspire-competence": P2("Inspiration talentueuse", INT, 2, ["encouragement", "aide"], why="mes encouragements valent une aide préparée pour la tâche choisie", vr={"src_idx": "uplifting-overture"}, **_CHANT),
"inspire-courage": P2("Inspiration vaillante", INT, P, ["courage"], 1, "1 ajouté aux coups, aux blessures et contre la peur", vr={"src_idx": "courageous-anthem"}, **_CHANT),
"inspire-defense": P2("Inspiration défensive", SEP, P, ["rempart"], 1, "1 ajouté à la défense et aux résistances ; les coups blessent un peu moins", vr={"src_idx": "rallying-anthem"}, **_CHANT),
"triple-time": P2("Triple mesure", INT, P, ["tempo", "vitesse", "mètres"], 3, "3 m de plus par instant", **_CHANT),
"heal-animal": P2("Guérison animale", HE, 2, ["vie"], 5, "1d8 en moyenne", cible_note=["bête"], guerit=True, options=[
    O("Forme de base", loc=(2, "METRES", "au toucher"), impact=(5, ["vie"], "1d8 en moyenne, au toucher, d'un geste")),
    O("Forme maximale", impact=(13, ["vie"], "1d8 + 8 en moyenne, à distance"))]),
"impaling-briars": P2("Ronces empaleuses", TR, P, ["ronce", "entrave"], 35, "le sol devient ronces ; à chaque instant : retenir, encombrer ou dresser un mur ; une ronce empale de 10d6 en moyenne", comb="Plante"),
"storm-lord": P2("Seigneur des tempêtes", EXI, P, ["nuée", "foudre", "temps"], 35, "le ciel s'assombrit ; à chaque instant : brouillard, pluie ou vent ; un éclair frappe de 10d6 en moyenne"),
"stormwind-flight": P2("Vol des vents d'orage", TP2, 1, ["vent", "envol"], why="les vents me portent : je vole comme je marche, et me pose en douceur à la fin", comb="Air"),
"tempest-surge": E2("Déferlante de tempête", 3, ["orage", "maladresse"], 7, "1d12 en moyenne ; gauche de 2, et 1 à chaque instant", impact_sats=[(2, ["maladresse"])]),
"apex-companion": P2("Compagnon suprême", TR, 2, ["bête", "colosse"], 30, "mon compagnon prend la forme suprême de son espèce : énorme, plus mordant, plus rapide", cond=["compagnon"], impact_sats=[(30, ["vie", "temporaire"]), (3, ["vitesse", "mètres"])]),
"fungal-exhalation": E2("Exhalaison fongique", P, ["spore", "nausée"], 15, "6d4 en moyenne ; la nausée"),
"hedge-prison": P2("Prison de haies", V("mouvement", True), 3, ["haie", "cube", "prison"], 20, "un cube de buissons denses l'enferme ; il faut le tailler, 20 points", comb="Plante"),
"mushroom-patch": P2("Parterre de champignons", EXI, P, ["champignon", "spore", "éblouissement"], why="terrain pénible ; à chaque instant, un nuage de spores éblouit", comb="Plante"),
"gravity-weapon": P2("Arme pesante", INT, 1, ["pesanteur", "frappe"], 2, "mon premier coup d'arme de chaque instant frappe de 2 de plus par dé de l'arme"),
"heal-companion": P2("Guérison du compagnon", HE, 2, ["vie"], 6, "1d10 en moyenne", cond=["compagnon"], guerit=True, options=[
    O("Forme de base", loc=(2, "METRES", "au toucher"), impact=(6, ["vie"], "1d10 en moyenne, au toucher, d'un geste")),
    O("Forme maximale", impact=(14, ["vie"], "1d10 + 8 en moyenne, à distance"))]),
"magic-hide": P2("Cuir magique", SEP, 2, ["cuir", "carapace"], 1, "1 ajouté à la défense de mon compagnon", cond=["compagnon"], cible_note=["garde"]),
"animal-feature": P2("Trait animal", TR, 1, ["trait", "bête"], why="un trait de bête, au choix", options=[
    O("Yeux de chat", impact=(P, ["trait", "bête", "pénombre"], "je vois dans la pénombre")), O("Griffes", impact=(4, ["trait", "bête", "griffe"], "des griffes de 1d6 en moyenne")),
    O("Mâchoire", impact=(5, ["trait", "bête", "croc"], "une mâchoire de 1d8 en moyenne"))]),
"enlarge-companion": P2("Compagnon agrandi", TR, 2, ["croissance", "colosse"], why="mon compagnon devient énorme", cond=["compagnon"]),
"hunters-luck": P2("Chance du chasseur", INT, 1, ["savoir", "essai"], why="pour me souvenir d'un ennemi : le meilleur de deux essais", cible_note=["mémoire"], cond=["souvenir"]),
"soothing-mist": P2("Brume apaisante", HE, 2, ["vie", "brume"], 9, "2d8 en moyenne, et un mal qui dure s'arrête ; un mort-vivant en est blessé d'autant", guerit=True),
"ephemeral-tracking": P2("Piste éphémère", VIS, 1, ["trace", "air", "eau"], why="je lis dans l'air et dans l'eau la trace de ce qui est passé depuis une heure"),
"rangers-bramble": P2("Ronce du rôdeur", V("mouvement", True), P, ["plante", "entrave"], 5, "les plantes retiennent mes ennemis ; les plus pris saignent de 2d4 en moyenne à chaque instant", comb="Plante"),
"hunters-vision": P2("Vision du chasseur", VIS, 3, ["proie", "aura"], why="ma proie luit pour moi et les miens : ni l'ombre ni l'invisibilité ne la cachent", cond=["proie"]),
"terrain-transposition": P2("Transposition de terrain", TP2, 1, ["téléportation", "nature"], why="en pleine nature, je me transporte en un lieu dégagé que je vois ; mon compagnon suit"),
"lay-on-hands": P2("Imposition astrale", HE, 2, ["main"], 6, "6 points", options=[
    O("Forme lumineuse", guerit=True, impact=(6, ["main", "vie", "lumineux"], "6 points rendus à un vivant, mieux gardé de 2 un instant ; un mort-vivant en perd 1d6")),
    O("Forme ténébreuse", verb=NE, src_idx="touch-of-corruption", impact=(4, ["main", "flétrissure", "ténébreux"], "1d6 en moyenne à un vivant ; un mort-vivant en regagne 6"))]),
"champions-sacrifice": P2("Sacrifice du champion", SEP, 2, ["sacrifice", "transfert"], why="tout le coup ou le sort qui frappait l'allié tombe sur moi à sa place", cond=["coup"]),
"heros-defiance": P2("Défi du héros", HE, 1, ["vie", "défi"], 45, "10d4 + 20 en moyenne, juste avant le coup qui m'aurait terrassé", cond=["coup"], guerit=True),
"spectral-advance": {**P2("Avancée spectrale", TP2, 1, ["spectre", "charge"], why="sous une forme d'esprit, je fonds sur un ennemi"), "src": "pf2r"},
"litany-of-self-interest": P2("Litanie de l'intérêt propre", ORD, 4, ["égoïsme", "élan"], 2, "2 ajouté à tout ce qu'elle fait pour elle-même ; elle ne peut plus aider personne", **_PSY),
"litany-against-sloth": P2("Litanie contre la paresse", NORD, 3, ["paresse", "lenteur"], 1, "ralentie de 1, incapable de riposter", **_PSY),
"litany-against-wrath": P2("Litanie contre la colère", NORD, 3, ["colère", "châtiment", "lumineux"], 11, "3d6 en moyenne chaque fois qu'elle blesse l'un de ceux que je protège", **_PSY),
"shadows-web": N2("Toile d'ombre", P, ["ténébreux", "étreinte", "faiblesse"], 35, "14d4 en moyenne ; affaiblis, les plus atteints étourdis"),
"wind-jump": P2("Saut du vent", TP2, 1, ["vent", "bond"], why="je vole comme je marche, mais dois finir chaque instant au sol"),
"ki-form": P2("Forme de ki", TR, 1, ["ki", "couronne"], 7, "je luis et je vole ; mes coups frappent de 1d6 de plus, et ma couronne brûle de 2d6 en moyenne qui commence son instant contre moi", vr={"src_idx": "qi-form"}, options=[
    O("Force", impact=(7, ["ki", "couronne", "force"], "couronne de force : 2d6 en moyenne ; coups de 1d6 de plus")),
    O("Forme lumineuse", impact=(7, ["ki", "couronne", "lumineux"], "couronne d'énergie de vie : 2d6 en moyenne ; coups de 1d6 de plus")),
    O("Forme ténébreuse", impact=(7, ["ki", "couronne", "ténébreux"], "couronne d'énergie de mort : 2d6 en moyenne ; coups de 1d6 de plus"))], sens=[("vue", None)], manif=["couronne", "lueur"]),
"abundant-step": P2("Pas abondant", TP2, 1, ["téléportation", "allure"], why="je me téléporte à vue, aussi loin que je cours en un instant", vr={"src_idx": "shrink-the-span"}),
"empty-body": P2("Corps vide", SEP, 1, ["éther", "immatériel"], why="je deviens éthéré une minute, sans effort", vr={"src_idx": "embrace-nothingness"}),
"ki-blast": E2("Déflagration de ki", P, ["ki", "force", "poussée"], 7, "2d6 en moyenne", vr={"src_idx": "qi-blast"}, options=[
    O("Forme de base", impact=(7, ["ki", "force", "poussée"], "2d6 en moyenne dans un cône court ; repousse")),
    O("Forme maximale", aoe={"type": "cone", "size": 60}, impact=(14, ["ki", "force", "poussée"], "4d6 en moyenne dans un cône quatre fois plus long ; tout l'instant y passe"))]),
"ki-rush": P2("Ruée de ki", TP2, 1, ["ki", "ruée", "flou"], why="deux déplacements d'un coup ; je reste flou jusqu'à mon prochain instant", vr={"src_idx": "qi-rush"}),
"ki-strike": P2("Frappe de ki", INT, 1, ["ki", "poing"], 4, "1 ajouté à mon coup à mains nues, qui frappe de 1d6 en moyenne de plus", vr={"src_idx": "inner-upheaval"}),
"quivering-palm": N2("Paume vibrante", 3, ["paume", "mot", "mort"], 80, "après mon coup à mains nues, un mot peut la tuer ; sinon 80, et étourdie", vr={"src_idx": "touch-of-death"}, **_VIV),
"wholeness-of-body": P2("Plénitude du corps", HE, 1, ["vie"], 8, "8 points", guerit=True, vr={"src_idx": "harmonize-self"}, options=[
    O("Guérir", impact=(8, ["vie"], "8 points")), O("Purger", impact=(P, ["poison", "maladie", "délivrance"], "tente de chasser un poison ou une maladie"))]),
"wronged-monks-wrath": E2("Colère du moine outragé", P, ["ki", "force", "foudre"], 20, "2d6 + 2d12 en moyenne", fam="A", options=[
    O("Forme de base", impact=(20, ["ki", "force", "foudre"], "2d6 + 2d12 en moyenne à ceux qui me touchent presque ; assourdit")),
    O("Forme maximale", aoe=_S(20), impact=(40, ["ki", "force", "foudre"], "4d6 + 4d12 en moyenne à 6 m autour ; tout l'instant y passe"))]),
"hasted-assault": P2("Assaut hâté", INT, 1, ["hâte", "frappe"], why="un coup de plus par instant, une minute durant"),
"runic-impression": P2("Empreinte runique", INT, 1, ["rune", "arme"], why="mon arme ou mes poings prennent une vertu : acide, feu, givre, foudre, tonnerre, spectre ou retour", fam="A"),
}
FICHES.update(PF2_FOC2)
FICHES["pied-piping"].update(vp2={})      # le Joueur de flûte focalisé : version PF2 de la page déjà publiée

# ----- Pathfinder 2, lot 17 : sorts focalisés gardés — ensorceleur et oracle -----
PF2_FOCAL_ECARTE.update({"angelic-halo": "ne fait que renforcer un autre sort", "extend-blood-magic": "magie du sang : mécanique de classe", "extend-spell": "ne fait que prolonger le prochain sort",
 "invoke-the-harrow": "jeu de cartes du Harrow (Golarion)", "debilitating-dichotomy": "malédiction de l'oracle", "heroic-feat": "accorde un don de guerrier", "revel-in-retribution": "accorde une réaction de classe",
 "flaming-fusillade": "ne fait que hâter un autre sort", "weapon-trance": "accorde une maîtrise d'armes : mécanique de jeu"})
PF2_FOC3 = {
"tentacular-limbs": P2("Membres tentaculaires", TR, 1, ["tentacule", "allonge", "mètres"], 3, "mes bras deviennent tentacules : je touche et frappe à 3 m"),
"aberrant-whispers": P2("Murmures aberrants", NORD, P, ["murmure", "stupeur"], 2, "des mots d'une langue inconnue : stupéfiés de 2", **_PSY),
"unusual-anatomy": P2("Anatomie insolite", TR, 1, ["chair", "amalgame"], 10, "10 retranché aux coups précis et décisifs ; je vois dans le noir ; qui me frappe de près reçoit 2d6 en moyenne d'acide", fam="A", impact_plus=[(7, ["acide", "riposte"], "2d6 en moyenne d'acide à qui me frappe de près")]),
"angelic-wings": P2("Ailes de lumière", TP2, 1, ["aile", "lumière", "envol"], why="des ailes de lumière : je vole comme je marche, trois instants, et elles éclairent", impact_sats=[(9, ["éclat", "mètres"])], sens=[("vue", None)], manif=["ailes"]),
"celestial-brand": P2("Marque de justice", VIS, 3, ["marque", "justice", "lumineux"], 2, "1 ajouté aux coups contre elle ; ceux que je protège la blessent de 1d4 en moyenne de plus", sens=[("vue", None)], manif=["symbole"]),
"gluttons-jaws": P2("Mâchoire du glouton", TR, 1, ["gueule", "croc"], 5, "une gueule d'ombre de 1d8 en moyenne ; chaque morsure me rend 1d6 de vie d'emprunt", impact_sats=[(4, ["vie", "temporaire"])]),
"swamp-of-sloth": P2("Marais de paresse", EXI, P, ["marais", "fange", "bestiole"], 4, "terrain pénible ; les bêtes de fange y mordent de 1d6 en moyenne"),
"diabolic-edict": P2("Édit imposé", ORD, 2, ["édit", "récompense", "tâche"], 1, "une tâche ordonnée : 1 ajouté à ce qui la sert ; refuser coûte autant", **_PSY, **_VIV),
"embrace-the-pit": P2("Traits du fiélon", TR, 1, ["corne", "fiélon"], 5, "5 retranché au feu, au poison et au ténébreux, 1 aux coups ; la face lumineuse me blesse davantage", fam="A", **_RES),
"hellfire-plume": E2("Panache de feu noir", P, ["panache", "ténébreux"], 28, "4d6 de feu + 4d6 ténébreux en moyenne"),
"flurry-of-claws": {**E2("Volée de griffes", 3, ["griffe", "dragon"], 5, "des griffes de dragon lacèrent deux ennemis voisins : 1d8 en moyenne chacun", qty_cible=2), "src": "pf2r"},
"dragon-breath": E2("Souffle du dragon", P, ["souffle", "dragon"], 18, "5d6 en moyenne, de l'énergie du dragon dont je tiens", fam="A"),
"dragon-wings": P2("Ailes du dragon", TP2, 1, ["aile", "envol", "mètres"], 18, "des ailes de cuir : je vole à 18 m par instant"),
"elemental-toss": E2("Jet élémentaire", 3, ["élément", "bloc"], 5, "1d8 en moyenne, de la matière de mon élément", fam="A"),
"elemental-motion": P2("Élan élémentaire", TP2, 1, ["élément", "allure"], why="mon élément me porte : voler, fouir ou nager, selon lui", fam="A"),
"elemental-blast": E2("Déflagration élémentaire", P, ["élément", "forme"], 28, "8d6 en moyenne, de la matière de mon élément, en éclat, cône ou ligne", fam="A"),
"faerie-dust": P2("Poussière de fée", NORD, P, ["poussière", "crédulité"], 2, "ceux qu'elle touche se laissent mieux tromper : 2 retranché à leur vigilance et à leur volonté", **_PSY),
"fey-disappearance": P2("Disparition féerique", NVIS, 1, ["invisibilité", "sous-bois"], why="invisible un instant, tant que je n'attaque pas ; les broussailles ne me gênent plus"),
"fey-glamour": P2("Charme féerique", EXI, P, ["illusion", "voile"], why="une illusion couvre un lieu, ou déguise ceux qui s'y trouvent, dix minutes"),
"jealous-hex": P2("Maléfice jaloux", NINT, 3, ["jalousie", "atout"], 1, "son plus grand atout lui est retiré de 1 : force, adresse, endurance ou esprit"),
"horrific-visage": P2("Visage horrifiant", PEUR, P, ["visage", "effroi"], 1, "mes traits deviennent ceux d'une guenaude : effrayés de 1", **_PSY),
"youre-mine": P2("Tu es à moi", ORD, 3, ["émotion", "emprise"], why="étourdie, puis à moi un instant : elle fait un geste que je choisis", **_PSY),
"ancestral-memories": P2("Mémoires ancestrales", INT, 1, ["souvenir", "savoir"], why="les souvenirs d'arcanistes morts me prêtent un savoir pour une minute", cible_note=["mémoire"]),
"arcane-countermeasure": P2("Contre-mesure arcanique", NINT, 4, ["affaiblissement"], 2, "le sort qu'on lance perd 1 cran ; 2 ajouté pour s'en défendre", cible_note=["sort"], cond=["sort"]),
"undeaths-blessing": P2("Bénédiction de la non-vie", TR, 2, ["tombe", "inversion"], 2, "les soins et les flétrissures la traitent en morte-vivante ; les flétrissures lui rendent 2 de plus", **_VIV),
"drain-life": N2("Drain de vie", 3, ["drain", "ténébreux"], 8, "3d4 en moyenne, que je gagne en vie d'emprunt", impact_sats=[(8, ["vie", "temporaire"])]),
"grasping-grave": N2("Tombe avide", P, ["bras", "squelette", "entrave"], 21, "6d6 en moyenne ; ralentis de 3 m", impact_sats=[(3, ["lenteur", "mètres"])]),
"blinding-beauty": P2("Beauté aveuglante", NVIS, P, ["beauté", "regard", "aveuglement"], why="un regard d'une beauté terrible : éblouis, voire aveuglés", **_PSY),
"consuming-darkness": N2("Ténèbres dévorantes", P, ["ombre", "ténébreux", "entrave"], 7, "mon ombre s'étend : 2d6 en moyenne, ralentit, et grandit à chaque instant"),
"dim-the-light": P2("Lumière vacillante", NVIS, 1, ["pénombre", "dérobade"], why="la lumière vacille : je me cache aussitôt, même à découvert"),
"establish-ward": P2("Domaine établi", REL, P, ["domaine", "nature", "frappe"], why="je me lie au lieu : en son sein, la nature frappe pour moi ; hors de lui, je m'affaiblis"),
"genies-veil": P2("Voile du génie", NVIS, 2, ["fumée", "dérobade"], why="elle disparaît dans une fumée colorée et reparaît : le coup la trouve mal", cond=["coup"]),
"hearts-desire": P2("Désir du cœur", EXI, 3, ["désir", "fantasme", "stupeur"], 2, "des visions de ce qu'elle désire : stupéfiée de 2, sans riposte", dur=(1, "MINUTES"), **_PSY),
"nymphs-token": P2("Gage de la nymphe", REL, 2, ["gage", "faveur"], 1, "un gage — mèche, fleur — porte chance à l'allié qui le garde : 1 ajouté"),
"sepulchral-mask": P2("Masque sépulcral", PEUR, P, ["masque", "regret"], 2, "1d4 en moyenne à l'esprit de ceux qui m'approchent ; 1 ajouté à ma volonté", **_PSY),
"shepherd-of-souls": P2("Berger des âmes", SEP, 2, ["sacrifice", "sursis"], 15, "je donne jusqu'à 15 de ma vie : le coup qui la frappe est réduit du double", impact_sats=[(30, ["rempart"])], cond=["coup"]),
"spirit-veil": P2("Voile des esprits", NVIS, 1, ["esprit", "voile"], why="estompé pour tous ; invisible aux morts-vivants, quels que soient leurs sens"),
"steal-shadow": N2("Ombre volée", 3, ["ombre", "larcin", "faiblesse"], 8, "3d4 en moyenne à chaque instant ; affaiblie ; je m'en nourris"),
"wish-twisted-form": P2("Forme tordue par le vœu", NINT, 3, ["vœu", "faille"], 5, "ses forces deviennent faiblesses : une énergie la blesse de 5 de plus, ses résistances cèdent", dur=(1, "MINUTES"), **_RES),
"abyssal-wrath": E2("Courroux astral", P, ["courroux"], 28, "4d6 + 4d6 en moyenne, d'une énergie et d'un choc tirés au sort", fam="A", vr={"src_idx": "chthonian-wrath"}, options=[
    O("Forme ténébreuse", impact=(28, ["courroux", "ténébreux"], "4d6 + 4d6 en moyenne : l'énergie de l'Abysse, sous une forme tirée au sort")),
    O("Forme lumineuse", impact=(28, ["courroux", "lumineux"], "4d6 + 4d6 en moyenne : l'énergie de l'Étoile, sous une forme tirée au sort"))]),
"dragon-claws": P2("Griffes du dragon", TR, 1, ["griffe", "dragon"], 6, "des griffes de 1d4 + 1d6 en moyenne ; 5 retranché à l'énergie du dragon dont je tiens", fam="A"),
"cleansing-flames": P2("Flammes purificatrices", V("qualite"), 2, ["flamme", "pureté"], why="des flammes défont un poison ou un mal : maladresse, faiblesse, fatigue, peur, paralysie, nausée, stupeur", fam="A"),
"rejuvenating-flames": P2("Flammes vivifiantes", HE, P, ["flamme", "vie"], 2, "1d4 en moyenne rendus aux alliés, 1 ajouté à leur vigueur ; autant de brûlure aux ennemis", guerit=True, fam="A"),
"shroud-of-flame": P2("Linceul de flammes", SEP, 1, ["flamme", "riposte"], 11, "3 à qui me touche ; 3d6 en moyenne à ceux qui m'entourent, à chaque instant", impact_sats=[(3, ["riposte"])]),
"unraveling-blast": P2("Avenir défait", NORD, 3, ["avenir", "vertige"], 5, "2d4 en moyenne ; un de ses avenirs détruit, elle reste prise au dépourvu", **_PSY),
"rewrite-possibility": P2("Possible réécrit", INT, 2, ["avenir", "essai"], why="une minute durant, je guide son sort : le meilleur de deux essais, une fois par instant"),
"ancestral-touch": P2("Toucher des ancêtres", PEUR, 3, ["ancêtre", "effroi"], 2, "1d4 en moyenne ; elle voit et sent mes ancêtres : effrayée", **_PSY, **_VIV),
"ancestral-defense": P2("Défense des ancêtres", SEP, 1, ["ancêtre", "volonté"], why="contre ce qui veut plier ma volonté : le meilleur de deux essais", cond=["emprise"], **_RES),
"ancestral-form": P2("Forme ancestrale", TR, 1, ["esprit", "invisibilité", "immatériel"], 10, "invisible et à demi immatériel : 10 retranché à tout, le double contre le non magique ; je vole"),
"battlefield-persistence": P2("Ténacité au combat", SEP, 1, ["ténacité"], 2, "2 ajouté à l'épreuve qui allait m'écarter du combat", cond=["coup"], **_RES),
"soul-siphon": N2("Siphon d'âme", 3, ["âme", "drain", "ténébreux"], 2, "1d4 en moyenne, vidée de 1 ; je gagne ce qu'elle perd en vie d'emprunt", **_VIV),
"armor-of-bones": P2("Armure d'os", SEP, 1, ["os", "rempart"], 3, "3 retranché au froid, à la foudre, au feu, aux pointes et aux tranchants", **_RES),
"claim-undead": P2("Mort-vivant revendiqué", ORD, 3, ["maîtrise", "service"], why="le mort-vivant me reconnaît pour maître, même arraché à un autre", cond=["MORTVIVANT"]),
"spray-of-stars": E2("Gerbe d'étoiles", P, ["étoile", "éblouissement"], 2, "1d4 en moyenne de feu ; éblouit"),
"interstellar-void": E2("Vide interstellaire", 3, ["vide", "froid", "fatigue"], 11, "3d6 en moyenne de froid, à chaque instant ; fatiguée"),
"moonlight-bridge": P2("Pont astral", EXI, P, ["pont"], why="un pont de 3 m de large et 36 de long ; mes ennemis ne peuvent y monter", aoe={"type": "line", "size": 120}, sens=[("vue", None)], manif=["pont"], options=[
    O("Forme lumineuse", impact=(P, ["pont", "lumineux"], "un pont de clarté, large de 3 m ; mes ennemis ne peuvent y monter")),
    O("Forme ténébreuse", impact=(P, ["pont", "ténébreux"], "un pont d'ombre, large de 3 m ; mes ennemis ne peuvent y monter"))]),
"incendiary-aura": P2("Aura incendiaire", INT, P, ["feu", "embrasement"], 5, "près de moi, qui est brûlé s'enflamme : 2d4 en moyenne à chaque instant", fam="A"),
"whirling-flames": E2("Flammes tourbillonnantes", P, ["tourbillon"], 18, "5d6 en moyenne"),
"life-link": P2("Lien vital", REL, 2, ["partage", "blessure"], 3, "elle regagne 1d4 ; puis, à chaque instant, 3 points de ses blessures passent sur moi", impact_sats=[(2, ["regain"])]),
"delay-affliction": P2("Affliction retardée", HE, 2, ["vie", "sursis"], 14, "3d8 en moyenne ; un mal qui l'afflige est suspendu", guerit=True),
"life-giving-form": P2("Forme vivifiante", TR, 1, ["lumière", "vie", "lumineux"], 2, "un phare de vie : 5 retranché aux coups précis, mes poings frappent de 1d4 de plus, mon toucher soigne ; le ténébreux me blesse de 5 de plus", impact_sats=[(5, ["rempart"])], sens=[("vue", None)], manif=["lueur"]),
"brain-drain": P2("Drain de cervelle", V("flux"), 3, ["souvenir", "larcin"], 5, "1d8 en moyenne ; je fouille ses souvenirs volés pour savoir ce qu'elle sait", **_PSY),
"access-lore": P2("Accès au savoir", INT, 1, ["savoir", "multivers"], why="je puise un savoir précis dans la connaissance du multivers, pour une minute", cible_note=["mémoire"]),
"dread-secret": P2("Secret redoutable", NINT, 3, ["secret", "faille", "effroi"], 1, "un secret contraire à leur nature : leur résistance cède ou leur faiblesse s'aggrave ; effrayés de 1", qty_cible=6),
"tempest-touch": E2("Toucher de tempête", 3, ["eau", "glace", "lenteur", "mètres"], 3, "1d4 + 1d4 en moyenne ; ralentie de 3 m", fam="A", impact_sats=[(4, ["choc"])]),
"thunderburst": E2("Éclat de tonnerre", P, ["air", "tonnerre", "surdité"], 14, "2d6 + 2d6 en moyenne ; assourdit", fam="A"),
"tempest-form": P2("Forme de tempête", TR, 1, ["corps", "fluide"], why="mon corps devient fluide", fam="A", options=[
    O("Air", impact=(4, ["corps", "fluide", "air", "foudre"], "je vole ; mes coups foudroient de 1d6 en moyenne")),
    O("Eau", impact=(P, ["corps", "fluide", "eau", "nage"], "je nage et passe par les fentes")),
    O("Brume", impact=(P, ["corps", "fluide", "brume", "voile"], "estompé, je flotte"))]),
"call-to-arms": P2("Appel aux armes", INT, P, ["cri", "élan"], 2, "2 ajouté à l'entrée en lice de mes alliés, et un peu de vie d'emprunt"),
"vision-of-weakness": P2("Vision de la faiblesse", VIS, 3, ["faille", "précision"], 2, "je sais ses faiblesses et sa plus faible résistance ; 2 ajouté à mon prochain coup contre elle"),
"temporal-distortion": P2("Distorsion temporelle", NORD, 3, ["temps", "hasard"], 4, "jetée en avant ou en arrière : gauche, faible ou stupéfiée, au hasard, 4 instants", impact_sats=[(4, ["instants"])]),
"time-skip": P2("Saut d'instant", INT, 2, ["temps", "hâte"], why="poussé de quelques instants en avant : un geste de plus à son prochain instant"),
"manifold-lives": P2("Vies multiples", NORD, 3, ["regret", "chemin", "stupeur"], 21, "6d6 en moyenne : mille vies qu'elle n'a pas vécues ; stupéfiée une minute", dur=(1, "MINUTES"), **_PSY),
}
FICHES.update(PF2_FOC3)

# ----- Pathfinder 2, lot 18 : sorts focalisés gardés — clerc (sorts de domaine, en Arcane, sans dieu) -----
PF2_FOCAL_ECARTE.update({"know-the-enemy": "n'est qu'une action de règles", "perfected-form": "même effet que Coup de chance", "perfected-body": "ajuste un degré de réussite",
 "mystic-beacon": "ne fait que renforcer le prochain sort d'un autre", "magics-vessel": "réceptacle de l'énergie d'une divinité", "zeal-for-battle": "relance l'initiative",
 "unity": "prête un modificateur de sauvegarde : mécanique de jeu", "tempt-fate": "ajuste un degré de réussite : mécanique de jeu", "string-of-fate": "échange des degrés de réussite : mécanique de jeu"})
_ESSAI = "le meilleur de deux essais"
PF2_FOC4 = {
"pushing-gust": P2("Rafale repoussante", NF, 3, ["vent", "poussée", "mètres"], 3, "repoussée de 3 m, de 1,5 m si elle tient bon", comb="Air"),
"disperse-into-air": P2("Dispersion dans l'air", SEP, 1, ["air", "immatériel"], why="après le coup, je deviens air jusqu'à la fin de l'instant : rien ne m'atteint, puis je reparais à 4,5 m", cond=["coup"], fam="A"),
"competitive-edge": P2("Esprit de compétition", INT, 1, ["émulation"], 1, "1 ajouté à mes coups et à mes entreprises ; davantage quand un ennemi proche brille"),
"face-in-the-crowd": P2("Visage dans la foule", NVIS, 1, ["foule", "banalité"], 2, "dans une foule, 2 ajouté pour passer inaperçu ; elle ne me gêne pas"),
"veil-of-confidence": P2("Voile d'assurance", SEP, 1, ["assurance", "peur"], 1, "ma peur recule de 1, et chaque peur à venir d'autant ; si je cède tout à fait, elle redouble", **_PSY),
"artistic-flourish": P2("Touche d'artiste", TR, 4, ["art", "ouvrage"], 1, "l'objet refait selon ma vision : 1 ajouté à son usage, dix minutes", cible_obj=["objet"]),
"cloak-of-shadow": P2("Cape d'ombre", NVIS, 2, ["ombre", "pénombre"], why="la vive lumière devient pénombre à 6 m autour d'elle : elle s'y dérobe mieux", impact_sats=[(6, ["rayon", "mètres"])]),
"deaths-call": P2("Appel de la mort", INT, 1, ["mort", "vigueur"], why="voir mourir me ranime : un regain de vie d'emprunt, double si c'était un mort-vivant", cond=["mort"]),
"eradicate-undeath": E2("Non-vie éradiquée", P, ["déluge", "lumineux"], 26, "4d12 en moyenne aux morts-vivants", cond=["MORTVIVANT"]),
"cry-of-destruction": E2("Cri de destruction", P, ["voix", "fracas"], 5, "1d8 en moyenne aux êtres et aux objets ; davantage si j'ai déjà blessé dans l'instant"),
"destructive-aura": P2("Aura destructrice", NINT, P, ["sable", "ruine"], 2, "2 retranché aux résistances de tous ceux qu'elle touche, moi compris", **_RES),
"sweet-dream": P2("Doux rêve", ORD, 2, ["sommeil", "rêve"], 1, "je l'endors et choisis son rêve : au réveil, 1 ajouté selon le rêve", **_PSY),
"dreamers-call": P2("Appel du rêveur", NORD, 3, ["rêverie", "suggestion"], why="noyée de rêveries : prise au dépourvu, fascinée, docile un instant", **_PSY),
"hurtling-stone": E2("Pierre lancée", 3, ["pierre"], 4, "1d6 en moyenne", comb="Roche"),
"localized-quake": E2("Séisme local", P, ["secousse", "chute"], 14, "4d6 en moyenne ; renverse", comb="Terre"),
"soothing-words": P2("Paroles apaisantes", SEP, 2, ["calme", "volonté"], 1, "1 ajouté à sa volonté, 2 contre les émotions ; une émotion qui la tient peut céder", **_PSY, impact_sats=[(2, ["émotion"])]),
"read-fate": P2("Lecture du destin", VIS, 4, ["destin", "présage"], why="un mot sur son sort prochain : bon, mauvais, les deux, ou rien"),
"fire-ray": E2("Rayon de feu", 3, ["rayon"], 7, "2d6 en moyenne"),
"flame-barrier": P2("Barrière aux flammes", SEP, 2, ["feu", "rempart"], 15, "15 retranché au feu qui la frappe", cond=["coup"], fam="A", **_RES),
"unimpeded-stride": P2("Foulée sans entrave", TP2, 1, ["liberté", "foulée"], why="je m'arrache à ce qui me retient par magie, puis je cours sans que le terrain me gêne"),
"word-of-freedom": P2("Mot de liberté", DISP, 2, ["mot", "délivrance"], why="un instant, un mal ne la tient plus : confusion, peur, prise, entrave ou paralysie"),
"healers-blessing": P2("Bénédiction du guérisseur", INT, 2, ["soin", "surcroît"], 2, "les sorts de soin lui rendent 2 de plus", **_VIV),
"rebuke-death": P2("Mort réprimandée", HE, P, ["vie", "agonie"], 11, "3d6 en moyenne à trois vivants au plus ; les mourants se relèvent sans séquelle", qty=3, guerit=True),
"overstuff": P2("Gavage", NQ, 3, ["repas", "nausée"], 1, "gavée d'un repas entier : nausée de 1", **_VIV),
"take-its-course": P2("Suivre son cours", INT, 4, ["mal", "hâte"], why="hâte ou aggrave un mal en cours : maladie, poison, plaie qui dure"),
"scholarly-recollection": P2("Souvenir d'érudit", INT, 1, ["savoir", "essai"], why="pour chercher ou me souvenir : " + _ESSAI, cond=["souvenir"]),
"brin-de-chance-pf2": P2("Brin de chance", INT, 2, ["chance", "essai"], why="une fois, pour résister : " + _ESSAI, src_idx="bit-of-luck"),      # la clé « bit-of-luck » est celle d'un sort de Pathfinder 1 écarté
"lucky-break": P2("Coup de chance", INT, 1, ["chance", "essai"], why="l'épreuve manquée se rejoue : " + _ESSAI, cond=["échec"]),
"athletic-rush": P2("Élan athlétique", INT, 1, ["corps", "vitesse", "mètres"], 3, "3 m de plus par instant et 2 ajouté aux tours de force ; un déplacement aussitôt"),
"enduring-might": P2("Force endurante", SEP, 1, ["force", "rempart"], 8, "8 retranché au coup qui me frappe, et davantage selon ma force", cond=["coup"], **_RES),
"touch-of-the-moon": P2("Toucher astral", INT, 4, ["marque"], why="une marque luit sur son front ; elle lui donne un bienfait qui change d'instant en instant", sens=[("vue", None)], manif=["marque", "lueur"], options=[
    O("Forme lumineuse", impact=(P, ["marque", "phase", "lumineux"], "une marque de clarté, au bienfait changeant")),
    O("Forme ténébreuse", impact=(P, ["marque", "phase", "ténébreux"], "une marque d'ombre, au bienfait changeant"))]),
"vibrant-thorns": P2("Épines vivaces", TR, 1, ["épine", "riposte"], 1, "qui me frappe de près se pique de 1 ; davantage après un sort de soin"),
"natures-bounty": P2("Largesse de la nature", HE, 1, ["vie", "fruit"], 29, "un fruit : qui le mange regagne 3d10 + 12 en moyenne et se trouve rassasié", guerit=True),
"waking-nightmare": P2("Cauchemar éveillé", PEUR, 3, ["cauchemar", "effroi"], 2, "effrayée de 2 ; endormie, elle se réveille en sursaut", **_PSY),
"shared-nightmare": P2("Cauchemar partagé", NORD, 3, ["cauchemar", "confusion", "échange"], why="nos cauchemars s'échangent : l'un de nous deux en sort confus — elle, si elle cède", **_PSY),
"savor-the-sting": P2("Savourer la douleur", NORD, 3, ["douleur", "délectation"], 2, "1d4 en moyenne, puis autant à chaque instant ; tant qu'elle souffre, 1 ajouté à mes coups contre elle", **_PSY),
"retributive-pain": P2("Douleur rendue", NORD, 3, ["douleur", "renvoi", "fractionné"], 2, "la moitié de ce qu'elle vient de m'infliger lui revient à l'esprit", cond=["coup"], **_PSY),
"charming-touch": P2("Toucher charmeur", REL, 4, ["attirance", "amitié"], why="elle me devient amicale, voire serviable, dix minutes", **_PSY),
"captivating-adoration": P2("Adoration captivante", ATT, P, ["charme", "fascination"], why="ceux qui m'approchent sont fascinés par moi, sauf ceux que j'en dispense", **_PSY),
"perfected-mind": P2("Esprit parfait", SEP, 1, ["méditation", "volonté"], why="je résiste à nouveau à ce qui tient mon esprit", **_PSY),
"protectors-sacrifice": P2("Sacrifice du protecteur", SEP, 2, ["sacrifice", "transfert"], 3, "3 points du coup qui frappe l'allié passent sur moi", cond=["coup"]),
"protectors-sphere": P2("Sphère du protecteur", SEP, P, ["aura", "rempart"], 3, "3 retranché à tout ce qui me blesse, et à mes alliés proches", **_RES),
"safeguard-secret": P2("Secret gardé", SEP, 2, ["secret", "silence"], 4, "un secret partagé : 4 ajouté pour le taire et le défendre contre qui veut le lire", **_PSY),
"dazzling-flash": P2("Éclair éblouissant", NVIS, P, ["éclair", "éblouissement"], why="un éclair de lumière : éblouis, voire aveuglés un instant"),
"agile-feet": P2("Pieds agiles", INT, 1, ["foulée", "vitesse", "mètres"], 2, "1,5 m de plus par instant, arrondi à 2 ; aucun terrain ne me gêne ; un déplacement aussitôt"),
"travelers-transit": P2("Passage du voyageur", TP2, 1, ["escalade", "nage"], why="je grimpe ou je nage aussi vite que je marche"),
"sudden-shift": P2("Esquive soudaine", NVIS, 1, ["pas", "voile"], why="un pas de côté, et je suis estompé un instant", cond=["coup"]),
"tricksters-twin": P2("Jumeau du farceur", EXI, 3, ["double", "fantasme"], why="elle seule voit un double de moi qui mime mes gestes : elle ne sait plus où je suis", **_PSY),
"word-of-truth": P2("Parole de vérité", VIS, 1, ["vérité", "signe"], why="un signe luit au-dessus de moi tant que je dis ce que je crois vrai : on sait que je ne mens pas", sens=[("vue", None)], manif=["signe"]),
"glimpse-the-truth": P2("Vérité entrevue", VIS, P, ["vérité", "illusion"], why="je vois à travers les illusions alentour", impact_sats=[(9, ["rayon", "mètres"])]),
"touch-of-obedience": P2("Toucher d'obéissance", NORD, 3, ["volonté", "stupeur"], 1, "sa volonté s'érode : stupéfiée de 1", **_PSY, **_VIV),
"commanding-lash": P2("Fouet du commandement", ORD, 3, ["douleur", "ordre"], why="à celle que je viens de blesser, un ordre d'un mot, qu'elle exécute", cond=["blessure"], **_PSY),
"touch-of-undeath": N2("Toucher de non-vie", 3, ["tombe", "ténébreux"], 4, "1d6 en moyenne ; les soins prennent moitié moins sur elle un instant", **_VIV),
"malignant-sustenance": P2("Subsistance maligne", HE, 2, ["regain", "ténébreux"], 7, "7 points rendus à chaque instant à un mort-vivant", cond=["MORTVIVANT"], guerit=True),
"downpour": P2("Averse", EXI, P, ["pluie", "voile"], 10, "une pluie battante : éteint les feux, cache, 10 retranché au feu", comb="Eau"),
"appearance-of-wealth": P2("Apparence de richesse", EXI, P, ["trésor", "fantasme", "fascination"], why="une vision de richesses immenses fascine ceux que l'or tente", **_PSY),
"precious-metals": P2("Métaux précieux", TR, 4, ["acier", "argent", "or"], why="le métal vil devient fer froid, cuivre, or, fer, argent ou acier, pour une minute", cible_obj=["objet"], fam="A"),
"weapon-surge": P2("Arme exaltée", INT, 4, ["arme", "surcroît"], 1, "son prochain coup : 1 ajouté, et un dé de plus", cible_obj=["arme"]),
"practice-makes-perfect": P2("C'est en forgeant", INT, 2, ["métier", "appui"], 2, "2 ajouté à l'essai en cours, 3 pour un maître", cond=["essai"]),
"blind-ambition": P2("Ambition aveugle", NORD, 3, ["ambition", "rancœur"], 2, "2 retranché pour résister à qui la tente de trahir ; elle en veut aux siens", vr={"src_idx": "ignite-ambition"}, **_PSY),
"darkened-eyes": P2("Yeux enténébrés", NVIS, 3, ["regard", "nuit"], why="sa vision dans le noir ou la pénombre s'éteint une minute ; au pire, elle est aveuglée", dur=(1, "MINUTES"), vr={"src_idx": "darkened-sight"}),
"positive-luminance": P2("Luminance vitale", HE, 1, ["lumière", "vie", "réserve"], 4, "je luis et j'amasse la vie, 4 puis davantage ; je la rends en soin, ou elle brûle les morts-vivants proches", guerit=True, vr={"src_idx": "vital-luminance"},
    sens=[("vue", None)], manif=["lueur"]),
"pulse-of-the-city": P2("Pouls de la cité", VIS, 1, ["cité", "rumeur"], why="le nom de la cité la plus proche, et un événement marquant qui s'y passe", vr={"src_idx": "pulse-of-civilization"}),
"splash-of-art": P2("Éclaboussure d'art", EXI, P, ["couleur", "hasard"], why="une pluie de couleurs illusoires : selon la couleur tirée, affaiblit, éblouit, stupéfie ou gêne", vr={"src_idx": "creative-splash"}, **_PSY),
"cinder-gaze": P2("Regard des braises", VIS, 1, ["flamme", "présage"], why="je lis dans les flammes et la fumée ce qui vient : mieux préparé au prochain danger", comp=["feu"]),
"euphoric-renewal": P2("Renouveau euphorique", INT, 1, ["agonie", "exaltation"], why="chaque fois que je reviens de l'agonie : hâté, raffermi, exalté"),
"frenzied-revelry": P2("Réjouissances frénétiques", INT, P, ["danse", "frénésie"], 1, "1 ajouté contre ce qui vise l'esprit, pour moi et mes alliés proches ; nos coups frappent plus fort, mais nous nous gardons moins"),
"hollow-heart": P2("Cœur vide", NREL, 3, ["ambition", "solitude"], 3, "elle ne tient plus personne pour allié, 3 instants", impact_sats=[(3, ["instants"])], **_PSY),
"isolation": P2("Isolement", NREL, 3, ["solitude", "voile"], why="la solitude la voile : ses alliés ne la voient ni ne l'entendent plus"),
"inevitable-destination": P2("Destination inévitable", V("mouvement", True), 3, ["chemin", "retour"], why="tous ses chemins mènent à moi : elle ne peut s'éloigner davantage"),
"purifying-veil": P2("Voile purificateur", SEP, 2, ["eau", "voile", "lumineux"], 14, "un voile de gouttelettes la cache ; 4d6 en moyenne aux morts-vivants et aux fiélons qui le traversent", fam="A"),
"shaken-confidence": P2("Assurance ébranlée", NORD, 3, ["moquerie", "doute"], why="moquée, elle doute : le pire de deux essais à sa prochaine entreprise", **_PSY),
"victory-cry": P2("Cri de victoire", INT, 2, ["cri", "gloire"], 4, "le coup décisif de l'allié résonne : 1d6 en moyenne de son en plus, et un geste aussitôt", cond=["coup"], fam="A"),
"weaponize-secret": P2("Secret armé", NORD, 3, ["secret", "rune"], 25, "la rune de son secret paraît : 7d6 en moyenne si elle agit contre moi", qty_cible=3, **_PSY),
"wind-whispers": P2("Murmures du vent", EXI, P, ["rumeur", "vent"], why="une rumeur, vraie ou fausse, portée par les brises aux oreilles de toute une contrée"),
"wordsmith": P2("Orfèvre des mots", TR, 4, ["texte", "langue", "clarté"], why="un écrit passe dans une autre langue, ou devient plus clair pour ses lecteurs", cible_obj=["écrit"]),
}
FICHES.update(PF2_FOC4)
for _k in ("delusional-pride", "moonbeam", "tidal-surge", "forced-quiet"): FICHES[_k].update(vp2={})      # focalisés du clerc dont la page existait déjà

# ----- Pathfinder 2, lot 19 : sorts focalisés gardés — sans classe marquée (archétypes, lignages, écoles de moines, élémentalistes) -----
PF2_FOCAL_ECARTE.update({"call-the-ten": "héros d'une école de Golarion", "magic-warrior-aspect": "masque d'un archétype de Golarion", "magic-warrior-transformation": "masque d'un archétype de Golarion",
 "invoke-the-crimson-oath": "serment d'un ordre de Golarion", "shall-not-falter-shall-not-rout": "serment d'un ordre de Golarion", "achaekeks-clutch": "symbole d'une divinité nommée",
 "mantis-form": "même effet que la Forme d'insecte", "electrified-crystal-ward": "crée un « danger » de règles sur une serrure", "share-burden": "ajuste un degré de réussite : mécanique de jeu"})
PF2_FOC5 = {
"unsettling-knowledge": P2("Savoir troublant", ATT, 3, ["savoir", "fascination"], why="un savoir caché, troublant et captivant : fascinée une minute", dur=(1, "MINUTES"), **_PSY),
"halcyon-mists": P2("Brumes sereines", HE, 2, ["brume", "vigueur"], 5, "1d8 en moyenne de vie d'emprunt ; un mal qui dure s'arrête", **_VIV),
"menacing-lament": P2("Complainte menaçante", NORD, P, ["complainte", "ouverture"], why="mes ennemis proches sont pris au dépourvu par mes coups et ne peuvent me prendre en tenaille", **_CHANT),
"valiant-anthem": P2("Hymne vaillant", INT, P, ["hymne", "vitesse", "mètres"], 3, "3 m de plus par instant et 1 ajouté aux coups de mes alliés", **_CHANT, impact_sats=[(1, ["précision"])]),
"elemental-sheath": P2("Gaine élémentaire", SEP, 1, ["armure", "élément"], 1, "une armure de l'élément choisi : 1 ajouté à ma défense, et l'élément me blesse moins", fam="A", cible_note=["garde"],
    options=[O(n, impact=(1, ["armure", w], "une armure de cet élément : 1 ajouté à ma défense")) for n, w in _ELEM6]),
"vicious-howl": P2("Hurlement farouche", INT, 1, ["hurlement", "ardeur"], 4, "4 ajouté à mes coups, et un regain de vie d'emprunt"),
"tireless-worker": P2("Travailleur infatigable", DISP, 2, ["fatigue", "suspension"], why="suspend un mal : maladresse, charge, faiblesse ou fatigue"),
"serrate": P2("Dentelure", INT, 4, ["acier", "dent"], 2, "le métal de l'arme se hérisse : 1d4 en moyenne de plus à chaque coup, un instant", cible_obj=["arme"], fam="A"),
"repel-metal": P2("Métal repoussé", SEP, 2, ["acier", "renvoi"], 2, "2 ajouté à sa défense contre le coup ; s'il manque, il retourne à l'envoyeur", cond=["coup"], cible_note=["garde"], fam="A"),
"arms-of-nature": P2("Armes de la nature", EXI, 4, ["bois", "arme"], 1, "je tire d'un tronc ou d'une poutre une arme de même bois, meilleure de 1", cible_obj=["objet"], fam="A"),
"wood-walk": P2("Marche du bois", TP2, 1, ["bois", "passage"], why="le bois se plie à mon pas : marches, échelles de lianes, branches qui me hissent", fam="A"),
"speaking-sky": P2("Ciel parlant", VIS, 1, ["air", "mouvement", "mètres"], 18, "l'air me dit tout ce qui bouge à 18 m", fam="A"),
"steal-the-sky": P2("Ciel dérobé", V("mouvement", True), 3, ["air", "chute", "mètres"], 18, "l'air ne la porte plus : elle descend de 18 m, et ne revole pas d'un instant", cond=["coup"]),
"ordained-purpose": P2("Dessein ordonné", NORD, P, ["remords", "rang"], 14, "4d6 en moyenne ; accablés d'avoir quitté leur place, ils se jettent à terre", **_PSY),
"split-the-tongue": P2("Langue fendue", NE, 3, ["langue", "mensonge", "stupeur"], 5, "1d8 en moyenne à qui vient de me mentir ; stupéfié", cond=["mensonge"]),
"beastmaster-trance": P2("Transe du maître des bêtes", VIS, 2, ["sens", "partage"], why="je perçois par les sens de mon compagnon, de très loin", cond=["compagnon"]),
"dance-of-darkness": P2("Danse des ténèbres", NVIS, P, ["danse", "obscurité"], why="je danse et laisse une nappe d'obscurité magique où je passe", aoe=_S(10)),
"shadow-illusion": P2("Illusion d'ombre", EXI, P, ["ombre", "fantasme"], why="l'image d'un être ou d'une chose, qui ne tient que dans la pénombre ou le noir"),
"shadow-jump": P2("Saut d'ombre", TP2, 1, ["ombre", "téléportation"], why="d'une ombre à une autre, à vue"),
"fearful-feast": P2("Festin de peur", V("flux"), 3, ["effroi", "dévoration"], 15, "j'aspire le courage d'un être effrayé : 6d4 en moyenne, sa peur croît de 2, et je m'en repais", cond=["effroi"], **_PSY),
"lift-natures-caul": P2("Voile de la nature levé", PEUR, P, ["vérité", "horreur", "stupeur"], why="ils voient le monde sans son voile, tordu et hideux : stupéfiés une minute, effrayés", **_PSY),
"hallowed-ground": P2("Sol béni", EXI, P, ["vie", "lumineux"], 6, "1d6 + 1d4 en moyenne aux morts-vivants, puis à ceux qui y restent", cond=["MORTVIVANT"]),
"eyes-of-the-dead": P2("Yeux des morts", VIS, 4, ["sens", "partage"], why="je perçois par les sens d'un mort-vivant qui me sert, de très loin", cond=["MORTVIVANT"]),
"shambling-horror": P2("Horreur titubante", V("existence"), 4, ["cadavre", "service"], why="un mort du jour se relève en squelette ou en zombi, à mon service dix minutes", cible_obj=["cadavre"]),
"subjugate-undead": P2("Mort-vivant subjugué", ORD, 3, ["maîtrise", "service"], why="le mort-vivant me sert une minute", cond=["MORTVIVANT"], dur=(1, "MINUTES")),
"path-of-least-resistance": P2("Voie de moindre résistance", TP2, 1, ["temps", "chemin", "choix"], why="j'essaie plusieurs routes et garde la plus sûre : deux déplacements que rien n'entrave"),
"waking-dream": P2("Rêve éveillé", NORD, 3, ["rêve", "confusion"], why="elle ne distingue plus le vrai péril de l'imaginaire : confuse", **_PSY),
"light-of-revelation": P2("Lumière de révélation", VIS, P, ["lumière", "caché"], 1, "une clarté à 9 m : 1 ajouté pour y trouver ce qui se cache", impact_sats=[(9, ["rayon", "mètres"])], sens=[("vue", None)], manif=["aura"]),
"perfect-strike": P2("Frappe parfaite", INT, 1, ["frappe", "essai"], why="le coup manqué se rejoue", cond=["échec"]),
"sun-blade": E2("Lame astrale ardente", 3, ["rayon", "lame"], 2, "1d4 en moyenne de feu, tiré de l'épée ou de la lance", fam="A", options=[
    O("Forme lumineuse", impact=(2, ["rayon", "lame", "lumineux"], "1d4 en moyenne ; bien davantage aux morts-vivants et aux êtres de l'ombre")),
    O("Forme ténébreuse", impact=(2, ["rayon", "lame", "ténébreux"], "1d4 en moyenne ; bien davantage aux êtres de lumière"))]),
"adapt-self": P2("Adaptation de soi", TR, 1, ["milieu", "adaptation"], why="un trait adapté au lieu : nager, respirer sous l'eau, grimper, voir dans le noir"),
"adaptive-ablation": P2("Ablation adaptative", SEP, 1, ["énergie", "accoutumance"], 5, "5 retranché à l'énergie qui vient de me blesser", cond=["coup"], **_RES),
"asterism": E2("Astérisme", P, ["étoile", "ligne", "constellation"], 14, "cinq lignes de feu d'étoile entre moi et ce que je relie : 4d6 en moyenne à qui les traverse", qty=5),
"bottle-the-storm": P2("Orage en bouteille", V("flux"), 1, ["foudre", "réserve"], 10, "10 retranché à la foudre qui me frappe ; je la garde et la rends dans mon prochain coup", cond=["coup"], fam="A"),
"charged-javelin": E2("Javelot chargé", 3, ["javelot", "champ"], 4, "1d6 en moyenne, puis 1 à chaque instant ; le champ gêne la cible"),
"delay-consequence": P2("Conséquence différée", ORD, 2, ["temps", "sursis"], why="la blessure qui la frappe ne prend effet qu'à la fin de l'instant suivant", cond=["coup"]),
"diamond-dust": E2("Poussière de diamant", P, ["cristal", "glace"], 7, "2d6 en moyenne à qui entre ou reste près de moi ; le sol gèle"),
"divine-plagues": N2("Plaies", 3, ["maladie", "plaie"], 1, "une maladie au choix : maladresse, faiblesse ou stupeur de 1, qui empire"),
"door-to-beyond": P2("Porte vers l'au-delà", ATT, P, ["fissure", "aspiration", "mètres"], 3, "des fissures hors du réel aspirent ce qui est proche de 3 m ; qui les touche est lacéré de 4d6 en moyenne", impact_plus=[(14, ["lacération"], "4d6 en moyenne à qui touche les fissures")]),
"draconic-barrage": E2("Barrage draconique", 3, ["dragon", "énergie", "hasard"], why="un petit dragon d'énergie volette autour de moi, d'une espèce tirée au sort, et se jette sur un ennemi", fam="A"),
"dust-storm": E2("Tempête de poussière", P, ["poussière", "étouffement"], 4, "cache, étouffe, et écorche de 1d6 en moyenne", comb="Poussière"),
"dutiful-challenge": P2("Défi loyal", REL, 3, ["défi", "duel"], 1, "1 retranché à ce qu'elle fait contre d'autres que moi, et à ce que je fais contre d'autres qu'elle", **_PSY),
"ectoplasmic-interstice": P2("Interstice ectoplasmique", TR, P, ["éther", "matière"], why="dans la zone, ce qui est sans corps en prend presque un : on le frappe, et il ne traverse plus"),
"eject-soul": P2("Âme éjectée", NREL, 3, ["âme", "corps", "étourdissement"], 1, "le lien de l'âme au corps vacille : étourdie de 1 ; au pire, l'âme sort un instant", **_VIV),
"empty-inside": P2("Vide intérieur", DISP, 1, ["vide", "émotion"], why="un éclat de vide dans mon esprit : une émotion qui me tient peut s'éteindre", **_PSY),
"ephemeral-hazards": P2("Dangers éphémères", EXI, P, ["piège", "fantasme"], 14, "quatre pièges illusoires : 4d6 en moyenne à l'esprit de qui les touche", qty=4, **_PSY),
"fallow-field": P2("Champ en friche", NINT, P, ["soin", "fractionné"], 2, "une lumière jaune : les soins n'y prennent qu'à moitié"),
"font-of-serenity": P2("Fontaine de sérénité", SEP, P, ["sérénité", "émotion"], 1, "1 ajouté contre les émotions ; qui touche la fontaine peut s'en défaire", **_PSY),
"foul-miasma": P2("Miasme infect", NQ, 3, ["maladie", "contagion"], why="sa maladie sort d'elle en brume et gagne ceux qui l'approchent", cond=["maladie"]),
"ghostly-transcription": P2("Transcription fantôme", VIS, 4, ["parole", "lettre"], why="ses paroles s'écrivent en lettres de lumière devant elle, dans les langues que je parle", sens=[("vue", None)], manif=["lettres"]),
"hyperfocus": P2("Hyperconcentration", INT, 4, ["sens", "netteté"], 1, "1 ajouté à ses sens précis ; ses sens diffus portent moitié moins"),
"lament": P2("Lamentation", NF, 3, ["plainte", "chagrin"], 5, "1d8 en moyenne ; davantage si une émotion me tient", **_PSY),
"oathkeepers-insignia": P2("Insigne du serment tenu", VIS, 1, ["serment", "gage"], why="un gage qui change d'aspect quand j'ai tenu ma promesse : on sait que je l'ai tenue"),
"object-memory": P2("Mémoire de l'objet", INT, 1, ["objet", "savoir-faire"], why="je tire d'une arme ou d'un outil l'expérience de ceux qui s'en sont servis", cible_note=["mémoire"]),
"overflowing-sorrow": P2("Chagrin débordant", NORD, P, ["chagrin", "émotion"], why="ma tristesse noie toute autre émotion chez ceux qui m'approchent, bonne ou mauvaise", **_PSY),
"parch": P2("Dessèchement", NQ, 3, ["vent", "soif"], 1, "desséchée : 1 retranché à tout, une minute ; pire pour les êtres d'eau", dur=(1, "MINUTES")),
"redact": P2("Caviardage", NVIS, 4, ["nom", "rature"], why="un nom s'efface de tous les écrits visés, un jour durant", cible_obj=["écrit"]),
"remember-the-lost": P2("Souvenir des oubliés", NF, P, ["mort", "grief"], 21, "6d6 en moyenne : les morts qui leur en veulent assaillent leur esprit", **_PSY),
"roar-of-the-wyrm": P2("Rugissement du dragon", PEUR, P, ["rugissement", "effroi"], 2, "effrayés de 2 ; les dragons, eux, m'en respectent davantage", **_PSY),
"stasis": P2("Stase", ORD, 4, ["temps", "arrêt"], why="le temps se fige pour elle un instant : rien ne l'atteint, elle ne fait rien"),
"swarm-form": P2("Forme de nuée", TR, 1, ["nuée", "corps"], 5, "je deviens une nuée de bestioles : 5 retranché aux pointes et aux tranchants, 5 ajouté à ce qui frappe en zone"),
"swarmsense": P2("Sens de la nuée", VIS, 1, ["nuée", "capteur"], why="une nuée rampante entend pour moi, et je la déplace"),
"winter-bolt": E2("Trait d'hiver", 3, ["glace", "éclat"], 5, "1d8 en moyenne ; le glaçon éclate ensuite en froid"),
"withering-grasp": N2("Poigne flétrissante", 4, ["pourriture", "ténébreux"], 7, "1d12 en moyenne, puis 1d4 à chaque instant ; ronge aussi les objets", impact_sats=[(2, ["persistance"])]),
"zenith-star": P2("Étoile au zénith", VIS, 3, ["étoile", "repère"], why="une petite étoile l'éblouit puis monte au ciel et marque où elle se trouve, un jour durant"),
"unblinking-flame-aura": P2("Flamme sans cillement : aura", HE, 1, ["flamme", "regard"], 15, "15 points rendus ; 2 ajouté à ma vigilance", guerit=True, fam="A"),
"unblinking-flame-emblem": P2("Flamme sans cillement : emblème", VIS, 3, ["flamme", "sceau"], 1, "un sceau de feu la marque : 1 ajouté aux coups contre elle, 1d6 de feu en plus", cond=["coup"], fam="A"),
"unblinking-flame-ignition": P2("Flamme sans cillement : embrasement", TR, 1, ["flamme", "aura"], 7, "acculé, je m'embrase : je vois tout, et mes coups brûlent de 1d12 en moyenne", fam="A"),
"unblinking-flame-revelation": P2("Flamme sans cillement : révélation", VIS, 3, ["flamme", "illusion"], why="une flamme révèle celle que je viens de frapper : ses illusions sont suspendues", cond=["coup"], fam="A"),
"unbreaking-wave-advance": P2("Vague sans brisure : avancée", NF, P, ["vague", "poussée", "mètres"], 3, "repoussés de 3 m", fam="A"),
"unbreaking-wave-barrier": P2("Vague sans brisure : barrière", SEP, P, ["vague", "cercle"], 1, "1 ajouté à ma défense ; qui approche est repoussé de 3 m, les plus atteints meurtris de 2d6", fam="A", impact_sats=[(3, ["poussée", "mètres"])]),
"unbreaking-wave-containment": P2("Vague sans brisure : entrave", V("mouvement", True), 3, ["eau", "lien"], 35, "quatre liens d'eau : clouées sur place ; 10d6 en moyenne quand je les broie", qty_cible=4, fam="A"),
"unbreaking-wave-vapor": P2("Vague sans brisure : vapeur", NVIS, 1, ["vapeur", "esquive"], 2, "estompé contre le coup, 2 ajouté à ma défense ; puis un pas ou deux", cond=["coup"], fam="A"),
"unfolding-wind-rush": P2("Vent déployé : ruée", TP2, 1, ["vent", "ruée"], why="deux déplacements d'un coup, jusque dans les airs", fam="A"),
"unfolding-wind-buffet": P2("Vent déployé : rafale", NF, 3, ["vent", "poing"], why="trois coups à mains nues sur la même cible ; si l'un porte, elle est repoussée", fam="A"),
"unfolding-wind-blitz": P2("Vent déployé : éclair", TP2, 1, ["vent", "envol", "frappe"], why="je vole deux fois plus loin que je cours, sans qu'on puisse riposter, en frappant au passage", fam="A"),
"unfolding-wind-crash": E2("Vent déployé : fracas", P, ["bond", "impact"], 63, "je bondis à 36 m et retombe : 18d6 en moyenne à 6 m autour", impact_sats=[(36, ["bond", "mètres"])], aoe=_S(20)),
"untwisting-iron-buffer": P2("Fer sans torsion : rempart", SEP, 1, ["ki", "rempart"], 15, "15 points de vie d'emprunt, trois instants", cible_note=["garde"]),
"untwisting-iron-roots": E2("Fer sans torsion : racines", P, ["terre", "secousse"], 7, "2d6 en moyenne ; ils chancellent, et le sol reste encombré", fam="A"),
"untwisting-iron-augmentation": P2("Fer sans torsion : renfort", INT, 1, ["poing", "acier", "argent"], 1, "mes poings valent le fer froid et l'argent : 1 de plus par dé", fam="A"),
"untwisting-iron-pillar": P2("Fer sans torsion : pilier", SEP, 1, ["terre", "pilier"], 50, "50 points de vie d'emprunt ; 5 retranché aux coups", fam="A", impact_sats=[(5, ["rempart"])]),
"for-love-for-lightning": E2("Foudre plantée", P, ["arme", "foudre"], 20, "l'arme plantée en terre crépite : 3d12 en moyenne à chaque instant où je soutiens le sort"),
"suns-fury": P2("Fureur astrale ardente", INT, 4, ["flamme", "arme"], 3, "l'arme s'enveloppe d'une flamme : 1d4 de feu et 1 en plus à chaque coup", cible_obj=["arme"], fam="A", options=[
    O("Forme lumineuse", impact=(3, ["flamme", "arme", "lumineux"], "une flamme claire, qui éclaire : 1d4 de feu et 1 de lumière en plus")),
    O("Forme ténébreuse", impact=(3, ["flamme", "arme", "ténébreux"], "une flamme noire : 1d4 de feu et 1 d'ombre en plus"))]),
"familiar-form": P2("Forme de familier", TR, 1, ["bête", "petit"], why="je deviens une petite bête de compagnie : chat, chauve-souris, corbeau, rat…"),
"spellmasters-ward": P2("Garde du maître des sorts", SEP, 1, ["rune", "sort"], 3, "jusqu'à 3 runes tournent autour de moi : chacune peut briser un sort qui me vise", cible_note=["résistance"], sens=[("vue", None)], manif=["runes"]),
"transcribe-moment": P2("Instant transcrit", VIS, P, ["écrit", "lieu", "exactitude"], why="un petit rouleau paraît, qui décrit avec une précision parfaite tout ce qui m'entoure"),
"combustion": E2("Combustion", 3, ["flamme", "persistance"], 18, "4d8 en moyenne", impact_plus=[(7, ["persistance"], "2d6 en moyenne à chaque instant")]),
"crushing-ground": E2("Sol broyeur", 3, ["terre", "mâchoire"], 7, "2d6 en moyenne ; le sol s'ouvre et se referme sur elle, et la ralentit", comb="Terre"),
"darklight": P2("Lumière noire", NVIS, P, ["ombre", "obscurité"], 7, "aucune lumière n'y luit ; les ombres frappent de 2d6 en moyenne"),
"inscrutable-mask": P2("Masque impénétrable", NVIS, 1, ["ombre", "masque"], 1, "un masque d'ombre : 1 ajouté pour mentir, feinter, intimider et me cacher dans la pénombre"),
"powerful-inhalation": E2("Inspiration puissante", P, ["air", "aspiration"], 18, "5d6 en moyenne : j'aspire tout l'air alentour ; ils en perdent la voix", comb="Air"),
"pulverizing-cascade": E2("Cascade pulvérisante", P, ["vague", "étau"], 18, "5d6 en moyenne entre deux vagues", comb="Eau"),
"rising-surf": P2("Vague montante", TP2, 1, ["vague", "glisse", "mètres"], 10, "une vague me porte sur 10,5 m, arrondi à 10, par-dessus les obstacles", comb="Eau"),
"stone-lance": E2("Lance de pierre", 3, ["lance", "empalement", "mètres"], 21, "6d6 en moyenne ; empalée, elle perd 3 m par instant", comb="Roche", impact_sats=[(3, ["lenteur", "mètres"])]),
"updraft": E2("Courant ascendant", 3, ["vent", "projection", "chute"], 7, "2d6 en moyenne : projetée en l'air, elle retombe à terre", comb="Air"),
"wildfire": P2("Feu de brousse", EXI, P, ["cendre", "flamme"], 1, "une nappe de cendre et de flammes : 1 de feu à chaque pas"),
"ki-cutting-sight": P2("Regard qui tranche le ki", VIS, 3, ["ki", "faille"], why="je vois où frapper pour arrêter le flux qui l'anime : mon prochain coup la trouve sans défense"),
}
for _k in "unsettling-knowledge halcyon-mists menacing-lament valiant-anthem elemental-sheath vicious-howl serrate repel-metal arms-of-nature wood-walk".split(): PF2_FOC5[_k]["src"] = "pf2r"
FICHES.update(PF2_FOC5)

# ----- Pathfinder 2 : focalisés rattachés à une page déjà publiée -----
if "goodberry" in FICHES: FICHES["goodberry"].update(vp2={}, vr={"src_idx": "cornucopia"})      # Baies nourricières ; « Cornucopia » en est la version remaniée

# ----- Pathfinder 2 : focalisés repris sur le texte source entier (21 novembre) -----
_R("crescent-scepter", impact=(P, ["insigne", "crainte"], "l'objet que je brandis paraît l'insigne du pouvoir que chacun redoute : qui veut me frapper est effrayé, et son coup s'en ressent"))
FICHES["shifting-form"]["options"].append(O("Flair", impact=(18, ["forme", "flair", "mètres"], "je flaire à 18 m")))
_R("malicious-shadow", impact=(6, ["ombre", "frappe"], "son ombre prend une forme mortelle et la frappe de 1d10 en moyenne à chaque instant, sans la quitter ; elle s'évanouit dans le noir complet"))
_R("spirit-object", impact_plus=[(2, ["frappe"], "1d4 en moyenne au voisin qu'il attaque à l'arrivée")])
_R("ki-form", impact_sats=[(9, ["rayon", "mètres"]), (2, ["émotion"])])
_R("tentacular-limbs", impact_sats=[(6, ["sort", "mètres"])])
_R("flurry-of-claws", impact=(7, ["griffe", "dragon"], "des griffes de dragon lacèrent deux ennemis voisins : 1d8 + 1d4 en moyenne chacun"))
_R("establish-ward", impact=(9, ["domaine", "nature", "frappe"], "je me lie au lieu : la nature y frappe pour moi de 2d8 en moyenne, un coup de plus par instant ; hors de lui, je suis ralenti de 1"), impact_sats=[(1, ["lenteur"])])
_R("wish-twisted-form", impact_sats=[(3, ["lenteur", "mètres"]), (1, ["résistance"])])
_R("rewrite-possibility", impact=(2, ["avenir", "essai"], "une minute : 1 ajouté à son entrée en lice ; une fois par instant, un essai rejoué avec 2 de plus, le meilleur gardé"), impact_sats=[(1, ["élan"])])
_R("life-giving-form", impact=(27, ["lumière", "vie", "lumineux"], "un phare de vie : mon toucher rend 6d8 en moyenne ; 5 retranché aux coups précis, mes poings frappent de 1d4 de plus ; le ténébreux me blesse de 5 de plus"),
   impact_plus=[(8, ["riposte", "lumineux"], "3d4 en moyenne aux morts-vivants qui me touchent")], guerit=True)
_R("tempest-form", impact_sats=[(10, ["rempart"])])
FICHES["tempest-form"]["options"][0] = O("Air", impact=(4, ["corps", "fluide", "air", "foudre"], "je vole à 6 m par instant, invisible dans les airs ; mes coups foudroient de 1d6 en moyenne"))
_R("touch-of-the-moon", options=[
    O("Forme lumineuse", impact=(4, ["marque", "phase", "lumineux"], "quatre phases, d'instant en instant : rien ; puis 1 aux coups et 4 aux blessures ; puis 1 aussi à la défense ; puis la défense seule")),
    O("Forme ténébreuse", impact=(4, ["marque", "phase", "ténébreux"], "quatre phases, d'instant en instant : rien ; puis 1 aux coups et 4 aux blessures ; puis 1 aussi à la défense ; puis la défense seule"))])
_R("vibrant-thorns", impact_plus=[(4, ["soin", "surcroît"], "1d6 en moyenne, juste après un de mes sorts de soin")])
_R("cinder-gaze", options=[
    O("Grand danger", impact=(2, ["flamme", "présage", "élan"], "2 ajouté à ma prochaine entrée en lice")),
    O("Vie nouvelle", impact=(P, ["flamme", "présage", "vie", "temporaire"], "un peu de vie d'emprunt à ma prochaine blessure")),
    O("Intuition vive", impact=(P, ["flamme", "présage", "savoir"], "le meilleur de deux essais pour me souvenir")),
    O("Bonne fortune", impact=(P, ["flamme", "présage", "chance"], "le meilleur de deux essais pour résister"))])
_R("euphoric-renewal", impact=(8, ["agonie", "exaltation"], "chaque fois que je reviens de l'agonie : un geste pour me relever, 1 ajouté à mes résistances, 8 points de vie d'emprunt"))
_R("sweet-dream", options=[
    O("Rêve de perspicacité", impact=(1, ["sommeil", "rêve", "raison"], "1 ajouté à ce qui relève de la raison")),
    O("Rêve de séduction", impact=(1, ["sommeil", "rêve", "prestance"], "1 ajouté à ce qui relève de la prestance")),
    O("Rêve de voyage", impact=(2, ["sommeil", "rêve", "vitesse", "mètres"], "1,5 m de plus par instant, arrondi à 2"))])
_R("overstuff", impact_sats=[(3, ["lenteur", "mètres"])])
_R("wordsmith", impact=(P, ["texte", "langue"], "un écrit passe dans une langue que je connais, sans rien y changer d'autre"))
_R("elemental-sheath", impact_sats=[(5, ["rempart"])])
_R("steal-the-sky", dur=(1, "MINUTES"))
_R("shadow-illusion", impact=(9, ["ombre", "fantasme"], "l'image d'un être ou d'une chose, qui ne tient que dans la pénombre ou le noir ; l'être frappe de 2d8 en moyenne"))
_R("hallowed-ground", impact_sats=[(1, ["faille"])])
_R("draconic-barrage", impact=(4, ["dragon", "énergie", "hasard"], "un petit dragon d'énergie, d'une espèce tirée au sort, crache sur un ennemi : 1d6 en moyenne, puis s'éteint"))
_R("hyperfocus", impact=(1, ["sens", "netteté"], "1 ajouté à ses sens précis, ses sens diffus deviennent précis ; mais elle ne perçoit plus rien au-delà de 6 m"), impact_sats=[(6, ["limite", "mètres"])])
_R("remember-the-lost", impact_plus=[(33, ["nom", "grief"], "6d10 en moyenne à l'ennemi dont je nomme les victimes")])
_R("winter-bolt", impact_plus=[(7, ["éclat", "froid"], "1d12 en moyenne de froid à elle et à ses voisins quand le glaçon éclate")])
_R("unblinking-flame-ignition", impact=(7, ["flamme", "aura"], "acculé, je m'embrase : je vois tout, je vole, un geste de plus par instant ; 1d12 en moyenne à qui commence son instant contre moi"))
_R("unbreaking-wave-advance", impact_plus=[(11, ["choc"], "3d6 en moyenne à qui est projeté contre un obstacle")])
_R("unfolding-wind-rush", impact_plus=[(P, ["mur", "vent"], "un mur de vent reste un instant là où je suis passé")])
_R("unfolding-wind-blitz", qty=3)
_R("spellmasters-ward", impact=(7, ["rune", "sort"], "jusqu'à 3 runes tournent autour de moi : chacune arrête 2d6 en moyenne des dégâts d'un sort"), qty=3)
_R("ki-cutting-sight", impact=(22, ["ki", "faille"], "je vois où arrêter le flux qui l'anime : mon prochain coup frappe de 4d10 en moyenne de plus"))
_R("charged-javelin", impact_sats=[(1, ["conducteur"])])
_R("wildfire", impact_plus=[(P, ["croissance"], "la nappe s'élargit à chaque instant où je la soutiens")])

# ----- Pathfinder 2, rituels, lot 1 : livre de base, version remaniée, Guide du joueur avancé (22 novembre) -----
# Un rituel inscrit son temps d'exécution au cercle Durée, son coût à la Composante (consommée), ses officiants en satellite
# Quantité de la Condition et en cercles périphériques. Homonyme d'un sort déjà publié, il en est une version ; l'échec qui
# peut s'écrire est une forme « Rituel manqué », l'autre reste une note.
_RT = dict(label="Rituel")
def _RM(**kw): return dict(label="Rituel manqué", **kw)
def _RV(page, rit, rem=None, **kw):
    """rit : rituel d'origine (None s'il n'existe que remanié) ; rem : rituel remanié (True = même nom)"""
    if rit: FICHES[page]["vp2"] = dict(src_idx=rit, **kw)
    if rem: FICHES[page]["vr"] = dict(src_idx=rit if rem is True else rem, **kw)
_M3 = (3, "METRES", "3 m"); _M6 = (6, "METRES", "6 m")
_MOI = dict(cible=1, cible_note=["officiant"])

_RV("animate-objects", "animate-object", True, qty_cible=None, loc=_M3, comp=["huile"],
    options=[_RT, _RM(impact=(P, ["animation", "fureur"], "l'objet s'anime, mais en furie : il cherche à détruire le meneur"))],
    notes=["Rituel : un jour de travail, un officiant en plus du meneur ; les huiles rares, d'autant plus chères que l'objet animé sera puissant, sont consommées. Manqué de peu, le rituel ne fait rien ; manqué tout à fait, l'objet s'anime en furie."])
_CONS = dict(aoe=_S(40), dur=(365, "JOURS"), cond=["autel"], comp=["encens", "offrande"], prix=(4, "platine"),
    notes=["Rituel : trois jours de chants, deux officiants en plus du meneur, autour d'un autel fixe. Le lieu favorise ceux qui s'y reconnaissent et gêne ceux qu'il réprouve. Manqué tout à fait, le lieu se refuse : pendant un an au moins, nul ne peut plus le consacrer (rien ne s'en inscrit)."])
_CONSO = lambda scelle: [
    dict(label="Consécration — lumineux" + scelle[0], impact=(1, ["lumineux", "faveur"] + scelle[1], "1 ajouté aux fidèles du lieu, 1 retranché à ceux qu'il réprouve" + scelle[2]), cible_note=[], **scelle[3]),
    dict(label="Profanation — ténébreux" + scelle[0], impact=(1, ["ténébreux", "faveur"] + scelle[1], "1 ajouté aux fidèles du lieu, 1 retranché à ceux qu'il réprouve" + scelle[2]), cible_note=[], **scelle[3])]
_SC0 = ("", [], "", {}); _SC7 = (", lieu scellé (rang 7)", ["ancrage"], " ; nul n'y entre ni n'en sort par magie, hormis les fidèles", dict(niveau=7, prix=(140, "platine")))
_RV("consecrate", "consecrate", True, options=_CONSO(_SC0) + _CONSO(_SC7), **_CONS)
_RV("create-undead", "create-undead", True, qty_cible=None, loc=_M3, cond=[], comp=["onyx"], cible_note=[], impact=(P, ["service"], "un mort relevé, à mon service s'il est assez faible"),
    options=[_RT, _RM(impact=(P, ["haine"], "le mort se relève, mais plein de haine : il cherche à détruire le meneur"))],
    notes=["Rituel : un jour, un officiant en plus du meneur ; l'onyx noir, d'autant plus cher que le mort relevé sera puissant, est consommé. Chaque sorte de mort-vivant a son propre rituel. Manqué tout à fait, le mort se relève dans la haine de qui l'a tiré de là."])
_RV("geas", "geas", True, cible=2, loc=_M3, cond=["accord"], impact=(P, ["serment"], "un acte imposé ou interdit, tenu aussi longtemps que la cible y consent"),
    impact_sats=[(4, ["nausée", "manquement"])], sats={}, dur=(P, None), fin=["accord"],
    options=[_RT, dict(label="Serment imposé (rang 5)", niveau=5, cible=3, cond=[], dur=(7, "JOURS"), fin=[]),
             _RM(cible=1, cond=[], impact=(P, ["serment"], "le serment retombe sur le meneur, contre son gré"))],
    notes=["Rituel : un jour, un officiant en plus du meneur, qui veille aux termes du serment. Qui est empêché de le tenir est pris de nausée, 1 de plus par jour, jusqu'à 4. Au rang 5, il se pose sur qui ne le veut pas, pour une semaine. Manqué tout à fait, il retombe sur le meneur."])
_RV("atonement", "atone", True, loc=_M3, comp=["encens", "offrande"], prix=(2, "platine"),
    notes=["Rituel : un jour, un officiant en plus du meneur ; encens et offrandes consommés, d'autant plus chers que le pénitent est puissant. Le pardon obtenu, il reste une tâche à accomplir, d'un mois au moins. Manqué de peu, la moitié du prix suffira la fois suivante ; manqué tout à fait, le pénitent est rejeté pour de bon (rien ne s'en inscrit)."])
_RV("plant-growth", "plant-growth", True, aoe=_S(2640), dur=(365, "JOURS"),
    options=[dict(label="Croissance végétale", impact=(P, ["croissance", "récolte"], "les récoltes d'un tiers plus abondantes")),
             dict(label="Flétrissement des récoltes", src_idx="blight", impact=(P, ["rabougrissement", "récolte"], "les récoltes réduites de moitié"))],
    notes=["Rituel : un jour, un officiant en plus du meneur, sur 800 m à la ronde et pour un an. Les deux formes se défont l'une l'autre. Manqué tout à fait, le rituel produit le contraire de ce qu'on voulait : sa forme manquée est l'autre forme de la page."])
_RV("call-spirit", "call-spirit", True, dur=(10, "MINUTES"), comp=["bougie", "encens"], prix=(5, "platine"), cond=["nom", "relique"], impact_sats=[(10, ["question"])],
    options=[_RT, _RM(impact=(P, ["mort", "hostile"], "des esprits mauvais répondent à la place et attaquent"), impact_sats=[])],
    notes=["Rituel : une heure, un officiant en plus du meneur ; il faut le nom de l'esprit et un lien avec lui (un bien, un vêtement, un reste). Une question par minute, dix minutes ; l'esprit répond comme il veut. Manqué tout à fait, des esprits mauvais viennent à sa place."])
_ALLY = lambda prim: dict(comp=["encens", "offrande"], prix=(2, "or"),
    options=[dict(label="Allié planaire"),
             dict(label="Appel primordial", src_idx="primal-call", cible=4, cible_sym=[], cond=[], cible_note=["bête", "fée", "plante"], loc=(160, "KILOMETRES", "160 km (100 miles)"), comp=["offrande"], prix=(1, "or")),
             _RM(impact=(P, ["courroux"], "l'entité s'offense : un signe de son déplaisir, ou un serviteur venu châtier"))],
    notes=["Rituel : un jour, deux officiants en plus du meneur (quatre pour l'Appel primordial, autour d'un cercle de fées), qui plaident la cause ; offrandes consommées, d'autant plus chères que l'être appelé est puissant. Le service se paie à part. Manqué tout à fait, l'entité s'offense."])
_RV("planar-ally", "planar-ally", "planar-servitor", **_ALLY(0))
_RV("resurrection", "resurrect", True, loc=_M3, cond=["mort"], cond_sats=[(1, ["ans"])], comp=["diamant"], prix=(75, "or"),
    impact=(P, ["vie", "retour"], "revient à la vie, à bout de forces"), impact_sats=[(7, ["jours", "faiblesse"])],
    options=[_RT, _RM(impact=(P, ["possession"], "un esprit mauvais prend le corps, ou pire"), impact_sats=[])],
    notes=["Rituel : un jour, deux officiants en plus du meneur ; le corps doit être là, à peu près entier, et la mort dater de moins d'un an. Les diamants, d'autant plus chers que le mort était puissant, sont consommés. Le revenu reste affaibli une semaine. Manqué tout à fait, autre chose prend le corps."])
_RV("awaken", "awaken-animal", True, loc=_M3, cible_note=["bête"], comp=["herbe"],
    impact=(10, ["raison", "lucidité", "prestance"], "l'esprit élevé jusqu'à 10 s'il était moindre ; la bête devient amicale"),
    options=[_RT, _RM(impact=(6, ["raison", "lucidité", "prestance", "haine"], "éveillée à 6 seulement, et dans une haine pure du meneur"))],
    notes=["Rituel : un jour, trois officiants en plus du meneur ; herbes consommées, d'autant plus chères que la bête est puissante. Manqué tout à fait, la bête s'éveille à demi et dans la haine."])
_RV("planar-binding", "planar-binding", "binding-circle", comp=["diagramme"], prix=(2, "or"), cible_note=[], impact=(P, ["marché"], "appelé dans le cercle pour y marchander un service"),
    options=[_RT, _RM(impact=(P, ["hostile"], "quelque chose d'affreux répond, que le cercle ne retient pas"))],
    notes=["Rituel : un jour, quatre officiants en plus du meneur dans l'édition d'origine (trois dans la version remaniée), chacun à l'un des points du diagramme où la puissance se concentre ; l'un d'eux trace le cercle qui retient l'être appelé le temps du marché. Les ingrédients du diagramme, d'autant plus chers que l'être est puissant, sont consommés. Manqué tout à fait, autre chose vient, et libre."])
_COM = lambda px, imp: dict(impact=imp, qty=7, dur=(10, "MINUTES"), comp=["encens"], prix=px,
    options=[dict(_RT), _RM(cible=1, cible_note=["psyché"], qty=None, loc=None, cond=[], impact=(4, ["hébétude"], "l'immensité entrevue hébète le meneur de 4, une semaine durant"), dur=(7, "JOURS"))],
    notes=["Rituel : un jour, un officiant en plus du meneur ; sept questions, dix minutes, des réponses d'un mot que l'être donne selon ses propres vues. Manqué tout à fait, le meneur entrevoit l'immensité et en reste hébété une semaine."])
_RV("commune", "commune", True, **_COM((15, "platine"), (P, ["réponse", "oui", "non"], "sept réponses d'un mot")))
_RV("commune-with-nature", "commune-with-nature", None, **_COM((6, "platine"), (P, ["savoir"], "sept réponses d'un mot sur le pays alentour")))
for _o in FICHES["commune-with-nature"]["vp2"]["options"][:1]: _o["loc"] = (5, "KILOMETRES", "5 km (3 miles)")
_RV("legend-lore", "legend-lore", "collective-memories", comp=["encens"], prix=(30, "platine"),
    options=[_RT, _RM(cible=1, cible_note=["psyché"], cond=[], impact=(P, ["passé", "absence"], "l'esprit du meneur se perd dans le passé, sourd au présent"), dur=(7, "JOURS"))],
    notes=["Rituel : un jour, deux officiants en plus du meneur ; le savoir vient dans l'heure qui suit. Manqué tout à fait, l'esprit du meneur se perd une semaine dans ce qu'il regardait."])
_RV("control-weather", "control-weather", True, loc=(3, "KILOMETRES", "3 km (2 miles)"), dur=(26, "HEURES"),
    notes=["Rituel : un jour, un officiant en plus du meneur ; le temps change sur 3 km à la ronde, pour 4d12 heures (26 en moyenne), selon ce que la saison permet. Manqué tout à fait, le temps tourne au contraire de ce qu'on voulait : le glyphe est le même, seul le résultat trahit."])
_RV("freedom", "freedom", None, loc=_M3, cond=["nom"], comp=["huile", "souvenir"], prix=(10, "platine"),
    impact=(P, ["libération", "prison", "pétrification", "stase"], "délivrée de tout ce qui l'emprisonne, la pétrifie ou la suspend"), impact_add=[],
    options=[_RT, _RM(verb=V("mouvement", True), cond=[], impact=(P, ["prison", "pétrification", "stase"], "l'entrave qu'on voulait lever se referme sur le meneur et les officiants"), **_MOI)],
    notes=["Rituel : un jour, deux officiants en plus du meneur, près de la cible ou du lieu où elle fut prise ; il faut son nom et son histoire. Huiles et objets liés à elle sont consommés, d'autant plus chers qu'elle est puissante. Manqué tout à fait, l'entrave se referme sur ceux qui officiaient."])
_RV("imprisonment", "imprisonment", None, loc=_M3, comp=["réactif"], prix=(80, "platine"),
    options=[dict(label="Enchaînement", impact=(P, ["prison", "chaînes"], "enchaînée, capable seulement de parler ; qui veut l'approcher ou la délivrer doit d'abord vaincre le sort")),
             dict(label="Prison close", impact=(P, ["prison", "lieu"], "incapable de quitter le lieu choisi ni de l'entamer")),
             dict(label="Sommeil", impact=(P, ["prison", "sommeil"], "un sommeil sans âge, que rompt un geste d'affection sincère")),
             dict(label="Stase temporelle", impact=(P, ["prison", "stase", "temps"], "suspendue hors du temps, pour la durée dite ou sans fin")),
             dict(label="Confinement minuscule (rang 9)", niveau=9, impact=(P, ["prison", "gemme"], "réduite ou changée en vapeur, enfermée dans un récipient ; le briser la tue")),
             dict(label="Ensevelissement (rang 10)", niveau=10, impact=(P, ["prison", "ensevelissement"], "ensevelie hors d'atteinte de tout, le lieu caché aux divinations")),
             _RM(impact=(P, ["prison"], "le meneur et les officiants s'emprisonnent eux-mêmes, de la façon qu'ils voulaient"), **_MOI)],
    notes=["Rituel : un jour, six officiants en plus du meneur, la cible tenue à 3 m tout du long ; les réactifs de la prison, d'autant plus chers que la cible est puissante, sont consommés. Seul le rituel de Liberté défait ces prisons. Manqué tout à fait, le meneur et les officiants s'emprisonnent eux-mêmes."])
_RV("glyph-of-warding", None, "rune-trap", loc=(2, "METRES", "contact"), comp=["pigment", "huile"], prix=(5, "or"),
    options=[dict(label="Glyphe de sort", impact=(P, ["piège", "sort"], "un sort hostile enfermé dans la rune, lâché sur qui la déclenche"), impact_sats=[(None, ["sort"])]),
             _RM(cible=P, aoe=_S(10), cond=[], impact=(14, ["force", "explosion"], "4d6 en moyenne par rang du sort enfermé, sur le meneur, l'officiant et tous ceux à 3 m"), impact_sats=[])],
    notes=["Rituel : une heure, un officiant en plus du meneur ; pigments et huiles consommés, d'autant plus chers que le sort enfermé est puissant. Un mot de passe ou un déclencheur garde la rune. Manqué tout à fait, la rune éclate au visage de ceux qui la traçaient."])
_RV("plane-shift", None, "planar-displacement", cible=P, qty_cible=None, aoe=_S(20), comp=["encens", "craie"], prix=(50, "platine"),
    notes=["Rituel : un jour, deux officiants en plus du meneur, dont l'un peut se tenir au lieu d'arrivée ; tous ceux du cercle changent de plan. Le cercle reste ouvert une minute pour qui veut revenir. Réussi de peu, on arrive à 1d10 × 40 km du but. Manqué tout à fait, on se trompe de plan, ou tout passage est interdit une semaine (rien ne s'en inscrit)."])
FICHES["wish"]["vr"] = dict(src_idx="manifestation", options=[dict(label="Manifestation"),
    dict(label="Souhait, rituel", src_idx="wish-rituel", loc=_M3, cond=["parole"], impact=(P, ["souhait"], "le plus grand désir de la cible, quel qu'il soit"), impact_sats=[],
         comp=["cendre", "pigment", "gemme"], prix=(10000, "platine"),
         notes=["Rituel : un jour, deux officiants en plus du meneur ; la cible dit son souhait à voix haute au début et à la fin. Réussi de peu, le souhait s'accomplit avec des suites imprévues ; manqué, il ne se fait pas, ou si peu que la cible en reste insatisfaite ; manqué tout à fait, il s'accomplit cruellement. Le glyphe est le même dans tous les cas : c'est l'issue qui trahit."])])
_RV("reincarnate", "reincarnate", None, loc=_M3, cond=["mort"], cond_sats=[(7, ["jours"])], comp=["herbe"], prix=(25, "or"), impact_sats=[(7, ["jours", "faiblesse"])],
    options=[_RT, _RM(impact=(P, ["vie", "corps", "bête"], "l'âme se trouve prise dans une bête sans raison"), impact_sats=[])],
    notes=["Rituel : quatre heures, deux officiants en plus du meneur ; un reste du corps suffit, la mort datant de moins d'une semaine. Le corps neuf est d'un peuple tiré au sort. Herbes consommées, d'autant plus chères que le mort était puissant. Manqué tout à fait, l'âme se trouve prise dans une bête."])
_RV("rest-eternal", "rest-eternal", None, loc=_M6, comp=["huile"], prix=(25, "or"),
    options=[_RT, _RM(cond=[], impact=(1, ["condamnation"], "les esprits s'irritent : le meneur et les officiants sont condamnés de 1, une semaine"), dur=(7, "JOURS"), **_MOI)],
    notes=["Rituel : un jour, deux officiants en plus du meneur ; les huiles dont on oint le corps sont consommées. L'esprit ne peut plus être appelé, relevé ni ramené, sauf par une magie plus haute. Manqué tout à fait, les esprits invoqués se retournent contre les officiants."])
_RV("simulacrum", "simulacrum", None, loc=_M6, cond=["vivant"], comp=["cheveu", "huile", "pigment"], prix=(30, "platine"),
    options=[_RT, _RM(impact=(P, ["glace", "hostile"], "le double s'éveille hostile à tous les officiants, et cherche leur perte"))],
    notes=["Rituel : un jour, trois officiants en plus du meneur ; un cheveu ou une goutte de sang du modèle, des huiles et des pigments, consommés. Le double de neige n'a ni les souvenirs ni les pouvoirs du modèle : il n'en a que l'apparence. Manqué tout à fait, il s'éveille hostile."])
_RV("astral-projection", "astral-projection", None, qty_cible=6, cond=["contact"], comp=["jacinthe"], prix=(5, "or"),
    options=[_RT, _RM(qty_cible=None, impact=(P, ["agonie", "condamnation"], "la séparation tourne mal : tous les officiants tombent, mourants"), **_MOI)],
    notes=["Rituel : une heure, deux officiants en plus du meneur, tous se tenant en cercle ; une jacinthe par voyageur, consommée. Les corps restent en suspens ; chacun peut revenir d'un geste. Le cordon rompu tue. Manqué tout à fait, tous les officiants tombent mourants."])
_RV("heroes-feast", "heroes-feast", None, qty_cible=10, comp=["offrande"], prix=(25, "or"),
    impact=(50, ["festin"], "50 points de vie rendus à chaque convive ; poison, maladie et peur chassés"), impact_plus=[(10, ["vigueur"], "10 points de vie d'appoint, douze heures")],
    options=[_RT, _RM(impact=(4, ["festin", "nausée"], "le festin est empoisonné : nausée de 4, douze heures sans remède"), impact_add=[], impact_plus=[], dur=(12, "HEURES"))],
    notes=["Rituel : quatre heures, un officiant en plus du meneur ; des êtres d'ailleurs servent dix convives, qu'il ne faut pas offenser. Manqué de peu, le festin n'a que le goût de la cendre ; manqué tout à fait, il est empoisonné."])
_RV("teleportation-circle", "teleportation-circle", None, dur=(1, "JOURS"), cond=["lieu", "connu"], comp=["encens", "craie"], prix=(50, "platine"), impact_sats=[(1620, ["kilomètres"])],
    notes=["Rituel : un jour, deux officiants en plus du meneur, dont l'un peut se tenir au lieu d'arrivée ; un cercle de 3 m mène, un jour durant, à un lieu connu à moins de 1 600 km (1 620, la valeur la plus proche qui s'écrive). Le double du prix l'ouvre dans les deux sens. Réussi de peu, on arrive à côté ; manqué tout à fait, le cercle mène au hasard (le glyphe est le même, seul le résultat trahit)."])
_RV("word-of-recall", "word-of-recall", None, qty_cible=7, dur=(365, "JOURS"), cond=["sanctuaire", "mot"], comp=["huile", "minéral"], prix=(500, "platine"),
    options=[_RT, _RM(impact=(P, ["plan", "rappel"], "le lien se noue à un lieu d'un autre plan : le mot y jette tous les participants"))],
    notes=["Rituel : sept jours, deux officiants en plus du meneur, au lieu sûr où l'on voudra revenir ; pendant un an, le mot dit par l'un des participants les y ramène tous, chacun à sa place. Manqué tout à fait, le lien se noue ailleurs, sans que nul le sache."])
_RV("clone", "clone", None, cond=["chair"], comp=["laboratoire"], prix=(10, "platine"), impact_sats=[(150, ["jours", "croissance"])],
    options=[_RT, _RM(impact=(P, ["clone", "intrus"], "le double paraît réussi, mais ne peut accueillir l'âme : une intelligence malveillante l'habite"))],
    notes=["Rituel : sept jours, trois officiants en plus du meneur ; un peu de chair de la cible, un laboratoire, des réactifs consommés. Le double croît 2d4 mois (5 en moyenne) ; l'âme y passe à la mort du corps, et s'y trouve affaiblie une semaine. Manqué tout à fait, autre chose l'habite."])
_RV("guards-and-wards", "ward-domain", None, aoe={"type": "cube", "size": 100}, dur=(7, "JOURS"), comp=["encens", "huile", "argent"], prix=(15, "platine"),
    impact=(P, ["verrou", "illusion", "scrutation", "ancrage"], "portes verrouillées, six entrées masquées en murs, scrutation aveugle, téléportation repoussée"), impact_sats=[(6, ["porte", "mur"])],
    options=[_RT, _RM(impact=(P, ["piège", "hostile"], "le lieu se piège contre le meneur et les siens"), impact_sats=[])],
    notes=["Rituel : un jour, trois officiants en plus du meneur, à brûler l'encens, oindre les seuils et tirer des lignes d'argent ; le domaine est gardé une semaine. Manqué tout à fait, le lieu se retourne contre ceux qu'il devait garder."])
_RV("demiplane", "create-demiplane", None, cond=["plan"], comp=["matière"], prix=(80, "platine"), aoe={"type": "cube", "size": 100},
    impact=(P, ["demi-plan", "clef"], "un demi-plan de 30 m de côté, et la clef qui y mène"),
    options=[_RT, dict(label="Aménagement", cond=["clef"], impact=(P, ["demi-plan", "ajout"], "le demi-plan agrandi d'autant, ou doté d'un trait : vie propre, élément, pesanteur, autre clef, portail, absence de bornes")),
             _RM(verb=V("mouvement"), no_aoe=True, cond=[], impact=(P, ["plan", "hostile"], "tous les officiants sont jetés sur un plan inconnu"), **_MOI)],
    notes=["Rituel : neuf jours, trois officiants en plus du meneur, depuis un plan qui touche à l'entre-deux ; les officiants y sont portés à la fin. Avec la clef, le même rituel agrandit ou aménage un demi-plan existant. Manqué tout à fait, tous sont jetés ailleurs."])

PF2_RIT1 = {
"inveigle": P2("Enjôlement", REL, 3, ["amitié", "confiance"], why="la cible me tient pour un ami proche et trouve raisonnable tout ce que je suggère", loc=_M3, dur=(365, "JOURS"), fin=["demande", "contraire"],
    cible_note=["psyché"], comp=["huile"], prix=(1, "platine"),
    options=[O("Rituel"), O("Rituel manqué", impact=(P, ["haine"], "la cible me hait pour toute la durée"), fin=[])]),
"heartbond": P2("Lien des cœurs", REL, 2, ["lien", "état", "direction"], why="une fois par jour, chacun sait où est l'autre, à quelle distance, et ce qui l'affecte", qty_cible=2, loc=_M6, dur=(P, None), fin=["anneau", "perte"],
    cond=["affection", "anneau"], comp=["vin", "anneau"], prix=(4, "platine"),
    options=[O("Rituel"), O("Rituel manqué", cond=[], fin=[], impact=(2, ["maladresse", "hébétude"], "un contrecoup discordant : chaque participant est maladroit et hébété de 2 dès qu'il approche d'un autre"), dur=(7, "JOURS"))]),
"unseen-custodians": P2("Gardiens invisibles", EXI, 7, ["service", "lieu"], why="trois serviteurs de force pure, attachés au lieu", cible_note=["serviteur"], qty=3, aoe={"type": "cube", "size": 100}, dur=(365, "JOURS"),
    comp=["huile", "sel", "herbe"], prix=(15, "or"),
    options=[O("Rituel"), O("Rituel manqué", qty=6, impact=(4, ["force", "hostile"], "six serviteurs hostiles, qui frappent de 1d6 en moyenne et brisent ce qui m'appartient"))]),
"fantastic-facade": P2("Façade fantastique", NVIS, P, ["ville", "apparence", "habitant"], why="l'aspect, le bruit, le toucher et l'odeur d'une ville entière et de ceux qui s'y trouvent", src_idx="fantastic-fa-ade",
    aoe=_S(5280), dur=(P, None), comp=["peinture", "voile", "minéral"], prix=(2000, "platine"), sens=[("vue", None), ("ouïe", None), ("toucher", None), ("odorat", None)], manif=["ville"],
    options=[O("Rituel"), O("Rituel manqué", impact=(P, ["apparence", "chaos"], "des illusions imprévues et sans maître : couleurs mouvantes, puanteurs, passants à l'air de squelettes"), dur=(30, "JOURS"))]),
}
FICHES.update(PF2_RIT1)

# ----- Pathfinder 2, rituels, lot 2 : Secrets de la magie, bestiaires, aventures, Rage des éléments (23 novembre) -----
_RI = O("Rituel")
def _RX(**kw): return O("Rituel manqué", **kw)
_Q = V("qualite")
PF2_RIT2 = {
"elemental-sentinel": P2("Sentinelle élémentaire", INV, 1, ["veille", "alerte"], why="un feu follet élémentaire, logé dans l'objet, veille sur la pièce et m'avertit en pensée de ce que je lui ai dit de guetter", cible_obj=["objet"],
    dur=(P, None), fin=["bris"], comp=["encens", "herbe"], prix=(15, "or"), impact_sats=[(30, ["pensée", "mètres"])],
    options=[_RI, _RX(impact=(P, ["veille", "mensonge"], "l'esprit, pris au piège, ne rend que des rapports trompeurs"))]),
"guardians-aegis": P2("Égide du gardien", REL, 2, ["lien", "état", "direction", "partage"], why="le gardien et son protégé savent toujours où est l'autre et ce qui l'affecte ; à moins de 9 m, le gardien prend sur lui une part des blessures du protégé", cible_note=["officiant"],
    dur=(7, "JOURS"), comp=["huile"], prix=(1, "platine"), impact_sats=[(9, ["partage", "mètres"])],
    options=[_RI, _RX(impact=(P, ["isolement"], "le lien se retourne : aucun des deux ne peut plus rien apporter de bon à l'autre"), impact_sats=[])]),
"mystic-carriage": P2("Carrosse mystique", EXI, 1, ["voyage", "destination"], why="un carrosse qui mène de lui-même au lieu nommé, par les routes et les chemins", cible_obj=["carrosse"],
    dur=(7, "JOURS"), fin=["arrivée"], cond=["nom", "lieu"], comp=["jouet", "encens", "plume"], prix=(5, "platine"), impact_sats=[(400, ["kilomètres"]), (18, ["allure", "mètres"]), (4, ["passager"])],
    options=[_RI, _RX(verb=INV, cible=4, cible_obj=[], cible_note=["cheval"], qty=4, impact=(P, ["hostile"], "nul carrosse : quatre chevaux surgissent et attaquent"), impact_sats=[], fin=[])]),
"concealments-curtain": P2("Rideau de dissimulation", NVIS, 3, ["vue", "officiant"], why="la cible ne peut plus voir aucun des officiants, et ne s'en doute pas ; ce n'est pas eux que le sort cache, c'est son œil qu'il ferme",
    dur=(7, "JOURS"), cond=["nom", "regard", "minuit"], comp=["miroir", "fruit", "aiguille"], prix=(10, "platine"),
    options=[_RI, _RX(cond=[], impact=(P, ["cécité"], "le sort se retourne : tous les officiants sont aveugles un jour"), dur=(1, "JOURS"), **_MOI)]),
"garden-of-death": P2("Jardin de mort", ATT, P, ["poison", "plante", "bête"], why="tout ce que le pays compte de plantes et de bêtes venimeuses vient croître et vivre là ; elles épargnent les officiants", aoe=_S(40),
    dur=(365, "JOURS"), comp=["eau", "poison", "sang"], prix=(5, "platine"),
    options=[_RI, _RX(no_aoe=True, impact=(P, ["morsure", "poison"], "la bête la plus venimeuse du pays mord chacun des officiants"), **_MOI)]),
"dread-ambience": P2("Atmosphère d'effroi", NQ, P, ["effroi"], 1, "le lieu pèse sur qui y entre : 1 retranché à quiconque y résiste à la peur", aoe=_S(2979),
    dur=(365, "JOURS"), comp=["bougie", "sel", "herbe"], prix=(8, "platine"),
    options=[_RI, _RX(no_aoe=True, impact=(1, ["volonté"], "1 retranché à la volonté des officiants, une semaine"), dur=(7, "JOURS"), **_MOI)]),
"portrait-of-spite": P2("Portrait de rancune", NQ, 3, ["maladresse", "faiblesse", "épuisement", "hébétude"], 2, "le châtiment choisi, infligé au portrait peint de son sang, frappe la cible de 2 ; le portrait en devient la caricature",
    dur=(365, "JOURS"), fin=["portrait", "destruction"], cond=["nom", "visage"], comp=["peinture", "sang"], prix=(10, "platine"), impact_sats=[(4, ["heures", "délai"])],
    options=[_RI, _RX(cond=[], fin=[], impact=(4, ["maladresse", "faiblesse", "épuisement", "hébétude"], "le portrait prend les traits des officiants : le châtiment les frappe eux, de 4"), **_MOI)]),
"the-worlds-a-stage": P2("Le monde est un théâtre", ORD, 2, ["destin", "essai"], 1, "le sort lie le destin à la pièce jouée : chaque officiant rejoue un essai, s'il sert l'issue mise en scène", cible_note=["officiant"],
    dur=(30, "JOURS"), cond=["représentation", "public"], cond_sats=[(100, ["spectateur"])], comp=["costume", "scène"], consumed=False,
    options=[_RI, _RX(impact=(1, ["condamnation"], "la pièce tourne au désastre et le destin frappe : chaque officiant est condamné de 1, un mois"))]),
"asmodean-wager": P2("Pari scellé", REL, 2, ["pari", "serment"], why="chaque parieur engage un bien ou une promesse sur une issue à venir ; le perdant est tenu par un serment des plus puissants", cible_note=["officiant"],
    dur=(P, None), fin=["issue"], cond=["accord"], comp=["parchemin", "encre", "gage"], prix=(5, "platine"),
    options=[O("Enjeu : un bien ou une promesse"),
             O("Enjeu : la vie", impact=(P, ["pari", "mort", "sursis"], "le perdant meurt sur-le-champ ; le gagnant survivra une fois à ce qui devait le tuer")),
             _RX(impact=(P, ["pari", "perte"], "les termes se retournent : tous les parieurs sont tenus pour perdants, quelle que soit l'issue"))]),
"awaken-object": P2("Éveil d'objet", TR, 1, ["conscience", "vue", "ouïe", "langue"], why="un petit objet inerte s'éveille : il voit, entend, comprend une langue sans la parler, et reste indifférent à tous", cible_obj=["objet"],
    dur=(P, None), comp=["gemme", "épice"], prix=(25, "platine")),
"ideal-mimicry": P2("Poupée d'envoûtement", NE, 3, ["douleur", "pensée", "poupée"], 11, "", loc=(60, "METRES", "60 m (200 pieds)"), qty=10, cond=["regard", "poupée"],
    comp=["cheveu", "ongle", "sang"], prix=(5, "platine"),
    options=[O("Forme de base", impact=(11, ["douleur", "pensée", "poupée"], "un seul lien dans la poupée (cheveu, ongle ou sang) : 3d6 en moyenne chaque fois qu'on la maltraite, dix fois")),
             O("Forme maximale", impact=(32, ["douleur", "pensée", "poupée"], "les trois liens : 9d6 en moyenne chaque fois, dix fois")),
             _RX(impact=(32, ["douleur", "pensée", "poupée"], "la poupée se retourne : chaque coup qu'on lui porte frappe les officiants de 9d6 en moyenne"), **_MOI)]),
"bathe-in-blood": P2("Bain de sang", TR, 1, ["jeunesse", "ans"], 20, "vingt ans de moins, ou vingt ans sans vieillir", cond=["sang", "peuple"], cond_sats=[(6, ["heures"])],
    comp=["herbe", "sang"], prix=(100, "platine"),
    options=[_RI, _RX(verb=NE, impact=(P, ["mort"], "le bain tue qui s'y plonge"))]),
"abyssal-pact": P2("Pacte astral", INV, 9, ["faveur"], why="", cond=["pair"], qty=3,
    options=_FACES(["faveur"], None, "un à trois êtres de la même face que moi, tenus de me rendre une faveur") + [_RX(impact=(P, ["hostile"], "dérangés, ils paraissent et attaquent aussitôt"))]),
"fey-abeyance": P2("Carillons contre les fées", NF, P, ["fée", "gêne", "fer"], why="les fées s'y sentent mal, tout coup les blesse comme le fer froid, et les cloches les tourmentent là où elles pendent", aoe={"type": "cube", "size": 60},
    dur=(7, "JOURS"), comp=["huile", "cloche"], prix=(5, "or"), impact_sats=[(3, ["cloche"])],
    options=[_RI, _RX(impact=(P, ["fée", "attirance"], "rien ne se fait, sinon qu'une fée importune s'intéresse au lieu"), impact_sats=[])]),
"tattoo-whispers": P2("Tatouages murmurants", REL, 2, ["tatouage", "murmure"], why="les officiants portent le même tatouage, orné d'une bouche : ce que l'un articule sans voix, le tatouage de l'autre le lui murmure", cible_note=["officiant"],
    loc=(36, "METRES", "36 m (120 pieds)"), dur=(1, "JOURS"), cond=["vue"], comp=["encre", "aiguille"], prix=(2, "platine"),
    options=[_RI, _RX(impact=(1, ["hébétude"], "un contrecoup de parasites : tous les officiants sont hébétés un jour"))]),
"community-repair": P2("Réparation commune", ORD, 1, ["réparation", "souvenir"], why="un ouvrage commun, pont, puits ou fresque, retrouve son état premier par la force des souvenirs qu'on y attache", cible_obj=["ouvrage"],
    loc=_M3, cond=["souvenir"], comp=["pigment"], prix=(5, "platine"),
    options=[_RI, _RX(verb=NINT, cible_obj=[], cond=[], impact=(3, ["allure", "mètres"], "l'ouvrage se refuse et les souvenirs s'aigrissent : près de lui, les officiants perdent 3 m d'allure et aucune joie ne les touche, une semaine"), dur=(7, "JOURS"), **_MOI)]),
"awaken-portal": P2("Réveil de portail", INT, 1, ["portail", "éveil"], why="un portail endormi se rouvre ; il faut l'éveiller à ses deux bouts, et le premier éveillé attend l'autre quelques jours", cible_obj=["portail"],
    dur=(4, "JOURS"),
    options=[_RI, _RX(verb=INV, cible=4, cible_obj=[], impact=(P, ["hostile"], "une créature hostile est tirée par le portail et attaque"), impact_plus=[(1, ["hébétude"], "le contrecoup hébète le meneur de 1, un jour")])]),
"extract-brain": P2("Extraction du cerveau", SEP, 3, ["cerveau", "conservation"], why="le cerveau d'un être consentant, entravé ou mort depuis moins d'une heure, retiré intact pour être placé dans un récipient ou un corps fabriqué", cond=["entrave"],
    comp=["outil", "sel"], prix=(10, "platine"),
    options=[_RI, _RX(impact=(P, ["cerveau", "intrus"], "l'opération semble réussir, mais le cerveau se déforme en une chose hostile"))]),
"statuette": P2("Statuette", NINT, 1, ["statuette", "taille"], why="un grand objet devient une statuette de lui-même, légère, jusqu'à ce qu'on la pose pour lui rendre sa taille", cible_obj=["objet"],
    dur=(1, "JOURS"), fin=["pose"], cond=["seuil"], cond_sats=[(85, ["mètres", "cubes"])],
    options=[_RI, _RX(cond=[], fin=[], impact=(P, ["statuette", "perte"], "c'est le meilleur objet que porte le meneur qui rétrécit, inutilisable"), dur=(7, "JOURS"))]),
"terminate-bloodline": P2("Extinction de lignée", NQ, 3, ["maladie", "lignée", "contagion"], why="un mal dépérissant frappe la cible et gagne, au simple contact, ses parents et ses enfants, qui le transmettent à leur tour",
    comp=["sang", "trésor"], prix=(10, "platine")),
"mosquito-blight": P2("Fléau de moustiques", INV, P, ["insecte", "maladie"], why="des insectes tenaces harcèlent quiconque entre, et lui portent chaque jour un mal qui épuise", aoe=_S(5280),
    dur=(P, None), fin=["ruche", "destruction"], comp=["ambre", "encens"], prix=(75, "platine"), impact_plus=[(1, ["insecte", "faveur"], "1 ajouté aux insectes et araignées du lieu")],
    options=[_RI, _RX(cible=1, no_aoe=True, fin=[], impact=(P, ["insecte", "maladie"], "les insectes se jettent sur le meneur et lui portent le mal"), impact_plus=[])]),
"phantom-ship": P2("Vaisseau fantôme", TR, 1, ["intangible", "équipage"], why="le navire et tous ceux qu'il porte deviennent intangibles ; il file à pleine allure quel que soit le vent, au travers des écueils, tant qu'il touche l'eau", cible_obj=["navire"],
    dur=(1, "HEURES"), cond=["mort-vivant", "équipage", "eau"], comp=["perle"], prix=(5, "platine"), impact_plus=[(1, ["navigation"], "1 ajouté à qui le manœuvre par gros temps")],
    options=[_RI, _RX(impact=(P, ["intangible", "chute"], "le navire seul devient intangible : tous passent au travers et tombent à l'eau"), dur=(10, "MINUTES"), impact_plus=[])]),
"unseen-heralds": P2("Hérauts invisibles", EXI, P, ["bouche", "voix"], why="trois bouches d'illusion posées dans le lieu, qui disent ce que je veux, quand je veux, ou le répètent", qty=3, aoe={"type": "cube", "size": 100},
    dur=(365, "JOURS"), comp=["huile", "sel", "herbe"], prix=(15, "or"), sens=[("ouïe", None)], manif=["voix"],
    options=[_RI, _RX(qty=6, impact=(P, ["bouche", "vacarme"], "les bouches hurlent, bredouillent et jurent sans trêve : nul repos à portée de voix"), dur=(1, "JOURS"))]),
"lucky-month": P2("Mois de chance", ORD, 2, ["chance", "essai"], 1, "une fois dans le mois, le porteur du gage rejoue un essai et garde le meilleur", dur=(30, "JOURS"), cond=["gage"],
    comp=["mets", "gage"], prix=(1, "platine"),
    options=[_RI, _RX(cond=[], impact=(1, ["malchance", "essai"], "une fois par semaine, le premier essai qui compte est rejoué et le pire gardé, gage porté ou non"))]),
"last-nights-vigil": P2("Veillée de la dernière nuit", _Q, 2, ["guérison", "maladie"], why="au matin, l'être aimé a recouvré toutes ses forces, et l'un de ses maux recule d'un degré", cond=["nuit", "amour", "veille"],
    comp=["encens"], prix=(1, "platine"),
    options=[_RI, _RX(verb=NQ, cible=1, cond=[], impact=(P, ["fatigue"], "la veille n'a servi à rien : le veilleur est épuisé un jour"), dur=(1, "JOURS"))]),
"regale-the-lost-ones": P2("Régal des égarés", ORD, P, ["esprit", "apaisement"], why="les esprits et les morts qui hantent le bourg, réjouis par le spectacle, se font moins hostiles et plus aisés à défaire", cible_note=["bourg"],
    dur=(365, "JOURS"), cond=["spectacle"], comp=["offrande", "costume"], prix=(2, "or"),
    options=[_RI, _RX(verb=NORD, impact=(P, ["esprit", "colère"], "les esprits s'irritent : plus sournois, plus redoutables"))]),
"sweetest-solstice": P2("Le plus doux des solstices", EXI, 2, ["soupe", "repas"], why="une soupe de sésame qui ne tarit pas : un repas chaud pour tout le bourg, une semaine durant", qty_cible=P,
    dur=(7, "JOURS"), cond=["hiver", "plaisanterie"], comp=["sésame", "sucre", "riz"], prix=(2, "or"), impact_plus=[(1, ["courage"], "1 ajouté aux officiants contre la peur, un mois")],
    options=[_RI, _RX(impact=(4, ["soupe", "nausée"], "la soupe est gâtée et rend le bourg malade ; les officiants en ont la nausée (4), douze heures sans remède"), impact_plus=[], dur=(12, "HEURES"))]),
"ransack-the-night": P2("Pillage de la nuit", NVIS, 2, ["dissimulation"], why="", cible_note=["officiant"], dur=(12, "HEURES"), cond=["nuit"], comp=["sel", "agrume", "épice"], prix=(75, "or"),
    options=[O("Forme ténébreuse", impact=(P, ["dissimulation", "ténébreux"], "une brume noire voile les officiants aux êtres de la face ténébreuse et aux morts-vivants les plus faibles, tant qu'ils ne les attaquent pas")),
             O("Forme lumineuse", impact=(P, ["dissimulation", "lumineux"], "une brume claire voile les officiants aux êtres de la face lumineuse les plus faibles, tant qu'ils ne les attaquent pas")),
             _RX(impact=(P, ["aveuglement"], "la brume trouble les sens des officiants : ce sont eux qui distinguent mal ces êtres, un jour durant"), dur=(1, "JOURS"))]),
"winters-breath": P2("Souffle de l'hiver", EXI, 2, ["thé", "réconfort"], why="un pavillon, un thé servi à six convives courtois : chacun choisit d'être remis de ses fatigues ou gardé du froid et du chaud", qty_cible=6,
    comp=["offrande"], prix=(15, "or"), impact_plus=[(10, ["vigueur"], "10 points de vie d'appoint, douze heures")], sens=[("vue", None), ("goût", None), ("odorat", None)], manif=["pavillon", "thé"],
    options=[_RI, _RX(impact=(3, ["thé", "nausée"], "le thé déçoit et accable : nausée de 3, douze heures sans remède"), impact_plus=[], dur=(12, "HEURES"))]),
"perfection-of-essence": PR("Perfection de l'essence", TR, 1, ["immortalité"], why="je ne vieillis plus que si je le veux, et rien ne me tue hors la vieillesse ; mort pour de bon, je renais adulte ailleurs au bout d'un an",
    dur=(P, None), fin=["interdit"], cond=["interdit", "poison"], cond_sats=[(3, ["interdit"])], comp=["mets", "herbe", "minéral"], prix=(4500, "platine"),
    options=[_RI, _RX(verb=NQ, cond=[], fin=[], impact=(P, ["poison"], "le poison de l'épreuve l'emporte, et plus virulent encore"))]),
"bountiful-oasis": PR("Oasis généreuse", EXI, P, ["source", "pureté"], why="une source pure jaillit, de quoi abreuver une douzaine de personnes ; elle se purifie d'elle-même à chaque aube", comb="Eau", aoe=_S(10),
    dur=(365, "JOURS"), comp=["goutte"],
    options=[_RI, _RX(impact=(P, ["croupissement", "maladie"], "une mare fétide qui ne sèche jamais, pleine d'insectes, et qui rend malade qui en boit"))]),
"sky-signs": PR("Signes du ciel", VIS, P, ["message", "ciel"], why="un message simple, écrit en nuages le jour ou en aurores la nuit, visible jusqu'à l'horizon", dur=(8, "HEURES"),
    comp=["lentille", "poussière"], prix=(30, "platine"), impact_sats=[(5, ["mot"])], sens=[("vue", None)], manif=["ciel"],
    options=[_RI, _RX(impact=(P, ["message", "contraire"], "les esprits de l'air, offensés, écrivent le contraire, lisible de tous"))]),
}
FICHES.update(PF2_RIT2)
_RV("mind-swap", "mind-swap", None, cible=2, qty_cible=2, loc=_M3, dur=(7, "JOURS"), cond=["peuple"], comp=["miroir"], prix=(5, "platine"),
    options=[_RT, _RM(qty_cible=None, cond=[], impact=(2, ["hébétude"], "des souvenirs brouillés se déversent : le meneur et l'officiant sont hébétés de 2, une semaine"), **_MOI)],
    notes=["Rituel : un jour, un officiant en plus du meneur ; deux êtres du même peuple échangent leurs esprits pour une semaine, chacun maître du corps de l'autre. Qui meurt dans un corps meurt tout à fait ; à la fin, l'esprit dont le corps est mort meurt aussi. Les miroirs ornés, d'autant plus chers que les cibles sont puissantes, sont consommés. Manqué tout à fait, les officiants restent hébétés."])
FICHES["planar-ally"]["vr"]["options"] = list(FICHES["planar-ally"]["vr"]["options"])
FICHES["planar-ally"]["vr"]["options"].insert(2, dict(label="Serviteur élémentaire", src_idx="elemental-servitor", cible_note=["élémentaire"], cible_sym=[], cond=[]))
# Rituels fondus dans une page (même glyphe) et rituels écartés, avec leur raison
PF2_RIT_FONDU = {"daemonic-pact": "abyssal-pact", "div-pact": "abyssal-pact", "infernal-pact": "abyssal-pact", "primal-call": "planar-ally", "blight": "plant-growth",
                 "commune-with-nature": "commune", "elemental-servitor": "planar-ally"}
PF2_RIT_ECARTE = {
 "purify-soul-path": "ne lève que la corruption d'une arme d'âme, mécanique d'archétype", "establish-nexus": "lignes telluriques et leur puisage : mécanique propre au jeu",
 "empower-ley-line": "lignes telluriques et leur puisage : mécanique propre au jeu", "angelic-messenger": "voyage d'un messager vers les fidèles de son dieu ; l'effet est le Changement de plan déjà publié",
 "owb-pact": "créatures propres à Golarion", "arcane-weaving": "échange de sorts connus : mécanique de classe", "amity-cycle": "cités de Thuvia (Golarion)",
 "create-skinstitch": "créature propre à Golarion, commandée au nom d'un dieu", "ravenous-reanimation": "dragon devenu mort-vivant d'une espèce propre au bestiaire",
 "unfettered-mark": "évasion d'une prison précise de Golarion", "commune-with-corazal": "entité et forêt de Golarion", "drain-planar-connection": "lieu et intrigue d'une aventure",
 "harrowing": "jeu de cartes divinatoire de Golarion ; ses effets sont des relances", "blunt-the-final-blade": "guillotines de Galt (Golarion)", "anima-invocation-modified": "intrigue d'une aventure",
 "raga-of-remembrance": "avatar d'un héros de Vudra (Golarion)", "power-of-the-beasts": "épreuve qui octroie un don de jeu", "seed-of-mercy": "épreuve qui octroie un don de jeu",
 "the-unseeing-blade-master": "épreuve qui octroie un don de jeu", "retreat-among-the-rains": "réapprentissage de dons : mécanique de jeu",
 "gnaw-at-the-moon": "culte de la lune, qui n'existe pas dans Inarama", "open-the-wall-of-ghosts": "lieu d'une aventure", "transmigrate": "intrigue d'une aventure",
}
# les paysages mentaux : écartés comme leurs équivalents de Pathfinder 1, pour la même raison
for _k in ("construct-mindscape", "mindscape-door", "mindscape-shift", "destroy-mindscape"):
    PF2_RIT_ECARTE[_k] = "repose sur les « mondes intérieurs » (mindscapes), sous-système de règles propre à Pathfinder"
PF2_RIT_DOUTE = []

# ----- Pathfinder 2 : sorts ordinaires repris sur le texte source entier (24 novembre) -----
def _AS(k, *sats): FICHES[k]["impact_sats"] = list(FICHES[k].get("impact_sats") or []) + list(sats)
def _AP(k, *plus): FICHES[k]["impact_plus"] = list(FICHES[k].get("impact_plus") or []) + list(plus)
_AS("tether", (3, ["lenteur", "mètres"]))
_AS("spiritual-guardian", (50, ["réserve"]))
_AS("duplicate-foe", (14, ["perte"]))
_AP("summon-archmage", (2, ["hébétude", "départ"], "à son départ, il hébète de 2 les ennemis proches et peut rompre l'un de leurs sorts"))
_AP("draw-the-lightning", (13, ["orage"], "2d12 en moyenne de plus sous un ciel d'orage"))
_AP("horizon-thunder-sphere", (7, ["éclat", "attente"], "tenue un instant de plus, elle éclate : 2d6 en moyenne à tous ceux à 3 m de la cible"))
_AP("pernicious-poltergeist", (2, ["effroi"], "ou bien il se montre : effroi de 2"), (18, ["force", "débris"], "ou bien il jette des débris : 4d8 en moyenne à tous"))
FICHES["wall-of-flesh"]["options"] = [O("Bouches", impact_plus=[(4, ["morsure"], "1d6 en moyenne à qui finit son instant près du mur")]),
    O("Yeux", impact_plus=[(2, ["vue", "vigilance"], "je vois par ses yeux : 2 ajouté à ma vigilance")]),
    O("Bras", impact_plus=[(P, ["étreinte"], "il agrippe qui finit son instant près de lui")])]
_AP("volcanic-eruption", (11, ["chaleur"], "3d6 en moyenne à tous ceux de la colonne et de ses abords, quoi qu'il arrive"))
_AS("volcanic-eruption", (50, ["gangue", "réserve"]))
_AP("indolent-haze", (15, ["âme", "dormeur"], "6d4 en moyenne à qui dort dans la brume"))
_i = FICHES["avenging-wildwood"]["impact"]; FICHES["avenging-wildwood"]["impact"] = (9, _i[1], _i[2] + " ; ses branches frappent de 2d8 en moyenne")
FICHES["summon-elemental-herald"]["options"] = [
    O("Air", impact=(45, ["héraut", "tornade"], "10d8 en moyenne à son arrivée"), impact_plus=[(P, ["rabat", "départ"], "à son départ, il jette à terre ou rabat de 12 m ceux d'une ligne")]),
    O("Terre", impact=(35, ["héraut", "crevasse"], "10d6 en moyenne à son arrivée ; les plus malchanceux tombent dans la crevasse"), impact_plus=[(28, ["fracas", "départ"], "5d10 en moyenne quand la crevasse se referme")]),
    O("Feu", impact=(35, ["héraut", "lave"], "10d6 en moyenne à son arrivée"), impact_plus=[(11, ["persistance"], "3d6 en moyenne à chaque instant"), (21, ["colonne", "départ"], "6d6 en moyenne à son départ")]),
    O("Métal", impact=(44, ["héraut", "éclat", "étincelle"], "4d8 + 4d12 en moyenne à son arrivée"), impact_plus=[(35, ["rouille", "départ"], "10d6 en moyenne au métal à son départ")]),
    O("Eau", impact=(44, ["héraut", "ouragan", "grêle"], "4d10 + 4d10 en moyenne à son arrivée"), impact_plus=[(27, ["flot", "départ"], "6d8 en moyenne à son départ, et repousse de 6 m")]),
    O("Bois", impact=(33, ["héraut", "racine"], "6d10 en moyenne à son arrivée ; 3 m d'allure en moins"), impact_plus=[(33, ["racine", "départ"], "6d10 en moyenne à son départ")])]

# ----- Pathfinder 2 : versions des pages déjà publiées, relues sur le texte source (24 novembre) -----
# La comparaison automatique ne voyait que niveau, portée, durée, zone et dégâts : ici, ce que le texte change d'autre.
def _VV(k, both=None, vp2=None, vr=None):
    for key, d in (("vp2", vp2), ("vr", vr)):
        if key in FICHES[k]:
            FICHES[k][key] = {**FICHES[k][key], **(both or {}), **(d or {})}
def _OB(k, *labels):
    o = {x["label"]: x for x in FICHES[k]["options"]}
    return [dict(o[l]) for l in labels]
_VV("chill-touch", dict(impact_sats=[]))
_VV("guidance", dict(impact=(1, ["chance"], "1 ajouté à un essai, au choix")))
_VV("mending", dict(impact=(5, ["réparation"], "5 points rendus à l'objet par rang du sort")))
_VV("prestidigitation", dict(options=_OB("prestidigitation", "Saveur et température") + [dict(label="Soulèvement", impact=(P, ["lévitation"], "un objet léger soulevé d'un pied"))] + _OB("prestidigitation", "Babiole", "Nettoyage")))
_VV("shocking-grasp", vp2=dict(impact_sats=[(2, ["persistance", "acier"])]), vr=dict(impact_sats=[(1, ["maladresse", "acier"])]))
_VV("bane", dict(impact=(1, ["chance"], "1 retranché aux attaques des ennemis de la zone"), qty_cible=None))
_VV("bless", dict(impact=(1, ["chance"], "1 ajouté aux attaques des alliés de la zone"), qty_cible=None))
_VV("burning-hands", dict(impact_add=[]))
_VV("charm-person", dict(cond=[]))
_VV("color-spray", dict(cond=[], impact=(P, ["aveuglement", "étourdissement"], "étourdie, aveuglée un instant, éblouie une minute")))
_VV("create-or-destroy-water", dict(options=[dict(label="Création", impact=(8, ["eau", "litres", "création"], "8 litres d'eau (2 gallons)"))]))
_VV("detect-magic", dict(impact=(P, ["présence"], "la présence ou l'absence de magie, rien de plus")))
_VV("entangle", dict(impact_sats=[(3, ["lenteur", "mètres"])]))
_VV("expeditious-retreat", dict(impact=(9, ["course", "mètres"], "9 m de plus par instant")))
_VV("false-life", vp2=dict(impact=(6, ["vie", "temporaire"], "6 points de vie d'appoint")), vr=dict(impact=(10, ["vie", "temporaire"], "10 points de vie d'appoint")))
_VV("feather-fall", dict(qty_cible=None))
_VV("floating-disk", dict(impact_sats=[(25, ["kilogrammes"])]))
_VV("goodberry", dict(impact=(8, ["vie", "nourriture"], "1d6 + 4 en moyenne"), qty_cible=None))
_VV("heroism", dict(impact=(1, ["chance"], "1 ajouté aux attaques, à la vigilance, aux résistances et aux talents"), impact_sats=[]))
_VV("hideous-laughter", dict(impact=(1, ["rire", "lenteur"], "pris de fou rire : ralenti de 1, sans riposte"), cond=["vivant"]))
_VV("jump", dict(impact=(9, ["saut", "mètres"], "un bond de 9 m en tout sens"), impact_add=[]))
_VV("mage-armor", dict(impact=(1, [], "1 ajouté à la garde")))
_VV("protection-from-evil-and-good", dict(impact=(1, ["protection"], "1 ajouté à la garde et aux résistances"), impact_sats=[]))
_VV("sleep", dict(cond=["vivant"], dur=(1, "MINUTES")))
_VV("acid-arrow", vr=dict(impact_sats=[(4, ["acide", "persistance"]), (3, ["traction", "mètres"])]))
_VV("alter-self", dict(options=_OB("alter-self", "Changement d'apparence")))
_VV("barkskin", dict(impact=(2, ["écorce", "résistance"], "2 retranché aux coups contondants et perforants ; le feu la blesse de 3 de plus"), impact_add=[], impact_sats=[(3, ["feu", "faille"])]))
_VV("blindness-deafness", dict(options=_OB("blindness-deafness", "Cécité"), dur=(1, "MINUTES")))
_VV("calm-emotions", dict(cond=[], options=None, impact=(P, ["calme", "hostilité"], "les émotions suspendues, nul geste hostile possible")))
_VV("enlarge-reduce", dict(impact_sats=[(2, ["frappe"]), (1, ["maladresse"])]))
_VV("gust-of-wind", dict(impact_sats=[(9, ["mètres"])]))
_VV("heat-metal", dict(impact_sats=[(P, ["lâcher"]), (5, ["persistance"])]))
_VV("hold-person", dict(cond=[], dur=(6, "SECONDES")))
_VV("knock", dict(impact=(4, ["ouverture"], "4 ajouté à qui tente d'ouvrir")))
_VV("lesser-restoration", vp2=dict(options=_OB("lesser-restoration", "Maladie")),
    vr=dict(options=_OB("lesser-restoration", "Cécité", "Surdité") + [dict(label="Faiblesse", impact=(P, ["faiblesse"], "la faiblesse levée")), dict(label="Nausée", impact=(P, ["nausée"], "la nausée levée"))]))
_VV("levitate", dict(impact=(3, ["mètres", "élévation"], "3 m par geste, vers le haut ou le bas")))
_VV("moonbeam", dict(impact_sats=[], impact_add=["éblouissement"]))
_VV("pass-without-trace", dict(impact=(4, ["sans-trace"], "4 ajouté à la difficulté de me pister"), qty_cible=None))
_VV("protection-from-poison", vr=dict(impact=(1, ["poison", "maladie", "malédiction", "recul"], "le mal recule d'un degré"), impact_add=[]))
_VV("ray-of-enfeeblement", dict(impact=(2, ["faiblesse"], "affaiblie de 2")))
_VV("scorching-ray", dict(options=[dict(label="Forme de base", qty=1), dict(label="Forme maximale", qty=3, impact=(14, ["feu"], "4d6 en moyenne par rayon, trois rayons sur trois cibles ; tout l'instant y passe"))]))
_VV("silence", dict(cible=2, no_aoe=True, impact=(P, ["silence"], "la cible ne fait plus aucun bruit")))
_VV("suggestion", dict(dur=(1, "MINUTES")))
_VV("web", dict(impact_sats=[(3, ["lenteur", "mètres"])]))
_VV("zone-of-truth", vr=dict(impact=(P, ["vérité", "cloche"], "une cloche tinte à chaque parole vraie"), impact_sats=[(2, ["mensonge"])]))
_VV("blink", dict(impact=(5, ["éthéré", "résistance"], "5 retranché à tout coup ; un saut de 3 m au hasard à chaque instant"), impact_sats=[(3, ["saut", "mètres"])]))
_VV("clairvoyance", dict(impact=(P, ["vue"], "voir depuis un point fixe, en tous sens")))
_VV("create-food-and-water", dict(impact=(6, ["nourriture", "ration"], "de quoi nourrir six personnes un jour"), qty=None))
_VV("dispel-magic", dict(impact_sats=[]))
_VV("fear", dict(cible=3, no_aoe=True, impact=(2, ["peur"], "effrayée de 2")))
_VV("fireball", dict(impact_add=[]))
_VV("fly", dict(impact=(6, ["vol", "mètres"], "vole à son allure, 6 m au moins")))
_VV("gaseous-form", dict(impact_sats=[(8, ["résistance"]), (3, ["vol", "mètres"])]))
_VV("glyph-of-warding", vp2=dict(options=_OB("glyph-of-warding", "Glyphe de sort")))
_VV("magic-circle", dict(impact=(1, ["barrière"], "1 ajouté à la garde et aux résistances de ceux du cercle"), impact_add=[]))
_VV("phantom-steed", dict(impact_sats=[(12, ["mètres"])]))
_VV("slow", dict(impact=(1, ["temps", "lenteur"], "ralentie de 1")))
_VV("speak-with-dead", dict(qty=3, impact=(P, ["réponse"], "trois réponses du cadavre")))
_VV("stinking-cloud", dict(impact=(1, ["nausée", "lenteur"], "nausée de 1 et lenteur de 1 dans le nuage")))
_VV("vampiric-touch", dict(impact_sats=[(10, ["vie", "temporaire"])]))
_VV("water-breathing", dict(qty_cible=5))
_VV("water-walk", dict(qty_cible=None))
_VV("banishment", dict(impact=(P, ["exil", "plan"], "renvoyée sur son plan d'origine")))
_VV("black-tentacles", dict(impact_sats=[(P, ["entrave"]), (4, ["persistance"])]))
_VV("confusion", dict(cible=3, no_aoe=True))
_VV("control-water", dict(options=[dict(label="Montée ou baisse des eaux", impact=(3, ["eau", "niveau", "mètres"], "le niveau de l'eau monte ou baisse de 3 m"))]))
_VV("death-ward", dict(impact=(4, ["mort", "résistance"], "4 ajouté contre la mort et l'énergie ténébreuse"), impact_sats=[(10, ["résistance"])], cond=[], fin=[]))
_VV("divination", dict(cible=1, cible_note=[], impact=(P, ["présage", "conseil"], "un indice sibyllin sur ce qui vient dans la semaine")))
_VV("fire-shield", dict(impact_plus=[(5, ["résistance", "froid"], "5 retranché au froid")]))
_VV("ice-storm", dict(impact=(9, ["froid"], "2d8 en moyenne de froid"), impact_plus=[(2, ["froid", "persistance"], "2 à chaque instant passé sous le nuage")]))
_VV("phantasmal-killer", dict(impact_sats=[(2, ["peur"])], impact_add=[]))
_VV("resilient-sphere", dict(impact_sats=[(40, ["réserve"])]))
_VV("secret-chest", vr=dict(impact=(P, ["pensée", "cache"], "le coffre rangé dans mon esprit, où moi seul le vois")))
_VV("stoneskin", dict(impact=(5, [], "5 retranché aux coups")))
_VV("arcane-hand", dict(impact=(P, ["main", "abri"], "une main de force s'interpose et m'abrite"), impact_add=[], impact_sats=[(50, ["réserve"])]))
_VV("cone-of-cold", vr=dict(options=[dict(label="Forme de base"), dict(label="Forme maximale", aoe=_S(30), loc=(150, "METRES", "150 m (500 pieds)"))]))
_VV("dominate-person", dict(cond=[]))
_VV("flame-strike", vp2=dict(impact_sats=[]), vr=dict(impact_sats=[(7, ["persistance"])]))
_VV("greater-restoration", dict(options=[dict(label="État", impact=(2, ["maladresse", "faiblesse", "hébétude", "recul"], "un état réduit de 2, ou deux de 1")), dict(label="Poison", impact=(1, ["poison", "recul"], "le poison recule d'un degré"))]))
_VV("raise-dead", dict(cond_sats=[(3, ["jours"])], impact_sats=[(7, ["jours", "faiblesse"])]))
_VV("scrying", dict(impact=(P, ["vue"], "voir la cible, où qu'elle soit")))
_VV("telekinesis", dict(options=_OB("telekinesis", "Objet"), impact_sats=[(6, ["mètres"])]))
_VV("telepathic-bond", dict(qty_cible=5))
_VV("tree-stride", dict(impact_sats=[(8, ["kilomètres"])]))
_VV("wall-of-force", dict(options=None, impact_sats=[(60, ["réserve"])]))
_VV("blade-barrier", vp2=dict(options=_OB("blade-barrier", "Mur droit")), vr=dict(options=None))
_VV("chain-lightning", dict(qty_cible=P))
_VV("disintegrate", dict(impact=(66, ["poussière"], "12d10 en moyenne")))
_VV("find-the-path", dict(impact=(P, ["chemin", "terrain"], "la route inspirée : le terrain difficile gêne moitié moins"), cond=[]))
_VV("flesh-to-stone", dict(impact=(1, ["pierre", "lenteur"], "ralentie de 1, puis de plus en plus, jusqu'à la pierre")))
_VV("globe-of-invulnerability", dict(impact_sats=[(3, ["seuil", "niveau"])]))
_VV("harm", dict(impact_sats=[], options=[dict(label="Forme de base"), dict(label="Forme maximale", cible=P, aoe=_S(30))]))
_VV("irresistible-dance", dict(dur=(1, "MINUTES")))
_VV("true-seeing", dict(impact_sats=[(18, ["mètres"])]))
_VV("wall-of-ice", dict(impact_sats=[(40, ["réserve"])]))
_VV("wall-of-thorns", dict(options=_OB("wall-of-thorns", "Mur droit"), impact_sats=[(20, ["réserve"])]))
_VV("wind-walk", vp2=dict(qty_cible=6, impact=(32, ["vent", "kilomètres", "heure"], "portés par le vent à 32 km à l'heure")),
    vr=dict(qty_cible=6, impact=(12, ["forme", "bête", "allure", "mètres"], "en bêtes du pays, à 12 m par instant sur terre, sous terre, dans l'air et dans l'eau")))
_VV("divine-word", dict(impact=(39, ["décret", "faiblesse"], "7d10 en moyenne ; affaiblie de 2 une minute"), cond=[]))
_VV("forcecage", dict(impact_sats=[(40, ["réserve"])]))
_VV("teleport", dict(qty_cible=5))
_VV("earthquake", dict(impact_plus=[(38, ["effondrement"], "11d6 en moyenne sous ce qui s'effondre")], impact_sats=[(12, ["fissure", "mètres"])]))
_VV("feeblemind", dict(impact=(4, ["hébétude"], "hébétée de 4, sans terme"), cible_note=["psyché"]))
_VV("glibness", dict(impact=(4, ["persuasion", "mensonge"], "4 ajouté à mes mensonges")))
_VV("holy-aura", dict(impact=(1, [], "1 ajouté à la garde et aux résistances des alliés de l'aura")))
_VV("mind-blank", dict(impact_sats=[(4, ["psyché", "résistance"])]))
_VV("sunburst", dict(impact_sats=[(P, ["aveuglement"]), (44, ["si:mort-vivant"])]))
_VV("meteor-swarm", dict(impact_sats=[(33, ["choc"])]))
_VV("daze", dict(cond=[]))
_VV("touch-of-idiocy", dict(impact=(2, ["hébétude"], "hébétée de 2"), cible_note=["psyché"]))
_VV("crushing-despair", dict(impact=(1, ["désespoir", "lenteur"], "sans riposte, et ralentie de 1 quand les sanglots l'emportent"), cible_note=["psyché"]))
_VV("discern-lies", dict(impact=(4, ["mensonge"], "4 ajouté à ma vigilance contre le mensonge")))
_VV("remove-fear", vp2=dict(impact=(P, ["peur"], "une peur levée")), vr=dict(impact=(P, ["peur", "fuite", "hébétude"], "la peur, la fuite ou l'hébétude levée")))
_VV("resist-energy", dict(options=[dict(o, impact=(5, o["impact"][1], "5 retranché")) for o in FICHES["resist-energy"]["options"]]))
_VV("dimensional-anchor", dict(dur=(10, "MINUTES")))
_VV("spell-turning", dict(impact=(P, ["sort", "renvoi"], "un sort qui me vise, retourné contre son auteur")))
_VV("mages-disjunction", vr=dict(impact_plus=[(28, ["force", "explosion"], "8d6 en moyenne quand la magie se défait")]))
_VV("glitterdust", dict(impact=(P, ["éblouissement", "révélation"], "éblouie une minute, son invisibilité levée")))
_VV("fire-seeds", vp2=dict(qty=4, options=[dict(label="Glands explosifs", impact=(14, ["feu", "jet"], "4d6 en moyenne"), impact_plus=[(7, ["feu", "persistance"], "2d6 en moyenne à qui entre dans les flammes, une minute")])]),
    vr=dict(qty=4, options=[dict(label="Cosses des saisons", impact=(21, ["saison", "jet"], "6d6 en moyenne, de foudre, de feu, de poison ou de froid selon la cosse"))]))
_VV("sound-burst", dict(impact_sats=[(P, ["surdité"])]))
_VV("searing-light", dict(impact=(18, ["lumière"], "5d6 en moyenne"), impact_sats=[(18, ["si:mort-vivant"])]))
_VV("polar-ray", vp2=dict(impact_sats=[(2, ["épuisement"])]), vr=dict(impact_sats=[(P, ["lenteur"])]))
_VV("implosion", dict(impact=(75, ["écrasement"], "75 points, une cible nouvelle à chaque instant soutenu"), qty=None))
_VV("scintillating-pattern", dict(cond=[]))
_VV("nightmare", dict(impact=(P, ["fatigue"], "s'éveille épuisée")))
_VV("shadow-walk", dict(qty_cible=10))
_VV("death-knell", dict(impact_sats=[(10, ["vie", "temporaire"]), (1, ["coup", "frappe"])]))
_VV("spectral-hand", dict(impact_sats=[]))
_VV("wail-of-the-banshee", dict(impact=(44, ["plainte", "âme"], "8d10 en moyenne aux vivants ennemis"), qty_cible=P, impact_sats=[(2, ["épuisement"])]))
_VV("animate-rope", dict(impact_sats=[(3, ["lenteur", "mètres"])]))
_VV("sculpt-sound", dict(qty_cible=None))
_VV("shrink-item", dict(impact=(P, ["taille", "pièce"], "réduit à la taille d'une pièce")))
_VV("rusting-grasp", dict(impact_sats=[(28, ["si:fer"]), (7, ["persistance"])]))
_VV("spike-stones", dict(impact=(3, ["perce"], "3 par pas fait dans la zone")))
_VV("baleful-polymorph", dict(dur=(1, "MINUTES")))
_VV("disrupting-weapon", dict(impact=(2, ["destruction"], "1d4 en moyenne de plus aux morts-vivants")), vp2=dict(qty_cible=2), vr=dict(qty_cible=3))
_VV("righteous-might", dict(impact_sats=[(10, ["vie", "temporaire"]), (3, ["résistance"])]))
_VV("rally-point", dict(impact=(P, ["ralliement", "retour"], "je reviens d'un geste au point marqué, s'il est à moins de 36 m"), impact_add=[], cond=[], cible_note=[]))
_VV("overwhelming-presence", dict(qty_cible=P))
_VV("dream-council", dict(qty_cible=12))
_VV("anticipate-peril", dict(impact=(1, ["danger", "vigilance"], "1 ajouté à sa prochaine entrée en lice")))
_VV("hypercognition", dict(impact_sats=[(6, ["savoir"])]))
_VV("life-bubble", dict(qty_cible=None))
_VV("waterproof", dict(impact_sats=[(10, ["résistance", "acide"])]))
_VV("fungal-infestation", dict(impact=(7, ["champignon", "persistance"], "2d6 en moyenne à chaque instant"), impact_sats=[(1, ["faille"])]))
_VV("life-pact", dict(qty_cible=6, impact_sats=[(3, ["don"])]))
_VV("massacre", dict(impact=(100, ["mort"], "100 points ; la mort pour les plus malchanceux")))
_VV("blistering-invective", dict(cible=3, no_aoe=True, impact=(7, ["parole", "feu", "persistance"], "2d6 en moyenne à chaque instant"), impact_sats=[(1, ["peur"])]))
_VV("etheric-shards", dict(impact=(2, ["éclat", "lenteur"], "1d4 en moyenne par pas fait dans la zone")))
_VV("final-sacrifice", dict(impact=(21, ["invoqué", "explosion"], "6d6 en moyenne à 6 m à la ronde")))
_VV("gentle-breeze", dict(impact=(10, ["vent", "repos", "guérison"], "10 points de vie à qui y reste dix minutes ; 2 ajouté contre les maux")))
_VV("hydraulic-push", dict(impact=(11, ["eau", "recul"], "3d6 en moyenne, repoussée de 1,5 m")))
_VV("hydraulic-torrent", dict(impact=(28, ["eau", "recul"], "8d6 en moyenne, repoussés de 1,5 m")))
_VV("sacred-nimbus", dict(impact_sats=[], options=[dict(label="Forme lumineuse", impact=(18, ["pluie", "lumineux"], "5d6 en moyenne aux êtres de la face ténébreuse et aux morts-vivants sous le nuage")),
                                                     dict(label="Forme ténébreuse", impact=(18, ["pluie", "ténébreux"], "5d6 en moyenne aux êtres de la face lumineuse sous le nuage"))]))
_VV("breath-of-life", vp2=dict(impact=(18, ["vie", "retour"], "4d8 en moyenne")), vr=dict(impact=(23, ["vie", "retour"], "5d8 en moyenne")))
_VV("cave-fangs", dict(impact=(21, ["roche", "croc"], "6d6 en moyenne")))
_VV("geyser", dict(impact=(25, ["eau", "brûlure"], "3d6 + 4d6 en moyenne ; projetée en l'air"), impact_sats=[(6, ["mètres", "élévation"])]))
_VV("summon-stampede", dict(impact=(36, ["piétinement"], "8d8 en moyenne à son départ"), impact_plus=[(P, ["peur"], "à son arrivée, la terreur")]))
_VV("tidal-surge", dict(cible=3, no_aoe=True, impact=(2, ["eau", "vague", "déplacement", "mètres"], "déplacée de 1,5 m sur terre, 3 m dans l'eau")))
_VV("vomit-swarm", dict(impact=(9, ["nuée", "morsure"], "2d8 en moyenne"), impact_sats=[(1, ["nausée"])]))
_VV("cup-of-dust", dict(impact=(2, ["soif", "fatigue"], "épuisée ; 1d4 en moyenne par heure")))
_VV("feast-of-ashes", dict(impact=(2, ["faim", "fatigue"], "épuisée ; 1d4 en moyenne par jour")))
_VV("divine-vessel", dict(impact_sats=[(40, ["vie", "temporaire"])]))
_VV("fiery-body", dict(impact_plus=[(11, ["riposte"], "3d6 en moyenne à qui me touche")], impact_sats=[(12, ["vol", "mètres"])]))
_VV("forced-quiet", dict(dur=(1, "MINUTES")))
_VV("frostbite", dict(impact=(5, ["froid"], "2d4 en moyenne")))
_VV("gravity-well", dict(impact_sats=[(5, ["traction", "mètres"])]))
_VV("penumbral-disguise", dict(impact=(1, ["déguisement", "discrétion", "pénombre"], "1 ajouté pour se cacher dans la pénombre")))

# ----- Pathfinder 2 : reliquat de la comparaison (24 novembre) -----
PF2_RELIQUAT = {
"invisibility-sphere": P2("Sphère d'invisibilité", NVIS, 2, ["invisibilité", "groupe"], why="moi et tous ceux du cercle, invisibles sauf les uns aux autres, tant qu'ils y restent", qty_cible=P, fin=["attaque", "sortie"]),
"endure": P2("Tenir bon", INT, 2, ["vie", "temporaire"], 5, "5 points de vie d'appoint, un instant", loc=(2, "METRES", "contact")),
"aerial-form": P2("Forme aérienne", TR, 1, ["forme", "envol"], 14, "", impact_sats=[(5, ["vie", "temporaire"]), (15, ["vol", "mètres"])], vr={},
    options=[O("Chauve-souris", impact=(14, ["forme", "envol", "croc", "écho"], "crocs : 2d8 + 5 en moyenne ; se dirige à l'écho, vole à 9 m"), impact_sats=[(5, ["vie", "temporaire"]), (9, ["vol", "mètres"])]),
             O("Oiseau", impact=(14, ["forme", "envol", "bec"], "bec : 2d8 + 5 en moyenne ; vole à 15 m")),
             O("Guêpe", impact=(10, ["forme", "envol", "dard"], "dard : 1d8 + 5 en moyenne, et 1d6 à chaque instant ensuite ; vole à 12 m"), impact_sats=[(5, ["vie", "temporaire"]), (12, ["vol", "mètres"]), (4, ["persistance"])])]),
"pest-form": P2("Forme de bestiole", TR, 1, ["forme", "minuscule", "discrétion"], why="une bête minuscule, chat, lézard, rat ou insecte : furtive, agile, incapable de frapper", impact_sats=[(6, ["allure", "mètres"]), (5, ["faille"])], vr={}),
}
FICHES.update(PF2_RELIQUAT)
FICHES["seeming"]["vp2"] = dict(src_idx="veil", qty_cible=10)
_pw = _OB("prismatic-wall", "Mur", "Sphère"); _pw[1]["src_idx"] = "prismatic-sphere"; _pw[1]["aoe"] = _S(10)
FICHES["prismatic-wall"]["vp2"] = dict(options=_pw)
for _k in ("vp2", "vr"):
    _v = FICHES["summon-monster-i"][_k]; _o = dict(_v["options"][0])
    _o.update(label=_o["label"].replace("lumineux", "ténébreux"), cible_sym=["tenebreux"], src_idx="summon-fiend")
    FICHES["summon-monster-i"][_k] = dict(_v, options=list(_v["options"]) + [_o])
_VV("clairvoyance", dict(options=[dict(label="Clairvoyance"), dict(label="Clairaudience", src_idx="clairaudience", impact=(P, ["ouïe"], "entendre depuis un point fixe"))]))
FICHES["wish"]["vp2"] = dict(FICHES["wish"]["vp2"], options=[dict(label="Souhait"), dict(label="Réalité altérée", src_idx="alter-reality"), dict(label="Phénomène primordial", src_idx="primal-phenomenon")])
_VV("invisibility", dict(options=[dict(label="Invisibilité"), dict(label="Objet invisible", src_idx="invisible-item", cible=1, cible_obj=["objet"])]))
_VV("blindness-deafness", dict(options=_OB("blindness-deafness", "Cécité") + [dict(_OB("blindness-deafness", "Surdité")[0], src_idx="deafness", dur=(10, "MINUTES"))]))
_VV("lesser-restoration", vp2=dict(options=_OB("lesser-restoration", "Maladie") + [dict(o, src_idx="restore-senses") for o in _OB("lesser-restoration", "Cécité", "Surdité")] + [dict(_OB("lesser-restoration", "Paralysie")[0], src_idx="remove-paralysis")]),
    vr=dict(options=FICHES["lesser-restoration"]["vr"]["options"] + [dict(label="Entrave", src_idx="sure-footing", impact=(P, ["maladresse", "étreinte", "paralysie"], "la maladresse, l'étreinte ou la paralysie levée"))]))
_VV("enlarge-reduce", dict(options=[dict(label="Agrandissement"), dict(label="Rapetissement", src_idx="shrink", impact=(P, ["stature", "minuscule"], "réduite à une taille minuscule, sans allonge"), impact_sats=[])]))
# relecture inversée des focalisés : deux retouches
_R("stone-lance", impact=(21, ["lance", "empalement"], "6d6 en moyenne ; empalée, elle perd 3 m par instant"))
FICHES["blind-ambition"]["vr"] = dict(FICHES["blind-ambition"]["vr"], dur=(10, "MINUTES"))
