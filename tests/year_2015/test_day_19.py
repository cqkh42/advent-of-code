import pytest

from aoc_cqkh42.year_2015 import day_19
from aoc_cqkh42.year_2015.day_19 import Molecule


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
    out = b.parse_line((Molecule('Al'), Molecule('ThF')))
    assert set(out) == {(Molecule('Al'), Molecule('ThF'))}

def test_line_parser_complex():
    b = day_19.RuleBuilder()
    out = b.parse_line((Molecule('Al'), Molecule('ThRnFAr')))
    expected = {
        (Molecule('Al'), Molecule('ThZaa')),
        (Molecule('Zaa'), Molecule('RnZab')),
        (Molecule('Zab'), Molecule('FAr')),
    }
    assert set(out) == expected

def test_molecule_equality():
    assert Molecule('AbC') == Molecule(['Ab', 'C'])