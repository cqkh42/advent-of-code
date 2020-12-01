from aoc_cqkh42.year_2015 import day_15


def test_part_a():
    data = 'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8\nCinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'
    assert day_15.part_a(data) == 62_842_880


def test_part_b():
    data = 'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8\nCinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'
    assert day_15.part_b(data) == 57_600_000
