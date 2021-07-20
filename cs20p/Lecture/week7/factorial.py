"""
The classic recursive factorial example, along with iterative, functional, and standard-library
alternatives.
"""

__author__ = "Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu"

import functools
import math
import operator
import sys
import timeit


def factorial_recursive(n: int) -> int:
  """
  Recursive code is often the easiest to write, and the slowest to run.
  (In a language like Python, anyway.)
  """
  # Base cases: 0! = 1! = 1
  if n < 2:
    return 1
  # Recursive step, guaranteed to proceed toward base case
  return n * factorial_recursive(n - 1)


def factorial_while(n: int) -> int:
  """
  What would be performant in a compiled language (C, C++, Java) is usually pretty slow in Python.
  """
  result = 1
  while 1 < n:
    result *= n
    n -= 1
  return result


def factorial_for(n: int) -> int:
  """
  Straightforward "for term in range" product.
  """
  result = 1
  for factor in range(2, n + 1):
    result *= factor
  return result


def factorial_reduce(n: int) -> int:
  """
  Functional reduction using multiplication as function, range as values, and 1 as initial value.
  """
  return functools.reduce(operator.mul, range(2, n + 1), 1)


if __name__ == '__main__':
  timings = dict()  # We'll keep timing info here to sort and display later.
  for i in range(100):
    for fun in (factorial_for, factorial_while, factorial_recursive, factorial_reduce,
                math.factorial):
      assert fun(i) == math.factorial(i)  # Ensure function works correctly.
      timings[f'{fun.__module__}.{fun.__name__}'] = timeit.timeit(f'fun(i)',
                                                                  globals=globals(), number=1000)
    shortest_time = max(min(timings.values()), sys.float_info.min)
    longest_name_len = max(len(fun_name) for fun_name in timings)
    print('\n'.join(f'{timing[0] + f"({i})":{longest_name_len + 4}} : {timing[1]:.6f}\t'
                    f'(×{timing[1] / shortest_time:.2f})'
                    for timing in sorted(timings.items(), key=lambda item: item[1])), end='\n\n')