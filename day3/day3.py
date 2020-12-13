lines = []
with open("/Users/pmaharjan/Documents/advent-of-code-2020/day3/input.txt") as file:
    for line in file:
        line = line.strip()
        lines.append(line)

part1_trees = 0
x = 0
y = 0
while y < len(lines):
    eachLine = lines[y]
    if eachLine[x] == "#":
        part1_trees += 1
    x = (x + 3) % 31
    y += 1

print("Part 1: {0}".format(part1_trees))


multiplied_trees = 1
slope_x_list = [1, 3, 5, 7, 1]
slope_y_list = [1, 1, 1, 1, 2]
for i in range(0, len(slope_y_list)):
    x = 0
    y = 0
    part2_tree = 0
    slope_x = slope_x_list[i]
    slope_y = slope_y_list[i]
    while y < len(lines):
        eachLine = lines[y]
        if eachLine[x] == "#":
            part2_tree += 1
        x = (x + slope_x) % 31
        y += slope_y
    multiplied_trees = multiplied_trees*part2_tree
print("Part 2: {0}".format(multiplied_trees))
