# -*- coding: utf-8 -*-
"""Exercice. Vérifiez qu’une chaîne débute par x 
suivi de deux caractères quelconques suivi de y. """

import re

result1 = re.match(r'x..y', 'xefyab')
result2 = re.match(r'x..y', 'xeyab')

# Afficher les résultats
print(result1)
print(result2)