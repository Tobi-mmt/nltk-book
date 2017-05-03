# -*- coding: utf-8 -*-
# Aufgaben 6, 7, 20, 21, 24, 30, 34, 39, 38, 41, 43  Bis Dienstag
# -----------------
# 41 list in nested loop
# -----------------
import re

words = ['attribution', 'confabulation', 'elocution',
         'sequoia', 'tenacious', 'unidirectional']
for i, word in enumerate(words):
    words[i] = re.sub(r'[^aeiou]', '', word)

print('My result: ', sorted(words))
print('Solution: ', ['aiuio', 'eaiou', 'eouio', 'euoia', 'oauaio', 'uiieioa'])