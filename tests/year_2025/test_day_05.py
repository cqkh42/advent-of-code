import pytest

from aoc_cqkh42.year_2025 import day_05


@pytest.fixture
def solution():
    return day_05.Solution(
        """3-5
10-14
16-20
12-18

1
5
8
11
17
32""")


def test_part_b(solution):
    assert solution.part_b() == 14