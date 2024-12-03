#Task: https://adventofcode.com/2024/day/3
import re

with open("Day 3/input.txt", 'r') as file:
    input = file.read()

# remove any linebreaks
input = re.sub("\n", "", input)

# Part 1
def eval(string):
    # extract numbers and multiply
    def multiply(string):
        numbers = string[4:-1].split(',')
        return int(numbers[0]) * int(numbers[1])

    # extract mults
    mults = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", string)

    sum = 0
    for mult in mults:
        sum += multiply(mult)
    return sum

print("Solution part 1: ", eval(input))

# Part 2
# delete all sequences between don'ts and dos or end of string
dos = re.sub("don't\(\).*?[do\(\)|$]", "", input)

print("Solution part 2: ", eval(dos))