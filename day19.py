# day 4vadvent of code 2024

def P1(towels, towelsDict, patterns):

    goodPatterns = []
    for pattern in patterns:
        sequence = FindFittingTowel2(towelsDict, pattern)
        if sequence != None:
            goodPatterns.append(pattern)
    return len(goodPatterns)

def P2(towels, patterns):
 
    return 

def FindFittingTowel2(towelsDict, remainingPattern):
    sequence = []
    if(len(remainingPattern) == 0):
        return sequence

    if remainingPattern[0] in towelsDict.keys():
        for towel in towelsDict[remainingPattern[0]]:
            if len(towel) > len(remainingPattern):
                continue
            if remainingPattern.startswith(towel):
                nextSequence = FindFittingTowel2(towelsDict, remainingPattern[len(towel):])
                if nextSequence != None:
                    return [towel] + nextSequence
    return None


def FindFittingTowel(towels, remainingPattern):
    sequence = []
    if(len(remainingPattern) == 0):
        return sequence

    if remainingPattern in towels:
        return [remainingPattern]    
    
    for towel in towels:
        if len(towel) > len(remainingPattern):
            continue
        if remainingPattern.startswith(towel):
            nextSequence = FindFittingTowel(towels, remainingPattern[len(towel):])
            if nextSequence != None:
                return [towel] + nextSequence
    return None

f = open("resources\day19.txt", "r")
line = f.readline()
towels = sorted([x.strip() for x in line.split(",")], key=len, reverse=True)
towelsDict = {}
for towel in towels:
    if towel[0] not in towelsDict.keys():
        towelsDict[towel[0]] = [towel]
    else :
        towelsDict[towel[0]].append(towel)
line = f.readline()
patterns = [line.strip() for line in f]
print(f"Day 19/1: {P1(towels, towelsDict, patterns)}")
print(f"Day 19/2: {P2(towels, patterns)}")

