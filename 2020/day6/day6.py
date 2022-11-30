file = open("/Users/jonathanlevin/git/adventofcode2020/day6/data.txt", "r")
lines = file.readlines()

answers = []
groupAnswers = []
for line in lines:
    if line == "\n":
        # print(groupAnswers)
        answers.append(groupAnswers)
        groupAnswers = []
    else:
        for char in line:
            # print(char)
            if char != "\n":
                groupAnswers.append(char.replace("\n", ""))

# print(answers)

newAnswers = []
for array in answers:
    newArray = []
    for elem in array:
        if(elem not in newArray):
            newArray.append(elem)
    newAnswers.append(newArray)

# print(newAnswers)

tSum = 0
for arr in newAnswers:
    tSum += len(arr)

print(tSum)

# pt 2

newAnswers = []

groupAnswers = []

for line in lines:
    groupAnswers = []
    if line == "\n":
        newAnswers.append([])
    else:
        for char in line:
            if char != "\n":
                groupAnswers.append(char.replace("\n", ""))
        newAnswers.append(groupAnswers)
# answers = []
# groupAnswers = []
# groupNum = 1
# for line in lines:
#     groupAnswers = []
#     if line == "\n":
#         # print(groupAnswers)
#         # answers.append({groupNum: groupAnswers})
#         groupNum += 1
#     else:
#         for char in line:
#             if char != "\n":
#                 groupAnswers.append(char.replace("\n", ""))

#         answers.append({groupNum: groupAnswers})

numInGroups = []
count = 0
for line in newAnswers:
    if len(line) != 0:
        count += 1
    else:
        numInGroups.append(count)
        count = 0

print(numInGroups)


# to have everyone answer a question a given element must be there numInGroups[idx] times
commonAnswers = []
for i in range(0, len(answers)):
    minCount = numInGroups[i]
    commonElements = []
    for elem in answers[i]:
        if answers[i].count(elem) == minCount and elem not in commonElements:
            commonElements.append(elem)

    commonAnswers.append(commonElements)

print(commonAnswers)

nSum = 0
for arr in commonAnswers:
    nSum += len(arr)
print(nSum)