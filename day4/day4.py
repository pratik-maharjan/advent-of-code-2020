def parse(passport):
    dictionary = {}
    for fields in passport:
        # print(fields.split(':')[0])
        dictionary[fields.split(':')[0]] = fields.split(':')[1]
        # print(fields.split(':')[1])
    # print(dictionary)
    return dictionary


def valid(each):
    val = 0
    if 'byr' in each and 'iyr' in each and 'eyr' in each and 'hgt' in each and 'hcl' in each and 'ecl' in each and 'pid' in each:
        val = 1
    return val


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
temp = temp.rstrip()
passports.append(temp)
# print(passports)
# print(len(passports))

eachPassport = {}
total = 0
for p in passports:
    passport = p.split()
    eachPassport = parse(passport)
    # print(eachPassport)
    total = total + valid(eachPassport)

print("Part 1: {0}".format(total))
