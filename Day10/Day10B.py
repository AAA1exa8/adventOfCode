instructions = open('input.txt', 'r')
register = 1
cycle = -1
screen = list([list('.'*40),list('.'*40),list('.'*40),list('.'*40),list('.'*40),list('.'*40)])

def draw():
    if cycle % 40 == register or cycle % 40 == register + 1 or cycle % 40 == register -1 :
        screen[cycle // 40][cycle % 40] = '#'

def noop():
    global cycle
    cycle += 1
    draw()

def addx(value: int):
    global register, cycle
    for i in range(2):
        cycle += 1
        draw()
    else:
        register += value
    

for instruction in instructions:
    instruction = instruction.replace('\n','')
    match instruction[:4]:
        case 'addx':
            addx(int(instruction.split(' ')[1]))
        case 'noop':
            noop()

for i in screen:
    for n in i:
        print(n, end='')
    print()