# -*- coding: utf-8 -*-
# 2, 10, 13, 14, 16, 17, 18, 19, 21, 23, 26, 31, 32, 35
# extra - 27: https://pdfs.semanticscholar.org/3973/ff27eb173412ce532c8684b950f4cd9b0dc8.pdf

##################
# 35 - Write a program to implement a brute-force algorithm for discovering word squares, a kind of n × n crossword
# in which the entry in the nth row is the same as the entry in the nth column.
# For discussion, see http://itre.cis.upenn.edu/~myl/languagelog/archives/002679.html
##################

import nltk
import random

num = 5


def find_word(length, corpus, first_letters=None):
    if first_letters:
        return [w.upper() for w in corpus if w.lower().startswith(first_letters.lower()) and len(w) == length][0]
    else:
        result = random.choice(corpus)
        return result.upper() if len(result) == length else find_word(length, corpus)


def solve_crossword(n, corpus):
    try:
        crossword = [find_word(n, corpus)]
        for i in range(1, n):
            letter = ''
            for j in range(0, i):
                letter += crossword[j][i]
            new = find_word(n, corpus, letter)
            crossword.append(new)
        return crossword
    except:
        return None


word_corpus = nltk.corpus.words.words('en')
result = None
while not result:
    result = solve_crossword(num, word_corpus)

for w in result:
    print(w)