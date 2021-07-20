"""
Hopefully this will be relatively painless!
"""

__author__ = 'A student in CS 20P, someone@jeff.cis.cabrillo.edu'


def counting_sort(data: list[int], min_value: int, max_value: int) -> None:
  """
  Performs counting sort on an list of integer values.

  :param data: a list of integers to sort
  :param min_value: the smallest possible value in data
  :param max_value: the largest possible value in data
  """
  '''
  elements = {}
  for i in data:
    elements[l] = elements.get(l,0) + 1 
  print elements
  '''
  range_list = range(min_value, max_value)
  for i in data:
    print(i)

# Remove/comment the following before submitting
if __name__ == '__main__':
  example = [-1, 3, 2, 5, -7, 10, 12]
  counting_sort(example, -7, 10)
  """
  import sys
  test_data = list(sys.stdin.read().encode('utf-8'))
  test_copy = test_data.copy()
  counting_sort(test_data, 0, 255)
  assert test_data == sorted(test_copy)
  """