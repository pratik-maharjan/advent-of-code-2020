lines = []
with open("input4.txt") as file:
    for line in file:
        line = line.strip()
        lines.append(line)
# print(lines)
# print(lines[0])
passports = []
x = 0
temp = ''
counter = 0
while x < len(lines):
    if lines[x] != '':
        temp = temp + ' ' + lines[x]
    else:
        temp = temp.lstrip()
        passports.append(temp)
        temp = ''
        counter += 1
    x += 1

# print(passports)
print(len(passports))


def valid(passport):
    diction = {}
    for fields in passport:
        diction = {fields}
        print(diction)


for p in passports:
    passport = p.split()
    print(passport)
    valid(passport)
