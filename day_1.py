# path = 'inputs/test_input/day1_test_input.txt'
path = 'inputs/day1_input.txt'

inventory = []
with open(path) as f:
    x = []
    for line in f:
        cal = line.strip()
        if cal != '':
            x.append(int(cal))
        else:
            inventory.append(x)
            x = []
    if x:
        inventory.append(x)

leaderboard = [0,0,0]
for i in inventory:
    if sum(i) > leaderboard[0]:
        leaderboard[2] = leaderboard[1]
        leaderboard[1] = leaderboard[0]
        leaderboard[0] = sum(i)
    elif sum(i) > leaderboard[1]:
        leaderboard[2] = leaderboard[1]
        leaderboard[1] = sum(i)
    elif sum(i) > leaderboard[2]:
        leaderboard[2] = sum(i)

print(sum(leaderboard))
