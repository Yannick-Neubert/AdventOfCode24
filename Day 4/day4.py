#Task: https://adventofcode.com/2024/day/4

input = []
with open("Day 4/input.txt", 'r') as file:
    for line in file:
        input.append(line.strip())

# Part 1
# add padding
input = ['.' * len(input[0])] + input + ['.' * len(input[0])]
for i, line in enumerate(input):
    input[i] = '.' + line + '.'

found = 0
# no need to check padding
for i in range(1, len(input[0]) - 1):
    for j in range(1, len(input) - 1):
        # check all directions starting from X
        dx = [0, 1, 1, 1, 0, -1, -1, -1]
        dy = [-1, -1, 0, 1, 1, 1, 0, -1]

        if input[i][j] == 'X':
            for k in range(len(dx)):
                if input[i+dy[k]][j+dx[k]] != 'M': continue
                if input[i+2*dy[k]][j+2*dx[k]] != 'A': continue
                if input[i+3*dy[k]][j+3*dx[k]] != 'S': continue
                found += 1

print("Solution part 1: ", found)

found = 0
# no need to check padding
for i in range(1, len(input[0]) - 1):
    for j in range(1, len(input) - 1):
        # check corners starting from A
        dx = [-1, 1, 1, -1]
        dy = [-1, -1, 1, 1]

        if input[i][j] == 'A':
            # count letters
            ms = 0
            ss = 0
            for k in range(len(dx)):
                if input[i+dy[k]][j+dx[k]] == 'M': ms += 1
                elif input[i+dy[k]][j+dx[k]] == 'S': ss += 1
            
            # needs two have two of both
            if ms == 2 and ss == 2:
                # same letter may not be diagonal
                if input[i-1][j-1] != input[i+1][j+1]:
                    found += 1

print("Solution part 2: ", found)