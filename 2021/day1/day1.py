import os, sys

sys.path.insert(0, os.path.abspath(".."))

from data import data


#  part 2
increased = 0
for idx, val in enumerate(data):
    cur = idx
    next = idx + 1
    if next >= len(data):
        break
    if data[next] > data[cur]:
        increased += 1

print(increased)

# part 2
# length of the sliding sum
sub_len = 3
summed_data = []
for idx, val in enumerate(data):
    # cant continue
    if idx > len(data) - sub_len:
        break
    # reset the running sum on incrememt
    s = 0
    for i in range(0, sub_len):
        s += data[idx + i]

    summed_data.append(s)

increased = 0
for idx, val in enumerate(summed_data):
    cur = idx
    next = idx + 1
    if next >= len(summed_data):
        break
    if summed_data[next] > summed_data[cur]:
        increased += 1

print(increased)
