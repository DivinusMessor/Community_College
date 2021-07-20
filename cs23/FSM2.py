#!/usr/bin/env python3.9

__author__ = 'Yukio Rivera'

"Python Program - Finite State Machine"

import sys
from collections import defaultdict

ndd = ""
states = int()
inputs = int()
strt = int()
accepting = []

# Reads input
i_nums = sys.stdin.read().split()


# Opens the FSM file to get the info to build the FSM
with open(sys.argv[1], 'r') as my_file:
  ndd = my_file.readline().split()[0]
  states = int(my_file.readline().split()[1])
  inputs = int(my_file.readline().split()[1])
  strt = int(my_file.readline().split()[1])
  accepting = my_file.readline().split()[1:]
  trans_line = my_file.readline().split()
  
  # Machine built
  machine = dict()
  current_state = strt
  for fsm in my_file:
    frm, to, symbol = fsm.split()
    machine.setdefault(frm,dict())
    machine[frm].setdefault(symbol, [])
    machine[frm][symbol].append(to)

# Recursive function to evaluate input
# How to get to accepted only using lambda not input
def evaluate(inpt, machine, path, acct):
  if len(inpt) == 0:
    trans = machine[str(path[-1])]
    if '-1' in trans:
      print(trans)
      for next in trans['-1']:
        if evaluate(inpt, machine, path + [next], acct):
          return True
    return str(path[-1]) in acct
  trans = machine[str(path[-1])]
  if '-1' in trans:
    for next in trans['-1']:
      if evaluate(inpt, machine, path + [next], acct):
        return True
  next_states = trans[str(inpt[0])]
  for next in next_states:
    if evaluate(inpt[1:], machine, path + [next], acct):
      return True
  return False

if evaluate(i_nums, machine, [strt], accepting) ==  True:
  print("Accepted")
else:
  print("Rejected")
