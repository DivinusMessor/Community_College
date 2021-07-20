"""
Experimentally timing a O(n) summation algorithm.
"""

__author__ = 'Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu'

import timeit


def manual_sum(data):
  """ Basic linear summation of a list. Note: Should always just use sum() in Python! """
  _sum = 0
  i = 0
  while i < len(data):
    _sum += data[i]
    i += 1
  return _sum


n = 2 ** 10
while n < 2 ** 20:
  _data = list(range(n))
  #testing how long the sum() function takes to run
  python_sum_time = timeit.timeit(stmt=lambda: sum(_data), number=1)
  #test how long the manual_sum() takes to run 
  manual_sum_time = timeit.timeit(stmt=lambda: manual_sum(_data), number=1)
  print(f'n = {n}\tbuilt-in: {python_sum_time:f}\tmanual: {manual_sum_time:f}')
  n *= 2