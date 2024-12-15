# day 11 advent of code 2024

def P1(stones):  
    return Iterate(stones, 25)

def P2(stones):  
    return Iterate(stones, 75)

def Iterate(stones, iterations):
    for i in range(0, iterations):
        print(f"iteration {i}:\t, stones {stones}\n")
        nextStones = []
        for stone in stones:
            nextStones.extend(NextStones(stone))
        stones = nextStones
    return len(stones)

def NextStones(stone):
    if stone == 0:
        return [1]
    stringStone = str(stone)
    if len(stringStone) % 2 == 0:
        c = int(len(stringStone)/2)
        return [int(stringStone[:c]), int(stringStone[c:])]
    else:
        return [stone * 2024]




f = open("resources\day11_test.txt", "r")
stones = [int(x) for x in f.read().split(" ")]
print(f"Day 11/1: {P1(stones)}")
#print(f"Day 11/2: {P2(stones)}")
f.close()
