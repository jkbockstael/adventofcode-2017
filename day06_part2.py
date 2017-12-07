# Advent of Code 2017 - Day 6 - Memory Reallocation - Part 2
# http://adventofcode.com/2017/day/6

import re
from day06_part1 import reallocate, reallocate_until_cycle

def cycle_length(memory):
    initial = memory[:]
    steps = 0
    while True:
        memory = reallocate(memory[:])
        steps = steps + 1
        # this is guaranteed to happen
        if memory == initial:
            return steps

memory = [int(x) for x in re.split('\s+', input())]
_, memory = reallocate_until_cycle(memory)
print(cycle_length(memory))
