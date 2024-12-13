# -*- coding: utf-8 -*-
"""Exercice. Un identifiant est de la forme LLLLJJMMAACC, LLLL est une 
séquence de quatre lettres, JJ le jour en chiffre, MM le mois en chiffres, AA 
les deux derniers chiffres de l’année et CC est un numéro de séquence de 
deux chiffres. Validez qu’une chaîne respecte la syntaxe d’un identifiant et 
extrayez chacun des groupes si la chaîne est valide. """

import re

identifiant = "BEDA10069001"

pattern = r'([A-Z]{4})([0-3][0-9])([0-1][0-9])([0-9]{2})([0-9]{2})'

match = re.match(pattern, identifiant)

if match:
    groupes = match.group(1, 2, 3, 4, 5)
    print("Identifiant valide. Groupes extraits :", groupes)
else:
    print("Identifiant invalide.")
