import textwrap

import pytest

from aoc_cqkh42.year_2015 import day_09


@pytest.fixture
def solution():
    data = """\
        London to Dublin = 464
        London to Belfast = 518
        Dublin to Belfast = 141
    """
    solution = day_09.Solution(textwrap.dedent(data))
    return solution


def test_part_a(solution):
    assert solution.part_a() == 605


def test_part_b(solution):
    assert solution.part_b() == 982
