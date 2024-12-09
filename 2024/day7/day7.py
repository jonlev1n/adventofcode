from aocd import lines, submit, get_data


test_data = [
    "190: 10 19"
    "3267: 81 40 27"
    "83: 17 5"
    "156: 15 6"
    "7290: 6 8 6 15"
    "161011: 16 10 13"
    "192: 17 8 14"
    "21037: 9 7 18 13"
    "292: 11 6 16 20"
]


def do_test(res, partial_res, operands, concat):
    if len(operands) == 0:
        return res == partial_res
    if partial_res > res:
        return False

    count = 0
    count += do_test(res, partial_res + operands[0], operands[1:], concat)
    count += do_test(res, partial_res * operands[0], operands[1:], concat)
    if concat:
        count += do_test(
            res, int(str(partial_res) + str(operands[0])), operands[1:], concat
        )

    return count


def preprocess_data(data):
    equations = []
    for line in data:
        eq = line.replace(":", "").split()
        equations.append(list(map(int, eq)))
    return equations


def part1():
    # data = test_data
    data = lines
    equations = preprocess_data(data)

    ans1 = 0
    for eq in equations:
        test_val = eq[0]
        first_operand, other_operands = eq[1], eq[2:]
        possible_sol = do_test(test_val, first_operand, other_operands, concat=False)

        if possible_sol > 0:
            ans1 += test_val
    return ans1


def part2():
    # data = test_data
    data = lines
    equations = preprocess_data(data)

    ans2 = 0
    for eq in equations:
        test_val = eq[0]
        first_operand, other_operands = eq[1], eq[2:]
        possible_sol = do_test(test_val, first_operand, other_operands, concat=True)

        if possible_sol > 0:
            ans2 += test_val

    return ans2


ans1 = part1()
ans2 = part2()

# uncomment these lines to submit
submit(ans1, part="a", day=7, year=2024)
submit(ans2, part="b", day=7, year=2024)
