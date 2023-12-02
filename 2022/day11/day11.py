import os
from aocd import lines, submit, get_data
import re, math, numpy as np


test_data = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_data():
    with open(os.path.join(__location__, "input.txt")) as input:
        data = input.read()
    return data


def get_value(s, old, d, r):
    # s is string, old is list, d is modulo
    if not len(old):
        return ([], [])
    s = s[4:]
    ns = "np.floor((np.array(old)" + s + ")/ r)"
    new_l = eval(ns)
    true_dest = list(new_l[np.mod(new_l, d) == 0])
    false_dest = list(new_l[np.mod(new_l, d) != 0])
    return (true_dest, false_dest)


def solve(input, rounds, reducer):
    monkeys = {}
    supermod = 1
    for line in input:
        if "Monkey" in line:
            key = re.findall(r"\d+", line)[0]
            key = int(key)

        if "Starting items:" in line:
            items = re.findall(r"\d+", line)

        if "Operation:" in line:
            op = line.split("= ")[1]

        if "Test" in line:
            modulo = re.findall(r"\d+", line)[0]

        if "true" in line:
            true_dest = re.findall(r"\d+", line)[0]

        if "false" in line:
            false_dest = re.findall(r"\d+", line)[0]
            monkeys[key] = {
                "items": [int(i) for i in items],
                "op": op,
                "modulo": int(modulo),
                "true_dest": int(true_dest),
                "false_dest": int(false_dest),
                "count": 0,
            }

    for m in monkeys:
        supermod *= monkeys[m]["modulo"]

    for r in range(0, rounds):
        for m in monkeys.keys():
            monkey = monkeys[m]
            op = monkey["op"]
            items = monkey["items"]
            modulo = monkey["modulo"]
            true_dest = monkey["true_dest"]
            false_dest = monkey["false_dest"]
            count = monkey["count"]
            (td, fd) = get_value(op, items, modulo, reducer)
            monkeys[true_dest]["items"] += [x % supermod for x in td]
            monkeys[false_dest]["items"] += [x % supermod for x in fd]
            monkeys[m]["items"] = []
            monkeys[m]["count"] += len(items)
    counts = []
    for m in monkeys.keys():
        counts.append(monkeys[m]["count"])
    counts = sorted(counts, reverse=True)
    return counts[0] * counts[1]


test_data = [
    "Monkey 0:",
    "Starting items: 79, 98",
    "Operation: new = old * 19",
    "Test: divisible by 23",
    "If true: throw to monkey 2",
    "If false: throw to monkey 3",
    "",
    "Monkey 1:",
    "Starting items: 54, 65, 75, 74",
    "Operation: new = old + 6",
    "Test: divisible by 19",
    "If true: throw to monkey 2",
    "If false: throw to monkey 0",
    "",
    "Monkey 2:",
    "Starting items: 79, 60, 97",
    "Operation: new = old * old",
    "Test: divisible by 13",
    "If true: throw to monkey 1",
    "If false: throw to monkey 3",
    "",
    "Monkey 3:",
    "Starting items: 74",
    "Operation: new = old + 3",
    "Test: divisible by 17",
    "If true: throw to monkey 0",
    "If false: throw to monkey 1",
]

# test_ans = solve(test_data, 10000)
# print(test_ans)

ans1 = solve(lines, 20, 3)
submit(ans1, day=11, year=2022, part="a")
ans2 = solve(lines, 10000, 1)
submit(ans2, day=11, year=2022, part="b")
