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

def inExpandedList(element, list):
    for node in list:
        if ([element.y, element.x] == [node.y, node.x]):
            return True

    return False
