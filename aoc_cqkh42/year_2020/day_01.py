"""
Solutions for day 1 of 2020's Advent of Code

"""
import itertools
import math


def _find_subset_with_sum(numbers, total, n) -> tuple:
    combs = (
        nums for nums in itertools.combinations(numbers, n)
        if sum(nums) == total
    )
    return next(combs)


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
    numbers = (int(num) for num in data.split('\n'))
    comb = _find_subset_with_sum(numbers, 2020, 2)
    return math.prod(comb)


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
    numbers = (int(num) for num in data.split('\n'))
    comb = _find_subset_with_sum(numbers, 2020, 3)
    return math.prod(comb)
