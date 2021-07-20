"""
Demonstrating decorator syntax vs. manually wrapping functions.
"""

import decorators
import time

# Will output a message showing how long it will sleep 
@decorators.log  # Choose this (decorator syntax)
def sleep_for(duration):
  time.sleep(duration)

# Will output a message showing how long it will sleep for 
# sleep_for = decorators.log(sleep_for)  # Or this: Old-style wrapping/shadowing

if __name__ == '__main__':
  sleep_for(1)