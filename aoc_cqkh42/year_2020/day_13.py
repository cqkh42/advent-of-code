"""
Solutions for day 13 of 2020's Advent of Code

"""
import itertools
from typing import Tuple


def _process(start, jump, index, num) -> Tuple[int, int]:
    found = []
    for t in itertools.count(start, jump):
        if (t + index) % num == 0:
            found.append(t)
        if len(found) == 2:
            break
    return found[0], found[1] - found[0]


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
    earliest, buses = data.split('\n')
    earliest = int(earliest)
    buses = [int(bus) for bus in buses.split(',') if bus != 'x']
    for minute in itertools.count(earliest):
        for bus in buses:
            if not (minute % bus):
                return (minute - earliest) * bus


def part_b(data, **_) -> int:
    _, buses = data.split('\n')

    buses = [(index, int(bus)) for index, bus in enumerate(buses.split(',')) if
             bus != 'x']
    start, jump = buses[0]
    for index, num in buses:
        start, jump = _process(start, jump, index, num)
    return start
