#!/usr/bin/env python3.9
"""
Acts as a shell for interactively calling functions in the rosalind module.
"""
__author__ = 'Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu'

import rosalind

if __name__ == '__main__':
  while True:
    try:
      command = input('🧬 ')
    except EOFError:
      break
    tokens = command.split()
    if not tokens:
      continue
    result = 'Invalid command'
    if tokens[0] == 'dna':
      if tokens[1].startswith('<'):
        with open(tokens[1].split('<')[1]) as in_file:
          result = rosalind.dna(in_file.read())
      else:
        result = rosalind.dna(tokens[1])
    elif tokens[0] == 'rna':
      if tokens[1].startswith('<'):
        with open(tokens[1].split('<')[1]) as in_file:
          result = rosalind.rna(in_file.read())
      else:
        result = rosalind.rna(tokens[1])
    elif tokens[0] == 'revc':
      if tokens[1].startswith('<'):
        with open(tokens[1].split('<')[1]) as in_file:
          result = rosalind.revc(in_file.read())
      else:
        result = rosalind.revc(tokens[1])
    elif tokens[0] == 'hamm':
      result = rosalind.hamm(tokens[1], tokens[2])
    print(result)