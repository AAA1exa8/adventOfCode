input = open('./input2.txt', 'r')
currentElfValue = 0
highestElfValue = [0, 0, 0]

def checkElfValue():
    for i in range(0, 3):
        if currentElfValue > highestElfValue[i]:
            highestElfValue[i] = currentElfValue
            break

for lines in input:
    if lines != '\n':
        currentElfValue += int(lines)
        continue
    checkElfValue()
    highestElfValue.sort()
    currentElfValue = 0

checkElfValue()
print(sum(highestElfValue), highestElfValue)