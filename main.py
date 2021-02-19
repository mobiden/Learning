myfile = open('input.txt', 'r', encoding='utf8')
countries = {}
n = int(myfile.readline())
for nu in range(n):
    line = myfile.readline()
    coun = line[:line.find(' ')].strip()
    city = line[line.find(' ') + 1:].split()
    for ci in city:
        countries[ci] = []
        countries[ci].append(coun)
m = int(myfile.readline())
for nu in range(m):
    line = myfile.readline().strip()
    if line in countries:
        print(*countries[line])

myfile.close()
