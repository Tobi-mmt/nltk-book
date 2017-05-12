# -*- coding: utf-8 -*-
# 2, 10, 13, 14, 16, 17, 18, 19, 21, 23, 26, 31, 32, 35
# extra - 27: https://pdfs.semanticscholar.org/3973/ff27eb173412ce532c8684b950f4cd9b0dc8.pdf

##################
# 13 - Write code to initialize a two-dimensional array of sets called word_vowels
##################
sent = ['Take', 'care', 'of', 'the', 'sense', ',', 'and', 'the', 'sounds', 'will', 'take', 'care', 'of', 'themselves', '.']


def word_vowels(word_list):
    return [[len(word), len([v for v in word if v in 'aeiou'])] for word in word_list]


print(word_vowels(sent))
