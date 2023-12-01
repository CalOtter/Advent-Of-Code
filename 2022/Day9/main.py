# with open("input.txt", "r") as file:
#     input = [line.strip().split(" ") for line in file.readlines()]
# visited = [["" for i in range(1000)] for pos in range(1000)]
# tail = [0, 0]
# head = [0, 0]
# sign = lambda a: (a > 0) - (a < 0)
#
# for instruction in input:
#     direction, magnitude = instruction
#     magnitude = int(magnitude)
#     for step in range(magnitude):
#         match direction:
#             case "R":
#                 head[1] += 1
#             case "L":
#                 head[1] -= 1
#             case "U":
#                 head[0] += 1
#             case "D":
#                 head[0] -= 1
#         if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
#             if head[0] != tail[0] and head[1] != tail[1]:
#                 tail[0] += sign(head[0] - tail[0])
#                 tail[1] += sign(head[1] - tail[1])
#             elif head[1] == tail[1]: # head and tail in same column
#                 tail[0] += sign(head[0] - tail[0])
#             else:
#                 tail[1] += sign(head[1] - tail[1])
#         visited[tail[0]][tail[1]] = "X"
# total = 0
# visited[0][0] = "S"
# for y in visited:
#     for x in y:
#         if x != "":
#          total += 1
# # for line in visited[::-1]:
# #     print(line)
# print(total)
with open("input.txt", "r") as file:
    input = [line.strip().split(" ") for line in file.readlines()]
visited = [["" for i in range(1000)] for pos in range(1000)]
knots = [[0,0] for knot in range(10)]
sign = lambda a: (a > 0) - (a < 0)

for instruction in input:
    direction, magnitude = instruction
    magnitude = int(magnitude)
    for step in range(magnitude):
        match direction:
            case "R":
                knots[0][1] += 1
            case "L":
                knots[0][1] -= 1
            case "U":
                knots[0][0] += 1
            case "D":
                knots[0][0] -= 1
        index = 0
        for knot in knots[1:]:
            index += 1
            front = knots[index-1]
            print(type(knot), type(front))
            if abs(front[0] - knot[0]) > 1 or abs(front[1] - knot[1]) > 1:
                if front[0] != knot[0] and front[1] != knot[1]:
                    knot[0] += sign(front[0] - knot[0])
                    knot[1] += sign(front[1] - knot[1])
                elif front[1] == knot[1]: # head and tail in same column
                    knot[0] += sign(front[0] - knot[0])
                else:
                    knot[1] += sign(front[1] - knot[1])
        visited[knots[-1][0]][knots[-1][1]] = "X"
total = 0
for y in visited:
    for x in y:
        if x != "":
         total += 1

print(total)