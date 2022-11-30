import copy
import time
import re
import math
file = open("/Users/jonathanlevin/git/adventofcode2020/day16/input.txt", "r")
# file = open("/Users/jonathanlevin/git/adventofcode2020/day16/test_input.txt", "r")
# file = open("/Users/jonathanlevin/git/adventofcode2020/day16/test_input2.txt", "r")

lines = file.readlines()

all_ranges = []
ranges = []
tickets = []
fields = []
reached_tickets = False
for line in lines:
    if line == "your ticket:\n":
        reached_tickets = True
    if not reached_tickets and line != "\n":
        numbers = re.findall('[0-9]+', line)
        numbers = map(int, numbers)
        numbers = [(numbers[0], numbers[1]), (numbers[2], numbers[3])]
        ranges.append(numbers)
        all_ranges += numbers
        field = line.split(':')[0]
        fields.append(field)

    elif reached_tickets and line != "\n":
        ticket = re.findall('[0-9]+', line)
        ticket = map(int, ticket)
        if(len(ticket) > 0):
            tickets.append(ticket)


def part1():
    error_rate = 0
    tix = []
    for ticket in tickets:
        ticket_valid = True
        for num in ticket:
                if not any(lower <= num <= upper for (lower, upper) in all_ranges):
                    error_rate += num
                    ticket_valid = False
        if ticket_valid:
            tix.append(ticket)
            
    # print(tix)

    return [error_rate, tix]

[p1, valid_tix] = part1()
# print(p1)

def part2():
    transposed = map(list, zip(*valid_tix))
    # print(valid_tix)
    # print(transposed)
    
    R = []

    c = 0
    for col in transposed:
        valid_ranges = list(range(0, len(ranges)))
        r = 0
        for rng in ranges:
            # print(valid_ranges)
            for num in col:
                if not any(lower <= num <= upper for (lower, upper) in rng):
                    valid_ranges.remove(r)
                    break
            
            r += 1
        # print(col)
        R.append(valid_ranges)
        c += 1
    print(R)

    while not all(len(rng) == 1 for rng in R):
        print("looping")
        single_vals = []

        for rng in R:
            if len(rng) == 1:
                single_vals.append(rng[0])


        for rng in R:
            if len(rng) > 1:
                for val in single_vals:
                    try:
                        rng.remove(val)
                    except:
                        pass
        
    # print(R)
    field_order= []
    for r in R:
        field_order.append(fields[r[0]])
    print(field_order)

    f_idx = 0
    m = 1
    for f in field_order:
        if 'departure' in f:
            m *= valid_tix[0][f_idx]
        f_idx += 1
    print(m)
                
part2()
