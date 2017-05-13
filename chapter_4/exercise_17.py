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
    return count.most_common(n)


words = brown.words(categories='news')
string = 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. A small river named Duden flows by their place and supplies it with the necessary regelialia'

print(shorten(words, 8))
print(shorten(string, 8))
