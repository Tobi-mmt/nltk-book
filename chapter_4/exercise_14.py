# -*- coding: utf-8 -*-
# 2, 10, 13, 14, 16, 17, 18, 19, 21, 23, 26, 31, 32, 35
# extra - 27: https://pdfs.semanticscholar.org/3973/ff27eb173412ce532c8684b950f4cd9b0dc8.pdf

##################
# 14 - Write a function novel10(text) that prints any word that appeared in the last 10% of a text that had not been
# encountered earlier.
##################


def novel10(text):
    len_9 = int(len(text) * 0.9)
    print(set(text[len_9:]).difference(set(text[:len_9])))


test = ['hello', 'this', 'is', 'my', 'test', 'so', 'far', 'so', 'good', 'yeah', 'yeah']
novel10(test)
