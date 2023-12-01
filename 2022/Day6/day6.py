with open("input.txt", "r") as file:
    input = file.read()
for index, char in enumerate(input):
    for char2 in input[index:index+14]:
        if input[index:index+14].count(char2) > 1:
           break
    else:
        print(index+14)
        break
