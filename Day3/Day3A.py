import string

text = open('./input2.txt', 'r')
num = 0
for lines in text:
    # converts the string to char array
    sack = list([char for char in lines])
    # splits the sack the first and second half
    rux1 = set(sack[:int((len(sack)+1)/2 -1)])
    rux2 = set(sack[int((len(sack)+1)/2 -1):])
    # gets intersect og the ruxacks
    char = str(rux1 & rux2)[2]
    # gets position of the char and adds it to num
    num += string.ascii_lowercase.index(char) + 1 if char.islower() else string.ascii_uppercase.index(char) + 27
   
print(num)