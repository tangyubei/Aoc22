# --- Day 6: Tuning Trouble ---

# Test Input
# datastream = 'bvwbjplbgvbhsrlpgdmjqwftvncz'

# Data
path = "inputs/day6_input.txt"

with open(path) as f:
    datastream = f.read()

# Part 1
# window = []
# i = 0
# while i+3 < len(datastream):
#     window = datastream[i:i+4]
#     if len(set(window)) == 4:
#         break
#     i += 1
# print(i+4)

# Part 2
window = []
i = 0
while i+3 < len(datastream):
    window = datastream[i:i+14]
    if len(set(window)) == 14:
        break
    i += 1
print(i+14)