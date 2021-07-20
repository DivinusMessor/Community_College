#!/usr/bin/env python3.9
"""
Demonstrating assertions to test our object-oriented approach to some Rosalind problems.

See: https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement
"""

__author__ = 'Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu'

from rosalind_oop import DnaSequence, RnaSequence

test_string = 'GATTACA'

dna = DnaSequence(test_string)
assert str(dna) == test_string

nucleotides = []
for base in dna:
  nucleotides.append(base)
assert nucleotides == list(test_string)

assert dna + dna == test_string + test_string

transcribed = dna.transcribe()
assert transcribed == test_string.translate({ord('T'): ord('U')})
assert transcribed == RnaSequence(test_string.translate({ord('T'): ord('U')}))