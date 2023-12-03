from cgi import test
import os
import re
from aocd import lines, submit, get_data


test_data = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]


def part1():
    # data = test_data
    data = lines
    # get all nums in line
    count = 0
    for idx, l in enumerate(data):
        nums = re.findall(r"\d+", l)
        for n in nums:
            row = idx
            s_col = re.search(rf"\b{n}\b", l).span()[0]
            e_col = s_col + len(n) - 1
            # compute surrounding coords
            surround = []
            for i in range(row - 1, row + 2):  # inclusive range means +2
                if i < 0 or i > len(data) - 1:
                    continue
                for j in range(s_col - 1, e_col + 2):
                    if (
                        j < 0
                        or j > len(l) - 1
                        or (i == row and j in range(s_col, e_col + 1))
                    ):
                        continue
                    surround.append(data[i][j])
            if not all(e == "." for e in surround):
                count += int(n)
    return count


def part2():
    # data = test_data
    data = lines
    # preprocess to find possible gears
    pos_gears = {}
    for row, l in enumerate(data):
        for col, j in enumerate(l):
            if j == "*":
                pos_gears[(row, col)] = []

    # then basically part 1
    for idx, l in enumerate(data):
        nums = re.finditer(r"\d+", l)
        for n in nums:
            row = idx
            num = n.group()
            s_col = n.start()
            e_col = n.end() - 1
            # compute surrounding coords
            for i in range(row - 1, row + 2):  # inclusive range means +2
                if i < 0 or i > len(data) - 1:
                    continue
                for j in range(s_col - 1, e_col + 2):
                    if (
                        j < 0
                        or j > len(l) - 1
                        or (i == row and j in range(s_col, e_col + 1))
                    ):
                        continue
                    # except only for *
                    if data[i][j] == "*":
                        pos_gears[(i, j)].append(int(num))

    # then go back through
    ratio = 0
    for key in pos_gears.keys():
        if len(pos_gears[key]) == 2:
            x = pos_gears[key][0] * pos_gears[key][1]
            ratio += x
    return ratio


ans1 = part1()
ans2 = part2()

# submit(ans1, part="a", day=3, year=2023) #! CORRECT!
# submit(ans2, part="b", day=3, year=2023) #! CORRECT!
