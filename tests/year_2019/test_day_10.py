import pytest

from aoc_cqkh42.year_2019 import day_10


@pytest.mark.xfail
@pytest.mark.parametrize(
    "data, answer",
    [("#", {(0, 0)}), (".#", {(1, 0)}), ("..\n##", {(1, 1), (0, 1)})],
)
def test__find_asteroids(data, answer):
    assert day_10._find_asteroids(data) == answer


@pytest.mark.xfail
@pytest.mark.parametrize(
    "origin, asteroids, answer",
    [
        ((1, 0), {(0, 0), (1, 0), (2, 0)}, {(2, 0), (0, 0)}),
        ((1, 0), {(0, 0), (1, 0), (2, 0), (3, 0)}, {(2, 0), (0, 0)}),
        (
                (3, 4),
                {
                    (1, 0),
                    (4, 0),
                    (0, 2),
                    (1, 2),
                    (2, 2),
                    (3, 2),
                    (4, 2),
                    (4, 4),
                    (4, 5),
                    (3, 4),
                },
                {(4, 0), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (4, 4),
                 (4, 5)},
        ),
    ],
)
def test__asteroids_in_sight(origin, asteroids, answer):
    assert day_10._asteroids_in_sight(origin, asteroids) == answer


@pytest.mark.parametrize(
    "origin, other, answer",
    [
        ((1, 1), (1, 0), 0),
        ((1, 1), (2, 1), 90),
        ((1, 1), (1, 2), 180),
        ((1, 1), (0, 1), 270),
        ((1, 1), (2, 0), 45),
        ((1, 1), (2, 2), 135),
        ((1, 1), (0, 2), 225),
        ((1, 1), (0, 0), 315),
        ((1, 1), (1, 1), -180),
    ],
)
def test__angle(origin, other, answer):
    assert day_10._angle(origin, other) == answer


@pytest.mark.xfail
def test_part_a():
    asteroids = ".#..#\n" ".....\n" "#####\n" "....#\n" "...##\n"
    assert day_10.part_a(asteroids) == 8
