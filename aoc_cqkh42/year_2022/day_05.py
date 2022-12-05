from collections import defaultdict
from copy import deepcopy

from aoc_cqkh42 import BaseSolution

import more_itertools
import parse


class Solution(BaseSolution):
    parser = parse.compile('move {:d} from {:d} to {:d}')

    def parse_data(self):
        #TODO if we knew the number of queues we could skip this bit
        queues = defaultdict(list)
        stacks = [line for line in self.lines if '[' in line]
        rows = [list(more_itertools.chunked(line, 4)) for line in stacks]
        for row in rows[-1::-1]:
            for index, column in enumerate(row, start=1):
                if column[1] != ' ':
                    queues[index].append(column[1])
        return queues

    def part_a(self):
        queues = deepcopy(self.parsed_data)
        for count, from_, to in self.parser.findall(self.data):
            p = queues[from_][-count:]
            queues[to].extend(reversed(p))
            del queues[from_][-count:]
        return ''.join(queues[i].pop(-1) for i in range(1, len(queues)+1))

    def part_b(self):
        queues = deepcopy(self.parsed_data)
        for count, from_, to in self.parser.findall(self.data):
            queues[to].extend(queues[from_][-count:])
            del queues[from_][-count:]
        return ''.join(queues[i].pop(-1) for i in range(1, len(queues) + 1))
