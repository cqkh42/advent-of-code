from aoc_cqkh42.year_2015 import day_9


def test_part_a():
    data = 'London to Dublin = 464\nLondon to Belfast = 518\nDublin to Belfast = 141'
    assert day_9.part_a(data) == 605


def test_part_b():
    data = 'London to Dublin = 464\nLondon to Belfast = 518\nDublin to Belfast = 141'
    assert day_9.part_b(data) == 982
