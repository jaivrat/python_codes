#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 18:54:52 2020

@author: jvsingh
"""

#@decorate
def target():
    print('running target()')


def my_decorate(f):
    print("Decorating with mydecorate")
    return(f)
    
#target = my_decorate(target)

#target()


def deco(func):
    def inner():
        print('running inner()')
    return inner

@deco
def target():
    print('running target()')
    

target()



class Foo:
    def __getitem__(self, pos):
        return range(0, 30, 10)[pos]




from random import shuffle


import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck2(collections.MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
    
    def __setitem__(self, position, value): #
        self._cards[position] = value

    def __delitem__(self, position): #
        del self._cards[position]

    def insert(self, position, value): #
        self._cards.insert(position, value
                           


import decimal

ctx = decimal.getcontext()






def __add__(self, other):
    try:
        pairs = itertools.zip_longest(self, other, fillvalue=0.0)
        return Vector(a + b for a, b in pairs)
    except TypeError:
        return NotImplemented











import re
import reprlib
RE_WORD = re.compile('\w+')

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
    
    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)



s = Sentence('"The time has come," the Walrus said,')


for word in s:
    print(word)


class Foo:
    def __iter__(self):
        pass



s = 'ABC'







class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
    
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word
        return


class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self


















