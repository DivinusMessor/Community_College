#!/usr/bin/env python3.9
"""
Using cProfile to count function calls.

Try, e.g.:

./call_profiler.py 'factorial.factorial_recursive(10)'
./call_profiler.py 'factorial.factorial_recursive(20)'
./call_profiler.py 'factorial.factorial_recursive(100)'

./call_profiler.py 'fibonacci.fibonacci_recursive(4)'
./call_profiler.py 'fibonacci.fibonacci_recursive(5)'
./call_profiler.py 'fibonacci.fibonacci_recursive(6)'
./call_profiler.py 'fibonacci.fibonacci_recursive(29)'
./call_profiler.py 'fibonacci.fibonacci_recursive(30)'
./call_profiler.py 'fibonacci.fibonacci_recursive(31)'
./call_profiler.py 'fibonacci.fibonacci_recursive(35)'
(and same with fibonacci_memoized)

./call_profiler.py 'gcd.gcd_euclidean(1, 1)'
./call_profiler.py 'gcd.gcd_euclidean(1, 10)'
./call_profiler.py 'gcd.gcd_euclidean(2**20, 2)'

./call_profiler.py 'permutations.set_permutations(set(range(4)))'
./call_profiler.py 'permutations.set_permutations(set(range(5)))'
./call_profiler.py 'permutations.set_permutations(set(range(6)))'
./call_profiler.py 'permutations.set_permutations(set(range(7)))'
"""

__author__ = "Jeffrey Bergamini for CS 20P, jeffrey.bergamini@cabrillo.edu"

import factorial
import fibonacci
import gcd
import permutations
import cProfile
import itertools
import sys


if __name__ == '__main__':
  cProfile.run(f'print({sys.argv[1]})', sort='calls')