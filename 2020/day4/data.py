file = open("/Users/jon/git/adventofcode2020/day4/data.txt", "r")
lines = file.readlines()

idx = 0
data = []
d = {}
for line in lines:
    if line == "\n":
        print(d)
        data.append(d)
        d = {}
    else:
        parsedLine = line.split(" ")
        for elem in parsedLine:
            d[elem.split(":")[0]] = elem.split(":")[1].replace("\n", "")
    # print(d)
    # print(data)


# print(data)
