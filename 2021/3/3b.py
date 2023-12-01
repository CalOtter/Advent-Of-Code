# does not work

zeros, ones, co2, oxygen, co2lines, oxygenlines, mostcommon, leastcommon = 0,0, "", "", [], [], {}, {}

with open("3.txt", "r") as file:
    lines = file.read().splitlines()
    oxygenlines = lines.copy()
    co2lines = lines.copy()

    for index in range(12):
        for line in oxygenlines:
            zeros += 1 if line[index] == "0" else 0
            ones += 1 if line[index] == "1" else 0
            mostcommon[index] = 1 if ones >= zeros else 0
            leastcommon[index] = 0 if ones >= zeros else 1
            zeros, ones = 0,0
        for line in oxygenlines:
            if int(line[index]) != mostcommon[index]:
                oxygenlines.remove(line)
    for index in range(12):
        for line in co2lines:
            zeros += 1 if line[index] == "0" else 0
            ones += 1 if line[index] == "1" else 0
            mostcommon[index] = 1 if ones >= zeros else 0
            leastcommon[index] = 0 if ones >= zeros else 1
            zeros, ones = 0, 0
        for line in co2lines:
            if int(line[index]) != leastcommon[index]:
                 co2lines.remove(line)
mostcommonvalue = ""
for value in mostcommon.values():
    mostcommonvalue += str(value)
leastcommonvalue = ""
for value in leastcommon.values():
    leastcommonvalue += str(value)
print(int(mostcommonvalue, 2), int(leastcommonvalue, 2))
print(oxygenlines, mostcommon.values())
print(co2lines, leastcommon.values())
