from aocd import lines, submit, get_data
import re


test_data = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
]


def part1():
    data = lines
    # data = test_data
    total_score = 0
    for line in data:
        _, trimmed = line.split(":")
        winning, mine = trimmed.split("|")
        winning_nums = re.findall(r"\d+", winning)
        my_nums = re.findall(r"\d+", mine)
        matches = 0
        for num in my_nums:
            if num in winning_nums:
                matches += 1

        if matches > 0:
            total_score += 2 ** (matches - 1)

    return total_score


def part2():
    data = lines
    # data = test_data
    cards = {}
    for i in range(0, len(data)):
        cards[i+1] = 1

    print(cards)

    for idx, line in enumerate(data):
        card = idx + 1
        _, trimmed = line.split(":")
        winning, mine = trimmed.split("|")
        winning_nums = re.findall(r"\d+", winning)
        my_nums = re.findall(r"\d+", mine)

        for c in range(0, cards[card]):
            matches = 0
            for num in my_nums:
                if num in winning_nums:
                    matches += 1

            for i in range(0, matches):
                cards[card + 1 + i] += 1

    total_cards = sum(cards.values())

    return total_cards


ans1 = part1()
ans2 = part2()

# submit(ans1, part="a", day=4, year=2023) # ! CORRECT!
submit(ans2, part="b", day=4, year=2023)
