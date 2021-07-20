>>> import collections
>>> demo = collections.Counter('Earth: Mostly harmless')
>>> demo
Counter({'s': 3, 'a': 2, 'r': 2, 't': 2, 'h': 2, ' ': 2, 'l': 2, 'E': 1, ':': 1, 'M': 1, 'o': 1, 'y': 1, 'm': 1, 'e': 1})
>>> demo.keys()
dict_keys(['E', 'a', 'r', 't', 'h', ':', ' ', 'M', 'o', 's', 'l', 'y', 'm', 'e'])
>>> demo.values()
dict_values([1, 2, 2, 2, 2, 1, 2, 1, 1, 3, 2, 1, 1, 1])
>>> demo.items()
dict_items([('E', 1), ('a', 2), ('r', 2), ('t', 2), ('h', 2), (':', 1), (' ', 2), ('M', 1), ('o', 1), ('s', 3), ('l', 2), ('y', 1), ('m', 1), ('e', 1)])
>>> demo['s']
3
>>> demo['!']
0

>>> '!'.join('robot')
'r!o!b!o!t'

print(' '.join(str(counts[base]) for base in 'ACGT'))


>>> sum(range(101))**2 - sum(x**2 for x in range(101))
25164150