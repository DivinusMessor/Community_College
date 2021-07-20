"""
Generators and generator expressions.

Project Euler Problem 4:
"Find the largest palindrome made from the product of two 3-digit numbers."

https://projecteuler.net/problem=4
"""

__author__ = "Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu"

import timeit
from itertools import product

CORRECT_RESULT = 906609


def while_loop():
  """ Straightforward brute-force solution """
  largest = 0
  i = 100
  while i < 1000:
    j = 100
    while j < 1000:
      n = i * j
      nstr = str(n)
      if nstr == nstr[::-1] and n > largest:
        largest = n
      j += 1
    i += 1
  return largest


def for_loop():
  """ Straightforward brute-force solution """
  largest = 0
  for a in range(100, 1000):
    for b in range(100, 1000):
      n = a * b
      nstr = str(a * b)
      if nstr == nstr[::-1] and n > largest:
        largest = n
  return largest


def generator_expression():
  """ Shorter but slower. """
  return max(
      a * b for a in range(100, 1000) for b in range(100, 1000) if str(a * b) == str(a * b)[::-1])


# Intertools product will return the cartesian product 
def itertools_product():
  """ Shorter but slower. """
  return max(a * b
             for (a, b) in product(range(100, 1000), range(100, 1000))
             if str(a * b) == str(a * b)[::-1])


if __name__ == "__main__":
  functions = while_loop, for_loop, generator_expression, itertools_product
  for fun in functions:
    assert fun() == CORRECT_RESULT
    fun_time = timeit.timeit(stmt=f"{fun.__name__}()", globals=globals(), number=2)
    print(f"{fun.__name__:{max(len(f.__name__) for f in functions)}}\t{fun_time}")