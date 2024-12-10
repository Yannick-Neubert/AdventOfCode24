#Task: https://adventofcode.com/2024/day/10
import numpy as np

with open("Day 10/input.txt") as file:
    input = file.read().strip().split('\n')

# split into 2d array
input = np.array([[int(x) for x in row] for row in input])

# Part 1 and 2
# get all start positions as tuples
zeros = list(zip(*np.where(input == 0)))
scoresP1 = np.zeros(len(zeros), dtype='int')
scoresP2 = np.zeros(len(zeros), dtype='int')

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# simple depth first search
# no need to keep track of visited nodes as we can only go upwards
def valid_neighbours(v):
    next = []
    for k in range(len(dx)):
        adjacent = ((v[0] + dy[k], v[1] + dx[k]))
        if adjacent[0] < 0 or adjacent[0] >= input.shape[0] or adjacent[1] < 0 or adjacent[1] >= input.shape[1]:
            continue
        if input[adjacent] - input[v] != 1:
            continue

        next.append(adjacent)
    return next

def DFS(v, nines):
    if input[v] == 9:
        nines.append(v)
    for next in valid_neighbours(v):
        DFS(next, nines)

# DFS from all start points
for id, start in enumerate(zeros):
    nines = []
    DFS(start, nines)
    scoresP1[id] = len(set(nines))
    scoresP2[id] = len(nines)

print("Solution Part 1: ", sum(scoresP1))
print("Solution Part 2: ", sum(scoresP2))