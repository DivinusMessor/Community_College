"""
Empirical speed tests of binary search (bisect.bisect_left) vs x in list.
"""

__author__ = 'Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu'

import bisect
import random
import timeit

#bisect is much faster then checking with "in"
def binary_search(data, val):
  """ Uses bisect.bisect_left to perform a binary search """
  return data[bisect.bisect_left(data, val)] == val


#This is a randomly genertted sorted list that we create
n = 2 ** 8
while n <= 2 ** 24:
  _data = sorted(random.randint(0, n) for i in range(n))  # n sorted random integers
  print('{}\t{:f}\t{:f}'.format(n,
                              #checking if some randomly generated number is in the list
                              timeit.timeit(stmt=lambda: random.randint(0, n) in _data,
                                            number=4) / 4,
                              #calling binary search and looking for a randomint
                              timeit.timeit(stmt=lambda: binary_search(_data, random.randint(0, n)),
                                            number=4)  /4))
  n *= 2