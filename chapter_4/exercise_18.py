# -*- coding: utf-8 -*-
# 2, 10, 13, 14, 16, 17, 18, 19, 21, 23, 26, 31, 32, 35
# extra - 27: https://pdfs.semanticscholar.org/3973/ff27eb173412ce532c8684b950f4cd9b0dc8.pdf

##################
# 18 - Write code to print out an index for a lexicon, allowing someone to look up words according to their meanings
# (or pronunciations; whatever properties are contained in lexical entries).
##################


def insert(trie, key, value):
    if key:
        first, rest = key[0], key[1:]
        if first not in trie:
            trie[first] = {}
        insert(trie[first], rest, value)
    else:
        trie['value'] = value


def lookup(trie, key):
    if key:
        first, rest = key[0], key[1:]
        if first not in trie:
            return 'no result'
        return lookup(trie[first], rest)
    else:
        return trie['value']

trie = {}
insert(trie, 'chat', 'Conversation, particularly casual.')
insert(trie, 'hello', 'Hello is a salutation or greeting in the English language.')
insert(trie, 'head', 'A head is the part of an organism which usually includes the eyes, ears, nose and mouth, each of which aid in various sensory functions such as sight, hearing, smell, and taste.')
insert(trie, 'tree', 'In botany, a tree is a perennial plant with an elongated stem, or trunk, supporting branches and leaves in most species')
insert(trie, 'red', 'Red is the color at the longer-wavelengths end of the spectrum of visible light next to orange, at the opposite end from violet.')

trie = dict(trie)
print(trie)
search_key = input('enter search key: ')
print('Definition of "{}": {}'.format(search_key, lookup(trie, search_key)))