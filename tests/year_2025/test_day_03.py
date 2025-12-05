import pytest

from aoc_cqkh42.year_2025 import day_03


@pytest.fixture
def solution():
    return day_03.Solution(
        """987654321111111
811111111111119
234234234234278
818181911112111""")


def test_part_b(solution):
    assert solution.part_b() == 3121910778619