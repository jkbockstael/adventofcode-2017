# Advent of Code 2017 - Day 1 - Inverse Captcha - Part 2
# http://adventofcode.com/2017/day/1

import sys
from day01_part1 import followed_digits

def part2(num):
    return sum(followed_digits(num, len(num) // 2))

num = sys.stdin.readline().strip()
print(part2(num))
