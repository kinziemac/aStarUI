from search_inserts import inExpandedList

def mapCoordinateValue(element, map):
    return map[element.y][element.x]

def removeInvalidMoves(map, boundary, presentIndex, stack):
    def removeFilter(element):
        if (inBoundaries(element, boundary) and
            abs(mapCoordinateValue(presentIndex, map) - mapCoordinateValue(element, map)) <= 3 and
            not inExpandedList(element, stack)
            ):
            return True
        else:
            return False

    return removeFilter

def inBoundaries(element, boundary):
    if (0 <= element.y < boundary) and (0 <= element.x < boundary):
        return True
    return False

def invalidInitials(index, boundary):
    if (0 > index[0] or
       index[0] >= boundary or
       0 > index[1] or
       index[1] >= boundary
       ):
       return True

    return False

def isListEmpty(list):
    if len(list) == 0:
        return True
    return False
