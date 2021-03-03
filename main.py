from itertools import permutations
from functools import reduce

line = open('input.txt', 'r', encoding='utf8').read().split()

stvar = list(map(lambda x: reduce(lambda a, b: str(a) + str(b), x),
                 (permutations(range(1, int(line[0]) + 1))))) # варианты забега


print(stvar[list(filter(lambda x: x[1],
    list(enumerate(map(lambda x: (all(map(lambda k:
        (x.find(line[4 + k * 4: 6 + k * 4][0]) <= x.find(line[4 + k * 4: 6 + k * 4][1])) ^
        (x.find(line[2 + k * 4: 4 + k * 4][0]) <= x.find(line[2 + k * 4: 4 + k * 4][1])),
                  range(int(line[1]))))),
             stvar)))))[0][0]]
      if list(filter(lambda x: x[1],
    list(enumerate(map(lambda x: (all(map(lambda k:
        (x.find(line[4 + k * 4: 6 + k * 4][0]) <= x.find(line[4 + k * 4: 6 + k * 4][1])) ^
        (x.find(line[2 + k * 4: 4 + k * 4][0]) <= x.find(line[2 + k * 4: 4 + k * 4][1])),
                  range(int(line[1]))))),
             stvar))))) != [] else '0')
"""
myansw = list(filter(lambda x: x[1],
    list(enumerate(map(lambda x: (all(map(lambda k:
        (x.find(line[4 + k * 4: 6 + k * 4][0]) <= x.find(line[4 + k * 4: 6 + k * 4][1])) ^
        (x.find(line[2 + k * 4: 4 + k * 4][0]) <= x.find(line[2 + k * 4: 4 + k * 4][1])),
                  range(int(line[1]))))),
             stvar)))))
"""