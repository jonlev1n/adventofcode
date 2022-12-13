import os
from aocd import lines, submit, get_data
import string, numpy as np, networkx as nx, math

test_data = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_data():
    with open(os.path.join(__location__, "input.txt")) as input:
        data = input.read()
    return data


def get_start_end(input):
    for i in range(0, len(input)):
        for j in range(0, len(input[i])):
            if input[i][j] == "S":
                start = (i, j)
            if input[i][j] == "E":
                end = (i, j)

    return (start, end)


def get_as(input):
    all_a = []
    for i in range(0, len(input)):
        for j in range(0, len(input[i])):
            if input[i][j] == "a":
                all_a.append((i, j))
    return all_a


def get_elevation(e):
    if e == "S":
        return get_elevation("a")
    if e == "E":
        return get_elevation("z")
    return string.ascii_letters.index(e)


def get_connected(input, coords):
    c = input[coords[0]][coords[1]]
    cur_elevation = get_elevation(c)
    surround = [
        (1, 0),
        (-1, 0),
        (0, -1),
        (0, 1),
    ]
    s_coords = [tuple(np.add(coords, s)) for s in surround]
    connected = []
    for s in s_coords:
        if s[0] in range(0, len(input)) and s[1] in range(0, len(input[0])):
            n = input[s[0]][s[1]]
            if get_elevation(n) - cur_elevation <= 1:
                connected.append((s[0], s[1]))
    return connected


def solve(input):

    (start, end) = get_start_end(input)
    all_a = get_as(input)
    all_a.insert(0, start)
    steps = []
    for start in all_a:
        dists = {}
        # distance to all other nodes should be infinite
        for i in range(0, len(input)):
            for j in range(0, len(input[0])):
                dists[(i, j)] = math.inf

        dists[start] = 0

        visited = []
        queue = [start]
        while len(queue) != 0:
            current = queue.pop(0)
            if current in visited:
                continue
            visited.append(current)
            connected = get_connected(input, current)
            for c in connected:
                if c not in visited:
                    queue.append(c)
                cur_dist = dists[current]
                new_dist = 1 + cur_dist
                connected_dist = dists[(c[0], c[1])]
                if new_dist < connected_dist:
                    dists[c[0], c[1]] = new_dist
        steps.append(dists[end])
    return (steps[0], min(steps))


test_data = [
    "Sabqponm",
    "abcryxxl",
    "accszExk",
    "acctuvwj",
    "abdefghi",
]

# print(solve(test_data))
(ans1, ans2) = solve(lines)
submit(ans1, day=12, year=2022, part="a")
submit(ans2, day=12, year=2022, part="b")
