points = {}
covered = []
same = []
from collections import Counter
with open("5.txt") as file:
    input = file.read()
    lines = input.strip().split("\n")
    for line in lines:
        start, end = line.split("->")
        startx, starty = [int(x) for x in start.split(",")]
        endx, endy = [int(x) for x in end.split(",")]
        if startx == endx:
            if endy > starty:
                for point in range(int(endy) - int(starty) + 1):
                    covered.append(((int(startx), point + int(starty))))
            elif starty > endy:
                for point in range(int(starty) - int(endy), -1, -1):
                    covered.append(((int(startx), int(starty) - point)))
        elif starty == endy:
            if endx > startx:
                for point in range(int(endx) - int(startx) + 1):
                    covered.append(((point + int(startx)), int(starty)))
            if startx > endx:
                for point in range(int(startx) - int(endx), -1, -1):
                    covered.append(((int(startx) - point, int(starty))))
count = 0
sent = []
counter = Counter(covered)
for point in covered:
    if covered.count(point) > 1 and point not in sent:
        sent.append(point)
        count += 1
print(count)
