"""
Module hash_practice defines three classes that take strategic advantage of hashability.
See: https://docs.python.org/3/glossary.html#term-hashable
"""

__author__ = 'Yukio Rivera, ysrivera@jeff.cis.cabrillo.edu'

import itertools  # For testing


class UnorderedTuple(tuple):
  """ A subclass of tuple that reports hash and equality without regard to order of elements. """

  def __eq__(self, other: tuple):
    """ An UnorderedTuple is equal to any other tuple containing the same elements in any order. """
    return hash(self) == hash(other)

  def __hash__(self):
    """ An UnorderedTuple's hash is calculating without regard to order of the tuple elements. """
    if not self:
      return 0
    wd = sorted(self)
    wd = tuple(wd)
    h_wd = hash(wd)
    return h_wd

  def __repr__(self) -> str:
    """ Returns a string that would result in reproducing this object when interpreted. """
    return f"{type(self).__name__}(({','.join(str(i) for i in self)}))"


class UnorderedString(str):
  """ A subclass of str that reports hash and equality without regard to order of characters. """

  def __eq__(self, other: str):
    """ An UnorderedString is equal to any other str containing the same elements in any order. """
    return set(self) == set(other)

  def __hash__(self):
    """ An UnorderedString's hash is calculated without regard to order of the characters. """
    if not self:
      return 0
    wd = sorted(self)
    wd = tuple(wd)
    h_wd = hash(wd)
    return h_wd

  def __repr__(self) -> str:
    """ Returns a string that would result in reproducing this object when interpreted. """
    return f"{type(self).__name__}('{self}')"


# Helper code for loading monoisotopic mass data
def _load_masses():
  """ Returns a dictionary mapping amino-acid characters to monoisotopic masses. """
  ret = dict()
  with open('/srv/datasets/amino-monoisotopic-mass') as mass_file:
    for line in mass_file:
      tokens = line.split()
      amino_acid = tokens[0]
      mass = float(tokens[1])
      ret[amino_acid] = mass
  return ret


class Protein(str):
  """ Represents an immutable sequence of amino acids. """

  _monoisotopic_masses = _load_masses()

  def __new__(cls, aminos=''):
    """
    Produces a str object if the given sequence of amino-acid characters is valid.

    This overriding of __new__() is the preferred way of subclassing an immutable type.
    This gives us an opportunity to add logic to the construction of a new object of this type.
    See: https://docs.python.org/3/reference/datamodel.html#object.__new__

    :param aminos: A sequence of single-character strings, expected to be in the amino-acid alphabet
    :raise: ValueError if aminos contains characters not found in the amino-acid alphabet
    """
    # This works and you can leve it alone, but I suggest looking up what it does!
    if aminos and any(char not in Protein._monoisotopic_masses for char in aminos):
      raise ValueError(
          'Invalid amino acid character: '
          f'{next(char for char in aminos if char not in Protein._monoisotopic_masses)}')
    return str.__new__(cls, aminos)

  def __hash__(self) -> int:
    """
    A Protein's hash is equivalent to a str object containing the same character sequence.
    """
    if not self:
      return 0
    h_wd = hash(self.__str__())
    return h_wd

  def __repr__(self) -> str:
    """ Returns a string that would result in reproducing this object when interpreted. """
    return f"{type(self).__name__}('{self}')"

  def mass(self) -> float:
    """
    Returns the mass of this protein (in Daltons), according to the monoisotopic mass table.
    See: http://rosalind.info/problems/prtm/
    """
    return sum(Protein._monoisotopic_masses[amino] for amino in self)


# Some assertion-based tests for these classes
if __name__ == '__main__':
  all_unordered_tuples = set()
  for permutation in itertools.permutations(list(range(5))):
    unordered = UnorderedTuple(permutation)
    assert unordered == tuple(range(5))  # Test UnorderedTuple.__eq__()
    all_unordered_tuples.add(unordered)
  assert len(all_unordered_tuples) == 1  # Test UnorderedTupe.__hash__()

  all_unordered_strings = set()
  for permutation in itertools.permutations('banana'):
    unordered = UnorderedString(''.join(permutation))
    assert unordered == 'banana'  # Test UnorderedString.__eq__()
    all_unordered_strings.add(unordered)
  assert len(all_unordered_strings) == 1  # Test UnorderedString.__hash__()

  demo_protein_str = 'MENEHQYSGARCSGQAAYVAKRQECAK'
  protein = Protein(demo_protein_str)
  assert abs(protein.mass() - 2996.34396) < 1e-6  # Test Protein.mass()

  many_proteins = set()
  demo_protein_strings = [line.strip() for line in open('/srv/datasets/ebola_orf_products')]
  for insertion_round in range(10):
    for demo_protein_str in demo_protein_strings:
      protein = Protein(demo_protein_str.strip())
      # Test Protein.__repr__()
      eval_repr_result = eval(repr(protein))
      assert isinstance(eval_repr_result, Protein)
      assert hash(protein) == hash(demo_protein_str)  # Test Protein.__hash__()
      many_proteins.add(protein)
  assert len(many_proteins) == len(demo_protein_strings)
