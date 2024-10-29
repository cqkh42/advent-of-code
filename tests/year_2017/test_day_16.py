import pytest

from aoc_cqkh42.year_2017.day_16 import Solution, swap

@pytest.fixture
def data():
    return """s1,x3/4,pe/b"""

def test_part_a(data):
    assert Solution(data).part_a(5) == 'baedc'


def test_swap():
    assert swap('abcde', 3) == 'cdeab'

def test_part_b(data):
    s = Solution(data)
    s.part_a()
    assert Solution(data).part_b() == 309