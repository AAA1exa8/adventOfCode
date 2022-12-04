text = open('./input.txt', 'r')

array = []
repeats = 0
for lines in text:
    tmp1 = lines.split(',')
    for items in tmp1:
        items = items.replace('\n', '')
        tmp2 = items.split('-')
        array.append(tmp2)
    array1 = set(range(int(array[0][0]), int(array[0][1])+1))
    array2 = set(range(int(array[1][0]), int(array[1][1])+1))
    if (array1 & array2) != set():
        repeats += 1
    array = []

print(repeats)