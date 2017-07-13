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

# 1 Which nouns are more common in their plural form, rather than their singular form?
tagged = brown.tagged_words()
# freq_nn = nltk.FreqDist(w for w, t in tagged if t == 'NN').most_common()
# freq_nns = nltk.FreqDist(w for w, t in tagged if t == 'NNS')
#
#
# for nn, nn_num in freq_nn:
#     nns_num = freq_nns.get(nn+'s')
#     if nns_num and nns_num >= nn_num:
#         print('{} - NN: {} NNS: {}'.format(nn, nn_num, nns_num))



# 2 Which word has the greatest number of distinct tags. What are they, and what do they represent?

# cfdist = nltk.ConditionalFreqDist(set(tagged))
#
# word_with_most_tags = sorted(((w[0], len(cfdist[w[0]].most_common())) for w in set(tagged)), key=lambda x: x[1], reverse=True)[0]
# print(cfdist[word_with_most_tags[0]].most_common())

# 3 List tags in order of decreasing frequency. What do the 20 most frequent tags represent?

cfdist = nltk.FreqDist(t for w, t in tagged)
#print(cfdist.most_common(20))

# 4 Which tags are nouns most commonly found after? What do these tags represent?
#prev_nn = nltk.FreqDist([tagged[i][1] for i, (w, t) in enumerate(tagged) if t == 'NN' and i >0])
print([tagged[int(i-1)][1] for i, (w, t) in enumerate(tagged) if t == 'NN'])
print(tagged[552103])


