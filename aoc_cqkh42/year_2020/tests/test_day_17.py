from aoc_cqkh42.year_2020 import day_17


def test_part_a():
    data = (
        '.#.\n'
        '..#\n'
        '###'
    )
    assert day_17.part_a(data) == 112


def test_part_b():
    data = (
        '.#.\n'
        '..#\n'
        '###'
    )
    assert day_17.part_b(data) == 848