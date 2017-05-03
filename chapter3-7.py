# -*- coding: utf-8 -*-
# Aufgaben 6, 7, 20, 21, 24, 30, 34, 39, 38, 41, 43  Bis Dienstag
# -----------------
# 7 write regex
# -----------------
import nltk, re

wordlist = nltk.corpus.words.words('en')

print([w for w in wordlist if re.search(r'^(a|the|an)$', w)])