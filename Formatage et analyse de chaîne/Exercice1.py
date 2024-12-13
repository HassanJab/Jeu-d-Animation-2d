# -*- coding: utf-8 -*-
"""Exercice. Vérifiez qu’une chaîne de caractère commence par la lettre z"""

import re

result1 = re.match(r'z', 'zorro')
result2 = re.match(r'z', 'torro')

print(result1)
print(result2)
