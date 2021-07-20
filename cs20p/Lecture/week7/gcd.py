"""
The classic recursive Euclidean GCD example, alongside iterative and library alternatives.
"""

__author__ = "Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu"

import math
import time


def euclidean_recursive(a: int, b: int) -> int:
  """
  Recursive code is often the easiest to write.
  It's also often the slowest to run.
  """
  if a > b:
    a, b = b, a  # Ensure a ≤ b
  return b if not a else euclidean_recursive(b % a, a)


def euclidean_iterative(a: int, b: int) -> int:
  """
  It's not difficult to write a straightforward iterative solution.
  Again, in C/C++/Java this would be /very/ fast. In Python, well...
  """
  if a > b:
    a, b = b, a  # Ensure a ≤ b
  while a:
    a, b = b % a, a
  return b


if __name__ == '__main__':
  timings = dict()  # We'll keep timing info here to sort and display later.
  for fun in (euclidean_recursive, euclidean_iterative, math.gcd):
    before = time.time()
    for x in range(500):
      for y in range(500):
        ret = fun(x, y)
    after = time.time()
    assert fun(x, y) == math.gcd(x, y)  # Ensure function works correctly.
    timings[f'{fun.__module__}.{fun.__name__}'] = after - before
  longest_name_len = max(len(fun_name) for fun_name in timings)
  shortest_time = min(timings.values())
  print('\n'.join(f'{timing[0]:{longest_name_len}} : {timing[1]}\t'
                  f'(×{timing[1] / shortest_time:.2f})'
                  for timing in sorted(timings.items(), key=lambda item: item[1])))