from aoc_cqkh42.helpers.graph.a_star import AStarBaseNode

import pytest


class Empty(AStarBaseNode):
    def __init__(self):
        pass


class Complete(AStarBaseNode):
    def __init__(self, d, h):
        self.distance = d
        self._h = h

    def h(self):
        return self._h


def test_missing_raises():
    with pytest.raises(TypeError):
        Empty()

@pytest.mark.parametrize(
    ['left', 'right'],
    [
        (Complete(1, 0), Complete(0, 0)),
        (Complete(0, 1), Complete(0, 0))
    ]

)
def test_gt_true(left, right):
    assert left > right