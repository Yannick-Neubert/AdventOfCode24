#Task: https://adventofcode.com/2024/day/9
from itertools import count

with open("Day 9/input.txt") as file:
    input = file.read().strip()

counter = count(0)
disk = [[next(counter)]*int(x) if i % 2 == 1 else ['.'] * int(x) for i,x in enumerate(input, 1)]
disk = [x for x in disk if x != []]
disk = [x for xs in disk for x in xs]
files = [x for x in disk if x != '.']

compact = [files.pop(0) if x != '.' else files.pop(-1) for x in disk if files]

sum = sum([x*i for i,x in enumerate(compact)])

# print(disk)
# print(files)
# print(compact)
print(sum)