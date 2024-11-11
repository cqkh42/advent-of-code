import itertools
from collections import defaultdict
from dataclasses import dataclass, field

import parse

from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution


@dataclass
class Bot:
    holding: set = field(default_factory=lambda: set())

    def add(self, value):
        self.holding.add(value)

    @property
    def low(self):
        return min(self.holding)

    @property
    def high(self):
        return max(self.holding)


class Solution(BaseSolution):
    bots = defaultdict(Bot)
    instructions = {}
    outputs = {}

    def _process_data(self):
        v = parse.findall("value {:d} goes to bot {:d}", self.input_)
        for v_, b in v:
            self.bots[b].add(v_)

        z = parse.findall(
            "bot {bot:d} gives low to {low[bot]:w} {low[value]:d} and high to {high[bot]:w} {high[value]:d}",
            self.input_,
        )
        self.instructions = {i["bot"]: i.named for i in z}

    def part_a(self):
        for bot, instruction in itertools.cycle(self.instructions.items()):
            holding = self.bots[bot]
            if holding == Bot({17, 61}):
                return bot
            self.update(bot, instruction)

    def part_b(self):
        for bot, instruction in itertools.cycle(self.instructions.items()):
            if {0, 1, 2}.issubset(self.outputs):
                return self.outputs[0] * self.outputs[1] * self.outputs[2]
            self.update(bot, instruction)

    def update(self, bot_id, instruction):
        holding = self.bots[bot_id]
        if len(holding.holding) < 2:
            return
        for end in ["low", "high"]:
            who = instruction[end]["value"]
            if instruction[end]["bot"] == "bot":
                self.bots[who].add(getattr(holding, end))
            else:
                self.outputs[who] = getattr(holding, end)


if __name__ == "__main__":
    submit_answers(Solution, 10, 2016)
