# -----------------
# 24 - text generator
# -----------------
import nltk
import collections
import re
import random
from nltk.corpus import brown


def random_word_of_n_common(text, n):
    words = collections.Counter(w.lower() for w in text if re.match('(\w+)', w)).most_common(n)
    randi = random.choice(words)[0]
    print("Random Word:", randi)
    return randi


def generate_model(text):
    bigrams = nltk.bigrams(text)
    cfdist = nltk.ConditionalFreqDist(bigrams)
    word = random_word_of_n_common(cfdist, 3)
    print("--------- output ---------")
    for i in range(20):
        print(word, end=' ')
        word = cfdist[word].max()


def random_corpus():
    category = random.choice(brown.categories())
    print("Category:", category)
    return brown.words(categories=category)

corpus = random_corpus()
corpus += random_corpus()
generate_model(corpus)

