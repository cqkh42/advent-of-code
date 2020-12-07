import pytest

from aoc_cqkh42.year_2019 import day_01


@pytest.mark.parametrize(
    'data, answer', [('12', 2), ('14', 2), ('1969', 654), ('100756', 33583)]
)
def test__fuel_needed(data, answer):
    assert day_01._fuel_needed(data) == answer


@pytest.mark.parametrize(
    'data, answer', [('14', 2), ('1969', 966), ('100756', 50346)]
)
def test__total_fuel_needed(data, answer):
    assert day_01._total_fuel_needed(data) == answer