import os
from aocd import lines, submit, get_data
import re, heapq


class Node:
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate

    def __lt__(self, other):
        return False

    def __repr__(self):
        return self.name


def find_paths(edges, goal):
    q = [(0, goal)]
    path_lengths = {goal: 0}
    while q:
        cost, current = heapq.heappop(q)
        for point, point_cost in edges[current].items():
            if point not in path_lengths or cost + point_cost < path_lengths[point]:
                path_lengths[point] = cost + point_cost
                heapq.heappush(q, (cost + point_cost, point))
    return path_lengths


def find_all_paths(edges, start_node):
    costs = {
        node: find_paths(edges, node)
        for node in edges
        if node is start_node or node.rate
    }
    for node, node_costs in costs.items():
        costs[node] = {x: c for x, c in node_costs.items() if x.rate}
    return costs


def parse_input(input):
    pat = re.compile(
        r"Valve (\S+) has flow rate=(\d+); tunnels? leads? to valves? (.+)"
    )
    nodes = {}
    edges = {}
    for line in input:
        match = pat.match(line)
        if match:
            name, rate, valves = match.groups()
            nodes[name] = Node(name, int(rate))
            edges[name] = valves.split(", ")

    for name, neighbours in list(edges.items()):
        del edges[name]
        edges[nodes[name]] = {nodes[neighbour]: 1 for neighbour in neighbours}

    start_node = nodes["AA"]
    return start_node, find_all_paths(edges, start_node)


def run_order(costs, start_node, nodes, t):
    release = 0
    current = start_node
    for node in nodes:
        cost = costs[current][node] + 1
        t -= cost
        assert t > 0
        release += t * node.rate
        current = node
    return release


def all_orders(distances, node, todo, done, time):
    for next_node in todo:
        cost = distances[node][next_node] + 1
        if cost < time:
            yield from all_orders(
                distances,
                next_node,
                todo - {next_node},
                done + [next_node],
                time - cost,
            )
    yield done


def solve(input):
    start_node, distances = parse_input(input)
    working_nodes = {node for node in distances if node.rate}

    p1_orders = all_orders(distances, start_node, working_nodes, [], 30)
    ans1 = max(run_order(distances, start_node, order, 30) for order in p1_orders)

    p2_orders = all_orders(distances, start_node, working_nodes, [], 26)
    p2_scores = [
        (run_order(distances, start_node, order, 26), set(order)) for order in p2_orders
    ]
    p2_scores.sort(key=lambda x: -x[0])

    best = 0
    for i, (sa, oa) in enumerate(p2_scores):
        if sa * 2 < best:
            break
        for sb, ob in p2_scores[i + 1 :]:
            if not oa & ob:
                score = sa + sb
                if score > best:
                    best = score
    ans2 = best
    return ans1, ans2


test_data = [
    "Valve AA has flow rate=0; tunnels lead to valves DD, II, BB",
    "Valve BB has flow rate=13; tunnels lead to valves CC, AA",
    "Valve CC has flow rate=2; tunnels lead to valves DD, BB",
    "Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE",
    "Valve EE has flow rate=3; tunnels lead to valves FF, DD",
    "Valve FF has flow rate=0; tunnels lead to valves EE, GG",
    "Valve GG has flow rate=0; tunnels lead to valves FF, HH",
    "Valve HH has flow rate=22; tunnel leads to valve GG",
    "Valve II has flow rate=0; tunnels lead to valves AA, JJ",
    "Valve JJ has flow rate=21; tunnel leads to valve II",
]

# print(solve(test_data))
ans1, ans2 = solve(lines)
submit(ans1, day=16, year=2022, part="a")
submit(ans2, day=16, year=2022, part="b")
