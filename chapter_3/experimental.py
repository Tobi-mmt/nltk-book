from bs4 import BeautifulSoup
import nltk, re, pprint
from nltk import word_tokenize

from urllib import request
url = "http://www.gutenberg.org/files/2554/2554.txt"
# response = request.urlopen(url)
# raw = response.read().decode('utf8')
# tokens = word_tokenize(raw)
# text = nltk.Text(tokens)
# text.collocations()
#
# # clean up html with BeautifulSoup
# url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
# html = request.urlopen(url).read().decode('utf8')
#
# raw = BeautifulSoup(html,"html.parser").get_text()
# tokens = word_tokenize(raw)

#############
#  regular expression
#############
wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]
search_terms = [w for w in wordlist if re.search('..j..t..', w)]
# regex rules:
# ^ start of string
# $ end of string
# . single character wildcard
# ? previous character is optional
# + amount of previous character is optional 1 to infinity
# * amount of previous character is optional 0 to infinity
# \ escaping for exp. a dot
# {3,5} number of repeats {from, to}
# (a|b) character on this position is a OR b

# do NOT interpret string - raw string
raw_string = r'\band\b'

datestring = [n for n in re.findall(r'[b-z]+$', 'analaphabet hallo georg')]


raw = """DENNIS: Listen, strange women lying in ponds distributing swords
is no basis for a system of government.  Supreme executive power derives from
a mandate from the masses, not from some farcical aquatic ceremony."""
tokens = word_tokenize(raw)

#########
# stemming
##########
porter = nltk.PorterStemmer()
[porter.stem(t) for t in tokens]

######
# lemmatisation
#########
wnl = nltk.WordNetLemmatizer()
[wnl.lemmatize(t) for t in tokens]

