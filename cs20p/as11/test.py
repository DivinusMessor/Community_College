import itertools  # For testing
from hash_practice import Protein, UnorderedTuple, UnorderedString

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