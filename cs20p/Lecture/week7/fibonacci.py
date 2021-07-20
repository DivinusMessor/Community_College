"""
The classic recursive Fibonacci sequence example, along with iterative, functional,
and standard-library alternatives.
"""

__author__ = "Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu"

import math
import sys
import timeit


def fibonacci_recursive(n: int) -> int:
  """
  Recursive code is often the easiest to write, and the slowest to run.
  Fibonacci sequence is a classic ill-suited case for recursion.
  (Two recursive calls in every recursive step. Function calls O(n!))
  """
  # Base cases: 0, 1 are the first two Fibonacci numbers
  if n < 2:
    return n
  # Recursive step: fib(n) = fib(n - 1) + fib(n - 2)
  return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_while(n: int) -> int:
  """ Sometimes a straightforward approach is best! """
  if n < 2:
    return n
  prev, current = 1, 1
  while n > 2:
    prev, current = current, prev + current
    n -= 1
  return current


def fibonacci_closed_form(n: int) -> int:
  """
  A closed-form solution to an infinite sequence can often be useful.
  https://mathworld.wolfram.com/BinetsFibonacciNumberFormula.html
  """
  return int(((1 + math.sqrt(5)) ** n - (1 - math.sqrt(5)) ** n) / (2 ** n * math.sqrt(5)))


def fibonacci_memoized(n: int, memos=dict()) -> int:
  """
  Recursive code is often the easiest to write, and the slowest to run.
  Fibonacci sequence is a classic ill-suited case for recursion.
  (Number of function calls grows exponentially.)
  """
  if n < 2:
    return n
  elif n in memos:
    return memos[n]
  ret = fibonacci_memoized(n - 1, memos) + fibonacci_memoized(n - 2, memos)
  memos[n] = ret
  return ret


if __name__ == '__main__':
  for i in range(40):
    results = set()  # Keep all results here to ensure functions work correctly.
    timings = dict()  # We'll keep timing info here to sort and display later.
    for fun in (fibonacci_recursive, fibonacci_while, fibonacci_closed_form, fibonacci_memoized):
      timings[f'{fun.__module__}.{fun.__name__}'] = timeit.timeit(f'results.add(fun(i))',
                                                                  globals=globals(), number=1)
    assert len(results) == 1  # All functions should return the same value.
    shortest_time = max(min(timings.values()), sys.float_info.min)
    longest_name_len = max(len(fun_name) for fun_name in timings)
    print('\n'.join(f'{timing[0] + f"({i})":{longest_name_len + 4}} : {timing[1]:.6f}\t'
                    f'(×{timing[1] / shortest_time:.2f})'
                    for timing in sorted(timings.items(), key=lambda item: item[1])), end='\n\n')