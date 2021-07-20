"""
Generators and generator expressions.

Project Euler Problem 1:
"Find the sum of all the multiples of 3 or 5 below 1000."

https://projecteuler.net/problem=1
"""

__author__ = "Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu"

import timeit

CORRECT_RESULT = 233168

# Slowest due to n+=1 everytime it adds a 1 its creates a new object that points to the new value 
def while_loop():
  """ Via a standard while loop. """
  n = 3
  result = 0
  while n < 1000:
    if not n % 3 or not n % 5:
      result += n
    n += 1
  return result


# Better than the top method because it makes the counter already using the range() function and does
# not require creating a new object
def for_loop():
  """ Via a standard for-in-range loop. """
  result = 0
  for n in range(1000):
    if not n % 3 or not n % 5:
      result += n
  return result


# Fastest approach 
def sum_list_comprehension():
  """ Summing a list comprehension. """
  # In this case, list is built with a comprehension, *then* the list is passed to sum().
  # For large lists, or iterative processes that might be cut short, this can be inefficient.
  # This list is small, so it doesn't really matter, and may actually be slightly faster.
  return sum([n for n in range(3, 1000) if not n % 3 or not n % 5])


def sum_generator_expression():
  """ Summing a generator expression. """
  # No list is built. sum() iterates the generator object, which yields one value at a time.
  # Generally this would be preferable to a list comprehension, but here shouldn't matter much.
  return sum(n for n in range(3, 1000) if not n % 3 or not n % 5)


if __name__ == "__main__":
  # Test and time our functions
  functions = while_loop, for_loop, sum_list_comprehension, sum_generator_expression
  for fun in functions:
    assert fun() == CORRECT_RESULT
    fun_time = timeit.timeit(stmt=f"{fun.__name__}()", globals=globals(), number=10000)
    print(f"{fun.__name__:{max(len(f.__name__) for f in functions)}}\t{fun_time}")