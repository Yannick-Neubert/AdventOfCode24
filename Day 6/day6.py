#Task: https://adventofcode.com/2024/day/6
import numpy as np

with open("Day 6/input.txt", 'r') as file:
    input = file.read().strip().split('\n')

# split into 2d array
input = [[*row] for row in input]

# add padding
input = [['0'] * len(input[0])] + input + [['0'] * len(input[0])]
for i, line in enumerate(input):
    input[i] = ['0'] + line + ['0']

input = np.array(input)

# Part 1
# use tuples for position


visited = []
def check(input):
    pos = tuple([arr[0] for arr in np.where(input == '^')])
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    dir = 0

    def add(pos, dir):
        return (pos[0] + dy[dir], pos[1] + dx[dir])

    for i in range(1000):
        if pos not in visited: 
            visited.append(pos)

        input[pos] = 'X'

        ahead = add(pos, dir)
        if input[ahead] == '0': break
        if input[ahead] == '#':
            dir = (dir + 1) % 4

        pos = add(pos, dir)    
    return(len(visited))

print("Solution part 1: ", check(input))

# for row in input:
#     print(row)

# obstacle can't be placed at start
start, *visited = visited

for visit in visited:
    input[visit] = '#'
    break