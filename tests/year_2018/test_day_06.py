import pytest

from aoc_cqkh42.year_2018 import day_06

@pytest.fixture
def data():
    return """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9"""

def test_infinite(data):
    assert day_06.Solution(data).find_infinite() == {0,1,2,5}
def test_part_a(data):
    assert day_06.Solution(data).part_a() == 17

def test_part_b(data):
    assert day_06.Solution(data).part_b(32) == 16