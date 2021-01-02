lines = []
with open("input5.txt") as file:
    for line in file:
        line = line.strip()
        lines.append(line)

# slice the string into rows and cols
# for rows, get row
# for cols, get col


def getRow(input, start, end):
    for i in input:
        if i == "F":
            end = int((start + end + 1) / 2) - 1
        else:
            start = int((start + end + 1) / 2)
    return start


def getCol(input, start, end):
    for i in input:
        if i == "L":
            end = int((start + end + 1) / 2) - 1
        else:
            start = int((start + end + 1) / 2)
    return start


highest = 0
seats = []
for l in lines:
    row = l[:7]
    col = l[7:]
    rowValue = getRow(row, 0, 127)
    colValue = getCol(col, 0, 7)
    seatId = (rowValue * 8) + colValue
    seats.append(seatId)
    if highest < int(seatId):
        highest = int(seatId)

print("Part 1: {0}".format(highest))


seats.sort()
mySeat = 0
for s in range(len(seats)-1):
    if seats[s+1] != seats[s]+1:
        mySeat = seats[s]+1
print("Part 2: {0}".format(mySeat))
