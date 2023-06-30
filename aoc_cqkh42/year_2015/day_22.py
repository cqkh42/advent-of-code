# TODO abstract dijkstra
# TODO abstract search
from dataclasses import dataclass, replace
from typing import Self

from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42.helpers.graph.dijkstra import dijkstra


class Solution(BaseSolution):
    def part_a(self):
        starting_state = State(PLAYER_HEALTH, *self.numbers, PLAYER_MANA)
        return dijkstra(starting_state)

    def part_b(self):
        starting_state = StateB(PLAYER_HEALTH, *self.numbers, PLAYER_MANA)
        return dijkstra(starting_state)

    def _process_data(self: Self) -> str:
        return self.input_


PLAYER_HEALTH = 50
PLAYER_MANA = 500
EFFECT_STATS = {
    # (duration, mana)
    "shield": (6, 113),
    "poison": (6, 173),
    "recharge": (5, 229),
}


@dataclass(frozen=True)
class State:
    player_health: int
    boss_health: int
    boss_damage: int
    mana: int
    used_mana: int = 0
    poison: int = 0
    recharge: int = 0
    shield: int = 0
    travelled: int = 0

    def __eq__(self, other):
        # TODO there is a way to get rid of these using eq and compare
        return self.used_mana == other.used_mana

    def __lt__(self, other):
        return self.used_mana < other.used_mana

    def __le__(self, other):
        return self.used_mana <= other.used_mana

    def __gt__(self, other):
        return self.used_mana > other.used_mana

    def __ge__(self, other):
        return self.used_mana >= other.used_mana

    @property
    def player_armor(self):
        return 7 * (self.shield > 0)

    def cast_effect(self, name, duration, mana):
        state = replace(
            self,
            mana=self.mana - mana,
            used_mana=self.used_mana + mana,
            **{name: duration},
        )
        return state

    def buff(self):
        return replace(
            self,
            boss_health=self.boss_health - (3 * (self.poison > 0)),
            mana=self.mana + (101 * (self.recharge > 0)),
            poison=max(self.poison - 1, 0),
            recharge=max(self.recharge - 1, 0),
            shield=max(self.shield - 1, 0),
        )

    def cast_attack(self, mana, boss_change=0, player_change=0):
        return replace(
            self,
            player_health=self.player_health + player_change,
            boss_health=self.boss_health - boss_change,
            mana=self.mana - mana,
            used_mana=self.used_mana + mana,
        )

    def attack_neighbours(self):
        return (
            self.cast_attack(*stats)
            for stats in [(53, 4, 0), (73, 2, 2)]
            if self.mana >= stats[0]
        )

    def boss_attack(self):
        return replace(
            self,
            player_health=self.player_health - self.boss_damage + self.player_armor,
        )

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
        new_states = (
            state
            for state in new_states
            if state.player_health > 0 or state.is_target()
        )
        return new_states

    def _n(self):
        effect_states = self.effect_moves()
        attack_states = self.attack_moves()
        return *attack_states, *effect_states

    def neighbours(self):
        yield from self._n()


class StateB(State):
    def neighbours(self):
        a = replace(self, player_health=self.player_health - 1)
        if a.player_health <= 0:
            return []
        yield from a._n()
