from aocd import lines, submit, get_data


test_data = [
    "x00: 1",
    "x01: 0",
    "x02: 1",
    "x03: 1",
    "x04: 0",
    "y00: 1",
    "y01: 1",
    "y02: 1",
    "y03: 1",
    "y04: 1",
    "",
    "ntg XOR fgs -> mjb",
    "y02 OR x01 -> tnw",
    "kwq OR kpj -> z05",
    "x00 OR x03 -> fst",
    "tgd XOR rvg -> z01",
    "vdt OR tnw -> bfw",
    "bfw AND frj -> z10",
    "ffh OR nrd -> bqk",
    "y00 AND y03 -> djm",
    "y03 OR y00 -> psh",
    "bqk OR frj -> z08",
    "tnw OR fst -> frj",
    "gnj AND tgd -> z11",
    "bfw XOR mjb -> z00",
    "x03 OR x00 -> vdt",
    "gnj AND wpb -> z02",
    "x04 AND y00 -> kjc",
    "djm OR pbm -> qhw",
    "nrd AND vdt -> hwm",
    "kjc AND fst -> rvg",
    "y04 OR y02 -> fgs",
    "y01 AND x02 -> pbm",
    "ntg OR kjc -> kwq",
    "psh XOR fgs -> tgd",
    "qhw XOR tgd -> z09",
    "pbm OR djm -> kpj",
    "x03 XOR y03 -> ffh",
    "x00 XOR y04 -> ntg",
    "bfw OR bqk -> z06",
    "nrd XOR fgs -> wpb",
    "frj XOR qhw -> z04",
    "bqk OR frj -> z07",
    "y03 OR x01 -> nrd",
    "hwm AND bqk -> z03",
    "tgd XOR rvg -> z12",
    "tnw OR pbm -> gnj",
]


def parse_data(data):
    m = {}
    Q = []
    for row in data:
        if not row == "":
            if ":" in row:
                key, value = row.split(": ")
                m[key] = int(value)
            else:
                key = row.split(" -> ")[1]
                k1, op, k2 = row.split(" -> ")[0].split(" ")
                Q.append((k1, op, k2, key))

    i = 0
    while len(Q):
        max_i = len(Q) - 1
        if i > max_i:
            i = 0

        (k1, op, k2, key) = Q[i]
        if k1 not in m or k2 not in m:
            pass
        else:
            Q.pop(i)
            if op == "AND":
                m[key] = m[k1] & m[k2]
            elif op == "OR":
                m[key] = m[k1] | m[k2]
            elif op == "XOR":
                m[key] = m[k1] ^ m[k2]
        i += 1

    return m


wires = {}
operations = []


def process(op, op1, op2):
    if op == "AND":
        return op1 & op2
    elif op == "OR":
        return op1 | op2
    elif op == "XOR":
        return op1 ^ op2


highest_z = "z00"
data = lines
for line in data:
    if ":" in line:
        wire, value = line.split(": ")
        wires[wire] = int(value)
    elif "->" in line:
        op1, op, op2, _, res = line.split(" ")
        operations.append((op1, op, op2, res))
        if res[0] == "z" and int(res[1:]) > int(highest_z[1:]):
            highest_z = res

wrong = set()
for op1, op, op2, res in operations:
    if res[0] == "z" and op != "XOR" and res != highest_z:
        wrong.add(res)
    if (
        op == "XOR"
        and res[0] not in ["x", "y", "z"]
        and op1[0] not in ["x", "y", "z"]
        and op2[0] not in ["x", "y", "z"]
    ):
        wrong.add(res)
    if op == "AND" and "x00" not in [op1, op2]:
        for subop1, subop, subop2, subres in operations:
            if (res == subop1 or res == subop2) and subop != "OR":
                wrong.add(res)
    if op == "XOR":
        for subop1, subop, subop2, subres in operations:
            if (res == subop1 or res == subop2) and subop == "OR":
                wrong.add(res)

while len(operations):
    op1, op, op2, res = operations.pop(0)
    if op1 in wires and op2 in wires:
        wires[res] = process(op, wires[op1], wires[op2])
    else:
        operations.append((op1, op, op2, res))

bits = [str(wires[wire]) for wire in sorted(wires, reverse=True) if wire[0] == "z"]
ans1 = int("".join(bits), 2)
ans2 = ",".join(sorted(wrong))


# uncomment these lines to submit
submit(ans1, part="a", day=24, year=2024)
submit(ans2, part="b", day=24, year=2024)
