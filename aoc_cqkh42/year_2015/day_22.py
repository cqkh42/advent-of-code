from copy import copy
from dataclasses import dataclass, field
import queue

import parse


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
        if not getattr(self, name):
            state = copy(self)
            setattr(state, name, duration)
            state.mana -= mana
            state.used_mana += mana
            return state
        else:
            state = copy(self)
            state.player_health = -100
            return state

    def buff(self):
        self.boss_health -= 3 * (self.poison > 0)
        self.mana += 101 * (self.recharge > 0)
        self.player_armor = 7 * (self.shield > 0)

        self.poison = max(self.poison-1, 0)
        self.recharge = max(self.recharge-1, 0)
        self.shield = max(self.shield-1, 0)

    def cast_attack(self, mana, boss_change=0, player_change=0):
        state = copy(self)
        state.player_health += player_change
        state.boss_health -= boss_change
        state.mana -= mana
        state.used_mana += mana
        return state

    def boss_attack(self):
        self.player_health -= self.boss_damage - self.player_armor

    def is_valid(self):
        return self.mana >= 0 and self.player_health > 0

    def is_complete(self):
        return self.boss_health <= 0

    def _next_moves(self):
        self.buff()
        casts = (self.cast_attack(*stats) for stats in [(53, 4, 0), (73, 2, 2)])
        effects = (
            self.cast_effect(name, duration, mana) for
            name, (duration, mana) in EFFECT_STATS.items()
        )
        new_states = (*casts, *effects)
        new_states = (state for state in new_states if state.is_valid())

        for new_state in new_states:
            new_state.buff()
            new_state.boss_attack()
            yield new_state

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
        z = state.next_moves()
        for i in z:
            if i.is_complete():
                return i.used_mana
            states.put(i)


def part_a(data):
    boss_health, boss_damage = parse.parse(
        'Hit Points: {:d}\nDamage: {:d}', data
    )
    starting_state = State(PLAYER_HEALTH, boss_health, PLAYER_MANA, boss_damage)
    return a_star(starting_state)


def part_b(data, **_):
    boss_health, boss_damage = parse.parse(
        'Hit Points: {:d}\nDamage: {:d}', data
    )
    starting_state = StateB(PLAYER_HEALTH, boss_health, PLAYER_MANA, boss_damage)
    starting_state.player_health -= 1
    return a_star(starting_state)
