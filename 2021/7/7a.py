from statistics import median
total = 0
with open("7.txt") as file:
    numbers = [int(x) for x in file.read().split(",")]
    med = median(numbers)
    for number in numbers:
        total += int(abs(number - med))
print(total)
