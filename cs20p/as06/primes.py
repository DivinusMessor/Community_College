"""
A module demonstrating generator functions and related concepts.
"""

__author__ = "Yukio Rivera for CS 20P, ysrivera.bergamini@cabrillo.edu"

from collections.abc import Callable, Iterator


def elements_under(sequence: Iterator[int], bound: int, predicate: Callable[[int], bool] = None) \
    -> Iterator[int]:
  """
  Yields a finite sequence of elements under a given bound, optionally matching a predicate.

  :param sequence: an infinite sequence of integers, e.g. primes()
  :param bound:  an exclusive upper bound for the yielded sequence
  :param predicate: includes only elements from the sequence for which this function returns True
  """
  for i in sequence:
    if i < bound:
      if not predicate:
        yield i
      # What if there is no predicate?
      elif predicate(i):
        yield i
    else:
      return StopIteration


def is_prime(n: int) -> bool:
  """ Returns whether n is prime. """
  # If 1 or 0 return false, not prime
  return prime_factors(n)[0] == n


def nth_element(sequence: Iterator[int], n: int) -> int:
  """
  Returns the nth element of a possibly infinite sequence of integers.

  :param sequence: a sequence of integers, e.g. primes()
  :param n: the sequence index desired
  :return: the value at index n of the sequence
  """
  gen_list = []
  for i in sequence:
    gen_list.append(i)
    if len(gen_list) == n + 1:
      return gen_list[n]


def primes() -> Iterator[int]:
  """ Yields an infinite sequence of prime numbers. """
  prime = 2
  # Infinite loop
  while True:
    # Using function to check for primes
    if is_prime(prime):
      yield prime
    prime += 2 if prime > 2 else 1


def prime_factors(n: int) -> list[int]:
  """ Returns a list of prime numbers with product n, in ascending order. """
  counter = 2
  prim_fac = []
  while counter <= n:
    # Checks to see if n is divisable by a prime
    if (n % counter) == 0:
      # If it is then counter is a prime so add to list and
      # increment to next number
      prim_fac.append(counter)
      n = n / counter
    else:
      # No prime was found so increase counter to next number
      counter += 1
  return prim_fac


def semiprimes() -> Iterator[int]:
  """ Yields an infinite sequence of semiprimes. """
  # start at 4, first semi prime, then you check if the number is a prime
  x = 4
  while x:
    check = prime_factors(x)
    if len(check) == 2:
      yield x
    x += 1
