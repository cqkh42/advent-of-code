from aoc_cqkh42.year_2016 import day_11

from pytest import mark
from aoc_cqkh42.helpers.graph import a_star



@mark.parametrize(
    ('lift', 'expected'),
    ((-1, False), (2, True), (4, False))
)
def test_node_is_valid_lift(lift, expected):
    node = day_11.Node((1,), (1,), lift, 0)
    assert node.is_valid() == expected


@mark.parametrize(
    ('chip', 'expected'),
    ((-1, False), (2, True), (4, False))
)
def test_node_is_valid_chips(chip, expected):
    node = day_11.Node((1,), (chip,), 0, 0)
    assert node.is_valid() is expected

# loose, no, protected
@mark.parametrize(
    ('generators', 'chips', 'expected'),
    (
        ((1, 0), (1, 1), False),  # loose chip with a gen
        ((1,1), (1, 1), True)  # protected chip with a gen
    )
)
def test_is_valid_loose_chip(generators, chips, expected):
    node = day_11.Node(generators, chips, 1, 0)
    assert node.is_valid() is expected


@mark.parametrize(
    ('generator', 'expected'),
    ((-1, False), (2, True), (4, False))
)
def test_node_is_valid_generators(generator, expected):
    node = day_11.Node((generator,), (0,), 0, 0)
    assert node.is_valid() == expected


def test_simple_neighbours_floor_0():
    node = day_11.Node((0,), (0,), 0, 0)
    expected = {
        day_11.Node((0,), (1,), 1, 1),
        day_11.Node((1,), (1,), 1, 1),
        day_11.Node((1,), (0,), 1, 1),
    }
    output = {node for node in node.neighbours()}
    assert output == expected


def test_simple_neighbours_floor_1():
    node = day_11.Node((1,), (1,), 1, 0)
    expected = {
        day_11.Node((0,), (1,), 0, 1),
        day_11.Node((0,), (0,), 0, 1),
        day_11.Node((1,), (0,), 0, 1),
        day_11.Node((2,), (1,), 2, 1),
        day_11.Node((2,), (2,), 2, 1),
        day_11.Node((1,), (2,), 2, 1),
    }
    output = {node for node in node.neighbours()}
    assert output == expected


def test_simple_neighbours_floor_3():
    node = day_11.Node((3,), (3,), 3, 0)
    expected = {
        day_11.Node((3,), (2,), 2, 1),
        day_11.Node((2,), (2,), 2, 1),
        day_11.Node((2,), (3,), 2, 1),
    }
    output = {node for node in node.neighbours()}
    assert output == expected


def test_neighbours_just_chips():
    node = day_11.Node(
        generators=(2, 2), chips=(0, 0), lift=0, distance=4
    )
    expected = {
        day_11.Node((2, 2), (0, 1), 1, 5),
        day_11.Node((2, 2), (1, 1), 1, 5),
        day_11.Node((2, 2), (1, 0), 1, 5),
    }
    output = {node for node in node.neighbours()}
    assert output == expected


def test_part_a_stepwise_neighbours():
    states = [
        day_11.Node((1, 2), (0, 0), 0, 0),
        day_11.Node((1, 2), (1, 0), 1, 1),
        day_11.Node((2, 2), (2, 0), 2, 2),
        day_11.Node((2, 2), (1, 0), 1, 3),
        day_11.Node((2, 2), (0, 0), 0, 4),
        day_11.Node((2, 2), (1, 1), 1, 5),
        day_11.Node((2, 2), (2, 2), 2, 6),
        day_11.Node((2, 2), (3, 3), 3, 7),
        day_11.Node((2, 2), (2, 3), 2, 8),
        day_11.Node((3, 3), (2, 3), 3, 9),
        day_11.Node((3, 3), (2, 2), 2, 10),
        day_11.Node((3, 3), (3, 3), 3, 11),
    ]
    for node, neighbour in zip(states, states[1:]):
        neighbours = {node for node in node.neighbours()}
        assert neighbour in neighbours


def test_part_a_small():
    node = day_11.Node((1, 2), (0, 0), 0, 0)
    target = day_11.Node((3, 3), (3, 3), 3, 0)

    assert a_star.AStar(node, target).run() == 11


