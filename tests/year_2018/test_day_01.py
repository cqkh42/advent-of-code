import pytest

from aoc_cqkh42.year_2018 import day_01

@pytest.fixture()
def inputs():
    return """+1
    -2
    +3
    +1"""

def test_part_a(inputs):
    assert day_01.Solution(inputs).part_a() == 3

def test_part_b(inputs):
    assert day_01.Solution(inputs).part_b() == 2