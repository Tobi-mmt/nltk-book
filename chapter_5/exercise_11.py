# -*- coding: utf-8 -*-
# 11, 13, 15, 17, 27, 34, 36, 39, 40, 43

##################
# 11 - Learn about the affix tagger (type help(nltk.AffixTagger)). Train an affix tagger and run it on some new text.
# Experiment with different settings for the affix length and the minimum word length. Discuss your findings.
##################
import nltk
from nltk.corpus import brown

tagged = brown.tagged_sents(categories='news')
gold = brown.tagged_sents(categories='hobbies')
words = brown.words(categories='hobbies')

AffTagger = nltk.AffixTagger(tagged, affix_length=-3, min_stem_length=1)
print(AffTagger.evaluate(gold))
