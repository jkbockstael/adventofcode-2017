# Advent of Code 2017 - Day 4 - High-Entropy Passphrases
# http://adventofcode.com/2017/day/4

import sys

def words(separator):
    def words_inner(line):
        return line.rstrip().split(separator)
    return words_inner

def unique(words):
    return len(words) == len(set(words))

if __name__ == '__main__':
    passphrases = sys.stdin.readlines()
    print(len(list(filter(unique, map(words(' '), passphrases)))))
