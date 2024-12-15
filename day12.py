# day 12 advent of code 2024
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __iter__(self):
        yield self.x
        yield self.y

    def __repr__(self):
        return f"({self.x},{self.y})"

    def __hash__(self):
        return hash((self.x, self.y))


# Returns true if point is in map
def IsInMap(map, point):
    return point.y >= 0 and point.y < len(map) and point.x >= 0 and point.x < len(map[point.y])

# Returns the valid next steps for a given point at a given level


def NextPoints(map, point):
    return [MoveUp(point), MoveDown(point), MoveLeft(point), MoveRight(point)]


def MoveUp(point):
    return Point(point.x, point.y - 1)


def MoveDown(point):
    return Point(point.x, point.y + 1)


def MoveLeft(point):
    return Point(point.x - 1, point.y)


def MoveRight(point):
    return Point(point.x + 1, point.y)


def ReadAllMap(f):
    map = []
    for line in f:
        map.append(list(line.strip()))
    return map


def FirstPointToVisit(map, visited):
    for y in range(len(map)):
        for x in range(len(map[y])):
            if Point(x, y) not in visited:
                return Point(x, y)
    return None

def GetRegion(map, point):
    visited = set(point)
    region = {"plant": map[point.y][point.x], "perimeter": 0,
                               "area": 0, "sides":0, "points": set([point])}
    borders = NextPoints(map, point)
    while len(borders) > 0:
        nextPoint = borders.pop()
        if not(IsInMap(map, nextPoint)):
            region["perimeter"] += 1            
        elif map[nextPoint.y][nextPoint.x] == map[point.y][point.x] and nextPoint not in region["points"]:
            borders += NextPoints(map, nextPoint)
            region["points"].add(nextPoint)
        elif map[nextPoint.y][nextPoint.x] != map[point.y][point.x]:
            region["perimeter"] += 1
        visited.add(nextPoint)
    region["area"] = len(region["points"])
    region["sides"] = len(set([p.x for p in region["points"]])) + len(set([p.y for p in region["points"]]))
    return region

def GetAllRegions(map):
    regions = []
    visited = set()
    p = FirstPointToVisit(map, visited)
    i = 0
    while(p != None):
        region = GetRegion(map, p)
        #RegionPrint(map, region, i)
        regions.append(region)
        visited = visited.union(region["points"])
        p = FirstPointToVisit(map, visited)
        i += 1
    return regions

def RegionPrint(map, region, index):
    p = region["plant"]
    f = open(f"resources\day12_test.{p}{index}.txt", "w")
    f.write(f"Plant: {region['plant']}, Area: {region['area']}, Perimeter: {region['perimeter']}\n")
    for y in range(len(map)):
        for x in range(len(map[y])):
            if Point(x, y) in region["points"]:
                f.write(p)
            else:
                f.write(".")
        f.write("\n")


def P1(map):
    regions = GetAllRegions(map)
    return sum([item["area"]*item["perimeter"] for item in regions])

def P2(map):
    regions = GetAllRegions(map)
    return sum([item["area"]*item["sides"] for item in regions])


f = open("resources\day12_test.txt", "r")
map = ReadAllMap(f)
f.close()
print(f"Day 12/1: {P1(map)}")
print(f"Day 12/2: {P2(map)}")
