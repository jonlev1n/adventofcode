from aocd import lines, submit, get_data


test_data = [
    "???.### 1,1,3",
    ".??..??...?##. 1,1,3",
    "?#?#?#?#?#?#?#? 1,3,1,6",
    "????.#...#... 4,1,1",
    "????.######..#####. 1,6,5",
    "?###???????? 3,2,1",
]

DP = {}


def f(dots, blocks, i, bi, current):
    key = (i, bi, current)
    if key in DP:
        return DP[key]
    if i == len(dots):
        if bi == len(blocks) and current == 0:
            return 1
        elif bi == len(blocks) - 1 and blocks[bi] == current:
            return 1
        else:
            return 0
    ans = 0
    for c in [".", "#"]:
        if dots[i] == c or dots[i] == "?":
            if c == "." and current == 0:
                ans += f(dots, blocks, i + 1, bi, 0)
            elif (
                c == "." and current > 0 and bi < len(blocks) and blocks[bi] == current
            ):
                ans += f(dots, blocks, i + 1, bi + 1, 0)
            elif c == "#":
                ans += f(dots, blocks, i + 1, bi, current + 1)
    DP[key] = ans
    return ans


def part1():
    # data = test_data
    data = lines

    ans1 = 0
    G = [[c for c in row] for row in data]
    for line in data:
        dots, blocks = line.split()
        blocks = [int(x) for x in blocks.split(",")]
        DP.clear()
        score = f(dots, blocks, 0, 0, 0)
        ans1 += score
    print(ans1)
    return ans1


def part2():
    # data = test_data
    data = lines

    ans2 = 0
    G = [[c for c in row] for row in data]
    for line in data:
        dots, blocks = line.split()
        dots = "?".join([dots, dots, dots, dots, dots])
        blocks = ",".join([blocks, blocks, blocks, blocks, blocks])
        blocks = [int(x) for x in blocks.split(",")]
        DP.clear()
        score = f(dots, blocks, 0, 0, 0)
        ans2 += score
    return ans2


ans1 = part1()
ans2 = part2()


# submit(ans1, part="a", day=12, year=2023) #! correct!
# submit(ans2, part="b", day=12, year=2023) #! correct!
