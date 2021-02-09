koo = []
answer = ''
for i in range(8):
    l = list(map(int, input().split()))
    for s in range(i):
        if koo[s][0] == l[0] or koo[s][1] == l[1]:
            answer = 'YES'
            break
        elif abs(koo[s][0] - l[0]) == abs(koo[s][1] - l[1]):
            answer = 'YES'
            break
        else:
            answer = 'NO'
    if answer == 'YES':
        break
    koo.append(l)
print(answer)
