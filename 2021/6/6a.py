with open("6.txt") as file:
    numbers = [int(x) for x in file.read().split(",")]
    for day in range(18):
        for index, number in enumerate(numbers):
            if number == 0:
                numbers[index] = 6
                numbers.append(9)
            else:
                numbers[index] -= 1
print(len(numbers))
