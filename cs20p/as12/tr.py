'''
Mimics tr linux command
'''
import sys

print(''.join(
    map(lambda x: x + ("\n" if x else ''), [
        "\n".join(
            list(
                map(lambda x: x.translate(x.maketrans(sys.argv[1], sys.argv[2])),
                    sys.stdin.read().split("\n")[:-1])))])), end='')
