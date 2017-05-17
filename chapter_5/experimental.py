import nltk
from nltk import word_tokenize

text = word_tokenize("And now for something completely different")
# tag words with part-of-speech tag
print(nltk.pos_tag(text))
# print the meaning of the shortcut
nltk.help.upenn_tagset('RB')
# homonyms (word with multiple meanings) are listed twice
text = word_tokenize("They refuse to permit us to obtain the refuse permit")
print(nltk.pos_tag(text))


# default dict for accessing an undefined key
from collections import defaultdict
frequency = defaultdict(int)
frequency['colorless'] = 4
print(frequency['ideas'])  # -> 0
