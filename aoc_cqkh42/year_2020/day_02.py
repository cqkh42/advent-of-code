"""
Solutions for day 2 of 2020's Advent of Code

"""
import parse

PARSER = parse.compile(r'{:d}-{:d} {:w}: {:w}')


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
    lines = PARSER.findall(data)
    is_valid = (low <= pw.count(char) <= high for low, high, char, pw in lines)
    return sum(is_valid)


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
    lines = PARSER.findall(data)
    once = [
        (pw[low-1] + pw[high-1]).count(char)
        for low, high, char, pw in lines
    ]
    return once.count(1)
