import pytest

from aoc_cqkh42.year_2019 import day_03


@pytest.mark.xfail
@pytest.mark.parametrize(
    "data, answer",
    [
        (
                "R3,U1,L2,D1",
                [(1, 0), (2, 0), (3, 0), (3, 1), (2, 1), (1, 1), (1, 0)],
        ),
        (
                "R10",
                [
                    (1, 0),
                    (2, 0),
                    (3, 0),
                    (4, 0),
                    (5, 0),
                    (6, 0),
                    (7, 0),
                    (8, 0),
                    (9, 0),
                    (10, 0),
                ],
        ),
    ],
)
def test__build_route(data, answer):
    assert list(day_03._build_route(data)) == answer


@pytest.mark.xfail
@pytest.mark.parametrize(
    "data, answer",
    [
        ("R8,U5,L5,D3\nU7,R6,D4,L4", 6),
        (
                "R75,D30,R83,U83,L12,D49,R71,U7,L72\n"
                "U62,R66,U55,R34,D71,R55,D58,R83",
                159,
        ),
        (
                "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\n"
                "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
                135,
        ),
    ],
)
def test_part_a(data, answer):
    assert day_03.part_a(data) == answer


@pytest.mark.xfail
@pytest.mark.parametrize(
    "data, answer",
    [
        ("R8,U5,L5,D3\nU7,R6,D4,L4", 30),
        (
                "R75,D30,R83,U83,L12,D49,R71,U7,L72\n"
                "U62,R66,U55,R34,D71,R55,D58,R83",
                610,
        ),
        (
                "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\n"
                "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
                410,
        ),
    ],
)
def test_part_b(data, answer):
    assert day_03.part_b(data) == answer
