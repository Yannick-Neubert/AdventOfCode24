import numpy as np
import re
import math

with open("Day 13/input.txt") as file:
    input = file.readlines()
    
input = [input[i:i+3] for i in range(0, len(input), 4)] 
pattern = r"X[+=](\d+), Y[+=](\d+)"

# Part 1 and 2
# solve the linear system with integers
# can be refactored as direct calculation since it's only a 2x2 matrix
# pressesA = (bx*y - by*x) / (bx*ay - by*ax)
# pressesB = (x-ax*A) / bx
# where ax, ay, bx, by, x, y = map(int, re.findall(r'(\d+)', machine))
def optimal_tokens(SHIFT=0):
    tokens = 0
    for slot in input:
        buttonA = [int(num) for num in re.search(pattern, slot[0].strip()).groups()]
        buttonB = [int(num) for num in re.search(pattern, slot[1].strip()).groups()]
        prize = [int(num) + SHIFT for num in re.search(pattern, slot[2].strip()).groups()]

        A = np.array([buttonA, buttonB]).T
        pressesA, pressesB = (np.linalg.solve(A, prize))
        
        # check if integer solvable
        if sum(abs(np.dot(A, [round(pressesA), round(pressesB)]) - prize)) < 1e-9:
                tokens += 3 * round(pressesA) + round(pressesB)
    return tokens

SHIFT = 10000000000000
print("Solution part 1: ", optimal_tokens())
print("Solution part 2: ", optimal_tokens(SHIFT))