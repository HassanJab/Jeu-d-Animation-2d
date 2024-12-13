# -*- coding: utf-8 -*-
"""Exercice. Vérifiez qu’une chaîne est de la
forme CLCLCL où C est un chiffre et L une lettre majuscule. """

import re

result1 = re.match(r'([0-9][A-Z]){3}$', '1A2C6B')
result2 = re.match(r'([0-9][A-Z]){3}$', '1A2C6B4S')
result3 = re.match(r'([0-9][A-Z]){3}$', '1AEC6B')

print(result1)
print(result2)
print(result3)
