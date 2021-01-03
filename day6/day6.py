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

# separate into groups
inter = []
temp2 = []
for l in lines:
    if l != '':
        temp2.append(l)
    else:
        inter.append(temp2)
        temp2 = []
inter.append(temp2)
# print(inter)

temp3 = []
temp4 = []
for i in inter:
    for j in i:
        temp3.append(set(j))
    temp4.append(temp3)
    temp3 = []

# print(temp4)
total = []
for i in temp4:
    intersection = set.intersection(*i)
    total.append(len(intersection))

print("Part 2: {0}".format(sum(total)))
