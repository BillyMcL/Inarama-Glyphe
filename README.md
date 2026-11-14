# Bibliothèque glyphique d'Inarama

Les sorts des **SRD 5.1 et 5.2** de D&D (règles de 2014 et de 2024), du **SRD 3.5**, de **Pathfinder 1** et de **Pathfinder 2** (en cours, école par école) transposés en glyphes d'Inarama : chaque sort en **glyphe circulaire** et en **glyphe en bande**, en notation **déclarée** et **non déclarée**, avec la lecture de chaque cercle et la traduction des annotations en Alde.

- 2375 sorts, 4098 formes (Arcane, Magie hybride, arts rares ; une forme par option de lancement ; une forme « version 2024 », « version 3.5 » ou « Pathfinder 1 » quand une autre édition change le glyphe).
- Chaque sort porte une description, la note qu'un arcaniste écrirait à côté du glyphe (`donnees/descriptions.json`).
- Pathfinder 1 : les sorts légaux en Pathfinder Society, plus ceux des sorts non légaux qui ont passé un tri strict (canon d'Inarama, puissance, intérêt) ; hors *Technology Guide*. Les noms propres de Golarion sont effacés, le sens du sort est gardé ; les sorts qui dépendent du monde de Golarion ou qui ne sont qu'une mécanique de jeu sont écartés et listés dans `PF1_RELECTURE` (`moteur/fiches.py`).
- Pathfinder 2 : édition d'origine et version remaniée ensemble ; un sort présent dans les deux reçoit une forme « version remaniée » quand son glyphe diffère. Le rang vaut le niveau (un tour de magie vaut 0) ; un sort de rang 10 sans équivalent dans D&D est de niveau 10. Les sorts écartés sont listés dans `PF2_ECARTE` (`moteur/fiches.py`). Sorts focalisés et rituels : à venir.
- Règle d'or : **deux glyphes strictement identiques sont le même sort**. La construction s'arrête si deux sorts différents produisent le même glyphe.

Le système glyphique lui-même (cercles, valeurs, annotations) est défini dans le dépôt de lore [Inarama-lore](https://github.com/BillyMcL/Inarama-lore), qui fait autorité. Cette bibliothèque en est une application : quand une règle change dans le lore, on l'applique ici.

## Lire la bibliothèque

Le site est publié automatiquement par GitHub Pages à chaque modification de la branche `main` :
**https://billymcl.github.io/Inarama-Glyphe/**

## Arborescence

| Chemin | Rôle |
|---|---|
| `moteur/fiches.py` | **Les fiches des sorts** : ce que les données D&D ne disent pas (nom français, famille, verbe, combinaison, cible, condition, impact, options…). C'est le fichier qu'on modifie le plus souvent. |
| `moteur/convert.py` | Conversion d'un sort D&D en glyphe : unités, valeurs, cercles, satellites, répartition astrale. |
| `moteur/site.py` | Génération du site (index, pages des sorts, règles) et contrôle d'unicité. |
| `moteur/gen_glyphs.py` | Dessin du glyphe circulaire. |
| `moteur/band_glyph.py` | Dessin du glyphe en bande. |
| `moteur/spells.py` | Valeurs (alphabet des neuf formes), noyaux, et les sorts du premier grimoire d'essai (la bibliothèque ne les reprend plus : tous ses sorts se génèrent depuis leurs données). |
| `moteur/lexique.py` | Lexique typé : les mots qu'un cercle Cible peut porter (être, objet, part, faculté, lieu), les mesures et leurs unités. Un mot nouveau se déclare ici. |
| `moteur/lint.py` | Contrôle de lecture des glyphes (Cible typée, Impact lisible, une énergie par cercle, unités, satellites annotés). La construction stricte s'arrête au premier défaut. |
| `moteur/build_picto.py` | Pictogrammes des douze verbes du noyau. |
| `moteur/alde.py`, `moteur/translit.py` | Écriture de l'Alde et translittération provisoire des annotations. |
| `moteur/combos.py` | Les 35 combinaisons élémentaires et la correspondance des écoles. |
| `moteur/compact.py` | Allègement des pages : chaque syllabe d'Alde dessinée une fois, puis réemployée. |
| `donnees/srd/spells.json` | Données des sorts du SRD 5.1, règles de 2014 (5e-bits). |
| `donnees/srd/spells-2024.json` | Données des sorts du SRD 5.2, règles de 2024 (5e-bits). |
| `donnees/srd/srd35/` | Texte du SRD 3.5 (OGL), lu par `moteur/srd35.py`. |
| `donnees/pf1/sorts-pf1.json` | Sorts de Pathfinder 1 (OGL), lus par `moteur/pf1.py`. |
| `donnees/grimoire_glyphique.html`, `donnees/glyphes_en_bande.html` | Documents de référence dont la page des règles reprend des sections. Le grimoire est en pause : on ne le modifie pas sans décision. |

## Construire le site sur son ordinateur

Il faut Python 3.10 ou plus récent, sans aucune bibliothèque à installer.

```
python moteur/site.py site
```

Le site apparaît dans le dossier `site/` (ignoré par git) : ouvrir `site/index.html`.
Pour que la construction s'arrête en cas de glyphe en double, comme sur GitHub : `STRICT=1 python moteur/site.py site` (sous Windows PowerShell : `$env:STRICT=1; python moteur/site.py site`).

## Publication

Le fichier `.github/workflows/publier.yml` reconstruit et publie le site à chaque envoi sur `main`. Une seule fois, dans les réglages du dépôt : **Settings → Pages → Build and deployment → Source : GitHub Actions**.

## Licence et attribution

Les données de sorts proviennent des *System Reference Documents 5.1 et 5.2* de Wizards of the Coast LLC, publié sous licence [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/legalcode), et du *System Reference Document 3.5*, publié sous l'Open Game License v1.0a. Voir `ATTRIBUTION.md`.

Le système glyphique, les conversions, les glyphes et l'univers d'Inarama sont des créations originales ; leur licence n'est pas encore fixée.
