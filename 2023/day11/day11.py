import numpy as np
import math
from aocd import lines, submit, get_data


test_data = [
    "...#......",
    ".......#..",
    "#.........",
    "..........",
    "......#...",
    ".#........",
    ".........#",
    "..........",
    ".......#..",
    "#...#.....",
]


def part1():
    # data = test_data
    data = lines
    # transform to 2d np array
    data = np.array([[c for c in string] for string in data])

    empty_rows = []
    empty_cols = []

    for idx, row in enumerate(data):
        if (row == ".").all():
            empty_rows.append(idx)

    for idx, col in enumerate(data.T):
        if (col == ".").all():
            empty_cols.append(idx)

    # insert nows and colums
    num_inserted = 0
    for r in empty_rows:
        data = np.insert(data, r + num_inserted, ".", axis=0)
        num_inserted += 1

    num_inserted = 0
    for c in empty_cols:
        data = np.insert(data, c + num_inserted, ".", axis=1)
        num_inserted += 1

    # get idx of #
    ys, xs = np.where(data == "#")
    #  transform to tuple
    c = [(ys[i], xs[i]) for i in range(0, len(ys))]
    # get all possible pairs as tuples of idxs of c
    p = [[p1, p2] for idx, p1 in enumerate(c) for p2 in c[idx + 1 :]]
    # get all min dists
    dists = 0
    for d in p:
        [c1, c2] = d
        y1, x1 = c1
        y2, x2 = c2
        dist = abs(y2 - y1) + abs(x2 - x1)
        dists += dist

    print("total:", dists)
    return dists


def part2():
    # data = test_data
    data = lines
    # transform to 2d np array
    data = np.array([[c for c in string] for string in data])

    empty_rows = []
    empty_cols = []

    for idx, row in enumerate(data):
        if (row == ".").all():
            empty_rows.append(idx)

    for idx, col in enumerate(data.T):
        if (col == ".").all():
            empty_cols.append(idx)

    ys, xs = np.where(data == "#")
    #  transform to tuple
    c = [(ys[i], xs[i]) for i in range(0, len(ys))]
    # get all possible pairs as tuples of idxs of c
    p = [[p1, p2] for idx, p1 in enumerate(c) for p2 in c[idx + 1 :]]

    dists = 0
    for d in p:
        [c1, c2] = d
        y1, x1 = c1
        y2, x2 = c2
        # original dist
        d0 = abs(y2 - y1) + abs(x2 - x1)
        # get ranges
        x_range = range(min(x1, x2) + 1, max(x1, x2))
        y_range = range(min(y1, y2) + 1, max(y1, y2))
        # get intersections of empty rows/cols in these ranges
        intersections = 0
        for r in empty_rows:
            if r in y_range:
                intersections += 1

        for c in empty_cols:
            if c in x_range:
                intersections += 1

        # for each intersecion add the appropriate number of extra steps
        scale = 1000000
        dist = d0 + intersections * (scale - 1)
        dists += dist

    print("total:", dists)
    return dists


ans1 = part1()
ans2 = part2()

# submit(ans1, part="a", day=11, year=2023) #! correct!
# submit(ans2, part="b", day=11, year=2023) #! correct!
