map = []
moves = []
map_ = []
max_items = 0
with open("./input2.txt","r") as read:
    met = False
    for line in read:
        if line == "\n":
            met = True
        if met == False:
            map.append(line)
        elif met == True and line != "\n":
            moves.append(line.replace("\n",""))
'''print(map)
print(moves)'''
for box in map:
    print(box.replace("\n",""))

def check(map_):
    count = 0
    for line in map_:
        for box in line:
            if box != "   ":
                count += 1
    if count != 65:
        print(count)
        print("ERROR")
def read_map(map: list):
    global max_items
    for index in range(len(map)):
        index = len(map)-index
        #print(index)
        #print(map[index-1])
        items = str(map[index-1]).replace("\n","").split(" ")
        # removing so many spaces from first line (1 2 3)
        if items.__contains__("1"):
            # its first line
            finished = False
            while finished is False:
                if not items.__contains__(""):
                    finished = True
                    break
                items.remove("")
            for item in items:
                items[items.index(item)] = f" {item} "
            max_items = len(items)
        elif items.__contains__(""):
            finished = False
            count = 0
            while finished is False:
                for item in items:
                    if item == "":
                        count += 1
                        if count %4 == 0:
                            items[items.index(item)] = "   "
                        else:
                            items.remove(item)
                    if not items.__contains__(""):
                        finished = True
        if not items.__contains__(" 1 "):
            while len(items) != len(map_[0]):
                items.append("   ")


        map_.append(items)


    print(f"{max_items} - max_items")


    print(f"len {len(map)}")
def read_instrutciotns(move: str):
    many = int(move.split(" ")[1])
    where = int(move.split(" ")[3])
    to = int(move.split(" ")[5])
    return many, where, to

def do_instruction(many: int, where: int, to:int):
    global max_items
    check(map_)
    # 1 2 1
    what_b = []
    print(f"Instructions {many, where, to}")
    print("MAP - FROM")
    for m in range(len(map_)):
        print(map_[len(map_) - m - 1])
    #loops through the map_ to get the line
    for n in range(len(map_)):
        #print(f"round {n} {many}")
        if many != 0:
            print(f"{len(map_), n, len(map_) - n - 1} - {where - 1} ")
            box = map_[len(map_) - n - 1][where - 1]
            if box != "   ":
                #print(f"box {box}")
                map_[len(map_) - n - 1][where - 1] = "   "
                what_b.append(box)
                many -= 1
            print(f"{len(map_) } {n} {len(map_) -n -1}")
            #print(f"Box from {map_[len(map_) - n - 1]} = {map_[len(map_) - n - 1][where - 1]}")
        else:
            break
    # assign the new positions
    much = len(what_b)
    for n in range(len(map_)):
        if much != 0:
            # I need to check from bottom to top
            # a nd only if I added the box can I do much -= 1
            #print("map")
            #print(f"item to replace = {map_[n][to-1]}")
            if map_[n][to-1] == "   ":
                print(f"{what_b[len(what_b)-1]} added to {n} {to - 1}")
                map_[n][to - 1] = what_b[len(what_b)-1]
                what_b.remove(what_b[len(what_b)-1])
                much -= 1
            #print(f" Boxes {what_b}")
            print("MAP - TO")
            for m in range(len(map_)):
                print(map_[len(map_) - m - 1])
        else:
            break
    # if there are boxes that werent added cuz there wasnt space above existing boxes
    while len(what_b) != 0:
        print(f"Left over {what_b}")
        new_l = []
        #print(to-1)
        print(max_items)
        for num in range(max_items):
            print(num)
            if num == to-1:
                new_l.append(what_b[len(what_b)-1])
                what_b.remove(what_b[len(what_b)-1])
            else:
                new_l.append("   ")
        print(f"{new_l} new line")
        map_.append(new_l)
        print(f" Boxes {what_b}")
        print("MAP")
        for m in range(len(map_)):
            print(map_[len(map_) - m - 1])

    print("MAP - TO FINISHED")
    for m in range(len(map_)):
        print(map_[len(map_) - m - 1])
    print(f"Left over {what_b} !!!")




    # now that we have the boxes we want to move, lets move them


read_map(map)
print("MAP")
for m in range(len(map_)):
    print(map_[len(map_) - m - 1])
print(map_)
for move in moves:
    read = read_instrutciotns(move)
    do_instruction(read[0],read[1],read[2])
print(map_)
