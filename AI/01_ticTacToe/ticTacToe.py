import random

board = [0,0,0,0,0,0,0,0,0]
winningPosition = [ [0,4,8] , [2,4,6] , [0,3,6], [1,4,7] , [0,1,2] , [3,4,5] , [6,7,8] , [2,5,8] ]

def boardDisplay():
    print("----------")
    print(board[0],end="")
    print(" | ",end="")
    print(board[1],end="")
    print(" | ",end="")
    print(board[2])
    print("----------")
    print(board[3],end="")
    print(" | ",end="")
    print(board[4],end="")
    print(" | ",end="")
    print(board[5])
    print("----------")
    print(board[6],end="")
    print(" | ",end="")
    print(board[7],end="")
    print(" | ",end="")
    print(board[8])
    print("----------")

def checkIfAvailable(pos): 
    if(board[pos] == 0):
        return 1
    else:
        return 0

def checkWin(player):
    for x in winningPosition:
        if board[x[0]]==board[x[1]] and board[x[1]]==board[x[2]] and board[x[0]]!=0:
            print(player+" Won")
            return 0
    for i in board:
        if i==0:
            return 1
    
    print("Draw Match")

def algoWin():
    n=-1

    for x in winningPosition:
        if (board[x[0]]==2 and board[x[1]]==2) and checkIfAvailable(x[2])==1:
            n = x[2]
            break
        elif (board[x[1]]==2 and board[x[2]]==2) and checkIfAvailable(x[0])==1:
            n = x[0]
            break
        elif (board[x[0]]==2 and board[x[2]]==2) and checkIfAvailable(x[1])==1:
            n = x[1]
            break

    return n

def stopPlayer():
    n = -1

    for x in winningPosition:
        if (board[x[0]]==1 and board[x[1]]==1) and checkIfAvailable(x[2])==1:
            n = x[2]
            break
        elif (board[x[1]]==1 and board[x[2]]==1) and checkIfAvailable(x[0])==1:
            n = x[0]
            break
        elif (board[x[0]]==1 and board[x[2]]==1) and checkIfAvailable(x[1])==1:
            n = x[1]
            break
    return n

def algoTryWin():
    n = -1

    for x in winningPosition:
        if board[x[0]]==1:
            if checkIfAvailable(x[2]==1):
                n = x[2]
                break
            elif checkIfAvailable(x[1]==1):
                n = x[1]
                break
        elif board[x[1]]==1:
            if checkIfAvailable(x[0]==1):
                n = x[0]
                break
            elif checkIfAvailable(x[2]==1):
                n = x[2]
                break
        elif board[x[2]]==1:
            if checkIfAvailable(x[0]==1):
                n = x[0]
                break
            elif checkIfAvailable(x[1]==1):
                n = x[1]
                break
    
    return n

def randomPos():
    while(1):
        n = random.randint(0,9)
        if checkIfAvailable(n)==1:
            return n


def algoPlay():
    n = algoWin()

    if n==-1:
        n = stopPlayer()
    
    if n==-1:
        n = algoTryWin()

    if n==-1:
        n = randomPos()

    print("Algorithm inserted at ",end="")
    print(n)
    board[n] = 2

def play():
    boardDisplay()
    flag = 1
    while(flag):
        print("\n---Player Turn--\n")
        playerPos = int(input("\nEnter position(0-9): "))
        if(checkIfAvailable(playerPos) == 1):
            board[playerPos] = 1 
            boardDisplay()
            flag = checkWin("Player")
            if flag==1:
                print("\n---Algorithm Turn--\n")
                algoPlay()
                boardDisplay()
                flag = checkWin("Algorithm")
        else:
            print("Can't insert in this position")

if __name__ == "__main__":
    play()