import re

# Test Data
# path = "inputs/test_input/day10_test_input.txt"

# # Data
path = "inputs/day10_input.txt"

lines = []
with open(path) as file:
    for f in file:
        lines.append(f.strip())

cycle = 1
X = 1
image = [[]]

def draw_pixel(pos, sprite_center):
    return '#' if sprite_center - 1 <= pos <= sprite_center + 1 else '.'

def run_cycle(cycle, X):
    col = (cycle - 1) % 40
    pixel = draw_pixel(col, X)
    image[-1].append(pixel)

    # Debug print (can comment out if not needed)
    # print(f"Cycle: {cycle}, X: {X}, Pixel: {pixel}, Col: {col}")
    # print(''.join(image[-1]))

    if len(image[-1]) == 40:
        image.append([])

for line in lines:
    if line == "noop":
        run_cycle(cycle, X)
        cycle += 1

    elif line.startswith("addx"):
        run_cycle(cycle, X)
        cycle += 1

        run_cycle(cycle, X)
        cycle += 1

        X += int(re.search(r"-?\d+", line).group())

# Print final image (strip trailing empty row if needed)
print("\nFinal image:\n")
for row in image:
    if row:  # skip empty rows
        print(''.join(row))