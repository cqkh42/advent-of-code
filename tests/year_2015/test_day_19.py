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


# def test_input_parser():
#     input_ = {
#         "Al": "ThF",
#         "Al": "ThRnFAr",
#     }
#     assert day_19._input_parser(input_) == {
#         "Al": "ThF",
#         "Al": "ThRnFAr",
#         "Zaa": "RnFAr",
#         "Zab": "FAr"
#     }

def test_line_parser_simple():
    b = day_19.Rules([(Molecule('a'), Molecule('b'))])
    out = b.parse_line((Molecule('Al'), Molecule('ThF')))
    assert set(out) == {(Molecule('Al'), Molecule('ThF'))}

def test_line_parser_complex():
    b = day_19.Rules([(Molecule('a'), Molecule('b'))])
    out = b.parse_line((Molecule('Al'), Molecule('ThRnFAr')))
    expected = {
        (Molecule('Al'), Molecule('ThZaa')),
        (Molecule('Zaa'), Molecule('RnZab')),
        (Molecule('Zab'), Molecule('FAr')),
    }
    assert set(out) == expected

def test_line_parser_complex_two():
    b = day_19.Rules([(Molecule("P"), Molecule("SiRnFAr"))])
    out = b.parse_line((Molecule("P"), Molecule("SiRnFAr")))
    expected = {
    }
    assert set(out) == expected
