from dataclasses import dataclass, field
import itertools
import queue
import math


@dataclass
class Item:
    cost: int
    damage: int
    armor: int


# noinspection SpellCheckingInspection
weapons = [
    Item(8, 4, 0),
    Item(10, 5, 0),
    Item(25, 6, 0),
    Item(40, 7, 0),
    Item(74, 8, 0)
]


# noinspection SpellCheckingInspection
armors = [
    Item(13, 0, 1),
    Item(31, 0, 2),
    Item(53, 0, 3),
    Item(75, 0, 4),
    Item(102, 0, 5),
    Item(0, 0, 0)
]

rings = [
    Item(25, 1, 0),
    Item(50, 2, 0),
    Item(100, 3, 0),
    Item(20, 0, 1),
    Item(40, 0, 2),
    Item(80, 0, 3),
    Item(0, 0, 0),
    Item(0, 0, 0)
]


@dataclass(order=True)
class Items:
    player_damage: int = field(compare=False)
    player_armor: int = field(compare=False)
    boss_health: int = field(compare=False)
    boss_damage: int = field(compare=False)
    boss_armor: int = field(compare=False)
    cost: int

    def winner(self):
        player_health = 100
        damage_to_player = max(self.boss_damage - self.player_armor, 1)
        damage_to_boss = max(self.player_damage - self.boss_armor, 1)

        player_turns_needed = math.ceil(self.boss_health / damage_to_boss)
        boss_turns_needed = math.ceil(player_health / damage_to_player)
        return player_turns_needed <= boss_turns_needed


def part_a(data):
    boss_stats = data.split('\n')
    boss_stats = dict(stat.split(': ') for stat in boss_stats)
    boss_stats = {k: int(v) for k, v in boss_stats.items()}
    boss_damage = boss_stats['Damage']
    boss_health = boss_stats['Hit Points']
    boss_armor = boss_stats['Armor']

    options = queue.PriorityQueue()

    for weapon, armor, ring_a, ring_b in itertools.product(
            weapons, armors, rings, rings):
        damage = weapon.damage + ring_a.damage + ring_b.damage
        a = armor.armor + ring_a.armor + ring_b.armor
        total_cost = weapon.cost + armor.cost + ring_a.cost + ring_b.cost
        i = Items(damage, a, boss_health, boss_damage, boss_armor, total_cost)

        options.put(i)
    while options.not_empty:
        items = options.get()
        if items.winner():
            return items.cost


def part_b(data, **_):
    boss_stats = data.split('\n')
    boss_stats = dict(stat.split(': ') for stat in boss_stats)
    boss_stats = {k: int(v) for k, v in boss_stats.items()}
    boss_damage = boss_stats['Damage']
    boss_health = boss_stats['Hit Points']
    boss_armor = boss_stats['Armor']

    options = queue.PriorityQueue()

    for weapon, armor, ring_a, ring_b in itertools.product(
            weapons, armors, rings, rings):
        damage = weapon.damage + ring_a.damage + ring_b.damage
        a = armor.armor + ring_a.armor + ring_b.armor
        total_cost = weapon.cost + armor.cost + ring_a.cost + ring_b.cost
        i = Items(damage, a, boss_health, boss_damage, boss_armor, -total_cost)

        options.put(i)
    while options.not_empty:
        items = options.get()
        if not items.winner():
            return -items.cost
