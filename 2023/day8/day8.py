from aocd import lines, submit, get_data
import numpy as np


# test_data = [
#     "RL",
#     "",
#     "AAA = (BBB, CCC)",
#     "BBB = (DDD, EEE)",
#     "CCC = (ZZZ, GGG)",
#     "DDD = (DDD, DDD)",
#     "EEE = (EEE, EEE)",
#     "GGG = (GGG, GGG)",
#     "ZZZ = (ZZZ, ZZZ)",
# ]

test_data = [
    "LLR",
    "",
    "AAA = (BBB, BBB)",
    "BBB = (AAA, ZZZ)",
    "ZZZ = (ZZZ, ZZZ)",
]

test_data_2 = [
    "LR",
    "",
    "11A = (11B, XXX)",
    "11B = (XXX, 11Z)",
    "11Z = (11B, XXX)",
    "22A = (22B, XXX)",
    "22B = (22C, 22C)",
    "22C = (22Z, 22Z)",
    "22Z = (22B, 22B)",
    "XXX = (XXX, XXX)",
]


def part1():
    # data = test_data
    data = lines
    instructions = data[0]
    nodes = {}
    for i in range(2, len(data)):
        node, t = data[i].split(" = ")
        l, r = t.replace("(", "").replace(")", "").split(", ")
        nodes[node] = {"L": l, "R": r}

    current_node = "AAA"
    steps = 0
    while current_node != "ZZZ":
        for i in instructions:
            steps += 1
            next_node = nodes[current_node][i]
            current_node = next_node

    print(steps)

    return steps


def part2():
    # data = test_data_2
    data = lines

    instructions = data[0]
    nodes = {}
    start_nodes = []
    for i in range(2, len(data)):
        node, t = data[i].split(" = ")
        l, r = t.replace("(", "").replace(")", "").split(", ")
        nodes[node] = {"L": l, "R": r}
        if node[-1] == "A":
            start_nodes.append(node)

    all_steps = []
    for current_node in start_nodes:
        steps = 0
        while current_node[-1] != "Z":
            for i in instructions:
                steps += 1
                next_node = nodes[current_node][i]
                current_node = next_node
        all_steps.append(steps)
    lcm = np.lcm.reduce(np.array(all_steps))
    print(lcm)
    return lcm


ans1 = part1()
ans2 = part2()

# submit(ans1, part="a", day=8, year=2023) #! correct!
submit(ans2, part="b", day=8, year=2023)
