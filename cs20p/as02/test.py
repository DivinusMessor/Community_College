#! /usr/bin/env python3.9
"""
Yukio Rivera
CS20P: Assigment_02 - Rosalind
rosalind.amino
rosalind.prot()
rosalind.potential_proteins()
"""
import re

amino = {}

with open("/srv/datasets/amino", 'r') as f:
  for line in f:
    r_list = line.split()
    codon = r_list[0].replace("T", "U")
    amino[codon] = r_list[2]


def prot(rna):
  """
  Calculates and returns the protein string encoded by an RNA string, or None if the encoding is
  invalid. A valid encoding consists of 12 or more codons, where the first is start codon 'AUG',
  followed by at least 10 more non-stop codons, and then a stop codon.
  (The shortest known protein is length 11: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3864261/)
  Amino-acid encoding information shall be taken from the dict represented by variable amino.
  :param rna: An RNA string (assumed to contain characters in 'ACGU', with len(rna) % 3 == 0).
  :return: The protein string encoded by rna, or None if the the encoding is invalid.
  """
  counter = 0
  end = 0
  s_rna = []
  eps = ""
  pro = ""
  f_amino = []
  start = rna.index("AUG")
  starting = rna[start:]
  s_rna = re.findall('...', starting)
  for y in s_rna:
    pro = amino.get(y)
    eps = eps + pro
    counter += 1
  if "O" in eps:
    end = eps.index("O")
    if end >= 11:
      f_amino = eps[:end]
      return f_amino
    else:
      return None
  else:
    return None


def potential_proteins(rna):
  """
  Calculates and returns all potential valid protein encodings in an RNA string. Any protein valid
  according to function prot() shall be considered valid by this function as well.
  Amino-acid encoding information shall be taken from the dict represented by variable amino.
  :param rna: An RNA string (assumed to contain characters in 'ACGU').
  :return: A list of the possible proteins in the RNA, in the order encountered in the RNA.
  """
  start_pos = []
  p_pro = []
  m_pro = []
  ami = ""
  start_c = "AUG"
  if "T" in rna:
    rna = rna.replace("T", "U")
  for i in re.finditer(start_c, rna):
    (start_pos.append(i.start()))
  for n in start_pos:
    p_pro.append(rna[n:])
  for q in p_pro:
    ami = prot(q)
    if ami is not None:
      m_pro.append(ami)
  return m_pro


def main():
  (potential_proteins("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"))
  (prot('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'))


# Keep this at the bottom
if __name__ == '__main__':
  main()

