import pytest

from aoc_cqkh42.year_2015 import day_19, day_19_help


@pytest.fixture
def transformations():
    return "H => HO\nH => OH\nO => HH\n\n"


# noinspection SpellCheckingInspection
@pytest.mark.parametrize("data, answer", [("HOH", 4), ("HOHOHO", 7)])
def test_part_a(data, answer, transformations):
    data = transformations + data
    solution = day_19.Solution(data)
    assert solution.part_a() == answer


def test_input_parser():
    input_ = {
        "Al": "ThF",
        "Al": "ThRnFAr",
    }
    assert day_19._input_parser(input_) == {
        "Al": "ThF",
        "Al": "ThRnFAr",
        "Zaa": "RnFAr",
        "Zab": "FAr"
    }

