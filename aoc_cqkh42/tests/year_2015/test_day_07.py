from aoc_cqkh42.year_2015 import day_07


def test_part_a():
    data = (
        '123 -> x\n'
        '456 -> y\n'
        'x AND y -> d\n'
        'x OR y -> e\n'
        'x LSHIFT 2 -> f\n'
        'y RSHIFT 2 -> g\n'
        'NOT x -> a\n'
        'NOT y -> i'
    )
    assert day_07.part_a(data) == 65412
