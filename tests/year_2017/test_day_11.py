import pytest

from aoc_cqkh42.year_2017.day_11 import Solution

@pytest.mark.parametrize('input_,output', [
    ('ne,ne,ne', 3),
    ('ne,ne,sw,sw', 0),
    ('ne,ne,s,s', 2),
    ('se,sw,se,sw,sw', 3)
])
def test_part_a(input_, output):
    assert Solution(input_).part_a() == output