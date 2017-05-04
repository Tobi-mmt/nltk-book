# -*- coding: utf-8 -*-
import nltk
import re

foo = 'hello'
bar = foo
re.sub(r'e', 'a', foo)
print(bar)

# cut dataset into train and test
text = nltk.corpus.nps_chat.words()
cut = int(0.9 * len(text))
training_data, test_data = text[:cut], text[cut:]

len(training_data) / len(test_data)

# joint tuple to string
word_lens = (5, 'hello'), (4, 'miau')
' '.join(w for (_, w) in word_lens)


##########################
# lists are mutable, while tuples are immutable!!!
#########################

# Python styleguide: http://www.python.org/dev/peps/pep-0008/


# first string in function is accesable with 'help(functionName)'
# example:
def get_text(file):
    """Read text from a file, normalizing whitespace and stripping HTML markup."""
    _text = open(file).read()
    _text = re.sub(r'<.*?>', ' ', _text)
    _text = re.sub('\s+', ' ', _text)
    return _text


# defining conditions for function input
def tag(word):
    assert isinstance(word, basestring), "argument to tag() must be a string"
    if word in ['a', 'the', 'all']:
        return 'det'
    else:
        return 'noun'


def cmp(a, b):  # python3 workaround for cmp in python2
    return (a > b) - (a < b)


sent = ['Take', 'care', 'of', 'the', 'sense', ',', 'and', 'the']
# custom sorting with lambda
sorted(sent, lambda x, y: cmp(len(y), len(x)))


###################
# efficient functions
##################
def search1(substring, words):
    result = []
    for word in words:
        if substring in word:
            result.append(word)
    return result


# this is more efficient, because of the yield statement
def search2(substring, words):
    for word in words:
        if substring in word:
            yield word


#####################
# use memoize to store the call of a function with it's parameters.
# so calling function a second time is just a lookup in memory
from nltk import memoize


@memoize
def virahanka4(n):
    if n == 0:
        return [""]
    elif n == 1:
        return ["S"]
    else:
        s = ["S" + prosody for prosody in virahanka4(n - 1)]
        l = ["L" + prosody for prosody in virahanka4(n - 2)]
        return s + l
