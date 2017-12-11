# Advent of Code 2017 - Day 7 - Recursive Circus
# http://adventofcode.com/2017/day/7

import sys

def parse_input(lines):
    tree = {}
    for line in lines:
        tokens = line.rstrip().split(' ')
        name = tokens[0]
        node = {'weight': int(tokens[1].strip('()'))}
        if '->' in tokens:
            children = tokens[tokens.index('->') + 1:]
            node['children'] = [child.strip(',') for child in children]
        else:
            node['children'] = []
        tree[name] = node
    return tree

def root_node(tree):
    nodes = list(tree.keys())
    for node in tree:
        for child in tree[node]['children']:
            nodes.remove(child)
    return nodes[0]

tree = parse_input(sys.stdin.readlines())
print(root_node(tree))
