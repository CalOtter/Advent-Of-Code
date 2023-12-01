from math import floor
total = 0
with open("7.txt") as file:
    numbers = [int(x) for x in file.read().split(",")]
    average = floor((sum(numbers) / len(numbers)))
    for number in numbers:
        for num in range(abs(number - average)):
            total += 1 + num
print(total)
