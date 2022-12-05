import pytest

from aoc_cqkh42.year_2015 import day_24


@pytest.fixture(scope="module")
def solution():
    data = "1\n2\n3\n4\n5\n7\n8\n9\n10\n11"
    return day_24.Solution(data)


def test_part_a(solution):
    assert solution.part_a() == 99


def test_part_b(solution):
    assert solution.part_b() == 44
