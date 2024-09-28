from aoc_cqkh42.year_2016.day_12 import Solution

from pytest import fixture


@fixture
def data():
    return """cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a"""


def test_computer(data):
    assert Solution(data).part_a() == 42

