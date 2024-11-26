import pytest

from aoc_cqkh42.year_2017 import day_05


@pytest.fixture
def solution():
    return day_05.Solution("0\n3\n0\n1\n-3")


def test_part_a(solution):
    assert solution.part_a() == 5


def test_part_b(solution):
    assert solution.part_b() == 10
