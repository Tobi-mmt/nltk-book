# -*- coding: utf-8 -*-
# Aufgaben 6, 7, 20, 21, 24, 30, 34, 39, 38, 41, 43  Bis Dienstag
# -----------------
# 41 list in nested loop
# -----------------

words = ['attribution', 'confabulation', 'elocution',
         'sequoia', 'tenacious', 'unidirectional']

s = sorted(set([''.join([c for c in w if c in 'aeiou']) for w in words]))

print('My result: ', sorted(s))
print('Solution: ', ['aiuio', 'eaiou', 'eouio', 'euoia', 'oauaio', 'uiieioa'])
