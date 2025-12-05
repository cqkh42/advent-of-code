import pytest

from aoc_cqkh42.year_2025 import day_01


@pytest.fixture
def solution():
    return day_01.Solution(
        """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""")

def test_part_a(solution):
    assert solution.part_a() == 3

def test_part_b(solution):
    assert solution.part_b() == 6

@pytest.mark.parametrize(("data", "expected"), [
    ("R1000", 10),
    ("L1000", 10),
    ("L600", 6),
    ("L650", 7),
    ("R600", 6),
    ("R650", 7),
])
def test_part_b_multiple(data, expected):
    assert day_01.Solution(data).part_b() == expected