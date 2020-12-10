import pytest

from aoc_cqkh42.year_2020 import day_10


def test__sort_adapters():
    adapters = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    answer = [0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22]
    assert day_10._sort_adapters(adapters) == answer


def test__chain_adapters():
    adapters = [0, 1, 2, 3, 6, 9]
    answer = ((1, 2, 3), (2, 3), (3,), (6,), 0, 0, (9,), 0, 0, tuple())
    assert day_10._chain_adapters(adapters) == answer


@pytest.mark.parametrize('num, answer', [(6, 1), (3, 1), (1, 2), (0, 4)])
def test__num_routes(num, answer):
    chain = ((1, 2, 3), (2, 3), (3,), (6,), 0, 0, (9,), 0, 0, tuple())
    assert day_10._num_routes(num, chain) == answer


@pytest.mark.parametrize(
    'data, answer',
    [
        ('16\n10\n15\n5\n1\n11\n7\n19\n6\n12\n4', 35),
        (
            '28\n33\n18\n42\n31\n14\n46\n20\n48\n47\n24\n23\n49\n45\n19\n38\n'
            '39\n11\n1\n32\n25\n35\n8\n17\n7\n9\n4\n2\n34\n10\n3',
            220
        )
    ]
)
def test_part_a(data, answer):
    assert day_10.part_a(data) == answer


@pytest.mark.parametrize(
    'data, answer',
    [
        ('16\n10\n15\n5\n1\n11\n7\n19\n6\n12\n4', 8),
        (
            '28\n33\n18\n42\n31\n14\n46\n20\n48\n47\n24\n23\n49\n45\n19\n38\n'
            '39\n11\n1\n32\n25\n35\n8\n17\n7\n9\n4\n2\n34\n10\n3',
            19208
        )
    ]
)
def test_part_b(data, answer):
    assert day_10.part_b(data) == answer
