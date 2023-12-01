with open("input.txt", "r") as file:
    lines = file.readlines()
score = 0
arr = {"X":1,"Y":2, "Z":3}
# for line in lines:
#     o, u = line.strip().split(" ")
#     print(o,u)
#     score += arr[u]
#     if (u == "X" and o == "C") or (u == "Z" and o =="B") or (u == "Y" and o == "A"):
#         score += 6
#         print("won")
#     elif (u == "X" and o == "A") or (u == "Y" and o =="B") or (u == "Z" and o == "C"):
#         score += 3
#         print("tie")
win = {"c":"x", "b":"z", "a":"y"}
tie = {"a":"x","b":"y","c":"z"}
loss = {"b":"x", "a":'z', "c":"y"}
for line in lines:
    o, u = line.strip().split(" ")
    o, u = o.lower(), u.lower()
    print(o,u)
    if u == "x":
        u = loss[o]
    elif u == "y":
        u = tie[o]
        score += 3
    elif u == "z":
        u = win[o]
        score += 6
    score += arr[u.upper()]


print(score)