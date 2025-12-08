import pytest

from aoc_cqkh42.year_2025 import day_06


@pytest.fixture
def solution():
    return day_06.Solution(
        """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """)


def test_part_b(solution):
    assert solution.part_b() == 3263827
