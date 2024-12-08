#Task: https://adventofcode.com/2024/day/8
import numpy as np

with open("Day 8/input.txt") as file:
    input = np.array([[*line] for line in file.read().strip().split("\n")])

antennas = {x: np.where(input == x) for x in input.ravel() if x != '.'}

# generates all pairs of positions
def generate_pairs(positions):
    positions = list(zip(*positions))
    # pair each element with the remaining, skip last (none remaining)
    pairs = [(x,y) for i,x in enumerate(positions) if i < len(positions) - 1 for y in positions[i + 1:]]
    return pairs

pairs = [generate_pairs(v) for v in antennas.values()]
pairs = [x for xs in pairs for x in xs] # flatten list

# checks if a position is out of bounds
def out_of_bounds(pos):
    if pos[0] < 0 or pos[0] >= input.shape[0] or pos[1] < 0 or pos[1] >= input.shape[1]:
        return True
    return False

# place antinodes
for pair in pairs:
    dy = pair[1][0] - pair[0][0]
    dx = pair[1][1] - pair[0][1]

    if dy % 3 == 0 and dx % 3 == 0:
        pass # never happens but valid in theory
    
    # for part 1: fix m = 1
    m = 0
    while True: 
        p1 = (pair[1][0] + m*dy, pair[1][1] + m*dx)
        if out_of_bounds(p1): 
            break
        input[p1] = '#'
        m += 1

    m = 0
    while True:
        p2 = (pair[0][0] - m*dy, pair[0][1] - m*dx)
        if out_of_bounds(p2): 
            break
        input[p2] = '#'
        m += 1

print(input)
print(len(np.where(input == '#')[0]))