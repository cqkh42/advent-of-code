import pytest

from aoc_cqkh42.year_2020 import day_08


@pytest.fixture
def data():
    data = (
        'nop +0\n'
        'acc +1\n'
        'jmp +4\n'
        'acc +3\n'
        'jmp -3\n'
        'acc -99\n'
        'acc +1\n'
        'jmp -4\n'
        'acc +6'
    )
    return data


def test_part_a(data):
    assert day_08.part_a(data) == 5


def test_part_b(data):
    assert day_08.part_b(data) == 8
