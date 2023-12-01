with open("8.txt") as file:
    sum = 0
    lines = [line.split("|")[-1] for line in file.readlines()]
    for line in lines:
        for item in line.split():
            if len(item) == 7 or len(item) == 4 or len(item) == 3 or len(item) == 2:
                sum += 1
print(sum)