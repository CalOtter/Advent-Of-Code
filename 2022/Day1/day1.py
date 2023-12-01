# with open("input.txt", "r") as file:
#     lines = file.readlines()
# currSum = 0
# greatest = 0
# for line in lines:
#     line = line.strip()
#     if line != "":
#         currSum += int(line)
#     else:
#         if currSum > greatest:
#             greatest = currSum
#         currSum = 0
# print(greatest)
with open("input.txt", "r") as file:
    lines = file.readlines()
currSum = 0
sumArray = []
for line in lines:
    line = line.strip()
    if line != "":
        currSum += int(line)
    else:
        sumArray.append(currSum)
        currSum = 0
sumArray.sort()
print(sumArray[-1])
print(int(sumArray[-1] + sumArray[-2] + sumArray[-3]))