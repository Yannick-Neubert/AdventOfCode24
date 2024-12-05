#Task: https://adventofcode.com/2024/day/3
import re

with open("Day 3/input.txt", 'r') as file:
    input = file.read()

# One-Liners P1 and P2:
print("P1: ", sum(list(map(lambda x: int(x[0]) * int(x[1]), [mult[4:-1].split(',') for mult in re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", re.sub("\n", "", input))]))))
print("P2: ", sum(list(map(lambda x: int(x[0]) * int(x[1]), [mult[4:-1].split(',') for mult in re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", re.sub("don't\(\).*?[do\(\)|$]", "", re.sub("\n", "", input)))]))))

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