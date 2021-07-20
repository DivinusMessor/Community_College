"""
Experimentally timing a O(n^2) summation algorithm.
"""

__author__ = 'Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu'

import timeit


def manual_sum(data):
  """ Quadratic summation of all 2-tuples from a list """
  """ Program Could be written 
  sum(i * j for i in data for j in data)
  """
  _sum = 0
  i = 0
  while i < len(data):
    j = 0
    while j < len(data):
      _sum += data[i] * data[j]
      j += 1
    i += 1
  return _sum


n = 2 ** 10
while n < 2 ** 20:
  _data = list(range(n))
  python_sum_time = timeit.timeit(stmt=lambda: sum(i * j for i in _data for j in _data), number=1)
  manual_sum_time = timeit.timeit(stmt=lambda: manual_sum(_data), number=1)
  print(f'n = {n}\tbuilt-in: {python_sum_time:f}\tmanual: {manual_sum_time:f}')
  n *= 2