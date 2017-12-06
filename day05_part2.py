# Advent of Code 2017 - Day 5 - A Maze of Twisty Trampolines, All Alike - Part 2
# http://adventofcode.com/2017/day/5

import sys

def run(program):
    steps = 0
    pc = 0
    while pc >= 0 and pc < len(program):
        target = pc + program[pc]
        program[pc] += -1 if program[pc] >= 3 else 1
        pc = target
        steps = steps + 1
    return steps

program = map(int, sys.stdin.readlines())
print(run(program))
