with open("input.txt", "r") as file:
    lines = [list("." + line.strip() + ".") for line in file.readlines()]
    lines.insert(0, ["." for _ in range(len(lines[0]))])
    lines.append(["." for _ in range(len(lines[0]))])

def part_1(lines):
    nums = []
    for r, line in enumerate(lines):
        seen = ""
        isPartNumber = False
        for c, char in enumerate(line):
            if char.isdigit():
                seen += char
                neighbors = lines[r-1][c-1:c+2] + lines[r+1][c-1:c+2]
                neighbors.append(lines[r][c-1])
                neighbors.append(lines[r][c+1])
                if any([not (x.isdigit() or x == ".") for x in neighbors]):
                    isPartNumber = True
            elif isPartNumber:
                nums.append(int(seen))
                seen = ""
                isPartNumber = False
            else:
                seen = ""
    return sum(nums)

def part_2(lines):
    nums = [[] for _ in range(len(lines))]
    sum = 0
    for r, line in enumerate(lines):
        seen = ""
        seen_c1 = -1
        isPartNumber = False
        for c, char in enumerate(line):
            if char.isdigit():
                seen += char
                if seen_c1 == -1:
                    seen_c1 = c
                neighbors = lines[r-1][c-1:c+2] + lines[r+1][c-1:c+2]
                neighbors.append(lines[r][c-1])
                neighbors.append(lines[r][c+1])
                if any([not (x.isdigit() or x == ".") for x in neighbors]):
                    isPartNumber = True
            elif isPartNumber:
                seen_c2 = c-1
                nums[r].append([int(seen), seen_c1, seen_c2])
                seen_c1 = -1
                seen = ""
                isPartNumber = False
            else:
                seen = ""
                seen_c1 = -1
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char == "*":
                adjacent = []
                if len(nums[r-1]) > 0:
                    for partNumber in nums[r-1]:
                        if partNumber[1]-1 <= c <= partNumber[2]+1:
                            adjacent.append(partNumber[0])
                if len(nums[r]) > 0:
                    for partNumber in nums[r]:
                        if partNumber[2] == c-1 or partNumber[1] == c+1:
                            adjacent.append(partNumber[0])
                if len(nums[r+1]) > 0:
                    for partNumber in nums[r+1]:
                        if partNumber[1]-1 <= c <= partNumber[2]+1:
                            adjacent.append(partNumber[0])
                if len(adjacent) == 2:
                    sum += adjacent[0] * adjacent[1]
    return sum
print(part_1(lines))
print(part_2(lines))