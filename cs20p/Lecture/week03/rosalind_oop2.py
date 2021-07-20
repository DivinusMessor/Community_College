"""
A module containing a hierarchy of classes for Rosalind problems, and/or bioinformatics in general.
"""
from __future__ import annotations  # We're living in the future! Python 3.10 type hints...

__author__ = 'Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu'

import collections
from collections.abc import Mapping, MutableSequence, Sequence
import re


class _Polynucleotide(MutableSequence):
  """
  Represents a mutable sequence of nucleotides.
  This is a base class for specialized classes representing DNA and RNA.
  """

  def __init__(self,
               sequence: _Polynucleotide | Sequence[str] | None,
               complement_map: Mapping[str, str] | None = None):
    """
    Constructs a sequence from another sequence or any suitable other object.

    :param sequence: another sequence, or a sequence containing single-character strings
    :param complement_map: a mapping for complementary bases in this sequence (keys: legal bases)
    """
    # Copy attributes from existing sequence
    if isinstance(sequence, _Polynucleotide):
      self._sequence = sequence._sequence
      self._complement_map = sequence._complement_map
    # Initialize data attributes and validate sequence characters
    else:
      self._sequence = list(sequence) if sequence else []
      self._complement_map = complement_map
      if any(base not in self._complement_map.keys() for base in self._sequence):
        raise ValueError('Invalid characters in sequence')

  def __add__(self, other: _Polynucleotide | Sequence[str]) -> _Polynucleotide:
    """
    Addition implies concatenation.

    :param other: another sequence, or a sequence containing single-character strings
    :return: a new sequence representing concatenation of the two
    """
    # Other sequence is exactly the same type: No need to validate
    if type(self) is type(other):
      return type(self)(self._sequence + other._sequence)  # Instantiate runtime type!
    # Otherwise, convert other sequence to list and let constructor validate
    if isinstance(other, Sequence):
      return type(self)(self._sequence + list(other))
    raise ValueError('Sequences must be of compatible type')

  def __bool__(self) -> bool:
    """
    :return: True if this sequence is non-empty
    """
    return bool(self._sequence)

  def __delitem__(self, loc: int | slice) -> None:
    """
    Deletes the value(s) at an index or a slice of this sequence.

    :param loc: the index or slice to delete
    """
    del self._sequence[loc]

  def __eq__(self, other: _Polynucleotide | Sequence[str]) -> bool:
    """
    Two sequences are equal if they contain the same sequence of nucleotides.

    :param other: another sequence
    :return: whether this sequence is equal to the other
    """
    # If same or subtype, compare by _sequence attribute
    if isinstance(other, type(self)):
      return self._sequence == other._sequence
    # Otherwise, get a list from the sequence and compare
    else:
      return self._sequence == list(other)

  def __getitem__(self, key: slice | int) -> str | _Polynucleotide:
    """
    Supports index and slice syntax. This also makes an object of this type iterable!

    :param key: an index or slice value
    :return: the base at the index, or a new sequence representing a slice of this sequence
    """
    if isinstance(key, slice):
      return type(self)(self._sequence[key])
    else:
      return self._sequence[key]

  def __imul__(self, other: int) -> _Polynucleotide:
    """
    Multiplication implies repeating the sequence some number of times.

    :param other: the number of repeats
    :return: this sequence
    """
    self._sequence *= other
    return self

  def __invert__(self) -> _Polynucleotide:
    """
    Inverting implies complementing.

    :return: the complement of this sequence
    """
    return self.complement()

  def __len__(self) -> int:
    """
    :return: the number of nucleotides in this sequence
    """
    return len(self._sequence)

  def __mul__(self, other: int) -> _Polynucleotide:
    """
    Multiplication implies repeating the sequence some number of times.

    :param other: the number of repeats
    :return: the repeated sequence
    """
    return type(self)(self._sequence * other)

  def __ne__(self, other: _Polynucleotide | Sequence[str]) -> bool:
    """
    Two sequences are not equal if they contain different sequences of nucleotides.

    :param other: another sequence
    :return: whether this sequence is equal to the other
    """
    # If same or subtype, compare by _sequence attribute
    if isinstance(other, type(self)):
      return self._sequence != other._sequence
    # Otherwise, get a list from the sequence and compare
    else:
      return self._sequence != list(other)

  def __neg__(self) -> _Polynucleotide:
    """
    Negating implies complementing.

    :return: the complement of this sequence
    """
    return self.complement()

  def __repr__(self) -> str:
    """
    :return: a printable representation of this sequence, appropriate for eval()
    """
    return f"{self.__module__}.{type(self).__name__}('{self}')"

  def __setitem__(self, key: slice | int, value) -> None:
    """
    Supports index/slice-based assignment.

    :param key: an index or a slice of this sequence
    :param value: another sequence or nucleotide to replace the slice or index
    :return: this sequence, as modified
    """
    if isinstance(key, slice):
      if any(base not in self._complement_map.keys() for base in value):
        raise ValueError('Invalid character for seq')
      self._sequence[key] = value
    elif isinstance(value, type(self)):
      self._sequence = self._sequence[:key] + value._sequence + self._sequence[key + 1:]
    else:
      if value not in self._complement_map.keys():
        raise ValueError('Invalid character for seq')
      self._sequence[key] = value

  def __str__(self) -> str:
    """
    :return: a string representation consisting of this sequence's nucleotides
    """
    return ''.join(self._sequence)

  def insert(self, index: int, value: str) -> None:
    """
    Insert an item at a given position. The first argument is the index of the element before which
    to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is
    equivalent to a.append(x).

    :param index: the position at which to insert
    :param value: the value to insert (must be a legal character for this sequence)
    :raise ValueError if the value is illegal
    """
    if value not in self._complement_map.keys():
      raise ValueError('Attempt to insert illegal character')
    self._sequence.insert(index, value)

  def complement(self, index: int | None = None) -> _Polynucleotide | None:
    """
    Returns a complementary sequence, or complements the nucleotide at a specific index.

    :param index: the base to complement
    :return: a complementary sequence of the same type, or None if an index was specified
    """
    if index is None:
      return type(self)(self._complement_map[base] for base in self._sequence)
    else:
      self._sequence[index] = self._complement_map[self._sequence[index]]

  def nucleotide_counts(self) -> Mapping[str, int]:
    """
    :return: a dict approximating the output expected for Rosalind DNA.
    """
    return dict(collections.Counter(self._sequence))

  def hamming_distance(self, other: _Polynucleotide | Sequence[str]) -> int:
    """
    Calculates the Hamming distance between two sequences of the same length (Rosalind HAMM).

    :param other: the other sequence (must be same length)
    :return: the Hamming distance between this sequence and the other
    """
    if len(self) != len(other):
      raise ValueError('Sequences must be of same length')
    return sum(1 for (this_nt, other_nt) in zip(self._sequence, other) if this_nt != other_nt)

  def motif_positions(self, motif: _Polynucleotide | str) -> Sequence[int]:
    """
    All locations of a motif within this sequence (Rosalind SUBS).

    :param motif: the motif to search for
    :return: a tuple containing all indexes at which the motif is found in this sequence
    """
    return tuple(match.start() for match in re.finditer(f'(?={motif})', str(self)))  # Fancy regex!


class Dna(_Polynucleotide):
  """ Represents a mutable DNA sequence. """

  def __init__(self, dna: Sequence[str] | None = None):
    """
    Constructs a DNA sequence.

    :param dna: a sequence containing single-character strings in 'ACGT'
    :raises: ValueError if dna is invalid
    """
    super().__init__(sequence=dna,
                     complement_map={
                       'A': 'T',
                       'T': 'A',
                       'C': 'G',
                       'G': 'C'
                     })

  def gc_content(self) -> float:
    """
    :return: the GC-content of this sequence
    """
    return sum(1 for base in self._sequence if base in 'GC') / len(self)

  def transcribe(self) -> Rna:
    """
    :return: this sequence transcribed to RNA
    """
    return Rna('U' if base == 'T' else base for base in self._sequence)


class Rna(_Polynucleotide):
  """ Represents a mutable RNA sequence. """

  def __init__(self, rna: Sequence[str] | None = None):
    """
    Constructs a RNA sequence.

    :param rna: a sequence containing single-character strings in 'ACGU'
    :raises: ValueError if rna is invalid
    """
    super().__init__(sequence=rna,
                     complement_map={
                       'A': 'U',
                       'U': 'A',
                       'C': 'G',
                       'G': 'C'
                     })

  def dna(self) -> Dna:
    """
    Generates and returns the DNA sequence from which this RNA would have been transcribed.

    :return: the DNA sequence corresponding to this RNA
    """
    return Dna('T' if base == 'U' else base for base in self._sequence)