# with open("input.txt", "r") as file:
#     count = 0
#     for line in file.readlines():
#         a, b = line.split(",")
#         amin, amax = a.split("-")
#         bmin, bmax = b.split("-")
#         if (int(amin) <= int(bmin) and int(amax) >= int(bmax)) or (int(amin) >= int(bmin) and int(amax) <= int(bmax)):
#             print(a,b)
#             count += 1
# with open("input.txt", "r") as file:
#     count = 0
#     for line in file.readlines():
#         a, b = line.split(",")
#         amin, amax = a.split("-")
#         bmin, bmax = b.split("-")
#
#         if (int(bmin) in range(int(amin), int(amax)+1)) or (int(amax) in range(int(bmin), int(bmax)+1)) or (int(amax) in range(int(bmin), int(bmax) +1) or (int(amin) in range(int(bmin), int(bmax)+1))):
#             count += 1
#             print(amin, amax)
#             print(bmin, bmax)

# Parse the input to extract the pairs of ranges
with open('input.txt', 'r') as f:
    ranges = []
    for line in f:
        # Split the line on the comma and strip leading/trailing whitespace from each part
        parts = [part.strip() for part in line.split(',')]

        # Check that there are exactly two parts
        if len(parts) != 2:
            raise ValueError('Invalid input format')

        # Try to convert the parts to integers
        try:
            low1, high1 = map(int, parts[0].split('-'))
            low2, high2 = map(int, parts[1].split('-'))
        except ValueError:
            raise ValueError('Invalid input format')

        # Add the range pair to the list of ranges
        ranges.append(((low1, high1), (low2, high2)))

# Iterate over all pairs of ranges and check if one of the ranges fully contains the other
counter = 0
for (low1, high1), (low2, high2) in ranges:
    if low1 <= low2 and high1 >= high2:
        # Range 1 fully contains range 2
        counter += 1
    elif low2 <= low1 and high2 >= high1:
        # Range 2 fully contains range 1
        counter += 1

# Output the counter as the answer to the problem
print(counter)