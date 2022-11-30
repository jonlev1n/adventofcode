import copy
import time
# import pyparsing
import re
import math

# file = open("/Users/jonathanlevin/git/adventofcode2020/day19/test_input.txt", "r")
file = open("/Users/jonathanlevin/git/adventofcode2020/day19/input.txt", "r")
# file = open("/Users/jonathanlevin/git/adventofcode2020/day19/test_input2.txt", "r")

lines = file.read().splitlines()

rules = {}
strings = []
reached_strings = False
for line in lines:
    if line == "":
        reached_strings = True
        pass
    elif not reached_strings:
        key = line.split(': ')[0]
        value = line.split(': ')[1]
        rules[key] = value
    else:
        strings.append(line)

def expand(num):
    while any(char.isdigit() for char in rules[num]):
        rule0 = rules[num].split(' ')
        for char in rule0:
            char = char.replace("(", "")
            char = char.replace(")", "")
            if char.isdigit():
                sub = rules[char]
                if len(rules[char].split(" ")) > 1:
                    sub = "(" + sub + ")"
                
                r = re.sub(r"\b{}\b".format(char), sub, rules[num])
                rules[num] = r


    rule = '('+rules[num].replace(' ', '')+')'
    print("expanded rule:")
    print(rule)
    regex = re.compile(rule)
    return (regex, rule)

# count = 0
# for s in strings:
#     match = regex.fullmatch(s)
#     if match is not None:
#         count += 1

def part1():
    count = 0
    regex, rule = expand('0')
    for s in strings:
        match = regex.fullmatch(s)
        if match is not None:
            count += 1
    print(count)

# part1()

def part2():
    regex42, r42 = expand('42')
    regex31, r31 = expand('31')    

    # rule 0 has to be updated:
    # r8 ends up being 42+ since it repeats over and over
    # r11 ends up being 42{i}31{i}
    # new_r31 = 
    
    total_count = 0
    for i in range(1, 5):
        new_r8 = r42 + '+'
        new_r11 = r42 + "{"+str(i)+"}" + r31 + "{"+str(i)+"}"
        new_r0 = new_r8 + new_r11

        count = 0
        regex = re.compile(new_r0)
        # print("regex: %s" % regex)
        for s in strings:
            match = regex.fullmatch(s)
            if match is not None:
                count += 1
        # print("count: %d" % count)
        total_count += count
    print("total count: %d" % total_count)



part2()
