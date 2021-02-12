n = int(input())


def phib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        n -= 1
        s = phib(n) + phib(n - 1)
        return s

print(phib(n))
