from collections import namedtuple

# Test Data
# path = "inputs/test_input/day9_test_input.txt"

# Data
path = "inputs/day9_input.txt"

Instruction = namedtuple("Instruction", ["dir", "steps"])
Position = namedtuple("Position", ["x", "y"])
instructions = []
with open(path) as f:
    for line in f:
        line = line.strip().split(' ')
        instructions.append(Instruction(line[0], int(line[1])))

dir_mapping = {'R': Position(1, 0), 'L': Position(-1, 0), 'U': Position(0, 1), 'D': Position(0, -1)}


# H = Position(0, 0)
# T = Position(0, 0)


def show_viz(H, T, y_max, x_max):
    for y in range(y_max - 1, -1, -1):
        r = ['.'] * x_max
        if y == T.y:
            r[T.x] = 'T'
        if y == H.y:
            r[H.x] = 'H'
        print(''.join(r))


def show_tails(tails, y_max, x_max):
    grid = [['.'] * x_max for _ in range(y_max)]
    for t in tails:
        grid[t.y][t.x] = '#'
    for i in range(y_max - 1, -1, -1):
        print(''.join(grid[i]))


moves_mapping = {
    Position(2, 0): Position(1, 0), Position(-2, 0): Position(-1, 0),
    Position(0, 2): Position(0, 1), Position(0, -2): Position(0, -1),
    Position(1, 2): Position(1, 1), Position(2, 1): Position(1, 1),
    Position(2, -1): Position(1, -1), Position(1, -2): Position(1, -1),
    Position(-1, -2): Position(-1, -1), Position(-2, -1): Position(-1, -1),
    Position(-2, 1): Position(-1, 1), Position(-1, 2): Position(-1, 1),
    Position(2, 2): Position(1, 1), Position(-2, 2): Position(-1, 1),
    Position(2, -2): Position(1, -1), Position(-2, -2): Position(-1, -1),
}


# heads = []
# tails = [T]


# # for instruction in instructions[0:5]:
# for instruction in instructions:
#     for _ in range(instruction.steps):
#
#         step = dir_mapping[instruction.dir]
#         H = Position(H.x + step.x, H.y + step.y)
#         dist = Position(H.x - T.x, H.y - T.y)
#         if dist in moves_mapping:
#             step = moves_mapping[dist]
#             T = Position(step.x + T.x, step.y + T.y)
#             tails.append(T)
#         # print("H: ", H)
#         # print("T: ", T)
#         # print(instruction)
#         # show_viz(H, T, 5,6)
#         # print("\n")
#         # print("==============")

# show_tails(tails, 6,5)
# print(tails)
# print(len(set(tails)))

# Part 2
def move_tail(H, T):
    dist = Position(H.x - T.x, H.y - T.y)
    # print("dist", dist)
    if dist in moves_mapping:
        s = moves_mapping[dist]
        T = Position(s.x + T.x, s.y + T.y)
    return T


knots = [Position(10, 10)] * 10
tails = []


def show_grid(pos, y_max, x_max):
    grid = [['.'] * x_max for _ in range(y_max)]

    for i in range(len(pos) - 1, -1, -1):
        marker = pos[i]
        s = 'H' if i == 0 else str(i)
        grid[marker.y][marker.x] = s

    for i in range(y_max - 1, -1, -1):
        print(''.join(grid[i]))

for instruction in instructions:

    for _ in range(instruction.steps):
        step = dir_mapping[instruction.dir]
        knots[0] = Position(knots[0].x + step.x, knots[0].y + step.y)
        new_head = knots[0]

        for i in range(1, len(knots)):
            knots[i] = move_tail(new_head, knots[i])
            if i == len(knots) - 1:
                tails.append(knots[i])
            new_head = knots[i]

print(len(set(tails)))
