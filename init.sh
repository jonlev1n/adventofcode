# initialization script for advent of code to set up the puzzles for the year

# run this in your AoC directiory

## AOC
#   |- 2020
#   |- 2021
#   |- ...

# get the current year
if [ $# -eq 0 ]; then
	YEAR=$(date "+ %Y")
	YEAR=${YEAR// /}
else
	YEAR=$1
fi

if [ ! -d "$YEAR" ]; then
	mkdir $YEAR
else
	echo "This year is already set up!"
	exit 0
fi

cd "$YEAR"

for i in {1..25}; do
	mkdir "day$i"
	touch "day$i/__init__.py"
	touch "day$i/day$i.py"
	touch "day$i/input.txt"
	echo "
from aocd import lines, submit, get_data


test_data = []


def part1():
    data = test_data
    # data = lines

    ans1 = None
    return ans1


def part2():
    data = test_data
    # data = lines

    ans2 = None
    return ans2


ans1 = part1()
ans2 = part2()

# uncomment these lines to submit
# submit(ans1, part=\"a\", day=${i}, year=${YEAR})
# submit(ans2, part=\"b\", day=${i}, year=${YEAR})
" >>"day${i}/day${i}.py"
done
