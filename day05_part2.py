# Advent of Code 2017 - Day 5 - A Maze of Twisty Trampolines, All Alike - Part 2
# http://adventofcode.com/2017/day/5

import sys
from day05_part1 import run

def change_jump(jump):
    return jump -1 if jump >= 3 else jump +1

program = map(int, sys.stdin.readlines())
print(run(change_jump, program))
