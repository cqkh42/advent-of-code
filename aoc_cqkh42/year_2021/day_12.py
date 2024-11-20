from collections import Counter, defaultdict
from dataclasses import dataclass
from queue import SimpleQueue
from typing import Tuple

from aoc_cqkh42.helpers.base_solution import BaseSolution


# todo could we feed in some parsing function
# todo some graph here
@dataclass(frozen=True)
class Route:
    route: Tuple[str, ...]

    @property
    def complete(self):
        return self.route[-1] == 'end'

    @property
    def current(self):
        return self.route[-1]

    def move(self, new: str):
        return Route((*self.route, new))

    def valid_part_a(self):
        lower = [step for step in self.route if step.islower()]
        return len(lower) == len(set(lower))

    def valid_part_b(self):
        lower = [step for step in self.route if step.islower()]
        c = Counter(lower)
        # start and end are at most 1
        return (c['start'] < 2) and (c.get('end', 1) < 2) and (list(c.values()).count(2) < 2) and max(c.values()) <= 2


class Solution(BaseSolution):
    def _parse(self):
        self.maps = defaultdict(list)
        for row in self.lines:
            a, b = row.split('-')
            self.maps[a].append(b)
            self.maps[b].append(a)
        return [Route(('start', i)) for i in self.maps['start']]

    def part_a(self):
        successful = set()
        queue = SimpleQueue()
        for start in self.parsed:
            queue.put(start)
        while not queue.empty():
            route = queue.get()
            for step in self.maps[route.current]:
                    new_route = route.move(step)
                    if new_route.complete:
                        successful.add(route)
                    elif new_route.valid_part_a():
                        queue.put(new_route)
        return len(successful)

    def part_b(self):
        successful = set()
        queue = SimpleQueue()
        for start in self.parsed:
            queue.put(start)
        while not queue.empty():
            route = queue.get()
            for step in self.maps[route.current]:
                new_route = route.move(step)
                if new_route.complete:
                    successful.add(new_route)
                elif new_route.valid_part_b():
                    queue.put(new_route)
        return len(successful)
