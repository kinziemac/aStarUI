###   Author: Mackenzie Higa - 301229885   ###
###        CMPT 310: Assignment 1          ###

class Index:
    def __init__(self, location, goal, previousIndex):
        self.y = location[0]
        self.x = location[1]
        self.distance = abs(goal[0] - location[0]) + abs(goal[1] - location[1])
        self.pathCost = 0

        if (previousIndex is not None and
            (0 <= self.y < boundary) and
            (0 <= self.x < boundary)
            ):
            self.pathCost = abs(map[self.y][self.x] - mapCoordinateValue(previousIndex)) + 1 + previousIndex.pathCost
        self.aStarValue = self.distance + self.pathCost

def handleParsingStrings(string):
    parsedString = string.replace(",", " ")
    parsedString = parsedString.replace("[", " ")
    parsedString = parsedString.replace("]", " ")
    parsedString = parsedString.split()

    parseLength = len(parsedString)
    for i in range(parseLength):
        parsedString[i] = int(parsedString[i])

    return parsedString

def initializeTxtData():
    file = open("Asst1.data.txt", "r")
    txtDataArray = file.readlines()
    fBoundary = int(txtDataArray[0])
    fStartGoal = handleParsingStrings(txtDataArray[1])
    fStart = [fStartGoal[0], fStartGoal[1]]
    fGoal = [fStartGoal[2], fStartGoal[3]]

    fMap = txtDataArray[2:]
    length = len(fMap)
    for i in range(length):
        fMap[i] = handleParsingStrings(fMap[i])

    return {
        "boundary" : fBoundary,
        "start"    : fStart,
        "goal"     : fGoal,
        "map"      : fMap
        }

def aStarSortedInsert(element, list):
    i = 0
    listLength = len(list)
    inserted = False
    if not inExpandedList(element, list):
        while (i < listLength and inserted == False):
            if element.aStarValue < list[i].aStarValue:
                inserted = True
                list.insert(i, element)
            i += 1

        if inserted == False:
            list.append(element)

def bestFirstInsert(element, list):
    i = 0
    listLength = len(list)
    inserted = False
    while (i < listLength and inserted == False and not inExpandedList(element, list)):
        if (element.distance <= list[i].distance):
            inserted = True
            list.insert(i, element)
        i += 1

    if inserted == False:
        list.append(element)

def createPath(pathList, expandedList):
    pathIndex = len(expandedList) - 1
    while pathIndex >= 0:
        if isListEmpty(pathList) or distanceBetweenNodes(pathList[0], expandedList[pathIndex]) == 1:
            pathList.insert(0,expandedList[pathIndex])
        pathIndex -= 1

def distanceBetweenNodes(element, comparedIndex):
    return (abs(element.y - comparedIndex.y) + abs(element.x - comparedIndex.x))


def inBoundaries(element):
    if (0 <= element.y < boundary) and (0 <= element.x < boundary):
        return True
    return False

def invalidInitials(index):
    if (0 > index[0] or
       index[0] >= boundary or
       0 > index[1] or
       index[1] >= boundary
       ):
       return True

    return False

def inExpandedList(element, list):
    for node in list:
        if ([element.y, element.x] == [node.y, node.x]):
            return True

    return False

def isListEmpty(list):
    if len(list) == 0:
        return True
    return False


def mapCoordinateValue(element):
    return map[element.y][element.x]

def printIndex(element):
    print('[', element.y, ', ', element.x, ']')

def removeInvalidMoves(element):
    if (inBoundaries(element) and
        abs(mapCoordinateValue(presentIndex) - mapCoordinateValue(element)) <= 3 and
        not inExpandedList(element, expandedStack)
        ):
        return True
    else:
        return False

def printOutput(dataCollection):
        print ("Number of expanded nodes for BFS:", dataCollection[0])
        print ("Path Cost of BFS:", dataCollection[1])
        print ("Number of nodes in path: ", len(dataCollection[2]))
        print ("Path of BFS")
        for element in dataCollection[2]:
            printIndex(element)

        print ("")
        print ("Number of expanded nodes for A* search:", dataCollection[3])
        print ("Path Cost of A* search:", dataCollection[4])
        print ("Number of nodes in path: ", len(dataCollection[5]))
        print ("Path of A* search")
        for element in dataCollection[5]:
            printIndex(element)

###----start of main function----###

# initialize path values
txtValues = initializeTxtData()
boundary = txtValues["boundary"]
startIndex = txtValues["start"]
goalIndex = txtValues["goal"]
map = txtValues["map"]
searchOutput = []
noSolution = False
searchCounter = 0

if invalidInitials(startIndex) or invalidInitials(goalIndex):
    noSolution = True

while searchCounter < 2 and noSolution == False:
    openQueue = []
    expandedStack = []
    path = []
    presentIndex = Index(startIndex, goalIndex, None)
    openQueue.append(presentIndex)

    # exit conditions
    atGoal = False

    while (atGoal == False and noSolution == False):
        if presentIndex.distance == 0:
            atGoal = True
            expandedStack.append(presentIndex)
        else:
            movablePlaces = [
                Index([presentIndex.y - 1, presentIndex.x], goalIndex, presentIndex), #down
                Index([presentIndex.y + 1, presentIndex.x], goalIndex, presentIndex),  #up
                Index([presentIndex.y, presentIndex.x + 1], goalIndex, presentIndex), #right
                Index([presentIndex.y, presentIndex.x - 1], goalIndex, presentIndex)] #left

            filteredMoves = filter(removeInvalidMoves, movablePlaces)
            for element in filteredMoves:
                if searchCounter == 0:
                    bestFirstInsert(element, openQueue)
                else:
                    aStarSortedInsert(element, openQueue)

            openQueue.remove(presentIndex)
            expandedStack.append(presentIndex)
            if isListEmpty(openQueue):
                noSolution = True
            else:
                presentIndex = openQueue[0]

    if noSolution == False:
        createPath(path, expandedStack)
        searchOutput.append(len(expandedStack))
        searchOutput.append(expandedStack[-1].pathCost)
        searchOutput.append(path)
        atGoal = False

    searchCounter += 1

if noSolution == True:
    print ("No Solution")
else:
    printOutput(searchOutput)


# map counts as global variable
# map = [[1, 1, 1, 2, 1, 1, 1, 1, 1, 1], #0
#        [1, 2, 2, 2, 1, 1, 1, 1, 1, 1], #1
#        [1, 2, 3, 2, 1, 3, 3, 1, 1, 1], #2
#        [4, 2, 2, 2, 2, 1, 1, 1, 1, 6], #3
#        [1, 2, 1, 1, 1, 1, 1, 1, 6, 1], #4
#        [1, 1, 1, 1, 1, 6, 1, 6, 1, 1], #5
#        [1, 1, 3, 1, 1, 1, 6, 1, 1, 1], #6
#        [1, 3, 1, 1, 6, 1, 1, 1, 2, 1], #7
#        [1, 1, 1, 1, 1, 1, 6, 1, 2, 1], #8
#        [1, 1, 1, 1, 1, 6, 1, 1, 1, 1]] #9
#         0  1  2  3  4  5  6  7  8  9
