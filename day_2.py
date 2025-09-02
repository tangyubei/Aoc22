import logging

# path = 'inputs/test_input/day2_test_input.txt'
path = 'inputs/day2_input.txt'

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

games = []
with open(path) as f:
    for line in f:
        games.append(line.strip().split(' '))

# Part 1
# def get_points_from_game(opponent, you):
#     if (opponent, you) in [("paper", "rock"), ("scissor", "paper"), ("rock", "scissor")]:
#         return 0
#     elif (opponent, you) in [("rock", "paper"), ("paper", "scissor"), ("scissor", "rock")]:
#         return 6
#     else:
#         return 3
#
# symbols = {'X': 'rock', 'Y': 'paper', 'Z': 'scissor', 'A': 'rock', 'B': 'paper', 'C': 'scissor'}
#
# total = 0
# for game in games:
#     o = symbols[game[0]]
#     print(o)
#     u = symbols[game[1]]
#     print(u)
#     p = get_points_from_game(o, u)
#     if u == 'rock':
#         p += 1
#     elif u == 'paper':
#         p += 2
#     else:
#         p += 3
#     total += p
# print(total)

# Part 2
# A = Rock, B = Paper, C = Scissor
# X = Lose, Y = Draw, Z = Win
outcome_scores = {'X': 0, 'Y': 3, 'Z': 6}
shape_scores = {'rock': 1, 'paper': 2, 'scissor': 3}
mapping = {'A': {'X': 'scissor', 'Y': 'rock', 'Z': 'paper'},
           'B': {'X': 'rock', 'Y': 'paper', 'Z': 'scissor'},
           'C': {'X': 'paper', 'Y': 'scissor', 'Z': 'rock'}}
total = 0
for game in games:
    outcome = game[1]
    opp = game[0]
    your_shape = mapping[opp][outcome]
    p = outcome_scores[outcome] + shape_scores[your_shape]
    total += p
print(total)

