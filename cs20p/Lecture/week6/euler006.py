"""
Generators and generator expressions.

Project Euler Problem 6:
"Find the difference between the sum of the squares of the first one hundred natural numbers and
the square of the sum."

https://projecteuler.net/problem=6
"""

__author__ = "Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu"

import timeit

CORRECT_RESULT = 25164150


def while_loops():
  square_of_sums = 0
  sum_of_squares = 0
  x = 1
  while x < 101:
    square_of_sums += x
    sum_of_squares += x**2
    x += 1
  square_of_sums **= 2
  return square_of_sums - sum_of_squares


def for_loops():
  square_of_sums = 0
  sum_of_squares = 0
  for x in range(1, 101):
    square_of_sums += x
    sum_of_squares += x**2
  square_of_sums **= 2
  return square_of_sums - sum_of_squares


# If you change the x*x to x^2 then it will be much slower 
def generator_expressions():
  return sum(x for x in range(1, 101))**2 - sum(x * x for x in range(1, 101))


def list_comprehensions():
  return sum([x for x in range(1, 101)])**2 - sum([x * x for x in range(1, 101)])


if __name__ == "__main__":
  functions = while_loops, for_loops, generator_expressions, list_comprehensions
  for fun in functions:
    assert fun() == CORRECT_RESULT
    fun_time = timeit.timeit(stmt=f"{fun.__name__}()", globals=globals(), number=100000)
    print(f"{fun.__name__:{max(len(f.__name__) for f in functions)}}\t{fun_time}")