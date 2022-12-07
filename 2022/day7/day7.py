import os
from aocd import lines, submit, get_data


test_data = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_data():
    with open(os.path.join(__location__, "input.txt")) as input:
        data = input.read()
    return data


class _file:
    def __init__(self, size, name) -> None:
        self.size = int(size)
        self.name = name

    def __str__(self):
        return "%s (file, size = %d)" % (self.name, self.size)


class _dir:
    def __init__(self, name) -> None:
        self.name = name
        self.children = []
        self.size = None

    def __str__(self):
        return "%s (dir, size = %s)" % (self.name, self.size)


def solve_a(input):
    dirs = []
    cur_dir = None
    sizes_to_sum = []
    for line in input:
        if line == "$ cd .." or line == "$ ls":
            continue
        s = line.split()
        if "$ cd" in line:
            dir_name = s[len(s) - 1]
            d = next((x for x in dirs if x.name == dir_name), None)
            if not d:
                d = _dir(name=dir_name)
                dirs.append(d)
            cur_dir = d
        elif "$" not in line:
            if "dir" in line:
                dir_name = s[len(s) - 1]
                if not any(d.name == dir_name for d in dirs):
                    d = _dir(name=dir_name)
                    dirs.append(d)
                    cur_dir.children.append(d)
            else:
                file_name = s[len(s) - 1]
                file_size = s[0]
                f = _file(size=file_size, name=file_name)
                cur_dir.children.append(f)

    for d in dirs:
        d.size = get_size(d)
        if d.size <= 100000:
            sizes_to_sum.append(d.size)
        print(d)

    return sum(sizes_to_sum)


def get_size(dir):
    # base case
    children = dir.children
    if all(c.size is not None for c in children):
        size = sum(c.size for c in dir.children)
        return size

    else:
        s = sum(c.size for c in children if c.size is not None)
        dirs = [c for c in children if c.size is None]
        for d in dirs:
            s += get_size(d)
        return s


data = lines
test_data = [
    "$ cd /",
    "$ ls",
    "dir a",
    "14848514 b.txt",
    "8504156 c.dat",
    "dir d",
    "$ cd a",
    "$ ls",
    "dir e",
    "29116 f",
    "2557 g",
    "62596 h.lst",
    "$ cd e",
    "$ ls",
    "584 i",
    "$ cd ..",
    "$ cd ..",
    "$ cd d",
    "$ ls",
    "4060174 j",
    "8033020 d.log",
    "5626152 d.ext",
    "7214296 k",
]
test_ans = solve_a(test_data)
# print(test_ans)
# ans1 = solve_a(data)
# submit(ans1, day=7, year=2022, part="a")
