from aocd import lines, submit, get_data


test_data = [
    "0 3 6 9 12 15",
    "1 3 6 10 15 21",
    "10 13 16 21 30 45",
]


def part1():
    # data = [[int(n) for n in l.split(" ")] for l in test_data]
    data = [[int(n) for n in l.split(" ")] for l in lines]

    def getSum(sequences):
        if all([s == 0 for s in sequences[-1]]):  # base case
            total = sum([s[-1] for s in sequences])
            return total
        else:  # compute new sequence and recur
            next_sequence = [
                sequences[-1][i + 1] - sequences[-1][i]
                for i in range(0, len(sequences[-1]) - 1)
            ]
            sequences.append(next_sequence)
            return getSum(sequences)

    sum_totals = 0
    for d in data:
        sum_totals += getSum([d])

    print(sum_totals)
    return sum_totals


def part2():
    # data = [[int(n) for n in l.split(" ")] for l in test_data]
    data = [[int(n) for n in l.split(" ")] for l in lines]

    def getSum(sequences):
        if all([s == 0 for s in sequences[-1]]):  # base case
            c = (
                "".join(
                    [
                        "(" + str(sequences[s][0]) + "-"
                        for s in range(0, len(sequences) - 1)
                    ]
                )
                + "0"
                + "".join([")" for s in range(0, len(sequences) - 1)])
            )
            total = eval(c)
            return total
        else:  # compute new sequence and recur
            next_sequence = [
                sequences[-1][i + 1] - sequences[-1][i]
                for i in range(0, len(sequences[-1]) - 1)
            ]
            sequences.append(next_sequence)
            return getSum(sequences)

    sum_totals = 0
    for d in data:
        sum_totals += getSum([d])

    print(sum_totals)
    return sum_totals


ans1 = part1()
ans2 = part2()

# submit(ans1, part="a", day=9, year=2023) #! correct!
# submit(ans2, part="b", day=9, year=2023) #! correct!
