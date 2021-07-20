"""
A quick decorator demonstration!
"""

__author__ = 'Yukio Rivera, ysrivera@jeff.cis.cabrillo.edu'


def lock_lists(func):
  """
  Converts any list arguments (positional and/or keyword) to tuples before passing them to the
  decorated function. Returns the value returned by decorated function.
  """

  def conv(*args, **kwargs):
    # List comprehension that will take the list from args and make it into a tuple
    args = [tuple(i) if isinstance(i, list) else i for i in args]
    # Dictionary comprehension that will make the list that is inputted and make it into a tuple
    kwargs = {tuple(value) if isinstance(value, list) else value for (key, value) in kwargs.items()}
    # Returns the function in the argument of lock_lists() with the new value of args/kwargs
    return func(*args, **kwargs)

  return conv


def copy_lists(func):
  """
  Converts any list arguments (positional and/or keyword) to copies of those same lists before
  passing them to the decorated function. Returns the value returned by decorated function.
  """

  def cop(*args, **kwargs):
    # List comprehension that will create a copy of the list into args
    args = [i.copy() if isinstance(i, list) else i for i in args]
    # Iterates through the key,values of the dictionary in kwargs and looks for a list
    kwargs = {
        key: value.copy() if isinstance(value, list) else value for (key, value) in kwargs.items()
    }
    # Returns the function in the argument of lock_lists() with the new value of args/kwargs
    return func(*args, **kwargs)

  return cop
