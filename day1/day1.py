lines = []
part1val = 0
with open("input1.txt") as file:
    for line in file:
        line = line.strip()
        lines.append(line)

i = 0
while i < len(lines):
    j = 0
    while j < len(lines):
        if (int(lines[i]) + int(lines[j])) == 2020:
            part1val = int(lines[i]) * int(lines[j])
        j += 1
    i += 1

print("Part 1: {0}".format(part1val))

part2val = 0
i = 0
while i < len(lines):
    j = 0
    while j < len(lines):
        k = 0
        while k < len(lines):
            if (int(lines[i]) + int(lines[j]) + int(lines[k])) == 2020:
                part2val = int(lines[i]) * int(lines[j]) * int(lines[k])
            k += 1
        j += 1
    i += 1

print("Part 2: {0}".format(part2val))
