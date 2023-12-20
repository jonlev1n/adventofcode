from aocd import lines, submit, get_data
import collections
import math


test_data = [
    "broadcaster -> a, b, c",
    "%a -> b",
    "%b -> c",
    "%c -> inv",
    "&inv -> a",
]


def parsed(data):
    m = {}

    for line in data:
        a, b = line.split(" -> ")
        b = b.split(", ")

        if a == "broadcaster":
            t = None
        else:
            t = a[0]
            a = a[1:]

        m[a] = (t, b)

    return m


def part1():
    # data = test_data
    data = lines

    data = parsed(data)

    num_low = 0
    num_high = 0
    memory = {}

    input_map = collections.defaultdict(list)

    for node, (_, dests) in data.items():
        for d in dests:
            input_map[d].append(node)

    for node, (t, _) in data.items():
        if t is None:
            continue
        if t == "%":
            memory[node] = False
        if t == "&":
            memory[node] = {d: False for d in input_map[node]}

    for _ in range(1000):
        todo = [(None, "broadcaster", False)]

        while todo:
            new_todo = []

            for src, node, is_high_pulse in todo:
                if is_high_pulse:
                    num_high += 1
                else:
                    num_low += 1

                info = data.get(node)
                if info is None:
                    continue

                t, dests = info
                if t == "%":
                    if is_high_pulse:
                        continue
                    state = memory[node]
                    memory[node] = not state
                    for d in dests:
                        new_todo.append((node, d, not state))
                    continue
                if t == "&":
                    state = memory[node]
                    state[src] = is_high_pulse

                    if sum(state.values()) == len(state):
                        # All are high, send a low pulse
                        to_send = False
                    else:
                        to_send = True

                    for d in dests:
                        new_todo.append((node, d, to_send))
                    continue
                if t is None:
                    for d in dests:
                        new_todo.append((node, d, is_high_pulse))
                    continue

            todo = new_todo

    ans1 = num_low * num_high
    print(ans1)
    return ans1


def part2():
    # data = test_data
    data = lines
    data = parsed(data)

    num_low = 0
    num_high = 0
    memory = {}

    input_map = collections.defaultdict(list)

    for node, (_, dests) in data.items():
        for d in dests:
            input_map[d].append(node)

    for node, (t, _) in data.items():
        if t is None:
            continue
        if t == "%":
            memory[node] = False
        if t == "&":
            memory[node] = {d: False for d in input_map[node]}
    single = input_map["rx"][0]
    sources = input_map[single]

    low_counts = {}
    rx_count = 0
    cycle = 0

    while len(low_counts) < len(sources):
        cycle += 1
        todo = [(None, "broadcaster", False)]

        while todo:
            new_todo = []

            for src, node, is_high_pulse in todo:
                if node in sources:
                    if not is_high_pulse:
                        if node not in low_counts:
                            low_counts[node] = cycle
                if node == "rx" and not is_high_pulse:
                    rx_count += 1

                if is_high_pulse:
                    num_high += 1
                else:
                    num_low += 1

                info = data.get(node)
                if info is None:
                    continue

                t, dests = info
                if t == "%":
                    if is_high_pulse:
                        continue
                    state = memory[node]
                    memory[node] = not state
                    for d in dests:
                        new_todo.append((node, d, not state))
                    continue
                if t == "&":
                    state = memory[node]
                    state[src] = is_high_pulse

                    if sum(state.values()) == len(state):
                        # All are high, send a low pulse
                        to_send = False
                    else:
                        to_send = True

                    for d in dests:
                        new_todo.append((node, d, to_send))
                    continue
                if t is None:
                    for d in dests:
                        new_todo.append((node, d, is_high_pulse))
                    continue

            todo = new_todo

    ans2 = math.lcm(*low_counts.values())
    print(ans2)
    return ans2


ans1 = part1()
ans2 = part2()

# uncomment these lines to submit
# submit(ans1, part="a", day=20, year=2023)  #! correct!
submit(ans2, part="b", day=20, year=2023)
