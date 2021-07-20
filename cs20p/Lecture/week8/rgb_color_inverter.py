#!/usr/bin/env python3
"""
Treating a bytearray as if it represents 24-bit RGB pixels.

Here we modify a 24-bit RGB "image" to invert the color components in each pixel, creating a
"negative" image.

We output raw binary data, suitable for input to a program like ImageMagick's "convert" utility:
convert img_file rgb:- | ./rgb_color_inverter.py | convert -depth 8 -size widthxheight rgb:- out.jpg
"""
__author__ = 'Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu'

import sys

# This is not an image, but we'll treat it like an array of 24-bit RGB pixels.
image = bytearray(sys.stdin.buffer.read())

for i in range(len(image)):
  image[i] = 255 - image[i]  # Each RGB component will be "inverted" (0-->255, 255-->0, etc.)

sys.stdout.buffer.write(image)