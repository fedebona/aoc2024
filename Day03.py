# day 3 advent of code 2024
import re

# Using regex to find all matches with the pattern "mul(x,y)" and sum the results
# findall returns directly a list of tuples of captured groups
def P1(f):
    text = f.read()
    results = [int(m[0])*int(m[1])
               for m in re.findall(r"mul\((\d+),(\d+)\)", text)]
    return sum(results)

# Using regex to find all matches with the pattern "mul(x,y)" and sum the results
# but also checking if the "do()" and "don't()" functions as validators or invalidators
# finditer is used to iterate over the matches returning a match object
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
