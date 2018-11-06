

class Index:
    def __init__(self, location, goal, previousIndex, boundary, map):
        self.y = location[0]
        self.x = location[1]
        self.distance = abs(goal[0] - location[0]) + abs(goal[1] - location[1])
        self.pathCost = 0

        if (previousIndex is not None and
            (0 <= self.y < boundary) and
            (0 <= self.x < boundary)
            ):
            self.pathCost = abs(map[self.y][self.x] - self.mapValue(previousIndex, map)) + 1 + previousIndex.pathCost
        self.aStarValue = self.distance + self.pathCost

    def mapValue(self, element, map):
        return map[element.y][element.x]
