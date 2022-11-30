import copy
import time
import pyparsing, re
import math

file = open("/Users/jonathanlevin/git/adventofcode2020/day18/test_input.txt", "r")
# file = open("/Users/jon/git/adventofcode2020/day18/input.txt", "r")

lines = file.read().splitlines()
# print(lines)
# for line in lines:
#     print(line)
# print(lines[0])

c = pyparsing.Word(pyparsing.alphanums) | "+" | "*"
parens = pyparsing.nestedExpr("(", ")", content=c)


def traverse_list(l, initial_value, initial_operator):
    sub_value = 0
    operator = "+"
    for idx, item in enumerate(l):
        if isinstance(item, list):
            prev_value = sub_value
            # print("prev_value: %d" % prev_value)
            if idx == 0:
                prev_operator = "+"
            else:
                prev_operator = l[idx - 1]
            sub_value = traverse_list(item, prev_value, prev_operator)

        else:
            try:
                num = int(item)
                if operator == "+":
                    sub_value += num
                elif operator == "*":
                    sub_value *= num
            except:
                operator = item
            print("sub array val: %d" % sub_value)

    if initial_operator == "+":
        sub_value += initial_value
    elif initial_operator == "*":
        sub_value *= initial_value
    
    return sub_value


flat_map = []
def traverse_list2(l, initial_value, initial_operator):
    sub_value = 0
    operator = "+"
    for idx, item in enumerate(l):
        if isinstance(item, list):
            prev_value = sub_value
            # print("prev_value: %d" % prev_value)
            if idx == 0:
                prev_operator = "+"
            else:
                prev_operator = l[idx - 1]
            # print("array: %s" % item)
            print("zzz")
            sub_value = traverse_list2(item, 0, prev_operator)
            print(sub_value)
            print("s")

        else:
            try:
                num = int(item)
                if operator == "+":
                    sub_value += num
                elif operator == "*":
                    sub_value *= num
            except:
                operator = item
            print("sub array val: %d" % sub_value)

    # print("initial_value: %d" % initial_value)
    if initial_operator == "+":
        sub_value += initial_value
    elif initial_operator == "*":
        sub_value *= initial_value
    
    flat_map.append(initial_value)
    flat_map.append(initial_operator)

    # print("sub_value: %d" % sub_value)
    return sub_value


def part1():
    ans = 0
    for l in lines:
        line = "(" + l + ")"
        l = parens.parseString(line).asList()[0]
        print(l)
        ans += traverse_list(l, 0, "+")
    # print(ans)
    print("xxx")


# part1()


def part2():
    # z = traverse_list(parens.parseString("(" + lines[4] + ")").asList(), 0, '+')
    
    z = lines[5].split(" ")
    zz = ''.join(char for char in z)
    print(zz)
    for idx, char in enumerate(zz):
        if char == '+':
           string = zz[0:idx - 1] + '(' + zz[idx] + ')' + zz[(idx +1):]
    print(string)


    # easier to change the input than algorithm
    line = "(" + lines[4] + ")"
    l = parens.parseString(line).asList()[0]
    # x = re.findall(r"(\d+ \+ \d+)", line)
    # print(x)


part2()
