instructions = open('input.txt', 'r')
register = 1
cycle = 0
strength = 0
chceckCycles = [20, 60, 100, 140, 180, 220]
def check():
    global strength
    if chceckCycles.count(cycle) > 0:
        strength += (register * cycle)

def noop():
    global cycle
    cycle += 1
    check()

def addx(value: int):
    global register, cycle
    for i in range(2):
        cycle += 1
        check()
    else:
        register += value
    

for instruction in instructions:
    instruction = instruction.replace('\n','')
    match instruction[:4]:
        case 'addx':
            addx(int(instruction.split(' ')[1]))
        case 'noop':
            noop()

print(strength)