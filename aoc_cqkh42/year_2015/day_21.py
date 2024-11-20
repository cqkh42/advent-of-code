import itertools
import math

import numpy as np

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

WEAPONS = [
    np.array([8, 0, 4]),
    np.array([10, 0, 5]),
    np.array([25, 0, 6]),
    np.array([40, 0, 7]),
    np.array([74, 0, 8]),
]


ARMORS = [
    np.array([13, 1, 0]),
    np.array([31, 2, 0]),
    np.array([53, 3, 0]),
    np.array([75, 4, 0]),
    np.array([102, 5, 0]),
    np.array([0, 0, 0]),
]


RINGS = [
    np.array([25, 0, 1]),
    np.array([50, 0, 2]),
    np.array([100, 0, 3]),
    np.array([20, 1, 0]),
    np.array([40, 2, 0]),
    np.array([80, 3, 0]),
    np.array([0, 0, 0]),
    np.array([0, 0, 0]),
]


class Solution(BaseSolution):
    def _parse(self):
        boss_health, *stats = self.numbers
        boss = np.array([0, *stats]) * -1

        p = [
            np.sum(combo, 0) + boss
            for combo in itertools.product(WEAPONS, ARMORS, RINGS, RINGS)
        ]
        return p

    def winner(self, boss_damage, player_damage):
        player_health = 100
        damage_to_player = max(-boss_damage, 1)
        damage_to_boss = max(player_damage, 1)

        player_turns_needed = math.ceil(self.numbers[0] / damage_to_boss)
        boss_turns_needed = math.ceil(player_health / damage_to_player)
        return player_turns_needed <= boss_turns_needed

    def part_a(self):
        return str(min(cost for cost, *stats in self.parsed if self.winner(*stats)))

    def part_b(self):
        return str(
            max(cost for cost, *stats in self.parsed if not self.winner(*stats))
        )


if __name__ == "__main__":
    submit_answers(Solution, 21, 2015)
