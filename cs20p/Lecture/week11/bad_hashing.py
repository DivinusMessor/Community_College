"""
If you want your own types to be hashable, your best bet is to use a pre-existing hash function!
"""
__author__ = 'Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu'

import random

words_list = open('/srv/datasets/many-english-words.txt').read().lower().split()


class SillyString(str):

  def __hash__(self):
    return 0  # We could/should ...

  def __eq__(self, other):
    return True  # ... play around with these

  def __repr__(self):
    escaped_apostrophes = str(self).replace("'", r"\'")
    return f"SillyString('{escaped_apostrophes}')"

  def __str__(self):
    return ''.join(c.lower() if random.random() < .5 else c.upper() for c in self)


regular_set = set(words_list)
silly_set = set(SillyString(word) for word in words_list)
