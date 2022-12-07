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
    def __init__(self, name, parent=None) -> None:
        self.name = name
        self.children = []
        self.size = None
        self.parent = parent

    def __str__(self):
        return "%s (dir, size = %s)" % (self.name, self.size)


def solve(input):
    dirs = []
    cur_dir = None
    sizes_to_sum = []
    total_disk = 70000000
    space_needed = 30000000
    dirs_to_delete = []
    for line in input:
        # dont need to do anything here
        if line == "$ ls":
            continue
        s = line.split()
        # handle directory changes
        if "$ cd" in line:
            dir_name = s[len(s) - 1]
            if dir_name == "..":
                cur_dir = cur_dir.parent
            else:
                # only create dirs when you cd into them
                d = _dir(name=dir_name, parent=cur_dir)
                if cur_dir is not None:
                    cur_dir.children.append(d)
                dirs.append(d)
                cur_dir = d
        # handle file creation
        elif "$" not in line and "dir" not in line:
            file_name = s[len(s) - 1]
            file_size = s[0]
            f = _file(size=file_size, name=file_name)
            cur_dir.children.append(f)

    # get directory sizes
    get_dir_sizes(dirs[0])  # seed with "/" - the recursion will take care of the rest
    for d in dirs:
        if d.name == "/":
            total_disk_used = d.size
            free_space = total_disk - total_disk_used
            min_delete_size = space_needed - free_space
        if d.size >= min_delete_size:
            dirs_to_delete.append(d.size)
        if d.size <= 100000:
            sizes_to_sum.append(d.size)

    return sum(sizes_to_sum), min(dirs_to_delete)


def get_dir_sizes(dir):
    # base case
    children = dir.children
    if all(c.size is not None for c in children):
        size = sum(c.size for c in dir.children)
        dir.size = size
    else:
        s = sum(c.size for c in children if c.size is not None)
        dirs = [c for c in children if c.size is None]
        for d in dirs:
            get_dir_sizes(d)
            s += d.size
        dir.size = s


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
# test_ans = solve(test_data)
# print(test_ans)
ans1 = solve(data)[0]
submit(ans1, day=7, year=2022, part="a")
ans2 = solve(data)[1]
submit(ans2, day=7, year=2022, part="b")
