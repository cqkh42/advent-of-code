import pytest

from aoc_cqkh42.year_2017.day_13 import Solution

@pytest.fixture
def data():
    return """0: 3
    1: 2
    4: 4
    6: 4"""

def test_part_a(data):
    assert Solution(data).part_a() == 24


def test_part_b(data):
    assert Solution(data).part_b() == 10