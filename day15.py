# day 15 advent of code 2024
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

def FindAllPoints(map, symbol):
    points = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == symbol:
                points.append(Point(x, y))
    return points

def FindPoint(map, symbol):
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == symbol:
                return Point(x, y)

def P1(map, moves):
    p = FindPoint(map, '@')
    for move in moves:
        if move == '^':
            nextPoint = Point(p.x, p.y - 1)
            if map[nextPoint.y][nextPoint.x] == '#':
                continue
            if map[nextPoint.y][nextPoint.x] == '.':
                map[p.y][p.x] = '.'
                map[nextPoint.y][nextPoint.x] = '@'
                p = nextPoint
                continue
            if map[nextPoint.y][nextPoint.x] == 'O':
                space = False
                pushedPoint = nextPoint
                while map[pushedPoint.y][pushedPoint.x] != '#':
                    pushedPoint = Point(pushedPoint.x, pushedPoint.y - 1)
                    if map[pushedPoint.y][pushedPoint.x] == '.':
                        space = True
                        break
                if space:
                    map[p.y][p.x] = '.'
                    map[nextPoint.y][nextPoint.x] = '@'
                    map[pushedPoint.y][pushedPoint.x] = 'O'
                    p = nextPoint
                    continue
        elif move == 'v':
            nextPoint = Point(p.x, p.y + 1)
            if map[nextPoint.y][nextPoint.x] == '#':
                continue
            if map[nextPoint.y][nextPoint.x] == '.':
                map[p.y][p.x] = '.'
                map[nextPoint.y][nextPoint.x] = '@'
                p = nextPoint
                continue  
            if map[nextPoint.y][nextPoint.x] == 'O':
                space = False
                pushedPoint = nextPoint
                while map[pushedPoint.y][pushedPoint.x] != '#':
                    pushedPoint = Point(pushedPoint.x, pushedPoint.y + 1)
                    if map[pushedPoint.y][pushedPoint.x] == '.':
                        space = True
                        break
                if space:
                    map[p.y][p.x] = '.'
                    map[nextPoint.y][nextPoint.x] = '@'
                    map[pushedPoint.y][pushedPoint.x] = 'O'
                    p = nextPoint
                    continue                 
        elif move == '<':
            nextPoint = Point(p.x - 1, p.y)
            if map[nextPoint.y][nextPoint.x] == '#':
                continue  
            if map[nextPoint.y][nextPoint.x] == '.':
                map[p.y][p.x] = '.'
                map[nextPoint.y][nextPoint.x] = '@'
                p = nextPoint
                continue        
            if map[nextPoint.y][nextPoint.x] == 'O':
                space = False
                pushedPoint = nextPoint
                while map[pushedPoint.y][pushedPoint.x] != '#':
                    pushedPoint = Point(pushedPoint.x - 1, pushedPoint.y)
                    if map[pushedPoint.y][pushedPoint.x] == '.':
                        space = True
                        break
                if space:
                    map[p.y][p.x] = '.'
                    map[nextPoint.y][nextPoint.x] = '@'
                    map[pushedPoint.y][pushedPoint.x] = 'O'
                    p = nextPoint
                    continue              
        elif move == '>':
            nextPoint = Point(p.x + 1, p.y)
            if map[nextPoint.y][nextPoint.x] == '#':
                continue
            if map[nextPoint.y][nextPoint.x] == '.':
                map[p.y][p.x] = '.'
                map[nextPoint.y][nextPoint.x] = '@'
                p = nextPoint
                continue    
            if map[nextPoint.y][nextPoint.x] == 'O':
                space = False
                pushedPoint = nextPoint
                while map[pushedPoint.y][pushedPoint.x] != '#':
                    pushedPoint = Point(pushedPoint.x + 1, pushedPoint.y)
                    if map[pushedPoint.y][pushedPoint.x] == '.':
                        space = True
                        break
                if space:
                    map[p.y][p.x] = '.'
                    map[nextPoint.y][nextPoint.x] = '@'
                    map[pushedPoint.y][pushedPoint.x] = 'O'
                    p = nextPoint
                    continue                    
    boxes = FindAllPoints(map, 'O')
    return CalculateBoxes(boxes)

def P2(map, moves):
    return 

def CalculateBoxes(boxes):
    return sum([p.y*100+p.x for p in boxes])

f = open("resources\day15.txt", "r")
map = []
for line in f:
    if line == "\n":
        break
    map.append(list(line.strip()))
moves = ""   
for line in f:
    moves += line.strip()
f.close()
print(f"Day 15/1: {P1(map, moves)}")
print(f"Day 15/2: {P2(map, moves)}")
