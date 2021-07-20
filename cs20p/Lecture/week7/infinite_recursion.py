"""
A function can call itself.
However, it should never do it this way...
"""

__author__ = 'Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu'

import sys
import traceback

# This program will result in a recussion error where it used its max
# amount of stacks went down too many levels of recussion
# It will throw an exception and ask user to change limit
# This goes into neagative 

def sing_it_louder(n):
  """ This will not end well. """
  print(f'{n} bottles of beer on the wall...')
  sing_it_louder(n - 1)


if __name__ == '__main__':
  while True:
    try:
      sing_it_louder(99)
    except Exception as e:
      traceback.print_exc(file=sys.stdout)
      new_limit = int(input('Wanna change the limit?: '))
      sys.setrecursionlimit(new_limit)  # You should probably never actually do this! For demo only.