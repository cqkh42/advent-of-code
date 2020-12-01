from aoc_cqkh42.year_2015 import day_17


def test_part_a():
    data = '20,15,10,5,5'
    assert day_17.part_a(data, target=25) == 4


def test_part_b():
    data = '20,15,10,5,5'
    assert day_17.part_b(data, target=25) == 3
