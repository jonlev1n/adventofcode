# def get_magnitude(l):
#     has_sublist = False
#     for i, n in enumerate(l):
#         if isinstance(n, list):
#             has_sublist = True
#             break

#     if has_sublist:
#         l[i] = get_magnitude(n)
#         return get_magnitude(l)

#     if not has_sublist:
#         m = 3 * l[0] + 2 * l[1]
#         return m


# def create_list(a):
#     if len(a) > 1:
#         l = [a[0], a[1]]
#         del a[0:2]
#         a.insert(0, l)
#         return create_list(a)
#     else:
#         return a[0]


# def reduce_list(a, d=0):
#     for n in a:
#         if isinstance(n, list):


# # test
# t1 = get_magnitude([[1, 2], [[3, 4], 5]])
# print(t1)
# t2 = get_magnitude([[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]])
# print(t2)

# l1 = create_list([[1, 1], [2, 2], [3, 3], [4, 4]])

# # a1 = reduce_list("[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]")
# a1 = reduce_list([[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]])
# # print
from binarytree import Node
from functools import reduce
from itertools import combinations
import re
from timeit import default_timer as timer


def tree_to_snail(tree):
    if tree.is_leaf():
        return str(tree.value)
    return f"[{tree_to_snail(tree.left)},{tree_to_snail(tree.right)}]"


def to_node(t, depth=0):
    if isinstance(t, tuple):
        node = Node(-1, to_node(t[0], depth + 1), to_node(t[1], depth + 1))
    else:
        node = Node(t)
    node.depth = depth
    return node


def split_node(node):
    if node.is_leaf():
        if node.value >= 10:
            node.left = Node(node.value // 2)
            node.right = Node(node.value - node.left.value)
            node.value = -1
            node.left.depth = node.depth + 1
            node.right.depth = node.depth + 1
            return True
        return False
    rc = split_node(node.left)
    rc = rc or split_node(node.right)
    return rc


def magnitude(n):
    if not n:
        return 0
    if n.is_leaf():
        return n.value
    return 3 * magnitude(n.left) + 2 * magnitude(n.right)


def snail_to_tree(sn):
    return to_node(eval(sn.replace("[", "(").replace("]", ")")))


def snail_explode(sn):
    depth = 0
    parse_state = 0
    left_acc = 0
    right_acc = 0
    last_bracket = -1

    for i in range(len(sn)):
        c = sn[i]
        if c == "[":
            last_bracket = i
            depth += 1
            parse_state = 0
        elif c == "]":
            if depth > 4 and parse_state == 2:
                left = sn[:last_bracket]
                right = sn[i + 1 :]
                if left_acc:
                    left_nos = re.findall(r"\d+", left)
                    if left_nos:
                        left_val = left_nos[-1]
                        left_index = left.rfind(left_val)
                        left = (
                            left[:left_index]
                            + str(int(left_val) + left_acc)
                            + left[left_index + len(left_val) :]
                        )
                if right_acc:
                    right_nos = re.findall(r"\d+", right)
                    if right_nos:
                        right_val = right_nos[0]
                        right_index = right.find(right_val)
                        right = (
                            right[:right_index]
                            + str(int(right_val) + right_acc)
                            + right[right_index + len(right_val) :]
                        )
                return left + "0" + right
            depth -= 1
            parse_state = 0
        elif c.isnumeric():
            if parse_state == 0:
                left_acc = int(c)
                right_acc = 0
                parse_state = 1
            elif parse_state == 1:
                left_acc = left_acc * 10 + int(c)
            elif parse_state == 2:
                right_acc = right_acc * 10 + int(c)
        elif c == ",":
            if parse_state == 1:
                parse_state = 2
            else:
                parse_state = 0
    return sn


def snail_split(sn):
    tsn = snail_to_tree(sn)
    split_node(tsn)
    return tree_to_snail(tsn)


def snail_simplify(sn):
    while True:
        nsn = snail_explode(sn)
        if nsn == sn:
            nsn = snail_split(sn)
        if nsn == sn:
            break
        sn = nsn
    return sn


def snail_addition(sn1, sn2):
    return snail_simplify(f"[{sn1},{sn2}]")


def snail_magnitude(sn):
    return magnitude(snail_to_tree(sn))


Node.is_leaf = lambda x: x.value != -1

with open("/Users/jon/git/adventofcode2021/day18/day18.txt") as f:
    snails = [line.strip() for line in f]

start = timer()
answer = reduce(lambda x, y: snail_simplify(snail_addition(x, y)), snails)
print("Part 1:", snail_magnitude(answer))
end_part1 = timer()
print("Time part 1:", end_part1 - start)

pair_list = [x for x in combinations(snails, 2)] + [
    x for x in combinations(snails[::-1], 2)
]
mag_list = [snail_magnitude(snail_addition(x[0], x[1])) for x in pair_list]

print("Part 2:", max(mag_list))
print("Time part 2:", timer() - end_part1)
