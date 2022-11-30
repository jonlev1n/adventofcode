from data import field


height = len(field)
width = len(field[0])


xIdx1 = 0
xIdx2 = 0
xIdx3 = 0
xIdx4 = 0
xIdx5 = 0

numTrees1 = 0
numTrees2 = 0
numTrees3 = 0
numTrees4 = 0
numTrees5 = 0


for i in range(0, height):
    # is the current space a tree?
    if field[i][xIdx1 % width] == "#":
        numTrees1 += 1
    if field[i][xIdx2 % width] == "#":
        numTrees2 += 1
    if field[i][xIdx3 % width] == "#":
        numTrees3 += 1
    if field[i][xIdx4 % width] == "#":
        numTrees4 += 1

    # advance the "x" index
    xIdx1 += 1
    xIdx2 += 3
    xIdx3 += 5
    xIdx4 += 7

for i in range(0, height, 2):
    if field[i][xIdx5 % width] == "#":
        numTrees5 += 1

    # advance xIdx
    xIdx5 += 1

print(numTrees1 * numTrees2 * numTrees3 * numTrees4 * numTrees5)
