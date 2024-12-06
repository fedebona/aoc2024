# day 5 avdvent of code 2024
def P1(rules, updates):
    return sum([ProcessUpdateP1(rules, update) for update in updates])

def P2(rules, updates):
    return sum([ProcessUpdateP2(rules, update) for update in updates])

# Take only middle value of valid updates
def ProcessUpdateP1(rules, update):
    if (IndexOfWrongUpdate(rules, update) == []):
        return update[int(len(update)/2)]
    return 0

# Take only the wrong updates and swaps failed rules until they are correct, and then take the middle value
def ProcessUpdateP2(rules, update):
    idx = IndexOfWrongUpdate(rules, update)
    if idx == []:
        return 0
    while idx != []:
        update[idx[0]], update[idx[1]] = update[idx[1]], update[idx[0]]
        idx = IndexOfWrongUpdate(rules, update)  
    return update[int(len(update)/2)]

# Returns the a list of invalid index for wrong update, empty list if all updates are correct 
def IndexOfWrongUpdate(rules, update):
    for i in range(0, len(update)):
        for j in range(i+1, len(update)):
            if not (update[j] in rules[update[i]]):
                return [i, j]
    return []

f = open("resources\day05.txt", "r")
#Rules is a dictionary with key as the first page in the rule and value as a list of valid second pages, to accelerate the search
rules = {}
for line in f:
    if line == "\n":
        break
    first, second = line.strip().split("|")
    if not (int(first) in rules):
        rules[int(first)] = []
    rules[int(first)].append(int(second))
updates = []
for line in f:
    updates.append([int(i) for i in line.strip().split(",")])
f.close()
print(f"Day 5/1: {P1(rules, updates)}")
print(f"Day 5/2: {P2(rules, updates)}")