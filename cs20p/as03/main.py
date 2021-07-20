#!/usr/bin/env python3.9
from rosalind import Dna, Rna, Protein



if __name__ == '__main__':
  protein = Protein("MAMAMA")
  print(protein)
  print(protein + protein)
  del protein[0]
  print(protein)
  dna = Dna("ATGATG")
  print(dna == protein)