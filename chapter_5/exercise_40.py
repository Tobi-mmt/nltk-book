# -*- coding: utf-8 -*-
# 11, 13, 15, 17, 27, 34, 36, 39, 40, 43

##################
# 40 - Inspect the diagnostic files created by the Brill tagger rules.out and errors.out.
# Obtain the demonstration code by accessing the source code (at http://www.nltk.org/code) and create your own
# version of the Brill tagger. Delete some of the rule templates, based on what you learned from inspecting rules.out.
# Add some new rule templates which employ contexts that might help to correct the errors you saw in errors.out.
##################
import nltk
from nltk.corpus import brown

brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')

tagger = nltk.tag.brill.nltkdemo18()
print(tagger)
