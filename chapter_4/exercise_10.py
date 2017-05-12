# -*- coding: utf-8 -*-
# 2, 10, 13, 14, 16, 17, 18, 19, 21, 23, 26, 31, 32, 35
# extra - 27: https://pdfs.semanticscholar.org/3973/ff27eb173412ce532c8684b950f4cd9b0dc8.pdf

##################
# 10 - Write a program to sort words by length.
##################

sent = ['Take', 'care', 'of', 'the', 'sense', ',', 'and', 'the', 'sounds', 'will', 'take', 'care', 'of', 'themselves', '.']

sent.sort(key=len)

print(sent)