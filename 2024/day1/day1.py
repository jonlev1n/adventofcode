import os
from aocd import lines, submit, get_data
import re


def part1():
    # data = test_data
    data = lines
    l = []
    r = []
    for row in data:
        l_num, r_num = row.split("   ")
        l.append(int(l_num))
        r.append(int(r_num))

    l.sort()
    r.sort()

    s = 0
    for i in range(0, len(r)):
        s += abs(r[i] - l[i])

    # submit(s, part="a", day=1, year=2024)


def part2():
    data = lines
    l = []
    r = []
    for row in data:
        l_num, r_num = row.split("   ")
        l.append(int(l_num))
        r.append(int(r_num))

    s = 0
    for i in range(0, len(l)):
        n = l[i]
        m = r.count(n)
        s += n * m

    submit(s, part="b", day=1, year=2024)


# part1()
part2()
