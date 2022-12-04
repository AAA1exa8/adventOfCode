text = open('./input2.txt', 'r')

array = []
repeats = 0
for lines in text:
    # splits the line in two parts by ,
    tmp1 = lines.split(',')
    for items in tmp1:
        # splits each part of tmp1 by - and adds it to array
        array.append(items.replace('\n', '').split('-'))
    # populates set 1 and 2 by values from input
    set1 = set(range(int(array[0][0]), int(array[0][1])+1))
    set2 = set(range(int(array[1][0]), int(array[1][1])+1))
    # if intersect of set 1 and 2 is equal to set 1 or 2 it adds one to repeats
    # (if one of the sets is in fully in the other it adds one to repeats)
    if ((set1 & set2) == set1) or ((set1 & set2) == set2):
        repeats += 1
    # resets array to empty
    array = []

print(repeats)