import itertools
from collections import defaultdict


def _square_before(num):
    for square in itertools.count(1):
        if num < square ** 2:
            return square - 1


def _x(num, square_before, maximum, odd_square, travelled):
    if _square_before(num+1)**2 == num:
        # it is a square number
        out = num ** 0.5 // 2
        multiplier = (-1) ** (not (num % 2))
        return multiplier * (out - (not multiplier+1))

    multiplier = (-1) ** (not odd_square)
    maximum += odd_square
    past_second_corner = max(travelled - square_before, 0)
    return multiplier * (maximum - past_second_corner)


def _y(num, square_before, maximum, odd_square, travelled):
    if _square_before(num+1)**2 == num:
        multiplier = (-1) ** (num % 2)
        return multiplier * (num ** 0.5 // 2)

    if num - square_before ** 2 > square_before:
        maximum += odd_square
        multiplier = (-1) ** (not odd_square)
        past_second_corner = min(travelled - square_before, 0)
        return multiplier * (maximum - past_second_corner)
    else:
        multiplier = (-1) ** odd_square
        return multiplier * (maximum - travelled)


def _coords(num):
    if num == 1:
        return 0, 0
    square_before = _square_before(num)
    maximum = square_before // 2
    squared_before = _square_before(num) ** 2
    odd_square = bool(square_before % 2)
    travelled = num - squared_before - 1
    x = _x(num, square_before, maximum, odd_square, travelled)
    y = _y(num, square_before, maximum, odd_square, travelled)
    return x, y


def _around_point(x, y):
    return itertools.product([x-1, x, x+1], [y-1, y, y+1])


def part_a(data):
    num = int(data)
    x, y = _coords(num)
    return abs(x) + abs(y)


def part_b(data, **_):
    tracked = defaultdict(int)
    tracked[(0, 0)] = 1
    target = int(data)
    for number in itertools.count(1):
        x, y = _coords(number)
        around = _around_point(x, y)
        total = sum(tracked[(x_, y_)] for x_, y_ in around)
        tracked[(x, y)] = total
        if total > target:
            return total
