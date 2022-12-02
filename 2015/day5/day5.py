import os
from aocd import lines, submit, get_data


test_data = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_data():
    with open(os.path.join(__location__, "input.txt")) as input:
        data = input.read()
    return data


def check_double(string, idx):
    if idx == len(string) - 1:
        return False
    return string[idx] == string[idx + 1]


def check_bad_string(string, idx):
    bad_strings = ["ab", "cd", "pq", "xy"]
    if idx == len(string) - 1:
        return False
    return string[idx : idx + 2] in bad_strings


def check_nice(string):

    vowels = ["a", "e", "i", "o", "u"]
    vowel_min = 3

    vowel_count = 0
    double = False
    bad_string = False
    for idx, char in enumerate(string):
        if char in vowels:
            vowel_count += 1
        if not double:
            double = check_double(string, idx)
        if not bad_string:
            bad_string = check_bad_string(string, idx)
            if bad_string:
                break
    nice = vowel_count >= vowel_min and double and not bad_string
    return nice


def check_sandwich(string, idx):
    if idx >= len(string) - 2:
        return False
    return string[idx] == string[idx + 2]


def check_nice_part_2(string):
    sandwich = False
    paired = False
    pairs = {}
    for idx, char in enumerate(string):
        if idx == len(string) - 1:
            break
        if not sandwich:
            sandwich = check_sandwich(string, idx)
        substr = string[idx : idx + 2]
        try:
            pairs[substr].append(idx)
        except:
            pairs[substr] = [idx]

    # check pairs
    for key in pairs.keys():
        indexes = pairs[key]
        if len(indexes) > 1:
            if len(indexes) == 2 and abs(indexes[0] - indexes[1]) == 1:
                paired = False
            else:
                paired = True
                break

    return sandwich and paired


def solve_a(input):
    nice_strings = 0
    for line in input:
        nice = check_nice(line)
        if nice:
            nice_strings += 1
    return nice_strings


def solve_b(input):
    nice_strings = 0
    for line in input:
        nice = check_nice_part_2(line)
        if nice:
            nice_strings += 1
    return nice_strings


data = get_data(day=5, year=2015)
lines = data.splitlines()
ans1 = solve_a(lines)
submit(ans1, day=5, year=2015, part="a")
ans2 = solve_b(lines)
submit(ans2, day=5, year=2015, part="b")
