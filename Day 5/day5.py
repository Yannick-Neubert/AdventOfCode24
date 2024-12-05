#Task: https://adventofcode.com/2024/day/5
import numpy as np
from functools import cmp_to_key

with open("Day 5/input.txt", 'r') as file:
    rules, updates = file.read().strip().split("\n\n")

# format data into lists like
# rules: [x, y] for X|Y
# updates [x, .., z] for X, .., Z
rules = rules.split("\n")
updates = updates.split("\n")

rules = [[int(x) for x in rule.split("|")] for rule in rules]
updates = [[int(x) for x in update.split(",")] for update in updates]

# Part 1
# check if every page obeys the rules
def valid(update):
    for i, elem in enumerate(update):
        ruleset = [rule for rule in rules if elem in rule]
        if not check_pos(set(update[:i]), elem, set(update[i+1:]), ruleset):
            return False
    return True

# check if a single page obeys its set of rules
def check_pos(pre, elem, post, ruleset):
    preset = {rule[0] for rule in ruleset if rule[1] == elem}
    postset = {rule[1] for rule in ruleset if rule[0] == elem}
    return pre.isdisjoint(postset) and post.isdisjoint(preset)

sum = 0
incorrect = []
for update in updates:
    # equivalent as per part 2:
    # if update == sorted(update, key=cmp_to_key(lambda x, y: -1 if [x, y] in rules else 1)):
    if valid(update): 
        sum += update[int((len(update) - 1)/2)]
    else:
        incorrect.append(update)

print("Solution part 1: ", sum)

# Part 2
sum = 0
for update in incorrect:
    # sort lists according to provided rules
    update = sorted(update, key=cmp_to_key(lambda x, y: -1 if [x, y] in rules else 1))
    if valid(update):
        sum += update[int((len(update) - 1)/2)]

print("Solution part 2: ", sum)