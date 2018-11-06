import tkinter as tk
import time
import threading

from index import Index
from search_inserts import aStarSortedInsert, bestFirstInsert, inExpandedList
from print_results import Printer
from parse_data import *
from index_checking import *
from create_path import *

# class Board():
#     def __init__(self):
#         self.thread = threading.Thread(target = self.makeMap)
#         self.thread.start()
#
#     def makeMap(self):
#
#
#     def callback(self):
#         self.root.quit()
#
#     def updateSquare(self):
#         tk.Label(self.root, text=str(map[i][j]), background=colors[(map[i][j] - 1)], borderwidth=15 ).grid(row=i,column=j)
#         self.makeMap()
#
#
#






txtValues = initializeTxtData()
boundary = txtValues["boundary"]
startIndex = txtValues["start"]
goalIndex = txtValues["goal"]
map = txtValues["map"]
printer = Printer()
searchOutput = []
noSolution = False
searchCounter = 0

# board = Board()
# time.sleep(2)
# updateSquare(4,4)
root = tk.Tk()
colors = ['#e6f7ff', '#b3e6ff', '#80d4ff', '#33bbff', '#00aaff', '#0077b3']
# root.protocol("WM_DELETE_WINDOW", callback)

for i in range(boundary):
    for j in range(boundary):
        tk.Label(root, text=str(map[i][j]), background=colors[(map[i][j] - 1)], borderwidth=15 ).grid(row=i,column=j)
root.mainloop()

if invalidInitials(startIndex, boundary) or invalidInitials(goalIndex, boundary):
    noSolution = True

while searchCounter < 2 and noSolution == False:
    openQueue = []
    expandedStack = []
    path = []
    presentIndex = Index(startIndex, goalIndex, None, boundary, map)
    openQueue.append(presentIndex)

    # exit conditions
    atGoal = False

    while (atGoal == False and noSolution == False):
        if presentIndex.distance == 0:
            atGoal = True
            expandedStack.append(presentIndex)
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

print('finished')


# if noSolution == True:
#     print ("No Solution")
# else:
#     printer.printOutput(searchOutput)


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
