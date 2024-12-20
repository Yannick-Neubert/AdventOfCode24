#Task: https://adventofcode.com/2024/day/2
import numpy as np

with open("Day 2/input.txt", 'r') as file:
    input = [np.fromstring(line, sep=" ", dtype='int64') for line in file]

# One-Liners P1 and P2:
print("P1: ", len([x for x in [[y-x for x, y in zip(line, line[1:])] for line in input] if min(x) >=1 and max(x) <= 3 or max(x) <= -1 and min(x) >= -3]))
print("P2: ", len([line for line in input if any(map(lambda x: min(x) >=1 and max(x) <= 3 or max(x) <= -1 and min(x) >= -3, map(lambda removed: [y-x for x, y in zip(removed, removed[1:])], [np.delete(line, i) for i in range(len(line))])))]))

# Part 1
# generate differences by pairing each row with itself shifted by one 
diffs = [[y-x for x, y in zip(line, line[1:])] for line in input]

def safety_check(line):
    if min(line) >= 1 and max(line) <= 3:
        return True
    if max(line) <= -1 and min(line) >= -3:
        return True
    return False

# count and separate safe lines
safe = 0
unsafe = []

for line in diffs:
    if safety_check(line): safe += 1 
    else: 
        unsafe.append(line)

print("Solution part 1: ", safe)

# Part 2
for line in unsafe:
    # remove ends
    if safety_check(line[1:]):
        safe += 1
        continue
    if safety_check(line[:-1]):
        safe += 1
        continue

    # remove middles by adding diff to left item
    for i in range(1, len(line)):
        dampened = line.copy()
        removed = line[i]
        dampened[i-1] += removed
        del dampened[i]
        if safety_check(dampened):
            safe += 1
            break

print("Solution part 2: ", safe)