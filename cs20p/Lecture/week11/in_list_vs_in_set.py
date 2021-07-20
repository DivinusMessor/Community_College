#!/usr/bin/env python3
"""
Experimental timings of list.__contains__(), tuple.__contains__(), and set.__contains__() via "in".
"""
__author__ = 'Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu'

import bisect
import sys
import timeit

# list, tuple, and set versions of all the words in a large spell-checking dictionary file
words_list = open('/srv/datasets/many-english-words.txt').read().lower().split()
words_tuple = tuple(words_list)
words_set = set(words_list)

# One word that doesn't exist in the dictionary, one near the beginning, one near the end
words = '!@#$%^&*()_+', 'apple', 'yellow'
collections = 'words_list', 'words_tuple', 'words_set'

# Time how long it takes to search for each word in each collection via "in"
for word in words:
  for collection in collections:
    timing = timeit.timeit(stmt=f'"{word}" in {collection}', globals=globals(), number=500)
    print(f'"{word}" in {collection:>{max(len(c) for c in collections)}} : {timing:.15f}')
  print()

# Inspect size of each collection via sys.getsizeof():
for c_name, c_obj in zip(collections, (words_list, words_tuple, words_set)):
  print(f'sys.getsizeof({c_name})\t{sys.getsizeof(c_obj)}')
print()

# Quick binary search example to compare "x in set" against "bisect.bisect_left(list, val)"
set_time = timeit.timeit(stmt=f'"{words[0]}" in words_set', globals=globals(), number=1000000)
bisect_left_time = timeit.timeit(stmt=f'bisect.bisect_left(words_list, "{words[0]}")',
                                 globals=globals(),
                                 number=1000000)
print(f'''"{words[0]}" in words_set : {set_time:15f}
bisect.bisect_left(words_list, "{words[0]}") : {bisect_left_time:15f}
''')

