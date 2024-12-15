# day 13 advent of code 2024

def P1(rules):
    tokens = []
    for rule in rules:
        tokens.append(CalculateTokens(rule, 0))
    return sum(tokens)


def P2(rules):
    tokens = []
    for rule in rules:
        tokens.append(CalculateTokens(rule, 10000000000000))
    return sum(tokens)


def CalculateTokens(rule, correction):
    # prize x* by - prize y *bx   / ax*by- ay*bx  80 A
    #   prizex * ay -prizey *ax  / ay * bx - ax * by    40 B
    tokens = 0
    if IsDivisionInteger((rule["Prize"]["X"]+correction) * rule["B"]["Y"] - (rule["Prize"]["Y"]+correction) * rule["B"]["X"], rule["A"]["X"] * rule["B"]["Y"] - rule["A"]["Y"] * rule["B"]["X"]) and IsDivisionInteger((rule["Prize"]["X"]+correction) * rule["A"]["Y"] - (rule["Prize"]["Y"]+correction) * rule["A"]["X"], rule["B"]["X"] * rule["A"]["Y"] - rule["A"]["X"] * rule["B"]["Y"]):
        movesA = ((rule["Prize"]["X"]+correction) * rule["B"]["Y"] - (rule["Prize"]["Y"]+correction)
                  * rule["B"]["X"]) / (rule["A"]["X"] * rule["B"]["Y"] - rule["A"]["Y"] * rule["B"]["X"])
        movesB = ((rule["Prize"]["X"]+correction) * rule["A"]["Y"] - (rule["Prize"]["Y"]+correction)
                  * rule["A"]["X"]) / (rule["B"]["X"] * rule["A"]["Y"] - rule["A"]["X"] * rule["B"]["Y"])
        tokens = movesA * 3 + movesB
    return int(tokens)


def IsDivisionInteger(a, b):
    if b == 0:
        return False
    return a % b == 0


def ReadRules(f):
    rules = []
    rule = {"A": {"X": 0, "Y": 0}, "B": {
        "X": 0, "Y": 0}, "Prize": {"X": 0, "Y": 0}}
    for line in f:
        line = line.strip()
        if line == "":
            rules.append(rule)
            rule = {"A": {"X": 0, "Y": 0}, "B": {
                "X": 0, "Y": 0}, "Prize": {"X": 0, "Y": 0}}
            continue
        parts = line.split(":")
        if parts[0] == "Button A":
            rule["A"]["X"] = int((parts[1].split(",")[0]).split("+")[1])
            rule["A"]["Y"] = int((parts[1].split(",")[1]).split("+")[1])
        elif parts[0] == "Button B":
            rule["B"]["X"] = int((parts[1].split(",")[0]).split("+")[1])
            rule["B"]["Y"] = int((parts[1].split(",")[1]).split("+")[1])
        elif parts[0] == "Prize":
            rule["Prize"]["X"] = int((parts[1].split(",")[0]).split("=")[1])
            rule["Prize"]["Y"] = int((parts[1].split(",")[1]).split("=")[1])
    rules.append(rule)
    return rules


f = open("resources\day13.txt", "r")
rules = ReadRules(f)
f.close()
print(f"Day 13/1: {P1(rules)}")
print(f"Day 13/2: {P2(rules)}")
