import pytest

from aoc_cqkh42.year_2015 import day_19, day_19_help


@pytest.mark.xfail
def test_solve():
    assert day_19.run(day_19_help.input_, day_19_help.molecule) == 195


@pytest.fixture
def transformations():
    return "H => HO\nH => OH\nO => HH\n\n"


# noinspection SpellCheckingInspection
@pytest.mark.parametrize("data, answer", [("HOH", 4), ("HOHOHO", 7)])
def test_part_a(data, answer, transformations):
    data = transformations + data
    solution = day_19.Solution(data)
    assert solution.part_a() == answer


# noinspection SpellCheckingInspection
@pytest.mark.xfail
@pytest.mark.parametrize(
    "data, answer",
    [
        ("HOH", 3),
    ],
)
def test_part_b(data, answer):
    transformations = (
        "\n".join(["e => H", "e => O", "H => HO", "H => OH", "O => HH"]) + f"\n\n{data}"
    )
    solution = day_19.Solution(transformations)
    assert solution.part_b() == answer
