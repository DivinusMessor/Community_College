#!/usr/bin/env python3
"""
Generating little-endian 16-bit 44.1 kHz PCM square waves.

Try input files /srv/datasets/song[012]

Pipe into, e.g.:
  play --type raw --channels 1 --bits 16 --rate 44100 --encoding signed-integer -
(Must have "sox" installed on your machine.)

Or into, e.g.:
  oggenc --raw -C 1 -o ~/public_html/test.ogg -
(oggenc is installed on our server)
"""
__author__ = 'Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu'

import sys

# Expect a sequence of lines containing frequency (Hz) and duration (s) values.
# Emit a PCM waveform (square waves) representing those sounds.

SAMPLE_RATE = 44_100  # Samples per second
AMPLITUDE = .5  # "Volume" (maximum percentage amplitude of waves)
MAX = round((2 ** 15 - 1) * AMPLITUDE)  # Maximum numeric sample value
# Square waves will oscillate between these two values.
EXTREMA = [
  MAX.to_bytes(length=2, byteorder='little', signed=True),
  (-MAX).to_bytes(length=2, byteorder='little', signed=True)
]

extremum_index = 0
for line in sys.stdin:
  frequency, duration = [float(token) for token in line.split()]
  # Number of samples per wave period
  samples_per_period = 0 if not frequency else round(SAMPLE_RATE / frequency)
  # Total number of samples to generate for this duration
  total_samples = round(duration * SAMPLE_RATE)
  output = bytearray()
  # Emit square waves
  for sample_num in range(total_samples):
    # Add bytes for whichever square-wave extremum we're on.
    for byte in EXTREMA[extremum_index]:
      output.append(byte)
    # Switch extrema when we're halfway through a wave period
    if frequency and not sample_num % (samples_per_period // 2):
      extremum_index = 0 if extremum_index else 1
  sys.stdout.buffer.write(output)