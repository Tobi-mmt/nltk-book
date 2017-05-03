# -*- coding: utf-8 -*-
# Aufgaben 6, 7, 20, 21, 24, 30, 34, 39, 38, 41, 43  Bis Dienstag
# -----------------
# 38 split across a line-break.
# -----------------

import nltk, re
from nltk.corpus import wordnet as wn


def remove_line_break(word):
    word_match = re.search(r'\w+-\n\w+', text)
    if word_match.string:
        w_one_liner = str(word.replace('\n', ''))
        w_without_hyphen =str(word.replace('-\n', ''))
        if wn.synsets(w_without_hyphen):
            return w_without_hyphen
        else:
            return w_one_liner

    else:
        return word


text = 'ABCDEFGHIJKLMNO-\nPQRSTUVWXYZ encyclo-\npedia das long-term so ein toler Teil-satz, ich fass \n es gar nicht. deswegen gibt es einen Zeilen-\numbruch!'
output = ''
for word in text.split(' '):
    output += remove_line_break(word) + ' '
print(output)
