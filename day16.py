# day 16 advent of code 2024
from queue import PriorityQueue

class Point:
    def __init__(self, x, y, score, direction):
        self.x = x
        self.y = y
        self.score = score
        self.direction = direction

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
    
    def __lt__(self, other):
        if isinstance(other, Point):
            return (self.x*1000+self.y < other.x*1000-  other.y)
        return False

    def __iter__(self):
        yield self.x
        yield self.y

    def __repr__(self):
        return f"({self.x},{self.y}, {self.score}, {self.direction})"

    def __hash__(self):
        return hash((self.x, self.y))


def FindPoint(map, symbol):
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == symbol:
                return Point(x, y, 0, ">")

# Returns true if point is in map


def IsInMap(map, point):
    return point.y >= 0 and point.y < len(map) and point.x >= 0 and point.x < len(map[point.y])

# Returns the valid next steps for a given point with a given direction


def NextPoints(map, point, currentDirection):
    nextPoints = []
    if currentDirection == ">":
        p = MoveUp(point, 1001)
        if map[p.y][p.x] != '#':
            nextPoints.append(p)
        p = MoveDown(point, 1001)
        if map[p.y][p.x] != '#':
            nextPoints.append(p)
        p = MoveRight(point, 1)
        if map[p.y][p.x] != '#':
            nextPoints.append(p)
    elif currentDirection == "<":
        p = MoveUp(point, 1001)
        if map[p.y][p.x] != '#':
            nextPoints.append(p)
        p = MoveDown(point, 1001)
        if map[p.y][p.x] != '#':
            nextPoints.append(p)
        p = MoveLeft(point, 1)
        if map[p.y][p.x] != '#':
            nextPoints.append(p)
    elif currentDirection == "^":
        p = MoveUp(point, 1)
        if map[p.y][p.x] != '#':
            nextPoints.append(p)
        p = MoveLeft(point, 1001)
        if map[p.y][p.x] != '#':
            nextPoints.append(p)
        p = MoveRight(point, 1001)
        if map[p.y][p.x] != '#':
            nextPoints.append(p)
    elif currentDirection == "v":
        p = MoveDown(point, 1)
        if map[p.y][p.x] != '#':
            nextPoints.append(p)
        p = MoveLeft(point, 1001)
        if map[p.y][p.x] != '#':
            nextPoints.append(p)
        p = MoveRight(point, 1001)
        if map[p.y][p.x] != '#':
            nextPoints.append(p)
    return nextPoints


def MoveUp(point, score):
    return Point(point.x, point.y - 1, score, "^")


def MoveDown(point, score):
    return Point(point.x, point.y + 1, score, "v")


def MoveLeft(point, score):
    return Point(point.x - 1, point.y, score, "<")


def MoveRight(point, score):
    return Point(point.x + 1, point.y, score, ">")


def ReadAllMap(f):
    map = []
    for line in f:
        map.append([x for x in list(line.strip())])
    return map


def CalculateScore(path):
    score = 0
    for p in path:
        score += p.score
    return score


def P1(map):
    frontier = PriorityQueue()
    start_point = FindPoint(map, "S")
    frontier.put((0, start_point))  # (priority, item)
    visited = set()
    came_from = {}
    came_from[start_point] = None
    cost_so_far = {}
    cost_so_far[start_point] = 0
   
    while not frontier.empty():
        current_priority, current_point = frontier.get()
        if map[current_point.y][current_point.x] == "E":
            break
        for next_point in NextPoints(map, current_point, current_point.direction):
            new_cost = cost_so_far[current_point] + next_point.score
            if next_point not in cost_so_far.keys() or new_cost <= cost_so_far[next_point]:
                cost_so_far[next_point] = new_cost
                priority = new_cost
                frontier.put((priority, next_point))
                came_from[next_point] = current_point
    count=0
    return current_priority


def P2(map):
    return


f = open("resources\day16.txt", "r")
map = ReadAllMap(f)
f.close()
print(f"Day 16/1: {P1(map)}")
print(f"Day 16/2: {P2(map)}")
