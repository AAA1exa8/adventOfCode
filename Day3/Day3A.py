import numpy as np
import string

text = open('./input.txt', 'r')
num = 0
for lines in text:
    sack = np.array([char for char in lines])  
    rux1 = sack[range(0, int((sack.size+1)/2 -1))]
    rux2 = sack[range(int((sack.size+1)/2 -1), (sack.size+1)-2)]
    value = str(np.intersect1d(rux1, rux2))[2]
    num += string.ascii_lowercase.index(value) + 1 if value.islower() else string.ascii_uppercase.index(value) + 27
   
print(num)