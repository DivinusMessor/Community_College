"""
Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces)
counting the respective number of times that
the symbols 'A', 'C', 'G', and 'T' occur in s.
"""

# Where does the input come from?
# Standard input!

import collections
import sys

counts = collections.Counter(sys.stdin.read())
print(' '.join(str(counts[base]) for base in 'ACGT'))