#!/usr/bin/env python3.9
"""
Reads a word-search grid from standard input, and prints all valid words in the grid to standard output. Specifically: 
"""

__author__ = 'Yukio Rivera, ysrivera@jeff.cis.cabrillo.edu'

import sys
import numpy as np

#def load_dictionary(dict_path):
'''
for word in open(dict_file):
  word = word.rstrip().upper()
  if len(word) >= min_len:  
    if (word[0] in spell_checker):
      spell_checker[word[0]].add(word) 
    else:
      spell_checker[word[0]] = set(word)
'''

#words that were found


def slice_and_check(wrds, min_len, spell_checker, found_words):
  counter= 0
  stng = ""
  for i in wrds:
    stng = (wrds[counter:counter + min_len])
    counter+=1
    #print(stng)
    if (len(stng) < min_len):
      break
    for key, value in spell_checker.items():
      if stng[0] == key:
        if stng in value:
          found_words.append(stng)
  return found_words


def main():
  #Variables that we are going to use
  spell_checker = dict()
  puzzle = []
  grid_len = 0
  found_words = []

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
  print(puzzle)

  #printing coulms
  #counter= 0
  wrds = ""
  #stng = ""
  for row in range(grid_len):
    for column in range(grid_len):
      col = (puzzle[column][row])
      wrds = wrds + col
  print(wrds)
  #print(wrds.reverse())
  slice_and_check(wrds, min_len, spell_checker, found_words)
  print(found_words)

#making this into a function
#def slice_and_check(wrds, min_len, spell_checker, found_words):
  """for i in wrds:
    stng = (wrds[counter:counter + min_len])
    counter+=1
    #print(stng)
    if (len(stng) < min_len):
      break
    for key, value in spell_checker.items():
      if stng[0] == key:
        if stng in value:
          print(stng)"""
  #Testing for grid
  '''
  
  print("------", puzzle[0], "----------")
  print(grid_len)
  '''
  #word_search(puzzle, grid_len, min_len)

# Keep this at the bottom
if __name__ == '__main__':
  main()