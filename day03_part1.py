# Advent of Code 2017 - Day 3 - Spiral Memory
# http://adventofcode.com/2017/day/3

import sys
import math

# n such as n^2 < cell and (n+2)^2 >= x
def previous_corner_root(cell):
    n = 3
    while ((n + 2)**2 < cell) or (n**2 >= cell):
        n = n + 2
    return n
    
def manhattan_distance(cell):
    if cell == 1:
        return 0
    if cell < 10:
        return (cell % 2) + 1
    else:
        # Between two corners the distances are a periodic symmetric
        # sequence based on the root of that corner's number:
        # n = 3: [4,3,2,3,4, ...]
        # n = 5: [6,5,4,3,4,5,6, ...]
        # n = 7: [8,7,6,5,4,5,6,7,8, ...]
        # ...
        n = previous_corner_root(cell)
        offset = (cell - n**2) % (n + 1)
        if offset < n // 2 + 1:
            return n + 1 - offset
        else:
            return offset

print(manhattan_distance(int(sys.stdin.readline())))
