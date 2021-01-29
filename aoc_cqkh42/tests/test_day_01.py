import pytest

from aoc_cqkh42.year_2015 import day_01


@pytest.mark.parametrize(
    'data, answer',
    [
        ('(())', 0), ('()()', 0), ('(((', 3), ('(()(()(', 3), ('))(((((', 3),
        ('())', -1), ('))(', -1), (')))', -3), (')())())', -3)
    ]
)
def test_part_a(data, answer):
    assert day_01.part_a(data) == answer


@pytest.mark.parametrize('data, answer', [(')', 1), ('()())', 5)])
def test_part_b(data, answer):
    assert day_01.part_b(data) == answer
