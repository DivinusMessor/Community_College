#!/usr/bin/env python3.9
"""
Testing the speed of str.count vs. manually iterating a string via Rosalind DNA (again).

Remember: chmod +x str_count_timing.py

Try e.g.
./str_count_timing.py </srv/datasets/chromosome4
./str_count_timing.py 100 </srv/datasets/nasuia-deltocephalinicola
"""
__author__ = 'Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu'

import sys
import timeit
from collections.abc import Iterable


def rosalind_dna_iterative(dna: Iterable[str]) -> tuple[int, int, int, int]:
  """
  Counts the DNA bases in an iterable object.

  Args:
    dna: An iterable object expected to contain single-character strings (e.g. str).

  Returns:
    A tuple[int, int, int, int] containing the number of 'A', 'C', 'G', and 'T' strings in dna.
  """
  a_count = 0
  c_count = 0
  g_count = 0
  t_count = 0
  for base in dna:
    if base == 'A':
      a_count += 1
    elif base == 'C':
      c_count += 1
    elif base == 'G':
      g_count += 1
    elif base == 'T':
      t_count += 1
  return (a_count, c_count, g_count, t_count)


def rosalind_dna_str_count(dna: str) -> tuple[int, int, int, int]:
  """
  Counts the DNA bases in a DNA string.

  Args:
    dna: A DNA string

  Returns:
    A tuple[int, int, int, int] containing the number of 'A', 'C', 'G', and 'T' strings in dna.
  """
  return (dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T'))


if __name__ == '__main__':
  test_dna = sys.stdin.read()
  repeats = 1 if len(sys.argv) < 2 else int(sys.argv[1])  # Conditional expression
  # lambda?! We'll talk about this later...
  iterative_time = timeit.timeit(lambda: rosalind_dna_iterative(test_dna), number=repeats)
  str_count_time = timeit.timeit(lambda: rosalind_dna_str_count(test_dna), number=repeats)
  # Multi-line f-string
  print(f'''Iterative time: {iterative_time}
str.count time: {str_count_time}
Ratio: {iterative_time / str_count_time:.2f}''')