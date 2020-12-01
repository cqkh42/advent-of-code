from dataclasses import dataclass


class Player:
    def __init__(self, health, mana, armour):
        self.health = health
        self._mana = mana
        self.armour = armour
        self.used_mana = 0

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, mana):
        self.used_mana += (self._mana - mana)
        self.mana = mana




@dataclass
class State:
    player_health: int
    boss_health: int
    mana: int
    used_mana: int
    player_armor: int
    effects: dict
    boss_damage: int

    EFFECT_STATS = {
        'shield': {'duration': 6, 'mana': 113},
        'poison': {'duration': 6, 'mana': 173},
        'recharge': {'duration': 5, 'mana': 229}
    }

    def change(self, **kwargs):
        d = {
            "player_health": self.player_health,
            "boss_health": self.boss_health,
            "mana": self.mana,
            "used_mana": self.used_mana,
            "player_armor": self.player_armor,
            "effects": self.effects,
            "boss_damage": self.boss_damage
        }
        d.update(kwargs)
        state = State(**d)
        if state.mana >= 0 and state.player_health > 0:
            return state

    def use_mana(self, mana):
        state = self.change(
            mana=self.mana - mana,
            used_mana=self.used_mana + mana
        )
        return state

    def add_effect(self, name):
        if name not in self.effects:
            stats = self.EFFECT_STATS[name]
            new = {name: stats['duration']}
            new.update(self.effects)
            return self.change(
                effects=new,
                mana=self.mana - stats['mana'],
                used_mana=self.used_mana + stats['mana']
            )

    def buff(self):
        self.boss_health = self.boss_health - 3 * (
                'poison' in self.effects)
        self.mana = self.mana + 101 * ('recharge' in self.effects)
        self.player_armor = 7 * ('shield' in self.effects)
        self.effects = {effect: turns - 1 for effect, turns in
                        self.effects.items() if turns > 1}

    def cast(self, mana, boss_change=0, player_change=0):
        state = self.change(
            player_health=self.player_health + player_change,
            boss_health=self.boss_health + boss_change,
            mana=self.mana - mana,
            used_mana=self.used_mana + mana
        )
        return state

    def boss_attack(self):
        self.player_health -= self.boss_damage
        self.player_health += self.player_armor

def part_a(data):
    player_health = 50
    player_mana = 500
    boss_stats = data.split('\n')
    boss_stats = dict(stat.split(': ') for stat in boss_stats)
    boss_stats = {k: int(v) for k, v in boss_stats.items()}
    boss_health = boss_stats['Hit Points']
    boss_damage = boss_stats['Damage']

    cheapest_victory = float('inf')
    states = [State(player_health, boss_health, player_mana, 0, 0, {}, boss_damage)]

    for state in states:
        state.buff()
        casts = (state.cast(*stats) for stats in [(53, -4, 0), (73, -2, +2)])
        effects = (state.add_effect(name) for name in
                   ['shield', 'poison', 'recharge'])
        new_states = (*casts, *effects)
        new_states = (state for state in new_states if state and state.used_mana < cheapest_victory)

        for new_state in new_states:
            new_state.buff()
            new_state.boss_attack()
            if new_state.boss_health <= 0:
                cheapest_victory = min(cheapest_victory, new_state.used_mana)
                continue
            if new_state.player_health > 0:
                states.append(new_state)

    return cheapest_victory


def part_b(data, **_):
    player_health = 50
    player_mana = 500

    boss_stats = data.split('\n')
    boss_stats = dict(stat.split(': ') for stat in boss_stats)
    boss_stats = {k: int(v) for k, v in boss_stats.items()}
    boss_health = boss_stats['Hit Points']
    boss_damage = boss_stats['Damage']

    cheapest_victory = float('inf')
    states = [State(player_health, boss_health, player_mana, 0, 0, {}, boss_damage)]

    for state in states:
        state = state.change(player_health=state.player_health - 1)
        if not state:
            continue
        state.buff()

        casts = (state.cast(*stats) for stats in [(53, -4, 0), (73, -2, +2)])
        effects = (state.add_effect(name) for name in
                   ['shield', 'poison', 'recharge'])
        new_states = (*casts, *effects)
        new_states = (state for state in new_states if state and state.used_mana < cheapest_victory)

        for new_state in new_states:
            new_state.buff()
            new_state.boss_attack()
            if new_state.boss_health <= 0:
                cheapest_victory = min(cheapest_victory, new_state.used_mana)
                continue
            if new_state.player_health > 0:
                states.append(new_state)

    return cheapest_victory
