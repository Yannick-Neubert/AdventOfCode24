#Task: https://adventofcode.com/2024/day/1
import numpy as np

input = np.loadtxt("Day 1/input.txt", dtype='int64')

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