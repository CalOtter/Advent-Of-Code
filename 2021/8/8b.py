def sc(shorter, longer):
    # return set(shorter).issubset((set(longer)))
    for char in ''.join(sorted(shorter)).strip():
        if char not in ''.join(sorted(longer)).strip():
            return False
    return True
with open("8.txt") as file:
    sum = 0
    lines = file.readlines()
    for line in lines:
        sol = ""
        answers = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: "", 0: ""}
        split = line.split()
        for item in split:
            item = ''.join(sorted(item))
            if len(item) == 2:
                answers[1] = item
            if len(item) == 3:
                answers[7] = item
            if len(item) == 4:
                answers[4] = item
            if len(item) == 7:
                answers[8] = item
            for attempt in range(2):
                for item in split:
                    item = ''.join(sorted(item)).strip()
                    if len(item) == 5 and sc(answers[1], item):
                        answers[3] = item
                    elif len(item) == 6 and not sc(answers[1], item):
                        answers[6] = item
                    elif len(item) == 6 and sc(answers[1], item) and sc(answers[4], item):
                        answers[9] = item
                    elif len(item) == 6:
                        answers[0] = item
                    elif len(item) == 5 and sc(item,answers[9]):
                        answers[5] = item
                    elif len(item) == 5 and not sc(answers[9], item) and not sc(answers[1], item):
                        answers[2] = item
        print(answers)
        answers = {answers[k] : k for k in range(10)}
        for item in line.split("|")[-1].split():
            item = ''.join(sorted(item))
            sol += str(answers[item])
        sum += int(sol)
        print(sol, sum)
# 0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 5:6, 7:3, 8:7, 9:6
print(sum)