pairs = {")" : "(", "]" : "[", "}" : "{", ">" : "<"}
points = {")" : 3,  "]" : 57, "}" : 1197, ">" : 25137}
sum = 0
remaining = []
with open("10.txt") as file:
  lines = file.readlines()
  for line in lines:
    corrupt = False
    line = line.strip()
    stack = []
    for char in line:
      if char in pairs.values():
        stack.append(char)
      elif char in pairs.keys() and pairs[char] == stack[-1]:
        stack.reverse()
        try:
            stack.remove(pairs[char])
        except:
            pass
        stack.reverse()
      else:
        sum += points[char]
        break
print(sum)


