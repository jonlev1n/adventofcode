import os
from aocd import lines, submit, get_data
import re


test_data = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet",
]

test_data_2 = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]


def part1():
    # data = test_data
    data = lines
    nums = []
    for row in data:
        for char in row:
            first_num = char if char.isnumeric() else False
            if first_num:
                break
        for char in reversed(row):
            last_num = char if char.isnumeric() else False
            if last_num:
                break
        nums.append(int(first_num + last_num))
    ans = sum(nums)
    submit(ans, part="a", day=1, year=2023)


def part2():
    num_map = dict(
        one=1, two=2, three=3, four=4, five=5, six=6, seven=7, eight=8, nine=9
    )
    regex = (
        r"(?=("
        + "|".join([str(num) for num in num_map.values()])
        + "|"
        + "|".join(num_map.keys())
        + "))"
    )

    def to_number(x):
        try:
            v = int(x)
        except ValueError:
            v = num_map[x]
        return str(v)

    # data = test_data_2
    data = lines

    ans = 0
    for row in data:
        n = re.findall(regex, row)
        ans += int(to_number(n[0]) + to_number(n[-1]))

    print(ans)
    # print(nums)
    submit(ans, part="b", day=1, year=2023)


# part1()
part2()
