# -*- coding: utf-8 -*-
"""Lexique typé des glyphes (règle 5 de l'audit du 14 novembre).

Chaque mot qu'un cercle Cible peut porter est déclaré ici, une fois, avec sa catégorie. Le contrôle (lint.py) refuse tout mot
qui n'y figure pas : un mot nouveau — autre édition, autre jeu — se déclare d'abord ici, dans la catégorie qui dit ce qu'il est.

La Cible dit QUI ou QUOI reçoit le sort, jamais ce que le sort fait :
  ETRE     une sorte d'être (précise la catégorie visée ; ne déclenche pas le mode objet)
  OBJET    une chose inerte, une matière, un mal ou une substance que l'on vise (mode objet)
  PART     une part de l'être (corps, psyché, âme…)
  FACULTE  une faculté de l'être que le sort renforce ou affaiblit
  LIEU     un lieu de destination ou d'effet
  TRAME    ce que l'on vise quand la Cible est vide (la trame elle-même)
  QUALITE  un qualificatif qui précise l'un des précédents
"""
ETRE = """bete elementaire plante fee monture mortvivant divinite esprit goule nuee araignee insecte ancetre serviteur creature vermine
cheval graine invoque molosse dragon millepattes equipage guepe aigle ver legion familier chauvesouris rat aberration squelette hantise
allie ecuyer savant mammouth singe corbeau cocher vipere grenouille loup batracien etre aurochs fourmi golem serpent double compagnon"""
OBJET = """objet arme cadavre eau trait metal ecrit porte pierre os projectile corde nourriture coffre armure bois baton piege talisman
rune baies serrure livre cape matiere mur instrument tertre fer recipient gemme plume potion echarpe mineral structure mecanisme feu
chene rose crane empreinte paroi piece bouclier carquois bourse remede contenant receptacle arc lanterne gant miroir œuf selle navire
botte etoffe pigne poison maladie entrave passage"""
PART = """psyche memoire sang ame souffle corps membre membres peau visage vital tete chair voix cœur gueule bras queue carapace poil
levre œil jambe barbe articulation poing cheveux croc langue vie age"""
FACULTE = """garde resistance force coup frappe aptitude endurance lucidite prestance adresse raison volonte"""
LIEU = """lieu plan surface terrain ethere"""
TRAME = """sort magie"""
QUALITE = """petit hostile lumineux tenebreux mort vivant naturelle toutes secret invisible"""
CIBLE = {c: set(v.upper().split()) for c, v in dict(ETRE=ETRE, OBJET=OBJET, PART=PART, FACULTE=FACULTE, LIEU=LIEU, TRAME=TRAME, QUALITE=QUALITE).items()}
CIBLE_MOTS = set().union(*CIBLE.values())

# Impact : notions mesurées (une valeur chiffrée exige une unité) et unités admises (règle 7)
MESURES = set("VISION VOL SAUT PAS ELEVATION PORTEE VITESSE STATURE PORT LECTURE ALLONGE".split())
UNITES = set("METRES KILOMETRES KILOGRAMMES LITRES FOIS MINUTES HEURES JOURS CUBES".split())
# verbes sous lesquels « vie » chiffrée serait lue comme un soin alors que le sort blesse (règle 3)
VERBES_NUISIBLES = set("Détruire Corrompre Révéler Séparer Dissimuler Réduire Ancrer Lier Déstabiliser Repousser Attirer Bannir".split())
