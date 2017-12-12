# Advent of Code 2017 - Day 7 - Recursive Circus - Part 2
# http://adventofcode.com/2017/day/7

from day07_part1 import *

def subtree_weight(tree, node):
    if tree[node]['children'] == []:
        return tree[node]['weight']
    else:
        return tree[node]['weight'] + sum([subtree_weight(tree, child) for child in tree[node]['children']])

def children_weights(tree, node):
    return [subtree_weight(tree, child) for child in tree[node]['children']]

def balanced_children(tree, node):
    weights = children_weights(tree, node)
    return min(weights) == max(weights)

def unbalanced_node(tree, node):
    parent = None
    current = node
    while not balanced_children(tree, current):
        bad_node, _ = find_unbalance(tree, current)
        parent = current
        current = bad_node
    return parent

def find_unbalance(tree, node):
    weights = children_weights(tree, node)
    if weights.count(min(weights)) > weights.count(max(weights)):
        delta = min(weights) - max(weights)
        bad_node = tree[node]['children'][weights.index(max(weights))]
    else:
        delta = max(weights) - min(weights)
        bad_node = tree[node]['children'][weights.index(min(weights))]
    return bad_node, delta

def fix_unbalance(tree, node):
    bad_node, delta = find_unbalance(tree, node)
    return tree[bad_node]['weight'] + delta

tree = parse_input(sys.stdin.readlines())
print(fix_unbalance(tree, unbalanced_node(tree, root_node(tree))))
