input = open('./input.txt', 'r')

Elf1 = 'A' # A 1 Rock B 2 Paper C 3 Scissors
exState = 'X'
scorey = 0


def swindle(state: int):
    global Elf1, scorey
    scorey += state
    match Elf1:
        case 'A':
            match state:
                case 0:
                    scorey += 3
                case 3:
                    scorey += 1
                case 6:
                    scorey += 2
        case 'B':
            match state:
                case 0:
                    scorey += 1
                case 3:
                    scorey += 2
                case 6:
                    scorey += 3
        case 'C':
            match state:
                case 0:
                    scorey += 2
                case 3:
                    scorey += 3
                case 6:
                    scorey += 1


for lines in input:
    Elf1 = lines[0]
    exState = lines[2]
    match exState:
        case 'X': # Lose
            swindle(0)
        case 'Y': # Draw
            swindle(3)
        case 'Z': # Win
            swindle(6)

print(scorey)