import pytest

from aoc_cqkh42.year_2025 import day_09


@pytest.fixture
def solution():
    return day_09.Solution(
        """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3""")


def test_part_a(solution):
    assert solution.part_a() == 50

def test_part_b(solution):
    assert solution.part_b() == 24