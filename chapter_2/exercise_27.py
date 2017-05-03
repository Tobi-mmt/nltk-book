# -----------------
# 27 - word sense
# -----------------
from nltk.corpus import wordnet as wn
part_of_speeches = ['n', 'v', 'a', 'r']


def average_polysemy(part_of_speech):
    synset_counter = 0
    word_count = 0
    synsets = wn.all_synsets(part_of_speech)
    for word_syn in synsets:
        for word in word_syn.lemma_names():
            # word = word_syn.name().split('.')[0]
            synset_counter += len(wn.synsets(word, part_of_speech))
            word_count += 1
    return synset_counter / word_count

avrg = {}
for v in part_of_speeches:
    avrg[v] = average_polysemy(v)

print(avrg)
