"""
Solutions for day 12 of 2020's Advent of Code

"""
from typing import Tuple


def rotate_right(n, e) -> Tuple[int, int]:
    return -e, n


def rotate_left(n, e) -> Tuple[int, int]:
    return e, -n


def part_a(data) -> int:
    directions = ['N', 'E', 'S', 'W']
    direction = 'E'
    n = 0
    e = 0
    for instruction in data.split('\n'):
        action = instruction[0]
        number = int(instruction[1:])
        if action == 'F':
            action = direction
        if action == 'N':
            n += number
        elif action == 'S':
            n -= number
        elif action == 'E':
            e += number
        elif action == 'W':
            e -= number
        elif action == 'R':
            turns = number / 90
            new_index = (directions.index(direction) + turns) % 4
            direction = directions[int(new_index)]
        elif action == 'L':
            turns = number / 90
            new_index = (directions.index(direction) - turns) % 4
            direction = directions[int(new_index)]

    return abs(n) + abs(e)


def part_b(data, **_) -> int:
    w_n = 1
    w_e = 10
    n = 0
    e = 0
    for instruction in data.split('\n'):
        action = instruction[0]
        number = int(instruction[1:])
        if action == 'F':
            n += (w_n*number)
            e += (w_e*number)
        if action == 'N':
            w_n += number
        elif action == 'S':
            w_n -= number
        elif action == 'E':
            w_e += number
        elif action == 'W':
            w_e -= number
        elif action == 'R':
            for _ in range(number // 90):
                w_n, w_e = rotate_right(w_n, w_e)
        elif action == 'L':
            for _ in range(number // 90):
                w_n, w_e = rotate_left(w_n, w_e)
    return abs(n) + abs(e)
