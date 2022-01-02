import textwrap

import pytest

from aoc_cqkh42.year_2015 import day_14


@pytest.fixture
def solution():
    data = """\
        Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
        Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
    """
    solution = day_14.Solution(textwrap.dedent(data))
    return solution


def test_part_a(solution):
    assert solution.part_a(1000) == 1120


def test_part_b(solution):
    assert solution.part_b(1000) == 689
