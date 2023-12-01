import re
with open("shorterinput.txt", "r") as file:
    starting, instructions = file.read().split("m", 1)
    instructions = instructions.split("\n")
    starting = starting.split("\n")
    columns = [[] for i in range(int(9))]
    nums = []
    for line in starting[:-3]:
        for position, char in enumerate(line):
            if char not in [" ", "[", "]"]:
                columns[int((position+3)/4) - 1].append(char)
    for position, line in enumerate(instructions):
        instructions[position] = (re.findall("\d+", line))
    for instruction in instructions:
        print(instruction)
        toappend = ""
        toappend = columns[(int(instruction[1]) - 1)][0:int(instruction[0])]
        del columns[(int(instruction[1]) - 1)][0:int(instruction[0])]
        for crate in toappend:
            columns[int(instruction[2]) - 1].insert(0, crate)
    print("".join([column[0] for column in columns]))
# import re
# with open("shorterinput.txt", "r") as file:
#     starting, instructions = file.read().split("m", 1)
#     instructions = instructions.split("\n")
#     starting = starting.split("\n")
#     columns = [[] for i in range(int(9))]
#     nums = []
#     for line in starting[:-3]:
#         for position, char in enumerate(line):
#             if char not in [" ", "[", "]"]:
#                 columns[int((position+3)/4) - 1].append(char)
#     print("Done parsing!")
#     for position, line in enumerate(instructions):
#         instructions[position] = (re.findall("\d+", line))
#     print("Regex done!")
#     for instruction in instructions:
#         print(instruction)
#         toappend = columns[(int(instruction[1]) - 1)][0:int(instruction[0])]
#         del columns[(int(instruction[1]) - 1)][0:int(instruction[0])]
#         for crate in toappend[::-1]:
#             columns[int(instruction[2]) - 1].insert(0, crate)
#     print("".join([column[0] for column in columns]))
