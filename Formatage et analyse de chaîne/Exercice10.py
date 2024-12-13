# -*- coding: utf-8 -*-
"""Exercice. Vérifiez qu’une chaîne débute 
par une séquence de trois lettres. """

import re

result1 = re.match(r'[A-Z]{3}', 'ABC123')
result2 = re.match(r'[A-Z]{3}', 'AB123')

print(result1)
print(result2)
