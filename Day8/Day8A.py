text = open('input.txt', 'r')
iterator = 0
count = 0
forrest = list()
turnedForrest = list()

for line in text:
    line = line.replace('\n', '')
    forrest.append(list())
    for tree in line:
        forrest[iterator].append(int(tree))
    iterator += 1
for i in range(len(forrest[0])):
    turnedForrest.append(list())
    for n in range(len(forrest)):
        turnedForrest[i].append(forrest[n][i])

def counting(localForrest: list):
    global count
    for row in range(len(localForrest)):
        line = localForrest[row]
        for column in range(len(line)):
            tree = line[column]
            tLine = turnedForrest[column]
            tColumn = row
            if row == 0 or row == len(localForrest) -1 or column == 0 or column == len(line) -1:
                count += 1
            else:
                if (tree == max(line[:column+1]) and line[:column+1].count(tree) == 1) or (tree == max(line[column:]) and line[column:].count(tree) == 1):
                    count += 1
                elif (tree == max(tLine[:tColumn+1]) and tLine[:tColumn+1].count(tree) == 1) or (tree == max(tLine[tColumn:]) and tLine[tColumn:].count(tree) == 1):
                    count += 1


counting(forrest)

print(count)