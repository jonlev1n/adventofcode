from time import clock_getres
from aocd import lines, submit, get_data
import re
from itertools import permutations


test_data = [
    "r, wr, b, g, bwu, rb, gb, br",
    "",
    "brwrr",
    "bggr",
    "gbbr",
    "rrbgbr",
    "ubwu",
    "bwurrg",
    "brgr",
    "bbrgwb",
]


def find_towel_combos(w, towels, memo, is_part_one) -> int:
    if len(w) == 0:
        return 1

    if w in memo:
        return memo[w]

    result = 0
    for i in range(0, len(w)):
        t = w[0 : i + 1]
        if t in towels:
            result += find_towel_combos(w[i + 1 :], towels, memo, is_part_one)
            if is_part_one and result == 1:
                return 1

    memo[w] = result
    return result


def part1():
    # data = test_data
    data = lines

    towels = data[0].split(", ")
    desired = data[2:]  # Skip the first row and the empty string

    count = 0
    for d in desired:
        if find_towel_combos(d, towels, {}, True):
            count += 1
    print(count)
    return count


def part2():
    # data = test_data
    data = lines

    towels = data[0].split(", ")
    desired = data[2:]  # Skip the first row and the empty string

    count = 0
    for d in desired:
        count += find_towel_combos(d, towels, {}, False)
    print(count)

    return count


ans1 = part1()
ans2 = part2()

# uncomment these lines to submit
submit(ans1, part="a", day=19, year=2024)
submit(ans2, part="b", day=19, year=2024)
