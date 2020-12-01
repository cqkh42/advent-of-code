from aoc_cqkh42.year_2015 import day_24


def test_part_a():
    data = '\n'.join([1,2,3,4,5,7,8,9,10,11])
    assert day_24.part_a(data) == 99


def test_part_b():
    data = '\n'.join([1,2,3,4,5,7,8,9,10,11])
    assert day_24.part_b(data) == 44
