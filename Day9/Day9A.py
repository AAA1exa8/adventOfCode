text =  open('input.txt', 'r')
Head = (0,0)
Tail = (0,0)
tailPositions = set()
DV = {'L': 0, 'U': -1, 'R': 0, 'D': 1}
DH = {'L': -1, 'U': 0, 'R': 1, 'D': 0}

def adjustTail():
    global Tail
    dr = (Head[0]-Tail[0])
    dc = (Head[1]-Tail[1])
    if abs(dr)<=1 and abs(dc)<=1:
        pass
    elif abs(dr)>=2 and abs(dc)>=2:
        Tail = (Head[0]-1 if Tail[0]<Head[0] else Head[0]+1, Head[1]-1 if Tail[1]<Head[1] else Head[1]+1)
    elif abs(dr)>=2:
        Tail = (Head[0]-1 if Tail[0]<Head[0] else Head[0]+1, Head[1])
    elif abs(dc)>=2:
        Tail = (Head[0], Head[1]-1 if Tail[1]<Head[1] else Head[1]+1)

for line in text:
    line = line.replace('\n', '')
    direction, amount = line.split(' ')
    amount = int(amount)
    for i in range(amount):
        Head = (Head[0]+ DH[direction], Head[1] + DV[direction])
        adjustTail()
        tailPositions.add(Tail)   

print(len(tailPositions))  
