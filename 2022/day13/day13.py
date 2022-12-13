import os
from aocd import lines, submit, get_data
from functools import cmp_to_key


test_data = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_data():
    with open(os.path.join(__location__, "input.txt")) as input:
        data = input.read()
    return data


def compare(a, b):
    if isinstance(a, int):
        if isinstance(b, int):
            if a < b:
                return 1
            if b < a:
                return -1
            return 0
        return compare([a], b)
    if isinstance(b, int):
        return compare(a, [b])

    for si in range(min((len(a), len(b)))):
        sr = compare(a[si], b[si])
        if 1 == sr:
            return 1
        if -1 == sr:
            return -1

    if len(a) < len(b):
        return 1
    if len(b) < len(a):
        return -1

    return 0


def solve(input):
    packets = []
    correct = 0
    for idx, pair in enumerate(input.split("\n\n")):
        l, r = map(eval, pair.split("\n"))
        packets.append(l)
        packets.append(r)
        if compare(l, r) == 1:
            correct += idx + 1

    decoder = 1
    packets.append([[2]])
    packets.append([[6]])
    packets = sorted(packets, key=cmp_to_key(compare), reverse=True)
    for idx, packet in enumerate(packets):
        kk = ascii(packet)
        if "[[2]]" == kk:
            decoder *= idx + 1
        if "[[6]]" == kk:
            decoder *= idx + 1

    return correct, decoder


data = get_data(day=13, year=2022)
ans1, ans2 = solve(data)
submit(ans1, day=13, year=2022, part="a")
submit(ans2, day=13, year=2022, part="b")
