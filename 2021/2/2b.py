direction, magnitude, aim, x, y = 0, 0, 0, 0, 0
with open("2.txt", "r") as file:
    for line in file.read().splitlines():
        direction, magnitude = line.split(" ")[0], line.split(" ")[1]
        y += int(magnitude) * aim if direction == "forward" else 0
        x += int(magnitude)   if direction == "forward" else 0
        aim -= int(magnitude) if direction == "up" else 0
        aim += int(magnitude) if direction == "down" else 0
print(x, y, x*y)
    