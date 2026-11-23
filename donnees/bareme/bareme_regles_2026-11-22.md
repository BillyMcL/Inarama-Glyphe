# Barème des sorts — règles consolidées (22 novembre 2026)

Ce document rassemble en un seul endroit les règles du barème validées entre le 15 et le 19 novembre, et ce qui a changé depuis dans la bibliothèque. Il sert de cahier des charges pour rebrancher le calcul sur la bibliothèque d'aujourd'hui, puis pour le passer en code dans le dépôt (l'éditeur s'en servira).

Documents détaillés, qui restent la référence pour les chiffres et l'historique des décisions :
- `claude/bareme_etats_echelles_2026-11-17.md` : les échelles de degrés (quel mot à quel degré) ;
- `claude/bareme_etats_couts_2026-11-17.md` : les prix (règle par famille, prix par degré, outils, déplacements, phase 3) ;
- `claude/bareme_etats_rangement_mots_2026-11-17.md` : le rôle de chaque mot (porte le degré, manière, montant, lève ou garde) ;
- `claude/bareme_etres_appeles_2026-11-17.md` : la puissance des êtres appelés.

## 1. Principe

- Le coût d'un sort est un palier de 0 à 9. Il se calcule **sur le glyphe seul** : Noyau, cercles, valeurs, mots et satellites. C'est indispensable pour l'éditeur, qui ne connaît que le glyphe.
- Convention d'Inarama : on ne cherche plus à retrouver le niveau du jeu d'origine. On colle aux sources quand elles s'accordent, on tranche quand elles divergent. Le niveau des sources sert à mesurer, pas à imposer.
- Mesure de référence (20 novembre, état de l'époque, 5 740 formes) : 62 % des formes à un palier du niveau de la source, 84 % à deux. Limites connues : tours de magie trop chers (+2,1), niveaux 7 à 9 trop bas (−1,8).

## 2. Le calcul, étape par étape

### 2.1 Le prix de chaque cercle d'Impact

Selon ce que porte le cercle :

| Le cercle porte | Prix |
|---|---|
| un être appelé (mot PUISSANCE) | sa puissance, sur l'échelle des êtres appelés ; obéir (injonction 8) est compris ; un être qui ne fait que consentir (suggestion) vaut 1 de moins |
| un seuil en Interaction (épreuve de puissance, dissipation) | le palier du seuil (dissiper jusqu'au palier N coûte N) |
| un seuil sur l'Impact (lever, garder, agir malgré) | prix d'infliger l'état au degré du seuil × coefficient de sa grande famille (sens 0,8 ; savoir 1,5 ; caché 0,4 ; esprit 0,4 ; corps 0,8), plancher 0,4 |
| un mot d'état (porte le degré) | le prix du degré sur l'échelle de son mot (tableau « Prix par degré ») ; « chance » × 1,5 |
| une blessure ou un soin (montant) | −2,8 + 1,25 × log2(montant total), jamais moins de 1 |
| un mode de déplacement, un déplacement forcé, un outil sans degré | le prix fixe de sa table |
| souhait | palier maximal du sort reproduit + 1 |
| aucun mot connu | 3,0 par défaut : c'est ce qu'il faut faire disparaître |

Mots de manière, de nature, de précision et de Cosmétique : aucun prix propre.

### 2.2 Ajustements d'un cercle d'Impact

- Effet répété à chaque instant (satellite Durée « chaque · instants ») : +1.
- Imparable : +0 sous 3, +1 de 3 à 6, +3 au-delà.
- Satellite de Condition sur l'effet : −0,3 × (prix − 3), seulement au-dessus de 3.
- Suspension (l'état revient à la fin) : −1.

### 2.3 Plusieurs effets

- Le plus cher compte entier ; chacun des autres ajoute une part : la moitié si le plus cher vaut moins de 3, un quart s'il vaut moins de 6, un dixième au-delà.
- Les mots de manière de l'écriture (contre, malgré, sans, sauf) n'ont pas de prix propre ; « tant que » sur une Durée compte comme une condition de fin ; « prochain » comme une occasion.
- Une injonction qui accompagne un être appelé est comprise dans sa puissance ; une suggestion retire 1.
- État d'un instant (6 secondes) : × 0,75.

### 2.4 Ce qui étend le sort (ajouts)

Chaque ajout est multiplié par la force de l'effet (prix ÷ 3, au plus 1). Le total des ajouts ne dépasse jamais le prix de l'effet + 1.

| Relation | Ajout |
|---|---|
| plusieurs cibles | +1 ; quatre ou plus +2 ; toutes les cibles choisies +2,5 (sort long : +4) |
| budget de vie à répartir | +1 sous 60, +2 au-delà |
| à distance | +0,4 |
| zone | +0,3 × log2(volume ÷ 30), au plus 3 |
| cible profonde (mots de Cible : AME, CORPS, ESPRIT, SORT) | +1 |
| condition qui ouvre (mots de Condition : MORT, SORT, ARTEFACT) | +1 |
| psyché | +0,3 |
| durée | +0,3 par décuplement depuis 6 s ; finie plafonnée à une semaine (1,5) ; sans fin 1,8 ; poids 1 / 0,5 / 0,25 selon que l'effet vaut moins de 3, moins de 6, ou plus |
| quantité (instances) | +log2(nombre) pour une blessure, la moitié pour un autre effet |

### 2.5 Ce qui restreint le sort (rabais)

- Limitation à une sorte d'êtres (effet général rétréci) : −3, ou −1 si l'effet vaut moins de 3. Une sorte qui n'est que ce que le sort atteint (portée) : rien.
- Condition de fin, occasion, cible-objet, exigence pour lancer, incantation longue : chacun −0,3 × (prix − 3) environ ; prix d'une Composante : 0,1, 0,2 ou 0,3 × (prix − 3) selon sa valeur, moitié si elle n'est pas consommée.
- Les rabais se cumulent ainsi : le plus fort entier, la moitié des autres, au total 2 au plus.
- Contrecoup (ce que le lanceur subit) : − part × prix de l'état subi.
- Seuil de vie par créature, ou budget à répartir : −30 % sous 30, −20 % sous 60, −10 % jusqu'à 120, rien au-delà.

### 2.6 Le palier

Le total est arrondi et borné de 0 à 10. Le palier 10 est celui de la Quintessence (sorts de rang 10 de PF2) : il est atteignable.

## 3. Ce qui a changé dans la bibliothèque depuis le 20 novembre, et ce que le barème doit en faire

| Changement | Effet sur le barème | État |
|---|---|---|
| Lexique fermé à 1 001 mots | les tables de prix doivent couvrir tout mot d'Impact qui porte un effet ; un mot hors des tables tombe au défaut 3,0 | à mesurer (étape 3 du plan) |
| Règle de la garde (22 novembre) : PROTECTION = bonus à la défense en degré ; REMPART = montant retranché par coup ; RESISTANCE = la moitié arrêtée, degré 5 ; IMMUNITE = plus rien ne passe, plein ; BARRIERE = ce qui arrête tout | échelle de la garde réécrite (voir 4.1) | validé le 22 novembre |
| Bonus en degré (moitié du bonus, arrondie au-dessus), appliqués partout | rien : la règle existait | fait |
| Nombres arrondis au plus proche de la vraie valeur, 5 formes au plus | le barème lit la valeur écrite sur le glyphe | fait |
| Concentration en Condition (« parole · concentration ») | aucun prix aujourd'hui | proposé : pas de rabais pour l'instant, à mesurer |
| Formes combinées (plusieurs Noyaux, cercles communs) | chaque Noyau apporte ses effets ; on applique la règle « plusieurs effets » (2.3) à l'ensemble ; les cercles communs (Cible, Durée, zone…) ne comptent qu'une fois | validé le 22 novembre |
| Mots nouveaux de l'écriture (contre, malgré, sans, tant que, prochain, sauf) | ce sont des mots de manière : aucun prix propre ; « tant que » sur une Durée est une condition de fin (rabais) ; « prochain » limite à un usage (rabais d'occasion) | validé le 22 novembre |

## 4. Propositions nouvelles (validées le 22 novembre)

### 4.1 L'échelle de la garde

| Mot | Degré | Ce que c'est | Prix proposé | D'où vient le prix |
|---|---|---|---|---|
| protection | 1 | +1 ou +2 à la défense | 1,2 | ancien prix de protection 1 |
| protection | 2 | +3 ou +4 | 1,6 | entre les anciens 1 et 3 |
| protection | 3 | +5 ou +6 | 1,9 | ancien prix de protection 3 |
| protection | 4 et plus | +7 et plus | droite de la règle montante (plein 4,0) | non vérifié |
| rempart | montant | N retranché à chaque coup | règle des montants (comme une blessure de N) | règle existante des montants |
| résistance | 5 | la moitié des coups arrêtée | 2,6 | ancien prix de protection 5 |
| immunité | plein | plus rien ne passe d'une nature | 4,0 | ancien prix du plein de la garde |
| barrière | plein | rien ne franchit (mur, zone) | 4,0 | inchangé |

### 4.2 Le calcul doit lire le glyphe, pas la source

Le calcul du 20 novembre lisait une partie des relations (durée, zone, cibles, prix d'une Composante) dans les données d'origine du sort. Pour l'éditeur, tout doit venir du glyphe :
- cibles : valeur et mots du cercle Cible, satellites de Quantité ;
- zone : cercles Forme et Ampleur ;
- distance : cercle Localisation ;
- durée : cercle Durée (permanent = plein) ;
- prix et consommation : cercle Composante ;
- occasion, fin, exigence : cercle Condition et ses satellites.
Si une relation n'a aucune trace dans le glyphe, c'est une lacune d'écriture, pas une règle du barème : elle sera listée.

## 5. Lacunes connues

- Tours de magie trop chers, niveaux 7 à 9 trop bas.
- Répétition d'un dégât ou d'un soin à chaque tour : comptée par l'ajustement +1, mal calée.
- Sorts sans fin (petits utilitaires et sorts forts mêlés).
- Plafond des ajouts qui bloque quelques sorts de haut niveau.
- Mots d'Impact sans prix : 388 mots relevés le 22 novembre par une mesure rapide (plafond, pas le compte réel) ; à classer par rôle avant de les chiffrer.
- Durabilité d'une matière créée non écrite sur 127 formes (instantanées dans le jeu, mais la chose reste).

## 6. Choix de calcul

- Pas de facteur par jeu dans le coût : le calcul du 20 novembre multipliait les montants par un facteur propre à chaque jeu (3.5 × 1,25, PF1 × 1,2, PF2 × 1,25). Un glyphe ne dit pas de quel jeu il vient : le coût d'Inarama lit le montant écrit. Le rapport de mesure donne les résultats avec et sans ce facteur, pour voir son effet.
- Tables : `bareme_tables_2026-11-22.json` (échelles, mots, montants, outils, coefficients de levée, fins).

## 7. Décision de cadrage (23 novembre)

- L'échelle d'Inarama est calée sur D&D 5 (5e et 2024). Un niveau n d'Inarama vaut à peu près un niveau n de D&D 5, quelle que soit la source du sort ; on peut faire mieux que D&D 5 là où il est mal équilibré, tant que ça reste sensé.
- Exigence ferme : un sort de niveau n est plus fort qu'un sort de niveau n−1 et plus faible qu'un sort de niveau n+1.
- Le barème se règle sur D&D 5 seulement. Les autres jeux ne sont pas des cibles : leur niveau d'origine reste affiché à titre indicatif, avec son système. La conversion se contrôle sur les sorts présents dans deux jeux (même effet → même palier d'Inarama).
- Une fois le barème réglé, le cercle d'Interaction de chaque sort recevra son niveau d'Inarama ; le niveau d'origine passera entre parenthèses avec son système. L'éditeur donnera le niveau d'Inarama, et une estimation du niveau dans chaque système d'origine.

## 8. Repères officiels de D&D 5 (Guide du maître, « Créer un sort », p. 283-284 ; repris par la communauté)

Dégâts moyens par niveau, une action, instantané :

| Niveau | Une cible, jet pour moitié | Plusieurs cibles, jet pour moitié |
|---|---|---|
| tour de magie | 5,5 (1d10) | 3,5 (1d6) |
| 1 | 11 (2d10) | 7 (2d6) |
| 2 | 16,5 (3d10) | 10,5 (3d6) |
| 3 | 27,5 (5d10) | 21 (6d6) |
| 4 | 33 (6d10) | 24,5 (7d6) |
| 5 | 38,5 (7d10) | 28 (8d6) |
| 6 | 55 (10d10) | 38,5 (11d6) |
| 7 | 60,5 (11d10) | 42 (12d6) |
| 8 | 66 (12d10) | 45,5 (13d6) |
| 9 | 82,5 (15d10) | 49 (14d6) |

Autres repères : un jet qui annule vaut environ 1,25 fois un jet pour moitié ; des dégâts sans jet valent environ 0,6 fois ; une action répétée chaque tour vaut la moitié du tableau ; à effet égal, une portée plus longue rend le sort plus cher ; un sort sans concentration doit être plus faible (la concentration est une contrainte) ; une incantation longue autorise plus de puissance, une action bonus ou une réaction moins ; un état handicapant sans nouveau jet chaque tour vaut au moins le niveau 6.

Constat : les dégâts de D&D 5 montent à peu près en ligne droite avec le niveau (environ +8 par niveau sur une cible). La règle actuelle du barème suppose un doublement des dégâts tous les 1,25 palier : elle donne 5,2 pour 82,5 dégâts au lieu de 9. C'est la cause probable des niveaux 7 à 9 trop bas.
