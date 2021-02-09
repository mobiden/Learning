l = list(map(int, input().split()))
lmin, lmax = [], []
xmin1, xmax1 = 0, 0
xmin2, xmax2 = 0, 0
xmin3, xmax3 = 0, 0

for i in range(len(l)):
    if l[i] >= 0:
        lmax.append(l[i])
        if xmax3 <= l[i]:
            xmax3 = l[i]
            if xmax3 > xmax2:
                xmax2, xmax3 = xmax3, xmax2
                if xmax2 > xmax1:
                    xmax1, xmax2 = xmax2, xmax1
    elif l[i] < 0:
        lmin.append(l[i])
        if xmin3 >= l[i]:
            xmin3 = l[i]
            if xmin3 < xmin2:
                xmin2, xmin3 = xmin3, xmin2
                if xmin2 < xmin1:
                    xmin1, xmin2 = xmin2, xmin1

if len(lmax) + len(lmin) <= 3:
    print(*lmax, *lmin)
elif len(lmax) == 0:
    ymax1 = ymax2 = ymax3 = lmin[0]
    for i in range(len(lmin)):
        if ymax3 <= lmin[i]:
                ymax3 = lmin[i]
                if ymax3 > ymax2:
                    ymax2, ymax3 = ymax3, ymax2
                    if ymax2 > ymax1:
                        ymax1, ymax2 = ymax2, ymax1
    print(ymax1, ymax2, ymax3)
elif len(lmax) == 1:
    print(xmax1, xmin1, xmin2)
elif len(lmax) >= 2:
    if xmax1 * xmax2 * xmax3 >= xmin1 * xmin2 * xmax1:
        print(xmax1, xmax2, xmax3)
    else:
        print(xmin1, xmin2, xmax1)
