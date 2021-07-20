'''
Mimics nl linux command
'''
import sys

print(''.join(
    map(lambda x: x + ("\n" if x else ''),
        ["\n".join(f"{x} {y}" for x, y in enumerate(sys.stdin.read().split("\n")[:-1], 1))])),
      end='')
