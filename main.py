# генеалогическое дерево
def addchild (parent, tempdict, theTree):
    s = 0
    while len(tempdict) > 0:
        if parent == tempdict[s][0]:
            chi = {tempdict[s][1]: {}}
            theTree.setdefault(parent, []).append(chi)
            tempdict.remove(tempdict[s])
        else:
            s += 1
            if s == len(tempdict):
                for x in range(len(theTree[parent])):
                    sdt = list(theTree[parent][x].items())[0][0]
                    print(theTree[parent].keys())
#                    parent = theTree[parent][x]
                    print(str(theTree[parent]))
                    parent = theTree[parent]
                    theTree = addchild(parent, tempdict, theTree[parent])


tempdict = []
theTree = {}
parents = set()
children = set()
myfile = open('input.txt', 'r', encoding='utf8')
n = int(myfile.readline())
for i in range(n - 1):
    x = myfile.readline().split()
    parent, child = x[1].strip(), x[0].strip()
    parents.add(parent)
    children.add(child)
    tempdict.append([parent, child])
parents -= children
parent = parents.pop()
theTree = addchild(parent, tempdict, theTree)

print(theTree)



myfile.close()
