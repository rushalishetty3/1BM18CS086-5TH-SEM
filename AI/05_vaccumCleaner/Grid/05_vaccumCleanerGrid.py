import math

grid = []
neigbhours = [[0,1,"right"],[1,0,"down"],[0,-1,"left"],[-1,0,"up"]]

def printDir(end,start):
    x = start[0] - end[0]
    y = start[1] - end[1]

    for l in range(abs(x)):
        if x > 0:
            print("Move up")
        elif x < 0:
            print("Move down")

    for l in range(abs(y)):
        if y > 0:
            print("Move left")
        elif y < 0:
            print("Move right")
            

def euclidDist(n,m,x):
    dist = float(math.sqrt((n-x[0])**2+(m-x[1])**2))
    return dist

def searchDirt(m,n,current):
    min = 999
    a = []

    for i in range(m):
        for j in range(n):
            if(grid[i][j]):
                if min > euclidDist(i,j,current):
                    min = euclidDist(i,j,current)
                    a = []
                    a.append(i)
                    a.append(j)
    return a


def check(m,n):
    for i in range(m):
        for j in range(n):
            if(grid[i][j]):
                return True
    
    return False

def clean(m,n,current):

    while(check(m,n)):
        if grid[current[0]][current[1]]:
            grid[current[0]][current[1]] = 0
            print("Cleaned ",str(current[0])," ",str(current[1]))  
        
        nextStep = []

        for x in neigbhours:
            a = []
            a.append(current[0]+x[0])
            a.append(current[1]+x[1])
            a.append(x[2])
            if a[0]>-1 and a[0]<m and a[1]>-1 and a[1]<n:
                if(grid[a[0]][a[1]]):
                    nextStep.append(a)
                    break

        if nextStep:
            print("Move ",nextStep[0][2])
            clean(m,n,nextStep[0])
        else:
            nearestDirt = searchDirt(m,n,current)
            if nearestDirt: 
                printDir(nearestDirt,current)
            clean(m,n,nearestDirt)

def start():
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of cols: "))

    print("Enter state: ")
    for i in range(m):
        a = []
        a = list(map(int, input().split(" ")))
        grid.append(a)

    start = []

    start = list(map(int, input("Enter start position: ").split(" ")))

    clean(m,n,start)

if __name__ == "__main__":
    start()