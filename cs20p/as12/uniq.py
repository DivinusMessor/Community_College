'''
Mimics uniq linux command
'''
import sys
import functools

print(''.join(
    map(lambda x: x + ("\n" if x else ''), [
        "\n".join(f"{x} {y}" for x, y in functools.reduce(
            lambda x, y: (x + [(1, y)]) if (x and x[-1][1]) != y else
            (x[:-1] + [(x[-1][0] + 1, y)]),
            sys.stdin.read().split("\n")[:-1], []))])), end='')
