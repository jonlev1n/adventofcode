import os
from aocd import lines, submit, get_data
import re
from sympy.solvers import solve
from sympy import Symbol


def parse(input):
    m = {}
    for line in input:
        key, math = line.split(": ")
        if math.isnumeric():
            m[key] = int(math)
        else:
            m[key] = math
    return m


def traverse(monkeys, key):
    if not type(monkeys[key]) == int:
        s = monkeys[key]
        try:
            op = re.findall(r"[-+*\/]", s)[0]
        except:
            return s
        key1, key2 = s.split(" %s " % op)
        v1 = traverse(monkeys, key1)
        v2 = traverse(monkeys, key2)
        if op == "-":
            try:
                monkeys[key] = v1 - v2
            except:
                monkeys[key] = "(%s - %s)" % (v1, v2)
        if op == "+":
            try:
                monkeys[key] = v1 + v2
            except:
                monkeys[key] = "(%s + %s)" % (v1, v2)
        if op == "*":
            try:
                monkeys[key] = int(v1 * v2)
            except:
                monkeys[key] = "(%s * %s)" % (v1, v2)
        if op == "/":
            try:
                monkeys[key] = int(v1 / v2)
            except:
                monkeys[key] = "(%s / %s)" % (v1, v2)
        return monkeys[key]
    else:
        return monkeys[key]


def main(input):
    m = parse(input)
    # m2 = m.copy()
    ans1 = traverse(m.copy(), "root")
    s = m["root"]
    op = re.findall(r"[-+*\/]", s)[0]
    key1, key2 = s.split(" %s " % op)
    m["humn"] = "x"
    m1 = m.copy()
    m2 = m.copy()
    v1 = traverse(m1, key1)
    v2 = traverse(m2, key2)
    if type(v1) == int:
        v1 = str(v1)
    if type(v2) == int:
        v2 = str(v2)
    # solve
    x = Symbol("x")
    ans2 = solve("%s - %s" % (v1, v2))[0]
    return ans1, ans2


test_data = [
    "root: pppw + sjmn",
    "dbpl: 5",
    "cczh: sllz + lgvd",
    "zczc: 2",
    "ptdq: humn - dvpt",
    "dvpt: 3",
    "lfqf: 4",
    "humn: 5",
    "ljgn: 2",
    "sjmn: drzm * dbpl",
    "sllz: 4",
    "pppw: cczh / lfqf",
    "lgvd: ljgn * ptdq",
    "drzm: hmdt - zczc",
    "hmdt: 32",
]

# main(test_data)
ans1, ans2 = main(lines)
submit(ans1, day=21, year=2022, part="a")
submit(ans2, day=21, year=2022, part="b")
