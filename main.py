import tkinter as tk
import time
import threading
import sys

from index import Index
from search_inserts import aStarSortedInsert, inExpandedList
from print_results import Printer
from parse_data import *
from index_checking import *
from create_path import *


def changeTileColor(row, column, color, sleepTime=1000.0):
    time.sleep(1/sleepTime)
    tk.Label(root, text=str(map[row][column]), background=color, borderwidth=3 ).grid(row=row,column=column)

def closeThread():
    time.sleep(10)
    root.quit()
    sys.exit()

def writePath(expandedList):
    pathList = []
    createPath(pathList, expandedList)
    root.title("Found!")
    time.sleep(2)
    for element in pathList:
        changeTileColor(element.y, element.x, '#FFD700', 250.0)

def aStarSearch():
    noSolution = False

    if invalidInitials(startIndex, boundary) or invalidInitials(goalIndex, boundary):
        noSolution = True

    openQueue = []
    expandedStack = []
    path = []
    presentIndex = Index(startIndex, goalIndex, None, boundary, map)
    openQueue.append(presentIndex)
    time.sleep(3)
    root.title("Searching..")

    # exit conditions
    atGoal = False

    while (atGoal == False and noSolution == False):
        changeTileColor(presentIndex.y, presentIndex.x, 'orange')
        if presentIndex.distance == 0:
            atGoal = True
            changeTileColor(presentIndex.y, presentIndex.x, '#00FA9A')
            expandedStack.append(presentIndex)
            writePath(expandedStack)
            closeThread()
        else:
            movablePlaces = [
                Index(
                    [presentIndex.y - 1, presentIndex.x],
                    goalIndex,
                    presentIndex,
                    boundary,
                    map), #down
                Index(
                    [presentIndex.y + 1, presentIndex.x],
                    goalIndex,
                    presentIndex,
                    boundary,
                    map),  #up
                Index(
                    [presentIndex.y, presentIndex.x + 1],
                    goalIndex,
                    presentIndex,
                    boundary,
                    map), #right
                Index(
                    [presentIndex.y, presentIndex.x - 1],
                    goalIndex,
                    presentIndex,
                    boundary,
                    map) #left
                    ]

            mapRemoval = removeInvalidMoves(map, boundary, presentIndex, expandedStack)
            filteredMoves = filter(mapRemoval, movablePlaces)
            for element in filteredMoves:
                # if searchCounter == 0:
                #     bestFirstInsert(element, openQueue)
                # else:
                aStarSortedInsert(element, openQueue)

            openQueue.remove(presentIndex)
            expandedStack.append(presentIndex)
            if isListEmpty(openQueue):
                noSolution = True
                closeThread()

            else:
                presentIndex = openQueue[0]

        if noSolution == False:
            createPath(path, expandedStack)
            searchOutput.append(len(expandedStack))
            searchOutput.append(expandedStack[-1].pathCost)
            searchOutput.append(path)
            atGoal = False


# Main #


txtValues = initializeTxtData()
boundary = txtValues["boundary"]
startIndex = txtValues["start"]
goalIndex = txtValues["goal"]
map = txtValues["map"]
printer = Printer()
searchOutput = []
searchCounter = 0

root = tk.Tk()
root.title("A* search")
colors = ['#BBFFFF', '#b3e6ff', '#80d4ff', '#33bbff', '#00aaff', '#0077b3']

for i in range(boundary):
    for j in range(boundary):
        tk.Label(root, text=str(map[i][j]), background=colors[(map[i][j] - 1)], borderwidth=3 ).grid(row=i,column=j)

t1 = threading.Thread(target=aStarSearch)
t1.start()
root.mainloop()
