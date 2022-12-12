import os
from aocd import lines, submit, get_data
import string, numpy as np, networkx as nx

test_data = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_data():
    with open(os.path.join(__location__, "input.txt")) as input:
        data = input.read()
    return data


def solve(input):

    G = nx.DiGraph()
    H = np.array([[*x.strip()] for x in input])

    S = tuple(*np.argwhere(H == "S"))
    H[S] = "a"
    E = tuple(*np.argwhere(H == "E"))
    H[E] = "z"

    N = nx.grid_2d_graph(*H.shape).to_directed()

    for a, b in N.edges():
        if ord(H[b]) <= ord(H[a]) + 1:
            G.add_edge(a, b)

    p = nx.shortest_path_length(G, target=E)
    return (p[S], min(p[a] for a in p if H[a] == "a"))


test_data = [
    "Sabqponm",
    "abcryxxl",
    "accszExk",
    "acctuvwj",
    "abdefghi",
]

(ans1, ans2) = solve(lines)
submit(ans1, day=12, year=2022, part="a")
submit(ans2, day=12, year=2022, part="b")
