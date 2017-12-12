# Advent of Code 2017 - Day 8 - I Heard You Like Registers - Part 2
# http://adventofcode.com/2017/day/8

import sys
from day08_part1 import run_instruction

def run_program(source):
    registers = {}
    largest_value = 0
    for line in source:
        registers = run_instruction(line, registers)
        largest_value = max(largest_value, max(registers.values()))
    return largest_value

program = sys.stdin.readlines()
print(run_program(program))
