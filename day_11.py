from dataclasses import dataclass
import re
import math

@dataclass
class Monkey:
    num: int
    inventory: list[int]=None
    operation: str=""
    test: int=0
    t: int=0
    f: int=0
    inspections: int=0

# test data
# path = "inputs/test_input/day11_test_input.txt"

# data
path = "inputs/day11_input.txt"

lines = []
with open(path) as file:
    for f in file:
        lines.append(f.strip())

def process_monkeys(Monkeys):
    pattern = r"-?\d+"
    j = 0

    for i in range(0, len(lines), 7):
        # Monkey ID
        match = re.search(pattern, lines[i])
        Monkeys.append(Monkey(int(match.group())))

        # Inventory
        Monkeys[j].inventory  = [int(x) for x in re.findall(pattern, lines[i+1])]

        # Operation
        Monkeys[j].operation = lines[i+2][17:]

        # Test, divisible
        Monkeys[j].test = int(re.search(pattern, lines[i+3]).group())

        # True
        Monkeys[j].t = int(re.search(pattern, lines[i+4]).group())

        # False
        Monkeys[j].f = int(re.search(pattern, lines[i+5]).group())

        j += 1

def process_operation(op, num):
    old = num
    return eval(op)

# for M in Monkeys:
#     print(M.inventory)

# def go_one_round(Monkeys):
#     for M in Monkeys:
#         # print("staring inventory", M.inventory)
#         for item in M.inventory[:]:
#             worry_level = process_operation(M.operation, item)
#             worry_level = math.floor(worry_level)
#             if worry_level % M.test == 0:
#                 Monkeys[M.t].inventory.append(worry_level)
#             else:
#                 Monkeys[M.f].inventory.append(worry_level)
#             M.inventory.remove(item)
#             M.inspections += 1
#     # for M in Monkeys:
#     #     print(f"inventory {M.num}: {M.inventory}")
#     # print("\n")


# TempMonkeys = []
# process_monkeys(TempMonkeys)
# for rounds in range(20):
#     go_one_round(TempMonkeys)
#
# for M in TempMonkeys:
#     print(f"Monkey {M.num}: {M.inventory}")
#
# for M in TempMonkeys:
#     print(f"Monkey {M.num} inspected items {M.inspections} times.")
#
def get_largest(nums):
    first = second = 0
    for n in nums:
        if n > first:
            second = first
            first = n
        elif n > second:
            second = n
    return first, second
#
# m1, m2 = get_largest([m.inspections for m in TempMonkeys])
#
# print(m1, m2)
# print(m1 * m2)

def go_one_round(Monkeys, max_mod):
    for M in Monkeys:
        # print("staring inventory", M.inventory)
        for item in M.inventory[:]:
            worry_level = process_operation(M.operation, item)
            if worry_level > max_mod:
                worry_level = worry_level % max_mod
            if worry_level % M.test == 0:
                Monkeys[M.t].inventory.append(worry_level)
            else:
                Monkeys[M.f].inventory.append(worry_level)
            M.inventory.remove(item)
            M.inspections += 1
    # for M in Monkeys:
    #     print(f"inventory {M.num}: {M.inventory}")
    # print("\n")

TempMonkeys = []
process_monkeys(TempMonkeys)

max_mod = 1
for M in TempMonkeys:
    max_mod *= M.test

for rounds in range(10_000):
    go_one_round(TempMonkeys, max_mod)

for M in TempMonkeys:
    print(f"Monkey {M.num}: {M.inventory}")

for M in TempMonkeys:
    print(f"Monkey {M.num} inspected items {M.inspections} times.")


m1, m2 = get_largest([m.inspections for m in TempMonkeys])

print(m1, m2)
print(m1 * m2)