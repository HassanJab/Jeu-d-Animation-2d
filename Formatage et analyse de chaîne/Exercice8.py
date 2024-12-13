# -*- coding: utf-8 -*-
"""Exercice. Trouvez la suite des chiffres au début d’une chaîne. """

import re

result1 = re.match(r'[0-9]*', '123xyz')
result2 = re.match(r'[0-9]*', 'xyz123')

print(result1)
print(result2)
