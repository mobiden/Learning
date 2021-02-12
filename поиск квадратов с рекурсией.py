from math import sqrt, floor


def kva(ans):

    n = int(input())
    if n != 0:
        sans = kva(ans + 1)
    else:
        return -1

    if (floor(sqrt(n))) ** 2 == n and n != 0:
        print(n)
        return -2
    else:

        if ans == 0:
            if sans == -1:
                print(0)
        else:
            return sans
kva(0)
