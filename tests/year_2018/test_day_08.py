import pytest

from aoc_cqkh42.year_2018 import day_08

@pytest.fixture
def data():
    return """2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"""

def test_get_metadata():
    data = [0, 1, 99, 2, 1, 1, 2]
    assert day_08.get_metadata(data) == ([2,1,1,2], [99])
def test_part_a(data):
    assert day_08.Solution(data).part_a() == 138

def test_part_b(data):
    assert day_08.Solution(data).part_b() == 66