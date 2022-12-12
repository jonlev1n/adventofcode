import os
from aocd import lines, submit, get_data
import string, numpy as np

test_data = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_data():
    with open(os.path.join(__location__, "input.txt")) as input:
        data = input.read()
    return data


def get_start_finish(input):
    for i in range(0, len(input)):
        for j in range(0, len(input[i])):
            if input[i][j] == "S":
                start = (i, j)
            if input[i][j] == "E":
                end = (i, j)
    return (start, end)


def get_elevation(e):
    if e == "S":
        return get_elevation("a")
    if e == "E":
        return get_elevation("z")
    return string.ascii_letters.index(e)


def get_neighbors(input, coords, elevation):
    # surround = [(-1, 1), (-1, 0), (-1, -1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]
    surround = [
        (1, 0),
        (-1, 0),
        (0, -1),
        (0, 1),
    ]  # ordering this way prioritizes going forward
    s_coords = [tuple(np.add(coords, s)) for s in surround]
    # neighbors = {}
    neighbors = []
    for s in s_coords:
        if s[0] in range(0, len(input)) and s[1] in range(0, len(input[0])):
            n = input[s[0]][s[1]]
            if get_elevation(n) - elevation <= 1:
                neighbors.append((s[0], s[1]))
                # if n in neighbors.keys():
                #     neighbors[n].append((s[0], s[1]))
                # else:
                #     neighbors[n] = [(s[0], s[1])]
    return neighbors


def solve(c, visited):
    print(c)
    while c != end:
        e = get_elevation(input[c[0]][c[1]])
        n = get_neighbors(input, c, e)
        if len(n) > 1:
            for new_c in n:
                solve(new_c, visited)
        if len(n) == 0 or all(new_c in visited for new_c in n):
            # dead end condition
            print("dead ending!")
            return "dead end"

        # pick the next one
        # move to the first one that you havent already been to?
        for new_c in n:
            if new_c not in visited:
                c = new_c

        visited.append(c)

    visited.append(end)
    return len((list(set(visited))))


test_data = [
    "Sabqponm",
    "abcryxxl",
    "accszExk",
    "acctuvwj",
    "abdefghi",
]
# test_ans = solve(test_data)
# print(test_ans)x

(start, end) = get_start_finish(test_data)
visited = []
c = start
visited = [c]
x = solve(c, visited)


# ans1 = solve(lines)
# submit(ans1, day=12, year=2022, part="a")
# ans2 = solve(lines)
# submit(ans2, day=12, year=2022, part="b")
