"""
Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces)
counting the respective number of times that
the symbols 'A', 'C', 'G', and 'T' occur in s.
"""

# Where does the input come from?
# Standard input!

import sys

adenine = 0
cytosine = 0
guanine = 0
thymine = 0

for letter in sys.stdin.read():
  if letter == 'A':
    adenine += 1
  elif letter == 'C':
    cytosine += 1
  elif letter == 'G':
    guanine += 1
  elif letter == 'T':
    thymine += 1

print(f'{adenine} {cytosine} {guanine} {thymine}')