from aocd import lines

test_data = [
    "NNCB",
    "",
    "CH -> B",
    "HH -> N",
    "CB -> H",
    "NH -> C",
    "HB -> C",
    "HC -> B",
    "HN -> C",
    "NN -> C",
    "BH -> H",
    "NC -> B",
    "NB -> B",
    "BN -> B",
    "BB -> N",
    "BC -> B",
    "CC -> N",
    "CN -> C",
]

data = test_data
# data = lines

subs = dict()
for d in data:
    if len(d) > 0:
        if "->" in d:
            s, sub = d.split(" -> ")
            subs[s] = sub
        else:
            p = d


# part 1
# steps = 10
# part 2
steps = 40
# init map
count = dict()
p_map = dict()
for idx, s in enumerate(p):
    sub_str = ""
    if idx < len(p) - 1:
        sub_str = s + p[idx + 1]
    if len(sub_str):
        try:
            p_map[sub_str] += 1
        except:
            p_map[sub_str] = 1
    try:
        count[s] += 1
    except:
        count[s] = 1


for i in range(0, steps):
    keys = p_map.keys()
    new_p_map = dict()
    for k in keys:
        fk = k[0]
        lk = k[1]
        num_p = p_map[k]
        mk = subs[k]

        try:
            new_p_map[fk + mk] += num_p
        except:
            new_p_map[fk + mk] = num_p

        try:
            new_p_map[mk + lk] += num_p
        except:
            new_p_map[mk + lk] = num_p

        try:
            count[mk] += num_p
        except:
            count[mk] = 1
    p_map = new_p_map

ans = max(count.values()) - min(count.values())
print(ans)
