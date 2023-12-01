with open("11.txt") as file:
    has_flashed = {}
    flashes = 0
    lines = file.readlines()
    for index, line in enumerate(lines):
        lines[index] = list(map(int, line.strip()))

    for line in lines:
        line.insert(0, -9999)
        line.append(-9999)
    lines.insert(0, [-9999 for i in range(12)])
    lines.append([-9999 for i in range(12)])
    for y, line in enumerate(lines):
        for index, int in enumerate(line):
            has_flashed[index, y] = False
    for day in range(400):
        sync = True
        for line in lines:
            for index, int in enumerate(line):
                line[index] += 1
        nine = True
        while nine:
            nine = False
            for y, line in enumerate(lines):
                for index, int in enumerate(line):
                    if line[index] > 9 and not has_flashed[index, y]:
                        has_flashed[index, y] = True
                        flashes += 1
                        nine = True
                        lines[y - 1][index] += 1  # up
                        lines[y + 1][index] += 1  # down
                        line[index - 1] += 1  # left
                        line[index + 1] += 1  # right
                        lines[y - 1][index - 1] += 1  # up left
                        lines[y - 1][index + 1] += 1  # up right
                        lines[y + 1][index - 1] += 1  # down left
                        lines[y + 1][index + 1] += 1  # down right
        for y, line in enumerate(lines):
            for index, int in enumerate(line):
                if has_flashed[index, y]:
                    line[index] = 0
                    has_flashed[index, y] = False
                elif line[index] > -100 and not has_flashed[index, y]:
                    sync = False
        if sync:
            print(day + 1)

