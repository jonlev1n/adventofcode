import os
from aocd import lines, submit, get_data


test_data = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_data():
    with open(os.path.join(__location__, "input.txt")) as input:
        data = input.read()
    return data


def solve_a(input):
    count = 0
    for line in input:
        r1 = line.split(",")[0].split("-")
        r2 = line.split(",")[1].split("-")
        r1 = list(map(lambda x: int(x), r1))
        r2 = list(map(lambda x: int(x), r2))
        if (r1[0] >= r2[0] and r1[1] <= r2[1]) or (r2[0] >= r1[0] and r2[1] <= r1[1]):
            count += 1

    return count


def solve_b(input):
    count = 0
    for line in input:
        r1 = line.split(",")[0].split("-")
        r2 = line.split(",")[1].split("-")
        r1 = list(map(lambda x: int(x), r1))
        r2 = list(map(lambda x: int(x), r2))
        r1 = list(range(r1[0], r1[1] + 1))
        r2 = list(range(r2[0], r2[1] + 1))

        for num in r1:
            if num in r2:
                count += 1
                break

    return count


test_data = ["2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8"]

# print(solve_a(test_data))
ans1 = solve_a(lines)
submit(ans1, day=4, year=2022, part="a")
# print(solve_b(test_data))
ans2 = solve_b(lines)
submit(ans2, day=4, year=2022, part="b")
