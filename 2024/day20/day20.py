from aocd import lines, submit, get_data
from collections import deque
from itertools import combinations


test_data = [
    "###############",
    "#...#...#.....#",
    "#.#.#.#.#.###.#",
    "#S#...#.#.#...#",
    "#######.#.#.###",
    "#######.#.#...#",
    "#######.#.###.#",
    "###..E#...#...#",
    "###.#######.###",
    "#...###...#...#",
    "#.#####.#.###.#",
    "#.#...#.#.#...#",
    "#.#.#.#.#.#.###",
    "#...#...#...###",
    "###############",
]


def parse_input():
    grid = lines
    s = e = None
    for i, row in enumerate(lines):
        for j, v in enumerate(row):
            if v == "S":
                s = (i, j)
            elif v == "E":
                e = (i, j)
    return grid, s, e


GRID, S, E = parse_input()
N, M = len(GRID), len(GRID[0])


def bfs():
    q = deque([(*S, [S])])
    seen = {S}
    while q:
        i, j, path = q.popleft()
        if (i, j) == E:
            return path
        for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if (
                0 <= ni < N
                and 0 <= nj < M
                and GRID[ni][nj] != "#"
                and (ni, nj) not in seen
            ):
                seen.add((ni, nj))
                q.append((ni, nj, path + [(ni, nj)]))


PATH = bfs()


def solve(cheat=2):
    path_length = len(PATH) - 1
    cost_start = {u: i for i, u in enumerate(PATH)}
    cost_end = {u: i for i, u in enumerate(reversed(PATH))}
    res = 0
    for u, v in combinations(PATH, 2):
        dist = sum(abs(x - y) for x, y in zip(u, v))
        if dist > cheat:
            continue
        if path_length - (cost_start[u] + cost_end[v] + dist) >= 100:
            res += 1
    return res


def part1():
    return solve()


def part2():
    return solve(20)


ans1 = part1()
ans2 = part2()
print(f"Part 1: {ans1}")
print(f"Part 2: {ans2}")


# uncomment these lines to submit
submit(ans1, part="a", day=20, year=2024)
submit(ans2, part="b", day=20, year=2024)
