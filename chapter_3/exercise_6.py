# -*- coding: utf-8 -*-
# Aufgaben 6, 7, 20, 21, 24, 30, 34, 39, 38, 41, 43  Bis Dienstag
# -----------------
# 6 describe regex
# -----------------
import nltk, re

wordlist = nltk.corpus.words.words('en')
print(wordlist)

a = [w for w in wordlist if re.search(r'[a-zA-Z]+', w)]  # alle Wörter mit einem oder mehr Buchstaben, egal ob groß oder klein
b = [w for w in wordlist if re.search(r'[A-Z][a-z]*', w)]  # alle Wörter mit Großbuchstabe am Anfang und 0 bis unendlich kleinen Buchstaben danach
c = [w for w in wordlist if re.search(r'p[aeiou]{,2}t', w)]  # alle Wörter mit Substring, der mit p anfängt und darauf folden 0 bis 2 Umlaute hat und mit t endet
d = [w for w in wordlist if re.search(r'\d+(\.\d+)?', w)]  # alle Zahlen mit und ohne Punkt getrennt
e = [w for w in wordlist if re.search(r'([^aeiou][aeiou][^aeiou])*', w)]  # alle Wörter mit einem Umlaut in der Mitte, OHNE Umlaut davor und mit variabel vielen Nicht-Umlauten danach
f = [w for w in wordlist if re.search(r'\w+|[^\w\s]+', w)]  # Wort oder nicht-white space

print(f)
