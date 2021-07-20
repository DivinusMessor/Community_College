"""
Project Euler Problem 9: Various approaches

https://projecteuler.net/problem=9

  A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
  For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
  There exists exactly one Pythagorean triplet for which a + b + c = 1000.
  Find the product abc.
"""

__author__ = "Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu"

import numpy
import timeit

CORRECT_RESULT = 31875000


def nested_for():
  """ Standard approach with nested for loops """
  for a in range(1, 996):  # a < b
    for b in range(a + 1, 997):  # b < c
      c = 1000 - a - b  # a + b + c == 1000
      if a**2 + b**2 == c**2:
        return a * b * c


def nested_for_numpy():
  """ Nested for loops w/ NumPy. """
  for a in numpy.arange(1, 996):  # a < b
    for b in numpy.arange(a + 1, 997):  # b < c
      c = 1000 - a - b  # a + b + c == 1000
      if a**2 + b**2 == c**2:
        return a * b * c


def generator_next():
  """ Generator expression passed to next()—we know there can be only one solution. """
  return next(a * b * (1000 - a - b)
              for a in range(1, 996)
              for b in range(a + 1, 997)
              if a**2 + b**2 == (1000 - a - b)**2 and a + b + (1000 - a - b) == 1000)


def generator_next_numpy():
  """ Generator expression w/ numpy.arange. """
  return next(a * b * (1000 - a - b)
              for a in numpy.arange(1, 996)
              for b in numpy.arange(a + 1, 997)
              if a**2 + b**2 == (1000 - a - b)**2 and a + b + (1000 - a - b) == 1000)


if __name__ == "__main__":
  functions = nested_for, nested_for_numpy, generator_next, generator_next_numpy
  for fun in functions:
    assert fun() == CORRECT_RESULT
    fun_time = timeit.timeit(stmt=f"{fun.__name__}()", globals=globals(), number=10)
    print(f"{fun.__name__:{max(len(f.__name__) for f in functions)}}\t{fun_time}")