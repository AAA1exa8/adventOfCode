text = open('input.txt', 'r')
iterator = 0
count = 0
highestScene = 0
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

def scenic(row, column, tree):
    global count, forrest, highestScene
    wLine = forrest[row][:column]
    wLine.reverse()
    eLine = forrest[row][column+1:]
    nLine = turnedForrest[column][:row]
    nLine.reverse()
    sLine = turnedForrest[column][row+1:]
    north = calcScenic(nLine, tree)
    south = calcScenic(sLine, tree)
    west = calcScenic(wLine, tree)
    east = calcScenic(eLine, tree)
    if (west * south * north * east) > highestScene:
        highestScene = (west * south * north * east)

def calcScenic(line: list, tree: int) -> int:
    count = 0
    for i in line:
        if i < tree:
            count += 1
        else:
            count +=1
            break
    return count


    


def counting():
    global count, forrest
    for row in range(len(forrest)):
        line = forrest[row]
        for column in range(len(line)):
            tree = line[column]
            tLine = turnedForrest[column]
            tColumn = row
            if (tree == max(line[:column+1]) and line[:column+1].count(tree) == 1) or (tree == max(line[column:]) and line[column:].count(tree) == 1):
                scenic(row, column, tree)
            elif (tree == max(tLine[:tColumn+1]) and tLine[:tColumn+1].count(tree) == 1) or (tree == max(tLine[tColumn:]) and tLine[tColumn:].count(tree) == 1):
                scenic(row, column, tree)


counting()

print(highestScene)