# day 6 advent of code 2024
import copy
class Point:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y and self.direction == other.direction
        return False

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.direction

    def __hash__(self):
        return hash((self.x, self.y, self.direction))

    def SamePosition(self, other):
        return self.x == other.x and self.y == other.y

# Navigates from starting point to exit. returns -1 if loop, -2 if fail, otherwise number of visited points
def Quit(currentMap, startingPoint):
    currentPoint = startingPoint
    visited = 0
    visitedSet = set()
    while (IsInMap(currentMap, currentPoint)):
        if currentPoint in visitedSet:
            return -1  # loop
        visitedSet.add(currentPoint)
        if currentMap[currentPoint.y][currentPoint.x] != 'X':
            visited += 1
            currentMap[currentPoint.y][currentPoint.x] = 'X'
        currentPoint = NextPoint(currentMap, currentPoint)
        if currentPoint.direction == 'fail':
            return -2  # fail
    return visited

def FindPoint(map, symbol):
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == symbol:
                return Point(x, y, symbol)

# Returns true if point is in map
def IsInMap(map, point):
    return point.y >= 0 and point.y < len(map) and point.x >= 0 and point.x < len(map[point.y])

# Returns the next valid point in the map
def NextPoint(map, point):
    nextPoint = StraightDirection(point)
    if not IsInMap(map, nextPoint):
        return Point(-1, -1, point.direction)
    while map[nextPoint.y][nextPoint.x] == '#' and IsInMap(map, nextPoint):
        nextPoint = SwitchDirection(
            Point(point.x, point.y, nextPoint.direction))
    return nextPoint

# Returns the next point in case of obstacle, switches direction
def SwitchDirection(point):
    if point.direction == '^':
        return MoveRight(point)
    if point.direction == '>':
        return MoveDown(point)
    if point.direction == 'v':
        return MoveLeft(point)
    if point.direction == '<':
        return MoveUp(point)
    return Point(-1, -1, "fail")

# Returns the next point in case of no obstacle
def StraightDirection(point):
    if point.direction == '^':
        return MoveUp(point)
    if point.direction == '>':
        return MoveRight(point)
    if point.direction == 'v':
        return MoveDown(point)
    if point.direction == '<':
        return MoveLeft(point)
    return Point(-1, -1, "fail")

def MoveUp(point):
    return Point(point.x, point.y - 1, "^")

def MoveDown(point):
    return Point(point.x, point.y + 1, "v")

def MoveLeft(point):
    return Point(point.x - 1, point.y, "<")

def MoveRight(point):
    return Point(point.x + 1, point.y, ">")

def ReadAllMap(f):
    map = []
    for line in f:
        map.append(list(line.strip()))
    return map

def P1(map):
    return Quit(map, FindPoint(map, '^'))

def P2(originalMap, map):
    startingPoint = FindPoint(originalMap, '^')
    loops = 0
    fails = 0
    # for each visited point of Part 1 and adds an obstacle to the original map and tries to navigate from starting point to exit
    for y in range(len(map)):
        for x in range(len(map[y])):
            current = Point(x, y, map[y][x])
            if current.direction == 'X' and not current.SamePosition(startingPoint):
                # deep copy of original map
                currentMap = copy.deepcopy(originalMap)
                currentMap[current.y][current.x] = '#'
                if Quit(currentMap, startingPoint) == -1:
                    loops += 1
                elif Quit(currentMap, startingPoint) == -2:
                    fails += 1  # should not happen
    return loops

f = open("resources\day06.txt", "r")
originalMap = ReadAllMap(f)
map = copy.deepcopy(originalMap)
f.close()
print(f"Day 6/1: {P1(map)}")
print(f"Day 6/2: {P2(originalMap, map)}")