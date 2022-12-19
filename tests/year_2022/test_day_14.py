import pytest

from aoc_cqkh42.year_2022 import day_14


@pytest.fixture(scope='module')
def solution():
    data = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""
    return day_14.Solution(data)


def test_part_a(solution):
    assert solution.part_a() == 24


def test_part_b(solution):
    assert solution.part_b() == 93
