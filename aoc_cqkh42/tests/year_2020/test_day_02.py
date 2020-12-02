import pytest

from aoc_cqkh42.year_2020 import day_02


@pytest.fixture
def data():
    return '1-3 a: abcde\n1-3 b: cdefg\n2-9 c: ccccccccc'


def test_part_a(data):
    assert day_02.part_a(data) == 2


def test_part_b(data):
    assert day_02.part_b(data) == 1
