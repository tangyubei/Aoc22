# --- Day 4: Camp Cleanup ---
from collections import namedtuple
# path = "inputs/test_input/day4_test_input.txt"
path = "inputs/day4_input.txt"

data = []
Assignment = namedtuple('Assignment', ['l', 'r'])
with open(path) as f:
    for line in f:
        assignment = line.strip().split(',')
        elf_1 = Assignment(*map(int, assignment[0].split('-')))
        elf_2 = Assignment(*map(int, assignment[1].split('-')))
        data.append((elf_1, elf_2))

# count = 0
# for elf_1, elf_2 in data:
#     if (elf_1.l >= elf_2.l and elf_1.r <= elf_2.r) or (elf_2.l >= elf_1.l and elf_2.r <= elf_1.r):
#         count += 1
# print(count)

# Part 2
def overlap(elf1, elf2):
    if (elf1.r >= elf2.l and elf1.l <= elf2.r) or (elf2.r >= elf1.l and elf2.l <= elf1.r) :
        return True
    else:
        return False

count = 0
for elf_1, elf_2 in data:
    if overlap(elf_1, elf_2):
        count += 1
print(count)