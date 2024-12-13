# -*- coding: utf-8 -*-
import re

"""Exercice. Vérifiez qu’une chaîne de caractère contient la lettre z."""

import re

result1 = re.search(r'z', 'raz')
result2 = re.search(r'z', 'torro')

print(result1)
print(result2)

