from collections import defaultdict

data = open('input.txt', 'r')
amountOfData = 1000000000

lines = list()
for line in data:
    lines.append(line.replace('\n', ''))

SZ = defaultdict(int)
path = []
for line in lines:
    line = line.split(' ')
    if line[1] == 'cd':
        if line[2] == '..':
            path.pop()
        else:
            path.append(line[2])
    elif line[1] == 'ls':
        continue
    elif line[0] == 'dir':
        continue
    else:
        sz = int(line[0])
        for i in range(1, len(path)+1):
            SZ['/'.join(path[:i])] += sz


max_used = 40000000
total_used = SZ['/']
need_to_free = total_used - max_used

for k,v in SZ.items():
    if v>=need_to_free:
        amountOfData = min(amountOfData, v)
print(amountOfData)