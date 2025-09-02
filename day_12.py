#test data
path = "inputs/test_input/day12_test_input.txt"

grid = []
with open(path) as file:
    for f in file:
        line = list(f.strip())
        grid.append(line)

