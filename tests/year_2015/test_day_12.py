import pytest

from aoc_cqkh42.year_2015 import day_12


@pytest.mark.parametrize(
    'data, answer',
    [
        ('[1,2,3]', 6),
        ('{"a":2,"b":4}', 6),
        ('[[[3]]]', 3),
        ('{"a":{"b":4},"c":-1}', 3),
        ('{"a":[-1,1]}', 0),
        ('[-1,{"a":1}]', 0),
        ('[]', 0),
        ('{}', 0)
    ]
)
def test_part_a(data, answer):
    solution = day_12.Solution(data)
    assert solution.part_a() == answer


@pytest.mark.parametrize(
    'data, answer',
    [
        ('[1,2,3]', 6),
        ('[1,{"c":"red","b":2},3]', 4),
        ('{"d":"red","e":[1,2,3,4],"f":5}', 0),
        ('[1,"red",5]', 6)
    ]
)
def test_part_b(data, answer):
    solution = day_12.Solution(data)
    assert solution.part_b() == answer
