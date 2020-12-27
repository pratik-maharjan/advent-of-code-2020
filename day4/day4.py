class Validator:
    def __init__(self, passport):
        self.passport = passport

    def check_field_count(self):
        return len(self.passport) == 8 or (len(self.passport) == 7 and 'cid' not in self.passport)

    def check_year(self, key, start, end):
        return len(self.passport[key]) == 4 and int(self.passport[key]) >= start and int(self.passport[key]) <= end

    def check_byr(self):
        return self.check_year('byr', 1920, 2002)

    def check_iyr(self):
        return self.check_year('iyr', 2010, 2020)

    def check_eyr(self):
        return self.check_year('eyr', 2020, 2030)

    def check_hcl(self):
        return self.passport['hcl'][0] == "#" and self.passport['hcl'][1:].isalnum()

    def check_ecl(self):
        return self.passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def check_pid(self):
        return len(self.passport['pid']) == 9

    def check_hgt(self):
        if self.passport['hgt'][-2:] == "cm":
            return int(self.passport['hgt'][:-2]) >= 150 and int(self.passport['hgt'][:-2]) <= 193
        elif self.passport['hgt'][-2:] == "in":
            return int(self.passport['hgt'][:-2]) >= 59 and int(self.passport['hgt'][:-2]) <= 76

    def is_valid(self):
        return (self.check_field_count() and self.check_byr() and self.check_iyr() and self.check_eyr()
            and self.check_hcl() and self.check_ecl() and self.check_pid() and self.check_hgt())


def get_passports(inp):
    passports = []
    passport = {}
    for line in inp:
        if line != "\n":
            line = line.rstrip().split(" ")
            line = [field.split(":") for field in line]
            for field in line:
                passport[field[0]] = field[1]
        else:
            passports.append(passport)
            passport = {}
    passports.append(passport)
    return passports


with open('input4.txt') as inp:
    passports = get_passports(inp)
    validators = [Validator(passport) for passport in passports]
    part_1_count = 0
    part_2_count = 0
    for validator in validators:
        if validator.check_field_count():
            part_1_count += 1
        if validator.is_valid():
            part_2_count += 1
    print("Part 1: {0}".format(part_1_count))
    print("Part 2: {0}".format(part_2_count))

# def parse(passport):
#     dictionary = {}
#     for fields in passport:
#         # print(fields.split(':')[0])
#         dictionary[fields.split(':')[0]] = fields.split(':')[1]
#         # print(fields.split(':')[1])
#     # print(dictionary)
#     return dictionary
#
# def validTwo(each):
#     val = 0
#     try:
#         if 'byr' in each and 'iyr' in each and 'eyr' in each and 'hgt' in each and 'hcl' in each and 'ecl' in each and 'pid' in each:
#             if (1920 <= int(each.get('bry')) <= 2002) and (2010 <= int(each.get('iyr')) <= 2020) and (2010 <= int(each.get('eyr')) <= 2020):
#                 if (each.get('hgt')[-2:] == 'cm' and 150 <= each.get('hgt')[:-2] <= 193) or (each.get('hgt')[-2:] == 'in' and 59 <= each.get('hgt')[:-2] <= 76):
#                     if (each.get('ecl') == 'amb') or (each.get('ecl') == 'blu') or (each.get('ecl') == 'brn') or (each.get('ecl') == 'gry') or (each.get('ecl') == 'grn') or (each.get('ecl') == 'hzl') or (each.get('ecl') == 'oth'):
#                         if len(each.get('pid')) == 9 and each.get('pid').isnumeric():
#                             if each.get('hcl')[:1] == '#':
#                                 for i in each.get('hcl')[1:]:
#                                     if i.isnumeric():
#                                         val = 1
#                                     else:
#                                         if i == 'a' or i == 'b' or i == 'c' or i == 'd' or i == 'e' or i == 'f':
#                                             val = 1
#     except:
#         val = val
#     return val
#
# def validOne(each):
#     val = 0
#     if 'byr' in each and 'iyr' in each and 'eyr' in each and 'hgt' in each and 'hcl' in each and 'ecl' in each and 'pid' in each:
#         val = 1
#     return val
#
# lines = []
# with open("input4.txt") as file:
#     for line in file:
#         line = line.strip()
#         lines.append(line)
# # print(lines)
# # print(lines[0])
# passports = []
# x = 0
# temp = ''
# counter = 0
# while x < len(lines):
#     if lines[x] != '':
#         temp = temp + ' ' + lines[x]
#     else:
#         temp = temp.lstrip()
#         passports.append(temp)
#         temp = ''
#         counter += 1
#     x += 1
# temp = temp.rstrip()
# passports.append(temp)
# # print(passports)
# # print(len(passports))
#
# eachPassport = {}
# totalOne = 0
# totalTwo = 0
# for p in passports:
#     passport = p.split()
#     eachPassport = parse(passport)
#     # print(eachPassport)
#     totalOne = totalOne + validOne(eachPassport)
#     totalTwo = totalTwo + validTwo(eachPassport)
#
# print("Part 1: {0}".format(totalOne))
# print("Part 2: {0}".format(totalTwo))
