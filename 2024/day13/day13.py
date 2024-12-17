from aocd import lines, submit, get_data
import numpy as np
import re

test_data = [
    "Button A: X+94, Y+34",
    "Button B: X+22, Y+67",
    "Prize: X=8400, Y=5400",
    "",
    "Button A: X+26, Y+66",
    "Button B: X+67, Y+21",
    "Prize: X=12748, Y=12176",
    "",
    "Button A: X+17, Y+86",
    "Button B: X+84, Y+37",
    "Prize: X=7870, Y=6450",
    "",
    "Button A: X+69, Y+23",
    "Button B: X+27, Y+71",
    "Prize: X=18641, Y=10279",
]


def part1():
    # data = test_data
    data = lines

    s = 0
    for i in range(0, len(data), 4):
        n1, n2 = map(int, re.findall(r"\d+", data[i]))
        n3, n4 = map(int, re.findall(r"\d+", data[i + 1]))
        n5, n6 = map(int, re.findall(r"\d+", data[i + 2]))

        a = np.array([[n1, n3], [n2, n4]])
        b = np.array([n5, n6])
        sol = np.linalg.solve(a, b)
        mask = [np.isclose(0, val % 1) or np.isclose(1, val % 1) for val in sol]
        if all(mask):
            s += 3 * int(round(sol[0])) + int(round(sol[1]))

    ans1 = s
    print(ans1)
    return ans1


def part2():
    # data = test_data
    data = lines
    np.set_printoptions(suppress=True)

    s = 0
    for i in range(0, len(data), 4):
        n1, n2 = map(int, re.findall(r"\d+", data[i]))
        n3, n4 = map(int, re.findall(r"\d+", data[i + 1]))
        n5, n6 = map(int, re.findall(r"\d+", data[i + 2]))

        n5 += 10000000000000
        n6 += 10000000000000

        a = np.array([[n1, n3], [n2, n4]])
        b = np.array([n5, n6])
        sol = np.round(np.linalg.solve(a, b))
        s += sol @ (3, 1) if (b == sol @ a.T).all() else 0

    ans2 = int(s)
    print(ans2)
    return ans2


ans1 = part1()
ans2 = part2()

# uncomment these lines to submit
submit(ans1, part="a", day=13, year=2024)
submit(ans2, part="b", day=13, year=2024)
