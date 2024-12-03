# day 2 advent of code 2024
def P1(f):
    safes = []
    for x in f:
        report = [int(v) for v in x.split()]
        safes.append(IsSafe(report))
    return sum(safes)

def P2(f):
    safes = 0
    for x in f:
        report = [int(v) for v in x.split()]
        safe = IsSafe(report)
        if safe == 1:
            safes += 1
            continue
        # Try removing one element at a time and check if it's safe
        for i in range(len(report)):
            report2 = report.copy()
            report2.pop(i)
            if IsSafe(report2):
                safes += 1
                break
    return safes

# Return 0 if not safe or 1 if safe, so I can sum the results
def IsSafe(report):
    for i in range(len(report)-1):
        diff = report[i+1] - report[i]
        if abs(diff) > 3 or abs(diff) == 0:
            return 0  # not safe
        if i == 0:
            ascending = diff > 0
            continue
        if diff < 0 and ascending:
            return 0
        if diff > 0 and not ascending:
            return 0
    return 1

f = open("resources\day02.txt", "r")
print(f"Day 2/1: {P1(f)}")
f.close()
f = open("resources\day02.txt", "r")
print(f"Day 2/2: {P2(f)}")
f.close()
