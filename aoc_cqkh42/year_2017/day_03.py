import functools
import itertools
from collections import defaultdict
from typing import Self

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    def _process_data(self: Self) -> int:
        return int(self.input_)

    def part_a(self):
        x, y = _coords(self.processed)
        return abs(x) + abs(y)

    def part_b(self):
        tracked = defaultdict(int)
        tracked[(0, 0)] = 1
        for number in itertools.count(1):
            x, y = _coords(number)
            around = _around_point(x, y)
            total = sum(tracked[(x_, y_)] for x_, y_ in around)
            tracked[(x, y)] = total
            if total > self.processed:
                return total


def _square_before(num):
    for square in itertools.count(1):
        if num < square ** 2:
            return square - 1


def _x(num, square_before, maximum, odd_square, travelled):
    if _square_before(num+1)**2 == num:
        # it is a square number

        multiplier = (-1) ** (not (num % 2))
        out = num ** 0.5 // 2
        return multiplier * (out - (not (multiplier+1)))

    multiplier = (-1) ** (not odd_square)
    maximum += odd_square
    past_second_corner = max(travelled - square_before, 0)
    return multiplier * (maximum - past_second_corner)


def _y(num, square_before, maximum, odd_square, travelled):
    if _square_before(num+1)**2 == num:
        multiplier = (-1) ** (num % 2)
        out = num ** 0.5 // 2
        return multiplier * out

    if num - square_before ** 2 > square_before:
        maximum += odd_square
        multiplier = (-1) ** (not odd_square)
        past_second_corner = min(travelled - square_before, 0)
        return multiplier * (maximum - past_second_corner)
    else:
        multiplier = (-1) ** odd_square
        return multiplier * (maximum - travelled)

@functools.cache
def _coords(num):
    if num == 1:
        return 0, 0
    square_before = _square_before(num)
    maximum = square_before // 2
    squared_before = square_before ** 2
    odd_square = bool(square_before % 2)
    travelled = num - squared_before - 1
    x = _x(num, square_before, maximum, odd_square, travelled)
    y = _y(num, square_before, maximum, odd_square, travelled)
    return x, y


def _around_point(x, y):
    return itertools.product([x-1, x, x+1], [y-1, y, y+1])

if __name__ == "__main__":
    submit_answers(Solution, 3, 2017)