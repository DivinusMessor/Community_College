"""
All permutations of a set.
"""

__author__ = "Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu"

import itertools
import math


def set_permutations(set_values: set) -> set[tuple]:
  """
  Returns all permutations of a set, as a set of tuples.
  There's no point in measuring this one's speed, but let's analyze the approach at least.
  """
  # Base case
  if not set_values:
    return {()}
  # Recursive step. This amount of work will grow quickly!
  all_permutations = set()
  for item in set_values:
    all_permutations.update({(item,) + p for p in set_permutations(set_values - {item})})
  return all_permutations


if __name__ == '__main__':
  for i in range(11):
    itertools_result = sorted(tuple(itertools.permutations(set(range(i)))))
    our_result = sorted(set_permutations(set(range(i))))
    assert itertools_result == our_result
    assert len(our_result) == math.factorial(i)  # !
    print(f'range({i}) (len {len(our_result)}): {our_result[:10]}'
          f' {"..." if len(our_result) > 10 else ""}')