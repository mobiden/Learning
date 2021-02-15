# минимальный бал ЕГЭ
myfile = open('input.txt', 'r', encoding='utf-8')
lines = myfile.readlines()
first = True
n = 0
stu = []
su = nsu = 0
mylist = [0] * 301
for x in lines:
    if first:
        n = int(x)
        first = False
    else:
        peo = tuple(x.split())
        if int(peo[-3]) >= 40 and int(peo[-2]) >= 40 and int(peo[-1]) >= 40:
            s = int(peo[-3]) + int(peo[-2]) + int(peo[-1])
            mylist[s] += 1
            pball = (s, int(peo[-3]), int(peo[-2]), int(peo[-1]))
            stu.append(pball)
            if su < s:
                su = s
                nsu = 1
            elif su == s:
                nsu += 1
myfile.close()
wball = -1
tempball = 0
if len(stu) <= n:
    wball = 0
elif nsu > n:
    wball = 1
else:
    for x in range(len(mylist) - 1, -1, -1):
        if mylist[x] > 0:
            tempball += mylist[x]

            if tempball > n:
                wball = myball
                break
            else:
                myball = x

openfile = open('output.txt', 'w', encoding='utf-8')
print(wball, file=openfile)
openfile.close()
