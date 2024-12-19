# day 17 advent of code 2024
import copy
def FetchAndRun(registers, instructions, current, output):
    instruction = instructions[current]
    incr = 2
    if instruction == 0:
        # adv
        result = registers["A"]//pow(2,
                                     GetCombo(instructions[current+1], registers))
        registers["A"] = result
    elif instruction == 1:
        # bxl
        result = registers["B"] ^ instructions[current+1]
        registers["B"] = result
    elif instruction == 2:
        # bst
        result = GetCombo(instructions[current+1], registers) % 8
        registers["B"] = result
    elif instruction == 3:
        # jnz
        if registers["A"] != 0:
            return instructions[current+1]
    elif instruction == 4:
        # bxc
        result = registers["B"] ^ registers["C"]
        registers["B"] = result
    elif instruction == 5:
        # out
        result = GetCombo(instructions[current+1], registers) % 8
        output.append(result)
    elif instruction == 6:
        # bdv
        result = registers["A"]//pow(2,
                                     GetCombo(instructions[current+1], registers))
        registers["B"] = result
    elif instruction == 7:
        # bdc
        # bdv
        result = registers["A"]//pow(2,
                                     GetCombo(instructions[current+1], registers))
        registers["C"] = result
    return current + incr


def GetCombo(value, registers):
    if value <= 3:
        return value
    if value == 4:
        return registers["A"]
    if value == 5:
        return registers["B"]
    if value == 6:
        return registers["C"]
    if value == 7:
        Exception("Invalid value")


def P1(registers, instructions):
    output = []
    current = 0
    while (True):
        current = FetchAndRun(registers, instructions, current, output)
        if current >= len(instructions):
            break
    return  ",".join(map(str, output))


def P2(originalRegisters, instructions):
    i = 0
    while (True):
        registers = copy.deepcopy(originalRegisters)
        registers["A"] = i
        output = P1(registers, instructions)
        if output == ",".join(map(str, instructions)):
            return i
        i += 1
    return 0


f = open("resources\day17.txt", "r")
registers = {"A": 0, "B": 0, "C": 0}
line = f.readline()
registers["A"] = int(line.split(":")[1].strip())
line = f.readline()
registers["B"] = int(line.split(":")[1].strip())
line = f.readline()
registers["C"] = int(line.split(":")[1].strip())
line = f.readline()
line = f.readline()
instructions = [int(x) for x in line.split(":")[1].split(",")]
originalRegisters = copy.deepcopy(registers)
print(f"Day 17/1: {P1(registers, instructions)}")
print(f"Day 17/2: {P2(originalRegisters, instructions)}")


f.close()
