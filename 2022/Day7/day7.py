with open("input.txt", "r") as file:
    commands = file.read().split("$")
filesystem = {}
currentpath = [""]
dirs = {}
for command in commands:
    if " cd " in command:
        target = command.split("cd ")[1].strip()
        if target == "..":
            currentpath.pop()
        else:
            currentpath.append(target)
    elif " ls\n" in command:
        output = command.split(" ls\n")[1].strip().split("\n")
        filesystem["/".join(currentpath)] = output
currentpath = []
print(filesystem)
def dirsize(path):
    sum = 0
    currentpath.append(path)
    for obj in filesystem['/'.join(currentpath)]:
        if "dir" in obj.split(" ")[0]:
            dr = obj.split("dir ")[1]
            sum += dirsize(dr)
        else:
            sum += int(obj.split(" ")[0])
    dirs['/'.join(currentpath)] = sum
    currentpath.pop()
    print(f"checked {path}, size was {sum}")
    return sum
dirsize("")
total = dirs[""]
lowest = 100000000000000000
for value in dirs.values():
    if 70000000 - total + value > 30000000  and value < lowest:
        lowest = value
print(lowest)