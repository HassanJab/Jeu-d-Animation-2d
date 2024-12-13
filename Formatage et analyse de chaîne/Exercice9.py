# -*- coding: utf-8 -*-
"""Exercice. Vérifiez qu’une chaîne débute 
par une suite d’une majuscule ou plus."""

import re

result1 = re.match(r'[A-Z]+', 'Allo')
result2 = re.match(r'[A-Z]+', 'ABCDabcd')

print(result1)
print(result2)
