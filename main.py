myDict = {}
myfile = open('input.txt', 'r', encoding='utf8')
mylist = []
partylist = []
su = allsum = 0
for line in myfile.readlines():
    party = line[:line.rfind(' ')].strip()
    partylist.append([0, party, 0, 0])
    myDict[party] = int(line[line.rfind(' '):])
    su += int(line[line.rfind(' '):])
myfile.close()
fz = su / 450
for x in myDict:
    vo = myDict[x]
    for i in range(len(partylist)):
        if partylist[i][1] == x:
            partylist[i][0] = vo
            partylist[i][2] = int(vo // fz)
            partylist[i][3] = vo % fz
            break
        #    mylist.append([vo, x, int(vo // fz), vo % fz])
    allsum += int(myDict[x] // fz)
while 450 - allsum > 0:
    for xp in sorted(partylist, key=lambda x: -x[3]):
        xp[2] += 1
        allsum += 1
        if 450 - allsum == 0:
            break
for i in partylist:
    print(i[1], i[2])
