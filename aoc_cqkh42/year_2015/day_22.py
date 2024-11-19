from dataclasses import dataclass, replace

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution
from aoc_cqkh42.helpers.graph.a_star import AStar, BaseNode


class Solution(BaseSolution):
    def part_a(self):
        starting_state = State(PLAYER_HEALTH, *self.numbers, PLAYER_MANA)
        return AStar(starting_state).run()

    def part_b(self):
        starting_state = State(PLAYER_HEALTH, *self.numbers, PLAYER_MANA, hard_mode=True)
        return AStar(starting_state).run()


PLAYER_HEALTH = 50
PLAYER_MANA = 500
EFFECT_STATS = [
    # (duration, mana)
    ("shield", 6, 113),
    ("poison", 6, 173),
    ("recharge", 5, 229),
]

def effect_moves(node):
    attacks = [
        node.cast_effect(name, duration, mana) for name, duration, mana in
        EFFECT_STATS
        if not getattr(node, name) and node.mana >= mana
    ]
    return attacks

def attack_moves(node):
    new_states = (
        node.cast_attack(*stats)
        for stats in [(53, 4, 0), (73, 2, 2)]
        if node.mana >= stats[0]
    )
    return new_states

@dataclass(frozen=True)
class State(BaseNode):
    player_health: int
    boss_health: int
    boss_damage: int
    mana: int
    hard_mode: bool = False
    distance: int = 0
    poison: int = 0
    recharge: int = 0
    shield: int = 0

    def cast_effect(self, name, duration, mana):
        state = replace(
            self,
            mana=self.mana - mana,
            distance=self.distance + mana,
            **{name: duration},
        )
        return state

    def cast_attack(self, mana, boss_change=0, player_change=0):
        return replace(
            self,
            player_health=self.player_health + player_change,
            boss_health=self.boss_health - boss_change,
            mana=self.mana - mana,
            distance=self.distance + mana,
        )

    def buff(self):
        return replace(
            self,
            boss_health=self.boss_health - (3 * (self.poison > 0)),
            mana=self.mana + (101 * (self.recharge > 0)),
            poison=max(self.poison - 1, 0),
            recharge=max(self.recharge - 1, 0),
            shield=max(self.shield - 1, 0),
        )

    def boss_attack(self):
        armour = 7 * (self.shield > 0)
        return replace(
            self.buff(),
            player_health=self.player_health - self.boss_damage + armour,
        )

    def is_target(self):
        return self.boss_health <= 0

    def _n(self):
        buffed = self.buff()
        effect_states = effect_moves(buffed)
        attack_states = attack_moves(buffed)
        a =  *attack_states, *effect_states
        new_states = (state.boss_attack() for state in a)
        new_states = (
            state for state in new_states
            if state.player_health > 0 or state.is_target()
        )
        return new_states

    def neighbours(self):
        if not self.hard_mode:
            yield from self._n()
        else:
            a = replace(self, player_health=self.player_health - 1)
            if a.player_health <= 0:
                return []
            yield from a._n()


if __name__ == "__main__":
    submit_answers(Solution, 22, 2015)
