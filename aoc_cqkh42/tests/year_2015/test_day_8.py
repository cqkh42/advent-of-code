from aoc_cqkh42.year_2015 import day_8


def test_part_a():
    data = '""\n"abc"\n"aaa\\"aaa"\n"\\x27"'
    assert day_8.part_a(data) == 12


def test_part_b():
    data = '""\n"abc"\n"aaa\\"aaa"\n"\\x27"'
    assert day_8.part_b(data) == 19
