# -*- coding: utf-8 -*-
"""Exercice. Vérifiez qu’une chaîne débute par une lettre majuscule. """

import re

result1 = re.match(r'[A-Z]', 'Abcd')
result2 = re.match(r'[A-Z]', 'abcd')

print(result1)
print(result2)
