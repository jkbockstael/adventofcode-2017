# Advent of Code 2017 - Day 2 - Corruption Checksum
# http://adventofcode.com/2017/day/2

import sys
import re

def parse_input(lines):
    return [parse_line(line) for line in lines]

def parse_line(line):
    return [int(x) for x in re.split('\s', line.rstrip())]

def checksum(rows):
    return sum([max(row) - min(row) for row in rows])

if __name__ == '__main__':
    rows = parse_input(sys.stdin.readlines())
    print(checksum(rows))
