def makeTuples(a):
    aList = list()
    for i in a:
        p1 = [(i,j) for j in a]
        aList = aList + p1
    return aList

def makeBlockedList():
    iNums = [1,3,6,8,11,13]
    iNums2 = [5,9]
    iNums3 = [6,8]
    aList = makeTuples(iNums)
    bList = makeTuples(iNums2)
    cList = makeTuples(iNums3)
    return aList + bList + cList

def addTuples(tup1,tup2):
    return tuple(sum(x) for x in zip(tup1, tup2))

def checkBounds(coords,size):
    if -1 in coords:
        return False
    for i in coords:
        if i >= size:
            return False
    return True

def validMove(player,direction,size):
    bl = makeBlockedList()
    coords = player["location"]
    nCoords = addTuples(coords,direction)
    if(checkBounds(nCoords,size)):
        if nCoords in bl:
            return False
        player["location"] = nCoords
        return True
    return False

def checkGoal(player,goal):
    if(goal == player["location"]):
        print("Congrats you've reached the goal")
        return True
    return False
