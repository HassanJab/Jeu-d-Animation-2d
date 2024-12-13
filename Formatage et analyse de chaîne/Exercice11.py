# -*- coding: utf-8 -*-
"""Exercice. Vérifiez qu’une chaîne contient un point. """

import re

# Tester une 
result1 = re.search(r'\.', 'abc.com')
result2 = re.search(r'\.', 'abccom')

print(result1)
print(result2)
