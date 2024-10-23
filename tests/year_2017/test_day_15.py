import pytest

from aoc_cqkh42.year_2017.day_15 import Solution

@pytest.fixture
def data():
    return """Generator A starts with 65
Generator B starts with 8921"""

def test_part_a(data):
    assert Solution(data).part_a() == 597

def test_part_b(data):
    assert Solution(data).part_b() == 309