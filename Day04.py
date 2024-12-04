# day 4vadvent of code 2024

def P1(map, WordToFind):
    FoundCount = 0
    for x in range(len(map)):
        for y in range(len(map[x])):
            FoundCount += FindWord(map, WordToFind, x, y)
    return FoundCount

# find a word in the map
def FindWord(map, WordToFind, x0, y0):
    FoundCount = 0
    if (map[x0][y0] != WordToFind[0]):
        return 0
    if (len(WordToFind) == 1):
        return 1
    # check all directions for second letter
    for x in range(max(x0-1, 0), min(x0+2, len(map))):
        for y in range(max(y0-1, 0), min(y0+2, len(map[x]))):
            if (x == x0 and y == y0):
                continue
            elif (map[x][y] != WordToFind[1]):
                continue
            else:
                IsMatch = True
                # check in the direction of the second letter for the others
                for i in range(2, len(WordToFind)):
                    if (x0+i*(x-x0) < 0 or x0+i*(x-x0) >= len(map) or y0+i*(y-y0) < 0 or y0+i*(y-y0) >= len(map[x])):
                        IsMatch = False
                        break
                    if (map[x0+i*(x-x0)][y0+i*(y-y0)] != WordToFind[i]):
                        IsMatch = False
                        break
                if (IsMatch):
                    FoundCount += 1
    return FoundCount

def P2(map):
    FoundCount = 0
    for x in range(len(map)):
        for y in range(len(map[x])):
            FoundCount += FindXmas(map, x, y)
    return FoundCount

# find a square representation of XMAS in the map
def FindXmas(map, x0, y0):
    # quits if the map is too small
    if (x0 + 2 >= len(map) or y0 + 2 >= len(map[x0])):
        return 0
    # quits if ath the corners we don't have M or S
    if (not (map[x0][y0] in ["M", "S"])):
        return 0
    if (not (map[x0][y0+2] in ["M", "S"])):
        return 0
    if (not (map[x0+2][y0] in ["M", "S"])):
        return 0
    if (not (map[x0+2][y0+2] in ["M", "S"])):
        return 0    
    # quits if there isn't an A in the middle
    if (map[x0+1][y0+1] != "A"):
        return 0
    # quits if the diagonals aren't opposite (M and S)
    if (map[x0][y0] == map[x0+2][y0+2]):
        return 0
    if (map[x0+2][y0] == map[x0][y0+2]):
        return 0    
    return 1

def readallmap(f):
    map = []
    for line in f:
        map.append(line.strip())
    return map

f = open("resources\day04.txt", "r")
map = readallmap(f)
f.close()

WordToFind = "XMAS"
print(f"Day 4/1: {P1(map, WordToFind)}")
print(f"Day 4/2: {P2(map)}")
