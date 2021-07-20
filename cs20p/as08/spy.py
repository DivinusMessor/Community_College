#!/usr/bin/env python3

"""
Python program that replicates the behavior of cs20p_image_steganography_decode
"""

__author__ = "Yukio Rivera for CS 20P, ysrivera.bergamini@cabrillo.edu"

import sys

# Look at the end bit of every pixel to get the bit of the message
# 8 bits make 1 character of the message (byte)
# 8 zeros means the end of the message it makes 0
# Start at the top left corner of the image
# you will get the binary 8 bit (byte) value of the
# pixel and then you have to look at the end of the pixel
# binary operations will help
# 8 0's make 0

__author__ = 'Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu'


def stego():
  type_of_img = int(sys.argv[1])
  counter = 0
  bit_list = 1
  while bit_list != 0:
    bit_list = 0
    for i in range(counter, counter + 8):
      lst = list(sys.stdin.buffer.read(type_of_img))
      # using bitwise and (&)
      get_last_bit = lst[i % type_of_img] & 1
      bit_list = bit_list << 1
      bit_list = bit_list | get_last_bit
    counter += 8
    if bit_list == 0:
      break
    print(chr(bit_list), end="")


def main():
  stego()


# Keep this at the bottom
if __name__ == '__main__':
  main()
