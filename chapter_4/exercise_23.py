# -*- coding: utf-8 -*-
# 2, 10, 13, 14, 16, 17, 18, 19, 21, 23, 26, 31, 32, 35
# extra - 27: https://pdfs.semanticscholar.org/3973/ff27eb173412ce532c8684b950f4cd9b0dc8.pdf

##################
# 23 - Write a recursive function lookup(trie, key) that looks up a key in a trie, and returns the value it finds.
# Extend the function to return a word when it is uniquely determined by its prefix
# (e.g. vanguard is the only word that starts with vang-, so lookup(trie, 'vang') should return the same thing
# as lookup(trie, 'vanguard')).
##################
import pprint


def insert(trie, key, value):
    if key:
        first, rest = key[0], key[1:]
        if first not in trie:
            trie[first] = {}
        insert(trie[first], rest, value)
    else:
        trie['value'] = value


def lookup(trie, key, ori=True):
    if key:
        first, rest = key[0], key[1:]
        if first not in trie:
            return 'no result'
        return lookup(trie[first], rest, ori)
    else:
        if 'value' in trie:
            if ori or ( not ori and len(trie.keys()) == 1):
                return trie['value']
            return 'too many results'
        else:
            if len(trie.keys()) == 1:
                return lookup(trie, next(iter(trie)), ori=False)
            return 'no result'

trie = {}
insert(trie, 'cha', 'cat')
insert(trie, 'charlotte', 'world')
insert(trie, 'head', 'cap')
insert(trie, 'tree', 'leaf')
insert(trie, 'red', 'blue')

trie = dict(trie)
search_key = input('enter search key: ')
print('Result for "{}" is "{}"'.format(search_key, lookup(trie, search_key)))
