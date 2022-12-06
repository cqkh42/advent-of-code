import pytest

from aoc_cqkh42.year_2022 import day_06


@pytest.fixture(scope='module')
def solution():
    data = """bvwbjplbgvbhsrlpgdmjqwftvncz"""
    return day_06.Solution(data)


def test_part_a(solution):
    assert solution.part_a() == 5


def test_part_b(solution):
    assert solution.part_b() == 23
