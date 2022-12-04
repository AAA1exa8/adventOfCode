text = open('./input2.txt', 'r')

array = []
repeats = 0
for lines in text:
    tmp1 = lines.split(',')
    #array.append(items.replace('\n', '').split('-') for items in tmp1)
    for items in tmp1:
        array.append(items.replace('\n', '').split('-'))
    array1 = set(range(int(array[0][0]), int(array[0][1])+1))
    array2 = set(range(int(array[1][0]), int(array[1][1])+1))
    if ((array1 & array2) == array1) or ((array1 & array2) == array2):
        repeats += 1
    array = []

print(repeats)