# day 8 advent of code 2024
from itertools import combinations
class Point:
    def __init__(self, x, y, antenna):
        self.x = x
        self.y = y
        self.antenna = antenna

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y and self.antenna == other.antenna
        return False

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.antenna

    def __hash__(self):
        return hash((self.x, self.y, self.antenna))

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, antenna={self.antenna})"

def P1(map):
    nodes = FindNodes(map)
    setAntinodes = set()
    for key in nodes.keys():
        if len(nodes[key]) > 1:
            # calculate antinodes
            setAntinodes = setAntinodes.union(
                CalculateAntinodesP1(map, nodes[key], key))
    return len(setAntinodes)

# Antinodes for part 2 are the sum of calculated antinodes and the sum of antennas
def P2(map):
    nodes = FindNodes(map)
    count = 0
    for key in nodes.keys():
        if len(nodes[key]) > 1:
            # calculate antinodes
            CalculateAntinodesP2(map, nodes[key], key)
            count += CountSymbols(map, key)
    count += CountSymbols(map, '#')
    return count

def ReadAllMap(f):
    map = []
    for line in f:
        map.append(list(line.strip()))
    return map

def FindNodes(map):
    nodes = {}
    for x in range(len(map)):
        for y in range(len(map[x])):
            if (map[x][y] != '.'):
                if not (map[x][y] in nodes):
                    nodes[map[x][y]] = []
                nodes[map[x][y]].append(Point(x, y, map[x][y]))
    return nodes

def CountSymbols(map, symbol):
    count = 0
    for x in range(len(map)):
        for y in range(len(map[x])):
            if (map[x][y] == symbol):
                count += 1
    return count

def IsInMap(map, point):
    return point.y >= 0 and point.y < len(map) and point.x >= 0 and point.x < len(map[point.y])

# calculates antinodes for each couple of nodes of same frequency
def CalculateAntinodesP1(map, nodes, frequency):
    tuples = list(combinations(nodes, 2))
    setAntinodes = set()
    for tuple in tuples:
        deltaX = tuple[0].x - tuple[1].x
        deltaY = tuple[0].y - tuple[1].y
        antinode1 = Point(tuple[0].x + deltaX, tuple[0].y + deltaY, frequency)
        if IsInMap(map, antinode1):
            # add antinode to set, frequency is not important because location must be unique
            setAntinodes.add((antinode1.x, antinode1.y)) 
        antinode2 = Point(tuple[1].x - deltaX, tuple[1].y - deltaY, frequency)
        if IsInMap(map, antinode2):
            setAntinodes.add((antinode2.x, antinode2.y))
    return setAntinodes

# calculates antinodes for part 2 for each couple of nodes of same frequency
# We mark the map with '#' for each antinode
def CalculateAntinodesP2(map, nodes, frequency):
    tuples = list(combinations(nodes, 2))
    for tuple in tuples:
        deltaX = tuple[0].x - tuple[1].x
        deltaY = tuple[0].y - tuple[1].y
        antinode1 = Point(tuple[0].x + deltaX, tuple[0].y + deltaY, frequency)
        while IsInMap(map, antinode1):
            if map[antinode1.x][antinode1.y] == '.':
                map[antinode1.x][antinode1.y] = '#'
            antinode1 = Point(antinode1.x + deltaX,
                              antinode1.y + deltaY, frequency)
        antinode2 = Point(tuple[1].x - deltaX, tuple[1].y - deltaY, frequency)
        while IsInMap(map, antinode2):
            if map[antinode2.x][antinode2.y] == '.':
                map[antinode2.x][antinode2.y] = '#'
            antinode2 = Point(antinode2.x - deltaX,
                              antinode2.y - deltaY, frequency)
    return

f = open("resources\day08.txt", "r")
map = ReadAllMap(f)
f.close()
print(f"Day 8/1: {P1(map)}")
print(f"Day 8/2: {P2(map)}")
f.close()