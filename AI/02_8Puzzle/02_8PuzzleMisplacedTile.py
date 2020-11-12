allChange = []

def checkPresent(state):
    for x in allChange:
        if(x == state):
            return 0
    
    allChange.append(state)

    return 1

def checkMoves(src): 
    emptyPos = src.index(0)

    moves = []

    if emptyPos not in [0,1,2]: 
        moves.append('u')
    if emptyPos not in [6,7,8]: 
        moves.append('d')
    if emptyPos not in [0,3,6]: 
        moves.append('l')
    if emptyPos not in [2,5,8]: 
        moves.append('r')

    return moves

def misplaced(target,temp):
    count = 0
    for i in range(9):
        if(target[i] != temp[i]):
            count += 1
    return count

def smallestMisplacedMove(moves,src,target): 
    least = 10
    emptyPos = src.index(0)

    nextStep = []

    for x in moves:
        temp = src.copy()
        if x == 'u':
            temp[emptyPos], temp[emptyPos-3] = temp[emptyPos-3], temp[emptyPos]
        if x == 'd':
            temp[emptyPos], temp[emptyPos+3] = temp[emptyPos+3], temp[emptyPos]
        if x == 'r':
            temp[emptyPos], temp[emptyPos+1] = temp[emptyPos+1], temp[emptyPos]
        if x == 'l':
            temp[emptyPos], temp[emptyPos-1] = temp[emptyPos-1], temp[emptyPos]
        
        noOfMisplaced = misplaced(target,temp)

        if(least > noOfMisplaced):
            if(checkPresent(temp)):
                least = noOfMisplaced
                dir = x
                nextStep = temp

    if(nextStep == []):
        print("No solution")
        exit(0)

    print("Direction - ",end="")
    print(dir)
    return nextStep

def printStep(src):
    i = 0

    print("\n")
    
    for j in range(3):
        print(src[i],end=" ")
        print(src[i+1],end=" ")
        print(src[i+2])
        i += 3
    print("\n")

def match(src,target):
    flag = 1
    count = 0

    while(flag):
        count += 1
        printStep(src)
        if(misplaced(src,target) > 0):
            moves = checkMoves(src)
            src = smallestMisplacedMove(moves,src,target)
        else:
            print("Success")
            print("Steps = ",end="")
            print(count)
            flag = 0

def play():

    src = []
    target = []

    print("Enter source:(0 in empty space) ")
    for i in range(3):
        for j in range(3):
            src.append(int(input()))
    
    print("Enter target:(0 in empty space) ")
    for i in range(3):
        for j in range(3):
            target.append(int(input()))

    match(src,target)

if __name__ == "__main__":
    play()