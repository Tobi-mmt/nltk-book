# -*- coding: utf-8 -*-
# Aufgaben 6, 7, 20, 21, 24, 30, 34, 39, 38, 41, 43  Bis Dienstag
# -----------------
# 24 hAck3r
# -----------------

import nltk, re


def hacker(text):
    text = text.lower()
    hacker_dict = {
        'e': '3',
        'i': '1',
        'o': '0',
        'l': '|',
        's': '5',
        '.': '5w33t!',
        'ate': '8'
    }
    for el in hacker_dict.keys():
        if el is 's':
            text = re.sub(r'^s', '$', text)
        text = text.replace(el, hacker_dict[el])
    return text


user_input = input('Text eingeben: ')
print(hacker(user_input))
