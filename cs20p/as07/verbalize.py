# ./verbalize.py

"""
A module that will verbalize given integers.
"""


__author__ = "Yukio Rivera for CS 20P, ysrivera.bergamini@cabrillo.edu"

digit_to_words = {}

with open('/srv/datasets/number_names.txt', 'r') as d_to_words:
  number_list = d_to_words.read().split()
counter = 1
for i in range(0, len(number_list), 2):
  digit_to_words[int(number_list[counter])] = number_list[i]
  counter += 2


def verbalize(n, power=0):
  if n >= 1000:
    result = []
    result = result + verbalize(n // 1000, power + 1)
    if n % 1000 > 0:
      result = result + verbalize(n % 1000, power)
    return result
  else:
    num_word = ""
    if n == 0 and power == 0:
      return [digit_to_words.get((n))]
    check_l = n // 100
    if check_l > 0:
      num_word += digit_to_words[(check_l)] + " " + digit_to_words[(100)] + " "
    check_r = n % 100
    if check_r > 0:
      if check_r >= 20:
        check_r_tens = (check_r // 10) * 10
        num_word += digit_to_words[(check_r_tens)]
        check_r_ones = (check_r % 10)
        if check_r_ones > 0:
          num_word += "-" + digit_to_words.get((check_r_ones))
      else:
        num_word += digit_to_words.get((check_r))
    if power > 0:
      num_word += " " + digit_to_words[(1000**power)]
    return [" ".join(num_word.split())]
