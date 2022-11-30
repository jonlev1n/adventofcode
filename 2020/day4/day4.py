from data import data
import re

count = 0

for item in data:
    # print(item)
    # validate the key/value pairs
    # byr must be 1920 - 2002

    # count if all fields are present
    if len(item.keys()) == 8:
        if (
            int(item["byr"]) >= 1920
            and int(item["byr"]) <= 2002
            and int(item["iyr"]) >= 2010
            and int(item["iyr"]) <= 2020
            and int(item["eyr"]) >= 2020
            and int(item["eyr"]) <= 2030
            and (
                re.search(r"^(1[5-8][0-9]|19[0-3])cm$", item["hgt"])
                or re.search(r"^(59|6[0-9]|7[0-6])in$", item["hgt"])
            )
            and re.search(r"^#[0-9a-z]{6}$", item["hcl"])
            and item["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            and re.search(r"^[0-9]{9}$", item["pid"])
        ):
            # print(item)
            count += 1
        else:
            print(item)

    # only count if less 7 and contains cid key
    if len(item.keys()) == 7:
        if "cid" not in item.keys():
            if (
                int(item["byr"]) >= 1920
                and int(item["byr"]) <= 2002
                and int(item["iyr"]) >= 2010
                and int(item["iyr"]) <= 2020
                and int(item["eyr"]) >= 2020
                and int(item["eyr"]) <= 2030
                and (
                    re.search(r"^(1[5-8][0-9]|19[0-3])cm$", item["hgt"])
                    or re.search(r"^(59|6[0-9]|7[0-6])in$", item["hgt"])
                )
                and re.search(r"^#[0-9a-z]{6}$", item["hcl"])
                and item["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                and re.search(r"^[0-9]{9}$", item["pid"])
            ):
                count += 1
            else:
                print(item)

print(count)

