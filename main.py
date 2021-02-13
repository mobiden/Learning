myfile = open('input.txt', 'r', encoding='utf-8')
lines = myfile.readlines()
valuepoblist = [0, 0, 0]
sizepoblist = [0, 0, 0]
for line in lines:
    peo = list(line.split())
    peo = (peo[0], peo[1], int(peo[2]), int(peo[3]))
    if valuepoblist[peo[2] - 9] < peo[3]:
        valuepoblist[peo[2] - 9] = peo[3]
        sizepoblist[peo[2] - 9] = 1
    elif valuepoblist[peo[2] - 9] == peo[3]:
        sizepoblist[peo[2] - 9] += 1
myfile.close()

print(*sizepoblist)
