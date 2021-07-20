#!/usr/bin/env python3.9
"""
Reads a word-search grid from standard input, and prints all valid words in the grid to standard output. Specifically: 
"""

__author__ = 'Yukio Rivera, ysrivera@jeff.cis.cabrillo.edu'

import sys
import numpy as np


def slice_and_check(wrds, min_len, spell_checker, found_words):
  counter= 0
  str_len = len(wrds)
  stng = ""
  long_str = ""
  for i in wrds:
    print(wrds)
    stng = (wrds[counter:counter + min_len])
    counter+=1
    #if (len(stng) < min_len):
      #break
    if (len(stng) >= min_len):
      print(stng)
      for key, value in spell_checker.items():
        if stng[0] == key:
          if stng in value:
            found_words.add(stng)


def make_string(s_list): 
  n_string = ""
  for i in s_list:
    n_string = n_string + i
  return n_string


def main():
  #Variables that we are going to use
  spell_checker = dict()
  puzzle = []
  grid_len = 0
  found_words = set()

  #Taking input from sys for minimum length of the word and the dictionary we are using 
  min_len = int(sys.argv[1])
  dict_file = sys.argv[2]

  #Creating dictionary that holds the words we are looking for 
  for word in open(dict_file):
    word = word.rstrip().upper()
    if len(word) >= min_len:  
      if (word[0] in spell_checker):
        spell_checker[word[0]].add(word) 
      else:
        spell_checker[word[0]] = set(word)
  
  #making numpy array to hold the word finder puzzle grid
  for grid in sys.stdin:
    puzzle.append(list(grid.rstrip()))
  puzzle = np.array(puzzle)
  
  #getting length of puzzle
  grid_len = len(puzzle[0])

  #printing columns
  c_wrds = ""
  rc_wrds = ""
  c_counter = 0
  for col in range(grid_len):
    column = (puzzle[:,col])
    c_wrds = make_string(column)
    rc_wrds = ''.join(reversed(c_wrds))
    slice_and_check(c_wrds, min_len, spell_checker, found_words)
    slice_and_check(rc_wrds, min_len, spell_checker, found_words)
  
  #printing rows
  r_wrds = ""
  rr_wrds = ""
  c_counter = 0
  for row in range(grid_len):
    rows = (puzzle[row,:])
    r_wrds = make_string(rows)
    rr_wrds = ''.join(reversed(r_wrds))
    slice_and_check(r_wrds, min_len, spell_checker, found_words)
    slice_and_check(rr_wrds, min_len, spell_checker, found_words)


#Printing Diag
  d_counter = 0
  check_str = ""
  diag_str = ""
  rdiag_str = ""

  #for i in (np.diagonal(puzzle, -grid_len+min_len+counter)):
  for i in range(0, grid_len+grid_len):
      check_str = (np.diagonal(puzzle, -grid_len+min_len+d_counter))
      #d_counter+=1
      if len(check_str) < min_len:
        break
      diag_str = make_string(check_str)
      rdiag_str = ''.join(reversed(diag_str))
      slice_and_check(diag_str, min_len, spell_checker, found_words)
      slice_and_check(rdiag_str, min_len, spell_checker, found_words)
      d_counter+=1
  
  
  for items in found_words:
    sys.stdout.write(items + "\n")
  

# Keep this at the bottom
if __name__ == '__main__':
  main()
