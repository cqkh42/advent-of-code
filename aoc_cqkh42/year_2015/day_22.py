# TODO abstract dijkstra
# TODO abstract search
from dataclasses import dataclass, field, replace

import parse

from aoc_cqkh42 import BaseSolution
from aoc_cqkh42.helpers.dijkstra import dijkstra


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
        return replace(
            self,
            boss_health=self.boss_health - (3 * (self.poison > 0)),
            mana=self.mana + (101 * (self.recharge > 0)),
            poison = max(self.poison-1, 0),
            recharge = max(self.recharge-1, 0),
            shield = max(self.shield-1, 0)
        )

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

    def effect_moves(self):
        for name, (duration, mana) in EFFECT_STATS.items():
            a = self.buff()
            if not getattr(a, name) and a.mana >= mana:
                a = a.cast_effect(name, duration, mana).buff().boss_attack()
                if a.player_health > 0 or a.is_target():
                    yield a

    def attack_moves(self):
        b = self.buff()
        new_states = b.attack_neighbours()
        new_states = (state.buff() for state in new_states)
        new_states = (state.boss_attack() for state in new_states)
        new_states = (state for state in new_states if
                      state.player_health > 0 or state.is_target())
        return new_states

    def _n(self):
        effect_states = self.effect_moves()
        attack_states = self.attack_moves()
        return *attack_states, *effect_states

    def neighbours(self):
        yield from self._n()


class StateB(State):
    def neighbours(self):
        self.player_health -= 1
        yield from self._n()


