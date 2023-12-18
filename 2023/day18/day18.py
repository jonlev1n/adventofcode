from aocd import lines, submit, get_data
import numpy as np
import math

test_data = [
    "R 6 (#70c710)",
    "D 5 (#0dc571)",
    "L 2 (#5713f0)",
    "D 2 (#d2c081)",
    "R 2 (#59c680)",
    "D 2 (#411b91)",
    "L 5 (#8ceee2)",
    "U 2 (#caa173)",
    "L 1 (#1b58a2)",
    "U 2 (#caa171)",
    "R 2 (#7807d2)",
    "U 3 (#a77fa3)",
    "L 2 (#015232)",
    "U 2 (#7a21e3)",
]

D = {
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1),
    "U": (-1, 0),
}


def part1():
    # data = test_data
    data = lines
    a = 0
    p = (0, 0)
    V = []
    for s in data:
        [d, n, c] = s.split()
        n = int(n)
        a += n
        t = D[d]
        x = tuple([n * x for x in t])
        p1 = tuple(map(lambda c1, c2: c1 + c2, p, x))
        V.append((p, p1))
        p = p1

    area = 0
    for v in V:
        (y, x) = v
        area += y[1] * x[0] - y[0] * x[1]
    area = int(abs(area) / 2)

    square_area = int(area - a / 2 + 1)
    a += square_area
    ans1 = a
    print(ans1)
    return ans1


def part2():
    # data = test_data
    data = lines

    a = 0
    p = (0, 0)
    V = []
    dd = {0: "R", 1: "D", 2: "L", 3: "U"}
    for s in data:
        [_, _, c] = s.split()
        c = c.replace("(", "").replace("#", "").replace(")", "")
        n = int(c[0:5], 16)
        d = int(c[-1])
        a += n
        t = D[dd[d]]
        x = tuple([n * x for x in t])
        p1 = tuple(map(lambda c1, c2: c1 + c2, p, x))
        V.append((p, p1))
        p = p1

    area = 0
    for v in V:
        (y, x) = v
        area += y[1] * x[0] - y[0] * x[1]
    area = int(abs(area) / 2)

    square_area = int(area - a / 2 + 1)
    a += square_area
    ans2 = a
    print(ans2)
    return ans2


ans1 = part1()
ans2 = part2()

# submit(ans1, part="a", day=18, year=2023) # ! correct!
submit(ans2, part="b", day=18, year=2023)
