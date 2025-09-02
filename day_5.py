import re
# path = "inputs/test_input/day5_test_input.txt"
path = "inputs/day5_input.txt"

#    [D]
#[N] [C]
#[Z] [M] [P]
# 1   2   3
# stacks = {1: ['Z','N'],
#              2: ['M','C','D'],
#              3: ['P']}

#     [W]         [J]     [J]
#     [V]     [F] [F] [S] [S]
#     [S] [M] [R] [W] [M] [C]
#     [M] [G] [W] [S] [F] [G]     [C]
# [W] [P] [S] [M] [H] [N] [F]     [L]
# [R] [H] [T] [D] [L] [D] [D] [B] [W]
# [T] [C] [L] [H] [Q] [J] [B] [T] [N]
# [G] [G] [C] [J] [P] [P] [Z] [R] [H]
#  1   2   3   4   5   6   7   8   9
#
stacks = {1: ['G', 'T', 'R', 'W'],
          2: ['G', 'C', 'H', 'P', 'M', 'S', 'V', 'W'],
3: ['C', 'L', 'T', 'S', 'G', 'M'],
4: ['J', 'H', 'D', 'M', 'W', 'R', 'F'],
5: ['P', 'Q', 'L', 'H', 'S', 'W', 'F', 'J'],
6: ['P', 'J', 'D', 'N', 'F', 'M', 'S'],
7: ['Z', 'B', 'D', 'F', 'G', 'C', 'S', 'J'],
8: ['R', 'T', 'B'],
9: ['H', 'N', 'W', 'L', 'C']}

instructions = []
begin = False
with open(path) as f:
    for line in f:
        if begin:
            numbers = list(map(int, re.findall(r'\d+', line)))
            instructions.append(numbers)
        if line == "\n":
           begin = True
#
# Part 1
# for i in instructions:
#     num = i[0]
#     start = stacks[i[1]]
#     end = stacks[i[2]]
#     for j in range(num):
#         crate = start.pop()
#         end.append(crate)


# Part 2
for i in instructions:
    num = i[0]
    start = stacks[i[1]]
    end = stacks[i[2]]
    new_stack = []
    for j in range(num):
        new_stack.append(start.pop())
    for k in range(num):
        end.append(new_stack.pop())

message = ""
for (key, val) in stacks.items():
    message += val[-1]
print(message)

