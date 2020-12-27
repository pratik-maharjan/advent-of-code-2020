def parse(passport):
    dictionary = {}
    for fields in passport:
        # print(fields.split(':')[0])
        dictionary[fields.split(':')[0]] = fields.split(':')[1]
        # print(fields.split(':')[1])
    # print(dictionary)
    return dictionary

def validTwo(each):
    val = 0
    try:
        if 'byr' in each and 'iyr' in each and 'eyr' in each and 'hgt' in each and 'hcl' in each and 'ecl' in each and 'pid' in each:
            if (1920 <= int(each.get('bry')) <= 2002) and (2010 <= int(each.get('iyr')) <= 2020) and (2010 <= int(each.get('eyr')) <= 2020):
                if (each.get('hgt')[-2:] == 'cm' and 150 <= each.get('hgt')[:-2] <= 193) or (each.get('hgt')[-2:] == 'in' and 59 <= each.get('hgt')[:-2] <= 76):
                    if (each.get('ecl') == 'amb') or (each.get('ecl') == 'blu') or (each.get('ecl') == 'brn') or (each.get('ecl') == 'gry') or (each.get('ecl') == 'grn') or (each.get('ecl') == 'hzl') or (each.get('ecl') == 'oth'):
                        if len(each.get('pid')) == 9 and each.get('pid').isnumeric():
                            if each.get('hcl')[:1] == '#':
                                for i in each.get('hcl')[1:]:
                                    if i.isnumeric():
                                        val = 1
                                    else:
                                        if i == 'a' or i == 'b' or i == 'c' or i == 'd' or i == 'e' or i == 'f':
                                            val = 1
    except:
        val = val
    return val

def validOne(each):
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
totalOne = 0
totalTwo = 0
for p in passports:
    passport = p.split()
    eachPassport = parse(passport)
    # print(eachPassport)
    totalOne = totalOne + validOne(eachPassport)
    totalTwo = totalTwo + validTwo(eachPassport)

print("Part 1: {0}".format(totalOne))
print("Part 2: {0}".format(totalTwo))
