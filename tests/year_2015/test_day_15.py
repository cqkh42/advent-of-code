import textwrap

import pytest

from aoc_cqkh42.year_2015 import day_15


@pytest.fixture
def solution():
    data = """\
        Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
        Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
    """
    solution = day_15.Solution(textwrap.dedent(data))
    return solution


def test_part_a(solution):
    assert solution.part_a() == 62_842_880


def test_part_b(solution):
    assert solution.part_b() == 57_600_000
