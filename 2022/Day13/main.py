with open("input.txt") as file:
    input = [[[eval(i) for i in line.split()] for line in (group.split("\n"))] for group in file.read().split("\n\n")]
correct = []
incorrect = []
def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left > right:
            incorrect.append(index + 1)
            return
    elif isinstance(left, list) and isinstance(right, list):
        if len(left) > len(right):
            incorrect.append(index+1)
            return
        if len(left) != 0:
            for i, element in enumerate(left):
                for element2 in right:
                    compare(element, element2)
    elif isinstance(left, int) and isinstance(right, list):
        left = [left]
        compare(left, right)
    elif isinstance(left, list) and isinstance(right, int):
        right = [right]
        compare(left, right)
    correct.append(index+1)

for index, pair in enumerate(input):
    compare(pair[0][0], pair[1][0])
for element in set(correct):
    if element not in set(incorrect):
        print(element)
