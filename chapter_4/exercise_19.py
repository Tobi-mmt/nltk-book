# -*- coding: utf-8 -*-
# 2, 10, 13, 14, 16, 17, 18, 19, 21, 23, 26, 31, 32, 35
# extra - 27: https://pdfs.semanticscholar.org/3973/ff27eb173412ce532c8684b950f4cd9b0dc8.pdf

##################
# 19 - Write a list comprehension that sorts a list of WordNet synsets for proximity to a given synset.
# For example, given the synsets minke_whale.n.01, orca.n.01, novel.n.01, and tortoise.n.01, sort them
# according to their shortest_path_distance() from right_whale.n.01.
##################

from nltk.corpus import wordnet as wn

synset = wn.synset('right_whale.n.01')
synsets = [wn.synset('minke_whale.n.01'), wn.synset('orca.n.01'), wn.synset('novel.n.01'), wn.synset('tortoise.n.01')]

sorted_synsets = sorted(((w, w.shortest_path_distance(synset)) for w in synsets), key=lambda w: w[1])

print(sorted_synsets)
