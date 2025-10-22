from aoc_cqkh42.helpers.graph import a_star
from aoc_cqkh42.year_2016.day_11 import ChipPair, ChipSet, Node
import pytest

_BARE_STATES = [
        (((0,1), (0,2)), 0),
        (((1,1), (0,2)), 1),
        (((2,2), (0,2)), 2),
        (((1,2), (0,2)), 1),
        (((0,2), (0,2)), 0),
        (((1,2), (1,2)), 1),
        (((2,2), (2,2)), 2),
        (((3,2), (3,2)), 3),
        (((2,2), (3,2)), 2),
        (((2,3), (3,3)), 3),
        (((2,3), (2,3)), 2),
        (((3,3), (3,3)), 3)
]
NODES = []
for pairs, floor in _BARE_STATES:
    pairs = [ChipPair(*pair) for pair in pairs]
    chipset = ChipSet(pairs, floor)
    node = Node(chipset, 1)
    NODES.append(node)

PAIRS = zip(NODES, NODES[1:])

@pytest.mark.parametrize("pair", PAIRS)
def test_states(pair):
    from_, to = pair
    neighbours = list(from_.neighbours())
    print(neighbours)
    assert to in neighbours

def test_part_a():
    chips = ChipSet([ChipPair(0, 1), ChipPair(0, 2)])
    start = Node(chips, 0)
    assert a_star.AStar(start).run() == 11


def test__neighbours():
    chips = ChipSet([ChipPair(0, 1), ChipPair(0, 2)])
    start = Node(chips, 0)
    neighbours = list(start._neighbours())
    expected = [
        Node(ChipSet([ChipPair(1, 1), ChipPair(0, 2)], 1), 1),
        Node(ChipSet([ChipPair(0, 1), ChipPair(1, 2)], 1), 1),
        Node(ChipSet([ChipPair(1, 1), ChipPair(1, 2)], 1), 1)
    ]
    assert neighbours == expected


def test_neighbours():
    chipsets = [
        ChipSet([ChipPair(1, 1), ChipPair(0, 2)], 1),
        ChipSet([ChipPair(0, 1), ChipPair(1, 2)], 1),
        ChipSet([ChipPair(1, 1), ChipPair(1, 2)], 1),
    ]
    assert [chipset.is_valid() for chipset in chipsets] == [True, False, False]
    assert len(set(chipsets)) == 3
    # assert neighbours == expected


def test_moves():
    chips = ChipSet([ChipPair(0, 1), ChipPair(0, 2)])
    start = Node(chips, 0)
    assert Node(ChipSet([ChipPair(1, 1), ChipPair(0, 2)], 1), 1) in list(
        start.neighbours())

def test_is_target():
    node = Node(ChipSet([ChipPair(3,3), ChipPair(3,3)], 3), 1)
    assert node.is_target()
