# day 22 advent of code 2024

def P1(numbers):
    for i in range(0, 2000):
        numbers = [NextValue(n) for n in numbers]
    return sum(numbers)


def Prune(n):
    return n % 16777216


def Mix(n1, n2):
    # bitwise xor
    return n1 ^ n2


def NextValue(n):
    step1 = Prune(Mix(n, n * 64))
    step2 = Prune(Mix(step1, int(step1 / 32)))
    return Prune(Mix(step2, 2048 * step2))


def P2(numbers):

    return


f = open("resources\day22.txt", "r")
numbers = [int(x.strip()) for x in f]
print(f"Day 4/1: {P1(numbers)}")
print(f"Day 4/2: {P2(numbers)}")
f.close()
