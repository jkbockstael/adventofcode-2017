# Advent of Code 2017 - Day 8 - I Heard You Like Registers
# http://adventofcode.com/2017/day/8

import sys

def run_program(source):
    registers = {}
    for line in source:
        registers = run_instruction(line, registers)
    return registers

def run_instruction(line, registers):
    tokens = line.rstrip().split(' ')
    register, operation, amount, _, guard, comp, value = tokens
    amount = int(amount)
    if register not in registers:
        registers[register] = 0
    if guard not in registers:
        registers[guard] = 0
    if eval(str(registers[guard]) + comp + value):
        if operation == 'inc':
            registers[register] += amount
        else:
            registers[register] -= amount
    return registers

def largest_register_value(registers):
    return max(registers.values())

if __name__ == '__main__':
    program = sys.stdin.readlines()
    print(largest_register_value(run_program(program)))
