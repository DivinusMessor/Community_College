"""
Generators and generator expressions.

Project Euler Problem 2:
"By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms."

https://projecteuler.net/problem=2
"""

__author__ = "Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu"

import timeit
import itertools  # Lots of good stuff in here!

CORRECT_RESULT = 4613732


# Generator Function 
# Its a generator because it continues to output after returning a value 
# yield statements return generator objects 
def fibonacci_generator():
  """ Yields an infinite sequence of Fibonacci numbers """
  two_back, one_back, current = 0, 1, 1
  # yield: returns a value, but function continues executing.
  # That's what makes this a generator function!
  # We should demo the next() function in combination with this.
  yield two_back
  yield one_back
  yield current
  while True:  # infinite loop!
    two_back = one_back
    one_back = current
    current = one_back + two_back
    yield current


def even_fibonacci_generator():
  """ Yields an infinite sequence of even Fibonacci numbers """
  two_back, one_back, current = 0, 1, 1
  yield two_back
  while True:
    two_back = one_back
    one_back = current
    current = one_back + two_back
    if not current % 2:
      yield current


#How to deal with infinite sequences using generators 
def iterate_generator():
  """ Iterate the infinite sequence with a for loop and break out when done """
  total = 0
  for fib in fibonacci_generator():
    if fib > 4_000_000:
      break  # Generator object will be garbage-collected after we break out of this loop
    if not fib % 2:
      total += fib
  return total


def iterate_even_generator():
  """ Iterate the infinite sequence with a for loop and break out when done """
  total = 0
  for fib in even_fibonacci_generator():
    if fib > 4_000_000:
      break
    total += fib
  return total


# Takewhile returns elements from the iterable as long as the predicate is true, predicate is a function
# predicate is the first input in the takewhile, this case lambda 
# Because this is a generate sequence it will open get you one value at a time even though
# it is an infinite sequence 
def sum_takewhile():
  """ Use an itertools function meant for this purpose. """
  return sum(
    itertools.takewhile(lambda f: f <= 4_000_000,
                        (f for f in fibonacci_generator() if not f % 2)))


# Needs to be generator because if you use list comprehension you create an infinite loop
# that will crash
def sum_takewhile_even():
  """ Use an itertools function meant for this purpose. """
  return sum(itertools.takewhile(lambda f: f <= 4_000_000, even_fibonacci_generator()))


def while_loop():
  """ Sometimes a straightforward approach is best! """
  previous, current = 0, 1
  total = 0
  while current <= 4_000_000:
    previous, current = current, previous + current
    if not current % 2:
      total += current
  return total


if __name__ == "__main__":
  functions = (iterate_generator, iterate_even_generator, sum_takewhile, sum_takewhile_even,
               while_loop)
  for fun in functions:
    assert fun() == CORRECT_RESULT
    fun_time = timeit.timeit(stmt=f"{fun.__name__}()", globals=globals(), number=100000)
    print(f"{fun.__name__:{max(len(f.__name__) for f in functions)}}\t{fun_time}")