import pytest

from aoc_cqkh42.year_2015 import day_2


@pytest.mark.parametrize(
    'data,answer',
    [
        ('2x3x4', 58), ('1x1x10', 43),
    ]
)
def test_part_a(data, answer):
    assert day_2.part_a(data) == answer


@pytest.mark.parametrize('data,answer', [('2x3x4', 34), ('1x1x10', 14)])
def test_part_b(data, answer):
    assert day_2.part_b(data) == answer