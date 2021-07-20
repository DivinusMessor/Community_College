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
  ##Length of range array is the difference between max-min
  array_len = max_value - min_value 
  print(array_len)
  range_list = []
  counter = 0
  print("unSorted data:", data)
  for i in range(0, array_len+1):
    range_list.append(0)
  print("first range list:", range_list) 
  for n in data:
    print(n)
    range_list[n-min_value] += 1 
  print("second range list:", range_list) 
  print("Input data:", data)
  print(len(range_list))
  for i in range(len(range_list)):
    print("i: ",i)
    while (range_list[i] > 0):
      data[counter] = i + min_value
      print("range_list[i]:", range_list[i])
      counter += 1
      range_list[i] -= 1
    print("Changed range list:", range_list)
    print("Sorting data:", data)
  print("Sorted data:", data)
  #needs to manipulate data now make new list
  '''
  data = []
  for q in range(len(range_list)):
    while range_list[q] > 0:
      data.append(q+min_value)
      range_list[q] -= 1
  #data[counter] = new value
  print(data)
  '''
# Remove/comment the following before submitting
if __name__ == '__main__':
  example = [-2999999, -3000000]
  counting_sort(example, -3000000, -2999999)
  """
  import sys
  test_data = list(sys.stdin.read().encode('utf-8'))
  test_copy = test_data.copy()
  counting_sort(test_data, 0, 255)
  assert test_data == sorted(test_copy)
  """