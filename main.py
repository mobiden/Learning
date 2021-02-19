myDict = {}
myfile = open('input.txt', 'r', encoding='utf8')
mylist = []
for line in myfile.readlines():
    listname = line.split()
    for word in listname:
        myDict[word] = myDict.get(word, 0) + 1
myfile.close()
for word in myDict:
    mylist.append((-myDict[word], word))
for word in sorted(mylist):
    print(word[1])
