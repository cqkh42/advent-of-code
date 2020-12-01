import pytest

from aoc_cqkh42.year_2015 import day_19


@pytest.mark.parametrize('data,answer', [('HOH', 4), ('HOHOHO', 7)])
def test_part_a(data, answer):
    data = 'H => HO\nH => OH\nO => HH\n\n' + data
    assert day_19.part_a(data) == answer


@pytest.mark.parametrize('data,answer', [('HOH', 3), ('HOHOHO', 6)])
def test_part_b(data, answer):
    data = 'e => H\ne => O\nH => HO\nH => OH\nO => HH\n\n' + data
    print(data)
    assert day_19.part_b(data) == answer
