# -----------------
# 23 Zipf's Law
# -----------------
import nltk
def plot_word_dist(corpus):
    cfd = nltk.FreqDist(word.lower() for word in corpus)
    cfd.plot()

# a large text
from nltk.book import *
corpus = text6
book_name = corpus.name

plot_word_dist(corpus)

# b random text
import random
randi_string = ""
for i in range(0, 99999):
    randi_string += random.choice("abcdefg ")
print(randi_string)
string_token = randi_string.split(" ")
plot_word_dist(string_token)
