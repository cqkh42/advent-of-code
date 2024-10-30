import pytest

from aoc_cqkh42.year_2017.day_16 import Solution

@pytest.fixture
def data():
    return """s1,x3/4,pe/b"""

def test_part_a(data):
    assert Solution(data).part_a(5) == 'baedc'


def test_part_b(data):
    assert False