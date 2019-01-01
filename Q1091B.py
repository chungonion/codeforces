import itertools
import random

num_input = int(input())
obelisk = []
clue = []
# permutations = perm([i for i in range(num_input)])
# print(permutations)
for i in range(0, num_input):
    x, y = list(map(int, input().split()))
    obelisk.append((x, y))

for i in range(0, num_input):
    x, y = list(map(int, input().split()))
    clue.append((x, y))


sum_x = 0
sum_y = 0
for i in range(0, num_input):
    sum_x += obelisk[i][0]+clue[i][0]
    sum_y += obelisk[i][1]+clue[i][1]

print("{:d} {:d}".format(sum_x//num_input, sum_y//num_input))
