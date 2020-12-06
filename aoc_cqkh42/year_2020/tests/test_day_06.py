import pytest

from aoc_cqkh42.year_2020 import day_06


@pytest.fixture
def data():
    data = (
        'abc\n'
        '\n'
        'a\nb\nc\n'
        '\n'
        'ab\nac\n'
        '\n'
        'a\na\na\na\n'
        '\n'
        'b'
        )
    return data


def test_part_a(data):
    assert day_06.part_a(data) == 11


def test_part_b(data):
    assert day_06.part_b(data) == 6
