# -*- coding: utf-8 -*-
"""Exercice. Extraire l’extension d’un nom de
fichier (suite de 2 à quatre lettres après le dernier .). """

import re

result1 = re.search(r'\.[a-zA-Z]{2,4}$', 'abc.com')
result2 = re.search(r'\.[a-zA-Z]{2,4}$', 'image.jpg')
result3 = re.search(r'\.[a-zA-Z]{2,4}$', 'document.pdf')

print(result1)  # Affichera ".com"
print(result2)  # Affichera ".jpg"
print(result3)  # Affichera ".pdf"
