from aocd import lines, submit, get_data


test_data = [
    "47|53",
    "97|13",
    "97|61",
    "97|47",
    "75|29",
    "61|13",
    "75|53",
    "29|13",
    "97|29",
    "53|29",
    "61|53",
    "97|53",
    "61|29",
    "47|13",
    "75|47",
    "97|75",
    "47|61",
    "75|61",
    "47|29",
    "75|13",
    "53|13",
    "",
    "75,47,61,53,29",
    "97,61,53,29,13",
    "75,29,13",
    "75,97,47,61,53",
    "61,13,29",
    "97,13,75,29,47",
]


def part1():
    # data = test_data
    data = lines
    rules = {}
    updates = []
    for row in data:
        if len(row) > 0:
            if "|" in row:
                k, v = row.split("|")
                if k in rules:
                    rules[k].append(v)
                else:
                    rules[k] = [v]

            else:
                p = row.split(",")
                updates.append([n for n in p])

    valid_updates = []
    for u in updates:
        valid = True
        for i in range(0, len(u)):
            sub = u[i:]
            n = sub.pop(0)
            for s in sub:
                values = rules[s] if s in rules else []
                if n in values:
                    valid = False
                    break
        if valid:
            valid_updates.append(u)

    ans1 = 0
    for v in valid_updates:
        # use // Floor Division
        m = len(v) // 2
        ans1 += int(v[m])

    # data = lines

    print(ans1)
    return ans1


def part2():
    # data = test_data
    data = lines
    rules = {}
    updates = []
    for row in data:
        if len(row) > 0:
            if "|" in row:
                k, v = row.split("|")
                if k in rules:
                    rules[k].append(v)
                else:
                    rules[k] = [v]

            else:
                p = row.split(",")
                updates.append([n for n in p])

    def check(update):
        for i, v in enumerate(update):
            for ii, vv in enumerate(update[i:]):
                values = rules[vv] if vv in rules else []
                if v in values:
                    return False
        return True

    def repair(update):
        repaired = update.copy()
        for i in range(len(repaired) - 1, -1, -1):
            for ii in range(i, -1, -1):
                values = rules[repaired[ii]] if repaired[ii] in rules else []
                if repaired[i] in values:
                    swap = repaired.pop(ii)
                    repaired.insert(i, swap)

        return repaired

    bad = []
    for u in updates:
        valid = True
        if not check(u):
            valid = False
            r = repair(u)

        if not valid:
            bad.append(int(r[len(r) // 2]))
    ans2 = sum(bad)
    print(ans2)
    return ans2


ans1 = part1()
ans2 = part2()

# uncomment these lines to submit
# submit(ans1, part="a", day=5, year=2024)
submit(ans2, part="b", day=5, year=2024)
