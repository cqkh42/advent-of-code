from dataclasses import dataclass
import itertools


@dataclass
class Item:
    name: str
    cost: int
    damage: int
    armor: int


weapons = [
    Item('dagger', 8, 4, 0),
    Item('shortsword', 10, 5, 0),
    Item('warhammer', 25, 6, 0),
    Item('longsword', 40, 7, 0),
    Item('greataxe', 74, 8, 0)
]

armors = [
    Item('leather', 13, 0, 1),
    Item('chainmail', 31, 0, 2),
    Item('splintmail', 53, 0, 3),
    Item('bandedmail', 75, 0, 4),
    Item('platemail', 102, 0, 5),
    Item('none', 0, 0, 0)
]

rings = [
    Item('damage_+1', 25, 1, 0),
    Item('damage_+2', 50, 2, 0),
    Item('damage_+3', 100, 3, 0),
    Item('defence_+1', 20, 0, 1),
    Item('defence_+2', 40, 0, 2),
    Item('defence_+3', 80, 0, 3),
    Item('none', 0, 0, 0),
    Item('none', 0, 0, 0)
]


def winner(player_stats, boss_stats):
    player_health = player_stats['Hit Points']
    boss_health = boss_stats['Hit Points']
    damage_to_player = max(boss_stats["Damage"] - player_stats["Armor"], 1)
    damage_to_boss = max(player_stats["Damage"] - boss_stats["Armor"], 1)

    while True:
        boss_health -= damage_to_boss
        if boss_health <= 0:
            return 'player'
        player_health -= damage_to_player
        if player_health <= 0:
            return 'boss'


def part_a(data):
    boss_stats = data.split('\n')
    boss_stats = dict(stat.split(': ') for stat in boss_stats)
    boss_stats = {k: int(v) for k, v in boss_stats.items()}

    cost = float('inf')
    weapon_armor_combos = itertools.product(weapons, armors)
    ring_options = itertools.combinations(rings, 2)

    for (weapon, armor), (ring_a, ring_b) in itertools.product(
            weapon_armor_combos, ring_options):
        player_stats = {
            'Damage': weapon.damage + ring_a.damage + ring_b.damage,
            'Armor': armor.armor + ring_a.armor + ring_b.armor,
            'Hit Points': 100
        }
        if winner(player_stats, boss_stats) == 'player':
            total_cost = weapon.cost + armor.cost + ring_a.cost + ring_b.cost
            cost = min(total_cost, cost)

    return cost


def part_b(data, **_):
    boss_stats = data.split('\n')
    boss_stats = dict(stat.split(': ') for stat in boss_stats)
    boss_stats = {k: int(v) for k, v in boss_stats.items()}

    cost = 0
    weapon_armor_combos = itertools.product(weapons, armors)
    ring_options = itertools.combinations(rings, 2)

    for (weapon, armor), (ring_a, ring_b) in itertools.product(
            weapon_armor_combos, ring_options):
        player_stats = {
            'Damage': weapon.damage + ring_a.damage + ring_b.damage,
            'Armor': armor.armor + ring_a.armor + ring_b.armor,
            'Hit Points': 100
        }
        if winner(player_stats, boss_stats) == 'boss':
            total_cost = weapon.cost + armor.cost + ring_a.cost + ring_b.cost
            cost = max(total_cost, cost)

    return cost
