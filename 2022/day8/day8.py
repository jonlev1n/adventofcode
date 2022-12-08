import os
from aocd import lines, submit, get_data


test_data = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_data():
    with open(os.path.join(__location__, "input.txt")) as input:
        data = input.read()
    return data


def solve_a(input):
    y = len(input)  # length
    x = len(input[0])  # width
    vis = x * 2 + (y - 2) * 2

    # i is y coord, j is x
    for i in range(1, y - 1):
        for j in range(1, x - 1):
            n = []
            e = []
            w = []
            s = []
            tree = int(input[i][j])
            for h in range(0, x):
                if h == j:
                    continue
                if h < j:
                    w.append(tree > int(input[i][h]))
                if h > j:
                    e.append(tree > int(input[i][h]))
            for v in range(0, y):
                if v == i:
                    continue
                if v < i:
                    n.append(tree > int(input[v][j]))
                if v > i:
                    s.append(tree > int(input[v][j]))

            if all(n) or all(e) or all(w) or all(s):
                vis += 1

    return vis


def solve_b(input):
    y = len(input)  # length
    x = len(input[0])  # width
    vis = x * 2 + (y - 2) * 2
    max_score = 0

    # i is y coord, j is x
    for i in range(1, y - 1):
        for j in range(1, x - 1):
            n = []
            e = []
            w = []
            s = []
            tree = int(input[i][j])
            for h in range(0, x):
                c = tree > int(input[i][h])
                if h == j:
                    continue
                if h < j:
                    w.insert(0, c)
                if h > j:
                    e.append(c)
            for v in range(0, y):
                c = tree > int(input[v][j])
                if v == i:
                    continue
                if v < i:
                    n.insert(0, c)
                if v > i:
                    s.append(c)

            try:
                s1 = n.index(False) + 1
            except:
                s1 = len(n)
            try:
                s2 = e.index(False) + 1
            except:
                s2 = len(e)
            try:
                s3 = w.index(False) + 1
            except:
                s3 = len(w)
            try:
                s4 = s.index(False) + 1
            except:
                s4 = len(s)

            score = s1 * s2 * s3 * s4
            if score > max_score:
                max_score = score

    return max_score


test_data = [
    "30373",
    "25512",
    "65332",
    "33549",
    "35390",
]


ans1 = solve_a(lines)
submit(ans1, day=8, year=2022, part="a")
ans2 = solve_b(lines)
submit(ans2, day=8, year=2022, part="b")
