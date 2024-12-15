#Task: https://adventofcode.com/2024/day/11
from functools import cache

with open("Day 11/input.txt") as file:
    input = file.readline().split()

input = [int(x) for x in input]

# Part 1 and 2
# apply blink rules to a single number n times
@cache
def blink(x, n):
    if n == 0:
        return 1
    if x == 0:
        return blink(1, n-1)
    elif len(str(x)) % 2 == 0:
        return blink(int(str(x)[:len(str(x))//2]), n-1) + blink(int(str(x)[len(str(x))//2:]), n-1)
    else:
       return blink(x * 2024, n-1)

# apply blink rules to all numbers
def cached_blink(input, n):
    return sum([blink(x, n) for x in input])

print("Solution part 1: ", cached_blink(input, 25))
print("Solution part 2: ", cached_blink(input, 75))