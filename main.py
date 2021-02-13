newfile = open('input.txt', 'r', encoding='utf-8')
lines = newfile.readlines()

S_end = [0, 0, 0]
for li in lines:
    lin = li.split(' ')
    lin = (lin[0], lin[1], int(lin[2]), int(lin[3]))
    if S_end[lin[2] - 9] < lin[3]:
        S_end[lin[2] - 9] = lin[3]
newfile.close()
# tofile = open('output.txt', 'w', encoding='utf-8')
# tofile.close()
print(*S_end)
