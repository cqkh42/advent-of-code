from collections import defaultdict
from dataclasses import dataclass
from queue import SimpleQueue

from aoc_cqkh42 import BaseSolution


@dataclass(frozen=True)
class Route:
    route: tuple

    @property
    def at_end(self):
        return self.route[-1] == 'end'

    def __getitem__(self, item):
        return self.route[item]


class Solution(BaseSolution):

    def parse_data(self):
        self.maps = defaultdict(list)
        for row in self.lines:
            a, b = row.split('-')
            self.maps[a].append(b)
            self.maps[b].append(a)

        return [Route(('start', i)) for i in self.maps['start']]

    def part_a(self):
        successful = set()
        queue = SimpleQueue()
        for start in self.parsed_data:
            queue.put(start)
        while not queue.empty():
            route = queue.get()
            if route.at_end:
                successful.add(route)
                continue
            new = self.maps[route[-1]]
            for n in new:
                if n.isupper() or n not in route:
                    queue.put(Route((*route, n)))
        return len(successful)

    def part_b(self):
        successful = set()
        queue = SimpleQueue()
        for start in self.parsed_data:
            queue.put(start)

        while not queue.empty():
            route = queue.get()
            if route[-1] == 'end':
                successful.add(route)
                continue
            new = self.maps[route[-1]]
            for n in new:
                if n.isupper():
                    queue.put((*route, n))
                # this one is only in once and nothing else is in twice
                # elif
                # # either it is upper, or it is lower an
                # if n.isupper() or n not in route:
                #     queue.put((*route, n))
        return len(successful)
