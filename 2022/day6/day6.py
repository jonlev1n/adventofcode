import os
from aocd import lines, submit, get_data


test_data = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_data():
    with open(os.path.join(__location__, "input.txt")) as input:
        data = input.read()
    return data


def solve(input, packet_length):
    for i in range(0, len(input)):
        if i >= len(input) - packet_length:
            break
        substr = input[i : i + packet_length]
        unique = list(set(substr))
        if len(unique) == packet_length:
            return i + packet_length


data = get_data(day=6, year=2022)
# test_data = [
#     "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
#     "bvwbjplbgvbhsrlpgdmjqwftvncz",
#     "nppdvjthqldpwncqszvftbrmjlhg",
#     "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
#     "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
# ]

# for t in test_data:
#     print(solve_a(t, 14))


ans1 = solve(data, 4)
submit(ans1, day=6, year=2022, part="a")

ans2 = solve(data, 14)
submit(ans2, day=6, year=2022, part="b")
