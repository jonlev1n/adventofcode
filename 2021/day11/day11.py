import numpy as np
from aocd import lines

test_data = [
    "5483143223",
    "2745854711",
    "5264556173",
    "6141336146",
    "6357385478",
    "4167524645",
    "2176841721",
    "6882881134",
    "4846848554",
    "5283751526",
]

data = lines

# data = test_data

# create array
arr  = []
for row in data:
    n = []
    for s in row:
        n.append(int(s))
    arr.append(n)

a = np.array(arr)


steps = 100


flashes = 0
cond = True
s = 0
while(cond):
# for s in range(0, steps):
    flashed = []
    # first increase every octopus by one
    for i,r in enumerate(a):
        for j,c in enumerate(r):
            a[i][j] += 1

            if a[i][j] > 9:
                flashed.append((i,j))
    
    for i,j in flashed:
        adj = []
        for x in range(i-1, i+2):
            for y in range(j-1,j+2):
                if x >= 0 and y >= 0 and x < len(a) and y < len(a[0]) and not (x == i and y == j):
                    val = a[x][y] 
                    adj.append((x,y))
                else:
                    pass

        for x,y in adj:
            if (x,y) not in flashed:
                a[x][y] += 1
                if a[x][y] > 9:
                    flashed.append((x,y))
        


    
    for i,r in enumerate(a):
        for j,c in enumerate(r):
            if a[i][j] > 9:
                flashes += 1
                a[i][j] = 0
    
    if s == steps - 1:
        ans1 = flashes

    cond = not np.all(a == 0)
    s+=1

ans2 = s
print(ans1)
print(ans2)