from copy import deepcopy

import more_itertools
import parse

from aoc_cqkh42.helpers.base_solution import BaseSolution


class Solution(BaseSolution):
    parser = parse.compile('move {:d} from {:d} to {:d}')

    @property
    def instructions(self):
        for count, from_, to in self.parser.findall(self.input_):
            yield count, from_ - 1, to - 1

    def _parse(self):
        lines, _ = more_itertools.split_at(self.lines, lambda line: line == '')
        stacks = (stack for stack in zip(*lines) if stack[-1] != ' ')
        queues = [
            [box for box in stack if box != ' '][::-1]
            for stack in stacks
        ]
        return queues

    def move_boxes(self, lifo=True):
        queues = deepcopy(self.parsed)
        for count, from_, to in self.instructions:
            if lifo:
                queues[to].extend(reversed(queues[from_][-count:]))
            else:
                queues[to].extend(queues[from_][-count:])
            del queues[from_][-count:]
        return ''.join(i[-1] for i in queues)

    def part_a(self):
        return self.move_boxes()

    def part_b(self):
        return self.move_boxes(False)
