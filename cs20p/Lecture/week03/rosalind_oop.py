"""
A module containing classes that represent mutable Pythonic nucleic-acid sequences.
"""
from __future__ import annotations  # We're living in the future! Python 3.10 type hints...

__author__ = 'Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu'

import collections
import re
from typing import Dict, Iterable, Mapping, Tuple


class _NucleicAcidSequence:
  """
  Represents a mutable nucleic acid sequence.
  To be subclassed by specific DNA and RNA sequence classes.
  """

  def __init__(self,
               sequence: _NucleicAcidSequence | Iterable[str] | None,
               complement_map: Mapping[str, str] | None = None):
    """
    Constructs a sequence from another sequence or any suitable other object.

    :param sequence: another sequence, or an iterable object yielding single-character strings
    :param complement_map: a mapping for complementary bases in this sequence (keys: legal bases)
    """
    # Copy attributes from existing sequence
    if isinstance(sequence, _NucleicAcidSequence):
      self._sequence = sequence._sequence
      self._complement_map = sequence._complement_map
    # Initialize data attributes and validate sequence characters
    else:
      self._sequence = list(sequence) if sequence else []
      self._complement_map = complement_map
      if any(base not in self._complement_map.keys() for base in self._sequence):  # Built-in any()!
        raise ValueError('Invalid characters in sequence')

  def __add__(self, other: _NucleicAcidSequence | Iterable[str]) -> _NucleicAcidSequence:
    """
    Addition implies concatenation.

    :param other: another sequence, or an iterable object yielding single-character strings
    :return: a new sequence representing concatenation of the two
    """
    # Other sequence is exactly the same type: No need to validate
    if type(self) is type(other):
      return type(self)(self._sequence + other._sequence)  # Instantiate runtime type!
    # Otherwise, convert other iterable object to list and let constructor validate
    if isinstance(other, Iterable):
      return type(self)(self._sequence + list(other))
    raise ValueError('Sequences must be of compatible type')

  def __bool__(self) -> bool:
    """
    :return: True if this sequence is non-empty
    """
    return bool(self._sequence)

  def __eq__(self, other: _NucleicAcidSequence | Iterable[str]) -> bool:
    """
    Two sequences are equal if they containing the same sequence of nucleotides.

    :param other: another sequence
    :return: whether this sequence is equal to the other
    """
    # If same or subtype, compare by _sequence attribute
    if isinstance(other, type(self)):
      return self._sequence == other._sequence
    # Otherwise, get a list from the iterable object and compare
    else:
      return self._sequence == list(other)

  def __getitem__(self, key: slice | int) -> str | _NucleicAcidSequence:
    """
    Supports index and slice syntax. This also makes a sequence iterable!

    :param key: an index or slice value
    :return: the base at the index, or a new sequence representing a slice of this sequence
    """
    if isinstance(key, slice):
      return type(self)(self._sequence[key])
    else:
      return self._sequence[key]

  def __iadd__(self, other: _NucleicAcidSequence | Iterable[str]) -> _NucleicAcidSequence:
    """
    Compound addition-assignment (this_sequence += other) implies concatenation.

    :param other: the other sequence to add
    :return: this sequence
    """
    if type(self) is type(other):
      self._sequence += other._sequence
    elif isinstance(other, Iterable):
      if any(base not in self._complement_map.keys() for base in other):
        raise ValueError('Invalid characters in sequence')
      self._sequence += list(other)
    else:
      raise ValueError('Sequences must be of compatible type')

    return self

  def __imul__(self, other: int) -> _NucleicAcidSequence:
    """
    Multiplication implies repeating the sequence some number of times.

    :param other: the number of repeats
    :return: this sequence
    """
    self._sequence *= other

  def __invert__(self) -> _NucleicAcidSequence:
    """
    :return: the complement of this sequence
    """
    return self.complement()

  def __len__(self) -> int:
    """
    :return: the number of nucleotides in this sequence
    """
    return len(self._sequence)

  def __mul__(self, other: int) -> _NucleicAcidSequence:
    """
    Multiplication implies repeating the sequence some number of times.

    :param other: the number of repeats
    :return: the repeated sequence
    """
    return type(self)(self._sequence * other)

  def __neg__(self) -> _NucleicAcidSequence:
    """
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
        raise ValueError('Invalid character for sequence')
      self._sequence[key] = value
    elif isinstance(value, type(self)):
      self._sequence = self._sequence[:key] + value._sequence[::] + self._sequence[key:]
    else:
      if value not in self._complement_map.keys():
        raise ValueError('Invalid character for sequence')
      self._sequence[key] = value

  def __str__(self) -> str:
    """
    :return: a string representation consisting of this sequence's nucleotides
    """
    return ''.join(self._sequence)

  def complement(self, index: int | None = None) -> _NucleicAcidSequence | None:
    """
    Returns a complementary sequence, or complements the nucleotide at a specific index.

    :param index: the base to complement
    :return: a complementary sequence of the same type, or None if an index was specified
    """
    if index is None:
      return type(self)(self._complement_map[base] for base in self._sequence)
    else:
      self._sequence[index] = self._complement_map[self._sequence[index]]

  def nucleotide_counts(self) -> Dict[str, int]:
    """
    :return: a dict approximating the output expected for Rosalind DNA.
    """
    return dict(collections.Counter(self._sequence))

  def hamming_distance(self, other: _NucleicAcidSequence | Iterable[str]) -> int:
    """
    Calculates the Hamming distance between two sequences of the same length (Rosalind HAMM).

    :param other: the other sequence (must be same length)
    :return: the Hamming distance between this sequence and the other
    """
    if len(self) != len(other):
      raise ValueError('Sequences must be of same length')
    return sum(1 for (this_nt, other_nt) in zip(self._sequence, other) if this_nt != other_nt)

  def motif_positions(self, motif: _NucleicAcidSequence | str) -> Tuple[int]:
    """
    All locations of a motif within this sequence (Rosalind SUBS).

    :param motif: the motif to search for
    :return: the indexes at which the motif is found in this sequence
    """
    return tuple(match.start() for match in re.finditer(f'(?={motif})', str(self)))  # Fancy regex!


class DnaSequence(_NucleicAcidSequence):
  """ Represents a mutable DNA sequence. """

  def __init__(self, dna: Iterable[str] | None = None):
    """
    Constructs a DNA sequence.

    :param dna: an iterable object containing single-character strings in 'ACGT'
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

  def transcribe(self) -> RnaSequence:
    """
    :return: this sequence transcribed to RNA
    """
    return RnaSequence('U' if base == 'T' else base for base in self._sequence)


class RnaSequence(_NucleicAcidSequence):
  """ Represents a mutable RNA sequence. """

  def __init__(self, rna: Iterable[str] | None = None):
    """
    Constructs a RNA sequence.

    :param rna: an iterable object containing single-character strings in 'ACGU'
    :raises: ValueError if rna is invalid
    """
    super().__init__(sequence=rna,
                     complement_map={
                       'A': 'U',
                       'U': 'A',
                       'C': 'G',
                       'G': 'C'
                     })

  def un_transcribe(self) -> DnaSequence:
    """
    :return: the DNA sequence equivalent to this one.
    """
    return DnaSequence('T' if base == 'U' else base for base in self._sequence)

  # And then we might start adding protein-related methods/classes