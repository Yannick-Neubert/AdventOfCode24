#Task: https://adventofcode.com/2024/day/14
import numpy as np
from tqdm import tqdm
import re

pattern = r"(-?\d+)"
WIDTH = 101
HEIGTH = 103

with open("Day 14/input.txt") as file:
    input = [list(map(int, re.findall(pattern, line))) for line in file]

# Part 1
# numpy has y before x, so indices ned to be swapped
positions = np.array([(line[1], line[0]) for line in input])
velocities = np.array([(line[3], line[2]) for line in input])

# calculates the new position after n steps
def add(position, velocity, n):
    return np.array([(position[0] + velocity[0] * n) % HEIGTH, (position[1] + velocity[1] * n) % WIDTH])

# calculates all new positions after n steps
def timestep(positions, velocities, n):
    return np.array([add(pos, vel, n) for pos, vel in zip(positions, velocities)])

# calculates the safety factor
def safety_factor(map):
    x_mid = WIDTH // 2
    y_mid = HEIGTH// 2
    
    top_left = map[:y_mid, :x_mid]
    top_right = map[:y_mid, x_mid + 1:]
    bottom_left = map[y_mid + 1:, :x_mid]
    bottom_right = map[y_mid + 1:, x_mid + 1:]

    return int(np.sum(top_left) * np.sum(top_right) * np.sum(bottom_left) * np.sum(bottom_right))

# fast forward 100 steps, count robots
new_positions = timestep(positions, velocities, 100)
map = np.zeros([HEIGTH, WIDTH])
np.add.at(map, (new_positions[:, 0], new_positions[:, 1]), 1)

print("Solution part 1: ", safety_factor(map))

# Part 2
# easier to use than arrays for this method
def map_to_str(map):
    return '\n'.join(''.join('#' if x != 0 else '.' for x in row) for row in map)

# optional: fast forward to a point in time
start = 7000
positions = timestep(positions, velocities, start)

# this is incredibly stupid but it works
# simulate until the tree pattern is found
# other fun min/max/outlier approaches include:
# minimizing entropy or variance or file size with compression
# flood fills, connected components, robot pairs
# fourier transform, orientation, safety factor
tree = '############'
while True:
    start += 1
    positions = timestep(positions, velocities, 1)
    map = np.zeros([HEIGTH, WIDTH])
    np.add.at(map, (positions[:, 0], positions[:, 1]), 1)
    if tree in map_to_str(map):
        break

print("Solution part 2: ", start)