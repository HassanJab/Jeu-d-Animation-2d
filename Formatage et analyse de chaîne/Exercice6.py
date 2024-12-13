# -*- coding: utf-8 -*-
"""Exercice. Vérifiez qu’une chaîne se termine par '123'.  """

import re

result1 = re.search(r'123$', 'abc12123')
result2 = re.search(r'123$', 'abc121234')

print(result1)
print(result2)
