# --- Day 3: Rucksack Reorganization ---
# path = "inputs/test_input/day3_test_input.txt"
path = "inputs/day3_input.txt"
inventory = []
with open(path) as f:
    for line in f:
        inventory.append(line.strip())

def get_priority_score(ch):
    if 'a' <= ch <= 'z':
        return ord(ch) - 96
    elif 'A' <= ch <= 'Z':
        return ord(ch) - 38
    else:
        return 0

# Part 1
# sum_priority = 0
# for r in inventory:
#     set_a = set(r[:len(r) // 2])
#     set_b = set(r[len(r) // 2:])
#     common = list(set_a & set_b)
#     sum_priority += get_priority_score(common[0])
# print(sum_priority)

# Part 2
i = 0
sum_priorities = 0
while i+2 < len(inventory):
    set_a = set(inventory[i])
    set_b = set(inventory[i + 1])
    set_c = set(inventory[i + 2])
    sets = sorted([set_a, set_b, set_c], key=len)
    result = list(sets[0] & sets[1] & sets[2])
    sum_priorities += get_priority_score(result[0])
    i = i+3
print(sum_priorities)