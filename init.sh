# initialization script for advent of code to set up the puzzles for the year

# run this in your AoC directiory

## AOC
#   |- 2020
#   |- 2021
#   |- ...

# get the current year
YEAR=$(date "+ %Y")
YEAR=${YEAR// /}
if [ ! -d "$YEAR" ]
then 
	mkdir $YEAR
else 
	echo "This year is already set up!"
	exit 0
fi

cd "$YEAR"

for i in {1..25}
do
 	mkdir "day$i"
	touch "day$i/__init__.py"
	touch "day$i/day$i.py"
	touch "day$i/input.txt"
	echo "import os
# from aocd import lines, submit

test_data = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def read_data():
	with open(os.path.join(__location__, 'input.txt')) as input:
		data = input.read()
	return data" >> "day$i/day$i.py" 
done    	
	
