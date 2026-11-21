"""Mots de jeu remplacés par des mots de l'univers (décisions de Baptiste, 15 novembre 2026).
Une annotation doit se lire du point de vue d'un arcaniste d'Inarama : aucun terme de règles.
Restent tels quels, par décision : « ki », « demi-plan ».
« temporaire », « persistance » et « par tour » ne sont plus des mots : ce sont des satellites (convert.emprunt_et_rythme)."""
# mot -> mots qui le remplacent, partout
# (lexique, 21 novembre 2026 : un nom d'école n'est plus renommé — INVOCATION, NECROMANCIE, TRANSMUTATION restent)
RENOMME = {
 "RETARD": ["délai"],            # une attente
 "ESSAI": ["chance"],            # « le meilleur de deux essais »
 "HUMANOIDE": ["peuple"],        # un être des peuples
 "ABERRATION": ["monstre"],
 "ETHERE": ["immatériel"],       # le plan éthéré n'existe pas dans Inarama
 "MAXIMUM": ["espérance"],       # « vie · maximum » : l'espérance de vie
}
# Doublons d'écriture : un seul mot par chose (le singulier ; le pluriel pour les unités de temps)
RENOMME.update({
 "AILES": ["aile"],
 "ALLIES": ["allie"],
 "AN": ["ans"],
 "AVEUX": ["aveu"],
 "BAIES": ["baie"],
 "BIENFAITS": ["bienfait"],
 "BRAISES": ["braise"],
 "CADAVRES": ["cadavre"],
 "CHAINES": ["chaine"],
 "CHAMPIGNONS": ["champignon"],
 "CHEVEUX": ["cheveu"],
 "CICATRICES": ["cicatrice"],
 "CLOQUES": ["cloque"],
 "COMETES": ["comete"],
 "CORBEAUX": ["corbeau"],
 "CORNES": ["corne"],
 "COULEURS": ["couleur"],
 "COUPS": ["coup"],
 "CROCS": ["croc"],
 "DOUBLES": ["double"],
 "DRAGONS": ["dragon"],
 "ECAILLES": ["ecaille"],
 "ECHARPES": ["echarpe"],
 "ECLAIRS": ["éclair"],
 "ECLATS": ["eclat"],
 "ENGRENAGES": ["engrenage"],
 "EPINES": ["epine"],
 "ESPRITS": ["esprit"],
 "ETINCELLES": ["etincelle"],
 "ETOILES": ["etoile"],
 "FILS": ["fil"],
 "FLAMMES": ["flamme"],
 "FLECHES": ["fleche"],
 "FLEURS": ["fleur"],
 "FOYERS": ["foyer"],
 "GRIFFES": ["griffe"],
 "HERBES": ["herbe"],
 "HEURE": ["heures"],
 "HURLEMENTS": ["hurlement"],
 "INSECTES": ["insecte"],
 "INSTANT": ["instants"],
 "JETS": ["jet"],
 "LAMES": ["lame"],
 "LETTRES": ["lettre"],
 "LEVRES": ["levre"],
 "LIANES": ["liane"],
 "LUEURS": ["lueur"],
 "LUMIERES": ["lumière"],
 "MASQUES": ["masque"],
 "MAUX": ["mal"],
 "MEMBRES": ["membre"],
 "MENOTTES": ["menotte"],
 "METEORES": ["meteore"],
 "MINUTE": ["minutes"],
 "MIROIRS": ["miroir"],
 "MOTIFS": ["motif"],
 "MOTS": ["mot"],
 "NOTES": ["note"],
 "OEIL": ["œil"],
 "ONDES": ["onde"],
 "OUTILS": ["outil"],
 "PARCHEMINS": ["parchemin"],
 "PETALES": ["petale"],
 "PHALENES": ["phalene"],
 "PILIERS": ["pilier"],
 "PLUMES": ["plume"],
 "POINTES": ["pointe"],
 "PORTES": ["porte"],
 "RACINES": ["racine"],
 "RAYONS": ["rayon"],
 "REPLIQUES": ["replique"],
 "RUNES": ["rune"],
 "SILHOUETTES": ["silhouette"],
 "SOINS": ["soin"],
 "SOMBRES": ["sombre"],
 "SPECTRES": ["spectre"],
 "SQUELETTES": ["squelette"],
 "TENTACULES": ["tentacule"],
 "TRAINEES": ["trainee"],
 "TRAITS": ["trait"],
 "USAGES": ["usage"],
 "VAPEURS": ["vapeur"],
 "VENTS": ["vent"],
 "VISAGES": ["visage"],
 "VRILLES": ["vrille"],
 "YEUX": ["œil"],
})
# Fusions par famille (grain validé par Baptiste le 15 novembre 2026 sur la famille des sentiments) : un mot employé sur une
# seule page se fond dans le mot de même sens déjà en usage ; un mot employé sur deux pages ou plus est gardé.
FUSIONS = {
 "ABOIEMENT": ["cri"], "ABSURDE": ["confusion"], "ACCES": ["passage"], "ACCOMPLISSEMENT": ["gloire"], "ACCOUTUMANCE": ["adaptation"],
 "ACCROC": ["entrave"], "ACCUSATION": ["condamnation"], "ACRETE": ["odeur"], "ADMIRATION": ["fascination"], "ADORATION": ["amour"],
 "AFFECTION": ["amitié"], "AFFINAGE": ["précision"], "AFFIRMATION": ["vérité"], "AFFUT": ["tranchant"], "AGATE": ["gemme"], "AGILITE": ["adresse"],
 "AGITATION": ["trouble"], "AGRUME": ["fruit"], "AJUSTEMENT": ["précision"], "ALBATROS": ["oiseau"], "ALIBI": ["leurre"], "ALLEGEMENT": ["aisance"],
 "ALLERRETOUR": ["retour"], "AMALGAME": ["fusion"], "AMBITION": ["désir"], "AMELIORATION": ["surcroît"], "AMER": ["goût"], "AMPUTATION": ["blessure"],
 "ANCRE": ["ancrage"], "ANEANTISSEMENT": ["destruction"], "ANGE": ["astral"], "ANGLES": ["direction"], "ANNEES": ["ans"], "ANNULATION": ["dissipation"],
 "ANOMALIE": ["trouble"], "APATHIE": ["torpeur"], "APESANTEUR": ["lévitation"], "APPRENTISSAGE": ["savoir"], "APPROBATION": ["accord"],
 "ARCENCIEL": ["couleur"], "ARDEUR": ["élan"], "ARGILE": ["boue"], "ARIDITE": ["dessèchement"], "ARMEE": ["foule"], "ARRIVEE": ["passage"],
 "ART": ["ouvrage"], "ARTICULATION": ["membre"], "ARTISTE": ["ouvrage"], "ASCENDANT": ["domination"], "ASSEMBLAGE": ["création"], "ASSEMBLEE": ["foule"],
 "ASSURANCE": ["confiance"], "ASTRE": ["étoile"], "ATOUT": ["chance"], "ATROPHIE": ["faiblesse"], "ATTACHE": ["lien"], "ATTACHEMENT": ["amitié"],
 "ATTENTE": ["délai"], "ATTENTION": ["vigilance"], "AUBE": ["jour"], "AUROCHS": ["bête"], "AUTHENTICITE": ["vérité"], "AVALEMENT": ["dévoration"],
 "AVERSION": ["répulsion"], "BABIOLE": ["objet"], "BAGUETTE": ["bâton"], "BAIN": ["eau"], "BALLADE": ["chant"], "BANNISSEMENT": ["renvoi"],
 "BARBE": ["poil"], "BASSIN": ["source"], "BATIMENT": ["édifice"], "BATRACIEN": ["bête"], "BAVARDAGE": ["voix"], "BAVE": ["crachat"],
 "BAVURE": ["trace"], "BEAUTE": ["fascination"], "BEC": ["croc"], "BELLADONE": ["herbe"], "BESTIALITE": ["fureur"], "BESTIOLE": ["vermine"],
 "BIJOU": ["trésor"], "BLAME": ["condamnation"], "BLASON": ["symbole"], "BLASPHEME": ["offense"], "BLIZZARD": ["neige"], "BLOC": ["pierre"],
 "BLOCAGE": ["arrêt"], "BOIRE": ["nourriture"], "BOISSON": ["nourriture"], "BOTTE": ["vêtement"], "BOUCLE": ["lien"], "BOURDON": ["son"],
 "BOURG": ["lieu"], "BOURSE": ["contenant"], "BRACELET": ["trésor"], "BREUVAGE": ["nourriture"], "BRIN": ["chance"], "BRIS": ["destruction"],
 "BROCHE": ["trésor"], "BRODERIE": ["ouvrage"], "BROUILLAGE": ["dissimulation"], "BROUSSAILLES": ["plante"], "BROYAGE": ["écrasement"],
 "BRUINE": ["pluie"], "BRUISSEMENT": ["son"], "BUTTE": ["terrain"], "CABLE": ["corde"], "CACHETTE": ["cache"], "CACOPHONIE": ["vacarme"],
 "CALCAIRE": ["pierre"], "CAMP": ["abri"], "CAPTIVATION": ["fascination"], "CAPTURE": ["saisie"], "CARILLON": ["cloche"], "CARQUOIS": ["contenant"],
 "CATALEPSIE": ["paralysie"], "CATAPULTE": ["projection"], "CAUTERE": ["soin"], "CAVEAU": ["tombe"], "CECITE": ["aveuglement"], "CERCUEIL": ["tombe"],
 "CERTITUDE": ["confiance"], "CERVEAU": ["tête"], "CHAPELET": ["talisman"], "CHAUFFE": ["chaleur"], "CHAUMIERE": ["demeure"], "CHAUVESOURIS": ["bête"],
 "CHENE": ["arbre"], "CICATRICE": ["marque"], "CLAIRVOYANCE": ["vision"], "CLEF": ["ouverture"], "CLEMENCE": ["pitié"], "CLIQUETIS": ["son"],
 "CLOCHETTE": ["cloche"], "CLONE": ["double"], "CLOU": ["pointe"], "COCHER": ["serviteur"], "COCON": ["abri"], "CODE": ["secret"], "COFFRE": ["contenant"],
 "COLLIER": ["trésor"], "COMBUSTION": ["embrasement"], "COMMUNION": ["lien"], "COMPAS": ["direction"], "COMPASSION": ["pitié"], "COMPLAINTE": ["plainte"],
 "COMPLOT": ["trahison"], "CONDUCTEUR": ["lien"], "CONFLUENCE": ["fusion"], "CONSECRATION": ["sanctuaire"], "CONSONANCE": ["musique"],
 "CONSTELLATION": ["étoile"], "CONSTRUCTION": ["édifice"], "CONTOURNEMENT": ["esquive"], "CONTRASTE": ["couleur"], "CONTRE": ["riposte"],
 "CONVICTION": ["confiance"], "CONVOITISE": ["désir"], "CONVOQUE": ["invoqué"], "CONVULSION": ["secousse"], "COQUE": ["coquilles"],
 "COQUILLAGE": ["coquilles"], "CORDON": ["corde"], "CORROSION": ["rongement"], "COSMOS": ["ciel"], "COSSE": ["graine"], "COTE": ["direction"],
 "COUCHE": ["rempart"], "COULEE": ["lave"], "COULOIR": ["passage"], "COUPE": ["taille"], "COUPURE": ["taille"], "COURBE": ["détournement"],
 "COURROUX": ["fureur"], "COUSSIN": ["rempart"], "COUTEAU": ["lame"], "COUTUME": ["savoir"], "CRAINTE": ["peur"], "CRAPAUD": ["bête"],
 "CREATEUR": ["création"], "CREVASSE": ["fissure"], "CRIQUETS": ["insecte"], "CROCHET": ["saisie"], "CROISSANT": ["symbole"], "CROUPISSEMENT": ["pourriture"],
 "CROYANCE": ["foi"], "CUMUL": ["surcroît"], "DALLE": ["pierre"], "DATE": ["temps"], "DEBRIS": ["ruine"], "DECAPITATION": ["mort"],
 "DECOMBRES": ["ruine"], "DECOMPOSITION": ["pourriture"], "DECRET": ["ordre"], "DEDALE": ["labyrinthe"], "DEFIANCE": ["doute"], "DEGAGEMENT": ["liberté"],
 "DEGOUT": ["répulsion"], "DEGRE": ["précision"], "DELABREMENT": ["ruine"], "DELECTATION": ["extase"], "DELUGE": ["pluie"], "DEMANDE": ["question"],
 "DEMANGEAISON": ["gêne"], "DEMONTAGE": ["façonnage"], "DEMORALISATION": ["désespoir"], "DENIGREMENT": ["mépris"], "DEPERDITION": ["perte"],
 "DERIVE": ["égarement"], "DESCENTE": ["chute"], "DESHYDRATATION": ["dessèchement"], "DESORIENTATION": ["égarement"], "DESTINATION": ["direction"],
 "DETACHEMENT": ["apaisement"], "DETENTE": ["repos"], "DETONATION": ["fracas"], "DEUIL": ["chagrin"], "DEVOUEMENT": ["zèle"], "DIAGRAMME": ["symbole"],
 "DISJONCTION": ["dissipation"], "DISPERSION": ["dissipation"], "DISTORSION": ["déviation"], "DIVIN": ["divinité"], "DOIGTS": ["main"],
 "DOMAINE": ["lieu"], "DOMESTIQUE": ["serviteur"], "DORE": ["or"], "DOREE": ["or"], "DORMANCE": ["sommeil"], "DORMEUR": ["sommeil"],
 "DORURE": ["or"], "DOUBLEMENT": ["double"], "DROGUE": ["poison"], "DURETE": ["solidité"], "EBULLITION": ["chaleur"], "ECHARDE": ["épine"],
 "ECHARPE": ["vêtement"], "ECLAIREUR": ["guide"], "ECORCE": ["peau"], "ECORCHEMENT": ["blessure"], "ECRAN": ["voile"], "ECRITURE": ["écrit"],
 "ECTOPLASME": ["spectre"], "ECUYER": ["serviteur"], "EDIT": ["ordre"], "EFFET": ["pouvoir"], "EGOISME": ["orgueil"], "ELAGAGE": ["taille"],
 "ELEGIE": ["chant"], "ELOCUTION": ["voix"], "ELOGE": ["gloire"], "ELOQUENCE": ["voix"], "EMPECHEMENT": ["entrave"], "EMPLATRE": ["soin"],
 "EMPOISONNEMENT": ["poison"], "EMULATION": ["élan"], "ENCOMBREMENT": ["gêne"], "ENCOURAGEMENT": ["courage"], "ENDUIT": ["huile"], "ENGLOUTISSEMENT": ["dévoration"],
 "ENGOURDISSEMENT": ["torpeur"], "ENGRENAGE": ["mécanisme"], "ENNUI": ["torpeur"], "ENQUETE": ["fouille"], "ENROUEMENT": ["gêne"], "ENTONNOIR": ["aspiration"],
 "ENTRAIN": ["élan"], "ENVIE": ["désir"], "ENVOI": ["transfert"], "EPAISSEUR": ["solidité"], "EPARGNE": ["sursis"], "EPAVE": ["ruine"],
 "ERRANCE": ["égarement"], "ERREUR": ["échec"], "ESCORTE": ["gardien"], "ESTIMATION": ["savoir"], "ESTOMAC": ["dévoration"], "ETANCHE": ["protection"],
 "ETAU": ["étreinte"], "ETENDARD": ["symbole"], "ETERNUEMENT": ["gêne"], "ETOFFE": ["vêtement"], "ETRANGER": ["intrus"], "ETRANGETE": ["trouble"],
 "EVASION": ["fuite"], "EVITEMENT": ["esquive"], "EXALTATION": ["extase"], "EXCEDENT": ["surcroît"], "EXCEPTION": ["choix"], "EXIGENCE": ["ordre"],
 "EXPANSION": ["croissance"], "EXPLORATION": ["fouille"], "EXTRADIMENSION": ["demi-plan"], "FABRICATION": ["création"], "FACULTE": ["aptitude"],
 "FAISCEAUX": ["lumière"], "FAMILIER": ["compagnon"], "FANGE": ["boue"], "FANTOME": ["spectre"], "FARCE": ["rire"], "FATALITE": ["destin"],
 "FAUSSEAURA": ["faux-semblant"], "FEINTE": ["leurre"], "FERMETURE": ["verrou"], "FERVEUR": ["zèle"], "FEUILLES": ["plante"], "FIBRE": ["fil"],
 "FICELLE": ["corde"], "FIN": ["arrêt"], "FINAL": ["arrêt"], "FIOLE": ["contenant"], "FLAMBEE": ["embrasement"], "FLAMMECHE": ["étincelle"],
 "FLEAU": ["châtiment"], "FLETRISSEMENT": ["flétrissure"], "FLEUVE": ["eau"], "FLOTTANT": ["lévitation"], "FLOTTEMENT": ["lévitation"],
 "FLUIDE": ["souplesse"], "FONTAINE": ["source"], "FORAGE": ["trou"], "FORMATION": ["création"], "FORMEVRAIE": ["vérité"], "FORT": ["édifice"],
 "FORTUNE": ["chance"], "FOSSE": ["trou"], "FOUISSEUR": ["trou"], "FOURMI": ["insecte"], "FOURREAU": ["contenant"], "FOURRURE": ["poil"],
 "FRACTURE": ["fêlure"], "FRAICHEUR": ["froid"], "FREMISSEMENT": ["vibration"], "FRISSON": ["secousse"], "FRONT": ["tête"], "FUSEE": ["signal"],
 "FUTUR": ["avenir"], "GAINE": ["contenant"], "GANGUE": ["pierre"], "GAUCHISSEMENT": ["difformité"], "GEL": ["givre"], "GEODE": ["gemme"],
 "GEOMETRIE": ["motif"], "GIGANTISME": ["stature"], "GLANAGE": ["nourriture"], "GLAS": ["mort"], "GLISSANT": ["glissade"], "GLISSE": ["glissade"],
 "GLISSEMENT": ["glissade"], "GOUFFRE": ["trou"], "GOUTTE": ["eau"], "GRAISSE": ["huile"], "GRAPPIN": ["saisie"], "GRAVATS": ["ruine"],
 "GRAVIER": ["pierre"], "GRENOUILLE": ["bête"], "GRESILLEMENT": ["son"], "GRIEF": ["offense"], "GROUPE": ["foule"], "GUERRE": ["combat"],
 "GUET": ["veille"], "GUIDANCE": ["guide"], "HABITANT": ["peuple"], "HALEINE": ["souffle"], "HALTE": ["arrêt"], "HARCELEMENT": ["poursuite"],
 "HARDE": ["meute"], "HARMONIE": ["musique"], "HERAUT": ["serviteur"], "HEROS": ["gloire"], "HONTE": ["remords"], "ICONE": ["symbole"],
 "IDEE": ["pensée"], "IMITATION": ["copie"], "IMMEDIAT": ["vitesse"], "IMMORTALITE": ["permanence"], "IMPACT": ["choc"], "IMPENETRABLE": ["barrière"],
 "IMPREGNATION": ["marque"], "IMPRESSION": ["empreinte"], "INCONSCIENT": ["torpeur"], "INDETECTABLE": ["dissimulation"], "INERTE": ["immobilité"],
 "INFAILLIBLE": ["précision"], "INFIRMITE": ["difformité"], "INNE": ["nature"], "INOFFENSIF": ["paix"], "INONDATION": ["vague"], "INSIGNE": ["symbole"],
 "INTERCESSION": ["faveur"], "INTERRUPTION": ["arrêt"], "INTERVALLE": ["distance"], "INTUITION": ["présage"], 
 "INVULNERABILITE": ["immunité"], "INVULNERABLE": ["immunité"], "IRIS": ["œil"], "ISOLANT": ["protection"], "ISSUE": ["passage"], "JACINTHE": ["gemme"],
 "JALOUSIE": ["haine"], "JAMBE": ["membre"], "JET": ["lancer"], "JEU": ["hasard"], "JOUET": ["objet"], "JOUTE": ["duel"], "JOYAU": ["gemme"],
 "JUGEMENT": ["condamnation"], "KILOGRAMMES": ["kilo"], "LABORATOIRE": ["outil"], "LACHETE": ["peur"], "LAIDEUR": ["difformité"], "LAMBEAUX": ["déchirure"],
 "LANGUEUR": ["torpeur"], "LATENCE": ["délai"], "LEGERETE": ["aisance"], "LEGION": ["foule"], "LEPRE": ["maladie"], "LETTRE": ["écrit"],
 "LIBELLULES": ["insecte"], "LIBERATION": ["délivrance"], "LIGNEE": ["parenté"], "LIMITE": ["seuil"], "LOI": ["ordre"], "LOTUS": ["fleur"],
 "LOURDEUR": ["poids"], "LUNE": ["lueur"], "MACHINE": ["mécanisme"], "MACHOIRE": ["gueule"], "MAGMA": ["lave"], "MAILLET": ["marteau"],
 "MALAISE": ["gêne"], "MALEFICE": ["malédiction"], "MANDRAGORE": ["herbe"], "MANOIR": ["demeure"], "MANQUEMENT": ["offense"], "MAQUETTE": ["image"],
 "MARIN": ["équipage"], "MEDAILLE": ["talisman"], "MEDITATION": ["calme"], "MEFIANCE": ["doute"], "METIER": ["savoir-faire"], "MIASME": ["gaz"],
 "MIME": ["leurre"], "MIMETISME": ["dissimulation"], "MIMIQUE": ["monstre"], "MINERAI": ["minéral"], "MINEUR": ["petit"], "MINIATURE": ["petit"],
 "MINUIT": ["nuit"], "MIRAGE": ["illusion"], "MISERICORDE": ["pitié"], "MOBILE": ["mouvement"], "MOITIE": ["partage"], "MONNAIE": ["pièce"],
 "MONOCLE": ["lentille"], "MOQUERIE": ["mépris"], "MOTDEPASSE": ["secret"], "MOYEN": ["stature"], "MULTIPLE": ["répétition"], "MULTIPLICATION": ["répétition"],
 "MULTIVERS": ["plan"], "MUSC": ["odeur"], "MUSICIENS": ["musique"], "MUTISME": ["silence"], "NAGEOIRE": ["nage"], "NARCISSISME": ["orgueil"],
 "NATURELLE": ["nature"], "NAVIGATION": ["voyage"], "NEANT": ["vide"], "NENUPHAR": ["fleur"], "NERVOSITE": ["trouble"],
 "NETTETE": ["précision"], "NEUTRALISATION": ["dissipation"], "NIMBE": ["halo"], "NOBLESSE": ["prestance"], "NON": ["réponse"], "NORD": ["direction"],
 "OBSERVATION": ["vigilance"], "OBSTACLE": ["entrave"], "OCCASION": ["chance"], "ONGLE": ["griffe"], "ONGUENT": ["huile"], "OPACITE": ["obscurité"],
 "ORBE": ["cristal"], "ORCHESTRE": ["musique"], "OREILLE": ["tête"], "ORIENTATION": ["direction"], "ORTIE": ["herbe"], "OSSEMENTS": ["os"],
 "OTAGE": ["saisie"], "OUI": ["réponse"], "OURAGAN": ["orage"], "OUTREPLAN": ["plan"], "OVATION": ["gloire"], "PACTE": ["contrat"],
 "PAGE": ["écrit"], "PALE": ["lueur"], "PALEUR": ["lueur"], "PALMURE": ["nage"], "PANACHE": ["flamme"], "PANSEMENT": ["soin"], "PAPILLONS": ["insecte"],
 "PARASITE": ["vermine"], "PARESSE": ["torpeur"], "PARI": ["gage"], "PART": ["partage"], "PARTICULE": ["poussière"], "PARTIE": ["partage"],
 "PATTES": ["marche"], "PAUME": ["main"], "PAVILLON": ["demeure"], "PAVOT": ["herbe"], "PERCEE": ["perce"], "PERFORATION": ["perce"],
 "PERROQUET": ["oiseau"], "PERSUASION": ["charme"], "PESSIMISME": ["désespoir"], "PESTE": ["maladie"], "PHALENE": ["insecte"], "PHENIX": ["oiseau"],
 "PHOBIE": ["peur"], "PIC": ["pointe"], "PIED": ["marche"], "PIGNE": ["graine"], "PILE": ["répétition"], "PIOCHE": ["outil"], "PION": ["serviteur"],
 "PITRERIE": ["rire"], "PLACAGE": ["entrave"], "PLACE": ["lieu"], "PLAISANTERIE": ["rire"], "PLANER": ["vol"], "PLAT": ["nourriture"],
 "PLOMB": ["métal"], "PLONGEON": ["nage"], "POLLEN": ["spore"], "PONCE": ["pierre"], "POSE": ["attitude"], "POTERIE": ["ouvrage"], "POUSSE": ["croissance"],
 "PRE": ["terrain"], "PREDATEUR": ["bête"], "PREHENSION": ["saisie"], "PRESENT": ["don"], "PREVISION": ["présage"], "PRIERE": ["foi"],
 "PRIVATION": ["faim"], "PROLONGATION": ["durée"], "PROPHETIE": ["présage"], "PROSTRATION": ["torpeur"], "PUBLIC": ["foule"], "PUITS": ["trou"],
 "PULSION": ["désir"], "PUSTULE": ["maladie"], "PYRITE": ["minéral"], "RABOUGRISSEMENT": ["flétrissure"], "RACE": ["espèce"], "RADEAU": ["navire"],
 "RAGE": ["fureur"], "RALLIEMENT": ["courage"], "RAMOLLISSEMENT": ["souplesse"], "RANCUNE": ["haine"], "RANCŒUR": ["haine"], "RANG": ["ordre"],
 "RANGEES": ["ordre"], "RANGEMENT": ["ordre"], "RAPETISSEMENT": ["petit"], "RASOIR": ["lame"], "RAT": ["vermine"], "RATION": ["nourriture"],
 "RAYONNEMENT": ["lumière"], "RECEPTACLE": ["contenant"], "RECHERCHE": ["fouille"], "RECOLTE": ["nourriture"], "RECOMPENSE": ["don"],
 "RECONFORT": ["apaisement"], "RECREATION": ["création"], "REDUCTION": ["petit"], "REEL": ["vérité"], "REFUGE": ["abri"], "REFUS": ["rejet"],
 "REGION": ["lieu"], "REGLAGE": ["précision"], "REGRET": ["remords"], "REGURGITATION": ["crachat"], "RELEVE": ["retour"], "RELIQUAIRE": ["talisman"],
 "RELIQUE": ["talisman"], "REMONTEE": ["élévation"], "REMPLACEMENT": ["échange"], "RENCONTRE": ["présence"], "RENOUVEAU": ["renaissance"],
 "REPERE": ["balise"], "REPLACEMENT": ["déplacement"], "REPLI": ["fuite"], "REPOUSSE": ["régénération"], "REPRESAILLES": ["vengeance"],
 "REPRISE": ["répétition"], "REQUIN": ["bête"], "RESEAU": ["lien"], "RESSEMBLANCE": ["apparence"], "RESURRECTION": ["renaissance"],
 "REVANCHE": ["vengeance"], "REVOCATION": ["renvoi"], "RICANEMENT": ["rire"], "RICOCHET": ["rebond"], "RIVIERE": ["eau"], "RIZ": ["nourriture"],
 "ROCHER": ["roche"], "ROSE": ["fleur"], "ROUE": ["mouvement"], "ROUGEOIEMENT": ["lueur"], "ROUGEUR": ["rouge"], "ROULADE": ["esquive"],
 "ROULEMENT": ["mouvement"], "ROUTE": ["chemin"], "RUCHE": ["insecte"], "RUPTURE": ["déchirure"], "RUSE": ["leurre"], "RYTHME": ["musique"],
 "SABLIER": ["temps"], "SACRE": ["sanctuaire"], "SALVE": ["répétition"], "SATIETE": ["nourriture"], "SAUVAGERIE": ["fureur"], 
 "SAVEUR": ["goût"], "SCARABEES": ["insecte"], "SCELLEMENT": ["sceau"], "SCEPTRE": ["bâton"], "SCORBUT": ["maladie"], "SCORPION": ["insecte"],
 "SCRUPULE": ["doute"], "SCULPTURE": ["statue"], "SECHAGE": ["dessèchement"], "SECHERESSE": ["dessèchement"], "SECONDAIRE": ["rebond"],
 "SEDUCTION": ["charme"], "SELLE": ["monture"], "SERENITE": ["paix"], "SERRES": ["griffe"], "SESAME": ["ouverture"], "SIENNE": ["couleur"],
 "SIFFLEMENT": ["son"], "SIGLES": ["symbole"], "SIMULACRE": ["double"], "SINGE": ["bête"], "SOLITUDE": ["isolement"], "SORTIE": ["passage"],
 "SOSIE": ["double"], "SOUMISSION": ["obéissance"], "SOUPCON": ["doute"], "SOUPE": ["nourriture"], "SOUSBOIS": ["terrain"], "SPASME": ["secousse"],
 "SPECTATEUR": ["foule"], "SPECTRAL": ["spectre"], "STABILITE": ["équilibre"], "STAGNATION": ["immobilité"], "STOCKAGE": ["contenant"],
 "STRUCTURE": ["édifice"], "SUAIRE": ["voile"], "SUBSTANCE": ["matière"], "SUCCION": ["drain"], "SUCRE": ["nourriture"], "SUIVI": ["piste"],
 "SUIVRE": ["poursuite"], "SUPERIEUR": ["grand"], "SYLVANIEN": ["nature"], "SYMPHONIE": ["musique"], "TALENT": ["savoir-faire"], "TAMBOURS": ["musique"],
 "TAUREAU": ["bête"], "TEINT": ["couleur"], "TERRASSEMENT": ["trou"], "TERRESTRE": ["terre"], "TERTRE": ["terrain"], "TEXTE": ["écrit"],
 "THE": ["nourriture"], "THRENE": ["chant"], "TIGE": ["plante"], "TIR": ["lancer"], "TOURMENT": ["douleur"], "TOUS": ["toutes"], "TOXIQUE": ["poison"],
 "TRAC": ["peur"], "TRAITRISE": ["trahison"], "TRAJECTOIRE": ["direction"], "TRANCHEE": ["trou"], "TRANSFORMATION": ["métamorphose"],
 "TRANSGRESSION": ["offense"], "TRANSLUCIDE": ["transparence"], "TREMBLEMENT": ["secousse"], "TRESSAGE": ["ouvrage"],
 "TRI": ["ordre"], "TRIDENT": ["lance"], "TRIPLE": ["répétition"], "TROMPETTE": ["musique"], "TRONC": ["arbre"], "TUNNEL": ["passage"],
 "UNISSON": ["accord"], "USURE": ["rongement"], "VACILLEMENT": ["chancellement"], "VAILLANCE": ["courage"], "VANITE": ["orgueil"], "VASE": ["contenant"],
 "VEGETATION": ["plante"], "VEHICULE": ["monture"], "VERDATRE": ["couleur"], "VERGLAS": ["givre"], "VERTICAL": ["élévation"],
 "VESTIGE": ["ruine"], "VICTIME": ["proie"], "VIEILLISSEMENT": ["âge"], "VIF": ["vitesse"], "VIPERE": ["serpent"],
 "VIVACITE": ["vitesse"], "VIVRES": ["nourriture"], "VOLEE": ["répétition"], "VOLUTES": ["fumée"], "VOUTE": ["abri"], "VŒU": ["serment"],
 "ŒUF": ["graine"],
}
FUSIONS.update({"LOUP": ["bête"], "OURS": ["bête"], "BLANC": ["couleur"]})
RENOMME.update(FUSIONS)

# (page, mot) -> mots qui le remplacent sur cette page ([] : le mot disparaît)
PAGE = {
 ("control-water", "NIVEAU"): ["hauteur"],                 # le niveau de l'eau
 ("greater-restoration", "NIVEAU"): ["vie", "durable"],    # la force vitale perdue, rendue
 ("nullify", "NIVEAU"): [],                                # « par niveau du lanceur » : une échelle de jeu
}
# Le seuil de niveau d'un sort (« arrête les sorts jusqu'au niveau 3 ») ne s'écrit plus en mots : le poids d'un sort se lit
# dans son cercle d'Interaction, donc le seuil devient un satellite Interaction (niveau + 1) sur l'Impact. Voir convert.sat_type.
import unicodedata as _u
def _norm(w): return "".join(c for c in _u.normalize("NFD", w.upper()) if _u.category(c) != "Mn").replace("'", "").replace("-", "")
def remplace(page, mot):
    """mots qui remplacent celui-ci, ou None ; une fusion se suit jusqu'au bout (cicatrices → cicatrice → marque)"""
    if (page, mot) in PAGE: return PAGE[(page, mot)]
    n = RENOMME.get(mot)
    for _ in range(4):
        if n and len(n) == 1 and _norm(n[0]) in RENOMME: n = RENOMME[_norm(n[0])]
        else: break
    return n

# ---------- Retouches de Baptiste, 15 novembre 2026 (soir) ----------
# La diversité des bêtes et l'échelle des lieux sont gardées : ces mots ne se fondent plus dans « bête » ou « lieu ».
for _k in """AUROCHS BATRACIEN CRAPAUD GRENOUILLE CHAUVESOURIS LOUP OURS REQUIN SINGE TAUREAU ALBATROS PERROQUET PHENIX RAT CRIQUETS FOURMI
LIBELLULES PAPILLONS PHALENE SCARABEES SCORPION VIPERE BOURG REGION DOMAINE PLACE BUTTE TERTRE PRE SOUSBOIS MANOIR CHAUMIERE CAMP FORT""".split():
    RENOMME.pop(_k, None)
# En échange (le compte reste à 1001) : des mots de deux pages qui disent la même chose qu'un mot déjà en usage, et les
# derniers mots isolés.
RENOMME.update({
 "ABSENCE": ["vide"], "ACCIDENT": ["malchance"], "AMOINDRISSEMENT": ["affaiblissement"], "ASPECT": ["apparence"], "AVERSE": ["pluie"],
 "BOURBIER": ["boue"], "CAMOUFLAGE": ["dissimulation"], "CHAOS": ["confusion"], "CONTRECOUP": ["riposte"], "DISPARITION": ["invisibilité"],
 "EFFONDREMENT": ["ruine"], "ENSEVELISSEMENT": ["enlisement"], "EROSION": ["rongement"], "HEMORRAGIE": ["saignement"],
 "LACERATION": ["déchirure"], "LANGAGE": ["langue"], "PLAIE": ["blessure"], "SUFFOCATION": ["étouffement"],
 "TURQUOISE": ["gemme"], "TOURMALINE": ["gemme"],                      # des pierres, en Composante
 "AGGRAVATION": ["croissance"], "BOITERIE": ["lenteur"], "CAUSE": ["origine"], "VASTITUDE": ["grand"], "VITRIFICATION": ["verre"],
 "REPRESENTATION": ["spectacle"], "SCENE": ["spectacle"],
 "JOUR": ["jours"],                                                    # « jour » est une durée : l'unité
 "SPHERES": ["sphère"],                                                # une forme : le cercle Forme s'en charge (formes_mots)
})
PAGE.update({
 # la lumière du jour est une lumière
 ("daylight", "JOUR"): ["lumière"], ("hallow", "JOUR"): ["lumière"], ("daybreak-arrow", "JOUR"): ["lumière"], ("morning-sun", "JOUR"): ["lumière"],
 ("illusory-hoard", "INTACT"): ["leurre"], ("stalwart-resolve", "INTEGRITE"): [],
 # mots à deux sens : un mot par sens
 ("electric-arc", "ARC"): ["éclair"],                                  # l'arc électrique ; « arc » reste l'arme
 ("er-adulas-moonblade", "ARC"): ["lame"], ("er-golden-arcs", "ARC"): ["lame"], ("er-glintstone-arc", "ARC"): ["lame"],
 ("keyhole", "REGARD"): ["vision"], ("heatvision", "REGARD"): ["vision"], ("shifting-form", "REGARD"): ["vision"],
 ("darkened-eyes", "REGARD"): ["vision"], ("unblinking-flame-aura", "REGARD"): ["vigilance"],     # « regard » reste le regard qu'on jette
 ("detect-relations", "SANG"): ["parenté"],                            # les liens du sang ; « sang » reste le sang
})
# « force » a deux sens. La faculté (la force d'un être) reste « force » : pages FORCE_FACULTE. La force d'une aura est sa
# « puissance ». L'énergie de force des règles n'est pas un mot : un Impact sans nature délivre la force brute du verbe
# (arcane §6.7), donc le mot disparaît ; là où il était seul sur un Impact plein, le mot qui dit l'effet le remplace.
FORCE_FACULTE = {"enhance-ability", "death-knell", "enticing-adulation", "enemys-heart", "song-of-strength", "psychic-leech", "hallow"}
FORCE_PUISSANCE = {"detect-evil-and-good", "detect-undead", "arcane-sight", "arcane-sight-greater", "detect-aberration", "invigorating-repose"}
FORCE_SEULE = {"symbol-of-sealing": ["barrière"], "emergency-force-sphere": ["barrière"], "spiritual-squire": ["serviteur"]}
_remplace0 = remplace
def remplace(page, mot):
    if mot == "FORCE":
        if page in FORCE_FACULTE: return None
        if page in FORCE_PUISSANCE: return ["puissance"]
        return FORCE_SEULE.get(page, [])
    return _remplace0(page, mot)
RENOMME.update({"CRIQUETS": ["criquet"], "LIBELLULES": ["libellule"], "PAPILLONS": ["papillon"], "SCARABEES": ["scarabée"]})

# ---------- Relecture du lexique par Baptiste, 16 novembre 2026 ----------
RENOMME.update({
 "PERMANENT": ["permanence"], "INVISIBLE": ["invisibilité"], "NOIRE": ["noir"],     # doublons
 "INCANTATION": ["sort"],                       # « ne peut plus lancer de sort »
 "REMANENCE": ["souvenir"], "FAUXSEMBLANT": ["illusion"], "DEROBADE": ["dissimulation"], "PESANTEUR": ["gravité"],
 "AGRESSION": ["combat"], "BATRACIEN": ["grenouille"], "VIPERE": ["serpent"],
 "COLONNES": ["colonne"],                       # une forme : le cercle Forme s'en charge (formes_mots)
})
# Une énergie ne s'écrit pas en mot sur l'Impact : elle s'inscrit par les symboles de sa combinaison élémentaire, en satellites.
# mot -> combinaison (voir combos.COMBOS) ; « terre » est l'élément seul.
ENERGIES = {"ACIER": "Acier", "DECHARGE": "Éclair", "FOUDRE": "Foudre", "FROID": "Glace", "SANSCHALEUR": "Glace", "LAVE": "Lave",
            "SABLE": "Sable", "BRUME": "Brume", "TERRE": "Terre"}
# Celui que l'effet vise ne s'écrit pas en mot sur l'Impact : c'est une valeur de Cible (2 un allié, 3 un ennemi), en satellite.
CIBLES = {"ALLIE": 2, "ENNEMI": 3}
# Seize places libérées par cette relecture : seize mots d'une page retrouvent leur nom propre plutôt que de se fondre
# dans un mot général (pierres, plantes, une couleur, deux heures du jour, un objet).
for _k in "AGATE JACINTHE GEODE PYRITE BELLADONE MANDRAGORE ORTIE PAVOT LOTUS NENUPHAR ROSE CHENE BLANC AUBE MINUIT ETENDARD".split():
    RENOMME.pop(_k, None)
RENOMME.update({"PHALENE": ["papillon"]})                  # un papillon de nuit
PAGE.update({("ironwood", "ACIER"): ["durcissement"]})     # « un bois aussi dur que l'acier » : la qualité, non l'énergie
for _k in "EPAVE CREVASSE OURAGAN".split(): RENOMME.pop(_k, None)     # trois places libérées : trois mots retrouvent leur nom

# ---------- Relecture de l'Impact, passe 2 (15 novembre 2026, soir) ----------
# « vol » ne dit plus que le vol dans les airs (« envol » s'y fond) ; dérober s'écrit « larcin », déjà en usage.
RENOMME["ENVOL"] = ["vol"]
for _p in ("covetous-urge", "covetous-aura", "theft-ward", "healing-thief", "claim-identity", "envious-urge", "arcana-theft", "beacon-of-guilt", "swipe"):
    PAGE[(_p, "VOL")] = ["larcin"]
RENOMME.pop("COUSSIN", None)        # un coussin n'est pas un rempart : le mot reprend sa place (celle qu'« envol » a libérée)
# faille = l'ouverture dans une défense ; faiblesse = la cible diminuée ; vulnérabilité = blessée davantage par une chose précise.
# « affaiblissement » disait la même chose que « faiblesse » : fondu (décision de Baptiste, 16 novembre 2026)
RENOMME["AFFAIBLISSEMENT"] = ["faiblesse"]; RENOMME["AMOINDRISSEMENT"] = ["faiblesse"]
