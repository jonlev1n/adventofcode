import os
from aocd import lines, submit, get_data


test_data = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_data():
    with open(os.path.join(__location__, "input.txt")) as input:
        data = input.read()
    return data


def solve_a(input):
    pass
    return


def solve_b(input):
    pass
    return


test_data = []
print(solve_a(test_data))
ans1 = solve_a(lines)
# submit(ans1, day=5, year=2022, part="a")
print(solve_b(test_data))
ans2 = solve_a(lines)
# submit(ans2, day=5, year=2022, part="b")
