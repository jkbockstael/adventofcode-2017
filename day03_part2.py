# Advent of Code 2017 - Day 3 - Spiral Memory - Part 2
# http://adventofcode.com/2017/day/3

def filled_neighbours(cells, position):
    x, y = position
    neighbours = []
    for i in [x - 1, x, x + 1]:
        for j in [y - 1, y, y + 1]:
            if (i, j) == position:
                continue
            if (i, j) in cells:
                neighbours.append(cells[(i, j)])
    return neighbours

def first_larger_than(threshold):
    moves = {'e': (1,0), 'n': (0,1), 'w': (-1,0), 's': (0,-1)}
    next_directions = {'e':'n', 'n':'w', 'w':'s', 's':'e'}
    filled_cells = {(0,0): 1}
    direction = 's'
    position = (0,0)
    value = 1
    while value <= threshold:
        x, y = position
        dx, dy = moves[next_directions[direction]]
        next_cell_if_turning = (x + dx, y + dy)
        if next_cell_if_turning not in filled_cells:
            direction = next_directions[direction]
        dx, dy = moves[direction]
        position = (x + dx, y + dy)
        value = sum(filled_neighbours(filled_cells, position))
        filled_cells[position] = value
    return value

print(first_larger_than(int(input())))
