import re

file = open("/Users/jonathanlevin/git/adventofcode2020/day7/rules.txt", "r")
# file = open("/Users/jonathanlevin/git/adventofcode2020/day7/test_rules.txt", "r")
# file = open("/Users/jonathanlevin/git/adventofcode2020/day7/test_rules2.txt", "r")
lines = file.readlines()

def strToNum(string):
    return int(string)
    

rules = []
for line in lines:
    line = line.replace ("\n", "")
    parent = re.search(r"\w+ \w+(?=\s+bags contain)", line).group(0)
    child_string = line.split("bags contain ", 1)[1]
    # children = child_string.split("bag")
    try:
        numbers = map(strToNum, re.findall(r"([0-9]+)", line))
        children = re.findall(r"(?<=\b[0-9]{1}\s)(\w+ \w+)", line)
    except:
        children = []
        numbers = None

    # print(children)
    # print(numbers)
    
    rules.append({"parent": parent, "children": children, "count": numbers})
    


    # print(parent)
    # print(child_string)
    # print(children)

# print(rules)


# want to find how many rules hold a shiny gold bag

# for every child that matches... add 1, then need to check parent of that - for each add one...
# search_string = "shiny gold"
# count = 0
# parents_to_check = []
# for rule in rules:
#     if search_string in rule["children"]:
#         print(rule)
#         parents_to_check.append(rule["parent"])

# print(parents_to_check)
count = 0
counted_rules = []
def count_rules(search_string):
    global count
    parents_to_check = []
    for rule in rules:
        if search_string in rule["children"] and rule not in counted_rules:
            count += 1
            parents_to_check.append(rule["parent"])
            counted_rules.append(rule)
    # total = count + current_count
    
    if len(parents_to_check) > 0:
        for parent in parents_to_check:
            print(parent)
            count_rules(parent)
    else:
        print(count)
        return count

# l = count_rules("shiny gold")


##### part 2
bag_dict = {}
for rule in rules:
    if rule['parent'] not in bag_dict.keys():
        bag_dict[rule['parent']] = [[rule["children"][i], rule['count'][i]] for i in range(0, len(rule['children']))]

print(bag_dict)
def part2(key, count):
    if len(bag_dict[key]) == 0:
        return 1
    for i in bag_dict[key]:
        count += (i[1] * part2(i[0], 0))
    return count+1

l = part2('shiny gold', 0) - 1
print(l)

