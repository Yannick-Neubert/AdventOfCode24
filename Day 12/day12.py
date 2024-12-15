#Task: https://adventofcode.com/2024/day/12
import numpy as np
from collections import deque

with open("Day 12/input.txt") as file:
    input = np.array([[*line] for line in file.read().strip().split("\n")])

input = np.pad(input, pad_width=1, mode="constant", constant_values='.')

# Part 1
visited = np.zeros(input.shape)

# directions
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# get adjacent cells of same type and borders
def neighbours(i, j, return_Edges = False):
    next = []
    edges = []
    for k in range(len(dx)):
        adjacent = (i + dy[k], j + dx[k])
        if adjacent[0] < 0 or adjacent[0] >= input.shape[0] or adjacent[1] < 0 or adjacent[1] >= input.shape[1]:
            continue
        if input[adjacent] != input[i, j]:
            edges.append((i, j, k))
            continue

        next.append(adjacent)
    if return_Edges:
        return next, edges
    return next

# traverse a field and return area, perimeter, borders
def traverse(i, j, return_edges = False):
    if visited[i, j]:
        return 0, 0, [] if return_edges else 0, 0
    
    visited[i, j] = 1

    adjacent = neighbours(i, j, return_edges)
    edges = []
    if return_edges:
        edges = adjacent[1]
        adjacent = adjacent[0]

    next = [x for x in adjacent if not visited[x]]
    buffer = [0, 0, []] if return_edges else [0, 0]
    for x in next:
        res = traverse(*x, return_edges)
        buffer[0] += res[0]
        buffer[1] += res[1]
        if return_edges:
            buffer[2] += res[2]
    if return_edges:
        return buffer[0] + 1, buffer[1] + 4 - len(adjacent), buffer[2] + edges
    else:
        return buffer[0] + 1, buffer[1] + 4 - len(adjacent),

# traverse each field
total = 0
for i in range(1, input.shape[0]-1):
    for j in range(1, input.shape[1]-1):
        if visited[i, j]:
            continue
        ret = traverse(i, j)
        total += ret[0] * ret[1]

print("Solution part 1: ", total)

# Part 2
# number of sides = number of corners
# a horizontal side is a corner if theres no horizontal edge left/right of it
# all corners have a horizontal edge
def count_corners(edges):
    corners = 0 
    for edge in sorted(edges):
        if (edge[0], edge[1] + 1) not in edges:
            corners += 1
        if (edge[0], edge[1] - 1) not in edges:
            corners += 1
    return corners

visited = np.zeros(input.shape)

# top and bottom edges need to be counted seperately
total = 0
for i in range(1, input.shape[0]-1):
    for j in range(1, input.shape[1]-1):
        if visited[i, j]:
            continue
        ret = traverse(i, j, return_edges=True)
        edges = ret[2]
        top_edges = [(edge[0], edge[1]) for edge in edges if edge[2] == 0]
        bottom_edges = [(edge[0], edge[1]) for edge in edges if edge[2] == 2]

        total += ret[0] * (count_corners(top_edges) + count_corners(bottom_edges))

print("Solution part 2: ", total)