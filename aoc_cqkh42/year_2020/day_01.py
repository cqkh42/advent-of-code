import itertools
import math


def _find_combination(numbers, total, n):
    combs = (   #pragma:  no branch
        nums for nums in itertools.combinations(numbers, n)
        if sum(nums) == total
    )
    return next(combs)


def part_a(data):
    numbers = (int(num) for num in data.split('\n'))
    comb = _find_combination(numbers, 2020, 2)
    return math.prod(comb)


def part_b(data, **_):
    numbers = (int(num) for num in data.split('\n'))
    comb = _find_combination(numbers, 2020, 3)
    return math.prod(comb)
