from aocd import lines
from aocd import submit

test_data = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "{([(<{}[<>[]}>{[]{[(<()>",
    "(((({<>}<{<{<>}{[]{[]{}",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
    "<{([{{}}[<[[[<>{}]]]>[]]",
]

# data = test_data
data = lines

open_chars = ["<", "(", "{", "["]
close_chars = [">", ")", "}", "]"]


def part1():
    # init to 0
    opens = []
    closes = []
    corrupted_lines = dict()
    point_values = {">": 25137, ")": 3, "}": 1197, "]": 57}
    corrupted_idxs = []
    for i in close_chars:
        corrupted_lines[i] = 0

    for i, l in enumerate(data):
        corrupted = False
        for s, c in enumerate(l):
            if c in open_chars:
                opens.append(c)

            if c in close_chars:
                # chech the last open
                last_open = opens.pop(len(opens) - 1)
                open_idx = open_chars.index(last_open)
                close_idx = close_chars.index(c)
                corrupted = open_idx != close_idx

            if corrupted:
                corrupted_lines[c] += 1
                corrupted_idxs.insert(0, i)
                break

    score = 0
    for i in close_chars:
        score += corrupted_lines[i] * point_values[i]

    # discard corrupted lines
    for i in corrupted_idxs:
        data.pop(i)
    return score


def part2():
    autoc = dict()
    point_values = {">": 4, ")": 1, "}": 3, "]": 2}
    for i, l in enumerate(data):
        opens = []
        for s, c in enumerate(l):
            if c in open_chars:
                opens.append(c)

            if c in close_chars:
                # closes.append(c)
                # pop both
                opens.pop(len(opens) - 1)

            # when you get to the end of the line, if opens = closes in len were good
            if s == len(l) - 1:
                lo = len(opens)
                if lo > 0:
                    opens.reverse()
                    line = ""
                    for i in opens:
                        idx = open_chars.index(i)
                        line += close_chars[idx]
                    autoc[line] = 0

    for k in autoc.keys():
        score = 0
        for i in k:
            score = score * 5 + point_values[i]

        autoc[k] = score

    sorted_scores = sorted(autoc.values())
    mid_score = sorted_scores[int((len(sorted_scores) - 1) / 2)]
    return mid_score


ans1 = part1()
print(ans1)
submit(ans1, part="a", day=10, year=2021)


ans2 = part2()
print(ans2)
submit(ans2, part="b", day=10, year=2021)
