#!/usr/bin/env python3.9
"""
Approximates some of the wc utility (counting lines, words, and bytes), e.g.:
  wc <wc.py
  wc *.py
  wc /srv/datasets/shakespeare*
"""
__author__ = 'Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu'

import sys
from typing import TextIO


def count_tokens(file: TextIO) -> dict[str, int]:
  """
  Returns a count of lines, words and bytes in a file object

  Args:
      file: The file from which to read.

  Returns:
    A dict with keys 'lines', 'words', and 'bytes' mapping to those counts from the file.
  """
  num_lines = 0
  num_words = 0
  num_bytes = 0
  for line in file:
    num_lines += 1
    num_words += len(line.split())
    num_bytes += len(line.encode('utf-8'))
  return {'lines': num_lines, 'words': num_words, 'bytes': num_bytes}


if __name__ == '__main__':
  results = []
  # stdin mode: Only read from standard input
  if len(sys.argv) < 2:
    results.append(count_tokens(sys.stdin))
  # File mode: Read from all command-line argument file paths
  else:
    for file_path in sys.argv[1:]:
      try:
        with open(file_path) as input_file:
          results.append(count_tokens(input_file))
      except Exception:
        results.append(f'{sys.argv[0]}: {file_path}: {sys.exc_info()[1].strerror}')
  if len(results) == 1:
    result = results[0]
    fmt = f'-{max(len(str(count)) for count in result.values())}d'
    print(f"{result['lines']:{fmt}} {result['words']:{fmt}} {result['bytes']:{fmt}}")
  else:
    totals = {'lines': 0, 'words': 0, 'bytes': 0}
    number_lengths = set()
    for result in results:
      if not isinstance(result, str):
        for key in 'lines', 'words', 'bytes':
          number_lengths.add(len(str(result[key])))
    fmt = f'-{max(number_lengths)}d'
    for file_path, result in zip(sys.argv[1:], results):
      if isinstance(result, str):
        print(result, file=sys.stderr)
      else:
        print(
            f"{result['lines']:{fmt}} {result['words']:{fmt}} {result['bytes']:{fmt}} {file_path}")
        for key in 'lines', 'words', 'bytes':
          totals[key] += result[key]
    print(f"{totals['lines']:{fmt}} {totals['words']:{fmt}} {totals['bytes']:{fmt}} total")