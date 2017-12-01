# Advent of Code 2017 - Day 1 - Inverse Captcha
# http://adventofcode.com/2017/day/1

import sys

def followed_digits(num, delta):
    return [int(num[p]) for p in range(len(num) - 1, -1, -1) if num[p] == num[p - delta]]

def part1(num):
    return sum(followed_digits(num, 1))

if __name__ == '__main__':
    num = sys.stdin.readline().strip()
    print(part1(num))
