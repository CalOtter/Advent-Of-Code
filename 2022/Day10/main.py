with open("input.txt", "r") as file:
    instructions = file.readlines()

def check(tick):
    if tick in [20, 60, 100, 140, 180, 220]:
        print(x, tick, x*tick)
        return x*tick
    return 0# for tick in range(len(instructions)):

#     total += check(tick)
#     if blocked != 0:
#         blocked -= 1
#     if blocked == 0:
#         x += to_add
#         to_add = 0
#         if instructions[i].strip() == "noop":
#             i += 1
#         elif "addx" in instructions[i]:
#             to_add = int(instructions[i].split(" ")[1])
#             i += 1
#             blocked = 2
i = 0
blocked = 0
tick = 0
to_add = 0
crt_x = 0
crt_y = 0
x = 1
grid = [["." for xx in range(40)] for yy in range(6)]
while i < len(instructions):
    if blocked != 0:
        blocked -= 1
    if blocked == 0:
        x += to_add
        to_add = 0
        if instructions[i].strip() == "noop":
            i += 1
        elif "addx" in instructions[i]:
            to_add = int(instructions[i].split(" ")[1])
            i += 1
            blocked = 2
    if crt_x in [x-1, x, x+1]:
        grid[crt_y][crt_x] = "#"
        print(instructions[i], crt_x)
    crt_x += 1
    if crt_x in [40, 80, 120, 160, 200, 240]:
        crt_y += 1
        crt_x = 0

for row in grid:
    print("".join(row))