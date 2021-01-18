from dataclasses import dataclass, field
import itertools
import queue
import math


@dataclass(order=True)
class Stats:
    cost: int
    player_damage: int = field(compare=False)
    boss_damage: int = field(compare=False)

    def __add__(self, other):
        if isinstance(other, Stats):
            cost = self.cost + other.cost
            damage = self.player_damage + other.player_damage
            armor = self.boss_damage + other.boss_damage
            return Stats(cost, damage, armor)
        else:
            raise TypeError

    def winner(self, boss_health):
        player_health = 100
        damage_to_player = max(-self.boss_damage, 1)
        damage_to_boss = max(self.player_damage, 1)

        player_turns_needed = math.ceil(boss_health / damage_to_boss)
        boss_turns_needed = math.ceil(player_health / damage_to_player)
        return player_turns_needed <= boss_turns_needed


# noinspection SpellCheckingInspection
weapons = [
    Stats(8, 4, 0),
    Stats(10, 5, 0),
    Stats(25, 6, 0),
    Stats(40, 7, 0),
    Stats(74, 8, 0)
]


# noinspection SpellCheckingInspection
armors = [
    Stats(13, 0, 1),
    Stats(31, 0, 2),
    Stats(53, 0, 3),
    Stats(75, 0, 4),
    Stats(102, 0, 5),
    Stats(0, 0, 0)
]

rings = [
    Stats(25, 1, 0),
    Stats(50, 2, 0),
    Stats(100, 3, 0),
    Stats(20, 0, 1),
    Stats(40, 0, 2),
    Stats(80, 0, 3),
    Stats(0, 0, 0),
    Stats(0, 0, 0)
]

def _parse_data(data):
    boss_stats = data.split('\n')
    boss_stats = dict(stat.split(': ') for stat in boss_stats)
    boss_stats = {k: int(v) for k, v in boss_stats.items()}
    boss_damage = boss_stats['Damage']
    boss_health = boss_stats['Hit Points']
    boss_armor = boss_stats['Armor']

    boss = Stats(0, -boss_armor, -boss_damage)
    return boss, boss_health

def part_a(data):
    boss, boss_health = _parse_data(data)

    options = queue.PriorityQueue()

    for items in itertools.product(weapons, armors, rings, rings):
        options.put(sum(items, boss))

    while options.not_empty:
        items = options.get()
        if items.winner(boss_health):
            return items.cost


def part_b(data, **_):
    boss, boss_health = _parse_data(data)
    options = queue.PriorityQueue()

    for items in itertools.product(weapons, armors, rings, rings):
        t = sum(items, boss)
        t.cost *= -1
        options.put(t)

    while options.not_empty:
        items = options.get()
        if not items.winner(boss_health):
            return -items.cost
