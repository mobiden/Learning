l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))


def merge(l1, l2):
    c = []
    j = i = 0
    while i <= len(l1) - 1:
        if l1[i] < l2[j]:
            c.append(l1[i])
            i += 1
        else:
            c.append(l2[j])
            j += 1
            if j > len(l2) - 1:
                if i < len(l1):
                    for k in range(i, len(l1)):
                        c.append(l1[k])
                break
    if j < len(l2) - 1:
        for k in range(j, len(l2)):
            c.append((l2[k]))
    return c

print(*merge(l1, l2))
