import pytest

from aoc_cqkh42.year_2020 import day_11


@pytest.fixture
def data():
    data = (
        'L.L\n'
        'LLL\n'
        '.L.'
    )
    return data


@pytest.fixture
def seats():
    seats = {
        (0, 0): 'L',
        (0, 1): 'L',
        (1, 1): 'L',
        (1, 2): 'L',
        (2, 0): 'L',
        (2, 1): 'L'
    }
    return seats


def test__parse_floor(data, seats):
    assert day_11._parse_floor(data) == seats


@pytest.mark.parametrize('x, y, answer', [(0, 0, 1), (0, 2, 1)])
def test__count_adjacent_seats(x, y, answer):
    seats = {(0, 0): '#', (0, 1): '#', (0, 2): 'L', (1, 0): 'L', (0, 3): '#'}
    assert day_11._count_adjacent_seats(x, y, seats) == answer


@pytest.mark.parametrize(
    'x, y, seats, answer',
    [
        (0, 0, {(0, 0): '#'}, '#'),
        (1, 1, {(1, 1): 'L', (1, 2): '#'}, 'L'),
        (1, 1, {(1, 1): 'L', (1, 2): 'L'}, '#'),
        (1, 1, {(1, 1): '#', (1, 2): 'L'}, '#'),
        (
            1,
            1,
            {(1, 1): '#', (1, 2): '#', (1, 0): '#', (2, 1): '#', (0, 1): '#'},
            'L'
        ),
        (6, 0, {(5, 0): '#', (6, 0): '#', (5, 1): '#', (6, 1): '#'}, '#')
    ]
)
def test__new_state(x, y, seats, answer):
    assert day_11._new_state(x, y, seats) == answer


def test__update_seats(seats):
    answer = {
        (0, 0): '#',
        (0, 1): '#',
        (1, 1): '#',
        (1, 2): '#',
        (2, 0): '#',
        (2, 1): '#'
    }
    assert day_11._update_seats(seats) == answer


def test_part_a():
    data = (
        'L.LL.LL.LL\n'
        'LLLLLLL.LL\n'
        'L.L.L..L..\n'
        'LLLL.LL.LL\n'
        'L.LL.LL.LL\n'
        'L.LLLLL.LL\n'
        '..L.L.....\n'
        'LLLLLLLLLL\n'
        'L.LLLLLL.L\n'
        'L.LLLLL.LL'
    )
    assert day_11.part_a(data) == 37


@pytest.mark.parametrize(
    'x, y, data, answer',
    [
        (1, 1, 'LLL\nLLL\nLLL', {(0,0), (1,0),(2,0),(0,3),(1,3),(2,3),(1,1),(1,3)}),
    ]
)
def test__find_seats_in_sight(x, y, data, answer):
    seats = day_11._parse_floor(data)
    assert day_11._find_seats_in_sight(x, y, seats) == answer