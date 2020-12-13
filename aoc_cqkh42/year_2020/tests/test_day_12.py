from aoc_cqkh42.year_2020 import day_12


def test_part_a():
    data = (
        'F10\n'
        'N3\n'
        'F7\n'
        'R90\n'
        'F11'
    )
    assert day_12.part_a(data) == 25


def test_part_b():
    data = (
        'F10\n'
        'N3\n'
        'F7\n'
        'R90\n'
        'F11'
    )
    assert day_12.part_b(data) == 286