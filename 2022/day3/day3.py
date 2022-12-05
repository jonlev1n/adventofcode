import os
from aocd import lines, submit, get_data
import string


test_data = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_data():
    with open(os.path.join(__location__, "input.txt")) as input:
        data = input.read()
    return data


def get_priority(s):
    priority = 0
    for char in s:
        priority += string.ascii_letters.index(char) + 1
    return priority


def solve_a(input):

    common = ""
    for line in input:
        l = len(line)
        h = int(l / 2)
        first = line[0:h]
        second = line[h:]

        s = ""
        for char in first:
            if char in second and char not in s:
                s += char

        common += s

    priority = get_priority(common)

    return priority


def solve_b(input):
    common = ""
    for i in range(0, len(input), 3):
        s1 = input[i]
        s2 = input[i + 1]
        s3 = input[i + 2]

        s = ""
        for char in s1:
            if char in s2 and char in s3 and char not in s:
                s += char
        common += s
    priority = get_priority(common)
    print(priority)
    return priority


test_data = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]
ans1 = solve_a(lines)
submit(ans1, day=3, year=2022, part="a")
ans2 = solve_b(lines)
submit(ans2, day=3, year=2022, part="b")
