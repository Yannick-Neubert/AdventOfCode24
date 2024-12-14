import numpy as np
from collections import deque

with open("Day 12/input.txt") as file:
    input = np.array([[*line] for line in file.read().strip().split("\n")])

input = np.pad(input, pad_width=1, mode="constant", constant_values='.')

visited = np.zeros(input.shape)

print(input)

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

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

def traverse(i, j, return_Edges = False):
    if visited[i, j]:
        return 0, 0
    
    visited[i, j] = 1

    adjacent = neighbours(i, j, return_Edges)
    # print(adjacent)
    edges = []
    if return_Edges:
        edges = adjacent[1]
        adjacent = adjacent[0]

    # print(i,j,edges,adjacent)

    # print(edges)
    next = [x for x in adjacent if not visited[x]]
    buffer = [0, 0, []] if return_Edges else [0, 0]
    for x in next:
        res = traverse(*x, return_Edges)
        buffer[0] += res[0]
        buffer[1] += res[1]
        if return_Edges:
            buffer[2] += res[2]
    if return_Edges:
        return buffer[0] + 1, buffer[1] + 4 - len(adjacent), buffer[2] + edges
    else:
        return buffer[0] + 1, buffer[1] + 4 - len(adjacent),


total = 0
for i in range(1, input.shape[0]-1):
    for j in range(1, input.shape[1]-1):
        if visited[i, j]:
            continue
        ret = traverse(i, j)
        total += ret[0] * ret[1]

print("Solution part 1: ", total)


visited = np.zeros(input.shape)

# print(neighbours(1, 1, True))
print(traverse(1, 1, return_Edges=True))
