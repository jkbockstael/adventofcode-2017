# Advent of Code 2017 - Day 1 - Inverse Captcha
# http://adventofcode.com/2017/day/1

import sys

def followed_digits(num):
    return [int(num[p]) for p in range(len(num) - 1, -1, -1) if num[p] == num[p - 1]]

num = sys.stdin.readline().strip()
print(sum(followed_digits(num)))
