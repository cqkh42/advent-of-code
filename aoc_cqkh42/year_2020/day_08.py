"""
Solutions for day 8 of 2020's Advent of Code

"""
import re
from typing import Tuple

import parse

REGEX = re.compile(r'nop|jmp')
PARSER = parse.compile(r'{:w} {:d}')


def _run_code(instructions) -> Tuple[int, bool]:
    visited = set()
    index = 0
    accumulator = 0
    while index not in visited:
        visited.add(index)
        try:
            instruction, number = instructions[index]
        except IndexError:
            return accumulator, False
        if instruction == 'nop':
            index += 1
        elif instruction == 'acc':
            accumulator += number
            index += 1
        else:
            index += number
    return accumulator, True


def _replace(match) -> str:
    replacement_dict = {
        'nop': 'jmp',
        'jmp': 'nop'
    }
    return replacement_dict[match.group()]


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
    instructions = list(PARSER.findall(data))
    accumulator, _ = _run_code(instructions)
    return accumulator


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
    matches = REGEX.finditer(data)
    potential_instructions = (
        data[:match.start()] + _replace(match) + data[match.end():]
        for match in matches
    )
    potential_instructions = (
        list(PARSER.findall(potential)) for potential in potential_instructions
    )
    results = (
        _run_code(instructions) for instructions in potential_instructions
    )
    results = (accumulator for accumulator, success in results if not success)
    return next(results)
