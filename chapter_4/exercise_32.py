# -*- coding: utf-8 -*-
# 2, 10, 13, 14, 16, 17, 18, 19, 21, 23, 26, 31, 32, 35
# extra - 27: https://pdfs.semanticscholar.org/3973/ff27eb173412ce532c8684b950f4cd9b0dc8.pdf

##################
# 32 - Develop a simple extractive summarization tool, that prints the sentences of a document which contain
# the highest total word frequency. Use FreqDist() to count word frequencies, and use sum to sum the frequencies
# of the words in each sentence. Rank the sentences according to their score. Finally, print the n highest-scoring
# sentences in document order. Carefully review the design of your program, especially your approach to this
# double sorting. Make sure the program is written as clearly as possible.
##################

from nltk.corpus import brown
import collections
import re

n_common_freq = 10
n_common_sent = 5

text = brown.words(categories='news')
text_sents = brown.sents(categories='news')
freq = collections.Counter(w.lower() for w in text if re.findall(r'\w', w)).most_common(n_common_freq)
freq_words = [w[0] for w in freq]

sent_sum = sorted([(sum(1 for word in sent if word.lower() in freq_words), ' '.join(sent)) for sent in text_sents],
                  reverse=True)[:n_common_sent]
print(sent_sum)
