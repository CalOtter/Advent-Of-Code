count = 0
windowed = []
with open("1.txt", "r") as file:
  lines = file.read().splitlines()
  for index, number in enumerate(lines):
      windowed.append((int(number) + int(lines[index-1]) + int(lines[index-2])))
  for index, window in enumerate(windowed):
    if window > windowed[index-1]:
        count += 1
print(count)