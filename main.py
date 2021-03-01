from sys import stdin
from functools import reduce
print(*(map(lambda z: reduce(lambda x, y: (2 - int(x) - int(y)) % 2, z),
            list(filter(lambda x: x[0] != ' ', zip(
                *(stdin.read().strip().split('\n')[1:])))))))
