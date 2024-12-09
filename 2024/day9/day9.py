import enum
from tabnanny import check
from aocd import lines, submit, get_data
import re
from itertools import groupby


test_data = ["2333133121414131402"]


def part1():
    # data = test_data[0]
    data = lines[0]

    s = []
    curId = 0
    for idx, c in enumerate(data):
        even = idx % 2 == 0
        num = int(c)
        for i in range(0, num):
            if even:
                s.append(str(curId))
            else:
                s.append(".")
        if not even:
            curId += 1

    pattern = r"^\d*\.*$"
    last_idx = -1
    while not re.fullmatch(pattern, "".join(s)):
        if s[last_idx] != ".":
            idx = s.index(".")
            s[idx] = s[last_idx]
            s[last_idx] = "."
        last_idx -= 1

    checksum = 0
    for idx, i in enumerate([c for c in s if c != "."]):
        checksum += idx * int(i)

    print(checksum)
    return checksum


def merge_empties(empty_intervals):
    i = 0
    while i < len(empty_intervals) - 1:
        if empty_intervals[i][1] == empty_intervals[i + 1][0]:
            to_replace = empty_intervals[i + 1]
            del empty_intervals[i + 1]
            empty_intervals[i] = (empty_intervals[i][0], to_replace[1])
        else:
            i += 1
    return empty_intervals


def part2():
    # data = test_data[0]
    data = lines[0]

    # store intervals of empties and files
    # if an empty interval can store a file, pop the interval, fragment it,
    # and put it back in the same place (if not delete it.).
    # calculate checksum for each interval.

    file_intervals = []
    empty_intervals = []

    is_file = True
    file_index = 0
    current_index = 0
    for num in data:
        if is_file:
            file_intervals.append((file_index, current_index, current_index + int(num)))
            file_index += 1
        else:
            empty_intervals.append((current_index, current_index + int(num)))
        is_file = not is_file
        current_index += int(num)

    disk_end = len(file_intervals) - 1
    while disk_end > 0:
        file_size = file_intervals[disk_end][2] - file_intervals[disk_end][1]
        empty_to_modify = -1
        for idx, e in enumerate(empty_intervals):
            if e[1] - e[0] >= file_size and e[0] < file_intervals[disk_end][1]:
                empty_to_modify = idx
                break

        if empty_to_modify != -1:
            interval = empty_intervals[empty_to_modify]
            if interval[1] - interval[0] == file_size:
                # remove interval
                del empty_intervals[empty_to_modify]
                empty_intervals.append(
                    (file_intervals[disk_end][1], file_intervals[disk_end][2])
                )
                file_intervals[disk_end] = (
                    file_intervals[disk_end][0],
                    interval[0],
                    interval[1],
                )
            else:
                empty_intervals[empty_to_modify] = (
                    interval[0] + file_size,
                    interval[1],
                )
                empty_intervals.append(
                    (file_intervals[disk_end][1], file_intervals[disk_end][2])
                )
                file_intervals[disk_end] = (
                    file_intervals[disk_end][0],
                    interval[0],
                    interval[0] + file_size,
                )

            empty_intervals = merge_empties(sorted(empty_intervals))

        # print(file_intervals[disk_end], empty_to_modify)
        disk_end -= 1

    checksum = 0
    for file_index, start, end in file_intervals:
        for i in range(start, end):
            checksum += file_index * i
    print(checksum)
    return checksum


# ans1 = part1()
ans2 = part2()

# uncomment these lines to submit
# submit(ans1, part="a", day=9, year=2024)
submit(ans2, part="b", day=9, year=2024)
