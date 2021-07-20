"""
Examples of custom decorator functions.
"""
__author__ = 'Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu'

import functools
import gc
import sys
import time


def log(func):
  """
  Prints messages on stderr announcing begin/end of calls to decorated functions.
  """

  @functools.wraps(func)  # Preserves namespace/docstring attributes of wrapped function
  def log_wrapper(*args, **kwargs):
    print(f'→{func.__name__} @ {time.time()}', file=sys.stderr)
    ret_val = func(*args, **kwargs)  # Pass along any necessary arguments
    print(f'←{func.__name__} @ {time.time()}', file=sys.stderr)
    return ret_val

  return log_wrapper


def timeit(func):
  """
  A custom function somewhat similar to timeit.timeit().
  Any function decorated by this will return (execution_time, return_value).
  """

  @functools.wraps(func)  # Preserves namespace/docstring attributes of wrapped function
  def timeit_wrapper(*args, **kwargs):
    gc.disable()  # Make sure garbage collection doesn't confound things
    before = time.perf_counter()
    ret_val = func(*args, **kwargs)
    after = time.perf_counter()
    gc.enable()
    return after - before, ret_val

  return timeit_wrapper