#!/usr/bin/env python3
"""
Empirical speed tests for:
  x in list
  Binary search (bisect.bisect_left)
  x in set
  x in frozenset
"""

__author__ = 'Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu'

import bisect
import random
import timeit

#checking the growth rate using different data tytpes 
def binary_search(data, val):
  """ Uses bisect.bisect_left to perform a binary search """
  return data[bisect.bisect_left(data, val)] == val


n = 2**8
repeats = 4
while n <= 2**24:
  data_sorted = sorted(random.randint(0, n) for i in range(n))
  data_set = set(data_sorted)
  data_frozenset = frozenset(data_sorted)
  time_list_in = timeit.timeit(stmt=lambda: random.randint(0, n) in data_sorted,
                               number=repeats) / repeats
  time_bisect = timeit.timeit(stmt=lambda: binary_search(data_sorted, random.randint(0, n)),
                              number=repeats) / repeats
  time_set_in = timeit.timeit(stmt=lambda: random.randint(0, n) in data_set,
                              number=repeats) / repeats
  time_frozenset_in = timeit.timeit(stmt=lambda: random.randint(0, n) in data_frozenset,
                                    number=repeats) / repeats
  print(f'{n}\t' + '\t'.join(
      format(time, 'f') for time in (time_list_in, time_bisect, time_set_in, time_frozenset_in)))
  n *= 2