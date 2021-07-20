#!/usr/bin/env python3.9
"""
A simple spell-checker for demonstrating the membership operation in Python's built-in collections.

Try varying:
  Container types with input from file /srv/datasets/us-constitution.txt
  Set containers given input files /srv/datasets/{joyce-ulysses.txt,tolstoy-anna-karenina.txt}
  Containers and input files /srv/datasets/{genius.txt,bill-of-rights.txt}
"""
from __future__ import annotations

__author__ = 'Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu'

import re
import sys
import time
from collections.abc import Callable, Container, Iterable


#Make a type of container that we chose. 
def load_dictionary(collection_type: Callable, dict_path: str) -> Container[str]:
  """
  Populates a container with a simple spell-checking sp_dictionary (one word per line).

  :param collection_type: the type of collection to populate
  :param dict_path: the path to the sp_dictionary file
  :return: the populated container
  """
  #It opens the dictionary that is the type specified seperates by white space. 
  #Its everything lowercase. It iterates through the dictionary line by line. 
  with open(dict_path) as dict_file:
    return collection_type(line.strip().lower() for line in dict_file)


#Gives back a list of words, word, if its a none emprty string that was misspelled
def misspelled_words(dictionary: Container[str], words: Iterable[str]) -> list[str]:
  """
  Finds and returns all misspelled words.

  :param dictionary: a container supporting membership test (in)
  :param words: the words to spell-check
  :return: a list containing all words not in dictionary, in the order encountered
  """
  #Returns a word that IS NOT in the dictionary 
  return [word for word in words if word and word not in dictionary]


#We get a callable object which is the type that we chose, path to dictionary that is a string,
#and an iterable collection of strings that we are going to check
def spell_check(dictionary_type: Callable, dict_path: str, to_check: Iterable[str]):
  #checking what time is it
  before_load = time.time()
  #the load_dictionary function, we give it some kind of container to fill up and create one
  #of the containers and fill it up with the words from the dictionary, specified by the type. 
  #it returns a populated container, filled with all the words of the spell check dictionary 
  dictionary = load_dictionary(dictionary_type, dict_path)
  after_load = time.time()
  before_check = time.time()
  #The misspelled function takes whatever we got back from the load dictionary, set list..., 
  #we are going to use it as a misspell dictionary and then its going to take whatever words
  #we want to check for spelling
  misspelled = misspelled_words(dictionary, to_check)
  after_check = time.time()
  if misspelled:
    print('\n'.join(misspelled))
  #The print output will also show some more information such as, path, words, spellcheck time
  print(f'''Collection type: {dictionary_type}
Dictionary path: {dict_path}
Words in dictionary: {len(dictionary)}
Dictionary load time: {after_load - before_load:f}
Words in text: {len(to_check)}
#Everything above is standardout put the bottom is standarderr
Spell-check time: {after_check - before_check:f}''', file=sys.stderr)


if __name__ == '__main__':
  # First command-line arg (if present) is the name of a built-in collection type
  
  #(cls.__name__: cls for cls in) is associating a container name to the type itself,  list, tuple, set, fronzenset so the program can 
  #Recognize the name. Mapping strings to types if the user makes a choice
  available_containers = {cls.__name__: cls for cls in (list, tuple, set, frozenset)}
  
  #if the user makes a choice we are going to use the first command line argument (sys.argv[1] as a key for the dictionary)
  #If the checker, if len(sys.argv) > 1 and the argument is in the available container dictionary, then it
  #will use the type or it will default to set, (else set)
  #The "/" is to continue the statement down below without breaking the argument 
  container_type = available_containers[sys.argv[1]] if len(sys.argv) > 1 and sys.argv[1] in \ 
                                                        available_containers else set
  # Second command-line arg (if present) is the path to a spell-checking dictionary file
  #If there is a second commandline arugment, path to a spell check library, use it or else it will default
  #to the many-english-words.txr
  dict_file_path = sys.argv[2] if len(sys.argv) > 2 else '/srv/datasets/many-english-words.txt'
  # Use a regular expression to compose a list of each "word" in stdin
  # See: https://docs.python.org/3/library/re.html#regular-expression-syntax
  #make a list of each word in the file that i split up by whitespace
  #the (re.) is a module that is used for regular expressions. its a pattern matchin 
  #It searches words based on the pattern (r"[^\w']+"). The pattern says look for anything that
  # isn't a word, charater, or apostrophy 
  # The (r) is for the interprepter to interpret the input as a (raw) string and nothing else.
  # To see the rest look up (re.) docstring
  #will returns words from a none empty string
  all_words = [word for word in re.split(r"[^\w']+", sys.stdin.read().lower()) if word]
  #Passin spellcheck function 
  #The container_type is the type the user chose, or set by deault 
  spell_check(container_type, dict_file_path, all_words)