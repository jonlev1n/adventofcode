import copy
import time
import re
import math
file = open("/Users/jonathanlevin/git/adventofcode2020/day15/input.txt", "r")
# file = open("/Users/jonathanlevin/git/adventofcode2020/day15/test_input.txt", "r")
# file = open("/Users/jonathanlevin/git/adventofcode2020/day15/test_input2.txt", "r")

numbers = file.readlines()[0].split(",")
numbers = [int(num) for num in numbers]

def part1(breakpt):
    indices = {} 
    for i in range(0, len(numbers)):
        indices[numbers[i]] = i
    # print(indices)
    idx = len(numbers) 
    cur = 0
    print(indices)
    while True:
        if(idx == breakpt):
            break
       
        if cur not in indices:
            indices[cur] = idx
            cur = 0
        else:
            last_idx = indices[cur]
            # print("last_idx %d" % last_idx)
            indices[cur] = idx
            cur = idx - last_idx
           
        

        # print("%d: %d" % (idx, cur))
        idx += 1
       

    return(cur)
n = 30000000
# n = 2020

# p1 = part1(x)
# print(p1)
# 
p2 = part1(n - 1)
print(p2)
