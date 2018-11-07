# A\* Search w/ GUI

#### Summary:

This projects implements A\* search to determine the optimal path from a starting index to a goal index. The application is written in Python3 and uses the library "Tkinter" to create the program's GUI.

#### Heuristic Value

The heuristic value chosen was based on the distance between the start index and the goal index. This was calculated by finding the sum of the absolute difference between each coordinates' respective x and y values.

- e.g. start index = [0, 0] and goal index = [8,7]. Absolute(startIndex.x - goalIndex.x) + Absolute(startIndex.y - goalIndex.y)

#### A\* Search

A* search uses two values to determine the best path: the step cost to the adjacent index, and the heuristic value mentioned above. A* search decides to add an index into it's expanded queue if the index **does not already exist in that queue** and **is currently the lowest cost index in open/fringe queue**. From there, the algorithm will expand the index that is currently the lowest cost node in it's expanded queue until the goal index is found.

```
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
```

#### Tkinter

This library is used to create a GUI for A\* search. A grid system is created based on the map values given in the initial text file. While the GUI is running, no other code can be run unless it exists in another thread. The `aStarSearch()` function runs concurrently on another thread and updates the grid backgrounds to show the functions progress.

#### Overall

The program implements a multithreaded solution to run the GUI concurrently with A* search's expanded queue to give a visual representation of A* search.
