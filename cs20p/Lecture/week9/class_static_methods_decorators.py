"""
Class/static methods via decorators.
"""
__author__ = "Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu"


class Dna:
  """ The ol' standby: A DNA sequence. """
  _complements = {"A": "T", "T": "A", "C": "G", "G": "C"}

  def __init__(self, sequence):
    self._sequence = list(filter(lambda c: c in Dna._complements, sequence))

  def __repr__(self):
    return f"Dna('{self}')"

  def __str__(self):
    return "".join(self._sequence)

  def reverse_complement(self):
    return Dna(map(Dna._complements.__getitem__, reversed(self._sequence)))

  @staticmethod
  def from_file_path(file_path):
    """ Factory method to produce a Dna object with the contents of a file at the given path. """
    return Dna(open(file_path).read())

  @staticmethod
  def from_file_object(file_object):
    """ Factory method to produce a Dna object with the contents of a file object. """
    return Dna(file_object.read())