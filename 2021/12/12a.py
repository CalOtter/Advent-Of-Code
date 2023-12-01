with open("12.txt") as file:
    lines = file.readlines()
    paths = {}
    current = ""
    traveled = []
    found = []
    for path in lines:
        start, end = path.strip().split("-")
        if start in paths.keys():
            paths[start].append(end)
        else:
            paths[start] = [end]
        if end in paths.keys():
            paths[end].append(start)
        else:
            paths[end] = [start]
    del paths[end]
    for path in paths.keys():
        if "start" in paths[path]:
            paths[path].remove("start")
print(paths)
def travel(start):
    end = paths[start][0]
    if start.islower():
        del paths[start]
        for path in paths:
            if start in paths[path]:
                paths[path].remove(start)
    traveled.append(end)
    return end
while True:
    for path in paths["start"]:
        traveled.append("start")
        if path in paths.keys():
            current = travel(path)
            while len(traveled) != 0:
                if current == "end":
                    if traveled not in found:
                        print(traveled)
                        found.append(traveled)
                    traveled = []
                    break
                else:
                    travel(current)
