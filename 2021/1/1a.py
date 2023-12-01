index = 0
count = 0
with open("1.txt", "r") as file:
  lines = file.readlines()
  for line in lines:
    if line > lines[index-1]:
      count += 1
    index += 1
  print(count)
# somehow gets one under answer
