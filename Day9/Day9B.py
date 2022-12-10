text =  open('input.txt', 'r')
Head = (0,0)
Tail = [(0,0) for i in range(9)]
print(Tail)
tailPositions = set()
DV = {'L': 0, 'U': -1, 'R': 0, 'D': 1}
DH = {'L': -1, 'U': 0, 'R': 1, 'D': 0}

def adjustTail(H,T):
    dr = (H[0]-T[0])
    dc = (H[1]-T[1])
    if abs(dr)<=1 and abs(dc)<=1:
        pass
    elif abs(dr)>=2 and abs(dc)>=2:
        T = (H[0]-1 if T[0]<H[0] else H[0]+1, H[1]-1 if T[1]<H[1] else H[1]+1)
    elif abs(dr)>=2:
        T = (H[0]-1 if T[0]<H[0] else H[0]+1, H[1])
    elif abs(dc)>=2:
        T = (H[0], H[1]-1 if T[1]<H[1] else H[1]+1)
    return T

for line in text:
    line = line.replace('\n', '')
    direction, amount = line.split(' ')
    amount = int(amount)
    for i in range(amount):
        Head = (Head[0]+ DH[direction], Head[1] + DV[direction])
        Tail[0] = adjustTail(Head, Tail[0]) # type: ignore
        for i in range(1, 9):
            Tail[i] = adjustTail(Tail[i-1], Tail[i]) # type: ignore
        tailPositions.add(Tail[8])   

  
print(len(tailPositions))