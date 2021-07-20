#!/usr/bin/env python3
"""
Treating a bytearray as if it represents 8-bit grayscale pixels.

Here we generate an "image" that gets brighter toward the center.

We output raw binary data, suitable for input to a program like ImageMagick's "convert" utility:
./grayscale_pixels.py | convert -depth 8 -size 1280x1024 gray:- ~/public_html/test.png
"""
__author__ = 'Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu'

import math
import sys

WIDTH = 1280
HEIGHT = 1024
MAX_DISTANCE = min(WIDTH, HEIGHT) / 2  # We'll only color pixels within this distance from center.

# This is not an image, but we'll treat it like a WIDTH×HEIGHT pixel array.
# (First WIDTH bytes are first row, second WIDTH bytes are second row, etc.)
# All zeros (black) to begin with.
image = bytearray(WIDTH * HEIGHT)

# Every pixel within MAX_DISTANCE from center gets increasing intensity toward the center
for row in range(HEIGHT):
  for col in range(WIDTH):
    distance_from_center = math.sqrt((col - WIDTH / 2) ** 2 + (row - HEIGHT / 2) ** 2)
    if distance_from_center <= MAX_DISTANCE:
      coordinate = row * WIDTH + col
      intensity = round((1 - distance_from_center / MAX_DISTANCE) * 255)
      image[coordinate] = intensity

# Write the "image" to standard output
sys.stdout.buffer.write(image)