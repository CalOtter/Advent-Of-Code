import numpy as np
from collections import defaultdict

with open("input.txt") as file:
    grid = np.array([[char for char in line.strip()] for line in file.readlines()])
starty, startx = np.where(grid == "S")
grid[starty, startx] = "a"
visited = defaultdict(None)
ymax, xmax = grid.shape
paths = []
def pathfind(y, x, path):
    if ([y[0], x[0]]) not in path:
        path.append([y[0], x[0]])
        current = ord(grid[y, x][0]) if grid[y, x] != "S" else 96
        up = ord((grid[y - 1, x][0])) if y != 0 else 999
        down = ord(str(grid[y + 1, x][0])) if y+1 != ymax else 999
        left = ord(str(grid[y, x - 1][0])) if x != 0 else 999
        right = ord(str(grid[y, x + 1][0])) if x + 1 != xmax else 999
        if 69 in [up, down, left, right] and current == 122:
            print(len(path))
        if 0 <= down - current <= 1:
            pathfind(y + 1, x, path)
        if 0 <= left - current <= 1:
            pathfind(y, x - 1, path)
        if 0 <= up - current <= 1:
            pathfind(y-1, x, path)
        if 0 <= right - current <= 1:
            pathfind(y, x + 1, path)
pathfind(starty, startx, [])
for path in paths:
    print(len(path), path)