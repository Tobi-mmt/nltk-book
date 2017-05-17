# -*- coding: utf-8 -*-
# 2, 10, 13, 14, 16, 17, 18, 19, 21, 23, 26, 31, 32, 35
# extra - 27: https://pdfs.semanticscholar.org/3973/ff27eb173412ce532c8684b950f4cd9b0dc8.pdf

##################
# 17 - Write a function shorten(text, n) to process a text, omitting the n most frequently occurring words of the text.
# How readable is it?
##################

import nltk
from nltk.corpus import brown
from nltk import word_tokenize
import collections


def shorten(text, n):
    if isinstance(text, str):
        text = word_tokenize(text)
    count = collections.Counter(text)
    common = [c for c, _ in count.most_common(n)]
    return ' '.join([w for w in text if w.lower() not in common])


words = brown.words(categories='news')
string = 'Far far away, behind the word mountains, far '

print(shorten(words, 8))
print(shorten(string, 1))
