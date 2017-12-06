# Advent of Code 2017 - Day 5 - A Maze of Twisty Trampolines, All Alike
# http://adventofcode.com/2017/day/5

import sys

def run(change_jump, program):
    steps = 0
    pc = 0
    while pc >= 0 and pc < len(program):
        target = pc + program[pc]
        program[pc] = change_jump(program[pc])
        pc = target
        steps = steps + 1
    return steps

def change_jump(jump):
    return jump + 1

if __name__ == '__main__':
    program = map(int, sys.stdin.readlines())
    print(run(change_jump, program))
