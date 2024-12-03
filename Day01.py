# Day 1 advent of code 2024
def P1(f):
    list1 = []
    list2 = []
    distance = 0
    for x in f:
        row = x.split()
        list1.append(int(row[0]))
        list2.append(int(row[1]))
    list1.sort()
    list2.sort()
    for i in range(len(list1)):
        distance += abs(list1[i] - list2[i])
    return distance

def P2(f):
    list1 = []
    list2 = []
    similarity = 0
    for x in f:
        row = x.split()
        list1.append(int(row[0]))
        list2.append(int(row[1]))
    for x in list1:
        similarity += (x * list2.count(x))
    return similarity

f = open("resources\day01.txt", "r")
print(f"Day 1/1: {P1(f)}")
f.close()
f = open("resources\day01.txt", "r")
print(f"Day 1/2: {P2(f)}")
f.close()
