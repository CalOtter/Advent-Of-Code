
with open("4.txt", "r") as file:
    input = file.read()
    numbers = (input.split("\n")[0]).split(",")
    called = []
    boards = [board.split("\n") for board in (input.split("\n\n")[1:])]
    remaining = boards.copy()
def check_boards():
    sum = 0
    col = []
    for number in numbers:
        called.append(int(number))
        if len(remaining) == 1:
            break
        for board in boards:
            for row in board:
                row = [int(x) for x in row.split(" ") if x != ""]
                if set(row).issubset(set(called)) and board in remaining:
                    try:
                        remaining.remove(board)
                    except:
                        pass
            for index, column in enumerate(board):
                for row in board:
                    row = [int(x) for x in row.split(" ") if x != ""]
                    col.append(row[index])
                if set(col).issubset(set(called)) and board in remaining:
                    try:
                        remaining.remove(board)
                    except:
                        pass
                col = []
    board = remaining[0]
    for row in board:
        row = [int(x) for x in row.split(" ") if x != ""]
        for num in row:
            if int(num) not in called:
                sum += int(num)
    return sum * int(number)
print(check_boards())
