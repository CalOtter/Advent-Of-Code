with open("input.txt", "r") as file:
    lines = file.readlines()
def solve_1(lines):
    sum = 0
    for line in lines:
        first = -1
        last = 0
        for char in line:
            try:
                char = int(char)
                if first == -1:
                    first = char
                last = char
            except:
                pass
        sum += int(str(first) + str(last))
    return sum
def solve_2(lines):
    sum = 0
    pairs = {
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9
    }
    for line in lines:
        first = -1
        last = 0
        i = 0
        seen = ""
        while i < len(line):
            if line[i].isdigit():
                if first == -1:
                    first = line[i]
                last = line[i]
            else:
                seen += line[i]
                for s in pairs.keys():
                    if s in seen:
                        if first == -1:
                            first = pairs[s]
                        last = pairs[s]
                        seen = line[i]
            i += 1
        sum += int(str(first) + str(last))
    return sum