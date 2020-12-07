lines = []
with open("/Users/pmaharjan/Desktop/advent of code/day3/input.txt") as file:
	for line in file:
		line = line.strip()
		lines.append(line)

counter = 1
count = 0
position = 0
trees = 0
for l in lines:
	if(counter > 11):
		counter = 0
		position = 0
	else:
		if(l[position] == '#'):
			trees += 1
			position = position + 3
		counter += 1

print(trees)
print(len(lines[0]))
