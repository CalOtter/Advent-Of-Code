zeros, ones, gammas, epsilions = 0,0, "", ""
with open("2.txt", "r") as file:
  lines = file.read().splitlines()
  for position in range(12):
    for line in lines:
      zeros += 1 if line[position] == "0" else 0
      ones += 1 if line[position] == "1" else 0
    gammas += "1" if zeros < ones else "0"
    epsilions += "1" if zeros > ones else "0"
    zeros, ones = 0,0
print(int("0b" + epsilions, 2) * int("0b" + gammas, 2))