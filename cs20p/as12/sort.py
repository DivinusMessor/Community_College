'''
Mimics sort linux command
'''
import sys

print(''.join(
    map(lambda x: x + ("\n" if x else ''), ["\n".join(sorted(
        sys.stdin.read().split("\n")[:-1]))])), end='')
