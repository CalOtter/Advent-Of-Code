
with open("4.txt", "r") as file:
    input = file.read()
    numbers = (input.split("\n")[0]).split(",")
    called = []
    boards = [board.split("\n") for board in (input.split("\n\n")[1:])]
def check_boards():
    sum = 0
    col = []
    for number in numbers:
        called.append(int(number))
        for board in boards:
            for row in board:
                row = [int(x) for x in row.split(" ") if x != ""]
                if set(row).issubset(set(called)):
                    for row in board:
                        row = [int(x) for x in row.split(" ") if x != ""]
                        for num in row:
                            if int(num) not in called:
                                sum += int(num)
                    return sum * int(number)
            for index, column in enumerate(board):
                for row in board:
                    row = [int(x) for x in row.split(" ") if x != ""]
                    col.append(row[index])
                if set(col).issubset(set(called)) and len(called):
                    for row in board:
                        row = [int(x) for x in row.split(" ") if x != ""]
                        for num in row:
                            if int(num) not in called:
                                sum += int(num)
                    return sum * int(number)
                col = []
print(check_boards())
