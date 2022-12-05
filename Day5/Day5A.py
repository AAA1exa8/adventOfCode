commands = open('./input.txt', 'r')

cargo = [['Z', 'N'], ['M', 'C', 'D'],['P']]
cargo2 = [['P', 'F', 'M', 'Q', 'W', 'G', 'R', 'T'], 
         ['H', 'F', 'R'], 
         ['P', 'Z', 'R', 'V', 'G', 'H', 'S', 'D'],
         ['Q', 'H', 'P', 'B', 'F', 'W', 'G'],
         ['P', 'S', 'M', 'J', 'H'],
         ['M', 'Z', 'T', 'H', 'S', 'R', 'P', 'L'],
         ['P', 'T', 'H', 'N', 'M', 'L'],
         ['F', 'D', 'Q', 'R'],
         ['D', 'S', 'C', 'N', 'L', 'P', 'H']]

skip = False
for command in commands:
    if command != '\n' and not skip:
        continue
    elif command == '\n':
        skip = True
        continue
    command = command.replace('\n', '').split(' ')
    howMuch = int(command[1])
    fromWhere = int(command[3])
    toWhere = int(command[5])
    position = len(cargo2[fromWhere - 1]) - 1
    for i in range(howMuch):
        cargo2[toWhere - 1].append(cargo2[fromWhere - 1][position - i])
        cargo2[fromWhere - 1].pop()

for char in cargo2:
    print(char[-1:][0], end='')