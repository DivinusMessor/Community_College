"""
Given: A DNA string s

of length at most 1000 nt.

Return: Four integers (separated by spaces) counting 
the respective number of times that the 
symbols 'A', 'C', 'G', and 'T' occur in s.
"""

#Where does the input come from?
#Read from standard input

import sys

adenine = 0
cytosine = 0
guanine = 0
thymine = 0

for line in sys.stdin:
  adenine += line.count('A')
  cytosine += line.count('C')
  guanine += line.count('G')
  thymine += line.count('T')

print(f'{adenine} {cytosine} {guanine} {thymine}')
