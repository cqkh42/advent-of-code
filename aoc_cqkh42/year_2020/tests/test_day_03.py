import pytest

from aoc_cqkh42.year_2020 import day_03


@pytest.fixture
def data():
    trees = (
        '..##.......\n'
        '#...#...#..\n'
        '.#....#..#.\n'
        '..#.#...#.#\n'
        '.#...##..#.\n'
        '..#.##.....\n'
        '.#.#.#....#\n'
        '.#........#\n'
        '#.##...#...\n'
        '#...##....#\n'
        '.#..#...#.#'
    )
    return trees


@pytest.mark.parametrize(
    'x,y,answer',
    [(1, 1, 2), (3, 1, 7), (5, 1, 3), (7, 1, 4), (1, 2, 2)]
)
def test__trees_in_path(data, x, y, answer):
    trees = data.split('\n')
    assert day_03._trees_in_path(trees, x, y) == answer


def test_part_a(data):
    assert day_03.part_a(data) == 7


def test_part_b(data):
    assert day_03.part_b(data) == 336
