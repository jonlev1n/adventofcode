import os
from aocd import lines, submit, get_data
import re


test_data = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_data():
    with open(os.path.join(__location__, "input.txt")) as input:
        data = input.read()
    return data


def solve_a(input):
    total = 0
    for line in input:
        total += len(line) - len(eval(line))

    return total


def solve_b(input):
    total = 0
    for line in input:
        total += 2 + line.count('"') + line.count("\\")

    return total


test_data = [r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"']
data = get_data(day=8, year=2015).splitlines()

# print(solve_a(test_data))
ans1 = solve_a(data)
submit(ans1, day=8, year=2015, part="a")
# print(solve_b(test_data))
ans2 = solve_b(data)
submit(ans2, day=8, year=2015, part="b")
