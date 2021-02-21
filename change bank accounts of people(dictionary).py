# change bank accounts of people
acc = {}
myfile = open('input.txt', 'r', encoding='utf8')
for line in myfile:
    xli = line.split()
    if xli[0] == 'DEPOSIT':
        acc[xli[1]] = acc.get(xli[1], 0) + int(xli[2])
    elif xli[0] == 'WITHDRAW':
        acc[xli[1]] = acc.get(xli[1], 0) - int(xli[2])
    elif xli[0] == 'BALANCE':
        if xli[1] in acc:
            print(acc[xli[1]])
        else:
            print('ERROR')
    elif xli[0] == 'TRANSFER':
        acc[xli[2]] = acc.get(xli[2], 0) + int(xli[3])
        acc[xli[1]] = acc.get(xli[1], 0) - int(xli[3])
    elif xli[0] == 'INCOME':
        for x in acc:
            if acc[x] > 0:
                p = int(xli[1]) / 100
                acc[x] = int((1 + p) * acc[x])
