# Advent of Code 2017 - Day 6 - Memory Reallocation
# http://adventofcode.com/2017/day/6

import re

def reallocate(memory):
    cell = memory.index(max(memory))
    value = memory[cell]
    memory[cell] = 0
    while value > 0:
        cell = (cell + 1) % len(memory)
        memory[cell] = memory[cell] + 1
        value = value - 1
    return memory

def reallocate_until_cycle(memory):
    steps = 0
    visited = []
    while memory not in visited:
        visited.append(memory)
        memory = reallocate(memory[:])
        steps = steps + 1
    return steps, memory

if __name__ == '__main__':
    memory = [int(x) for x in re.split('\s+', input())]
    steps, _ = reallocate_until_cycle(memory)
    print(steps)
