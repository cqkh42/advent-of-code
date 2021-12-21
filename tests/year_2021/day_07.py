import pytest

from aoc_cqkh42.year_2021 import day_07


@pytest.fixture
def solution():
    data = "16,1,2,0,4,2,7,1,2,14"
    return day_07.Solution(data)


def test_part_a(solution):
    assert solution.part_a() == 37


def test_part_b(solution):
    assert solution.part_b() == 168