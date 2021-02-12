n, x = int(input()), float(input())
s = 0
b = 0

while s != n + 1:
    a = float(input())
    b = b * x + a
    s += 1

print(b)
