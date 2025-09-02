# --- Day 7: No Space Left On Device ---
from dataclasses import dataclass
import re

@dataclass
class File:
    name: str
    size: int

class TreeNode:
    def __init__(self, name=None, val=0, type=None, parent=None):
        self.name = name
        self.val = val
        self.type = type
        self.children = []
        self.parent = parent

    def add_child(self, child_node):
        child_node.parent = self
        self.children.append(child_node)

# Test Data
# path = "inputs/test_input/day7_test_input.txt"

# Input
path = "inputs/day7_input.txt"

# Load data
instructions = []
with open(path) as f:
    for line in f:
        instructions.append(line.strip())

root = TreeNode()
cur = None
cd_dir_pattern = re.compile(r'^\$ cd\s+(?!\.\.)([^\s]+)')
i = 0

while i < len(instructions):
    line = instructions[i]

    # Handle "$ cd <dirname>" (excluding "..")
    if cd_dir_pattern.match(line):
        dir_name = line[5:]
        if cur is None:
            root.name = dir_name
            root.type = 'dir'
            cur = root
        else:
            # Move to existing child directory
            for child in cur.children:
                if child.name == dir_name:
                    cur = child
                    break
        i += 1
        continue

    # Handle "$ ls"
    if line == '$ ls':
        i += 1
        while i < len(instructions) and not instructions[i].startswith('$'):
            entry = instructions[i]
            if entry.startswith('dir '):
                new_node = TreeNode(name=entry[4:])
                new_node.type = 'dir'
            else:
                size, name = entry.split(' ', 1)
                new_node = TreeNode(name=name, val=int(size))
                new_node.type = 'file'
            cur.add_child(new_node)
            i += 1
        continue

    # Handle "$ cd .."
    if line == '$ cd ..':
        cur = cur.parent
        i += 1
        continue

def compute_total_val(node):
    # Base: leaves have their own val
    if not node.children:
        return node.val
    # Recursively sum children's values
    node.val = sum(compute_total_val(child) for child in node.children)
    return node.val

compute_total_val(root)

# directories = []
# def dfs(node):
#     if not node:
#         return
#     if node.val < 100_000 and node.type == 'dir':
#         directories.append(node)
#     print("Node", node.name, ": with type", node.type, " and size ", node.val)  # Visit current node
#     for child in node.children:
#         dfs(child)

# dfs(root)
# sum_size = sum(d.val for d in directories)
# print(sum_size)

# Part 2
directories = []
def dfs(node):
    if not node:
        return
    directories.append(node)
    # print("Node", node.name, ": with type", node.type, " and size ", node.val)  # Visit current node
    for child in node.children:
        dfs(child)

dfs(root)

TOTAL_SPACE = 70_000_000
REQUIRED = 30_000_000
print(directories)
cur_space = TOTAL_SPACE - root.val
min_directory = TOTAL_SPACE
for d in directories:
    if cur_space + d.val >= REQUIRED:
        min_directory = min(d.val, min_directory)
print(min_directory)
