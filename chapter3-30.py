# -*- coding: utf-8 -*-
# Aufgaben 6, 7, 20, 21, 24, 30, 34, 39, 38, 41, 43  Bis Dienstag
# -----------------
# 30 stemmeing
# -----------------

import nltk, re

tokens = nltk.corpus.brown.words(categories='news')

porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()

porter_stem = [porter.stem(t) for t in tokens]
lancaster_stem = [lancaster.stem(t) for t in tokens]

print('Original \t Porter \t Lancaster')
for i, t in enumerate(tokens):
    if str(porter_stem[i]) != str(lancaster_stem[i]):
        print(t, '\t ', porter_stem[i], '\t ', lancaster_stem[i])
