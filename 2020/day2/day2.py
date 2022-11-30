from data import output

compliantPasswords = 0
newCompliantPasswords = 0
for item in output:
    # password is compliant if
    # the designated letter is in the password MORE than rangeMin
    # AND LESS than rangeMax
    letterCount = item["password"].count(item["letter"])
    if letterCount >= item["rangeMin"] and letterCount <= item["rangeMax"]:
        compliantPasswords += 1

    if (
        item["password"][item["firstIndex"]] == item["letter"]
        and item["password"][item["secondIndex"]] != item["letter"]
    ) or (
        item["password"][item["firstIndex"]] != item["letter"]
        and item["password"][item["secondIndex"]] == item["letter"]
    ):
        newCompliantPasswords += 1
print(compliantPasswords)
print(newCompliantPasswords)
