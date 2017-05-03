import nltk

# from nltk.book import *

# fdist5 = FreqDist(text5)
# print(sorted(w for w in set(text5) if len(w) > 7 and fdist5[w] > 7))

# print(text4.collocations())
# fdist = FreqDist(len(w) for w in text1)
# print(fdist.most_common())
# fdist.plot(len(fdist))

# print(sorted(w for w in text5 if w.startswith('b')))

# print(set(sent3) < set(text1))

# #################################
# ##########  chapter 2 ###########
# #################################

# from nltk.corpus import gutenberg
# print(nltk.corpus.gutenberg.words('austen-emma.txt'))
#
#
# for fileid in gutenberg.fileids():
#     num_chars = len(gutenberg.raw(fileid))
#     num_words = len(gutenberg.words(fileid))
#     num_sents = len(gutenberg.sents(fileid))
#     num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
#     print(round(num_chars / num_words), round(num_words / num_sents), round(num_words / num_vocab), fileid)

# print(gutenberg.sents('shakespeare-macbeth.txt'))
# from nltk.corpus import webtext
# for fileid in webtext.fileids():
#     print(fileid, webtext.raw(fileid)[:565], '...')

# from nltk.corpus import brown
# days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# genres = ['news', 'romance']
#
# cfd = nltk.ConditionalFreqDist(
#     (genre, day)
#     for genre in genres
#     for w in brown.words(categories=genre)
#     for day in days
#     if w.lower().startswith(day.lower()))
#
# cfd.tabulate(conditions=genres, samples=days)


# get meaning of word pairs with bigrams
# from nltk.book import *
#
#
# def generate_model(cfdist, word, num=15):
#     for i in range(num):
#         print(word, end=' ')
#         word = cfdist[word].max()
#
# text = text7
# bigrams = nltk.bigrams(text)
# cfd = nltk.ConditionalFreqDist(bigrams)
# print(generate_model(cfd, 'cash'))

# stopwords
# from nltk.corpus import stopwords
# print(stopwords.words('german'))


# names
# names = nltk.corpus.names
# male_names = names.words('male.txt')
# female_names = names.words('female.txt')


# # synonyms
# from nltk.corpus import wordnet as wn
# # find a synonym-st for motocar
# print(wn.synsets('motorcar'))
# # print synonym set of car
# print(wn.synset('car.n.01').lemma_names())
# # definition
# wn.synset('car.n.01').definition()
# # get all lemmas
# wn.lemmas('car')
# # dinge, die Teil des Baumes sind
# wn.synset('tree.n.01').part_meronyms()
# # Dinge, zu denen ein Baum dazu gehört
# wn.synset('tree.n.01').member_holonyms()
# # walk verursacht step
# wn.synset('walk.v.01').entailments()
#
# # semantische Ähnlichkeit
# right = wn.synset('right_whale.n.01')
# minke = wn.synset('minke_whale.n.01')
# right.lowest_common_hypernyms(minke)
# # >>> [Synset('baleen_whale.n.01')]
# # ähnlihckeit von 0 - 1
# right.path_similarity(minke)
# # mehr Ähnlichkeitswrte mit
# help(wn)

# #################################
# ###### Exercises chapter 2 ######
# #################################

# -----------------
# 2
# from nltk.corpus import gutenberg
# print('words: ', len(nltk.corpus.gutenberg.words('austen-persuasion.txt')))
# print('word types: ', len(set(nltk.corpus.gutenberg.words('austen-persuasion.txt'))))

# -----------------
# 3
# print(nltk.corpus.brown.words(categories='news'))

# -----------------
# 4
# fileids = nltk.corpus.state_union.fileids()
# targets = ['men', 'women', 'people']
#
# plot = nltk.ConditionalFreqDist(
#     (id, target)
#     for id in fileids
#     for word in nltk.corpus.state_union.words(fileids=id)
#     for target in targets
#     if target in word
# )
# plot.plot()

# -----------------
# 5
# -----------------
# from nltk.corpus import wordnet as wn
# word = 'penis'
# synset = wn.synsets(word)[0]
# print('member_meronyms: ', synset.member_meronyms())
# print('part_meronyms: ', synset.part_meronyms())
# print('substance_meronyms: ', synset.substance_meronyms())
# print('member_holonyms: ', synset.member_holonyms())
# print('part_holonyms: ', synset.part_holonyms())
# print('substance_holonyms: ', synset.substance_holonyms())

# -----------------
# 7
# -----------------

# from nltk.corpus import brown
# print(nltk.Text(brown.words()).concordance('hello'))

# -----------------
# 8
# -----------------
# import nltk
# names = nltk.corpus.names
#
# plot = nltk.ConditionalFreqDist(
#     (gender, name[0])
#     for gender in names.fileids()
#     for name in names.words(fileids=gender)
# )
# plot.plot()

# -----------------
# 9 - bedeutung von Wörtern vergleichen
#  -----------------
import nltk
# from nltk import sent_tokenize, word_tokenize
# from nltk.book import *
# from nltk.corpus import stopwords
# text_1 = text1
# text_2 = text2
#
#
# set_1 = set(word.lower() for word in text_1)
# set_2 = set(word.lower() for word in text_2)
#
# intersect = set(stopwords.words('english')) - set_1.intersection(set_2)
#
# sent_1 = sent_tokenize(' '.join(text_1))
# sent_2 = sent_tokenize(' '.join(text_2))
#
#
# book_dict = dict()
# for set_word in intersect:
#     book_dict[set_word] = []
#     for sent in sent_1:


