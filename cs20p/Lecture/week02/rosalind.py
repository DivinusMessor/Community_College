"""
Implements various Rosalind problems as functions.
"""
__author__ = 'Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu'


def dna(dna_str: str) -> dict[str, int]:
  """
  Counts the bases in a DNA string.

  Args:
    dna_str: A DNA string (expected to contain A/C/G/T characters).

  Returns:
    A dict[str, int] where the keys are DNA bases in 'ACGT', and the values are the base counts.
  """
  # Straightforward version:
  return {
      'A': dna_str.count('A'),
      'C': dna_str.count('C'),
      'G': dna_str.count('G'),
      'T': dna_str.count('T')
  }
  # Using a dict comprehension:
  # return {base: dna_str.count(base) for base in 'ACGT'}


def rna(dna_str: str) -> str:
  """
  Returns an RNA string transcribed from a DNA string.

  Args:
    dna_str: A DNA string (expected to contain A/C/G/T characters).

  Returns:
    The transcribed RNA string of dna_str.
  """
  return dna_str.replace('T', 'U')


def revc(dna_str: str) -> str:
  """
  Returns the reverse complement of a DNA string.

  Args:
    dna_str: A DNA string (expected to contain A/C/G/T characters).

  Returns:
    The reverse complement of dna_str.
  """
  # Using str.translate and string slicing
  return dna_str.translate({
      ord('A'): ord('T'),
      ord('T'): ord('A'),
      ord('C'): ord('G'),
      ord('G'): ord('C')
  })[::-1]


def hamm(dna_1: str, dna_2: str) -> int:
  """
  Calculates and returns the Hamming distance between two DNA strings.

  Args:
    dna_1: A DNA string (expected to contain A/C/G/T characters).
    dna_2: A DNA string (expected to contain A/C/G/T characters).

  Returns:
    The Hamming distance between dna_1 and dna_2.
  """
  # Straightforward version
  hamming_distance = 0
  for i in range(len(dna_1)):
    if dna_1[i] != dna_2[i]:
      hamming_distance += 1
  return hamming_distance
  # Using sum with a generator expression and zip()
  # return sum(1 for (a, b) in zip(dna_1, dna_2) if a != b)