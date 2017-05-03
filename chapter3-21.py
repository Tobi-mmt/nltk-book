# -*- coding: utf-8 -*-
# Aufgaben 6, 7, 20, 21, 24, 30, 34, 39, 38, 41, 43  Bis Dienstag
# -----------------
# 21 website extraction
# -----------------
from bs4 import BeautifulSoup
import nltk, re
from urllib import request


def unknown(url):
    response = request.urlopen(url)
    raw = response.read().decode('utf8')
    raw_clean = BeautifulSoup(raw, "html.parser")
    for script in raw_clean(["script", "style"]):
        script.decompose()  # clean from script and style tags
    raw_clean = raw_clean.get_text()
    tokens = nltk.word_tokenize(raw_clean)
    raw_list = [w for w in tokens if re.search('^\w+$', w)]
    known_words = nltk.corpus.words.words()
    unknown_words = [w.lower() for w in raw_list if w not in known_words]
    return set(unknown_words)

user_iput = input('Website eingeben, z.B. haribo.de: ')
url = "http://www." + user_iput

words = unknown(url)
print('{} Unbekannt Worte auf der Website {}: {}.'.format(len(words), user_iput, words))
