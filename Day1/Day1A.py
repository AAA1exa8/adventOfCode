input = open('./input2.txt', 'r')
currentElf = 1
currentElfValue = 0
highestElf = 0
highestElfValue = 0

# changes highest elf value to the current elf value if it higher
def compare():
    global currentElf, highestElf, currentElfValue, highestElfValue
    if currentElfValue > highestElfValue:
        highestElf = currentElf
        highestElfValue = currentElfValue

# if the line is not new line it adds value of the to the current elf value end skips to next loop
for lines in input:
    if lines != '\n':
        currentElfValue += int(lines)
        continue
    # if the line is new line it runs the compare function then resets the current elf values
    compare()
    currentElf += 1
    currentElfValue = 0
# runs the compare function for thel last elf then prints solution
compare()
print(highestElf, '\n', highestElfValue)