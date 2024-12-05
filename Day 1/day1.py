#Task: https://adventofcode.com/2024/day/1
import numpy as np

input = np.loadtxt("Day 1/input.txt", dtype='int64')

# One-Liners P1 and P2:
print("P1: ", np.sum(abs(np.sort(input, axis=0)[:, 0] - np.sort(input, axis=0)[:, 1])))
print("P2: ", sum([l * list(input[:, 1]).count(l) for l in input[:, 0]]))

# Part 1
sorted = np.sort(input, axis=0)
diffs = abs(sorted[:, 0] - sorted[:, 1])
diff = np.sum(diffs)
print("Solution part 1: ", diff)

# Part 2
left, right = sorted[:, 0], sorted[:, 1]
unique, counts = np.unique(right, return_counts=True)

sum = 0
for l in left:
    count = counts[np.where(unique == l)]
    sum += l * count[0] if count.size != 0 else 0

print("Solution part 2: ", sum)