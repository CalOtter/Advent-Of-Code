counts = {}
with open("6.txt") as file:
    numbers = [int(x) for x in file.read().split(",")]
    for number in range(10):
        counts[number] = 0
    for number in numbers:
        counts[number] += 1
    for day in range(256):
        counts[7] += counts[0]
        counts[9] = counts[0]
        for number in range(0, 9):
            counts[number] = counts[number + 1]
print(sum(counts.values()) - counts[9])
# why do I have to do - counts[9]? not sure, but it made the code work so its there
lo