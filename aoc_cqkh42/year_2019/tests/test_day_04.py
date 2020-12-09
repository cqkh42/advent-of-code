import pytest

from aoc_cqkh42.year_2019 import day_04


@pytest.mark.parametrize(
    'password, answer', [(111111, True), (223450, False), (1237890, False)]
)
def test__is_valid(password, answer):
    assert day_04._is_valid(password) == answer

