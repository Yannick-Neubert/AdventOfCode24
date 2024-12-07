#Task: https://adventofcode.com/2024/day/6
import numpy as np
from tqdm import tqdm

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
visited = []

# O(n*m) possible using graphs
# returns #places visited or -1 if there's a loop
def check(input):
    seen = []
    pos = tuple([arr[0] for arr in np.where(input == '^')])
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    dir = 0

    def add(pos, dir):
        return (pos[0] + dy[dir], pos[1] + dx[dir])

    # step by step simulation
    while True:
        if pos not in visited: 
            visited.append(pos)

        ahead = add(pos, dir)
        if input[ahead] == '0': break
        if input[ahead] == '#':
            pair = (*ahead, dir)
            dir = (dir + 1) % 4
            if pair in seen:
                return -1
            seen.append(pair)

            # may need to turn twice
            ahead = add(pos, dir)
            if input[ahead] == '#':
                dir = (dir + 1) % 4
            
        pos = add(pos, dir)    
    return(len(visited))

print("Solution part 1: ", check(input))

# Part 2
# obstacle can't be placed at start
start, *visits = visited
loops = 0

# Optimizable by starting from further into the simulation
for visit in tqdm(visits):
    input[visit] = '#'
    if check(input) == -1:
        loops += 1
    input[visit] = '.'
print("Solution part 2: ", loops)