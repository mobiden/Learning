l = list(map(int, input().split()))
# kegli i broski

kegli = [kegli for kegli in range(l[0])]
num = l[0]
for i in range(l[1]):
    k = list(map(int, input().split()))
# from l to r
    for keg in range(k[0] - 1, k[1]):
        if kegli.count(keg) > 0:
            kegli.remove(keg)

for ske in range(num):
    if kegli.count(ske) > 0:
        print('I', end='')
    else:
        print('.', end='')
