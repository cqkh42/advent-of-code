import pytest

from aoc_cqkh42.year_2020 import day_05


@pytest.mark.parametrize(
    'data, answer',
    [
        ('BFFFBBFRRR', 70),
        ('FFFBBBFRRR', 14),
        ('BBFFBBFRLL', 102),
        ('FBFBBFFRLR', 44)
    ]
)
def test__row(data, answer):
    assert day_05._row(data) == answer


@pytest.mark.parametrize(
    'data, answer',
    [
        ('BFFFBBFRRR', 7),
        ('FFFBBBFRRR', 7),
        ('BBFFBBFRLL', 4),
        ('FBFBBFFRLR', 5)
    ]
)
def test__col(data, answer):
    assert day_05._col(data) == answer


@pytest.mark.parametrize(
    'data, answer',
    [
        ('BFFFBBFRRR', 567),
        ('FFFBBBFRRR', 119),
        ('BBFFBBFRLL', 820),
        ('FBFBBFFRLR', 357)
    ]
)
def test__seat_id(data, answer):
    assert day_05._seat_id(data) == answer
