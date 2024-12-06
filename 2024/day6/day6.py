from re import A
from aocd import lines, submit, get_data
import numpy as np
from collections import defaultdict
from bisect import insort, bisect

test_data = [
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#...",
]
# y,x
UP = (-1, 0)
RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)

RIGHT_TURN = {UP: RIGHT, RIGHT: DOWN, DOWN: LEFT, LEFT: UP}


def part1():
    # data = test_data
    data = lines

    arr = [[x for x in row] for row in data]
    arr = np.array(arr)
    start = np.where(arr == "^")
    start = (start[0][0], start[1][0])
    minY = 0
    minX = 0
    maxY = len(arr) - 1
    maxX = len(arr[0]) - 1

    d = UP
    c = start
    next_space = tuple(map(sum, zip(start, d)))

    p = [start]
    while True:
        print(c)
        next_space = tuple(map(sum, zip(c, d)))
        if not (minY <= next_space[0] <= maxY and minX <= next_space[1] <= maxX):
            if c not in p:
                p.append(c)
            break
        if arr[next_space[0]][next_space[1]] == "#":
            print("hit #")
            d = RIGHT_TURN[d]
            next_space = tuple(map(sum, zip(c, d)))

        c = next_space
        if c not in p:
            p.append(c)

    ans1 = len(p)
    print(ans1)
    return ans1


def part2():
    # data = test_data
    data = lines
    grid = [[x for x in row] for row in data]
    m, n = len(grid), len(grid[0])
    obstacles = {
        "rows": defaultdict(list),
        "cols": defaultdict(list),
    }
    for r in range(m):
        for c in range(n):
            if grid[r][c] == "#":
                insort(obstacles["rows"][r], c)
                insort(obstacles["cols"][c], r)
            if grid[r][c] == "^":
                start = (r, c, "up")

    def move(r, c, d, obstacles):
        r_obs = obstacles["rows"][r]
        c_obs = obstacles["cols"][c]

        if d == "up":
            if not c_obs or c_obs[0] > r:
                new_r = -1
            else:
                i = bisect(c_obs, r)
                new_r = c_obs[i - 1] + 1
            return new_r, c, "right"

        if d == "right":
            if not r_obs or r_obs[-1] < c:
                new_c = n
            else:
                i = bisect(r_obs, c)
                new_c = r_obs[i] - 1
            return r, new_c, "down"

        if d == "down":
            if not c_obs or c_obs[-1] < r:
                new_r = m
            else:
                i = bisect(c_obs, r)
                new_r = c_obs[i] - 1
            return new_r, c, "left"

        if d == "left":
            if not r_obs or r_obs[0] > c:
                new_c = -1
            else:
                i = bisect(r_obs, c)
                new_c = r_obs[i - 1] + 1
            return r, new_c, "up"

    candidates = set()
    r, c, d = start
    while r in range(m) and c in range(n):
        new_r, new_c, new_d = move(r, c, d, obstacles)
        if d == "up":
            candidates |= set((i, c) for i in range(new_r + 1, r + 1))
        elif d == "right":
            candidates |= set((r, j) for j in range(c, new_c))
        elif d == "down":
            candidates |= set((i, c) for i in range(r, new_r))
        elif d == "left":
            candidates |= set((r, j) for j in range(new_c + 1, c + 1))
        r, c, d = new_r, new_c, new_d

    def is_looping(obstacles):
        r, c, d = start
        visited = set([start])
        while r in range(m) and c in range(n):
            r, c, d = move(r, c, d, obstacles)
            if (r, c, d) in visited:
                return True
            visited.add((r, c, d))
        return False

    loop_count = 0
    for r, c in candidates:
        insort(obstacles["rows"][r], c)
        insort(obstacles["cols"][c], r)
        loop_count += is_looping(obstacles)
        obstacles["rows"][r].remove(c)
        obstacles["cols"][c].remove(r)

    return loop_count


ans1 = part1()
ans2 = part2()

# uncomment these lines to submit
# submit(ans1, part="a", day=6, year=2024)
submit(ans2, part="b", day=6, year=2024)
