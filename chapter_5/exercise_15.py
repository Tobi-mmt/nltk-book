# -*- coding: utf-8 -*-
# 11, 13, 15, 17, 27, 34, 36, 39, 40, 43

##################
# 15 - Write programs to process the Brown Corpus and find answers to the following questions:

# Which nouns are more common in their plural form, rather than their singular form?
# (Only consider regular plurals, formed with the -s suffix.)
# Which word has the greatest number of distinct tags. What are they, and what do they represent?
# List tags in order of decreasing frequency. What do the 20 most frequent tags represent?
# Which tags are nouns most commonly found after? What do these tags represent?

##################
import nltk
from nltk.corpus import brown


tagged = brown.tagged_words()
freq_nn = nltk.FreqDist(w for w, t in tagged if t == 'NN').most_common()
freq_nns = nltk.FreqDist(w for w, t in tagged if t == 'NNS')


for nn, nn_num in freq_nn:
    nns_num = freq_nns.get(nn+'s')
    if nns_num and nns_num >= nn_num:
        print('{} - NN: {} NNS: {}'.format(nn, nn_num, nns_num))


print(freq_nns)
