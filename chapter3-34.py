# -*- coding: utf-8 -*-
# Aufgaben 6, 7, 20, 21, 24, 30, 34, 39, 38, 41, 43  Bis Dienstag
# -----------------
# 34 adjectives to nouns like canadian -> canada
# -----------------

import nltk
from nltk.corpus import wordnet as wn
user_input = 'canadian'


def nounify(adj_word):
    set_of_related_nouns = set()

    for lemma in wn.lemmas(wn.morphy(adj_word, wn.ADJ), pos="a"):
        for related_form in lemma.derivationally_related_forms():
            for synset in wn.synsets(related_form.name(), pos=wn.NOUN):
                if wn.synset('person.n.01') in synset.closure(lambda s: s.hypernyms()):
                    set_of_related_nouns.add(synset)

    return set_of_related_nouns


print(nounify(user_input))