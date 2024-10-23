import pytest

from aoc_cqkh42.year_2017.day_14 import Solution, hex_to_bytes

@pytest.fixture
def data():
    return "flqrgnkx"


@pytest.mark.parametrize('input_,output', [
    ('a', '1010'),
    ('0', '0000'),
    ('c', '1100'),
    ('2', '0010'),
    ('0', '0000'),
    ('1', '0001'),
    ('7', '0111'),
])
def test_hex_to_bytes(input_, output):
    assert hex_to_bytes(input_) == output

def test_part_a(data):
    assert Solution(data).part_a() == 8108

def test_part_b(data):
    assert Solution(data).part_b() == 1242