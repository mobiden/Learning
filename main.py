# проверка контрольной работы
def checkUpper(word):
    x = 0
    for i in word:
        if i.isupper():
            x += 1
            if x > 1:
                break
    return True if x == 1 else False


theDict = {}
nuerr = 0
myfile = open('input.txt', 'r', encoding='utf8')
n = int(myfile.readline())
for i in range(n):
    dword = str(myfile.readline().strip())
    if dword.lower() not in theDict:
        theDict[dword.lower()] = []
    theDict[dword.lower()].append(dword)

for line in myfile.readlines():
    xline = line.split()
    for word in xline:
        if word.lower() not in theDict:
            if not checkUpper(word):
                nuerr += 1
#            else:
#               theDict[word.lower()] = word
        else:
            if word not in theDict[word.lower()]:
                nuerr += 1
print(nuerr)
myfile.close()
