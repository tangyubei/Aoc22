import ast
from itertools import zip_longest

# test data
# path = "inputs/test_input/day13_test_input.txt"

# data
path = "inputs/day13_input.txt"

lines = []
with open(path) as f:
    lines = [ast.literal_eval(line.strip()) for line in f if line.strip()]

left = lines[::2]
right = lines[1::2]

def compare(left, right):
    for l, r in zip_longest(left, right, fillvalue=None):
        if l is None:
            return True  # Left ran out first
        if r is None:
            return False  # Right ran out first

        # Handle list vs int cases
        if isinstance(l, list) and isinstance(r, list):
            result = compare(l, r)
        elif isinstance(l, list):
            result = compare(l, [r])
        elif isinstance(r, list):
            result = compare([l], r)
        else:
            # Compare integers
            if l < r:
                return True
            elif l > r:
                return False
            else:
                continue  # Equal, go to next pair
        if result is not None:
            return result
    return None

# Part 1

# index = 0
# sum = 0
# for x,y in zip(left, right):
#     index += 1
#     if compare(x,y):
#         sum += index
#
# print(sum)

# Part 2

def swap_elements(lt, i,j):
    lt[i], lt[j] = lt[j], lt[i]

# lines.append([[2]])
# lines.append([[6]])

sorted_lines = []

# for l in lines:
#     sorted_lines.append(l)
#     j = len(sorted_lines) - 2
#     for i in range(len(sorted_lines)-1, 0, -1):
#         if compare(sorted_lines[i], sorted_lines[j]):
#             swap_elements(sorted_lines, i, j)
#             j -= 1
#         else:
#             break

def add_elem(presorted, l):
    presorted.append(l)
    j = len(presorted) - 2
    for i in range(len(presorted)-1, 0, -1):
        if compare(presorted[i], presorted[j]):
            swap_elements(presorted, i, j)
            j -= 1
        else:
            break
    return j+1

for l in lines:
    # sorted_lines.append(l)
    i = add_elem(sorted_lines, l)


first_divider = add_elem(sorted_lines, [[2]])+1
second_divider = add_elem(sorted_lines, [[6]])+1

print(first_divider)
print(second_divider)

print(first_divider * second_divider)

