import pytest

from aoc_cqkh42.year_2022 import day_02


@pytest.fixture(scope='module')
def solution():
    data = """A Y
B X
C Z"""
    return day_02.Solution(data)


def test_part_a(solution):
    assert solution.part_a() == 15


def test_part_b(solution):
    assert solution.part_b() == 12
