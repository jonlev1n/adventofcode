from aocd import lines, submit, get_data
import networkx as nx
import functools as ft


test_data = [
    "jqt: rhn xhk nvd",
    "rsh: frs pzl lsr",
    "xhk: hfx",
    "cmg: qnr nvd lhk bvb",
    "rhn: xhk bvb hfx",
    "bvb: xhk hfx",
    "pzl: lsr hfx nvd",
    "qnr: nvd",
    "ntq: jqt hfx bvb xhk",
    "nvd: lhk",
    "lsr: lhk",
    "rzs: qnr cmg lsr rsh",
    "frs: qnr lhk lsr",
]


def part1():
    # data = test_data
    data = lines

    g = nx.Graph()

    for row in data:
        k, vs = row.split(": ")[0], row.split(": ")[1].split()

        for v in vs:
            g.add_edge(k, v)

    sever = nx.minimum_edge_cut(g)

    for k, v in sever:
        g.remove_edge(k, v)

    els = list(map(len, nx.connected_components(g)))
    ans1 = ft.reduce(lambda x, y: x * y, els, 1)
    print(ans1)
    return ans1


def part2():
    data = test_data
    # data = lines

    ans2 = None
    return ans2


ans1 = part1()
ans2 = part2()

# uncomment these lines to submit
submit(ans1, part="a", day=25, year=2023)
# submit(ans2, part="b", day=25, year=2023)
