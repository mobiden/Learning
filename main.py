# генеалогическое дерево
def nupa(person, parent, theTree):
    for x in theTree:
        if x == person:
            if theTree[x] == parent:
                return 1
            else:
                return nupa(theTree[x], parent, theTree) + 1


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
    theTree.update({child: parent})
myfile.close()
parents -= children
allpeople = parents | children
parent = parents.pop()
for person in sorted(allpeople):
    if person == parent:
        print(person, 0)
    else:
        print(person, nupa(person, parent, theTree))
