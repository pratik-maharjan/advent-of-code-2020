lines = []
valid = 0
with open("/Users/pmaharjan/Documents/advent-of-code-2020/day2/input.txt") as file:
    for line in file:
        line = line.strip()
        lines.append(line)

for l in lines:  # 15-16 f: ffffffffffffffhf
    list = l.split()  # ["15-16", "f:", "ffffffffffffffhf"]
    i = 0
    while i < len(list):
        # print(list[i+1])
        bound = list[0].split("-")  # "15-16"
        # print(bound)
        lower = bound[0]  # 15
        upper = bound[1]  # 16
        # print("lower: {0} \nupper: {1}".format(lower,upper))
        letter = list[1][0]
        # print("letter: {0}".format(letter))
        pattern = list[2]
        # print("pattern: {0}".format(pattern))
        count = 0
        for x in pattern:
            if x == letter:
                count += 1
        # print(count)
        if int(lower) <= int(count) <= int(upper):
            valid += 1

        # print
        i += 3
# print("Part 1: {0}".format(valid))

part2 = 0
for l in lines:  # 15-16 f: ffffffffffffffhf
    list = l.split()  # ["15-16", "f:", "ffffffffffffffhf"]
    i = 0
    while i < len(list):
        # print(list[i+1])
        bound = list[0].split("-")  # "15-16"
        # print(bound)
        positionone = bound[0]  # 15
        positiontwo = bound[1]  # 16
        # print("position one: {0} \nposition two: {1}".format(lower,upper))
        letter = list[1][0]
        # print("letter: {0}".format(letter))
        pattern = list[2]
        # print("pattern: {0}".format(pattern))
        if ((pattern[int(positionone) - 1] == letter and pattern[int(positiontwo) - 1] != letter) or (
                pattern[int(positionone) - 1] != letter and pattern[int(positiontwo) - 1] == letter)):
            part2 += 1

        # print
        i += 3

print("Part 1: {0}".format(valid))
print("Part 2: {0}".format(part2))
