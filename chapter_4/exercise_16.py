# -*- coding: utf-8 -*-
# 2, 10, 13, 14, 16, 17, 18, 19, 21, 23, 26, 31, 32, 35
# extra - 27: https://pdfs.semanticscholar.org/3973/ff27eb173412ce532c8684b950f4cd9b0dc8.pdf

##################
# 16 - Read up on Gematria, a method for assigning numbers to words, and for mapping
# between words having the same number to discover the hidden meaning of texts
# (http://en.wikipedia.org/wiki/Gematria, http://essenes.net/gemcal.htm).
##################
import nltk
from nltk.corpus import brown
from nltk import word_tokenize

letter_vals = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 80, 'g': 3, 'h': 8,
               'i': 10, 'j': 10, 'k': 20, 'l': 30, 'm': 40, 'n': 50, 'o': 70, 'p': 80, 'q': 100,
               'r': 200, 's': 300, 't': 400, 'u': 6, 'v': 6, 'w': 800, 'x': 60, 'y': 10, 'z': 7, '#': 0}


def gematria(word):
    try:
        return sum(letter_vals[l] for l in word) if type(word) == type(str('')) else 0
    except:
        return 0


for category in brown.categories():
    corpus = brown.words(categories=category)
    devil_words = sum(1 for w in corpus if gematria(str(w).lower()) == 666)
    print('{} containes {} times the gematria "666"'.format(category, devil_words))
