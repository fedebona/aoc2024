# day 24 advent of code 2024
import re


class Operation:
    def __init__(self, op, x, y, z):
        self.op = op
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.op} {self.x} {self.y} {self.z}"

    def __repr__(self):
        return self.__str__()

    def Value(self, wires):
        if self.op == "AND":
            return wires[self.x] & wires[self.y]
        elif self.op == "OR":
            return wires[self.x] | wires[self.y]
        elif self.op == "XOR":
            return wires[self.x] ^ wires[self.y]
        else:
            return 1/0

    def IsValid(self, wires):
        if self.x not in wires.keys() or self.y not in wires.keys():
            return False
        return True


def CalculateValue(wires, ops):
    validWires = wires.copy()
    for op in ops:
        if op.IsValid(validWires):
            validWires[op.z] = op.Value(validWires)
    return validWires


def CountZWires(ops):
    return max([int(op.z.strip("z")) for op in ops if op.z.startswith("z")]) + 1


def AllZWires(wires, zeds):
    currentZeds = 0
    for wire in wires.keys():
        if wire.startswith("z"):
            currentZeds += 1
    return currentZeds == zeds


def P1(wires, ops):
    zeds = CountZWires(ops)
    while not (AllZWires(wires, zeds)):
        wires = CalculateValue(wires, ops)
    # orderedKeys = sorted(wires.keys(), reverse=True)
    val = ""
    for i in range(zeds - 1, -1, -1):
        currKey = f"z{i:0>2}"
        val += f"{wires[currKey]}"
    return int(val, 2)


def P2(f):

    return


f = open("resources\day24.txt", "r")
wires = {}
ops = []
for line in f:
    if line == "\n":
        break
    wires[line.split(":")[0]] = int(line.split(" ")[1].strip())

ops = [Operation(m[1], m[0], m[2], m[3]) for m in re.findall(
    r"(\w+)\s(XOR|OR|AND)\s(\w+)\s->\s(\w+)", f.read())]

print(f"Day 24/1: {P1(wires, ops)}")
print(f"Day 24/2: {P2(f)}")
f.close()
