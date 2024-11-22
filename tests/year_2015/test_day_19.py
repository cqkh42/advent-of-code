import pytest

from aoc_cqkh42.year_2015 import day_19
from aoc_cqkh42.year_2015.day_19 import Compound


@pytest.fixture
def transformations():
    return "H => HO\nH => OH\nO => HH\n\n"


# noinspection SpellCheckingInspection
@pytest.mark.parametrize("data, answer", [("HOH", 4), ("HOHOHO", 7)])
def test_part_a(data, answer, transformations):
    data = transformations + data
    solution = day_19.Solution(data)
    assert solution.part_a() == answer


def test_line_parser_simple():
    b = day_19.RuleBuilder()
    out = b.parse_line((Compound('Al'), Compound('ThF')))
    assert set(out) == {(Compound('Al'), Compound('ThF'))}

def test_line_parser_complex():
    b = day_19.RuleBuilder()
    out = b.parse_line((Compound('Al'), Compound('ThRnFAr')))
    expected = {
        (Compound('Al'), Compound('ThZaa')),
        (Compound('Zaa'), Compound('RnZab')),
        (Compound('Zab'), Compound('FAr')),
    }
    assert set(out) == expected

def test_molecule_equality():
    assert Compound('AbC') == Compound(['Ab', 'C'])