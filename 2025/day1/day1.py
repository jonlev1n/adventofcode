from aocd import lines, submit, get_data


test_data = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82",
]


def part1():
    # data = test_data
    start_num = 50
    data = lines

    cur = start_num
    pw = 0
    for line in data:
        d = line[0]
        num = int(line[1:])
        if d == "L":
            cur = (cur - num) % 100
        if d == "R":
            cur = (cur + num) % 100
        if cur == 0:
            pw += 1

    print(pw)

    ans1 = pw
    return ans1


def part2():
    # data = test_data
    data = lines

    pw = 0
    y = 50
    res = 0
    for line in data:
        n = int(line[1:])
        x = -1 * n if line[0] == "L" else n
        assert 0 <= y < 100
        w, y_ = divmod(y + x, 100)
        res += (
            # number of passes through 0
            abs(w)
            # account for false pass when starting from 0 and going L
            - (y == 0 and x < 0)
            # account for missing pass (w == 0) when reaching 0
            + (y_ == 0 and x < 0)
        )
        y = y_
    print(res)
    return res


ans1 = part1()
ans2 = part2()

# uncomment these lines to submit
# submit(ans1, part="a", day=1, year=2025)
submit(ans2, part="b", day=1, year=2025)
