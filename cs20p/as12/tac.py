'''
Mimics tac linux command
'''
import sys

print(''.join(
    map(lambda x: x + ("\n" if x else ''),
        ["\n".join(list(reversed(sys.stdin.read().split("\n")[:-1])))])),
      end='')
