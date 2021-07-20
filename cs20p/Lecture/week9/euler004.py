"""
Generators and generator expressions.

Project Euler Problem 4:
"Find the largest palindrome made from the product of two 3-digit numbers."

https://projecteuler.net/problem=4
"""

__author__ = "Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu"

import decorators
from itertools import product

CORRECT_RESULT = 906609


@decorators.log
@decorators.timeit
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


# Without the decorator, we here would have to then explicitly shadow the function:
# while_loop = decorators.timeit(while_loop)


@decorators.log
@decorators.timeit
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


@decorators.log
@decorators.timeit
def generator_expression():
  """ Shorter but slower. """
  return max(
      a * b for a in range(100, 1000) for b in range(100, 1000) if str(a * b) == str(a * b)[::-1])


@decorators.log
@decorators.timeit
def itertools_product():
  """ Shorter but slower. """
  return max(a * b
             for (a, b) in product(range(100, 1000), range(100, 1000))
             if str(a * b) == str(a * b)[::-1])


if __name__ == "__main__":
  functions = while_loop, for_loop, generator_expression, itertools_product
  timings = []
  for fun in functions:
    fun_time, result = fun()
    assert result == CORRECT_RESULT
    timings.append((fun_time, fun.__name__))
  timings.sort()
  for fun_time, fun_name in timings:
    print(f"{fun_name:{max(len(f.__name__) for f in functions)}}\t{fun_time}")