import os
from aocd import lines, submit, get_data
import re, copy


test_data = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_data():
    with open(os.path.join(__location__, "input.txt")) as input:
        data = input.read()
    return data


def solve_a(ics, instructions):
    for i in instructions:
        [num, src, dest] = re.findall(r"\d+", i)
        for i in range(0, int(num)):
            box = ics[src].pop(0)
            ics[dest].insert(0, box)

    s = "".join([stack[0] for stack in ics.values()])
    return s


def solve_b(ics, instructions):
    for i in instructions:
        [num, src, dest] = re.findall(r"\d+", i)
        boxes = ics[src][0 : int(num)]
        ics[src] = ics[src][int(num) :]
        ics[dest] = boxes + ics[dest]
    s = "".join([stack[0] for stack in ics.values()])
    return s


# test_ics = {"1": ["N", "Z"], "2": ["D", "C", "M"], "3": ["P"]}  # initial conditions
# test_instructions = [
#     "move 1 from 2 to 1",
#     "move 3 from 1 to 3",
#     "move 2 from 2 to 1",
#     "move 1 from 1 to 2",
# ]

ics = {
    "1": ["P", "Z", "M", "T", "R", "C", "N"],
    "2": ["Z", "B", "S", "T", "N", "D"],
    "3": ["G", "T", "C", "F", "R", "Q", "H", "M"],
    "4": ["Z", "R", "G"],
    "5": ["H", "R", "N", "Z"],
    "6": ["D", "L", "Z", "P", "W", "S", "H", "F"],
    "7": ["M", "G", "C", "R", "Z", "D", "W"],
    "8": ["Q", "Z", "W", "H", "L", "F", "J", "S"],
    "9": ["N", "W", "P", "Q", "S"],
}
instructions = [line for line in lines if "move" in line]

# print(solve_a(test_ics, test_instructions))
ans1 = solve_a(copy.deepcopy(ics), instructions)
submit(ans1, day=5, year=2022, part="a")

# print(solve_b(test_ics, test_instructions))
ans2 = solve_b(copy.deepcopy(ics), instructions)
submit(ans2, day=5, year=2022, part="b")
