import os
from aocd import lines, submit, get_data


test_data = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_data():
    with open(os.path.join(__location__, "input.txt")) as input:
        data = input.read()
    return data


def solve_a(input):
    coords = ["0,0"]
    x = y = 0
    for i in input:
        if i == "^":
            y += 1
        if i == "v":
            y -= 1
        if i == ">":
            x += 1
        if i == "<":
            x -= 1

        coord = "%d,%d" % (x, y)
        if coord not in coords:
            coords.append(coord)

    return len(coords)


def solve_b(input):
    coords = ["0,0"]
    s1x = s2x = s1y = s2y = 0
    for idx, i in enumerate(input):
        if idx % 2 == 0:
            # s1 moves
            if i == "^":
                s1y += 1
            if i == "v":
                s1y -= 1
            if i == ">":
                s1x += 1
            if i == "<":
                s1x -= 1
        else:
            if i == "^":
                s2y += 1
            if i == "v":
                s2y -= 1
            if i == ">":
                s2x += 1
            if i == "<":
                s2x -= 1

        s1c = "%d,%d" % (s1x, s1y)
        s2c = "%d,%d" % (s2x, s2y)
        if s1c not in coords:
            coords.append(s1c)
        if s2c not in coords:
            coords.append(s2c)
    return len(coords)


data = get_data(year=2015, day=3)
ans1 = solve_a(data)
ans2 = solve_b(data)
submit(ans1, day=3, year=2015, part="a")
submit(ans2, day=3, year=2015, part="b")
