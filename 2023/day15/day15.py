import os
from aocd import lines, submit, get_data


test_data = ["rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"]


def getHASH(step):
    value = 0
    for c in step:
        askee = ord(c)
        value += askee
        value *= 17
        value %= 256
    return value


def part1():
    # data = test_data
    data = lines
    seq = data[0].split(",")
    ans1 = 0
    for step in seq:
        value = getHASH(step)
        ans1 += value

    print(ans1)
    return ans1


def part2():
    # data = test_data
    data = lines
    hashmap = {}
    # preprocess
    for i in range(0, 256):
        hashmap[i] = {}

        # {label: (focal, index), label2: (focal2, index2)...}

    seq = data[0].split(",")
    for step in seq:
        op = "=" if "=" in step else "-"
        [label, fl] = step.split("=") if op == "=" else [step[0 : len(step) - 1], None]
        box = getHASH(label)

        if op == "=":
            hashmap[box][label] = fl
        elif op == "-":
            if label in hashmap[box].keys():
                del hashmap[box][label]

        # then sum the power
    ans2 = 0
    for i in hashmap.keys():
        box = hashmap[i]
        box_idx = i + 1
        for idx, j in enumerate(box.keys()):
            p_idx = idx + 1
            s = box_idx * p_idx * int(box[j])
            ans2 += s

    print(ans2)
    return ans2


ans1 = part1()
ans2 = part2()

# submit(ans1, part="a", day=15, year=2023) #! correct!
submit(ans2, part="b", day=15, year=2023)
