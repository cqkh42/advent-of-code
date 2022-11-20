from collections import defaultdict
from dataclasses import dataclass, field, replace
from queue import SimpleQueue

from aoc_cqkh42 import BaseSolution

#todo some graph here
@dataclass
class Route:
    def __init__(self, current):
        self.current = current
        self.visited = defaultdict(int, {current: 1, 'start': 1})

    def move(self, new: str):
        new_route = Route(new)
        new_route.visited = self.visited.copy()
        new_route.visited[new] += 1
        return new_route

    @property
    def double_dipped(self):
        v = max([v for k, v in self.visited.items() if k.islower() and k not in ['start', 'end']], default = 0)
        return v == 2

    @property
    def max_lower(self):
        return max((v for k, v in self.visited.items() if k.islower() and k not in ['start', 'end']), default=0)


class Solution(BaseSolution):
    def parse_data(self):
        self.maps = defaultdict(list)
        for row in self.lines:
            a, b = row.split('-')
            self.maps[a].append(b)
            self.maps[b].append(a)
        return [Route(i) for i in self.maps['start']]

    def part_a(self):
        successful = 0
        queue = SimpleQueue()
        for start in self.parsed_data:
            queue.put(start)
        while not queue.empty():
            route = queue.get()
            if 'end' in route.visited:
                successful += 1
                continue
            for step in self.maps[route.current]:
                if step.isupper() or step not in route.visited:
                    new_route = route.move(step)
                    queue.put(new_route)
        return successful

    def part_b(self):
        successful = 0
        queue = SimpleQueue()
        for start in self.parsed_data:
            queue.put(start)
        while not queue.empty():
            route = queue.get()
            for step in self.maps[route.current]:
                new_route = route.move(step)
                if step == 'start':
                    continue
                elif step == 'end':
                    successful += 1
                    continue
                elif new_route.double_dipped and step in route.visited and step.islower():
                    continue
                # print(route.current, step)

                # either is upper, havent visited it before, or havenet double dipped
                queue.put(new_route)

                # elif  new_route.double_dipped:
                #     print('we cannot go back here', new_route.visited)
        return successful
