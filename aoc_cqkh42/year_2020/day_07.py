"""
Solutions for day 7 of 2020's Advent of Code

"""
import itertools
import re
from typing import Dict

REGEX = re.compile(r'(\d*?) ?(\w+? \w+?) bag')


def _parse_bags(data) -> Dict[str, Dict[str, int]]:
    rows = (REGEX.findall(row) for row in data.split('\n'))
    d = {
        color[1]: {sub_color: int(num) for num, sub_color in parts if num}
        for color, *parts in rows
    }
    return d


def _can_contain(color, mapping) -> set:
    if not mapping[color]:
        return set()
    found = (_can_contain(color, mapping) for color in mapping[color])
    found = set(itertools.chain.from_iterable(found))
    found.update(mapping[color])
    return found


def _count_bags(color, mapping) -> int:
    if not mapping[color]:
        return 1
    found = (
        num * _count_bags(sub_color, mapping)
        for sub_color, num in mapping[color].items()
    )
    return sum(found) + 1


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
    mapping = _parse_bags(data)
    total_mapping = (_can_contain(color, mapping) for color in mapping)
    return sum('shiny gold' in color for color in total_mapping)


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
    mapping = _parse_bags(data)
    return _count_bags('shiny gold', mapping) - 1
