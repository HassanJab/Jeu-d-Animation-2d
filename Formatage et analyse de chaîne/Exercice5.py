# -*- coding: utf-8 -*-
"""Exercice. Vérifiez qu’une chaîne est égale à '123'. """

import re

result1 = re.match(r'123$', '123')
result2 = re.match(r'123$', '1234')

print(result1)
print(result2)
