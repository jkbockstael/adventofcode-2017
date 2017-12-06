# Advent of Code 2017 - Day 4 - High-Entropy Passphrases - Part 2
# http://adventofcode.com/2017/day/4

from day04_part1 import *

def letters(word):
    return ''.join(sorted(word))

def valid(words):
    return unique(list(map(letters, words)))

passphrases = sys.stdin.readlines()
print(len(list(filter(valid, map(words(' '), passphrases)))))
