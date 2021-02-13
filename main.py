n = int(input())
uch = []
for x in range(n):
    nuch = list(input().split())
    nuch = [int(nuch[1]), nuch[0]]
    uch.append(nuch)

uch.sort(reverse=True)
for x in range(n):
    print(uch[x][1])
