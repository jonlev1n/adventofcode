import os
from aocd import lines, submit, get_data
import math

test_data = [
    "1=-0-2",
    "12111",
    "2=0=",
    "21",
    "2=01",
    "111",
    "20012",
    "112",
    "1=-1=",
    "1-12",
    "12",
    "1=",
    "122",
]

DIGITS_MAP = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
REVERSED = {2: "2", 1: "1", 0: "0", -1: "-", -2: "="}
DIGITS = DIGITS_MAP.values()
BASE = 5


def solve(input):
    s = 0
    for line in input:
        s += from_snafu(line)
    ans1 = to_snafu(s)
    return ans1


def from_snafu(num):
    l = len(num)
    v = 0
    for i, char in enumerate(num):
        v += DIGITS_MAP[char] * BASE ** (l - 1 - i)
    return v


def to_snafu(num):
    nums = []
    while True:
        remainder = num % BASE
        if remainder not in DIGITS:
            quotient = math.ceil(num / BASE)
            remainder -= BASE
        else:
            quotient = math.floor(num / BASE)
        nums.append(remainder)
        if num < BASE:
            break
        num = quotient
    nums.reverse()
    s = ""
    for n in nums:
        s += REVERSED[n]

    return s


# solve(test_data)
ans1 = solve(lines)
submit(ans1, day=25, year=2022, part="a")
