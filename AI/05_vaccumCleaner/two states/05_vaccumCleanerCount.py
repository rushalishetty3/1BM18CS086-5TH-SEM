import random

environment = {'A': 0, 'B': 0} # assumed initial state
cleanCount = {'A': 0, 'B': 0}

def countMore(x):
    print("Cleaned two times at "+ x + " location.")
    exit(0)

def checkDirt():
    return random.randint(0,1)

def setEnvironment():
    environment['A'] = checkDirt()
    environment['B'] = checkDirt()

    print("\nNew environment: ",end="")
    print(environment)

def cleaned():
    print("\nBoth the locations are cleaned.")
    exit(0)

def newState(current):
    setEnvironment()

    if(environment['A'] == 0 and environment['B'] == 0):
        cleaned()
    else:
        cleanAt(current)

def cleanAt(state):

    print("\nVaccum cleaner at "+state+" location.")
    dirt = environment[state] # 0-nodirt 1-dirt

    if dirt == 1:
        if cleanCount[state] == 2:
            countMore(state)
        cleanCount[state] += 1
        print("Location "+ state +" is dirty.")
        print("Vaccum cleaner cleaned the dirt at "+state+".")
        environment[state] = 0
    else:
        print("Location "+state+" is clean.")
    
    if state == 'A':
        if environment['B']:
            print("Vaccum cleaner moving to B location.")
            cleanAt('B')
    else:
        if environment['A']:
            print("Vaccum cleaner moving to A location.")
            cleanAt('A')

    print("\nCurrent environment: ",end="")
    print(environment)

    newState(state)
 
def start():
    print("Enter starting state(A,B): ",end="")
    current = input()
    newState(current)

if __name__ == "__main__":
    start()