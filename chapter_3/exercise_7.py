# -*- coding: utf-8 -*-
# Aufgaben 6, 7, 20, 21, 24, 30, 34, 39, 38, 41, 43  Bis Dienstag
# -----------------
# 7 write regex
# -----------------
import nltk, re
from nltk import word_tokenize

word_list = nltk.corpus.words.words('en')

print([w for w in word_list if re.search(r'^(a|the|an)$', w)])


digits = "The student didn't know how to calculate 3+4 or 45*2+12 or 3+3+3 or 444+5*9000 or 4*4."
word_list = word_tokenize(digits)
print([w for w in word_list if re.search(r'^(\d|\*|\+)+$', w)])
