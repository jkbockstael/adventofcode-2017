# Advent of Code 2017 - Day 9 - Stream Processing
# http://adventofcode.com/2017/day/9

def stream_score(line):
    score = 0
    depth = 0
    in_garbage = False
    skip_char = False
    for char in line:
        if not in_garbage:
            if char == '{':
                depth = depth + 1
            elif char == '}':
                score = score + depth
                depth = depth - 1
            elif char == '<':
                in_garbage = True
        else:
            if skip_char:
                skip_char = False
            elif char == '!':
                skip_char = True
            elif char == '>':
                in_garbage = False
    return score

print(stream_score(input()))
