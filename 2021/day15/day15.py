import numpy as np
from aocd import lines
import math

test_data = [
    "1163751742",
    "1381373672",
    "2136511328",
    "3694931569",
    "7463417111",
    "1319128137",
    "1359912421",
    "3125421639",
    "1293138521",
    "2311944581",
]

# data = test_data
data = lines

a = [[int(n) for n in d] for d in data]
a = np.array(a)


def find_adj(cur, visited, l, w):
    x = cur[1]  # col
    y = cur[0]  # row
    adj = []
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if (
                i >= 0
                and j >= 0
                and i < w
                and j < l
                and not (x == i and y == j)
                and (x == i or y == j)  #! no diagonal
            ):
                adj.append((j, i))
    return adj


# find the min score for all adj
# part1([start])


def one(arr):

    l, w = arr.shape
    dists = np.full(arr.shape, l ** 2)
    # start in top left
    start = (0, 0)
    dists[0][0] = 0
    visited = []
    cur = start
    for i in range(0, l):
        for j in range(0, w):
            cur = (j, i)
            adj = find_adj(cur, visited, l, w)
            for pt in adj:

                pt_val = arr[pt[0]][pt[1]]
                cur_dist = dists[cur[0]][cur[1]]
                min_dist = dists[pt[0]][pt[1]]

                if cur_dist + pt_val < min_dist:
                    dists[pt[0]][pt[1]] = cur_dist + pt_val

    min_dist = int(dists[l - 1][w - 1] - dists[0][0])
    print(dists)
    print(min_dist)


def two():
    ret = make_massive(a)
    print(a)
    print("")
    print(ret)
    one(ret)


def make_massive(arr):
    l, w = arr.shape
    b = np.zeros((l * 5, w * 5), dtype=int)

    for i in range(0, 5):
        for j in range(0, 5):
            c = arr + i + j
            for q in range(0, l):
                for z in range(0, w):
                    if c[q][z] > 9:
                        c[q][z] -= 9

            # once c is determined...
            b[i * l : i * l + l, j * w : j * w + w] = c
    zed = np.array([[int(n) for n in d] for d in b])
    return zed


one(a)
two()
