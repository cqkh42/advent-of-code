"""
Solutions for day 3 of 2020's Advent of Code

"""
import math


def _trees_in_path(trees, x, y) -> int:
    trees = trees[::y]
    width = len(trees[0])
    x_steps = (x * y for y in range(len(trees)))
    x_looped = (x % width for x in x_steps)
    trees = (row[x] == '#' for row, x in zip(trees, x_looped))
    return sum(trees)


def part_a(data) -> int:
    trees = data.split('\n')
    return _trees_in_path(trees, 3, 1)


def part_b(data, **_) -> int:
    trees = data.split('\n')
    routes = [
        _trees_in_path(trees, 1, 1),
        _trees_in_path(trees, 3, 1),
        _trees_in_path(trees, 5, 1),
        _trees_in_path(trees, 7, 1),
        _trees_in_path(trees, 1, 2),
    ]
    return math.prod(routes)
