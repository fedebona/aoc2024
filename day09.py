# day 9 advent of code 2024
def P1(content):
    expandedDisk = expandDisk(content)

    # loop backwards
    for i in range(len(expandedDisk)-1, -1, -1):
        if expandedDisk[i] == '.':
            continue
        firstFreeSpace = expandedDisk.index('.')
        if firstFreeSpace >= i:
            break
        expandedDisk[firstFreeSpace] = expandedDisk[i]
        expandedDisk[i] = '.'
    return CalculateCheckSum(expandedDisk)

# expand the disk reading compact content
def expandDisk(content):
    i = 0
    id = 0
    expandedDisk = []
    for block in content:
        if i % 2 == 0:
            diskblock = int(block)
            for j in range(diskblock):
                expandedDisk.append(id)
            id = id + 1
        else:
            spaceblock = int(block)
            for j in range(spaceblock):
                expandedDisk.append('.')
        i = i + 1
    return expandedDisk

def CalculateCheckSum(disk):
    checksum = 0
    for i in range(len(disk)):
        if disk[i] == '.':
            continue
        checksum = checksum + i*disk[i]
    return checksum

def P2(f):
    expandedDisk = expandDisk(content)

    # loop backwards
    currentFile = '.'
    i = len(expandedDisk)-1
    id = expandedDisk[i]
    #Loop for each id except the first one
    while id > 0:
        currentFile = expandedDisk[i]
        j = i
        while expandedDisk[j] == currentFile:
            j = j - 1
        if currentFile == '.':
            i = j
            continue
        size = i - j
        newLocation = CheckForEnoughSpace(expandedDisk, size)
        # If there is no space before current location, we need to move to the next id
        if newLocation == -1 or newLocation > j:
            i = j
            id = id - 1
            continue
        for k in range(j, i):
            expandedDisk[newLocation] = currentFile
            expandedDisk[k + 1] = '.'
            newLocation = newLocation + 1
        i = j
        id = id - 1

    return CalculateCheckSum(expandedDisk)

def CheckForEnoughSpace(disk, size):
    l = ['.'] * size
    for i in range(len(disk) - size + 1):
        if disk[i:i + size] == l:
            return i
    return -1  # Return -1 if the sublist is not found

f = open("resources\day09.txt", "r")
content = f.read()
f.close()
print(f"Day 9/1: {P1(content)}")
print(f"Day 9/2: {P2(content)}")
