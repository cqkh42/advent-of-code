import pytest

from aoc_cqkh42.year_2017 import day_22

@pytest.fixture
def solution():
    data = """..#
#..
..."""
    return day_22.Solution(data)

@pytest.mark.parametrize('current,change,expected', [
    ('N', 1, 'E'),
    ("N", -1, 'W'),
    ('E', 1, 'S'),
    ('E', -1, 'N'),
    ('W', 1, 'N'),
    ('W', -1, 'S')
])
def test_turn(solution, current, change, expected):
    solution.direction = current
    solution.turn(change)
    assert solution.direction == expected

def test_part_a(solution):
    assert solution.part_a() == 5587

def test_part_a_small(solution):
    assert solution.part_a(70) == 41

def test_part_b(solution):
    assert solution.part_b(100) == 26