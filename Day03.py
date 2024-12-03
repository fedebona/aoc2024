# day 3 advent of code 2024
import re


def P1(f):
    text = f.read()
    results = [int(m[0])*int(m[1])
               for m in re.findall(r"mul\((\d+),(\d+)\)", text)]
    return sum(results)


def P2(f):
    enabled = True
    results = []
    text = f.read()
    for m in re.finditer(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)", text):
        if m.group(0) == "don't()":
           enabled = False
        elif m.group(0) == "do()":
            enabled = True
        elif enabled:
            results.append(int(m.group(1))*int(m.group(2)))
    return sum(results)


f = open("resources\day03.txt", "r")
print(f"Day 3/1: {P1(f)}")
f.close()
f = open("resources\day03.txt", "r")
print(f"Day 3/2: {P2(f)}")
f.close()
