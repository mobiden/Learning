newfile = open('input.txt', 'r', encoding='utf-8')
lines = newfile.readlines()
s9 = s10 = s11 = 0
t9 = t10 = t11 = 0
S_end = []
for li in lines:
    lin = li.split(' ')
    lin = (lin[0], lin[1], int(lin[2]), int(lin[3]))
    S_end.append(lin)
newfile.close()
S_end.sort()
tofile = open('output.txt', 'w', encoding='utf-8')
for i in S_end:
    print(i[0], i[1], i[3], file=tofile)
tofile.close()
