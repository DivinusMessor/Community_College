'''
Mimics fold linux command
'''
import sys
from io import StringIO
import functools

print(''.join(
    map(lambda x: x + ("\n" if x else ''), ['\n'.join(map(
        lambda x: '\n'.join(iter(functools.partial(StringIO(x).read, int(
            sys.argv[1])), '')), sys.stdin.read().split("\n")[:-1]))])), end='')
