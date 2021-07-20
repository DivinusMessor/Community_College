"""
Hopefully this will be relatively painless!
"""

__author__ = 'Yukio Rivera, ysrivera@jeff.cis.cabrillo.edu'


def counting_sort(data: list[int], min_value: int, max_value: int) -> None:
  """
  Performs counting sort on an list of integer values.

  :param data: a list of integers to sort
  :param min_value: the smallest possible value in data
  :param max_value: the largest possible value in data
  """
  # Length of range array is the difference between max-min
  array_len = max_value - min_value
  range_list = []
  counter = 0
  # Creating the temp array
  for i in range(0, array_len + 1):
    range_list.append(0)
  # Keeping track of the elements
  for n in data:
    range_list[n - min_value] += 1
  # Sorting the array
  for i in range(len(range_list)):
    while range_list[i] > 0:
      data[counter] = i + min_value
      counter += 1
      range_list[i] -= 1
