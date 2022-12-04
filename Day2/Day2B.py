from enum import IntEnum
input = open('./input.txt', 'r')
class state(IntEnum):
    LOSE = 0
    DRAW = 1
    WIN = 2
Elf1 = 'A' # A 1 Rock B 2 Paper C 3 Scissors
exState = 'X'
scorey = 0
# those are values that correspond to how moch score would be added to yor score based on if you LOSE DRAW WIN
# (these scores are for the hand you would use in return not for the outcome score)
rock = [3, 1, 2]
paper = [1, 2, 3]
scissor = [2, 3, 1]
# adds 0, 3 or 6 (three times more than the outcome enumerator)
def swindle(state: int):
    global Elf1, scorey
    scorey += state*3
    # gets the score value from corresponding array
    match Elf1:
        case 'A':
            scorey += rock[state]
        case 'B':
            scorey += paper[state]
        case 'C':
            scorey += scissor[state]

# gets the values for outcome of the match and the other elf
for lines in input:
    Elf1 = lines[0]
    exState = lines[2]
    # passes the outcome state to the swindle function
    match exState:
        case 'X': # Lose
            swindle(state.LOSE)
        case 'Y': # Draw
            swindle(state.DRAW)
        case 'Z': # Win
            swindle(state.WIN)

print(scorey)