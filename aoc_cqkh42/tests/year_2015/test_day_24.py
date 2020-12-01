from aoc_cqkh42.year_2015 import day_24


def test_part_a():
    data = '1\n2\n3\n4\n5\n7\n8\n9\n10\n11'
    assert day_24.part_a(data) == 99


def test_part_b():
    data = '1\n2\n3\n4\n5\n7\n8\n9\n10\n11'
    assert day_24.part_b(data) == 44
