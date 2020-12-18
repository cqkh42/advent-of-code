import pytest

from aoc_cqkh42.year_2020 import day_18



@pytest.mark.parametrize(
    'data, answer',
    [
        ('1 + 2 * 3 + 4 * 5 + 6', 71),
        ('1 + (2 * 3) + (4 * (5 + 6))', 51),
        ('2 * 3 + (4 * 5)', 26),
        ('5 + (8 * 3 + 9 + 3 * 4 * 3)', 437),
        ('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 12240),
        ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 13632)
    ]
)
def test_do(data, answer):
    assert day_18.do(data) == answer


@pytest.mark.parametrize(
    'data, answer',
    [
        ('1 + 2 * 3 + 4 * 5 + 6', 231),
        ('1 + (2 * 3) + (4 * (5 + 6))', 51),
        ('2 * 3 + (4 * 5)', 46),
        ('5 + (8 * 3 + 9 + 3 * 4 * 3)', 1445),
        ('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 669060),
        ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 23340)
    ]
)
def test_do_b(data, answer):
    assert day_18.do_b(data) == answer