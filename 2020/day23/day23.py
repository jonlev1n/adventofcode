import copy
import time
import re
import math
import numpy as np

# file = open("/Users/jonathanlevin/git/adventofcode2020/day23/test_input.txt", "r")
file = open("/Users/jon/git/adventofcode2020/day23/input.txt", "r")
# file = open("/Users/jonathanlevin/git/adventofcode2020/day23/test_input2.txt", "r")

l = file.read()

cups_list = [int(d) for d in l]
cups_p2 = [max(cups_list) + 1 * i for i in range(1, 1000000 - max(cups_list) + 1)]
cups_list = cups_list + cups_p2


class Cup:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def printcup(self):
        print("data: %d" % self.data)
        print("next: %d" % self.next.data)


class SLinkedList:
    struct = {}

    def __init__(self):
        self.head = None

    # Print the linked list
    def listprint(self):
        head = self.head
        print(head.data)
        printval = head.next
        while printval is not head:
            print(printval.data)
            printval = printval.next


def shuffle():
    cups = SLinkedList()
    C = [Cup(c) for c in cups_list]
    Cup_Dict = {}
    for idx, cup in enumerate(C):
        if idx == 0:
            cups.head = cup

        if idx == len(C) - 1:
            cup.next = cups.head
        else:
            cup.next = C[idx + 1]
        Cup_Dict[str(cup.data)] = cup

    moves = 10000000
    v_max = max(cups_list)
    print(v_max)

    for i in range(0, moves):
        f = Cup_Dict[str(cups.head.next.data)]
        s = Cup_Dict[str(cups.head.next.next.data)]
        t = Cup_Dict[str(cups.head.next.next.next.data)]
        x = [cups.head.data, f.data, s.data, t.data]

        v = cups.head.data - 1 if cups.head.data > 1 else v_max
        while v in x:
            v -= 1
            if v < 1:
                v = v_max
            # break
        cups.head.next = cups.head.next.next.next.next
        cups.head = cups.head.next

        # cup = cups.head
        cup = Cup_Dict[str(v)]
        tmp = cup.next
        cup.next = f
        f.next = s
        s.next = t
        t.next = tmp

    return cups, Cup_Dict


def part1():
    cups, Cup_Dict = shuffle()
    cup = Cup_Dict["1"]
    ans = []
    while cup.next.data != 1:
        ans.append(cup.next.data)
        cup = cup.next
    ans = "".join(str(num) for num in ans)
    print("Part 1: %s" % ans)


def part2():
    start_time = time.time()
    cups, Cup_Dict = shuffle()
    cup = Cup_Dict["1"]
    ans = [cup.next.data, cup.next.next.data]
    print("============ %d ============" % (time.time() - start_time))
    print("Part 2: %d" % (ans[0] * ans[1]))


# part1()

part2()

