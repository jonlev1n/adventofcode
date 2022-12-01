import os
from aocd import lines, submit, get_data

test_data = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_data():
    with open(os.path.join(__location__, "input.txt")) as input:
        data = input.read()
    return data


def solve(input):
    tot = 0
    ribbon = 0
    for line in input:
        l, w, h = line.split("x")
        l = int(l)
        w = int(w)
        h = int(h)
        a = l * w
        b = l * h
        c = h * w
        sides = sorted([l, w, h])
        sides.pop()
        s1 = sides[0]
        s2 = sides[1]
        bow = l * w * h
        ribbon += bow + 2 * s1 + 2 * s2
        slack = min(a, b, c)
        tot += 2 * a + 2 * b + 2 * c + slack
    return (tot, ribbon)


data = get_data(day=2, year=2015)
data = data.splitlines()
(ans1, ans2) = solve(data)
submit(ans1, day=2, year=2015, part="a")
submit(ans2, day=2, year=2015, part="b")
