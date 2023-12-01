# import math
#
# with open("input.txt", "r") as file:
#     f = file.readlines()
#     monkeys = [[x.strip() for x in f[i:i + 7]] for i in range(0, len(f), 7)]
#
#
# class monkey():
#     def __init__(self, s):
#         self.items = [int(x) for x in s[1].split("Starting items:")[1].split(",")]
#         self.operation = s[2].split("new = ")[1]
#         self.test = int(s[3].split("divisible by ")[1])
#         self.true = int(s[4].split("throw to monkey ")[1])
#         self.false = int(s[5].split("throw to monkey ")[1])
#         self.inspects = 0
#
#     def turn(self, monkeys):
#         if len(self.items) == 0:
#             return
#         for index, item in enumerate(self.items):
#             old = item
#             item = math.floor(eval(self.operation)/3)
#             if not (item % self.test):
#                 monkeys[self.true].catch(item)
#             else:
#                 monkeys[self.false].catch(item)
#             self.inspects += 1
#         self.items = []
#
#     def catch(self, item):
#         self.items.append(item)
#
#     def count(self):
#         return self.inspects
#
#
# for i, m in enumerate(monkeys):
#     monkeys[i] = monkey(m)
# for round in range(10000):
#     for monkey in monkeys:
#         monkey.turn(monkeys)
# highest = []
# for monkey in monkeys:
#     highest.append(monkey.count())
# highest.sort(reverse=True)
# print(highest[0] * highest[1])
import math

import math

with open("input.txt", "r") as file:
    f = file.readlines()
    monkeys = [[x.strip() for x in f[i:i + 7]] for i in range(0, len(f), 7)]


class monkey():
    def __init__(self, s):
        self.items = [int(x) for x in s[1].split("Starting items:")[1].split(",")]
        self.operation = s[2].split("new = ")[1]
        self.test = int(s[3].split("divisible by ")[1])
        self.true = int(s[4].split("throw to monkey ")[1])
        self.false = int(s[5].split("throw to monkey ")[1])
        self.inspects = 0

    def turn(self, monkeys):
        if len(self.items) == 0:
            return
        for index, item in enumerate(self.items):
            old = item
            item = eval(self.operation)%supermod
            if not (item % self.test):
                monkeys[self.true].catch(item)
            else:
                monkeys[self.false].catch(item)
            self.inspects += 1
        self.items = []

    def catch(self, item):
        self.items.append(item)

    def count(self):
        return self.inspects


for i, m in enumerate(monkeys):
    monkeys[i] = monkey(m)
supermod = math.lcm(*tuple([monkey.test for monkey in monkeys]))
for round in range(10000):
    highest = []
    for monkey in monkeys:
        monkey.turn(monkeys)
    for monkey in monkeys:
        highest.append(monkey.count())
highest.sort(reverse=True)
print(highest)
print(highest[0] * highest[1])