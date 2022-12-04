input = open('./input.txt', 'r')

Elf1 = 'A'
Elfy = 'X'
scorey = 0
for lines in input:
    # sets the values of both elfes
    Elf1 = lines[0]
    Elfy = lines[2]
    # adds to your score value based on what was your hand
    match Elfy:
        case 'X': # Rock
            scorey += 1
        case 'Y': # Paper
            scorey += 2
        case 'Z': # Scissor
            scorey += 3
    # adds to your score value based on if you won or lost
    match [Elfy, Elf1]:
        case ['X', 'A'] | ['Y', 'B'] | ['Z', 'C']:
            scorey += 3
        case ['X', 'C'] | ['Y', 'A'] | ['Z', 'B']:
            scorey += 6
print(scorey)