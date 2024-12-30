# day 23 advent of code 2024
from itertools import combinations


def P1(links):
    validSets = FindSets(links)
    return len(validSets)


def P2(links):
    return "".join(FindLargestSets(links))


def FindSets(links):
    sets = []
    indices = []
    goodSets = set()
    for j in range(len(links)):
        for i in range(len(links)):
            if links[i].intersection(links[j]) != set():
                sets.append(links[j].union(links[i]))
                indices.append((i, j))
    for i in range(len(sets)):
        currentSet = sets[i]
        for j in range(len(links)):
            link = links[j]
            if currentSet.intersection(link) != set():
                if len(currentSet) == 3 and len(currentSet.union(link)) == 3 and j not in indices[i]:
                    if StartsWithLetter(currentSet, "t"):
                        goodSets.add(frozenset(currentSet))
    return goodSets

def FindLargestSets(links):
    sets = []
    indices = []
    goodSets = set()
    for j in range(len(links)):
        for i in range(len(links)):
            if links[i].intersection(links[j]) != set():
                sets.append(links[j].union(links[i]))
                indices.append((i, j))
    for i in range(len(sets)):
        currentSet = sets[i]
        for j in range(len(links)):
            link = links[j]
            if currentSet.intersection(link) != set() and len(currentSet) == len(currentSet.union(link)) and j not in indices[i]:
                goodSets.add(frozenset(currentSet))
    return goodSets

                    


def StartsWithLetter(currentSet, letter):
    for link in currentSet:
        if link.startswith(letter):
            return True
    return False


f = open("resources\day23_test.txt", "r")
links = [set(x.strip().split("-")) for x in f]
print(f"Day 23/1: {P1(links)}")
print(f"Day 23/2: {P2(links)}")
f.close()
