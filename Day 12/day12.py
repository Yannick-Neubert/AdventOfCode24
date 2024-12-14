import numpy as np
from collections import deque

with open("Day 12/input.txt") as file:
    input = np.array([[*line] for line in file.read().strip().split("\n")])

visited = np.zeros(input.shape)

print(input)

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def neighbours(i, j):
    next = []
    for k in range(len(dx)):
        adjacent = (i + dy[k], j + dx[k])
        if adjacent[0] < 0 or adjacent[0] >= input.shape[0] or adjacent[1] < 0 or adjacent[1] >= input.shape[1]:
            continue
        if input[adjacent] != input[i, j]:
            continue

        next.append(adjacent)
    return next

def traverse(i, j):
    if visited[i, j]:
        return 0, 0
    
    visited[i, j] = 1
    adjacent = neighbours(i, j)

    next = [x for x in adjacent if not visited[x]]
    buffer = [0, 0]
    for x in next:
        res = traverse(*x)
        buffer[0] += res[0]
        buffer[1] += res[1]
    ret = buffer[0] + 1, buffer[1] + 4 - len(adjacent)
    return ret

total = 0
for i in range(input.shape[0]):
    for j in range(input.shape[1]):
        if visited[i, j]:
            continue
        ret = traverse(i, j)
        total += ret[0] * ret[1]

print("Solution part 1: ", total)