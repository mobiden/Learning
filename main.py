# подсчет продаж и ассортимента по покупателям
itemDict = {}
myfile = open('input.txt', 'r', encoding='utf8')
for line in myfile:
    xline = list(line.split())
    if xline[0] not in itemDict:
        itemDict[xline[0]] = {}
    if xline[1] not in itemDict[xline[0]]:
        itemDict[xline[0]][xline[1]] = 0
    itemDict[xline[0]][xline[1]] += int(xline[2])
myfile.close()
for fam in sorted(itemDict):
    print(fam + ':')
    for i in sorted(itemDict[fam]):
        print(i, itemDict[fam][i])
