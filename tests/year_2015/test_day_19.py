import pytest

from aoc_cqkh42.year_2015 import day_19


@pytest.fixture
def transformations():
    return 'H => HO\nH => OH\nO => HH\n\n'


# noinspection SpellCheckingInspection
@pytest.mark.parametrize('data, answer', [('HOH', 4), ('HOHOHO', 7)])
def test_part_a(data, answer, transformations):
    data = transformations + data
    solution = day_19.Solution(data)
    assert solution.part_a() == answer


# noinspection SpellCheckingInspection
@pytest.mark.parametrize('data, answer', [
    ('HOH', 3),
    ('HOHOHO', 6)
])
def test_part_b(data, answer, transformations):
    transformations = """\
    e => H
    e => O
    H => HO
    H => OH
    O => HH"""
    data = transformations
    print(data)
    solution = day_19.Solution(data)
    assert solution.part_b() == answer
