import pytest

from aoc_cqkh42.year_2017 import day_01


@pytest.mark.parametrize(
    'data, answer', [('1122', 3), ('1111', 4), ('1234', 0), ('91212129', 9)]
)
def test_part_a(data, answer):
    assert day_01.part_a(data) == answer


@pytest.mark.parametrize(
    'data, answer',
    [('1212', 6), ('1221', 0), ('123425', 4), ('123123', 12), ('12131415', 4)]
)
def test_part_b(data, answer):
    assert day_01.part_b(data) == answer
