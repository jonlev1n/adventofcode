from aocd import lines, submit, get_data
from collections import defaultdict
import networkx as nx
import itertools

test_data = [
    "kh-tc",
    "qp-kh",
    "de-cg",
    "ka-co",
    "yn-aq",
    "qp-ub",
    "cg-tb",
    "vc-aq",
    "tb-ka",
    "wh-tc",
    "yn-cg",
    "kh-ub",
    "ta-co",
    "de-co",
    "tc-td",
    "tb-wq",
    "wh-td",
    "ta-ka",
    "td-qp",
    "aq-cg",
    "wq-ub",
    "ub-vc",
    "de-ta",
    "wq-aq",
    "wq-vc",
    "wh-yn",
    "ka-de",
    "kh-ta",
    "co-tc",
    "wh-qp",
    "tb-vc",
    "td-yn",
]


G = nx.Graph()
data = lines
for row in data:
    G.add_edge(row[0:2], row[3:5])

combos = set()
max_clique = []
for clique in nx.find_cliques(G):
    if len(clique) > len(max_clique):
        max_clique = clique
    for combo in itertools.combinations(clique, 3):
        if len(list(filter(lambda x: x[0] == "t", combo))):
            combos.add(tuple(sorted(combo)))
ans1 = len(combos)
ans2 = ",".join(sorted(max_clique))


# uncomment these lines to submit
submit(ans1, part="a", day=23, year=2024)
submit(ans2, part="b", day=23, year=2024)
