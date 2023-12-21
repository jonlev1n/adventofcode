from aocd import lines, submit, get_data
from collections import defaultdict, deque
import numpy as np


test_data = [
    "...........",
    ".....###.#.",
    ".###.##..#.",
    "..#.#...#..",
    "....#.#....",
    ".##..S####.",
    ".##..#...#.",
    ".......##..",
    ".##.#.####.",
    ".##..##.##.",
    "...........",
]


def part1():
    # data = test_data
    data = lines

    A = np.array([[c for c in s] for s in data])
    steps = 64
    sy, sx = np.where(A == "S")

    P = [(sy[0], sx[0])]
    D = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(0, steps):
        NP = []
        for p in P:
            for d in D:
                y, x = tuple(map(lambda i, j: i + j, p, d))
                if A[y][x] != "#":
                    NP.append((y, x))
        P = list(set(NP))

    ans1 = len(P)
    print(ans1)
    return ans1


def part2():
    # data = test_data
    data = lines

    grid = {}
    start = None
    w = len(data[0])
    h = len(data)
    for y, v1 in enumerate(data):
        for x, v2 in enumerate(v1):
            grid[(x, y)] = v2
            if v2 == "S":
                start = (x, y)

    steps = 26501365
    neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = defaultdict(set)
    visited[0].add(start)
    prev_len = 0
    a = []
    for s in range(steps):
        for point in visited[s]:
            x, y = point
            for n in neighbors:
                dx, dy = n
                ix, iy = x + dx, y + dy
                # print(x, dx, y, dy, ix, iy, grid.get((ix, iy), None))
                if grid.get((ix % w, iy % h), None) in [".", "S"]:
                    visited[s + 1].add((ix, iy))

        if s % w == steps % w:
            print(s, len(visited.get(s)), len(visited.get(s)) - prev_len, s // w)
            prev_len = len(visited.get(s))
            a.append(prev_len)

        if len(a) == 3:
            break

    # print(len(visited.get(len(visited)-1)))

    def f(n):
        b0 = a[0]
        b1 = a[1] - a[0]
        b2 = a[2] - a[1]
        return b0 + b1 * n + (n * (n - 1) // 2) * (b2 - b1)

    ans2 = f(steps // w)
    print(ans2)
    return ans2


ans1 = part1()
ans2 = part2()

# uncomment these lines to submit
submit(ans1, part="a", day=21, year=2023)
# submit(ans2, part="b", day=21, year=2023)
