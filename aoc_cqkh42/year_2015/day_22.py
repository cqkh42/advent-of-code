from copy import deepcopy, copy
from dataclasses import dataclass

import parse


PLAYER_HEALTH = 50
PLAYER_MANA = 500
EFFECT_STATS = {
    # (duration, mana)
    'shield': (6, 113),
    'poison': (6, 173),
    'recharge': (5, 229)
}


@dataclass
class State:
    player_health: int
    boss_health: int
    mana: int
    boss_damage: int
    used_mana: int = 0
    poison: int = 0
    recharge: int = 0
    shield: int = 0

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
            if state.mana >= 0 and state.player_health > 0:
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
        if state.mana >= 0 and state.player_health > 0:
            return state

    def boss_attack(self):
        self.player_health -= self.boss_damage - self.player_armor


def mm(state, cheapest_victory):
    states = []
    state.buff()
    casts = (state.cast_attack(*stats) for stats in [(53, 4, 0), (73, 2, 2)])
    effects = (
        state.cast_effect(name, duration, mana) for
        name, (duration, mana) in EFFECT_STATS.items()
    )
    new_states = (*casts, *effects)
    new_states = (
        state for state in new_states
        if state and state.used_mana < cheapest_victory
    )

    for new_state in new_states:
        new_state.buff()
        new_state.boss_attack()
        if new_state.boss_health <= 0:
            cheapest_victory = min(cheapest_victory, new_state.used_mana)
            continue
        if new_state.player_health > 0:
            states.append(new_state)
    return states, cheapest_victory


def part_a(data):
    boss_health, boss_damage = parse.parse('Hit Points: {:d}\nDamage: {:d}', data)

    cheapest_victory = float('inf')
    states = {
        State(PLAYER_HEALTH, boss_health, PLAYER_MANA, boss_damage)
    }
    seen = set()

    while states:
        state = states.pop()
        if state in seen:
            continue
        else:
            seen.add(state)
        z, cheapest_victory = mm(state, cheapest_victory)
        z = set(z)
        states.update(z)

    return cheapest_victory


def part_b(data, **_):
    boss_health, boss_damage = parse.parse('Hit Points: {:d}\nDamage: {:d}',
                                           data)

    cheapest_victory = float('inf')
    states = {
        State(PLAYER_HEALTH, boss_health, PLAYER_MANA, boss_damage)
    }
    seen = set()

    while states:
        state = states.pop()
        state.player_health -= 1
        if state in seen:
            continue
        else:
            seen.add(state)
        z, cheapest_victory = mm(state, cheapest_victory)
        z = set(z)
        states.update(z)

    return cheapest_victory
