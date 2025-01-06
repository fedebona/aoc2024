# advent of code 2024
from queue import PriorityQueue
day_no = 18


class Point:
    def __init__(self, x, y, directions=None):
        self.x = x
        self.y = y
        self.score = 1
        if directions is not None:
            self.direction = directions
        else:
            self.direction = ">"

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __lt__(self, other):
        if isinstance(other, Point):
            return (self.x*1000+self.y < other.x*1000 - other.y)
        return False

    def __iter__(self):
        yield self.x
        yield self.y

    def __repr__(self):
        return f"({self.x},{self.y}, {self.score}, {self.direction})"

    def __hash__(self):
        return hash((self.x, self.y))


def IsInMap(map, point):
    return point.y >= 0 and point.y < len(map) and point.x >= 0 and point.x < len(map[point.y])

# Returns the valid next steps for a given point with a given direction


def NextPoints(map, point, visited):
    nextPoints = []
    p = MoveUp(point)
    if IsInMap(map, p) and map[p.y][p.x] != '#' and p not in visited:
        nextPoints.append(p)
    p = MoveDown(point)
    if IsInMap(map, p) and map[p.y][p.x] != '#' and p not in visited:
        nextPoints.append(p)
    p = MoveLeft(point)
    if IsInMap(map, p) and map[p.y][p.x] != '#' and p not in visited:
        nextPoints.append(p)
    p = MoveRight(point)
    if IsInMap(map, p) and map[p.y][p.x] != '#' and p not in visited:
        nextPoints.append(p)
    return nextPoints


def MoveUp(point):
    return Point(point.x, point.y - 1)


def MoveDown(point):
    return Point(point.x, point.y + 1)


def MoveLeft(point):
    return Point(point.x - 1, point.y)


def MoveRight(point):
    return Point(point.x + 1, point.y)


def P1(points):
    map = CreateMap(mapSize)
    for i in range(iterations):
        p = points[i]
        map[p.y][p.x] = '#'

    frontier = PriorityQueue()
    start_point = Point(0, 0)
    visited = set()
    visited.add(start_point)
    frontier.put((0, start_point))  # (priority, item)
    came_from = {}
    came_from[start_point] = None
    cost_so_far = {}
    cost_so_far[start_point] = 0

    while not frontier.empty():
        current_priority, current_point = frontier.get()
        if current_point == Point(mapSize-1, mapSize-1):
            break
        for next_point in NextPoints(map, current_point, visited):
            new_cost = cost_so_far[current_point] + next_point.score
            if next_point not in cost_so_far.keys() or new_cost <= cost_so_far[next_point]:
                cost_so_far[next_point] = new_cost
                priority = new_cost
                frontier.put((priority, next_point))
                visited.add(next_point)
                came_from[next_point] = current_point

#    for p in visited:
#        map[p.x][p.y] = 'O'

    return cost_so_far[Point(mapSize-1, mapSize-1)]


def P2(points):

    return


def GetPoints(f):
    points = []
    for line in f:
        points.append(
            Point(int(line.strip().split(',')[0]), int(line.strip().split(',')[1])))
    return points


def CreateMap(mapSize):
    map = []
    for x in range(0, mapSize):
        map.append(['.' for y in range(0, mapSize)])
    return map


isTest = False
if isTest:
    mapSize = 7
    iterations = 12
    suffix = "_test"
else:
    mapSize = 71
    iterations = 1024
    suffix = ""

f = open(f"resources\day{day_no:02}{suffix}.txt", "r")
points = GetPoints(f)

f.close()
print(f"Day {day_no}/1: {P1(points)}")
print(f"Day {day_no}/2: {P2(points)}")
