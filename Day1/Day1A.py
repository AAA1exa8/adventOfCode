input = open('./input2.txt', 'r')
currentElf = 1
currentElfValue = 0
highestElf = 0
highestElfValue = 0

def change():
    global currentElf, highestElf, currentElfValue, highestElfValue
    if currentElfValue > highestElfValue:
        highestElf = currentElf
        highestElfValue = currentElfValue
    currentElf += 1
    currentElfValue = 0


for lines in input:
    if lines != '\n':
        currentElfValue += int(lines)
        continue
    change()
change()
print(highestElf, '\n', highestElfValue)