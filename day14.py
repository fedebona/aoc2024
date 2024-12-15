# day 14 advent of code 2024
import re


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


def P1(map, instructions, width, height):
    iterations = 100
    Iterate(map, instructions, iterations)
    middleX = width//2
    middleY = height//2
    return RobotsInRange(map, 0, middleX, 0, middleY) * RobotsInRange(map, middleX+1, width, 0, middleY) * RobotsInRange(map, 0, middleX, middleY+1, height) * RobotsInRange(map, middleX+1, width, middleY+1, height)


def P2(map, instructions, width, height):
    iterations = 100
    for i in range(iterations):
        map = CreateEmptyMap(width, height)
        Iterate(map, instructions, i)
        PrintMap(i, map)
    return


def Iterate(map, instructions, iterations):
    for i in range(len(instructions)):
        finalXposition = (
            instructions[i]["position"].x + iterations*instructions[i]["velocity"].x) % len(map)
        finalYposition = (
            instructions[i]["position"].y + iterations*instructions[i]["velocity"].y) % len(map[0])
        map[finalXposition][finalYposition].append(i)

def PrintMap(iteration, map):
    f = open(f"resources\day14\{iteration}.txt", "w")
    for i in range(len(map)):
        for j in range(len(map[0])):
            if len(map[i][j]) > 0:
                f.write("#")
            else:
                f.write(".")
        f.write("\n")

def RobotsInRange(map, x1, x2, y1, y2):
    total = 0
    for x in range(x1, x2):
        for y in range(y1, y2):
            total += len(map[x][y])
    return total


def GetInstructions(f):
    text = f.read()
    instructions = []
    for m in re.finditer(r"p=([-]?\d+),([-]?\d+)\sv=([-]?\d+),([-]?\d+)", text):
        instruction = {"position": Point(int(m.group(1)), int(
            m.group(2))), "velocity": Point(int(m.group(3)), int(m.group(4)))}
        instructions.append(instruction)
    return instructions


def CreateEmptyMap(width, height):
    map = []
    for i in range(0, width):
        row = []
        for j in range(0, height):
            row.append([])
        map.append(row)
    return map


f = open("resources\day14.txt", "r")
width = 101
height = 103
instructions = GetInstructions(f)
map = CreateEmptyMap(width, height)
f.close()
print(f"Day 14/1: {P1(map, instructions, width, height)}")
print(f"Day 14/2: {P2(map, instructions, width, height)}")
