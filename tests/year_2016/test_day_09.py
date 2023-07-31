import pytest

from aoc_cqkh42.year_2016 import day_09


@pytest.mark.parametrize(
    ["input_", "expected"],
    (
        ("ADVENT", "ADVENT"),
        ("A(1x5)BC", "ABBBBBC"),
        ("(3x3)XYZ", "XYZXYZXYZ"),
        ("A(2x2)BCD(2x2)EFG", "ABCBCDEFEFG"),
        ("(6x1)(1x3)A", "(1x3)A"),
        ("X(8x2)(3x3)ABCY", "X(3x3)ABC(3x3)ABCY"),
    ),
)
def test_expand_string(input_, expected):
    assert day_09.expand_string(input_) == expected


@pytest.mark.parametrize(
    ["input_", "expected"],
    (
        ("ADVENT", 6),
        ("A(1x5)BC", 7),
        ("(3x3)XYZ", 9),
        ("A(2x2)BCD(2x2)EFG", 11),
        ("(6x1)(1x3)A", 6),
        ("X(8x2)(3x3)ABCY", 18),
    ),
)
def test_part_a(input_, expected):
    solution = day_09.Solution(input_)
    assert solution.part_a() == expected


@pytest.mark.parametrize(
    ["input_", "expected"],
    (
        ("(3x3)XYZ", 9),
        ("X(8x2)(3x3)ABCY", 20),
        ("(27x12)(20x12)(13x14)(7x10)(1x12)A", 241920),
        ("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", 445),
    ),
)
def test_part_b(input_, expected):
    solution = day_09.Solution(input_)
    assert solution.part_b() == expected
