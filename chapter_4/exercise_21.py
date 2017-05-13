# -*- coding: utf-8 -*-
# 2, 10, 13, 14, 16, 17, 18, 19, 21, 23, 26, 31, 32, 35
# extra - 27: https://pdfs.semanticscholar.org/3973/ff27eb173412ce532c8684b950f4cd9b0dc8.pdf

##################
# 21 - Write a function that takes a text and a vocabulary as its arguments and returns the set of words that appear
# in the text but not in the vocabulary. Both arguments can be represented as lists of strings. Can you do this in
# a single line, using set.difference()?
##################

from nltk import word_tokenize


def differ(_text, _vocabulary):
    return set(_text).difference(set(_vocabulary))

text = word_tokenize('these are some words in the a my hello')
vocabulary = word_tokenize('these are some words')

print(differ(text, vocabulary))
