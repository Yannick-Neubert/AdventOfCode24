#Task: https://adventofcode.com/2024/day/7

import time
start_time = time.time()

with open("Day 7/input.txt", 'r') as file:
    input = file.read().strip().split('\n')

def parse(row):
    res, nums = row.split(':')
    return [int(res)] + [int(num) for num in nums.split()]

input = [parse(row) for row in input]

#-------------------------------------------------------------------------------------------------#
# Part 1 - check Part 2 for comments
def try_opsP1(res, nums):
    # shorthand for (num a X num b) X num c where X is one of + *
    a, b, c = nums[0], nums[1], nums[-1]

    # base case
    if len(nums) == 2:
        if a * b == res or a + b == res:
            return res
        return 0
    
    elif res % c == 0:
        if c * try_opsP1(int(res/c), nums[:-1]) == res or c + try_opsP1(res-c, nums[:-1]) == res:
            return res
    else:
        if c + try_opsP1(res-c, nums[:-1]) == res:
            return res
    return 0

sum = 0
for equation in input:
    if try_opsP1(equation[0], equation[1:]) == equation[0]:
        sum += equation[0]
        
print("Solution part 1: ", sum)
#-------------------------------------------------------------------------------------------------#

# Part 2:
# recursively try operators from right to left
# while checking divisibility (reverse mult) and seperatability (reverse concat) as shortcuts
# res acts as reverse accumulator, getting reduced each step
def try_ops(res, nums):
    # shorthand for (num a X num b) X num c where X is one of + * ||
    a, b, c = nums[0], nums[1], nums[-1]

    # base case
    if len(nums) == 2:
        if a * b == res or a + b == res or int(str(a) + str(b)) == res:
            return res
        return 0
    
    # check divisibility AND seperatability
    # in this case we'd need to test all three operators
    if res % c == 0 and str(res)[-len(str(c)):] == str(c):
        if c * try_ops(int(res/c), nums[:-1]) == res or c + try_ops(res-c, nums[:-1]) == res or int(str(try_ops(int(str(res)[:-len(str(c))]), nums[:-1])) + str(c)) == res:
            return res
    # check if only one is true
    # only need to check 2 operators
    elif str(res)[-len(str(c)):] == str(c):
        if c + try_ops(res-c, nums[:-1]) == res or int(str(try_ops(int(str(res)[:-len(str(c))]), nums[:-1])) + str(c)) == res:
            return res
    # these two are all that's necessary for part 1
    elif res % c == 0:
        if c * try_ops(int(res/c), nums[:-1]) == res or c + try_ops(res-c, nums[:-1]) == res:
            return res
    # if none are true, we only need to check summation
    else:
        if c + try_ops(res-c, nums[:-1]) == res:
            return res
    return 0

sum = 0
for equation in input:
    if try_ops(equation[0], equation[1:]) == equation[0]:
        sum += equation[0]

print("Solution part 2: ", sum)