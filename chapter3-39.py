# -*- coding: utf-8 -*-
# Aufgaben 6, 7, 20, 21, 24, 30, 34, 39, 38, 41, 43  Bis Dienstag
# -----------------
# 39 Soundex
# -----------------

import re
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
    output = str_word[0].upper()

    for letter in str_word[1:]:
        number = replace_consonants(letter)
        if output[-1] != number:
            output += number

    first_in_dict = replace_consonants(str_word[0])
    if str(first_in_dict) in '123456':
        output = output[0] + output[2:] if output[1] == str(first_in_dict) else output
    output += '000'
    output = re.sub(r'#', '', output)
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
