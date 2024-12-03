from aocd import lines, submit, get_data
import re

test_data = ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]


def part1():
    # data = test_data[0]
    data = lines
    ans1 = 0
    for row in data:
        ms = re.findall(r"mul\(\d{1,3},\d{1,3}\)", row)
        for m in ms:
            ns = list(map(int, re.findall(r"\d{1,3}", m)))
            ans1 += ns[0] * ns[1]
    print(ans1)
    # data = lines

    return ans1


def part2():
    # data = test_data
    data = lines
    ans2 = 0
    superstring = ""
    for row in data:
        superstring += row

    superstring = data = "do()" + superstring + """don't()"""

    matches = re.findall(r"(?<=do\(\))((?:.|\n)*?)(?=don't\(\))", superstring)
    for i in matches:
        ms = re.findall(r"mul\(\d{1,3},\d{1,3}\)", i)
        for m in ms:
            ns = list(map(int, re.findall(r"\d{1,3}", m)))
            ans2 += ns[0] * ns[1]

    print(ans2)
    return ans2


ans1 = part1()
ans2 = part2()

# uncomment these lines to submit
# submit(ans1, part="a", day=3, year=2024)
submit(ans2, part="b", day=3, year=2024)
