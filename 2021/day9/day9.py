from aocd import lines
import numpy as np
test_data = [
    "2199943210",
    "3987894921",
    "9856789892",
    "8767896789",
    "9899965678",
]

# data = test_data
data = lines
arr  = []
for row in data:
    n = []
    for s in row:
        n.append(int(s))
    arr.append(n)

a = np.array(arr)

# part 1 - iterate through and find the low points
low_points = []
low_idx = []
for i, r in enumerate(a):
    for j, c in enumerate(r):
        curr = a[i][j]
        # if i = 0:

        # if i = len(r):
        adj = []
        if i-1 >= 0:
            adj.append(a[i-1][j])
        if j - 1 >= 0:
            adj.append(a[i][j-1])
        if i + 1 < len(a):
            adj.append(a[i+1][j])
        if j + 1 < len(r):
            adj.append(a[i][j+1])

        if all(adj > curr):
            low_points.append(curr)
            low_idx.append((i,j))

ans1 = sum(low_points) + len(low_points)
# 21   43210
# 3 878 4 21
#  85678 8 2
# 87678 678 
#  8   65678


# init basins
basins = dict()
for l in low_idx:
    basins[l] = [l]

# total basin size should be all elements NOT 9
total_basin_size = np.count_nonzero(a!=9)
cond = sum(len(x) for x in basins.values()) == total_basin_size

counted = []
while(not cond):
    for i, r in enumerate(a):
        for j, c in enumerate(r):

            adj = []
            if i-1 >= 0:
                adj.append((i-1,j))
            if j - 1 >= 0:
                adj.append((i,j-1))
            if i + 1 < len(a):
                adj.append((i+1,j))
            if j + 1 < len(r):
                adj.append((i,j+1))

            # check if it is next to a point that is in a basin
            for k in basins.keys():
                # print(i,j)
                if any([x in basins[k] for x in adj]) and (i,j) not in basins[k] and a[i][j] != 9:
                    basins[k].append((i,j))

    cond = sum(len(x) for x in basins.values()) == total_basin_size
    
sizes = [len(x) for x in basins.values()]
# only need 3 largest
largest = []
# print(sizes)
for i in range (0,3):
    largest.append(max(sizes))
    sizes.remove(max(sizes))
print(np.prod(largest))


