import string
from typing import Self, Any

import more_itertools
import parse
from collections import defaultdict
from aoc_cqkh42 import submit_answers
from aoc_cqkh42.helpers.base_solution import BaseSolution

text = """If the current value is {:d}:
    - Write the value {:d}.
    - Move one slot to the {:w}.
    - Continue with state {:w}."""
class Solution(BaseSolution):
    tape = defaultdict(int)
    iters = 0
    state = None
    cursor = 0

    def _parse(self: Self) -> Any:
        states = {}
        p = parse.compile(text)
        matches = p.findall(self.input_)
        pairs = more_itertools.chunked(matches, 2)
        for state, (val_0, val_1) in zip(string.ascii_uppercase, pairs):
            s_map = {
                0: {
                    'set': val_0[1],
                    'step': -1 if val_0[2] == 'left' else 1,
                    'state': val_0[3]
                },
                1: {
                    'set': val_1[1],
                    'step': -1 if val_1[2] == 'left' else 1,
                    'state': val_1[3]
                }
            }
            states[state] = s_map

        a = parse.search('Begin in state {:w}.', self.input_)
        self.state = a[0]

        b = parse.search('Perform a diagnostic checksum after {:d} steps.', self.input_)
        self.iters = b[0]

        return states

    def part_a(self):
        for _ in range(self.iters):
            val = self.tape[self.cursor]
            action = self.parsed[self.state][val]
            self.tape[self.cursor] = action['set']
            self.cursor += action['step']
            self.state = action['state']
        return sum(self.tape.values())



if __name__ == "__main__":
    submit_answers(Solution,25, 2017)
