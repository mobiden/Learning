
a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input()),

if a != 0 and b != 0 and c != 0 and d != 0:
    if f != 0:
        if a / c == b / d != e / f:
            print('0')
        elif a / c == b / d == e / f:
            p = -a / b
            q = e / b
            print('1', p, q)
        elif a / c != b / d:
            y = (f * a - c * e) / (d * a - c * b)
            x = (e - b * y) / a
            print('2', x, y)
    else:
        if a / c == b / d and e != 0:
            print('0')
        elif a / c != b / d:
            y = (f * a - c * e) / (d * a - c * b)
            x = (e - b * y) / a
            print('2', x, y)
        else:
            print('1', -a / b, '0')
# without 0

if a == b == c == d == e == f == 0:
    print('5')

elif a == b == c == d == 0 and (e != 0 or f != 0):
    print('0')

elif (a == 0 and b == 0 and c == 0 and d != 0):
    if e != 0:
        print('0')
    else:
        print('4', f / d)
elif (a == 0 and c == 0 and d == 0 and b != 0):
    if f != 0:
        print('0')
    else:
        print('4', e / b)
elif (b == 0 and c == 0 and d == 0 and a != 0):
    if f != 0:
        print('0')
    else:
        print('3', e / a)
elif (a == 0 and b == 0 and d == 0 and c != 0):
    if e != 0:
        print('0')
    else:
        print('3', f / c)

elif a == b == 0 and e != 0:
    print('0')
elif c == d == 0 and f != 0:
    print('0')

elif a == c == 0:
    if f != 0:
        if b / d == e / f:
            print('4', e / b)
        else:
            print('0')
    else:
        if e == 0:
            print('4', '0')
        else:
            print('0')
elif b == d == 0:
    if f != 0:
        if a / c == e / f:
            print('3', e / a)
        else:
            print('0')
    else:
        if e == 0:
            print('3', '0')
        else:
            print('0')

elif a == b == e == 0:
    print('1', -c / d, f / d)
elif c == d == f == 0:
    print('1', -a / b, e / b)

elif a == 0 and b != 0 and c != 0:
    y = e / b
    x = (f - d * y) / c
    print('2', x, y)
elif b == 0 and a != 0 and d != 0:
    x = e / a
    y = (f - c * x) / d
    print('2', x, y)
elif c == 0 and d != 0 and a != 0:
    y = f / d
    x = (e - b * y) / a
    print('2', x, y)
elif d == 0 and b != 0 and c != 0:
    x = f / c
    y = (e - a * x) / b
    print('2', x, y)
