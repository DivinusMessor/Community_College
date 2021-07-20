"""
Generators and generator expressions.

Project Euler Problem 5:
"What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"

https://projecteuler.net/problem=5
"""

__author__ = "Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu"

import math
import timeit

CORRECT_RESULT = 232792560


def for_gcd():
  """ Clever solution! """
  # Build a product of:
  # 1 * 1/GCD(1, 1) * 2/GCD(2, 1/GCD(1, 1)), 3/GCD(3, 1/GCD(1, 1) * 2/GCD(2, 1/GCD(1, 1))), etc.
  # 1 * (1 // 1) * (2 // 1) * (3 // 1) * (4 // 2) * (5 // 1) * (6 // 6) * (7 // 1) * (8 // 4) * ...
  result = 1
  for factor in range(1, 21):
    result *= factor // math.gcd(factor, result)
  return result


def generator_expression():
  """ This one works, but will be fairly slow. Brute-forcing this problem is inefficient. """
  # next() will stop the first time the generator yields a value (which will be the smallest)
  return next(x for x in range(20, 10**20, 20) if all(not x % n for n in range(2, 20)))


def list_comprehension():
  """ This one is bad news! Building this entire list will be time-prohibitive... """
  return next([x for x in range(20, 10**20, 20) if all(not x % n for n in range(2, 20))])


if __name__ == "__main__":
  functions = for_gcd, generator_expression  # , list_comprehension
  for fun in functions:
    assert fun() == CORRECT_RESULT
    fun_time = timeit.timeit(stmt=f"{fun.__name__}()", globals=globals(), number=1)
    print(f"{fun.__name__:{max(len(f.__name__) for f in functions)}}\t{fun_time}")