# with open("input.txt", "r") as file:
#     grid = [[int(char) for char in row.strip()] for row in file.readlines()]
#     marked = [["" for i in range(len(grid[0]))]for pos in range(len(grid))]
# for y, row in enumerate(grid):
#     rowmin = -1
#     for x, tree in enumerate(row):
#         column = [grid[y][x] for y, row in enumerate(grid)]
#         if x == 0 or y == 0 or x == len(row) or y == len(row):
#             marked[y][x] = "1"
#         for height in row[:x]:
#             if tree <= height:
#                 break
#         else:
#             marked[y][x] = "1"
#         for height in row[x+1:]:
#             if tree <= height:
#                 break
#         else:
#             marked[y][x] = "1"
#         for height in column[:y]:
#             if tree <= height:
#                 break
#         else:
#             marked[y][x] = "1"
#         for height in column[y+1:]:
#             if tree <= height:
#                 break
#         else:
#             marked[y][x] = "1"
#
# total = 0
# for pos in marked:
#     total += pos.count("1")
# print(marked)
# print(total)
highest = 0
with open("input.txt", "r") as file:
    grid = [[int(char) for char in row.strip()] for row in file.readlines()]
for y, row in enumerate(grid):
    for x, tree in enumerate(row):
        left = 0
        right = 0
        up = 0
        down = 0
        column = [grid[y][x] for y, row in enumerate(grid)]
        for height in row[:x][::-1]:
            if tree <= height:
                left += 1
                break
            else:
                left += 1
        for height in row[x+1:]:
            if tree <= height:
                right += 1
                break
            else:
                right += 1
        for height in column[:y][::-1]:
            if tree <= height:
                up += 1
                break
            else:
                up += 1
        for height in column[y+1:]:
            if tree <= height:
                down += 1
                break
            else:
                down += 1
        total = left * right * up * down
        if total > highest:
            highest = total

print(highest)