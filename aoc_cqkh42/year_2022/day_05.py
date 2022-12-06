from collections import defaultdict
from copy import deepcopy

from aoc_cqkh42 import BaseSolution

import more_itertools
import parse


class Solution(BaseSolution):
    parser = parse.compile('move {:d} from {:d} to {:d}')

    def parse_data(self):
        a, _ = self.data.split('\n\n')
        queues = [[x for x in reversed(i) if x != ' '] for i in zip(*a.split('\n')) if i[-1] != ' ']
        queues = [[], *queues]
        return queues

    def part_a(self):
        queues = deepcopy(self.parsed_data)
        for count, from_, to in self.parser.findall(self.data):
            p = queues[from_][-count:]
            queues[to].extend(reversed(p))
            del queues[from_][-count:]
        return ''.join(i[-1] for i in queues[1:])

    def part_b(self):
        queues = deepcopy(self.parsed_data)
        for count, from_, to in self.parser.findall(self.data):
            queues[to].extend(queues[from_][-count:])
            del queues[from_][-count:]
        return ''.join(i[-1] for i in queues[1:])
