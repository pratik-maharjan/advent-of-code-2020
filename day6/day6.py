lines = []
with open("input6.txt") as file:
    for line in file:
        line = line.strip()
        lines.append(line)
# print(lines)

# separate into groups
groups = []
temp = ''
for l in lines:
    if l != '':
        temp = temp + l
    else:
        groups.append(temp)
        temp = ''
groups.append(temp)
# print(groups)

# get the unique set from each group
unique = []
for g in groups:
    unique.append(len(set(g)))
# print(unique)

print("Part 1: {0}".format(sum(unique)))
