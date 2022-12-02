import os
from aocd import lines, submit, get_data
import re

test_data = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_data():
    with open(os.path.join(__location__, "input.txt")) as input:
        data = input.read()
    return data


test_data = [
    "NOT y -> i",
    "NOT x -> h",
    "y RSHIFT 2 -> g",
    "x LSHIFT 2 -> f",
    "x OR y -> e",
    "x AND y -> d",
    "456 -> y",
    "123 -> x",
]


def solve_a(input):
    values = {}
    errors = True

    while errors:
        errors = False
        for line in input:
            l = line.split(" -> ")
            num = l[0].isnumeric() or len(l[0]) < 3
            if num:
                try:
                    value = int(l[0]) if l[0].isnumeric() else values[l[0]]
                    values[l[1]] = value
                except:
                    errors = True

            else:
                try:
                    if "AND" in l[0]:
                        v = l[0].split(" AND ")
                        v1 = int(v[0]) if v[0].isnumeric() else values[v[0]]
                        v2 = int(v[1]) if v[1].isnumeric() else values[v[1]]
                        values[l[1]] = v1 & v2

                    if "OR" in l[0]:
                        # split again
                        v = l[0].split(" OR ")
                        v1 = int(v[0]) if v[0].isnumeric() else values[v[0]]
                        v2 = int(v[1]) if v[1].isnumeric() else values[v[1]]
                        values[l[1]] = v1 | v2

                    if "NOT" in l[0]:
                        # split again
                        v = l[0].split("NOT ")
                        v1 = int(v[1]) if v[1].isnumeric() else values[v[1]]
                        values[l[1]] = 65535 - v1

                    if "RSHIFT" in l[0]:
                        v = l[0].split(" RSHIFT ")
                        v1 = int(v[0]) if v[0].isnumeric() else values[v[0]]
                        shift = int(v[1])
                        values[l[1]] = v1 >> shift

                    if "LSHIFT" in l[0]:
                        # split again
                        v = l[0].split(" LSHIFT ")
                        v1 = int(v[0]) if v[0].isnumeric() else values[v[0]]
                        shift = int(v[1])
                        values[l[1]] = v1 << shift

                except Exception as e:
                    errors = True
    return values


def solve_b(ans1, input):
    values = {}
    errors = True

    while errors:
        errors = False
        for line in input:
            if line == "14146 -> b":
                line = "%d -> b" % ans1
            l = line.split(" -> ")
            num = l[0].isnumeric() or len(l[0]) < 3
            if num:
                try:
                    value = int(l[0]) if l[0].isnumeric() else values[l[0]]
                    values[l[1]] = value
                except:
                    errors = True

            else:
                try:
                    if "AND" in l[0]:
                        v = l[0].split(" AND ")
                        v1 = int(v[0]) if v[0].isnumeric() else values[v[0]]
                        v2 = int(v[1]) if v[1].isnumeric() else values[v[1]]
                        values[l[1]] = v1 & v2

                    if "OR" in l[0]:
                        # split again
                        v = l[0].split(" OR ")
                        v1 = int(v[0]) if v[0].isnumeric() else values[v[0]]
                        v2 = int(v[1]) if v[1].isnumeric() else values[v[1]]
                        values[l[1]] = v1 | v2

                    if "NOT" in l[0]:
                        # split again
                        v = l[0].split("NOT ")
                        v1 = int(v[1]) if v[1].isnumeric() else values[v[1]]
                        values[l[1]] = 65535 - v1

                    if "RSHIFT" in l[0]:
                        v = l[0].split(" RSHIFT ")
                        v1 = int(v[0]) if v[0].isnumeric() else values[v[0]]
                        shift = int(v[1])
                        values[l[1]] = v1 >> shift

                    if "LSHIFT" in l[0]:
                        # split again
                        v = l[0].split(" LSHIFT ")
                        v1 = int(v[0]) if v[0].isnumeric() else values[v[0]]
                        shift = int(v[1])
                        values[l[1]] = v1 << shift

                except Exception as e:
                    errors = True
    return values


data = get_data(day=7, year=2015)
data = data.splitlines()
ans1 = solve_a(data)["a"]
submit(ans1, day=7, year=2015, part="a")
ans2 = solve_b(ans1, data)["a"]
submit(ans2, day=7, year=2015, part="b")
