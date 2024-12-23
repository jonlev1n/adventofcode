from aocd import lines, submit, get_data
from math import floor
from functools import reduce
from collections import defaultdict
from itertools import accumulate, pairwise


test_data = [
    "1",
    "10",
    "100",
    "2024",
]


def get_secret_num(n):
    a = n * 64
    b = a ^ n
    c = b % 16777216
    d = floor(c / 32)
    e = d ^ c
    f = e % 16777216
    g = f * 2048
    h = g ^ f
    return h % 16777216


def part1():
    # data = test_data
    data = lines

    nums = [int(x) for x in data]
    s = []

    for n in nums:
        for _ in range(0, 2000):
            n = get_secret_num(n)
        s.append(n)
    ans1 = sum(s)
    print(ans1)
    return ans1


def evolve(n):
    n = ((n << 6) ^ n) & 0xFFFFFF
    n = ((n >> 5) ^ n) & 0xFFFFFF
    n = ((n << 11) ^ n) & 0xFFFFFF
    return n


def part2():
    # data = test_data
    data = lines

    nums = [int(x) for x in data]
    bananas = defaultdict(int)
    for n in nums:
        steps = list(accumulate(range(2000), lambda acc, _: evolve(acc), initial=n))
        delta = [y % 10 - x % 10 for x, y in pairwise(steps)]
        seen = set()
        for i in range(len(steps) - 4):
            cur = tuple(delta[i : i + 4])
            if cur in seen:
                continue
            seen.add(cur)
            bananas[cur] += steps[i + 4] % 10
    return max(bananas.values())


ans1 = part1()
ans2 = part2()

# uncomment these lines to submit
submit(ans1, part="a", day=22, year=2024)
submit(ans2, part="b", day=22, year=2024)
