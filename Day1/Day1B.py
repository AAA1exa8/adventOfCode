input = open('./input2.txt', 'r')
currentElfValue = 0
highestElfValue = [0, 0, 0]

# runs trough highest Elf Value and replaces one of the elements if it is lower then the current elf value
# if there is such value it stops the function
def compare():
    for i in range(0, 3):
        if currentElfValue > highestElfValue[i]:
            highestElfValue[i] = currentElfValue
            return
# if the line is not new line the line is added as int to current elf value then skips to next iteration
for lines in input:
    if lines != '\n':
        currentElfValue += int(lines)
        continue
    # if the line is new line it runs the compare fucntion
    #! then sorts the highestElfValue array from lowest to highest
    # then resets current elf value
    compare()
    highestElfValue.sort()
    currentElfValue = 0
# runs compare for the last elf
compare()
print(sum(highestElfValue), highestElfValue)