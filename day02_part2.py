# Advent of Code 2017 - Day 2 - Corruption Checksum - Part 2
# http://adventofcode.com/2017/day/2

import sys
import math
from day02_part1 import parse_line, parse_input

def even_division(nums):
    nums = sorted(nums)
    for i in range(len(nums)):
        a = nums[i]
        for b in nums[i + 1:]:
            # The problem statement guarantees that this will happen
            if a == math.gcd(a, b):
                return b // a
    
def checksum(rows):
    return sum([even_division(row) for row in rows])

rows = parse_input(sys.stdin.readlines())
print(checksum(rows))
