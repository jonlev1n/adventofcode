from aocd import lines, submit, get_data
import numpy as np

test_data = [
    "#.##..##.",
    "..#.##.#.",
    "##......#",
    "##......#",
    "..#.##.#.",
    "..##..##.",
    "#.#.##.#.",
    "",
    "#...##..#",
    "#....#..#",
    "..##..###",
    "#####.##.",
    "#####.##.",
    "..##..###",
    "#....#..#",
]


def part1():
    # data = test_data
    data = lines

    patterns = []
    pattern = []
    for row in data:
        if row == "":
            pattern = np.array(pattern)
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append([c for c in row])
    pattern = np.array(pattern)
    patterns.append(pattern)

    ans1 = 0
    for p in patterns:
        rows = []
        cols = []
        # first check rows
        for i in range(0, len(p) - 1):
            if (p[i] == p[i + 1]).all():
                rows.append(i)

        for r in rows:
            l = r
            u = r + 1

            while l in range(0, len(p)) and u in range(0, len(p)):
                if not (p[l] == p[u]).all():
                    break
                if l == 0 or u == len(p) - 1:
                    ans1 += 100 * (r + 1)
                l -= 1
                u += 1

        t = p.T
        for j in range(0, len(t) - 1):
            if (t[j] == t[j + 1]).all():
                cols.append(j)

        for c in cols:
            l = c
            u = c + 1

            while l in range(0, len(t)) and u in range(0, len(t)):
                if not (t[l] == t[u]).all():
                    break
                if l == 0 or u == len(t) - 1:
                    ans1 += c + 1
                l -= 1
                u += 1

    print(ans1)
    return ans1


def part2():
    # data = test_data
    data = lines

    patterns = []
    pattern = []
    for row in data:
        if row == "":
            pattern = np.array(pattern)
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append([c for c in row])
    pattern = np.array(pattern)
    patterns.append(pattern)

    rows = []
    cols = []
    # first check rows
    ans2 = 0
    for p in patterns:
        found = False
        print("new pattern!")
        for i in range(0, len(p) - 1):
            if (p[i] == p[i + 1]).all() or list(p[i] == p[i + 1]).count(False) == 1:
                rows.append(i)

        t = p.T
        for j in range(0, len(t) - 1):
            if (t[j] == t[j + 1]).all() or list(t[j] == t[j + 1]).count(False) == 1:
                cols.append(j)

        for r in rows:
            l = r
            u = r + 1
            if found:
                break

            d = 0
            while l in range(0, len(p)) and u in range(0, len(p)):
                diffs = list(p[l] == p[u]).count(False)
                d += diffs
                if diffs > 1 or d > 1:
                    break
                if (l == 0 or u == len(p) - 1) and d == 1:
                    ans2 += 100 * (r + 1)
                    print("found at row:", r)
                    found = True
                    break
                l -= 1
                u += 1

        for c in cols:
            l = c
            u = c + 1
            if found:
                break

            d = 0
            while l in range(0, len(t)) and u in range(0, len(t)):
                diffs = list(t[l] == t[u]).count(False)
                d += diffs
                if diffs > 1 or d > 1:
                    break
                if (l == 0 or u == len(t) - 1) and d == 1:
                    ans2 += c + 1
                    print("found at col:", c)
                    found = True
                    break
                l -= 1
                u += 1

    print(ans2)
    return ans2


ans1 = part1()
ans2 = part2()


# submit(ans1, part="a", day=13, year=2023)  #! correct!
submit(ans2, part="b", day=13, year=2023)
