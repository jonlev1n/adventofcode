import copy
import time
import re
import math
import numpy as np

# file = open("/Users/jonathanlevin/git/adventofcode2020/day21/test_input.txt", "r")
file = open("/Users/jonathanlevin/git/adventofcode2020/day21/input.txt", "r")
# file = open("/Users/jonathanlevin/git/adventofcode2020/day21/test_input2.txt", "r")

lines = file.read().splitlines()


possible_allergens = {}
full_list = []
for line in lines:
    line = line.replace(")", "").replace(",", "")
    # print(line.split(" (contains "))
    allergens = line.split(" (contains ")[1].split(" ")
    ingredients = line.split(" (contains ")[0].split(" ")
    keys = [word for word in allergens]
    full_list = full_list + ingredients
    for k in keys:
        try:
            v = possible_allergens[k]
            v.append(ingredients)
            possible_allergens[k] = v
        except:
            vals = []
            vals.append(ingredients)
            possible_allergens[k] = vals


allergens = {}
while len(allergens) < len(possible_allergens):
    for k in possible_allergens:
        v = possible_allergens[k]
        e = list(set.intersection(*map(set, v)))
        t = allergens.values()
        for i in t:
            try:
                e.remove(i)
            except:
                pass
        if len(e) == 1:
            allergens[k] = e[0]

count = 0
for item in full_list:
    if item not in allergens.values():
        count += 1
print("Part 1: %d" % count)

keys = [key for key in allergens]
sorted_keys = sorted(keys)
cdl = ""
for k in sorted_keys:
    cdl = cdl + allergens[k] + ","
# trim last comma
cdl = cdl[0:len(cdl) - 1]
print("Part 2: %s" % cdl)
