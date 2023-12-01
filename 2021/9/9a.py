with open("9.txt") as file:
  sum = 0
  lines = file.readlines()
  for y, line in enumerate(lines):
    line = [int(i) for i in line.strip()]
    for index, point in enumerate(line):
          above = int(lines[y-1][index]) if y != 0 else 10
          below = int(lines[y+1][index]) if y != len(lines) - 1 else 10
          if int(above) > line[index] and below > line[index]:
            sum += line[index] + 1
print(sum)
