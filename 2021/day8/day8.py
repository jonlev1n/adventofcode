from aocd import lines

# data = lines
# test_data= [
#     # "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf",
#     "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
#     "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
#     "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
#     "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
#     "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
#     "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
#     "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
#     "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
#     "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
#     "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
# ]
# data = test_data

data = lines
outputs = [l.split("|")[1] for l in data]
# part 1

# 1 4 8 7
count = sum(1 for o in outputs for s in o.split() if len(s) in [2,3,4,7])

print(count)

# part 2

total = 0
for d in data:
    puzzle, code = d.split("|")
    words = puzzle.split()
    one = [x for x in words if len(x) == 2][0]
    four = [x for x in words if len(x) == 4][0]
    seven = [x for x in words if len(x) == 3][0]
    eight = [x for x in words if len(x) == 7][0]

    six_seg = [x for x in words if len(x) == 6]
    five_seg = [x for x in words if len(x) == 5]

    for word in six_seg:
        if not all(l in word for l in seven):
            six = word

    six_seg.remove(six)
    
    for word in six_seg:
        if not all(l in word for l in four):
            zero = word
        else:
            nine = word

    for word in five_seg:
        if all(l in word for l in one):
            three = word

    five_seg.remove(three)

    for word in five_seg:
        if all(l in six for l in word):
            five = word
        else:
            two = word

    nums = {zero:"0", one: "1", two:"2", three: "3", four:"4", five:"5", six:"6", seven:"7", eight:"8", nine: "9"}

    keys = list(nums.keys())
    translated = int(''.join([nums[num] for word in code.split() for num in keys if sorted(word) == sorted(num)]))


    # sum_num = int(''.join([nums[x] for x in translated]))
    total += translated
print(total)


