# -*- coding: utf-8 -*-

"""Exercice. Vérifiez qu’une chaîne contient la chaîne de caractères Python."""

import re

result1 = re.search(r'Python', 'Le langage Python est facile à apprendre')
result2 = re.search(r'Python', 'Le langage Java est facile à apprendre')

print(result1)
print(result2)