from operator import indexOf
from aocd import lines, submit, get_data


test_data = [
    "7 6 4 2 1",
    "1 2 7 8 9",
    "9 7 6 2 1",
    "1 3 2 4 5",
    "8 6 4 4 1",
    "1 3 6 7 9",
]


def part1():
    # data = test_data
    data = lines
    safe = 0
    for row in data:
        levels = list(map(int, row.split(" ")))
        diffs = []
        for i in range(0, (len(levels) - 1)):
            d = levels[i] - levels[i + 1]
            diffs.append(d)
        if all(x < 0 and x > -4 for x in diffs):
            safe += 1
        if all(x < 4 and x > 0 for x in diffs):
            safe += 1

    ans1 = safe
    return ans1


def part2():
    # data = test_data
    data = lines
    safe = 0
    for row in data:
        levels = list(map(int, row.split(" ")))
        diffs = []
        for i in range(0, (len(levels) - 1)):
            d = levels[i] - levels[i + 1]
            diffs.append(d)
        if all(x < 0 and x > -4 for x in diffs):
            safe += 1
        elif all(x < 4 and x > 0 for x in diffs):
            safe += 1
        else:
            # not safe, try removing a numbera
            for j in range(0, len(levels)):
                new_levels = [x for x in levels]
                new_levels.pop(j)
                new_diffs = []
                for i in range(0, (len(new_levels) - 1)):
                    d = new_levels[i] - new_levels[i + 1]
                    new_diffs.append(d)
                if all(x < 0 and x > -4 for x in new_diffs):
                    safe += 1
                    break
                elif all(x < 4 and x > 0 for x in new_diffs):
                    safe += 1
                    break

    ans2 = safe
    return ans2


# ans1 = part1()
ans2 = part2()

# uncomment these lines to submit
# submit(ans1, part="a", day=2, year=2024)
submit(ans2, part="b", day=2, year=2024)
