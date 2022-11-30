from input import input

for item1 in input:
    for item2 in input:
        for item3 in input:
            if item1 + item2 + item3 == 2020:
                print(item1)
                print(item2)
                print(item3)
                print(item1 * item2 * item3)
                break
