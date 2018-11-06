from index_checking import isListEmpty

def createPath(pathList, expandedList):
    pathIndex = len(expandedList) - 1
    while pathIndex >= 0:
        if isListEmpty(pathList) or distanceBetweenNodes(pathList[0], expandedList[pathIndex]) == 1:
            pathList.insert(0,expandedList[pathIndex])
        pathIndex -= 1

def distanceBetweenNodes(element, comparedIndex):
    return (abs(element.y - comparedIndex.y) + abs(element.x - comparedIndex.x))
