# -*- coding: utf-8 -*-
# Aufgaben 6, 7, 20, 21, 24, 30, 34, 39, 38, 41, 43  Bis Dienstag
# -----------------
# 39 Soundex
# -----------------

import nltk, re
from nltk.corpus import wordnet as wn
from nltk import word_tokenize

representation = {
    1: ['B', 'F', 'P', 'V'],
    2: ['C', 'G', 'J', 'K', 'Q', 'S', 'X', 'Z'],
    3: ['D', 'T'],
    4: ['L'],
    5: ['M', 'N'],
    6: ['R']
}


def soundex(word):
    str_word = str(word)
    output = str_word[0]  # copy first letter

    for letter in str_word[1:]:
        number = replace_consonants(letter)
        if output[-1] != number:
            output += number
    output += '000'
    output = re.sub('#', '', output)
    return output[:4]


def replace_consonants(letter):
    for i, r in enumerate(representation):
        if letter.upper() in representation[i + 1]:
            return str(i + 1)
        elif letter.upper() in 'AEIOU':
            return '#'
    return ''

string = "Robert Ashcraft and Rupert Tymczak and Rubin Pfister"
names = word_tokenize(string)
for name in names:
    print(name, soundex(name))
