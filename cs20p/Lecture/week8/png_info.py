#!/usr/bin/env python3
"""
Determine whether command-line arguments are paths to PNG image files.

The first eight bytes of a PNG datastream always contain the following (decimal) values:
137 80 78 71 13 10 26 10
"""
__author__ = 'Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu'

import sys

def is_png(path):
  try:
    # Open the file in binary mode for reading rb
    file = open(path, mode='rb')
    # Read its contents into a bytes object
    contents = file.read(8)
    return contents == bytes([137, 80, 78, 71, 13, 10, 26, 10])
  except Exception as error:
    print(f'Error: {error}')

for file_path in sys.argv[1:]:
  if is_png(file_path):
    print(file_path, 'IS a PNG')
  else:
    print(file_path, 'IS NOT a PNG')