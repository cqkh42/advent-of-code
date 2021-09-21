# TODO A* Class
from dataclasses import dataclass, field, replace
import queue

from dataclass_property import field_property
import parse


from aoc_cqkh42 import BaseSolution


class Solution(BaseSolution):
    def parse_data(self):
        boss_health, boss_damage = parse.parse(
            'Hit Points: {:d}\nDamage: {:d}', self.data
        )
        return boss_health, boss_damage

    def part_a(self):
        boss_health, boss_damage = self.parsed_data
        starting_state = State(PLAYER_HEALTH, boss_health,
                               boss_damage, PLAYER_MANA)
        return dijkstra(starting_state)

    def part_b(self):
        boss_health, boss_damage = self.parsed_data
        starting_state = StateB(PLAYER_HEALTH, boss_health,
                                boss_damage, PLAYER_MANA)
        return dijkstra(starting_state)


PLAYER_HEALTH = 50
PLAYER_MANA = 500
EFFECT_STATS = {
    # (duration, mana)
    'shield': (6, 113),
    'poison': (6, 173),
    'recharge': (5, 229)
}


@dataclass(unsafe_hash=True, eq=True, order=True)
class State:
    player_health: int = field(compare=False, hash=True)
    boss_health: int = field(compare=False)
    boss_damage: int = field(compare=False)
    mana: int = field(compare=False)
    used_mana: int = field(default=0, compare=True)
    poison: int = field(default=0, compare=False)
    recharge: int = field(default=0, compare=False)
    shield: int = field(default=0, compare=False)
    # player_armor: int = field(default=0, compare=False)
    travelled: int = field(default=0, compare=False)

    @property
    def player_armor(self):
        return 7 * (self.shield > 0)

    def cast_effect(self, name, duration, mana):
        state = replace(
            self,
            mana=self.mana-mana,
            used_mana=self.used_mana+mana,
            **{name: duration}
        )
        return state

    def buff(self):
        self.boss_health -= 3 * (self.poison > 0)
        self.mana += 101 * (self.recharge > 0)

        self.poison = max(self.poison-1, 0)
        self.recharge = max(self.recharge-1, 0)
        self.shield = max(self.shield-1, 0)
        return self

    def cast_attack(self, mana, boss_change=0, player_change=0):
        return replace(
            self,
            player_health=self.player_health+player_change,
            boss_health=self.boss_health-boss_change,
            mana=self.mana-mana,
            used_mana=self.used_mana+mana
        )

    def attack_neighbours(self):
        return (self.cast_attack(*stats) for stats in [(53, 4, 0), (73, 2, 2)] if self.mana >= stats[0])

    def boss_attack(self):
        self.player_health -= self.boss_damage - self.player_armor
        return self

    def is_target(self):
        return self.boss_health <= 0

    def neighbours(self):
        a = self.buff()
        effects = (
            a.cast_effect(name, duration, mana) for
            name, (duration, mana) in EFFECT_STATS.items()
            if not getattr(a, name) and a.mana >= mana
        )
        new_states = (*self.attack_neighbours(), *effects)
        new_states = (state.buff() for state in new_states)
        new_states = (state.boss_attack() for state in new_states)
        new_states = (state for state in new_states if state.player_health > 0 or state.boss_health <= 0)

        yield from new_states


class StateB(State):
    def neighbours(self):
        self.player_health -= 1
        a = self.buff()
        attacks = (a.cast_attack(*stats) for stats in [(53, 4, 0), (73, 2, 2)]
                   if a.mana >= stats[0])
        effects = (
            a.cast_effect(name, duration, mana) for
            name, (duration, mana) in EFFECT_STATS.items()
            if not getattr(a, name) and a.mana >= mana
        )
        new_states = (*attacks, *effects)
        new_states = (state.buff() for state in new_states)
        new_states = (state.boss_attack() for state in new_states)
        new_states = (state for state in new_states if
                      state.player_health > 0 or state.boss_health <= 0)
        yield from new_states


def dijkstra(start):
    frontier = queue.PriorityQueue()

    frontier.put(start)
    visited = set()

    while frontier.not_empty:
        node = frontier.get()
        if node in visited:
            continue
        if node.is_target():
            return node.used_mana
        visited.add(node)
        for neighbour in node.neighbours():
            frontier.put(neighbour)
