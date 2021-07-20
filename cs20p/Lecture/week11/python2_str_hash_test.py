#!/usr/bin/env python2
"""
Illustrating a string-hashing algorithm used in Python 2.
"""
__author__ = 'Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu'


class mystring(str):
  """ Implements pretty much Python 2's string hash function """

  def __hash__(self):
    if not self:
      return 0
    value = ord(self[0]) << 7
    for char in self:
      value = (1000003 * value) ^ ord(char)
    value ^= len(self)
    if value == -1:
      value = -2
    return value


if __name__ == '__main__':
  test = 'OK'
  s = mystring(test)
  assert hash(test) == hash(s)
  print test, hash(test)
  print s, hash(s)
