from collections import Counter
with open("input.txt", "r") as file:
    lines = file.readlines()
score = 0
# for line in lines:
#     a, b = line[:int((len(line)/2))], line[int(len(line)/2):]
#     print(a,b)
#     for item in Counter(a).keys():
#         if item in Counter(b).keys():
#             print(item,((ord(item) - 96 if item.lower() == item else (ord(item) - 64 + 26))))
#             score += ((ord(item) - 96 if item.lower() == item else (ord(item) - 64 + 26)))
# print(score)
for group in [lines[x:x+3] for x in range(0,len(lines), 3)]:
    a, b ,c = Counter(group[0]), Counter(group[1]), Counter(group[2])
    for item in Counter(a).keys():
        if item in Counter(b).keys() and item != "\n":
            if item in Counter(c).keys():
                print(item.strip())
                item_score = ((ord(item) - 96 if item.lower() == item else (ord(item) - 64 + 26)))
                score += item_score
print(score)