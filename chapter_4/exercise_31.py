# -*- coding: utf-8 -*-
# 2, 10, 13, 14, 16, 17, 18, 19, 21, 23, 26, 31, 32, 35
# extra - 27: https://pdfs.semanticscholar.org/3973/ff27eb173412ce532c8684b950f4cd9b0dc8.pdf

##################
# 31 - Obtain some raw text, in the form of a single, long string. Use Python's textwrap module to break it up
# into multiple lines. Now write code to add extra spaces between words, in order to justify the output.
# Each line must have the same width, and spaces must be approximately evenly distributed across each line.
# No line can begin or end with a space.
##################
import textwrap


def fill_space(sent, n, rec=0):
    diff = n - len(sent)
    filled = sent.replace(' ', '  ', diff)
    return filled if len(filled) == n else fill_space(filled, n, rec + 1)


text = '''Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth. Even the all-powerful Pointing has no control about the blind texts it is an almost unorthographic life One day however a small line of blind text by the name of Lorem Ipsum decided to leave for the far World of Grammar. The Big Oxmox advised her not to do so, because there were thousands of bad Commas, wild Question Marks and devious Semikoli, but the Little Blind Text didn’t listen. She packed her seven versalia, put her initial into the belt and made herself on the way. When she reached the first hills of the Italic Mountains, she had a last view back on the skyline of her hometown Bookmarksgrove, the headline of Alphabet Village and the subline of her own road, the Line Lane.'''
text_wrap = textwrap.wrap(text, width=40)
text_max = len(max(text_wrap, key=len))
text_output = [fill_space(sent, text_max) for sent in text_wrap]
print([(w, len(w)) for w in text_output])
