# Pathfinder Algorithm

## Best First Search & A\* Search

### Heuristic Value

The heuristic value chosen was based on distance between the start index and the goal index. This was calculated by finding the sum of the absolute difference between each coordinates' respective x and y values.

- e.g. start index = [0, 0] and goal index = [8,7]. Absolute(startIndex.x - goalIndex.x) + Absolute(startIndex.y - goalIndex.y)

When this values reaches 0, the agent has arrived at the goal index.

### F(n) values

While the Best First Search algorithm and A\* Search algorithm look very similar, the key difference was how nodes were inserted into the search queue (openQueue). Both treat the openQueue as a priority queue.

####Best First Search
Best first search was based around the heuristic value; it is the only value used to perform the search.

- e.g. f(n) = g(n) + h(n)
- where h(n) = heuristic, g(n) = 0

```
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
```

This function inserts the node into the list, the
