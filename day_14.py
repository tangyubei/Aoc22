import ast

# path = "inputs/test_input/day14_test_input.txt"

path = "inputs/day14_input.txt"

COORDINATES = []
x_max = y_max = 0
x_min = y_min = 500
with open(path) as file:
    for f in file:
        line = [ast.literal_eval(l) for l in f.strip().split(" -> ")]
        COORDINATES.append(line)
        for l in line:
            x_max = max(x_max, l[0])
            y_max = max(y_max, l[1])
            x_min = min(x_min, l[0])
            y_min = min(y_min, l[1])

def get_grid(r, c_max, c_min):
    grid = []
    for _ in range(0,r):
        l = []
        for _ in range(c_min,c_max):
            l.append('.')
        grid.append(l)
    return grid

def draw_on_grid(grid, x, y):
    grid[y][x] = '+'

# for coords in COORDINATES:
#     for c in coords:
#         print(c[0]-494, c[1])
#         g[c[1]][c[0]-494] = '+'

coord = COORDINATES[0]

def get_tuples_between(t1, t2):
    result = []
    x1, y1 = t1
    x2, y2 = t2

    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            result.append((x, y))
    return result

def draw_path_on_grid(grid, path, offset):
    for i,j in zip(path[:-1], path[1:]):
        print(i, j)
        tuples_between = get_tuples_between(i,j)
        for t in tuples_between:
            draw_on_grid(grid,t[0]-offset-1,t[1])

g = get_grid(y_max+1, x_max, x_min)

for c in COORDINATES:
    draw_path_on_grid(g, c, x_min)

draw_on_grid(g, 500 - x_min-1, 0)
# for _ in g:
#     print(''.join(_))

with open("outputs/day14_output.txt", "w") as file:
    for _ in g:
        file.write(''.join(_))
        file.write('\n')