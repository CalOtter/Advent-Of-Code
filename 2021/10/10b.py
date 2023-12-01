from statistics import median
pairs = {")" : "(", "]" : "[", "}" : "{", ">" : "<"}
inverse = {"(" : ")", "[" : "]", "{" : "}", "<" : ">"}
points = {")" : 1,  "]" : 2, "}" : 3, ">" : 4}
linescores = []
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
        corrupt = True
        break
    if not corrupt:
      remaining.append(line)
  for line in remaining:
    linescore = 0
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
        break
    added = ""
    stack.reverse()
    for char in stack:
      added += (inverse[char])
    for char in added:
      linescore  = (linescore * 5) + points[char]
    linescores.append(linescore)
print(median(linescores))