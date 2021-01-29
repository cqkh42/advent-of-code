from dataclasses import dataclass, field, replace
import queue

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
        starting_state = State(PLAYER_HEALTH, boss_health, PLAYER_MANA,
                               boss_damage)
        return a_star(starting_state)

    def part_b(self):
        boss_health, boss_damage = self.parsed_data
        starting_state = StateB(PLAYER_HEALTH, boss_health, PLAYER_MANA,
                                boss_damage)
        return a_star(starting_state)

PLAYER_HEALTH = 50
PLAYER_MANA = 500
EFFECT_STATS = {
    # (duration, mana)
    'shield': (6, 113),
    'poison': (6, 173),
    'recharge': (5, 229)
}


@dataclass(order=True)
class State:
    player_health: int=field(compare=False)
    boss_health: int=field(compare=False)
    mana: int=field(compare=False)
    boss_damage: int=field(compare=False)
    used_mana: int = 0
    poison: int = field(default=0, compare=False)
    recharge: int = field(default=0, compare=False)
    shield: int=field(default=0, compare=False)


    player_armor: int = 0

    def __hash__(self):
        return hash(
            (self.player_health, self.boss_health, self.mana, self.poison, self.recharge, self.shield)
        )

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
        self.player_armor = 7 * (self.shield > 0)

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

    def boss_attack(self):
        # self.buff()
        self.player_health -= self.boss_damage - self.player_armor
        return self

    def is_complete(self):
        return self.boss_health <= 0

    def _next_moves(self):
        self.buff()
        attacks = (self.cast_attack(*stats) for stats in [(53, 4, 0), (73, 2, 2)] if self.mana >= stats[0])
        effects = (
            self.cast_effect(name, duration, mana) for
            name, (duration, mana) in EFFECT_STATS.items()
            if not getattr(self, name) and self.mana >= mana
        )
        new_states = (*attacks, *effects)
        new_states = (state.buff() for state in new_states)
        new_states = (state.boss_attack() for state in new_states)
        new_states = (state for state in new_states if state.player_health > 0 or state.boss_health <= 0)

        yield from new_states


    def next_moves(self):
        yield from self._next_moves()


class StateB(State):
    def next_moves(self):
        self.player_health -= 1
        yield from self._next_moves()


def a_star(state):
    states = queue.PriorityQueue()

    states.put(state)
    seen = set()

    while states.not_empty:
        state = states.get()
        if state in seen:
            continue
        else:
            seen.add(state)
        neighbours = state.next_moves()
        if state.is_complete():
            return state.used_mana
        for neighbour in neighbours:
            states.put(neighbour)



