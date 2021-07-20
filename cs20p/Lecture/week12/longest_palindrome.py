#!/usr/bin/env python3
"""
Various approaches to finding the longest palindrome.
Note: Not all are guaranteed to break ties in the same way.

Try testing with lots of data, e.g. /srv/datasets/many-english-words.txt
"""

__author__ = "Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu"

import functools
import re
import sys
import timeit


def procedural_naive(words):
  """
    Not functional programming: Straightworward loops, if statements, assignments
    """
  longest_pal = None
  for word in words:
    lower_word = word.lower()
    if lower_word == lower_word[::-1] and (not longest_pal or len(lower_word) > len(longest_pal)):
      longest_pal = word
  return longest_pal


def filter_max(words):
  """
    Functional programming:
    1. Filter words to get only palindromes
       (Assignment expression avoids having to call .lower() on each word twice.)
    2. Call max, telling it to use len() as a key

    See: https://www.python.org/dev/peps/pep-0572/
    See: https://docs.python.org/3/whatsnew/3.8.html#assignment-expressions
    """
  return max(filter(lambda word: (word := word.lower()) == word[::-1], words), key=len)


def filter_map_sorted(words):
  """
    Functional programming:
    1. Filter words to get only palindromes
    2. Map those palindromes to tuples: (len(palindrome), palindrome))
    3. Sort those tuples
    4. Longest palindrome is second element of last tuple
    """
  return sorted(
      map(
          lambda word: (len(word), word),
          filter(lambda word: (word := word.lower()) == word[::-1], words),
      ))[-1][1]


def filter_map_reduce(words):
  """
    Functional programming:
    1. Filter words to get only palindromes
    2. Map those palindromes to tuples: (len(palindrome), palindrome))
    3. Sort those tuples
    4. Longest palindrome is second element of last tuple
    """
  return functools.reduce(
      lambda a, b: a if a > b else b,
      map(
          lambda word: (len(word), word),
          filter(lambda word: (word := word.lower()) == word[::-1], words),
      ),
  )[1]


def max_generator_expression(words):
  """
    Functional programming via generator expression:
    1. Use a generator expression to generate all palindromes
    2. Call max, telling it to use len() as a key
    """
  return max((word for word in words if (lower_word := word.lower()) == lower_word[::-1]), key=len)


def max_list_comprehension(words):
  """
    Functional programming via generator expression:
    1. Use a list comprehension to produce all palindromes
    2. Call max, telling it to use len() as a key
    """
  return max((word for word in words if (lower_word := word.lower()) == lower_word[::-1]), key=len)


if __name__ == "__main__":
  # Break input into words (see: https://docs.python.org/3/library/re.html)
  all_words = re.split(r"\W+", sys.stdin.read())
  number = 10 if len(sys.argv) < 2 else int(sys.argv[1])
  print(f"Testing each function {number} time(s) each. Input contains {len(all_words)} words.")
  return_values = set()
  timings = []
  functions = (
      procedural_naive,
      filter_max,
      filter_map_sorted,
      filter_map_reduce,
      max_generator_expression,
      max_list_comprehension,
  )
  for fun in functions:
    duration = timeit.timeit(stmt=f"return_values.add({fun.__name__}(all_words))",
                             globals=globals(),
                             number=number)
    timings.append((duration, fun.__name__))
  print(return_values)
  assert len(set(len(pal) for pal in return_values)) == 1
  for duration, fun_name in sorted(timings):
    print(f"{fun_name:{max(len(fun.__name__) for fun in functions)}} : {duration:.15f}")