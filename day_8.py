# Test Data
# path = "inputs/test_input/day8_test_input.txt"

# Data
path = "inputs/day8_input.txt"

grid = []
with open(path) as f:
    for line in f:
        row = [int(x) for x in line.strip()]
        grid.append(row)

num_rows = len(grid)
num_cols = len(grid[0])
count = 0
grid_T = list(map(list, zip(*grid)))

# Part 1
# for i in range(num_rows):
#     for j in range(num_cols):
#         target = grid[i][j]
#
#         right_pivot = grid[i][j+1:]
#         left_pivot = grid[i][:j]
#         down_pivot = grid_T[j][i+1:]
#         up_pivot = grid_T[j][:i]
#
#         if len(right_pivot) == 0 or len(left_pivot) == 0 or len(down_pivot) == 0 or len(up_pivot) == 0 or target > max(right_pivot) or target > max(left_pivot) or target > max(up_pivot) or target > max(down_pivot):
#             count += 1
#
# print(count)

# Part 2
def score_trees(target, row):
    score = 0
    i = 0
    while i < len(row):
        if target > row[i]:
            score += 1
        elif target <= row[i] and i < len(row):
            score += 1
            break
        else:
            break
        i += 1
    return score

max_score = 0
for i in range(num_rows):
    for j in range(num_cols):
        target = grid[i][j]
        right_pivot = grid[i][j+1:]
        left_pivot = grid[i][:j][::-1]
        down_pivot = grid_T[j][i+1:]
        up_pivot = grid_T[j][:i][::-1]
        s = score_trees(target, right_pivot) * score_trees(target, left_pivot) * score_trees(target, down_pivot) * score_trees(target, up_pivot)
        max_score = max(max_score, s)
print(max_score)





