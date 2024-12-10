#Task: https://adventofcode.com/2024/day/9
from itertools import count

with open("Day 9/input.txt") as file:
    input = file.read().strip()

# Part 1
# map storage as [id, ..., id, '.', ..., '.']
counter = count(0)
disk = [[next(counter)]*int(x) if i % 2 == 1 else ['.'] * int(x) for i,x in enumerate(input, 1)]
disk = [x for x in disk if x != []]
disk = [x for xs in disk for x in xs]

# get all files on disk
files = [x for x in disk if x != '.']

# defrag storage and generate checksum
compact = [files.pop(0) if x != '.' else files.pop(-1) for x in disk if files]
res = sum([x*i for i,x in enumerate(compact)])
print("Solution part 1: ", res)

# Part 2
# map storage as [[start pos, length of segment, id], ...,  [...]]
pos = 0
id = count(0)
disk = [[(pos := pos + int(x)) - int(x), int(x), next(id)] if i % 2 == 1 else [(pos := pos + int(x)) - int(x), int(x), '.'] for i,x in enumerate(input, 1)]
disk = [x for x in disk if x[1] > 0]

# get all files on disk
files = [x for x in disk if x[2] != '.']

# defrag storage
compact = disk.copy()
for file in reversed(disk):
    if file[2] == '.':
        continue

    # find next free space
    i, space = next(((i, x) for i, x in enumerate(compact) if x[2] == '.' and x[1] >= file[1]), (None, None))
    if space:
        if space[0] > file[0]:
            # no space to the left
            if files: files.pop(-1)
            continue
        if space[1] == file[1]:
            # file fits exactly
            compact[i][2], file[2] = file[2], '.' 
        else:
            # more space than needed
            compact.insert(i + 1, [space[0] + file[1], space[1] - file[1], '.'])
            compact[i], file[2] = [space[0], file[1], file[2]], '.'
    if files: files.pop(-1)

# generate checksum
compact = [x for xs in [[x[2]]*x[1] for x in compact] for x in xs]
res = sum([x*i if x != '.' else 0 for i,x in enumerate(compact)])
print("Solution Part 2: ", res)