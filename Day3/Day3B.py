import string

text = open('./input.txt', 'r')
rext = 0
num = 0
value = 0
rux1, rux2, rux3 = set(), set(), set()

for lines in text:
    match rext:
        case 0:
            rux1 = set(lines[:-1])
            rext+=1
        case 1:
            rux2 = set(lines[:-1])
            rext+=1
        case 2:
            rux3 = set(lines[:-1])
            rext = 0
            value = str(rux1 & rux2 & rux3)[2]
            num += string.ascii_lowercase.index(value) + 1 if value.islower() else string.ascii_uppercase.index(value) + 27                   

print(num)