"""
Yukio Rivera
CS20P: Assigment_01 - Computing GC Content

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the
GC-content of that string. Rosalind allows for a default error of 0.001 in
all decimal answers unless otherwise stated;
"""

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

try:
    total = adenine + cytosine + guanine + thymine
    gc_count = guanine + cytosine
    gc_perct = (gc_count / total) * 100
    print(round(gc_perct, 6))

except ZeroDivisionError:
    print(0)
