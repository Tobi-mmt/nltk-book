# -----------------
# 28 - similarity
# -----------------
import nltk
from nltk.corpus import wordnet as wn

word_pairs = ['car-automobile', 'gem-jewel', 'journey-voyage', 'boy-lad', 'coast-shore', 'asylum-madhouse', 'magician-wizard', 'midday-noon', 'furnace-stove', 'food-fruit', 'bird-cock', 'bird-crane', 'tool-implement', 'brother-monk', 'lad-brother', 'crane-implement', 'journey-car', 'monk-oracle', 'cemetery-woodland', 'food-rooster', 'coast-hill', 'forest-graveyard', 'shore-woodland', 'monk-slave', 'coast-forest', 'lad-wizard', 'chord-smile', 'glass-magician', 'rooster-voyage', 'noon-string']

pair_score = []
for word_pair in word_pairs:
    word_arr = word_pair.split('-')
    word1 = wn.synsets(word_arr[0])[0]
    word2 = wn.synsets(word_arr[1])[0]
    pair_score.append((word_pair, word1.path_similarity(word2)))

print(sorted(pair_score, key=lambda pair: pair[1], reverse=True))   # sort by score value