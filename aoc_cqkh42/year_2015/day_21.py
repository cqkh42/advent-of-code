import itertools
import math

import numpy as np
import parse

from aoc_cqkh42 import BaseSolution


WEAPONS = [
    np.array([8, 0, 4]),
    np.array([10, 0, 5]),
    np.array([25, 0, 6]),
    np.array([40, 0, 7]),
    np.array([74, 0, 8])
]


ARMORS = [
    np.array([13, 1, 0]),
    np.array([31, 2, 0]),
    np.array([53, 3, 0]),
    np.array([75, 4, 0]),
    np.array([102, 5, 0]),
    np.array([0, 0, 0])
]


RINGS = [
    np.array([25, 0, 1]),
    np.array([50, 0, 2]),
    np.array([100, 0, 3]),
    np.array([20, 1, 0]),
    np.array([40, 2, 0]),
    np.array([80, 3, 0]),
    np.array([0, 0, 0]),
    np.array([0, 0, 0])
]


def winner(boss_damage, player_damage, boss_health):
    player_health = 100
    damage_to_player = max(-boss_damage, 1)
    damage_to_boss = max(player_damage, 1)

    player_turns_needed = math.ceil(boss_health / damage_to_boss)
    boss_turns_needed = math.ceil(player_health / damage_to_player)
    return player_turns_needed <= boss_turns_needed


class Solution(BaseSolution):
    def parse_data(self):
        matches = parse.findall(r'{:d}', self.data)
        boss_health, *stats = [result[0] for result in matches]
        boss = np.array([0, *stats])*-1
        return boss, boss_health

    def part_a(self):
        cheapest = float('inf')
        for combo in itertools.product(WEAPONS, ARMORS, RINGS, RINGS):
            cost, *stats = np.sum(combo, 0) + self.parsed_data[0]
            if winner(*stats, self.parsed_data[1]):
                cheapest = min(cheapest, cost)
        return cheapest

    def part_b(self):
        priciest = 0
        for combo in itertools.product(WEAPONS, ARMORS, RINGS, RINGS):
            cost, *stats = np.sum(combo, 0) + self.parsed_data[0]
            if not winner(*stats, self.parsed_data[1]):
                priciest = max(priciest, cost)
        return priciest
