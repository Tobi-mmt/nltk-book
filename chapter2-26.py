# -----------------
# 26 - branching factor
# -----------------
from nltk.corpus import wordnet as wn
nouns = wn.all_synsets('n')

hypo_counter = 0
hyper_counter = 0
noun_counter = 0
for noun in nouns:
    hypo_counter += len(noun.hyponyms())
    hyper_counter += len(noun.hypernyms())
    noun_counter += 1
avrg_hypo = hypo_counter / noun_counter
avrg_hyper = hyper_counter / noun_counter

print("In average there are:", avrg_hypo, 'hyponyms and', avrg_hyper, 'hypernyms in', noun_counter, 'noun.')
