"""
Solutions for day 3 of 2020's Advent of Code

"""
import math


def _trees_in_path(trees, x, y) -> int:
    trees = trees[::y]
    width = len(trees[0])
    x_steps = ((x * y) % width for y in range(len(trees)))
    trees = [row[x] for row, x in zip(trees, x_steps)]
    return trees.count('#')


def part_a(data) -> int:
    """
    Solution for part a

    Parameters
    ----------
    data: str

    Returns
    -------
    answer: int

    """
    trees = data.split('\n')
    return _trees_in_path(trees, 3, 1)


def part_b(data, **_) -> int:
    """
    Solution for part b

    Parameters
    ----------
    data: str

    Returns
    -------
    answer: int

    """
    trees = data.split('\n')
    routes = (
        _trees_in_path(trees, x, y)
        for x, y in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    )
    return math.prod(routes)
