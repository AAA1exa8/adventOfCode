import string

text = open('./input.txt', 'r')
iteration = 0
num = 0
char = 0
rux1, rux2, rux3 = set(), set(), set()

# populates 1st, 2nd, 3rd ruxack 
for lines in text:
    match iteration:
        case 0:
            rux1 = set(lines[:-1])
            iteration+=1
        case 1:
            rux2 = set(lines[:-1])
            iteration+=1
        case 2:
            # on the 3rd iteration it gets char intersecting all three ruxsacks and gets its value
            rux3 = set(lines[:-1])
            iteration = 0
            char = str(rux1 & rux2 & rux3)[2]
            num += string.ascii_lowercase.index(char) + 1 if char.islower() else string.ascii_uppercase.index(char) + 27                   

print(num)