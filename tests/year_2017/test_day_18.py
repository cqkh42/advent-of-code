import pytest

from aoc_cqkh42.year_2017.day_18 import Solution

@pytest.fixture
def data():
    return """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2"""

def test_part_a(data):
    assert Solution(data).part_a() == 4


# def test_part_b():
#     assert Solution('3').part_b() == 638